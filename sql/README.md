# SQL setup for embedding dimensions

Choose one schema and keep it aligned with `.env`:

- `sql/setup_1536.sql` -> `VECTOR(1536)` (recommended default)
- `sql/setup.sql` -> `VECTOR(3072)` (higher quality, only if your pgvector accepts 3072)

After running one SQL script in PostgreSQL, set the same value in `.env`:

```env
EMBEDDING_DIMENSIONS=1536
```

or

```env
EMBEDDING_DIMENSIONS=3072
```

Then re-run ingestion to regenerate all embeddings.

If your PostgreSQL/pgvector setup rejects `VECTOR(3072)`, use `1536`.

## Additional migrations

After the base setup script, run optional migrations according to the features you use:

- `sql/migrate_hybrid_search.sql`: enables hybrid search RPC `hybrid_match_chunks`.
- `sql/add_knowledge_gaps.sql`: creates `knowledge_gaps` table and RPCs:
  - `upsert_knowledge_gap`
  - `get_top_knowledge_gaps`
- `sql/add_feedback_memory.sql`: creates reviewed correction memory tables + RPCs:
  - `submit_feedback`
  - `list_pending_feedback`
  - `approve_feedback`
  - `reject_feedback`
  - `publish_feedback`
  - `search_feedback_chunks`
- `sql/add_evaluation_tables.sql`: creates benchmark tables:
  - `evaluation_runs`
  - `evaluation_results`
  - `evaluation_run_summary` (view)

In Docker, the local PostgreSQL bootstrap runs these scripts automatically on the first startup of the `postgres` service.
