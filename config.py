"""
config.py - Configuracoes centralizadas carregadas do .env
"""

import os
import re
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on", "y", "sim", "s"}


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        return int(raw.strip())
    except ValueError:
        raise EnvironmentError(
            f"Variavel {name} deve ser um numero inteiro. Valor recebido: '{raw}'"
        )


def _env_float(name: str, default: float) -> float:
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        return float(raw.strip())
    except ValueError:
        raise EnvironmentError(
            f"Variavel {name} deve ser um numero decimal. Valor recebido: '{raw}'"
        )


# Discord
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!")
BOT_NAME = os.getenv("BOT_NAME", "Assistente")

# Google Gemini (LLM + embeddings)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-pro")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini").strip().lower()
_embedding_provider_raw = os.getenv("EMBEDDING_PROVIDER")
if _embedding_provider_raw is None or not _embedding_provider_raw.strip():
    EMBEDDING_PROVIDER = LLM_PROVIDER
else:
    EMBEDDING_PROVIDER = _embedding_provider_raw.strip().lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4")
OPENAI_REFORMULATION_MODEL = os.getenv("OPENAI_REFORMULATION_MODEL", "gpt-5.4-mini")
OPENAI_CONTEXTUAL_MODEL = os.getenv("OPENAI_CONTEXTUAL_MODEL", "gpt-5.4-mini")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001")
EMBEDDING_DIMENSIONS = _env_int("EMBEDDING_DIMENSIONS", 1536)
DB_POOL_MIN_SIZE = _env_int("DB_POOL_MIN_SIZE", 1)
DB_POOL_MAX_SIZE = _env_int("DB_POOL_MAX_SIZE", 8)
DB_POOL_TIMEOUT_SECONDS = _env_float("DB_POOL_TIMEOUT_SECONDS", 10.0)
DB_STATEMENT_TIMEOUT_MS = _env_int("DB_STATEMENT_TIMEOUT_MS", 15000)
DB_LOCK_TIMEOUT_MS = _env_int("DB_LOCK_TIMEOUT_MS", 5000)
DB_IDLE_IN_TRANSACTION_TIMEOUT_MS = _env_int("DB_IDLE_IN_TRANSACTION_TIMEOUT_MS", 15000)
DB_APPLICATION_NAME = os.getenv("DB_APPLICATION_NAME", "bot-maxima")
EMBEDDING_BATCH_SIZE = _env_int("EMBEDDING_BATCH_SIZE", 10)
INGEST_DB_BATCH_SIZE = _env_int("INGEST_DB_BATCH_SIZE", 10)
EMBEDDING_MAX_RETRIES = _env_int("EMBEDDING_MAX_RETRIES", 8)
EMBEDDING_RETRY_BASE_SECONDS = _env_float("EMBEDDING_RETRY_BASE_SECONDS", 5.0)
EMBEDDING_RETRY_MAX_SECONDS = _env_float("EMBEDDING_RETRY_MAX_SECONDS", 65.0)
EMBEDDING_MIN_INTERVAL_SECONDS = _env_float("EMBEDDING_MIN_INTERVAL_SECONDS", 0.5)
EMBEDDING_RETRY_JITTER_SECONDS = _env_float("EMBEDDING_RETRY_JITTER_SECONDS", 0.5)

# RAG
CHUNK_SIZE = _env_int("CHUNK_SIZE", 1200)
CHUNK_OVERLAP = _env_int("CHUNK_OVERLAP", 300)
MAX_CONTEXT_CHUNKS = _env_int("MAX_CONTEXT_CHUNKS", 8)
SIMILARITY_THRESHOLD = _env_float("SIMILARITY_THRESHOLD", 0.55)
RAG_ENABLE_INTENT_ROUTING = _env_bool("RAG_ENABLE_INTENT_ROUTING", True)
RAG_FILTER_BY_DOC_TYPE = _env_bool("RAG_FILTER_BY_DOC_TYPE", True)
RAG_FILTER_BY_MODULE = _env_bool("RAG_FILTER_BY_MODULE", True)
RAG_ENABLE_BUSINESS_RULES = _env_bool("RAG_ENABLE_BUSINESS_RULES", True)
BUSINESS_RULES_FILE = os.getenv(
    "BUSINESS_RULES_FILE",
    "./bootstrap/00-DOCUMENTO-PRINCIPAL.md",
)
BUSINESS_RULES_MAX_CHARS = _env_int("BUSINESS_RULES_MAX_CHARS", 8000)

