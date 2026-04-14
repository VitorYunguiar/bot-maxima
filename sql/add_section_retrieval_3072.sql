-- Section-aware retrieval layer for 3072-dimensional embeddings.
-- Extends analytical context with:
-- - retrieval_text/embedding/fts in document_sections
-- - indexable retrieval columns in document_chunks
-- - section-aware RPCs with fetch_limit and optional section filtering

CREATE EXTENSION IF NOT EXISTS vector;

ALTER TABLE documents
ADD COLUMN IF NOT EXISTS priority INTEGER DEFAULT 5;

ALTER TABLE document_sections
ADD COLUMN IF NOT EXISTS retrieval_text TEXT;

ALTER TABLE document_sections
ADD COLUMN IF NOT EXISTS embedding VECTOR(3072);

ALTER TABLE document_sections
ADD COLUMN IF NOT EXISTS fts tsvector GENERATED ALWAYS AS (
    to_tsvector('portuguese', COALESCE(retrieval_text, ''))
) STORED;

CREATE INDEX IF NOT EXISTS document_sections_embedding_hnsw_idx
ON document_sections
USING hnsw (embedding vector_cosine_ops)
WITH (m = 24, ef_construction = 128);

CREATE INDEX IF NOT EXISTS document_sections_fts_idx
ON document_sections USING gin(fts);

ALTER TABLE document_chunks
ADD COLUMN IF NOT EXISTS module TEXT;

ALTER TABLE document_chunks
ADD COLUMN IF NOT EXISTS doc_type TEXT;

ALTER TABLE document_chunks
ADD COLUMN IF NOT EXISTS source_type TEXT;

ALTER TABLE document_chunks
ADD COLUMN IF NOT EXISTS doc_priority INTEGER;

UPDATE document_chunks dc
SET
    module = COALESCE(dc.module, dc.metadata->>'module'),
    doc_type = COALESCE(dc.doc_type, d.doc_type, dc.metadata->>'doc_type'),
    source_type = COALESCE(dc.source_type, dc.metadata->>'source_type'),
    doc_priority = COALESCE(
        dc.doc_priority,
        CASE
            WHEN COALESCE(dc.metadata->>'doc_priority', '') ~ '^-?[0-9]+$'
                THEN (dc.metadata->>'doc_priority')::INTEGER
            ELSE NULL
        END,
        d.priority,
        5
    )
FROM documents d
WHERE d.id = dc.document_id;

CREATE INDEX IF NOT EXISTS document_chunks_module_idx
ON document_chunks(module);

CREATE INDEX IF NOT EXISTS document_chunks_doc_type_idx
ON document_chunks(doc_type);

CREATE INDEX IF NOT EXISTS document_chunks_source_type_idx
ON document_chunks(source_type);

CREATE INDEX IF NOT EXISTS document_chunks_doc_priority_idx
ON document_chunks(doc_priority DESC);

CREATE INDEX IF NOT EXISTS document_chunks_section_doc_chunk_idx
ON document_chunks(section_id, document_id, chunk_index);

DROP FUNCTION IF EXISTS public.match_chunks(vector, integer, double precision, text[], text[], uuid[], integer);
DROP FUNCTION IF EXISTS public.match_chunks(vector, integer, real, text[], text[], uuid[], integer);
DROP FUNCTION IF EXISTS public.hybrid_match_chunks(vector, text, integer, double precision, double precision, double precision, text[], text[], uuid[], integer);
DROP FUNCTION IF EXISTS public.hybrid_match_chunks(vector, text, integer, real, real, real, text[], text[], uuid[], integer);
DROP FUNCTION IF EXISTS public.hybrid_match_sections(vector, text, integer, double precision, double precision, double precision, text[], text[], integer);
DROP FUNCTION IF EXISTS public.hybrid_match_sections(vector, text, integer, real, real, real, text[], text[], integer);

