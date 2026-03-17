"""
bot_common.py — Logica compartilhada entre bot Discord e bot Teams.
Evita duplicacao de codigo de historico, cooldown, split e formatacao.
"""

import time
from collections import OrderedDict

import config


class ConversationManager:
    """Gerencia historico de conversa por canal/conversa com LRU e cooldown por usuario."""

    def __init__(self):
        self.history: OrderedDict = OrderedDict()
        self._user_last_ask: dict = {}

    def get_history(self, channel_id) -> list[dict]:
        """Retorna historico do canal com evicao LRU."""
        if channel_id in self.history:
            self.history.move_to_end(channel_id)
            return self.history[channel_id]
        if len(self.history) >= config.MAX_HISTORY_CHANNELS:
            self.history.popitem(last=False)
        self.history[channel_id] = []
        return self.history[channel_id]

    def trim_history(self, channel_id):
        """Mantem apenas as ultimas MAX_HISTORY_PAIRS trocas."""
        history = self.history.get(channel_id, [])
        max_msgs = config.MAX_HISTORY_PAIRS * 2
        if len(history) > max_msgs:
            self.history[channel_id] = history[-max_msgs:]

    def clear_history(self, channel_id):
        """Limpa historico de um canal."""
        self.history.pop(channel_id, None)

    def check_cooldown(self, user_id) -> float | None:
        """Retorna segundos restantes se em cooldown, senao None."""
        last = self._user_last_ask.get(user_id, 0)
        remaining = config.COOLDOWN_SECONDS - (time.monotonic() - last)
        if remaining > 0:
            return remaining
        self._user_last_ask[user_id] = time.monotonic()
        return None


def split_message(text: str, limit: int) -> list[str]:
    """Divide mensagem respeitando limites de linha e espaco."""
    if len(text) <= limit:
        return [text]
    parts = []
    while text:
        if len(text) <= limit:
            parts.append(text)
            break
        split_at = text.rfind("\n", 0, limit)
        if split_at <= 0:
            split_at = text.rfind(" ", 0, limit)
        if split_at <= 0:
            split_at = limit
        parts.append(text[:split_at])
        text = text[split_at:].lstrip("\n")
    return parts


def format_sources(chunks: list[dict], style: str = "discord") -> str:
    """Formata fontes dos chunks retornados.

    style: 'discord' usa backticks, 'teams' usa negrito.
    """
    sources = set()
    for chunk in chunks:
        filename = chunk.get("filename", "")
        similarity = chunk.get("similarity", 0)
        if filename:
            if style == "discord":
                safe_name = filename.replace("`", "'")
                sources.add(f"`{safe_name}` ({similarity:.0%})")
            else:
                sources.add(f"**{filename}** ({similarity:.0%})")
    if sources:
        return f"\n\n**Fontes:** {', '.join(sorted(sources))}"
    return ""