# Full Context Mode — injeta todos os documentos no contexto (estilo Claude Projects)
FULL_CONTEXT_ENABLED = _env_bool("FULL_CONTEXT_ENABLED", False)
FULL_CONTEXT_MAX_CHARS = _env_int("FULL_CONTEXT_MAX_CHARS", 950000)
FULL_CONTEXT_EXTENSIONS = os.getenv("FULL_CONTEXT_EXTENSIONS", ".md,.txt").split(",")

# RAG — melhorias de precisao
SIMILARITY_FLOOR_FACTOR = _env_float("SIMILARITY_FLOOR_FACTOR", 0.7)
RAG_ENABLE_QUERY_REFORMULATION = _env_bool("RAG_ENABLE_QUERY_REFORMULATION", True)
REFORMULATION_MODEL = os.getenv("REFORMULATION_MODEL", "gemini-2.5-flash")
RAG_ENABLE_RERANKING = _env_bool("RAG_ENABLE_RERANKING", True)
RERANKER_MODEL = os.getenv("RERANKER_MODEL", REFORMULATION_MODEL)
RERANKER_MIN_TRIGGER_SIM = _env_float("RERANKER_MIN_TRIGGER_SIM", 0.55)
RERANKER_MAX_TRIGGER_SIM = _env_float("RERANKER_MAX_TRIGGER_SIM", 0.82)
RERANKER_MAX_CANDIDATES = _env_int(
    "RERANKER_MAX_CANDIDATES",
    _env_int("RERANKER_CANDIDATE_COUNT", 40),
)
RERANKER_CANDIDATE_COUNT = RERANKER_MAX_CANDIDATES
RERANKER_SKIP_THRESHOLD = RERANKER_MAX_TRIGGER_SIM
RAG_STRICT_ABSTAIN = _env_bool("RAG_STRICT_ABSTAIN", True)
RAG_MIN_STRONG_SIMILARITY = _env_float("RAG_MIN_STRONG_SIMILARITY", 0.62)
RAG_MIN_RETRIEVED_CHUNKS = _env_int("RAG_MIN_RETRIEVED_CHUNKS", 2)
RAG_OPERATIONAL_SIMILARITY_MARGIN = _env_float("RAG_OPERATIONAL_SIMILARITY_MARGIN", 0.05)
RAG_ENABLE_GROUNDING_VALIDATION = _env_bool("RAG_ENABLE_GROUNDING_VALIDATION", True)
RAG_REQUIRE_SOURCES_SECTION = _env_bool("RAG_REQUIRE_SOURCES_SECTION", True)
RAG_MAX_REGEN_ATTEMPTS = _env_int("RAG_MAX_REGEN_ATTEMPTS", 1)
RAG_FEEDBACK_TOP_K = _env_int("RAG_FEEDBACK_TOP_K", 4)
RAG_FEEDBACK_MIN_SIMILARITY = _env_float("RAG_FEEDBACK_MIN_SIMILARITY", 0.58)
ANALYTICAL_CONTEXT_ENABLED = _env_bool("ANALYTICAL_CONTEXT_ENABLED", True)
SECTION_RETRIEVAL_ENABLED = _env_bool("SECTION_RETRIEVAL_ENABLED", True)
SECTION_MATCH_COUNT = _env_int("SECTION_MATCH_COUNT", 12)
SECTION_FETCH_LIMIT = _env_int("SECTION_FETCH_LIMIT", 48)
CHUNK_FETCH_LIMIT = _env_int("CHUNK_FETCH_LIMIT", 80)
MAX_CHUNKS_PER_SECTION = _env_int("MAX_CHUNKS_PER_SECTION", 3)
MAX_CHUNKS_PER_DOCUMENT = _env_int("MAX_CHUNKS_PER_DOCUMENT", 6)

