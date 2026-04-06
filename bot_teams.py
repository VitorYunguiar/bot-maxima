"""
bot_teams.py — Bot Microsoft Teams com RAG, usando a mesma base do bot Discord.

Uso:
    iniciar_teams.bat
    py bot_teams.py

Pacote do Teams:
    gerar_manifest_teams.bat
    .\.venv\Scripts\python.exe scripts\build_teams_package.py

Requer:
    - Credenciais TEAMS_* no .env (Azure Bot Registration)
    - Metadata TEAMS_MANIFEST_* no .env para gerar o pacote do Teams
    - URL publica apontando para porta TEAMS_PORT (default: 3978)
    - ngrok http 3978  (para testes locais)
"""

import asyncio
import json
import logging
import re
import time

from aiohttp import web
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    BotFrameworkAdapter,
    TurnContext,
    ActivityHandler,
)
from botbuilder.schema import Activity, ActivityTypes

import config
import rag
from bot_common import ConversationManager, split_message

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Historico e cooldown centralizados
_conv = ConversationManager()


def _parse_feedback_command_payload(payload: str) -> dict:
    parts = [p.strip() for p in payload.split("||")]
    if len(parts) < 3:
        raise ValueError(
            "Formato invalido. Use: corrigir pergunta || resposta_bot || resposta_corrigida "
            "[|| level=global|tenant;tenant=...;erp=...;version=...] [|| tag1,tag2]"
        )

    question = parts[0]
    bot_answer = parts[1]
    corrected_answer = parts[2]
    scope: dict[str, str] = {"level": "global"}
    tags: list[str] = []

    if len(parts) >= 4 and parts[3]:
        for item in parts[3].split(";"):
            if "=" not in item:
                continue
            key, value = item.split("=", 1)
            key = key.strip().lower()
            value = value.strip()
            if key in {"level", "tenant", "erp", "version"} and value:
                scope[key] = value

    if len(parts) >= 5 and parts[4]:
        tags = [t.strip() for t in parts[4].split(",") if t.strip()]

    return {
        "question": question,
        "bot_answer": bot_answer,
        "corrected_answer": corrected_answer,
        "scope": scope,
        "tags": tags,
    }


def _is_teams_admin(user_id: str) -> bool:
    if not config.TEAMS_ADMIN_IDS:
        return True
    return str(user_id) in set(config.TEAMS_ADMIN_IDS)


async def _require_admin(turn_context: TurnContext, user_id: str) -> bool:
    if _is_teams_admin(user_id):
        return True
    await turn_context.send_activity(
        "Comando restrito a revisores admins. Configure seu usuario em TEAMS_ADMIN_IDS."
    )
    return False


# ── Bot Teams ────────────────────────────────────────────

