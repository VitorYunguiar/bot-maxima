-- Tabela para rastrear queries sem resposta (knowledge gaps).
-- Permite ao time de documentacao priorizar conteudo faltante.

CREATE TABLE IF NOT EXISTS knowledge_gaps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    query TEXT NOT NULL,
    max_similarity FLOAT DEFAULT 0,
    platform TEXT,
    occurrences INTEGER DEFAULT 1,
    first_seen TIMESTAMPTZ DEFAULT NOW(),
    last_seen TIMESTAMPTZ DEFAULT NOW(),
    resolved BOOLEAN DEFAULT FALSE
);

-- Indice para consultar gaps mais frequentes
CREATE INDEX IF NOT EXISTS knowledge_gaps_occurrences_idx
ON knowledge_gaps(occurrences DESC)
WHERE resolved = FALSE;

-- Indice para buscar gap existente por query
CREATE INDEX IF NOT EXISTS knowledge_gaps_query_idx
ON knowledge_gaps(query);

-- Funcao para registrar ou incrementar um knowledge gap
CREATE OR REPLACE FUNCTION public.upsert_knowledge_gap(
    p_query TEXT,
    p_max_similarity FLOAT DEFAULT 0,
    p_platform TEXT DEFAULT 'discord'
)
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO knowledge_gaps (query, max_similarity, platform, occurrences, first_seen, last_seen)
    VALUES (p_query, p_max_similarity, p_platform, 1, NOW(), NOW())
    ON CONFLICT (query)
    DO UPDATE SET
        occurrences = knowledge_gaps.occurrences + 1,
        last_seen = NOW(),
        max_similarity = GREATEST(knowledge_gaps.max_similarity, EXCLUDED.max_similarity),
        platform = EXCLUDED.platform;
END;
$$;

-- Constraint unique na query para o upsert funcionar (idempotente)
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'knowledge_gaps_query_unique'
    ) THEN
        ALTER TABLE knowledge_gaps
        ADD CONSTRAINT knowledge_gaps_query_unique UNIQUE (query);
    END IF;
END;
$$;

-- Funcao para listar top N knowledge gaps nao resolvidos
CREATE OR REPLACE FUNCTION public.get_top_knowledge_gaps(
    p_limit INT DEFAULT 10
)
RETURNS TABLE (
    query TEXT,
    occurrences INTEGER,
    max_similarity FLOAT,
    platform TEXT,
    last_seen TIMESTAMPTZ
)
LANGUAGE sql
AS $$
    SELECT query, occurrences, max_similarity, platform, last_seen
    FROM knowledge_gaps
    WHERE resolved = FALSE
    ORDER BY occurrences DESC
    LIMIT p_limit;
$$;

-- Garantir visibilidade imediata das funcoes no PostgREST (Supabase REST /rpc)
NOTIFY pgrst, 'reload schema';
