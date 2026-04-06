# Regras Base

Arquivo bootstrap versionado para permitir que o projeto suba em uma maquina nova
mesmo antes da copia da pasta `documentos/`.

Uso recomendado:

- mantenha este arquivo como fallback no GitHub
- se houver uma base documental local da Maxima, ajuste `BUSINESS_RULES_FILE` no `.env`
  para apontar para o documento principal real
- se a pasta `documentos/` for copiada para a maquina nova, voce pode usar o arquivo
  real em vez deste bootstrap

Este arquivo existe apenas para evitar falha de inicializacao quando
`RAG_ENABLE_BUSINESS_RULES=true`.