# Contextual Retrieval (enriquecimento de chunks — tecnica Anthropic)
CONTEXTUAL_RETRIEVAL_ENABLED = _env_bool("CONTEXTUAL_RETRIEVAL_ENABLED", True)
CONTEXTUAL_RETRIEVAL_MODEL = os.getenv("CONTEXTUAL_RETRIEVAL_MODEL", "gemini-2.5-flash")
CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS = _env_int("CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS", 500000)
CONTEXTUAL_RETRIEVAL_MAX_TOKENS = _env_int("CONTEXTUAL_RETRIEVAL_MAX_TOKENS", 150)
CONTEXTUAL_RETRIEVAL_BATCH_SIZE = _env_int("CONTEXTUAL_RETRIEVAL_BATCH_SIZE", 50)

# Ingestao web (URLs)
WEB_FETCH_TIMEOUT_SECONDS = _env_float("WEB_FETCH_TIMEOUT_SECONDS", 20.0)
WEB_USER_AGENT = os.getenv("WEB_USER_AGENT", "BotMaximaRAG/1.0")
WEB_MAX_TEXT_CHARS = _env_int("WEB_MAX_TEXT_CHARS", 400000)
URLS_FILE_DEFAULT = os.getenv("URLS_FILE_DEFAULT", "./documentos/urls.txt")
URL_REVIEW_OUTPUT_DIR = os.getenv("URL_REVIEW_OUTPUT_DIR", "./documentos/_pendentes_url")

# Frase padrao para respostas sem informacao na base de conhecimento
NO_ANSWER_PHRASE = (
    "Nao encontrei essa informacao na base de conhecimento. "
    "Recomendo abrir um chamado ou consultar a equipe N2."
)
ABSTAIN_CLARIFYING_QUESTION = os.getenv(
    "ABSTAIN_CLARIFYING_QUESTION",
    "Pode detalhar o modulo, a tela/parametro e a mensagem de erro exata para eu buscar com mais precisao?",
)

