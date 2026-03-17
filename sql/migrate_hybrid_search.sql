-- ==============================================
-- MIGRACAO: Busca Hibrida (Vetor + Full-Text Search)
-- Execute este SQL no Supabase SQL Editor APOS o setup inicial.
-- Nao destroi dados existentes — apenas adiciona funcionalidade.
-- ==============================================

-- 1. Adicionar coluna tsvector para full-text search (portugues)
-- A coluna e gerada automaticamente a partir do conteudo do chunk.
ALTER TABLE document_chunks
ADD COLUMN IF NOT EXISTS fts tsvector
GENERATED ALWAYS AS (to_tsvector('portuguese', content)) STORED;

-- 2. Criar indice GIN para buscas full-text rapidas
CREATE INDEX IF NOT EXISTS document_chunks_fts_idx
ON document_chunks USING gin(fts);

-- 3. Dropar funcao antiga hybrid_match_chunks se existir
DROP FUNCTION IF EXISTS hybrid_match_chunks(vector, text, integer, double precision, float, float);

-- 4. Criar funcao de busca hibrida com Reciprocal Rank Fusion (RRF)
-- Combina resultados de busca vetorial e full-text search.
-- RRF formula: score = sum(1 / (k + rank)) onde k=60 (constante padrao)
CREATE OR REPLACE FUNCTION hybrid_match_chunks(
    query_embedding VECTOR(1536),
    query_text TEXT,
    match_count INT DEFAULT 8,
    match_threshold FLOAT DEFAULT 0.55,
    vector_weight FLOAT DEFAULT 0.6,
    fts_weight FLOAT DEFAULT 0.4
)
RETURNS TABLE (
    id UUID,
    document_id UUID,
    content TEXT,
    chunk_index INTEGER,
    metadata JSONB,
    filename TEXT,
    similarity FLOAT
)
LANGUAGE plpgsql
AS $$
DECLARE
    rrf_k CONSTANT INT := 60;  -- constante RRF (valor padrao da literatura)
    fetch_limit CONSTANT INT := 30;  -- buscar mais candidatos para depois filtrar
BEGIN
    PERFORM set_config('hnsw.ef_search', '100', true);

    RETURN QUERY

    -- CTE 1: Busca vetorial (semantica)
    WITH vector_results AS (
        SELECT
            dc.id,
            ROW_NUMBER() OVER (ORDER BY dc.embedding <=> query_embedding ASC) AS rank_pos,
            (1 - (dc.embedding <=> query_embedding))::FLOAT AS vec_similarity
        FROM document_chunks dc
        WHERE 1 - (dc.embedding <=> query_embedding) >= match_threshold * 0.7  -- threshold mais relaxado para over-retrieve
        ORDER BY dc.embedding <=> query_embedding ASC
        LIMIT fetch_limit
    ),

    -- CTE 2: Busca full-text (keyword)
    fts_results AS (
        SELECT
            dc.id,
            ROW_NUMBER() OVER (ORDER BY ts_rank_cd(dc.fts, plainto_tsquery('portuguese', query_text)) DESC) AS rank_pos,
            ts_rank_cd(dc.fts, plainto_tsquery('portuguese', query_text))::FLOAT AS fts_rank
        FROM document_chunks dc
        WHERE dc.fts @@ plainto_tsquery('portuguese', query_text)
        ORDER BY ts_rank_cd(dc.fts, plainto_tsquery('portuguese', query_text)) DESC
        LIMIT fetch_limit
    ),

    -- CTE 3: Combinar com RRF (Reciprocal Rank Fusion)
    combined AS (
        SELECT
            COALESCE(vr.id, fr.id) AS chunk_id,
            -- RRF score: peso * (1 / (k + rank)) para cada fonte
            COALESCE(vector_weight * (1.0 / (rrf_k + vr.rank_pos)), 0) +
            COALESCE(fts_weight * (1.0 / (rrf_k + fr.rank_pos)), 0) AS rrf_score,
            COALESCE(vr.vec_similarity, 0)::FLOAT AS vec_similarity
        FROM vector_results vr
        FULL OUTER JOIN fts_results fr ON vr.id = fr.id
    ),

    -- CTE 4: Ranquear e pegar top resultados
    top_matches AS (
        SELECT
            c.chunk_id,
            c.rrf_score,
            c.vec_similarity
        FROM combined c
        ORDER BY c.rrf_score DESC
        LIMIT match_count
    ),

    -- CTE 5: Expandir com chunks vizinhos (mesma logica do match_chunks original)
    neighbor_indices AS (
        SELECT DISTINCT dc.document_id AS doc_id, ni.idx
        FROM top_matches tm
        JOIN document_chunks dc ON dc.id = tm.chunk_id
        CROSS JOIN LATERAL (
            VALUES (dc.chunk_index - 1), (dc.chunk_index), (dc.chunk_index + 1)
        ) AS ni(idx)
        WHERE ni.idx >= 0
    ),

    expanded AS (
        SELECT
            dc.id,
            dc.document_id,
            dc.content,
            dc.chunk_index,
            dc.metadata,
            d.filename,
            COALESCE(
                tm.rrf_score,
                (
                    -- Vizinhos herdam 90% do score do chunk adjacente
                    SELECT MAX(tm2.rrf_score) * 0.90
                    FROM top_matches tm2
                    JOIN document_chunks dc2 ON dc2.id = tm2.chunk_id
                    WHERE dc2.document_id = dc.document_id
                      AND ABS(dc2.chunk_index - dc.chunk_index) = 1
                )
            )::FLOAT AS similarity
        FROM neighbor_indices ni
        JOIN document_chunks dc ON dc.document_id = ni.doc_id AND dc.chunk_index = ni.idx
        JOIN documents d ON d.id = dc.document_id
        LEFT JOIN top_matches tm ON tm.chunk_id = dc.id
    )

    -- Retornar resultados unicos ordenados por relevancia
    SELECT DISTINCT ON (e.id)
        e.id,
        e.document_id,
        e.content,
        e.chunk_index,
        e.metadata,
        e.filename,
        e.similarity
    FROM expanded e
    WHERE e.similarity IS NOT NULL
    ORDER BY e.id, e.similarity DESC;
END;
$$;
