"""
bot_teams.py — Bot Microsoft Teams com RAG, usando a mesma base do bot Discord.

Uso:
    py bot_teams.py

Requer:
    - TEAMS_APP_ID e TEAMS_APP_PASSWORD no .env (do Azure Bot Registration)
    - URL publica apontando para porta TEAMS_PORT (default: 3978)
    - ngrok http 3978  (para testes locais)
"""

import asyncio
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
            bot_name = turn_context.activity.recipient.name
            # Remove tags <at>...</at>
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
            answer, chunks = await asyncio.wait_for(
                asyncio.to_thread(rag.ask, question, list(history)),
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
        hist = _conv.get_history(conv_id)
        hist.append({"role": "user", "content": question})
        hist.append({"role": "assistant", "content": answer})
        _conv.trim_history(conv_id)

        # Registrar knowledge gap se similaridade baixa
        max_sim = (
            max((rag._safe_similarity(c.get("similarity", 0)) for c in chunks), default=0.0)
            if chunks
            else 0.0
        )
        if max_sim < config.CONFIDENCE_THRESHOLD:
            asyncio.get_event_loop().run_in_executor(
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
            msg = (
                f"**Status da Base de Conhecimento**\n\n"
                f"- Documentos: **{stats.get('total_documents', 0)}**\n"
                f"- Chunks indexados: **{stats.get('total_chunks', 0)}**\n"
                f"- Modelo: {config.GEMINI_MODEL}\n"
                f"- Embeddings: {config.EMBEDDING_MODEL}"
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

    async def _handle_help(self, turn_context: TurnContext):
        """Mostra comandos disponiveis."""
        msg = (
            "**Sabidao — Assistente Tecnico Maxima**\n\n"
            "Consulto a base de documentos para responder perguntas sobre "
            "maxPedido, ERPs e ferramentas de gestao.\n\n"
            "**Como usar:**\n"
            "- Envie qualquer mensagem para perguntar sobre os documentos\n"
            "- Exemplo: *Como configurar o parametro USAGRADE no maxPedido?*\n\n"
            "**Comandos:**\n"
            "- **status** — estatisticas da base de conhecimento\n"
            "- **fontes** — lista de documentos indexados\n"
            "- **limpar** — limpa o historico de conversa\n"
            "- **ping** — verifica se o bot esta ativo\n"
            "- **ajuda** — esta mensagem\n\n"
            "💡 *Dica: quanto mais especifica a pergunta, melhor a resposta.*"
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
