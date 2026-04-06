# Bot Maxima

Bot de suporte com RAG para Discord e Microsoft Teams.

## O que vai no GitHub

Este repositório fica pronto para `git clone` em outra maquina, com:

- codigo do bot
- scripts de bootstrap e inicializacao
- `.env.example` completo
- template do manifest do Teams
- fallback versionado para `BUSINESS_RULES_FILE`

Arquivos locais e secretos nao vao para o GitHub:

- `.env`
- `.venv`
- `documentos/`
- `teams_manifest/build/`

## Setup em uma maquina nova

Clone o repositório e rode:

```powershell
setup_maquina.bat
```

Depois preencha o `.env` com as credenciais reais.

## Iniciar

Discord:

```powershell
iniciar.bat
```

Teams:

```powershell
gerar_manifest_teams.bat
iniciar_teams.bat
```

## Teams

O pacote do Teams e gerado a partir do `.env`.

Principais campos:

- `TEAMS_APP_ID`
- `TEAMS_APP_PASSWORD`
- `TEAMS_TENANT_ID`
- `TEAMS_MANIFEST_*`

Guia rapido:

- [GUIA_TEAMS.md](./GUIA_TEAMS.md)

## Observacoes de implantacao

- o endpoint do Teams precisa ser HTTPS publico
- para ambiente corporativo, o ideal e hospedar em infraestrutura da empresa ou Azure
- `documentos/` nao e versionado; se a operacao depender de ingestao local ou base documental local,
  copie essa pasta separadamente para a maquina nova
