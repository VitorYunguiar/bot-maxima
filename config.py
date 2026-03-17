"""
config.py - Configuracoes centralizadas carregadas do .env
"""

import os
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
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001")
EMBEDDING_DIMENSIONS = _env_int("EMBEDDING_DIMENSIONS", 1536)
EMBEDDING_BATCH_SIZE = _env_int("EMBEDDING_BATCH_SIZE", 10)
EMBEDDING_MAX_RETRIES = _env_int("EMBEDDING_MAX_RETRIES", 8)
EMBEDDING_RETRY_BASE_SECONDS = _env_float("EMBEDDING_RETRY_BASE_SECONDS", 5.0)
EMBEDDING_RETRY_MAX_SECONDS = _env_float("EMBEDDING_RETRY_MAX_SECONDS", 65.0)
EMBEDDING_MIN_INTERVAL_SECONDS = _env_float("EMBEDDING_MIN_INTERVAL_SECONDS", 0.5)
EMBEDDING_RETRY_JITTER_SECONDS = _env_float("EMBEDDING_RETRY_JITTER_SECONDS", 0.5)

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

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
    "./documentos/00-REGRAS-NEGOCIO-MAXPEDIDO.md",
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

# Contextual Retrieval (enriquecimento de chunks — tecnica Anthropic)
CONTEXTUAL_RETRIEVAL_ENABLED = _env_bool("CONTEXTUAL_RETRIEVAL_ENABLED", True)
CONTEXTUAL_RETRIEVAL_MODEL = os.getenv("CONTEXTUAL_RETRIEVAL_MODEL", "gemini-2.5-flash")
CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS = _env_int("CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS", 500000)
CONTEXTUAL_RETRIEVAL_MAX_TOKENS = _env_int("CONTEXTUAL_RETRIEVAL_MAX_TOKENS", 150)

# Ingestao web (URLs)
WEB_FETCH_TIMEOUT_SECONDS = _env_float("WEB_FETCH_TIMEOUT_SECONDS", 20.0)
WEB_USER_AGENT = os.getenv("WEB_USER_AGENT", "BotMaximaRAG/1.0")
WEB_MAX_TEXT_CHARS = _env_int("WEB_MAX_TEXT_CHARS", 400000)
URLS_FILE_DEFAULT = os.getenv("URLS_FILE_DEFAULT", "./documentos/urls.txt")
URL_REVIEW_OUTPUT_DIR = os.getenv("URL_REVIEW_OUTPUT_DIR", "./documentos/_pendentes_url")

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
        "\"Nao encontrei essa informacao na base de conhecimento. Recomendo abrir um chamado ou consultar a equipe N2.\"\n"
        "- Se a documentacao cobrir apenas PARTE da pergunta, responda so a parte documentada e diga claramente o que nao foi encontrado.\n"
        "- Na duvida, NAO responda. E melhor dizer que nao sabe do que dar uma informacao errada.\n\n"
        "## Regras de resposta\n"
        "- Responda SOMENTE com base nos documentos fornecidos como contexto.\n"
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

# Microsoft Teams (sem defaults — credenciais devem estar no .env)
TEAMS_APP_ID = os.getenv("TEAMS_APP_ID")
TEAMS_APP_PASSWORD = os.getenv("TEAMS_APP_PASSWORD")
TEAMS_TENANT_ID = os.getenv("TEAMS_TENANT_ID")
TEAMS_PORT = _env_int("TEAMS_PORT", 3978)

# Bot - limites
COOLDOWN_SECONDS = _env_float("COOLDOWN_SECONDS", 10.0)
ASK_TIMEOUT_SECONDS = _env_float("ASK_TIMEOUT_SECONDS", 120.0)
MAX_HISTORY_PAIRS = _env_int("MAX_HISTORY_PAIRS", 20)
MAX_HISTORY_CHANNELS = _env_int("MAX_HISTORY_CHANNELS", 100)
MAX_QUESTION_LENGTH = _env_int("MAX_QUESTION_LENGTH", 4000)
MAX_IMAGE_SIZE_MB = _env_int("MAX_IMAGE_SIZE_MB", 20)
MAX_IMAGES_PER_MESSAGE = _env_int("MAX_IMAGES_PER_MESSAGE", 5)
ASK_MAX_TOKENS = _env_int("ASK_MAX_TOKENS", 8192)
CONFIDENCE_THRESHOLD = _env_float("CONFIDENCE_THRESHOLD", 0.65)
DISCORD_MSG_LIMIT = _env_int("DISCORD_MSG_LIMIT", 1990)
TEAMS_MSG_LIMIT = _env_int("TEAMS_MSG_LIMIT", 25000)

# Derivados
MAX_IMAGE_SIZE_BYTES = MAX_IMAGE_SIZE_MB * 1024 * 1024

# Diretorio de documentos
DOCS_DIR = os.getenv("DOCS_DIR", "./documentos")
FAILED_INGEST_REPORT = os.getenv("FAILED_INGEST_REPORT", "./ingest_failures.json")

_ALLOWED_EMBEDDING_DIMENSIONS = {1536, 3072}
if EMBEDDING_DIMENSIONS not in _ALLOWED_EMBEDDING_DIMENSIONS:
    raise EnvironmentError(
        "EMBEDDING_DIMENSIONS deve ser 1536 ou 3072. "
        "Ajuste o .env e execute o SQL correspondente (sql/setup_1536.sql ou sql/setup.sql)."
    )


# Validacao
_REQUIRED_SHARED = {
    "GEMINI_API_KEY": GEMINI_API_KEY,
    "SUPABASE_URL": SUPABASE_URL,
    "SUPABASE_SERVICE_KEY": SUPABASE_SERVICE_KEY,
}

_REQUIRED_DISCORD = {
    "DISCORD_TOKEN": DISCORD_TOKEN,
}

_REQUIRED_TEAMS = {
    "TEAMS_APP_ID": TEAMS_APP_ID,
    "TEAMS_APP_PASSWORD": TEAMS_APP_PASSWORD,
    "TEAMS_TENANT_ID": TEAMS_TENANT_ID,
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
    required = dict(_REQUIRED_SHARED)
    if platform == "discord":
        required.update(_REQUIRED_DISCORD)
    elif platform == "teams":
        required.update(_REQUIRED_TEAMS)

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
    _check_range("BUSINESS_RULES_MAX_CHARS", BUSINESS_RULES_MAX_CHARS, min_val=500, max_val=40000)
    _check_range("COOLDOWN_SECONDS", COOLDOWN_SECONDS, min_val=0)
    _check_range("ASK_TIMEOUT_SECONDS", ASK_TIMEOUT_SECONDS, min_val=5)
    _check_range("MAX_HISTORY_PAIRS", MAX_HISTORY_PAIRS, min_val=1)
    _check_range("EMBEDDING_BATCH_SIZE", EMBEDDING_BATCH_SIZE, min_val=1, max_val=100)
    _check_range("SIMILARITY_FLOOR_FACTOR", SIMILARITY_FLOOR_FACTOR, min_val=0.1, max_val=1.0)
    _check_range("CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS", CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS, min_val=1000, max_val=32000)
