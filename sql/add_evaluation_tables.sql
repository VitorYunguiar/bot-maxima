-- Tabelas para benchmark offline de qualidade de respostas RAG.

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS evaluation_runs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    run_type TEXT NOT NULL DEFAULT 'offline',
    dataset_name TEXT NOT NULL,
    model TEXT NOT NULL,
    embedding_model TEXT NOT NULL,
    total_cases INTEGER NOT NULL DEFAULT 0,
    created_by TEXT,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS evaluation_runs_created_at_idx
ON evaluation_runs(created_at DESC);

CREATE TABLE IF NOT EXISTS evaluation_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    run_id UUID NOT NULL REFERENCES evaluation_runs(id) ON DELETE CASCADE,
    case_id TEXT NOT NULL,
    question TEXT NOT NULL,
    expected_behavior TEXT NOT NULL,
    expected_intent TEXT,
    predicted_intent TEXT,
    abstained BOOLEAN NOT NULL DEFAULT FALSE,
    citation_ok BOOLEAN NOT NULL DEFAULT FALSE,
    grounded BOOLEAN NOT NULL DEFAULT FALSE,
    top_similarity FLOAT,
    latency_ms INTEGER,
    score FLOAT NOT NULL DEFAULT 0,
    trace JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS evaluation_results_run_idx
ON evaluation_results(run_id);

CREATE INDEX IF NOT EXISTS evaluation_results_case_idx
ON evaluation_results(case_id);

CREATE OR REPLACE VIEW evaluation_run_summary AS
SELECT
    r.id AS run_id,
    r.dataset_name,
    r.model,
    r.embedding_model,
    r.total_cases,
    r.created_at,
    AVG(er.score)::FLOAT AS avg_score,
    AVG(CASE WHEN er.grounded THEN 1 ELSE 0 END)::FLOAT AS grounded_rate,
    AVG(CASE WHEN er.citation_ok THEN 1 ELSE 0 END)::FLOAT AS citation_ok_rate,
    AVG(CASE WHEN er.abstained THEN 1 ELSE 0 END)::FLOAT AS abstain_rate
FROM evaluation_runs r
LEFT JOIN evaluation_results er ON er.run_id = r.id
GROUP BY r.id, r.dataset_name, r.model, r.embedding_model, r.total_cases, r.created_at;

NOTIFY pgrst, 'reload schema';
