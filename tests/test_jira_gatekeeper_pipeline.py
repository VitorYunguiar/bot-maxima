import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import jira_gatekeeper_pipeline as pipeline


def _comment(comment_id: str, body, author: str = "Filipe do Amaral Padilha", created: str = "2026-04-14T10:00:00.000-0300"):
    return {
        "id": comment_id,
        "author": {"displayName": author, "emailAddress": "filipe.padilha@maxima.com.br"},
        "created": created,
        "updated": created,
        "body": body,
    }


def _attachment(filename: str) -> dict:
    return {
        "id": filename,
        "filename": filename,
        "mimeType": "application/octet-stream",
        "size": 10,
        "created": "2026-04-14T10:00:00.000-0300",
        "author": {"displayName": "Filipe do Amaral Padilha"},
        "content": f"https://jira.local/{filename}",
    }


def _make_issue(
    key: str,
    *,
    summary: str,
    passos="Passo 1",
    apresentado="Resultado atual",
    esperado="Resultado esperado",
    descricao="Descricao do problema",
    comments=None,
    attachments=None,
    assunto="Assunto teste",
    erp="PROTON",
    natureza="Dúvida",
    assignee="Filipe do Amaral Padilha",
):
    return {
        "key": key,
        "fields": {
            "summary": summary,
            "description": descricao,
            "status": {"name": "Resolvido"},
            "created": "2026-04-14T09:00:00.000-0300",
            "updated": "2026-04-14T10:00:00.000-0300",
            "assignee": {"displayName": assignee, "emailAddress": "filipe.padilha@maxima.com.br"},
            "reporter": {"displayName": "Analista N1"},
            "attachment": attachments or [],
            "comment": {"comments": comments or [], "total": len(comments or [])},
            "customfield_10221": passos,
            "customfield_10222": apresentado,
            "customfield_10223": esperado,
            "customfield_10320": assunto,
            "customfield_10232": erp,
            "customfield_10407": natureza,
        },
    }


class FakeJiraClient:
    def __init__(self, fields_payload, issues):
        self.fields_payload = fields_payload
        self.issues = issues

    def fetch_fields(self):
        return copy.deepcopy(self.fields_payload)

    def search_issues(self, jql, *, limit=None, page_size=100):
        keys = list(self.issues.keys())
        if limit is not None:
            keys = keys[:limit]
        return [{"key": key, "fields": {"summary": self.issues[key]["fields"]["summary"]}} for key in keys]

    def fetch_issue_detail(self, issue_key, field_ids):
        return copy.deepcopy(self.issues[issue_key])


class FakeLlm:
    def __init__(self, *, approved=True):
        self.model = "fake-gold-model"
        self.approved = approved
        self.supporting_texts = []

    def extract_facts(self, *, problem_context, comment_text):
        self.supporting_texts.append(comment_text)
        return {
            "causa": "Divergencia no dado enviado pelo ERP",
            "evidencias": ["Valor no ERP difere do valor enviado via API"],
            "acao_recomendada": ["Orientar o ERP a revisar a apuracao"],
            "parametros": [],
            "sql": ["SELECT 1 FROM DUAL"],
            "responsavel": "ERP do cliente",
            "limitacoes": [],
            "proximo_passo": "Comparar o banco interno do ERP com o payload enviado para a Maxima.",
        }

    def canonicalize_answer(self, *, problem_context, facts):
        return (
            "Foi validado que a divergencia esta na apuracao do ERP. "
            "A orientacao e comparar o banco interno do ERP com os dados enviados via API.\n\n"
            "```sql\nSELECT 1 FROM DUAL\n```"
        )

    def verify_groundedness(self, *, answer, supporting_text):
        return {
            "approved": self.approved,
            "unsupported_claims": [] if self.approved else ["Frase nao suportada."],
            "notes": "",
        }