class TeamsBot(ActivityHandler):
    """Bot Teams que responde perguntas usando RAG."""

    async def on_message_activity(self, turn_context: TurnContext):
        """Chamado quando o bot recebe uma mensagem."""
        text = (turn_context.activity.text or "").strip()
        user_id = turn_context.activity.from_property.id or "unknown"
        conv_id = turn_context.activity.conversation.id or "unknown"

        # Remover mencao do bot do texto (Teams inclui <at>BotName</at>)
        if turn_context.activity.recipient and turn_context.activity.recipient.name:
            text = re.sub(r"<at>.*?</at>", "", text).strip()

        if not text:
            await turn_context.send_activity("Me envie uma pergunta e eu vou consultar a base de documentos!")
            return

        # Comandos especiais
        lower = text.lower()

        if lower in ("ping", "!ping"):
            await turn_context.send_activity("Pong! Bot Teams ativo.")
            return

        if lower in ("status", "!status"):
            await self._handle_status(turn_context)
            return

        if lower in ("fontes", "!fontes", "docs", "documentos"):
            await self._handle_fontes(turn_context)
            return

        if lower in ("limpar", "!limpar", "clear"):
            _conv.clear_history(conv_id)
            await turn_context.send_activity("Historico de conversa limpo!")
            return

        if lower in ("ajuda", "!ajuda", "help", "!help"):
            await self._handle_help(turn_context)
            return

        if lower.startswith("corrigir "):
            await self._handle_corrigir(turn_context, user_id, text[len("corrigir "):].strip())
            return

        if lower in ("correcoes", "correcoes pendentes", "feedback pendentes"):
            if not await _require_admin(turn_context, user_id):
                return
            await self._handle_correcoes_pendentes(turn_context)
            return

        if lower.startswith("aprovar-correcao "):
            if not await _require_admin(turn_context, user_id):
                return
            payload = text[len("aprovar-correcao "):].strip()
            if not payload:
                await turn_context.send_activity("Uso: aprovar-correcao <id> [observacao]")
                return
            parts = payload.split(" ", 1)
            feedback_id = parts[0].strip()
            note = parts[1].strip() if len(parts) > 1 else ""
            await self._handle_aprovar_correcao(turn_context, user_id, feedback_id, note)
            return

        if lower.startswith("rejeitar-correcao "):
            if not await _require_admin(turn_context, user_id):
                return
            payload = text[len("rejeitar-correcao "):].strip()
            if not payload:
                await turn_context.send_activity("Uso: rejeitar-correcao <id> [motivo]")
                return
            parts = payload.split(" ", 1)
            feedback_id = parts[0].strip()
            note = parts[1].strip() if len(parts) > 1 else ""
            await self._handle_rejeitar_correcao(turn_context, user_id, feedback_id, note)
            return

        if lower.startswith("publicar-correcao "):
            if not await _require_admin(turn_context, user_id):
                return
            feedback_id = text[len("publicar-correcao "):].strip()
            if not feedback_id:
                await turn_context.send_activity("Uso: publicar-correcao <id>")
                return
            await self._handle_publicar_correcao(turn_context, user_id, feedback_id)
            return

        # Pergunta via RAG
        await self._handle_question(turn_context, user_id, conv_id, text)

    async def _handle_question(self, turn_context: TurnContext, user_id: str, conv_id: str, question: str):
        """Processa pergunta via RAG."""
        # Validacao de tamanho
        if len(question) > config.MAX_QUESTION_LENGTH:
            await turn_context.send_activity(
                f"Pergunta muito longa ({len(question)} caracteres). "
                f"O limite e {config.MAX_QUESTION_LENGTH} caracteres. Tente resumir."
            )
            return

        # Cooldown
        remaining = _conv.check_cooldown(user_id)
        if remaining is not None:
            await turn_context.send_activity(f"Aguarde {remaining:.0f}s antes de perguntar novamente.")
            return

        logger.info("QUERY user=%s conv=%s len=%d (teams)", user_id, conv_id, len(question))

        # Typing indicator
        await turn_context.send_activity(Activity(type=ActivityTypes.typing))

        history = _conv.get_history(conv_id)

        t_start = time.monotonic()
        try:
            answer, chunks, trace = await asyncio.wait_for(
                asyncio.to_thread(
                    rag.ask,
                    question,
                    list(history),
                    None,
                    config.SYSTEM_PROMPT_TEAMS,
                    "teams",
                    None,
                ),
                timeout=config.ASK_TIMEOUT_SECONDS,
            )
        except asyncio.TimeoutError:
            await turn_context.send_activity("A consulta excedeu o tempo limite. Tente novamente.")
            return
        except Exception as e:
            logger.error("Erro no RAG: %s", e)
            await turn_context.send_activity(f"Erro ao processar a pergunta: {str(e)[:200]}")
            return
        elapsed = time.monotonic() - t_start

        # Atualizar historico
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer})
        _conv.trim_history(conv_id)

        logger.info(
            "ANSWER_TRACE %s",
            json.dumps(
                {
                    "platform": "teams",
                    "user_id": user_id,
                    "conversation_id": conv_id,
                    "elapsed_ms": int(elapsed * 1000),
                    "trace": trace,
                },
                ensure_ascii=False,
            ),
        )

        # Registrar knowledge gap se similaridade baixa
        max_sim = rag._safe_similarity(trace.get("top_similarity", 0.0))
        if max_sim < config.CONFIDENCE_THRESHOLD:
            asyncio.get_running_loop().run_in_executor(
                None, rag.log_knowledge_gap, question, max_sim, "teams"
            )

        # Formatar e enviar
        response = answer

        # Teams suporta mensagens longas, mas dividir se exceder o limite
        if len(response) <= config.TEAMS_MSG_LIMIT:
            await turn_context.send_activity(response)
        else:
            parts = split_message(response, limit=config.TEAMS_MSG_LIMIT)
            for part in parts:
                await turn_context.send_activity(part)

    async def _handle_status(self, turn_context: TurnContext):
        """Mostra estatisticas da base."""
        try:
            stats = await asyncio.to_thread(rag.get_stats)
            model_info = await asyncio.to_thread(rag.get_model_config)
            msg = (
                f"**Status da Base de Conhecimento**\n\n"
                f"- Documentos: **{stats.get('total_documents', 0)}**\n"
                f"- Chunks indexados: **{stats.get('total_chunks', 0)}**\n"
                f"- Modelo: {model_info.get('generation_model')} ({model_info.get('llm_provider')})\n"
                f"- Embeddings: {model_info.get('embedding_model')} ({model_info.get('embedding_provider')})"
            )
            await turn_context.send_activity(msg)
        except Exception as e:
            await turn_context.send_activity(f"Erro ao buscar status: {e}")

    async def _handle_fontes(self, turn_context: TurnContext):
        """Lista documentos indexados."""
        try:
            docs = await asyncio.to_thread(rag.list_documents)
            if not docs:
                await turn_context.send_activity("Nenhum documento indexado ainda.")
                return

            lines = ["**Documentos na Base**\n"]
            for doc in docs[:30]:
                name = doc.get("filename", "?")
                chunks = doc.get("chunk_count", 0)
                doc_type = doc.get("doc_type", "?")
                lines.append(f"- **{name}** (tipo: {doc_type}, chunks: {chunks})")

            await turn_context.send_activity("\n".join(lines))
        except Exception as e:
            await turn_context.send_activity(f"Erro ao listar documentos: {e}")

    async def _handle_corrigir(self, turn_context: TurnContext, user_id: str, payload: str):
        try:
            parsed = _parse_feedback_command_payload(payload)
            feedback_id = await asyncio.to_thread(
                rag.submit_feedback_item,
                query=parsed["question"],
                bot_answer=parsed["bot_answer"],
                corrected_answer=parsed["corrected_answer"],
                tags=parsed["tags"],
                scope=parsed["scope"],
                created_by=f"teams:{user_id}",
                platform="teams",
                source_message_id=turn_context.activity.id,
            )
            await turn_context.send_activity(
                f"Correcao registrada com sucesso. ID: `{feedback_id}` (status: `PENDING`)."
            )
        except Exception as e:
            await turn_context.send_activity(f"Erro ao registrar correcao: {e}")

    async def _handle_correcoes_pendentes(self, turn_context: TurnContext):
        try:
            pending = await asyncio.to_thread(rag.list_pending_feedback_items, 10)
            if not pending:
                await turn_context.send_activity("Nao ha correcoes pendentes.")
                return
            lines = ["**Correcoes Pendentes**\n"]
            for item in pending:
                feedback_id = item.get("id", "?")
                question = (item.get("query") or "?")[:120]
                scope = item.get("scope") or {}
                if isinstance(scope, dict):
                    scope_txt = ", ".join(
                        f"{k}={v}" for k, v in scope.items() if str(v).strip()
                    ) or "global"
                else:
                    scope_txt = "global"
                lines.append(f"- `{feedback_id}` | {scope_txt} | {question}")
            await turn_context.send_activity("\n".join(lines))
        except Exception as e:
            await turn_context.send_activity(f"Erro ao listar correcoes pendentes: {e}")

    async def _handle_aprovar_correcao(
        self,
        turn_context: TurnContext,
        user_id: str,
        feedback_id: str,
        note: str = "",
    ):
        try:
            await asyncio.to_thread(
                rag.approve_feedback_item,
                feedback_id,
                f"teams:{user_id}",
                note or None,
            )
            await turn_context.send_activity(f"Correcao `{feedback_id}` aprovada.")
        except Exception as e:
            await turn_context.send_activity(f"Erro ao aprovar correcao: {e}")

    async def _handle_rejeitar_correcao(
        self,
        turn_context: TurnContext,
        user_id: str,
        feedback_id: str,
        note: str = "",
    ):
        try:
            await asyncio.to_thread(
                rag.reject_feedback_item,
                feedback_id,
                f"teams:{user_id}",
                note or None,
            )
            await turn_context.send_activity(f"Correcao `{feedback_id}` rejeitada.")
        except Exception as e:
            await turn_context.send_activity(f"Erro ao rejeitar correcao: {e}")

    async def _handle_publicar_correcao(
        self,
        turn_context: TurnContext,
        user_id: str,
        feedback_id: str,
    ):
        try:
            chunk_id = await asyncio.to_thread(
                rag.publish_feedback_item,
                feedback_id,
                f"teams:{user_id}",
                None,
            )
            await turn_context.send_activity(
                f"Correcao `{feedback_id}` publicada na memoria vetorial. Chunk: `{chunk_id}`."
            )
        except Exception as e:
            await turn_context.send_activity(f"Erro ao publicar correcao: {e}")

    async def _handle_help(self, turn_context: TurnContext):
        """Mostra comandos disponiveis."""
        msg = (
            "**Sabidao - Assistente Tecnico Maxima**\n\n"
            "Consulto a base de documentos para responder perguntas sobre "
            "maxPedido, ERPs e ferramentas de gestao.\n\n"
            "**Como usar:**\n"
            "- Envie qualquer mensagem para perguntar sobre os documentos\n"
            "- Exemplo: *Como configurar o parametro USAGRADE no maxPedido?*\n\n"
            "**Comandos:**\n"
            "- **status** - estatisticas da base de conhecimento\n"
            "- **fontes** - lista de documentos indexados\n"
            "- **limpar** - limpa o historico de conversa\n"
            "- **ping** - verifica se o bot esta ativo\n"
            "- **ajuda** - esta mensagem\n"
            "- **corrigir <payload>** - registra correcao para revisao\n"
            "- **correcoes pendentes** - (admin) lista fila de revisao\n"
            "- **aprovar-correcao <id>** / **rejeitar-correcao <id>** / **publicar-correcao <id>** - (admin)\n\n"
            "Dica: quanto mais especifica a pergunta, melhor a resposta."
        )
        await turn_context.send_activity(msg)

    async def on_members_added_activity(self, members_added, turn_context: TurnContext):
        """Mensagem de boas-vindas quando alguem adiciona o bot."""
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Ola! Sou o assistente de documentos. "
                    "Envie uma pergunta e eu vou consultar a base de conhecimento. "
                    "Digite **ajuda** para ver os comandos disponiveis."
                )


