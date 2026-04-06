# Offline Evaluation (maxPedido)

This folder contains the baseline benchmark workflow for maxPedido quality.

## Files

- `evaluation/datasets/maxpedido_seed_cases.json`: curated seed scenarios.
- `evaluation/build_dataset.py`: builds merged benchmark dataset.
- `evaluation/run_offline_eval.py`: runs end-to-end RAG evaluation and stores metrics.

## 1) Build dataset

```powershell
python evaluation/build_dataset.py --knowledge-gap-limit 20
```

Optional ticket cases file:

```powershell
python evaluation/build_dataset.py --tickets-file evaluation/datasets/tickets_cases.json
```

Default output:

- `evaluation/datasets/maxpedido_eval_dataset.json`

## 2) Run benchmark

Dry-run (no DB writes):

```powershell
python evaluation/run_offline_eval.py --dry-run
```

Store in Supabase (`evaluation_runs` + `evaluation_results`):

```powershell
python evaluation/run_offline_eval.py
```

Optional limit and custom report:

```powershell
python evaluation/run_offline_eval.py --limit 50 --output-report evaluation/reports/latest.json
```

## KPIs tracked

- `grounded_rate`
- `citation_ok_rate`
- `abstain_rate`
- `intent_accuracy`
- `avg_score`

Use these metrics as regression gates before rollout.