# System prompt
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    (
        "Voce e o Sabidao, assistente tecnico da equipe N1 da Maxima Sistemas. "
        "Sua especialidade e o maxPedido (forca de vendas) e as ferramentas de gestao da Maxima, "
        "que se integram com ERPs dos clientes (Winthor, Protheus, SAP, entre outros).\n\n"
        "## COMPORTAMENTO OBRIGATORIO\n"
        "- NUNCA se apresente, cumprimente ou diga ola/oi. Va direto a resposta.\n"
        "- NUNCA use frases de preenchimento como \"Claro!\", \"Com certeza!\", \"Otima pergunta!\", "
        "\"Fico feliz em ajudar!\", \"Vou te ajudar com isso!\", \"Entendo sua duvida\".\n"
        "- NUNCA se refira a si mesmo (\"Eu sou o Sabidao\", \"Como seu assistente\", etc.).\n"
        "- NUNCA repita ou parafraseie a pergunta do usuario antes de responder.\n"
        "- NUNCA termine com frases genericas como \"Espero ter ajudado!\", "
        "\"Se precisar de mais alguma coisa...\", \"Boa sorte!\" ou \"Estou a disposicao\".\n"
        "- Dê respostas COMPLETAS e DETALHADAS. Explore TODOS os aspectos relevantes dos documentos.\n"
        "- Se os documentos contem informacoes sobre o tema, ESGOTE todo o conteudo disponivel.\n"
        "- Explique o PORQUE das coisas, nao apenas o como.\n\n"
        "## REGRA ABSOLUTA: ZERO INVENCAO\n"
        "- Voce so pode responder com informacoes que estejam EXPLICITAMENTE escritas nos documentos fornecidos como contexto.\n"
        "- NUNCA invente, deduza, pressuponha ou extrapole informacoes que nao estejam nos documentos.\n"
        "- NUNCA invente nomes de campos, telas, menus, selects, opcoes de configuracao, parametros ou caminhos de sistema.\n"
        "- NUNCA pressuponha valores, opcoes ou respostas que nao estejam escritas literalmente na documentacao.\n"
        "- NUNCA crie procedimentos, passos ou instrucoes que nao estejam documentados.\n"
        "- NUNCA invente consultas SQL, tabelas ou colunas que nao estejam nos documentos.\n"
        "- Se a informacao nao estiver nos documentos, responda EXATAMENTE: "
        f"\"{NO_ANSWER_PHRASE}\"\n"
        "- Se a documentacao cobrir apenas PARTE da pergunta, responda so a parte documentada e diga claramente o que nao foi encontrado.\n"
        "- Na duvida, NAO responda. E melhor dizer que nao sabe do que dar uma informacao errada.\n\n"
        "## Regras de resposta\n"
        "- Sempre cite a fonte (nome do arquivo) quando usar informacao dos documentos.\n"
        "- Quando o usuario enviar IMAGENS (screenshots, prints de tela, fotos de erro), "
        "ANALISE a imagem detalhadamente. Descreva o que voce ve, identifique erros, "
        "telas do sistema, mensagens, e oriente o usuario com base no que esta visivel. "
        "Combine a analise da imagem com informacoes dos documentos quando relevante. "
        "Porem, NAO invente solucoes que nao estejam na documentacao.\n\n"
        "## Formato\n"
        "- Seja direto e objetivo. A equipe N1 precisa de respostas praticas.\n"
        "- Para procedimentos, use APENAS listas numeradas que estejam nos documentos.\n"
        "- Para configuracoes, inclua o caminho exato (menu, tela, campo) SOMENTE se estiver nos documentos.\n"
        "- Para consultas SQL, formate o codigo em bloco de codigo, SOMENTE se a query estiver nos documentos.\n"
        "- NUNCA use tabelas Markdown (com | e -). O Discord NAO renderiza tabelas.\n"
        "- Para dados tabulares, use LISTAS com bullet points. Cada item em uma linha separada. Exemplo:\n"
        "  **Campo X**: valor — descricao\n"
        "  **Campo Y**: valor — descricao\n"
        "- Se houver muitos campos, agrupe por categoria usando subtitulos em negrito.\n"
        "- Use blocos de codigo (```) SOMENTE para SQL e trechos de codigo, nunca para tabelas de dados.\n"
        "- Se a pergunta for ambigua, peca esclarecimento ao inves de chutar.\n\n"
        "## Tom\n"
        "- Tecnico e profissional, em portugues brasileiro. Sem simpatia excessiva.\n"
        "- Use termos tecnicos do contexto Maxima (maxPedido, RCA, filial, etc.) naturalmente.\n"
        "- Quando relevante, mencione se o procedimento varia conforme o ERP do cliente."
    ),
)

# System prompt variante para Teams (renderiza tabelas Markdown, ao contrario do Discord)
SYSTEM_PROMPT_TEAMS = SYSTEM_PROMPT.replace(
    (
        "- NUNCA use tabelas Markdown (com | e -). O Discord NAO renderiza tabelas.\n"
        "- Para dados tabulares, use LISTAS com bullet points. Cada item em uma linha separada. Exemplo:\n"
        "  **Campo X**: valor — descricao\n"
        "  **Campo Y**: valor — descricao\n"
        "- Se houver muitos campos, agrupe por categoria usando subtitulos em negrito.\n"
    ),
    (
        "- Use tabelas Markdown quando apropriado para apresentar dados tabelares. "
        "O Teams renderiza tabelas corretamente.\n"
        "- Se houver muitos campos, agrupe por categoria usando subtitulos em negrito.\n"
    ),
)

