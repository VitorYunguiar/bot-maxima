# SQL setup for embedding dimensions

Choose one schema and keep it aligned with `.env`:

- `sql/setup_1536.sql` -> `VECTOR(1536)` (recommended default and usually compatible in Supabase)
- `sql/setup.sql` -> `VECTOR(3072)` (higher quality, only if your pgvector accepts 3072)

After running one SQL script in Supabase, set the same value in `.env`:

```env
EMBEDDING_DIMENSIONS=1536
```

or

```env
EMBEDDING_DIMENSIONS=3072
```

Then re-run ingestion to regenerate all embeddings.

If Supabase rejects `VECTOR(3072)`, use `1536`. This is typically due to pgvector limits in the project instance/version.

## Additional migrations

After the base setup script, run optional migrations according to the features you use:

- `sql/migrate_hybrid_search.sql`: enables hybrid search RPC `hybrid_match_chunks`.
- `sql/add_knowledge_gaps.sql`: creates `knowledge_gaps` table and RPCs:
  - `upsert_knowledge_gap`
  - `get_top_knowledge_gaps`

If these RPCs are missing in Supabase, the bot will receive `404 / PGRST202` from `/rest/v1/rpc/...`.
