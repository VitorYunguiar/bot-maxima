# Teams

## Preencher o `.env`

Configure no `.env`:

- `TEAMS_APP_ID`
- `TEAMS_APP_PASSWORD`
- `TEAMS_TENANT_ID`
- `TEAMS_ADMIN_IDS`
- `TEAMS_PORT`
- `TEAMS_MANIFEST_SHORT_NAME`
- `TEAMS_MANIFEST_FULL_NAME`
- `TEAMS_MANIFEST_SHORT_DESCRIPTION`
- `TEAMS_MANIFEST_FULL_DESCRIPTION`
- `TEAMS_MANIFEST_DEVELOPER_NAME`
- `TEAMS_MANIFEST_DEVELOPER_WEBSITE_URL`
- `TEAMS_MANIFEST_DEVELOPER_PRIVACY_URL`
- `TEAMS_MANIFEST_DEVELOPER_TERMS_URL`
- `TEAMS_MANIFEST_ACCENT_COLOR`

Use o `.env.example` como base.

## Instalar dependencias

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Gerar o pacote do Teams

```powershell
gerar_manifest_teams.bat
```

Ou:

```powershell
.\.venv\Scripts\python.exe scripts\build_teams_package.py
```

Saida gerada em `teams_manifest/build/`:

- `manifest.json`
- `bot-azure.zip`

## Subir o bot

Em producao, o bot roda no servidor Linux. Esta maquina nao executa mais o
runtime do Teams; ela serve para editar, testar o que for local e enviar
atualizacoes para o repositorio. O servidor recebe as mudancas com `git pull`.

```powershell
iniciar_teams.bat
```

Ou:

```powershell
.\.venv\Scripts\python.exe scripts\check_teams_runtime.py
.\.venv\Scripts\python.exe bot_teams.py
```

## Configuracao externa

- Publique a URL do bot apontando para `https://<host-publico>:<TEAMS_PORT>/api/messages`
- Nao use `ngrok` neste ambiente; a porta deve ficar aberta no servidor Linux que hospeda o bot
- No Azure Bot, configure o endpoint `/api/messages`
- Importe `teams_manifest/build/bot-azure.zip` no Teams

## Observacoes

- O `TEAMS_APP_ID` e usado tanto no runtime quanto no `manifest.id` e no `bots[].botId`
- O fluxo novo usa `teams_manifest/manifest.template.json` como fonte versionada
- Os artefatos gerados em `teams_manifest/build/` sao os arquivos para publicar
- Mudancas de codigo devem ser versionadas e aplicadas no servidor via `git pull`