# Microsoft Teams (sem defaults — credenciais devem estar no .env)
TEAMS_APP_ID = os.getenv("TEAMS_APP_ID")
TEAMS_APP_PASSWORD = os.getenv("TEAMS_APP_PASSWORD")
TEAMS_TENANT_ID = os.getenv("TEAMS_TENANT_ID")
TEAMS_PORT = _env_int("TEAMS_PORT", 3978)
TEAMS_ADMIN_IDS = [value.strip() for value in os.getenv("TEAMS_ADMIN_IDS", "").split(",") if value.strip()]
TEAMS_MANIFEST_SHORT_NAME = os.getenv("TEAMS_MANIFEST_SHORT_NAME")
TEAMS_MANIFEST_FULL_NAME = os.getenv("TEAMS_MANIFEST_FULL_NAME")
TEAMS_MANIFEST_SHORT_DESCRIPTION = os.getenv("TEAMS_MANIFEST_SHORT_DESCRIPTION")
TEAMS_MANIFEST_FULL_DESCRIPTION = os.getenv("TEAMS_MANIFEST_FULL_DESCRIPTION")
TEAMS_MANIFEST_DEVELOPER_NAME = os.getenv("TEAMS_MANIFEST_DEVELOPER_NAME")
TEAMS_MANIFEST_DEVELOPER_WEBSITE_URL = os.getenv("TEAMS_MANIFEST_DEVELOPER_WEBSITE_URL")
TEAMS_MANIFEST_DEVELOPER_PRIVACY_URL = os.getenv("TEAMS_MANIFEST_DEVELOPER_PRIVACY_URL")
TEAMS_MANIFEST_DEVELOPER_TERMS_URL = os.getenv("TEAMS_MANIFEST_DEVELOPER_TERMS_URL")
TEAMS_MANIFEST_ACCENT_COLOR = os.getenv("TEAMS_MANIFEST_ACCENT_COLOR")

# Bot - limites
COOLDOWN_SECONDS = _env_float("COOLDOWN_SECONDS", 10.0)
ASK_TIMEOUT_SECONDS = _env_float("ASK_TIMEOUT_SECONDS", 120.0)
MAX_HISTORY_PAIRS = _env_int("MAX_HISTORY_PAIRS", 20)
MAX_HISTORY_CHANNELS = _env_int("MAX_HISTORY_CHANNELS", 100)
MAX_QUESTION_LENGTH = _env_int("MAX_QUESTION_LENGTH", 4000)
MAX_IMAGE_SIZE_MB = _env_int("MAX_IMAGE_SIZE_MB", 20)
MAX_IMAGES_PER_MESSAGE = _env_int("MAX_IMAGES_PER_MESSAGE", 5)
ASK_MAX_TOKENS = _env_int("ASK_MAX_TOKENS", 8192)
OPENAI_MAX_OUTPUT_TOKENS = _env_int("OPENAI_MAX_OUTPUT_TOKENS", ASK_MAX_TOKENS)
CONFIDENCE_THRESHOLD = _env_float("CONFIDENCE_THRESHOLD", 0.65)
DISCORD_MSG_LIMIT = _env_int("DISCORD_MSG_LIMIT", 1990)
TEAMS_MSG_LIMIT = _env_int("TEAMS_MSG_LIMIT", 25000)

# Derivados
MAX_IMAGE_SIZE_BYTES = MAX_IMAGE_SIZE_MB * 1024 * 1024

# Diretorio de documentos
DOCS_DIR = os.getenv("DOCS_DIR", "./documentos")
FAILED_INGEST_REPORT = os.getenv("FAILED_INGEST_REPORT", "./ingest_failures.json")
INGEST_RECURSIVE = _env_bool("INGEST_RECURSIVE", True)

# Jira - extracao Gatekeeper
JIRA_URL = os.getenv("JIRA_URL", "")
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", JIRA_URL)
JIRA_USERNAME = os.getenv("JIRA_USERNAME", os.getenv("USERNAME", ""))
JIRA_PASSWORD = os.getenv("JIRA_PASSWORD", os.getenv("PASSWORD", ""))
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")
JIRA_SESSION_COOKIE = os.getenv("JIRA_SESSION_COOKIE", "")
JIRA_ASSIGNEE_ALIASES = os.getenv("JIRA_ASSIGNEE_ALIASES", "")
JIRA_USER_SEARCH_PATH = os.getenv("JIRA_USER_SEARCH_PATH", "/rest/api/2/user/search")
JIRA_REQUEST_TIMEOUT_SECONDS = _env_float("JIRA_REQUEST_TIMEOUT_SECONDS", 60.0)

