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

Para ambiente Docker, use `DATABASE_URL` apontando para o servico `postgres`
definido no `docker-compose.yml`.

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
- [GUIA_DOCKER.md](./GUIA_DOCKER.md)

## Docker

Arquivos prontos:

- `Dockerfile`
- `docker-compose.yml`
- `.dockerignore`

Subida rapida:

```sh
docker compose build
docker compose up -d postgres
```

Depois da inicializacao do banco, rode a ingestao inicial:

```sh
docker compose --profile tools run --rm ingest
```

Com os documentos indexados, suba os bots:

```sh
docker compose up -d discord_bot teams_bot
```

Gerar pacote do Teams:

```sh
docker compose --profile tools run --rm teams_package
```

## Observacoes de implantacao

- o endpoint do Teams precisa ser HTTPS publico
- para ambiente corporativo, o ideal e hospedar em infraestrutura da empresa ou Azure
- `documentos/` nao e versionado; se a operacao depender de ingestao local ou base documental local,
  copie essa pasta separadamente para a maquina nova

## Extracao Gatekeeper

O pipeline dataset-first para tickets do Gatekeeper fica em `scripts/extract_jira_gatekeeper_filipe.py`.

Para uso simples no Windows, abra `abrir_extrator_gatekeeper.bat`.
Isso abre uma janela com botao `Extrair tickets` e grava os `.md` em
`documentos/gatekeeper_markdowns` por padrao.

Variaveis principais no `.env`:

- `JIRA_URL` ou `JIRA_BASE_URL`
- `JIRA_USERNAME` + `JIRA_API_TOKEN`
- ou `JIRA_USERNAME` + `JIRA_PASSWORD`
- ou `JIRA_SESSION_COOKIE`
- `JIRA_ASSIGNEE_ALIASES`

Exemplo de execucao:

```powershell
py scripts\extract_jira_gatekeeper_filipe.py --limit 20 --no-llm
```

Saida padrao:

- `datasets/gatekeeper_filipe/raw`
- `datasets/gatekeeper_filipe/normalized`
- `datasets/gatekeeper_filipe/gold`
- `datasets/gatekeeper_filipe/review`