# ── Error handler ────────────────────────────────────────

async def on_error(context: TurnContext, error: Exception):
    """Handler global de erros."""
    logger.error("Erro nao tratado: %s", error, exc_info=True)
    try:
        await context.send_activity("Ocorreu um erro interno. Tente novamente.")
    except Exception:
        pass


# ── Servidor aiohttp ─────────────────────────────────────

SETTINGS = BotFrameworkAdapterSettings(
    app_id=config.TEAMS_APP_ID,
    app_password=config.TEAMS_APP_PASSWORD,
    channel_auth_tenant=config.TEAMS_TENANT_ID,
)
ADAPTER = BotFrameworkAdapter(SETTINGS)
ADAPTER.on_turn_error = on_error

BOT = TeamsBot()


async def messages(req: web.Request) -> web.Response:
    """Endpoint principal — recebe mensagens do Teams via Azure Bot Service."""
    if "application/json" not in req.headers.get("Content-Type", ""):
        return web.Response(status=415)

    body = await req.json()
    activity = Activity().deserialize(body)

    # Ignorar atividades de typing (enviadas enquanto o usuário digita)
    if activity.type == "typing":
        return web.Response(status=200)

    auth_header = req.headers.get("Authorization", "")

    await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    return web.Response(status=201)


async def health(req: web.Request) -> web.Response:
    """Health check endpoint."""
    return web.json_response({"status": "ok", "platform": "teams"})


def init_app() -> web.Application:
    """Cria e configura a aplicacao aiohttp."""
    app = web.Application()
    app.router.add_post("/api/messages", messages)
    app.router.add_get("/api/health", health)
    return app


# ── Start ─────────────────────────────────────────────────

if __name__ == "__main__":
    config.validate(platform="teams")

    app = init_app()

    logger.info("Iniciando bot Teams na porta %s...", config.TEAMS_PORT)
    logger.info("Endpoint: http://localhost:%s/api/messages", config.TEAMS_PORT)
    logger.info("Health:   http://localhost:%s/api/health", config.TEAMS_PORT)

    try:
        web.run_app(app, host="0.0.0.0", port=config.TEAMS_PORT)
    except KeyboardInterrupt:
        logger.info("Bot Teams encerrado.")
