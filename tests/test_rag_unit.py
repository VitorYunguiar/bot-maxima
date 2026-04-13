import unittest
from unittest.mock import patch

import config
import db
import rag


class TestIntentRouting(unittest.TestCase):
    def test_sql_lookup_intent_for_maxpedido_tables(self):
        query = "Preciso de select na tabela mxsintegracaopedido para analisar erro"
        plan = rag._classify_query_intent(query)

        self.assertEqual(plan["intent"], "sql_lookup")
        self.assertIn("sql_integracao", plan["modules"])

    def test_configuration_intent_for_usagrade(self):
        query = "Como configurar o parametro USAGRADE na rotina ParamFilial"
        plan = rag._classify_query_intent(query)

        self.assertEqual(plan["intent"], "configuration")
        self.assertIn("parametros_configuracao", plan["modules"])


class TestStrictAbstain(unittest.TestCase):
    def test_abstains_when_similarity_is_weak(self):
        chunks = [{"similarity": 0.42, "filename": "doc.md"}]
        with patch.multiple(
            config,
            RAG_STRICT_ABSTAIN=True,
            RAG_MIN_RETRIEVED_CHUNKS=1,
            RAG_MIN_STRONG_SIMILARITY=0.62,
            RAG_OPERATIONAL_SIMILARITY_MARGIN=0.05,
        ):
            abstain, reason = rag._should_strict_abstain("Como configurar parametro?", chunks)

        self.assertTrue(abstain)
        self.assertEqual(reason, "low_similarity")

    def test_abstains_when_too_few_chunks(self):
        chunks = [{"similarity": 0.90, "filename": "doc.md"}]
        with patch.multiple(
            config,
            RAG_STRICT_ABSTAIN=True,
            RAG_MIN_RETRIEVED_CHUNKS=2,
            RAG_MIN_STRONG_SIMILARITY=0.62,
            RAG_OPERATIONAL_SIMILARITY_MARGIN=0.05,
        ):
            abstain, reason = rag._should_strict_abstain("Fluxo de pedido", chunks)

        self.assertTrue(abstain)
        self.assertEqual(reason, "few_chunks")


class TestCitationValidation(unittest.TestCase):
    def test_accepts_grounded_answer_with_inline_citations(self):
        answer = (
            "Use o parametro USAGRADE para habilitar grade [fonte: guia-maxpedido.md].\n\n"
            "Fontes:\n"
            "- guia-maxpedido.md"
        )

        valid, errors, cited = rag._validate_grounded_answer(
            answer=answer,
            allowed_sources={"guia-maxpedido.md"},
            question="Como configurar USAGRADE?",
            require_sources_section=True,
        )

        self.assertTrue(valid)
        self.assertEqual(errors, [])
        self.assertIn("guia-maxpedido.md", cited)

    def test_accepts_sources_section_without_inline_citation(self):
        answer = (
            "A tabela principal e mxsintegracaopedido.\n\n"
            "Fontes:\n"
            "- guia-maxpedido.md"
        )

        valid, errors, _ = rag._validate_grounded_answer(
            answer=answer,
            allowed_sources={"guia-maxpedido.md"},
            question="Qual tabela de integracao?",
            require_sources_section=True,
        )

        self.assertTrue(valid)
        self.assertEqual(errors, [])


class TestCitationFormatting(unittest.TestCase):
    def test_moves_inline_citations_to_sources_section(self):
        answer = (
            "Conta corrente usa parametro X [fonte: guia-maxpedido.md].\n"
            "Outro ponto [fonte: parametros.md]."
        )
        formatted, cited = rag._enforce_sources_section_only(
            answer,
            allowed_sources={"guia-maxpedido.md", "parametros.md"},
            source_display_map={
                "guia-maxpedido.md": "GUIA-MAXPEDIDO.md",
                "parametros.md": "PARAMETROS.md",
            },
        )

        self.assertNotIn("[fonte:", formatted.lower())
        self.assertIn("Fontes:", formatted)
        self.assertIn("- GUIA-MAXPEDIDO.md", formatted)
        self.assertIn("- PARAMETROS.md", formatted)
        self.assertEqual(cited, {"guia-maxpedido.md", "parametros.md"})


