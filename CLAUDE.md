# Carrier - Phoenix Web App

## Source of Truth
**Always consult `AGENTS.md` before making code decisions.**
**Always write idiomatic, pattern-matched, efficient, performant code and avoid excess defensive programming**
**Always use English for this project**

## Code Quality - Self Review (MANDATORY)

Before presenting ANY generated or modified code, you MUST internally verify it against ALL criteria below. Do NOT present code that fails any check — fix issues silently before showing the result:

1. **Idiomatic**: Uses language/framework conventions (pattern matching over conditionals, pipe operator, guard clauses, with statements, multi-clause functions)
2. **No redundancy**: No dead code, no repeated logic, no unnecessary variables or intermediate steps, no code that could be collapsed
3. **Efficient**: No N+1 queries, no unnecessary iterations, proper Ecto preloads, bulk operations where applicable
4. **Clean**: No excess defensive programming, no unnecessary nil/error checks on trusted internal data, no verbose conditionals that could be simplified with pattern matching
5. **Consistent**: Follows existing codebase conventions, naming patterns, and module structure
6. **Minimal**: Only the code needed — no over-engineering, no premature abstractions, no "just in case" code paths

The user should NEVER need to ask for a review of code you just generated. If you would find issues reviewing it, fix them first.