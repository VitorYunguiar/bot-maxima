"""
Runs offline end-to-end evaluation against the current RAG pipeline and stores results in Supabase.
"""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
import sys
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import config
import rag


def _load_dataset(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, list):
        raise ValueError("Dataset must be a JSON array")
    cases = [item for item in payload if isinstance(item, dict) and str(item.get("question") or "").strip()]
    if not cases:
        raise ValueError("Dataset has no valid cases")
    return cases


def _is_abstained(answer: str, trace: dict[str, Any]) -> bool:
    if bool(trace.get("abstained")):
        return True
    return str(answer or "").strip().startswith(config.NO_ANSWER_PHRASE)


def _behavior_match(expected_behavior: str, abstained: bool, answer: str) -> bool:
    expected = (expected_behavior or "exact_answer").strip().lower()
    if expected == "exact_answer":
        return not abstained
    if expected == "no_answer":
        return abstained
    if expected == "partial_abstain":
        # Accept either a strict abstain or a partial response that includes no-answer phrase.
        return abstained or (config.NO_ANSWER_PHRASE in (answer or ""))
    return not abstained


def _citation_ok(abstained: bool, trace: dict[str, Any]) -> bool:
    if abstained:
        return True
    grounding_errors = trace.get("grounding_errors") or []
    cited = trace.get("cited_files") or []
    return (len(grounding_errors) == 0) and (len(cited) > 0)


def _grounded(abstained: bool, trace: dict[str, Any]) -> bool:
    grounding_errors = trace.get("grounding_errors") or []
    if abstained:
        return len(grounding_errors) == 0 or trace.get("abstention_reason") in {
            "no_chunks",
            "few_chunks",
            "low_similarity",
            "low_similarity_operational",
            "no_context_after_merge",
            "grounding_validation_failed",
        }
    return len(grounding_errors) == 0


def _score_case(
    *,
    behavior_match: bool,
    intent_match: bool,
    citation_ok: bool,
    grounded: bool,
) -> float:
    score = 0.0
    score += 0.45 if behavior_match else 0.0
    score += 0.20 if intent_match else 0.0
    score += 0.20 if citation_ok else 0.0
    score += 0.15 if grounded else 0.0
    return round(score, 4)


def _insert_run(*, dataset_name: str, total_cases: int, metadata: dict[str, Any]) -> str:
    model_info = rag.get_model_config()
    row = rag.supabase_insert(
        "evaluation_runs",
        {
            "run_type": "offline",
            "dataset_name": dataset_name,
            "model": model_info.get("generation_model"),
            "embedding_model": model_info.get("embedding_model"),
            "total_cases": total_cases,
            "created_by": "offline_eval_script",
            "metadata": {
                **metadata,
                "llm_provider": model_info.get("llm_provider"),
                "embedding_provider": model_info.get("embedding_provider"),
            },
        },
    )
    if not row:
        raise RuntimeError("Failed to create evaluation run")
    return str(row[0]["id"])