class TestGatekeeperPipelineUnits(unittest.TestCase):
    def test_require_jira_credentials_accepts_url_username_and_password_aliases(self):
        with patch.dict(
            "os.environ",
            {
                "JIRA_URL": "https://suporte.maximatech.com.br",
                "JIRA_API_TOKEN": "",
                "JIRA_PASSWORD": "",
                "USERNAME": "vitor.adriao",
                "PASSWORD": "segredo",
            },
            clear=False,
        ), patch.multiple(
            pipeline.config,
            JIRA_BASE_URL="",
            JIRA_URL="",
            JIRA_USERNAME="",
            JIRA_PASSWORD="",
            JIRA_API_TOKEN="",
            JIRA_SESSION_COOKIE="",
            JIRA_REQUEST_TIMEOUT_SECONDS=60.0,
        ):
            credentials = pipeline._require_jira_credentials()

        self.assertEqual(credentials.base_url, "https://suporte.maximatech.com.br")
        self.assertEqual(credentials.username, "vitor.adriao")
        self.assertEqual(credentials.password, "segredo")

    def test_discover_field_ids_uses_discovered_ids_and_fallbacks(self):
        fields_payload = [
            {"id": "customfield_90001", "name": "Passos para reproduzir"},
            {"id": "description", "name": "Description"},
        ]

        field_ids = pipeline.discover_field_ids(fields_payload)

        self.assertEqual(field_ids["passos_reproduzir"], "customfield_90001")
        self.assertEqual(field_ids["descricao"], "description")
        self.assertEqual(field_ids["resultado_apresentado"], "customfield_10222")

    def test_jira_value_to_text_handles_adf_and_html(self):
        adf = {
            "type": "doc",
            "content": [
                {"type": "paragraph", "content": [{"type": "text", "text": "Linha A"}]},
                {
                    "type": "bulletList",
                    "content": [
                        {"type": "listItem", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Item 1"}]}]},
                    ],
                },
                {
                    "type": "codeBlock",
                    "content": [{"type": "text", "text": "SELECT * FROM dual"}],
                },
            ],
        }

        html = "<p>Primeira linha</p><ul><li>Segundo item</li></ul>"

        self.assertIn("Linha A", pipeline.jira_value_to_text(adf))
        self.assertIn("- Item 1", pipeline.jira_value_to_text(adf))
        self.assertIn("SELECT * FROM dual", pipeline.jira_value_to_text(adf))
        self.assertIn("Primeira linha", pipeline.jira_value_to_text(html))
        self.assertIn("- Segundo item", pipeline.jira_value_to_text(html))
        self.assertEqual(pipeline.jira_value_to_text({"value": "Winthor", "id": "1"}), "Winthor")

    def test_build_problem_context_preserves_fixed_order(self):
        sections = pipeline.OrderedDict(
            [
                ("Passos para reproduzir", "Passo 1"),
                ("Resultado apresentado", "Apresentado"),
                ("Resultado esperado", "Esperado"),
                ("Descrição", "Descricao"),
            ]
        )

        text = pipeline.build_problem_context(sections)

        self.assertLess(text.index("## Passos para reproduzir"), text.index("## Resultado apresentado"))
        self.assertLess(text.index("## Resultado apresentado"), text.index("## Resultado esperado"))
        self.assertLess(text.index("## Resultado esperado"), text.index("## Descrição"))

    def test_substantive_comment_and_attachment_flag(self):
        strong = "Validado que o ERP envia valor divergente. Necessario comparar a API e revisar o parametro."
        weak = "Segue anexo."

        self.assertTrue(pipeline.is_substantive_comment(strong))
        self.assertFalse(pipeline.is_substantive_comment(weak))
        self.assertTrue(
            pipeline._attachment_dependency(
                "## Descrição\nVer anexo",
                [{"clean_body": "Segue anexo.", "is_substantive": False}],
                [_attachment("evidencia.xlsx")],
            )
        )


class TestGatekeeperPipelineIntegration(unittest.TestCase):
    def setUp(self):
        self.fields_payload = [
            {"id": "customfield_10221", "name": "Passos para reproduzir"},
            {"id": "customfield_10222", "name": "Resultado apresentado"},
            {"id": "customfield_10223", "name": "Resultado esperado"},
            {"id": "customfield_10320", "name": "Assunto"},
            {"id": "customfield_10232", "name": "Qual ERP do cliente?"},
            {"id": "customfield_10407", "name": "Natureza"},
            {"id": "description", "name": "Description"},
        ]

    def test_pipeline_generates_raw_normalized_gold_and_review_outputs(self):
        issues = {
            "GATE-1": _make_issue(
                "GATE-1",
                summary="Comentario forte",
                comments=[
                    _comment(
                        "1",
                        "Bom dia\nFoi validado que o ERP esta apurando valor maior que o enviado via API. "
                        "Necessario comparar os dados internos do ERP com o payload enviado para a Maxima.",
                    )
                ],
            ),
            "GATE-2": _make_issue(
                "GATE-2",
                summary="Multiplos comentarios",
                comments=[
                    _comment(
                        "2a",
                        "Validado que o RCA possui permissao, mas faltava parametro na filial. "
                        "Necessario revisar a parametrizacao antes do reprocessamento.",
                    ),
                    _comment("2b", "Orientar o cliente a ajustar o parametro na rotina correta e reprocessar a carga."),
                ],
            ),
            "GATE-3": _make_issue(
                "GATE-3",
                summary="Sem resposta substantiva",
                comments=[_comment("3a", "Ok.")],
            ),
            "GATE-4": _make_issue(
                "GATE-4",
                summary="Dependente de anexo",
                comments=[_comment("4a", "Nos anexos esta a planilha para validar. Segue anexo.")],
                attachments=[_attachment("planilha.xlsx")],
            ),
            "GATE-5": _make_issue(
                "GATE-5",
                summary="Comentario com SQL",
                comments=[
                    _comment(
                        "5a",
                        "-- Valor sem deduzir\nSELECT SUM(PVENDA) FROM MXSHISTORICOPEDC WHERE TRUNC(DATA) = TO_DATE('01/02/2025','dd/mm/yyyy');",
                    )
                ],
                attachments=[_attachment("query.txt")],
            ),
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            client = FakeJiraClient(self.fields_payload, issues)
            llm = FakeLlm(approved=True)
            runner = pipeline.GatekeeperDatasetPipeline(
                jira_client=client,
                output_dir=Path(tmpdir),
                review_threshold=0.80,
                llm_processor=llm,
                no_llm=False,
                assignee_aliases=["Felipe do Amaral Padilha"],
            )

            manifest = runner.run()

            normalized_path = Path(tmpdir) / "normalized" / "issues.jsonl"
            gold_path = Path(tmpdir) / "gold" / "pairs.jsonl"
            review_path = Path(tmpdir) / "review" / "review.csv"
            raw_manifest = Path(tmpdir) / "raw" / "manifest.json"

            self.assertTrue(normalized_path.exists())
            self.assertTrue(gold_path.exists())
            self.assertTrue(review_path.exists())
            self.assertTrue(raw_manifest.exists())
            self.assertEqual(manifest["normalized_issues"], 5)

            normalized_rows = [json.loads(line) for line in normalized_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            gold_rows = [json.loads(line) for line in gold_path.read_text(encoding="utf-8").splitlines() if line.strip()]

            by_key = {row["issue_key"]: row for row in normalized_rows}
            self.assertEqual(by_key["GATE-2"]["primary_comment_ids"], ["2a", "2b"])
            self.assertIn("needs_review", by_key["GATE-3"]["quality_flags"])
            self.assertIn("requires_attachment_review", by_key["GATE-4"]["quality_flags"])
            self.assertNotIn("requires_attachment_review", by_key["GATE-5"]["quality_flags"])
            self.assertEqual(len(gold_rows), 3)
            self.assertTrue(
                any("faltava parametro na filial" in text and "ajustar o parametro" in text for text in llm.supporting_texts)
            )

    def test_pipeline_keeps_ticket_out_of_gold_when_grounding_fails(self):
        issues = {
            "GATE-10": _make_issue(
                "GATE-10",
                summary="Grounding falho",
                comments=[
                    _comment(
                        "10a",
                        "Validado no ambiente que faltava o parametro da filial. "
                        "Necessario ajustar a parametrizacao correta e reprocessar a carga.",
                    )
                ],
            )
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            client = FakeJiraClient(self.fields_payload, issues)
            llm = FakeLlm(approved=False)
            runner = pipeline.GatekeeperDatasetPipeline(
                jira_client=client,
                output_dir=Path(tmpdir),
                review_threshold=0.75,
                llm_processor=llm,
                no_llm=False,
            )

            runner.run()

            normalized_rows = [
                json.loads(line)
                for line in (Path(tmpdir) / "normalized" / "issues.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            gold_rows = [
                json.loads(line)
                for line in (Path(tmpdir) / "gold" / "pairs.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]

            self.assertEqual(len(gold_rows), 0)
            self.assertIn("grounding_failed", normalized_rows[0]["quality_flags"])


if __name__ == "__main__":
    unittest.main()
