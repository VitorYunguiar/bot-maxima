-- ==============================================
-- MIGRACAO: Adicionar coluna priority na tabela documents
-- Rode este SQL no Supabase SQL Editor
-- ==============================================

-- Adicionar coluna de prioridade (default 5 = normal)
ALTER TABLE documents ADD COLUMN IF NOT EXISTS priority INTEGER DEFAULT 5;

-- Atualizar prioridades dos documentos existentes
-- 10 = Core MDs (documentos estruturados principais)
UPDATE documents SET priority = 10
WHERE filename SIMILAR TO '0[0-5]-%' AND doc_type = 'md';

-- 8 = Documentos estruturados de suporte
UPDATE documents SET priority = 8
WHERE filename IN (
    'SERVICE-DESK-PROCESSOS.md',
    'SERVICE_DESK_MAXIMA_ORGANIZADO.md',
    'GLOSSARIO.MD',
    'base-maxgestao.md',
    'ARTIGOS_BASE.md'
);

-- 3 = Documentos muito grandes (penalizar para nao dominar resultados)
UPDATE documents SET priority = 3
WHERE chunk_count > 400;

-- Verificar resultado
SELECT filename, doc_type, chunk_count, priority
FROM documents
ORDER BY priority DESC, filename;