def run_evaluation(
    *,
    dataset: list[dict[str, Any]],
    dataset_name: str,
    dry_run: bool,
    limit: int | None,
) -> dict[str, Any]:
    selected = dataset[:limit] if limit and limit > 0 else dataset

    started_at = datetime.now(timezone.utc).isoformat()
    run_id = "DRY_RUN"
    if not dry_run:
        run_id = _insert_run(
            dataset_name=dataset_name,
            total_cases=len(selected),
            metadata={"started_at": started_at},
        )

    rows_to_store: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []

    for index, case in enumerate(selected, start=1):
        case_id = str(case.get("id") or f"case-{index:04d}")
        question = str(case.get("question") or "").strip()
        expected_behavior = str(case.get("expected_behavior") or "exact_answer").strip().lower()
        expected_intent = str(case.get("expected_intent") or "general").strip().lower()
        scope = case.get("scope") if isinstance(case.get("scope"), dict) else {"level": "global"}

        t0 = time.perf_counter()
        answer, _chunks, trace = rag.ask(
            question,
            conversation_history=None,
            images=None,
            system_prompt=None,
            platform="offline_eval",
            scope=scope,
        )
        latency_ms = int((time.perf_counter() - t0) * 1000)

        predicted_intent = str((trace.get("query_plan") or {}).get("intent") or "general").strip().lower()
        abstained = _is_abstained(answer, trace)
        behavior_match = _behavior_match(expected_behavior, abstained, answer)
        citation_ok = _citation_ok(abstained, trace)
        grounded = _grounded(abstained, trace)
        intent_match = expected_intent == predicted_intent
        score = _score_case(
            behavior_match=behavior_match,
            intent_match=intent_match,
            citation_ok=citation_ok,
            grounded=grounded,
        )

        result = {
            "run_id": run_id,
            "case_id": case_id,
            "question": question,
            "expected_behavior": expected_behavior,
            "expected_intent": expected_intent,
            "predicted_intent": predicted_intent,
            "abstained": abstained,
            "citation_ok": citation_ok,
            "grounded": grounded,
            "top_similarity": rag._safe_similarity(trace.get("top_similarity", 0.0)),
            "latency_ms": latency_ms,
            "score": score,
            "trace": trace,
            "answer_preview": (answer or "")[:240],
        }
        results.append(result)

        rows_to_store.append(
            {
                "run_id": run_id,
                "case_id": case_id,
                "question": question,
                "expected_behavior": expected_behavior,
                "expected_intent": expected_intent,
                "predicted_intent": predicted_intent,
                "abstained": abstained,
                "citation_ok": citation_ok,
                "grounded": grounded,
                "top_similarity": result["top_similarity"],
                "latency_ms": latency_ms,
                "score": score,
                "trace": trace,
            }
        )

    if not dry_run and rows_to_store:
        rag.supabase_insert("evaluation_results", rows_to_store)

    total = len(results)
    grounded_rate = (sum(1 for r in results if r["grounded"]) / total) if total else 0.0
    citation_rate = (sum(1 for r in results if r["citation_ok"]) / total) if total else 0.0
    abstain_rate = (sum(1 for r in results if r["abstained"]) / total) if total else 0.0
    intent_accuracy = (
        sum(1 for r in results if r["expected_intent"] == r["predicted_intent"]) / total
    ) if total else 0.0
    avg_score = (sum(float(r["score"]) for r in results) / total) if total else 0.0

    return {
        "run_id": run_id,
        "dataset_name": dataset_name,
        "total_cases": total,
        "avg_score": round(avg_score, 4),
        "grounded_rate": round(grounded_rate, 4),
        "citation_ok_rate": round(citation_rate, 4),
        "abstain_rate": round(abstain_rate, 4),
        "intent_accuracy": round(intent_accuracy, 4),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run offline RAG benchmark and store metrics in Supabase")
    parser.add_argument(
        "--dataset",
        default="evaluation/datasets/maxpedido_eval_dataset.json",
        help="Path to benchmark dataset (JSON array)",
    )
    parser.add_argument(
        "--dataset-name",
        default="maxpedido_offline_eval",
        help="Logical dataset name stored in evaluation_runs",
    )
    parser.add_argument("--limit", type=int, default=0, help="Optional max number of cases")
    parser.add_argument("--dry-run", action="store_true", help="Run without writing to Supabase")
    parser.add_argument(
        "--output-report",
        default="",
        help="Optional output JSON report path",
    )
    args = parser.parse_args()

    dataset_path = Path(args.dataset)
    dataset = _load_dataset(dataset_path)

    summary = run_evaluation(
        dataset=dataset,
        dataset_name=args.dataset_name,
        dry_run=args.dry_run,
        limit=args.limit,
    )

    report_path = Path(args.output_report) if args.output_report else None
    if report_path is None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        report_path = Path(f"evaluation/reports/{stamp}_{args.dataset_name}.json")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Run ID: {summary['run_id']}")
    print(f"Dataset: {summary['dataset_name']}")
    print(f"Total cases: {summary['total_cases']}")
    print(f"Average score: {summary['avg_score']:.4f}")
    print(f"Groundedness: {summary['grounded_rate']:.2%}")
    print(f"Citation correctness: {summary['citation_ok_rate']:.2%}")
    print(f"Abstention rate: {summary['abstain_rate']:.2%}")
    print(f"Intent accuracy: {summary['intent_accuracy']:.2%}")
    print(f"Report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