_ALLOWED_EMBEDDING_DIMENSIONS = {1536, 3072}
if EMBEDDING_DIMENSIONS not in _ALLOWED_EMBEDDING_DIMENSIONS:
    raise EnvironmentError(
        "EMBEDDING_DIMENSIONS deve ser 1536 ou 3072. "
        "Ajuste o .env e execute o SQL correspondente (sql/setup_1536.sql ou sql/setup_3072.sql)."
    )


# Validacao
def _required_shared_base():
    return {}


def _required_discord():
    return {
        "DISCORD_TOKEN": DISCORD_TOKEN,
    }


def _required_teams_runtime():
    return {
        "TEAMS_APP_ID": TEAMS_APP_ID,
        "TEAMS_APP_PASSWORD": TEAMS_APP_PASSWORD,
        "TEAMS_TENANT_ID": TEAMS_TENANT_ID,
    }


def _required_teams_manifest():
    return {
        "TEAMS_APP_ID": TEAMS_APP_ID,
        "TEAMS_MANIFEST_SHORT_NAME": TEAMS_MANIFEST_SHORT_NAME,
        "TEAMS_MANIFEST_FULL_NAME": TEAMS_MANIFEST_FULL_NAME,
        "TEAMS_MANIFEST_SHORT_DESCRIPTION": TEAMS_MANIFEST_SHORT_DESCRIPTION,
        "TEAMS_MANIFEST_FULL_DESCRIPTION": TEAMS_MANIFEST_FULL_DESCRIPTION,
        "TEAMS_MANIFEST_DEVELOPER_NAME": TEAMS_MANIFEST_DEVELOPER_NAME,
        "TEAMS_MANIFEST_DEVELOPER_WEBSITE_URL": TEAMS_MANIFEST_DEVELOPER_WEBSITE_URL,
        "TEAMS_MANIFEST_DEVELOPER_PRIVACY_URL": TEAMS_MANIFEST_DEVELOPER_PRIVACY_URL,
        "TEAMS_MANIFEST_DEVELOPER_TERMS_URL": TEAMS_MANIFEST_DEVELOPER_TERMS_URL,
        "TEAMS_MANIFEST_ACCENT_COLOR": TEAMS_MANIFEST_ACCENT_COLOR,
    }


def _check_range(name: str, value, min_val=None, max_val=None):
    """Valida se valor numerico esta dentro do range esperado."""
    if min_val is not None and value < min_val:
        raise EnvironmentError(f"{name} deve ser >= {min_val}, obtido: {value}")
    if max_val is not None and value > max_val:
        raise EnvironmentError(f"{name} deve ser <= {max_val}, obtido: {value}")