class TestAnalyticalContextFormatting(unittest.TestCase):
    def test_build_context_includes_analytical_block_before_evidence(self):
        chunks = [
            {
                "id": "chunk-1",
                "document_id": "doc-1",
                "filename": "pedidos.md",
                "content": "Validar MXSINTEGRACAOPEDIDO quando o pedido nao aparece no ERP.",
                "chunk_index": 0,
                "similarity": 0.91,
                "heading_path": "Pedidos > Pedido nao aparece no ERP",
                "semantic_context": "Secao: Pedidos > Pedido nao aparece no ERP | Tabelas: MXSINTEGRACAOPEDIDO",
                "answer_mode": "troubleshooting",
                "entities": {
                    "tables": ["MXSINTEGRACAOPEDIDO"],
                    "parameters": [],
                    "endpoints": [],
                    "statuses": [],
                    "error_terms": ["pedido nao aparece no ERP"],
                },
                "metadata": {"doc_priority": 5, "source_kind": "kb"},
            }
        ]

        context = rag.build_context(chunks)

        self.assertIn("<analytical_context>", context)
        self.assertIn("Assunto/secoes: Pedidos > Pedido nao aparece no ERP", context)
        self.assertIn("Tabelas: MXSINTEGRACAOPEDIDO", context)
        self.assertLess(context.index("<analytical_context>"), context.index("<evidence>"))


class TestOpenAIExtraction(unittest.TestCase):
    def test_extracts_text_from_nested_content_item(self):
        content = [{"type": "text", "text": {"value": "Resposta final"}}]
        extracted = rag._openai_extract_text(content)
        self.assertEqual(extracted, "Resposta final")

    def test_extracts_text_from_message_refusal(self):
        extracted = rag._openai_extract_text(
            None,
            message={"role": "assistant", "content": "", "refusal": "Nao posso ajudar com isso."},
        )
        self.assertEqual(extracted, "Nao posso ajudar com isso.")

    def test_extracts_fallback_choice_text(self):
        extracted = rag._openai_extract_text(
            None,
            raw_response={"choices": [{"text": "Fallback de texto"}]},
        )
        self.assertEqual(extracted, "Fallback de texto")


class TestGroundingFallbackBehavior(unittest.TestCase):
    def test_keeps_answer_when_only_non_critical_grounding_error(self):
        answer = "Conta corrente usa este fluxo [fonte: guia.md].\n\nFontes:\n- guia.md"
        non_critical_error = ["Foram detectadas afirmacoes factuais sem citacao inline."]

        with patch.multiple(
            config,
            RAG_ENABLE_GROUNDING_VALIDATION=True,
            RAG_REQUIRE_SOURCES_SECTION=True,
            RAG_MAX_REGEN_ATTEMPTS=0,
        ), patch(
            "rag._validate_grounded_answer",
            return_value=(False, non_critical_error, {"guia.md"}),
        ):
            revised_answer, errors, cited, attempts = rag._apply_grounding_regeneration(
                answer=answer,
                question="Como trabalhar com conta corrente?",
                system="system",
                conversation_history=[],
                images=[],
                allowed_sources={"guia.md"},
            )

        self.assertNotIn("[fonte:", revised_answer.lower())
        self.assertIn("Fontes:", revised_answer)
        self.assertEqual(errors, non_critical_error)
        self.assertIn("guia.md", cited)
        self.assertEqual(attempts, 0)

    def test_abstains_when_grounding_error_is_critical(self):
        critical_error = ["Resposta vazia."]

        with patch.multiple(
            config,
            RAG_ENABLE_GROUNDING_VALIDATION=True,
            RAG_REQUIRE_SOURCES_SECTION=True,
            RAG_MAX_REGEN_ATTEMPTS=0,
        ), patch(
            "rag._validate_grounded_answer",
            return_value=(False, critical_error, set()),
        ):
            revised_answer, errors, _cited, attempts = rag._apply_grounding_regeneration(
                answer="Resposta sem fontes",
                question="Como trabalhar com conta corrente?",
                system="system",
                conversation_history=[],
                images=[],
                allowed_sources={"guia.md"},
            )

        self.assertTrue(revised_answer.startswith(config.NO_ANSWER_PHRASE))
        self.assertEqual(errors, critical_error)
        self.assertEqual(attempts, 0)


class TestDatabaseValidation(unittest.TestCase):
    def test_validate_database_accepts_env_url(self):
        with patch.dict("os.environ", {"DATABASE_URL": "postgresql://bot_maxima:bot_maxima@localhost:5432/bot_maxima"}):
            db.validate_database_config()

    def test_validate_database_rejects_missing_env_url(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(EnvironmentError):
                db.validate_database_config()


if __name__ == "__main__":
    unittest.main()