CREATE OR REPLACE FUNCTION public.match_chunks(
    query_embedding VECTOR(3072),
    match_count INT DEFAULT 8,
    match_threshold FLOAT DEFAULT 0.55,
    filter_doc_types TEXT[] DEFAULT NULL,
    filter_modules TEXT[] DEFAULT NULL,
    filter_section_ids UUID[] DEFAULT NULL,
    fetch_limit INT DEFAULT 80
)
RETURNS TABLE (
    id UUID,
    document_id UUID,
    content TEXT,
    chunk_index INTEGER,
    metadata JSONB,
    filename TEXT,
    similarity FLOAT,
    section_id UUID,
    heading_path TEXT,
    semantic_context TEXT,
    entities JSONB,
    answer_mode TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    safe_fetch_limit INT := GREATEST(fetch_limit, match_count);
    max_expanded INT := GREATEST(match_count * 2, match_count);
BEGIN
    PERFORM set_config('hnsw.ef_search', GREATEST(100, safe_fetch_limit)::TEXT, true);

    RETURN QUERY
    WITH section_scope AS (
        SELECT DISTINCT neighbor.id AS section_id
        FROM document_sections seed
        JOIN document_sections neighbor
          ON neighbor.document_id = seed.document_id
         AND neighbor.section_index BETWEEN seed.section_index - 1 AND seed.section_index + 1
        WHERE COALESCE(array_length(filter_section_ids, 1), 0) > 0
          AND seed.id = ANY(filter_section_ids)
    ),
    base_chunks AS (
        SELECT
            dc.id,
            dc.document_id,
            dc.content,
            dc.chunk_index,
            dc.metadata,
            dc.embedding,
            d.filename,
            dc.section_id,
            COALESCE(dc.heading_path, ds.heading_path, dc.metadata->>'heading_path', '') AS heading_path,
            COALESCE(dc.semantic_context, ds.semantic_context, dc.metadata->>'semantic_context', '') AS semantic_context,
            COALESCE(NULLIF(dc.entities, '{}'::jsonb), ds.entities, dc.metadata->'entities', '{}'::jsonb) AS entities,
            COALESCE(dc.answer_mode, ds.answer_mode, dc.metadata->>'answer_mode', 'general') AS answer_mode
        FROM document_chunks dc
        JOIN documents d ON d.id = dc.document_id
        LEFT JOIN document_sections ds ON ds.id = dc.section_id
        WHERE (
            COALESCE(array_length(filter_doc_types, 1), 0) = 0
            OR COALESCE(dc.doc_type, d.doc_type, dc.metadata->>'doc_type', '') = ANY(filter_doc_types)
        )
        AND (
            COALESCE(array_length(filter_modules, 1), 0) = 0
            OR COALESCE(dc.module, ds.module, dc.metadata->>'module', '') = ANY(filter_modules)
            OR (
                COALESCE(dc.module, ds.module, dc.metadata->>'module', '') = ''
                AND NOT (dc.metadata ? 'module')
            )
        )
        AND (
            COALESCE(array_length(filter_section_ids, 1), 0) = 0
            OR dc.section_id IN (SELECT section_id FROM section_scope)
        )
    ),
    top_matches AS (
        SELECT
            bc.id,
            bc.document_id,
            bc.content,
            bc.chunk_index,
            bc.metadata,
            bc.filename,
            (1 - (bc.embedding <=> query_embedding))::FLOAT AS similarity
        FROM base_chunks bc
        WHERE 1 - (bc.embedding <=> query_embedding) >= match_threshold
        ORDER BY bc.embedding <=> query_embedding ASC
        LIMIT safe_fetch_limit
    ),
    top_ranked AS (
        SELECT *
        FROM top_matches
        ORDER BY similarity DESC
        LIMIT match_count
    ),
    neighbor_indices AS (
        SELECT DISTINCT tm.document_id AS doc_id, ni.idx
        FROM top_ranked tm
        CROSS JOIN LATERAL (
            VALUES (tm.chunk_index - 1), (tm.chunk_index), (tm.chunk_index + 1)
        ) AS ni(idx)
        WHERE ni.idx >= 0
    ),
    expanded AS (
        SELECT
            bc.id,
            bc.document_id,
            bc.content,
            bc.chunk_index,
            bc.metadata,
            bc.filename,
            COALESCE(
                tm.similarity,
                (
                    SELECT MAX(tm2.similarity) * 0.90
                    FROM top_ranked tm2
                    WHERE tm2.document_id = bc.document_id
                      AND ABS(tm2.chunk_index - bc.chunk_index) = 1
                )
            )::FLOAT AS similarity,
            bc.section_id,
            bc.heading_path,
            bc.semantic_context,
            bc.entities,
            bc.answer_mode
        FROM neighbor_indices ni
        JOIN base_chunks bc ON bc.document_id = ni.doc_id AND bc.chunk_index = ni.idx
        LEFT JOIN top_ranked tm ON tm.id = bc.id
    )
    SELECT
        f.id,
        f.document_id,
        f.content,
        f.chunk_index,
        f.metadata,
        f.filename,
        f.similarity,
        f.section_id,
        f.heading_path,
        f.semantic_context,
        f.entities,
        f.answer_mode
    FROM (
        SELECT DISTINCT ON (e.id)
            e.id,
            e.document_id,
            e.content,
            e.chunk_index,
            e.metadata,
            e.filename,
            e.similarity,
            e.section_id,
            e.heading_path,
            e.semantic_context,
            e.entities,
            e.answer_mode
        FROM expanded e
        WHERE e.similarity IS NOT NULL
        ORDER BY e.id, e.similarity DESC
    ) f
    ORDER BY f.similarity DESC
    LIMIT max_expanded;
END;
$$;

CREATE OR REPLACE FUNCTION public.hybrid_match_chunks(
    query_embedding VECTOR(3072),
    query_text TEXT,
    match_count INT DEFAULT 8,
    match_threshold FLOAT DEFAULT 0.55,
    vector_weight FLOAT DEFAULT 0.6,
    fts_weight FLOAT DEFAULT 0.4,
    filter_doc_types TEXT[] DEFAULT NULL,
    filter_modules TEXT[] DEFAULT NULL,
    filter_section_ids UUID[] DEFAULT NULL,
    fetch_limit INT DEFAULT 80
)
RETURNS TABLE (
    id UUID,
    document_id UUID,
    content TEXT,
    chunk_index INTEGER,
    metadata JSONB,
    filename TEXT,
    similarity FLOAT,
    section_id UUID,
    heading_path TEXT,
    semantic_context TEXT,
    entities JSONB,
    answer_mode TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    rrf_k CONSTANT INT := 60;
    safe_fetch_limit INT := GREATEST(fetch_limit, match_count);
    max_expanded INT := GREATEST(match_count * 2, match_count);
BEGIN
    PERFORM set_config('hnsw.ef_search', GREATEST(100, safe_fetch_limit)::TEXT, true);

    RETURN QUERY
    WITH section_scope AS (
        SELECT DISTINCT neighbor.id AS section_id
        FROM document_sections seed
        JOIN document_sections neighbor
          ON neighbor.document_id = seed.document_id
         AND neighbor.section_index BETWEEN seed.section_index - 1 AND seed.section_index + 1
        WHERE COALESCE(array_length(filter_section_ids, 1), 0) > 0
          AND seed.id = ANY(filter_section_ids)
    ),
    base_chunks AS (
        SELECT
            dc.id,
            dc.document_id,
            dc.content,
            dc.chunk_index,
            dc.metadata,
            dc.embedding,
            dc.fts,
            d.filename,
            dc.section_id,
            COALESCE(dc.heading_path, ds.heading_path, dc.metadata->>'heading_path', '') AS heading_path,
            COALESCE(dc.semantic_context, ds.semantic_context, dc.metadata->>'semantic_context', '') AS semantic_context,
            COALESCE(NULLIF(dc.entities, '{}'::jsonb), ds.entities, dc.metadata->'entities', '{}'::jsonb) AS entities,
            COALESCE(dc.answer_mode, ds.answer_mode, dc.metadata->>'answer_mode', 'general') AS answer_mode
        FROM document_chunks dc
        JOIN documents d ON d.id = dc.document_id
        LEFT JOIN document_sections ds ON ds.id = dc.section_id
        WHERE (
            COALESCE(array_length(filter_doc_types, 1), 0) = 0
            OR COALESCE(dc.doc_type, d.doc_type, dc.metadata->>'doc_type', '') = ANY(filter_doc_types)
        )
        AND (
            COALESCE(array_length(filter_modules, 1), 0) = 0
            OR COALESCE(dc.module, ds.module, dc.metadata->>'module', '') = ANY(filter_modules)
            OR (
                COALESCE(dc.module, ds.module, dc.metadata->>'module', '') = ''
                AND NOT (dc.metadata ? 'module')
            )
        )
        AND (
            COALESCE(array_length(filter_section_ids, 1), 0) = 0
            OR dc.section_id IN (SELECT section_id FROM section_scope)
        )
    ),
    vector_results AS (
        SELECT
            bc.id,
            ROW_NUMBER() OVER (ORDER BY bc.embedding <=> query_embedding ASC) AS rank_pos,
            (1 - (bc.embedding <=> query_embedding))::FLOAT AS vec_similarity
        FROM base_chunks bc
        WHERE 1 - (bc.embedding <=> query_embedding) >= match_threshold * 0.7
        ORDER BY bc.embedding <=> query_embedding ASC
        LIMIT safe_fetch_limit
    ),
    fts_results AS (
        SELECT
            bc.id,
            ROW_NUMBER() OVER (
                ORDER BY ts_rank_cd(bc.fts, websearch_to_tsquery('portuguese', query_text)) DESC
            ) AS rank_pos,
            ts_rank_cd(bc.fts, websearch_to_tsquery('portuguese', query_text))::FLOAT AS fts_rank
        FROM base_chunks bc
        WHERE bc.fts @@ websearch_to_tsquery('portuguese', query_text)
        ORDER BY ts_rank_cd(bc.fts, websearch_to_tsquery('portuguese', query_text)) DESC
        LIMIT safe_fetch_limit
    ),
    combined AS (
        SELECT
            COALESCE(vr.id, fr.id) AS chunk_id,
            COALESCE(vector_weight * (1.0 / (rrf_k + vr.rank_pos)), 0) +
            COALESCE(fts_weight * (1.0 / (rrf_k + fr.rank_pos)), 0) AS rrf_score,
            vr.vec_similarity::FLOAT AS vec_similarity,
            (vr.id IS NOT NULL AND fr.id IS NOT NULL) AS in_both
        FROM vector_results vr
        FULL OUTER JOIN fts_results fr ON vr.id = fr.id
    ),
    top_matches AS (
        SELECT
            c.chunk_id,
            c.rrf_score,
            c.vec_similarity
        FROM combined c
        WHERE c.vec_similarity >= match_threshold * 0.5
           OR c.in_both
        ORDER BY c.rrf_score DESC
        LIMIT match_count
    ),
    neighbor_indices AS (
        SELECT DISTINCT bc.document_id AS doc_id, ni.idx
        FROM top_matches tm
        JOIN base_chunks bc ON bc.id = tm.chunk_id
        CROSS JOIN LATERAL (
            VALUES (bc.chunk_index - 1), (bc.chunk_index), (bc.chunk_index + 1)
        ) AS ni(idx)
        WHERE ni.idx >= 0
    ),
    expanded AS (
        SELECT
            bc.id,
            bc.document_id,
            bc.content,
            bc.chunk_index,
            bc.metadata,
            bc.filename,
            COALESCE(
                tm.vec_similarity,
                (
                    SELECT MAX(tm2.vec_similarity) * 0.90
                    FROM top_matches tm2
                    JOIN base_chunks bc2 ON bc2.id = tm2.chunk_id
                    WHERE bc2.document_id = bc.document_id
                      AND ABS(bc2.chunk_index - bc.chunk_index) = 1
                )
            )::FLOAT AS similarity,
            bc.section_id,
            bc.heading_path,
            bc.semantic_context,
            bc.entities,
            bc.answer_mode
        FROM neighbor_indices ni
        JOIN base_chunks bc ON bc.document_id = ni.doc_id AND bc.chunk_index = ni.idx
        LEFT JOIN top_matches tm ON tm.chunk_id = bc.id
    )
    SELECT
        f.id,
        f.document_id,
        f.content,
        f.chunk_index,
        f.metadata,
        f.filename,
        f.similarity,
        f.section_id,
        f.heading_path,
        f.semantic_context,
        f.entities,
        f.answer_mode
    FROM (
        SELECT DISTINCT ON (e.id)
            e.id,
            e.document_id,
            e.content,
            e.chunk_index,
            e.metadata,
            e.filename,
            e.similarity,
            e.section_id,
            e.heading_path,
            e.semantic_context,
            e.entities,
            e.answer_mode
        FROM expanded e
        WHERE e.similarity IS NOT NULL
        ORDER BY e.id, e.similarity DESC
    ) f
    ORDER BY f.similarity DESC
    LIMIT max_expanded;
END;
$$;

CREATE OR REPLACE FUNCTION public.hybrid_match_sections(
    query_embedding VECTOR(3072),
    query_text TEXT,
    match_count INT DEFAULT 12,
    match_threshold FLOAT DEFAULT 0.55,
    vector_weight FLOAT DEFAULT 0.65,
    fts_weight FLOAT DEFAULT 0.35,
    filter_doc_types TEXT[] DEFAULT NULL,
    filter_modules TEXT[] DEFAULT NULL,
    fetch_limit INT DEFAULT 48
)
RETURNS TABLE (
    id UUID,
    document_id UUID,
    section_index INTEGER,
    heading_path TEXT,
    title TEXT,
    module TEXT,
    answer_mode TEXT,
    semantic_context TEXT,
    entities JSONB,
    retrieval_text TEXT,
    filename TEXT,
    similarity FLOAT
)
LANGUAGE plpgsql
AS $$
DECLARE
    rrf_k CONSTANT INT := 60;
    safe_fetch_limit INT := GREATEST(fetch_limit, match_count);
BEGIN
    PERFORM set_config('hnsw.ef_search', GREATEST(100, safe_fetch_limit)::TEXT, true);

    RETURN QUERY
    WITH base_sections AS (
        SELECT
            ds.id,
            ds.document_id,
            ds.section_index,
            ds.heading_path,
            ds.title,
            COALESCE(ds.module, '') AS module,
            ds.answer_mode,
            ds.semantic_context,
            ds.entities,
            ds.retrieval_text,
            ds.embedding,
            ds.fts,
            d.filename,
            COALESCE(d.doc_type, '') AS doc_type
        FROM document_sections ds
        JOIN documents d ON d.id = ds.document_id
        WHERE (
            COALESCE(array_length(filter_doc_types, 1), 0) = 0
            OR COALESCE(d.doc_type, '') = ANY(filter_doc_types)
        )
        AND (
            COALESCE(array_length(filter_modules, 1), 0) = 0
            OR COALESCE(ds.module, '') = ANY(filter_modules)
            OR COALESCE(ds.module, '') = ''
        )
    ),
    vector_results AS (
        SELECT
            bs.id,
            ROW_NUMBER() OVER (ORDER BY bs.embedding <=> query_embedding ASC) AS rank_pos,
            (1 - (bs.embedding <=> query_embedding))::FLOAT AS vec_similarity
        FROM base_sections bs
        WHERE bs.embedding IS NOT NULL
          AND 1 - (bs.embedding <=> query_embedding) >= match_threshold * 0.65
        ORDER BY bs.embedding <=> query_embedding ASC
        LIMIT safe_fetch_limit
    ),
    fts_results AS (
        SELECT
            bs.id,
            ROW_NUMBER() OVER (
                ORDER BY ts_rank_cd(bs.fts, websearch_to_tsquery('portuguese', query_text)) DESC
            ) AS rank_pos,
            ts_rank_cd(bs.fts, websearch_to_tsquery('portuguese', query_text))::FLOAT AS fts_rank
        FROM base_sections bs
        WHERE bs.fts @@ websearch_to_tsquery('portuguese', query_text)
        ORDER BY ts_rank_cd(bs.fts, websearch_to_tsquery('portuguese', query_text)) DESC
        LIMIT safe_fetch_limit
    ),
    combined AS (
        SELECT
            COALESCE(vr.id, fr.id) AS section_id,
            COALESCE(vector_weight * (1.0 / (rrf_k + vr.rank_pos)), 0) +
            COALESCE(fts_weight * (1.0 / (rrf_k + fr.rank_pos)), 0) AS rrf_score,
            vr.vec_similarity::FLOAT AS vec_similarity,
            (vr.id IS NOT NULL AND fr.id IS NOT NULL) AS in_both
        FROM vector_results vr
        FULL OUTER JOIN fts_results fr ON vr.id = fr.id
    )
    SELECT
        bs.id,
        bs.document_id,
        bs.section_index,
        bs.heading_path,
        bs.title,
        bs.module,
        bs.answer_mode,
        bs.semantic_context,
        bs.entities,
        bs.retrieval_text,
        bs.filename,
        COALESCE(c.vec_similarity, 0.0)::FLOAT AS similarity
    FROM combined c
    JOIN base_sections bs ON bs.id = c.section_id
    WHERE c.vec_similarity >= match_threshold * 0.5
       OR c.in_both
    ORDER BY c.rrf_score DESC, c.vec_similarity DESC
    LIMIT match_count;
END;
$$;

NOTIFY pgrst, 'reload schema';