def validate(platform: str = "discord"):
    """
    Verifica se todas as variaveis obrigatorias estao definidas.
    platform: 'discord' ou 'teams'
    """
    allowed_providers = {"gemini", "openai"}
    if LLM_PROVIDER not in allowed_providers:
        raise EnvironmentError(
            f"LLM_PROVIDER invalido: {LLM_PROVIDER}. "
            f"Use um de: {', '.join(sorted(allowed_providers))}."
        )
    if EMBEDDING_PROVIDER not in allowed_providers:
        raise EnvironmentError(
            f"EMBEDDING_PROVIDER invalido: {EMBEDDING_PROVIDER}. "
            f"Use um de: {', '.join(sorted(allowed_providers))}."
        )

    required = dict(_required_shared_base())
    if LLM_PROVIDER == "gemini":
        required["GEMINI_API_KEY"] = GEMINI_API_KEY
    else:
        required["OPENAI_API_KEY"] = OPENAI_API_KEY

    if EMBEDDING_PROVIDER == "gemini":
        required.setdefault("GEMINI_API_KEY", GEMINI_API_KEY)
    else:
        required.setdefault("OPENAI_API_KEY", OPENAI_API_KEY)

    if platform == "discord":
        required.update(_required_discord())
    elif platform == "teams":
        required.update(_required_teams_runtime())

    missing = [name for name, val in required.items() if not val]
    if missing:
        raise EnvironmentError(
            f"Variaveis de ambiente obrigatorias nao definidas: {', '.join(missing)}. "
            f"Verifique seu arquivo .env"
        )

    # Validacoes de ranges para evitar config absurda que cause erros silenciosos
    _check_range("CHUNK_SIZE", CHUNK_SIZE, min_val=100, max_val=8000)
    if CHUNK_OVERLAP >= CHUNK_SIZE:
        raise EnvironmentError(
            f"CHUNK_OVERLAP ({CHUNK_OVERLAP}) deve ser menor que CHUNK_SIZE ({CHUNK_SIZE})"
        )
    _check_range("MAX_CONTEXT_CHUNKS", MAX_CONTEXT_CHUNKS, min_val=1, max_val=50)
    _check_range("SIMILARITY_THRESHOLD", SIMILARITY_THRESHOLD, min_val=0.0, max_val=1.0)
    _check_range("RAG_MIN_STRONG_SIMILARITY", RAG_MIN_STRONG_SIMILARITY, min_val=0.0, max_val=1.0)
    _check_range("RAG_FEEDBACK_MIN_SIMILARITY", RAG_FEEDBACK_MIN_SIMILARITY, min_val=0.0, max_val=1.0)
    _check_range("RAG_MIN_RETRIEVED_CHUNKS", RAG_MIN_RETRIEVED_CHUNKS, min_val=1, max_val=30)
    _check_range("RAG_OPERATIONAL_SIMILARITY_MARGIN", RAG_OPERATIONAL_SIMILARITY_MARGIN, min_val=0.0, max_val=0.5)
    _check_range("RAG_MAX_REGEN_ATTEMPTS", RAG_MAX_REGEN_ATTEMPTS, min_val=0, max_val=3)
    _check_range("RAG_FEEDBACK_TOP_K", RAG_FEEDBACK_TOP_K, min_val=1, max_val=20)
    _check_range("RERANKER_MAX_CANDIDATES", RERANKER_MAX_CANDIDATES, min_val=2, max_val=80)
    _check_range("RERANKER_MIN_TRIGGER_SIM", RERANKER_MIN_TRIGGER_SIM, min_val=0.0, max_val=1.0)
    _check_range("RERANKER_MAX_TRIGGER_SIM", RERANKER_MAX_TRIGGER_SIM, min_val=0.0, max_val=1.0)
    _check_range("BUSINESS_RULES_MAX_CHARS", BUSINESS_RULES_MAX_CHARS, min_val=500, max_val=40000)
    _check_range("COOLDOWN_SECONDS", COOLDOWN_SECONDS, min_val=0)
    _check_range("ASK_TIMEOUT_SECONDS", ASK_TIMEOUT_SECONDS, min_val=5)
    _check_range("MAX_HISTORY_PAIRS", MAX_HISTORY_PAIRS, min_val=1)
    _check_range("EMBEDDING_BATCH_SIZE", EMBEDDING_BATCH_SIZE, min_val=1, max_val=100)
    _check_range("SIMILARITY_FLOOR_FACTOR", SIMILARITY_FLOOR_FACTOR, min_val=0.1, max_val=1.0)
    _check_range("SECTION_MATCH_COUNT", SECTION_MATCH_COUNT, min_val=1, max_val=50)
    _check_range("SECTION_FETCH_LIMIT", SECTION_FETCH_LIMIT, min_val=SECTION_MATCH_COUNT, max_val=200)
    _check_range("CHUNK_FETCH_LIMIT", CHUNK_FETCH_LIMIT, min_val=MAX_CONTEXT_CHUNKS, max_val=300)
    _check_range("MAX_CHUNKS_PER_SECTION", MAX_CHUNKS_PER_SECTION, min_val=1, max_val=10)
    _check_range("MAX_CHUNKS_PER_DOCUMENT", MAX_CHUNKS_PER_DOCUMENT, min_val=1, max_val=20)
    _check_range("DB_POOL_MIN_SIZE", DB_POOL_MIN_SIZE, min_val=1, max_val=100)
    _check_range("DB_POOL_MAX_SIZE", DB_POOL_MAX_SIZE, min_val=DB_POOL_MIN_SIZE, max_val=200)
    _check_range("DB_POOL_TIMEOUT_SECONDS", DB_POOL_TIMEOUT_SECONDS, min_val=1.0, max_val=120.0)
    _check_range("DB_STATEMENT_TIMEOUT_MS", DB_STATEMENT_TIMEOUT_MS, min_val=0, max_val=600000)
    _check_range("DB_LOCK_TIMEOUT_MS", DB_LOCK_TIMEOUT_MS, min_val=0, max_val=600000)
    _check_range("DB_IDLE_IN_TRANSACTION_TIMEOUT_MS", DB_IDLE_IN_TRANSACTION_TIMEOUT_MS, min_val=0, max_val=600000)
    _check_range("CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS", CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS, min_val=1000, max_val=2000000)
    _check_range("CONTEXTUAL_RETRIEVAL_BATCH_SIZE", CONTEXTUAL_RETRIEVAL_BATCH_SIZE, min_val=1, max_val=200)
    _check_range("OPENAI_MAX_OUTPUT_TOKENS", OPENAI_MAX_OUTPUT_TOKENS, min_val=256, max_val=32768)

    if RERANKER_MIN_TRIGGER_SIM > RERANKER_MAX_TRIGGER_SIM:
        raise EnvironmentError(
            "RERANKER_MIN_TRIGGER_SIM deve ser <= RERANKER_MAX_TRIGGER_SIM"
        )

    if RAG_ENABLE_BUSINESS_RULES:
        rules_path = Path(BUSINESS_RULES_FILE)
        if not rules_path.exists() or not rules_path.is_file():
            raise EnvironmentError(
                "RAG_ENABLE_BUSINESS_RULES=true, mas BUSINESS_RULES_FILE nao existe "
                f"ou nao e arquivo: {BUSINESS_RULES_FILE}"
            )


def validate_teams_manifest():
    """Valida as variaveis necessarias para gerar o pacote do Microsoft Teams."""
    required = _required_teams_manifest()
    missing = [name for name, val in required.items() if not val]
    if missing:
        raise EnvironmentError(
            "Variaveis de ambiente obrigatorias para gerar o pacote do Teams nao definidas: "
            f"{', '.join(missing)}. Verifique seu arquivo .env"
        )

    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", TEAMS_MANIFEST_ACCENT_COLOR or ""):
        raise EnvironmentError(
            "TEAMS_MANIFEST_ACCENT_COLOR deve estar no formato #RRGGBB. "
            f"Valor recebido: {TEAMS_MANIFEST_ACCENT_COLOR!r}"
        )


def get_teams_manifest_context() -> dict[str, str]:
    """Retorna os valores usados para preencher o template do manifest do Teams."""
    validate_teams_manifest()
    return {
        "TEAMS_APP_ID": TEAMS_APP_ID,
        "TEAMS_MANIFEST_SHORT_NAME": TEAMS_MANIFEST_SHORT_NAME,
        "TEAMS_MANIFEST_FULL_NAME": TEAMS_MANIFEST_FULL_NAME,
        "TEAMS_MANIFEST_SHORT_DESCRIPTION": TEAMS_MANIFEST_SHORT_DESCRIPTION,
        "TEAMS_MANIFEST_FULL_DESCRIPTION": TEAMS_MANIFEST_FULL_DESCRIPTION,
        "TEAMS_MANIFEST_DEVELOPER_NAME": TEAMS_MANIFEST_DEVELOPER_NAME,
        "TEAMS_MANIFEST_DEVELOPER_WEBSITE_URL": TEAMS_MANIFEST_DEVELOPER_WEBSITE_URL,
        "TEAMS_MANIFEST_DEVELOPER_PRIVACY_URL": TEAMS_MANIFEST_DEVELOPER_PRIVACY_URL,
        "TEAMS_MANIFEST_DEVELOPER_TERMS_URL": TEAMS_MANIFEST_DEVELOPER_TERMS_URL,
        "TEAMS_MANIFEST_ACCENT_COLOR": TEAMS_MANIFEST_ACCENT_COLOR,
    }
