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

- O bot Teams continua ouvindo internamente em `TEAMS_PORT=3978`
- O proxy HTTPS publica o bot em `https://sabidao.maximatech.com.br:8443/api/messages`
- No Azure Bot, configure o Messaging endpoint exatamente como `https://sabidao.maximatech.com.br:8443/api/messages`
- Nao use `ngrok` neste ambiente; a porta publica `8443` deve ficar liberada no firewall/NAT
- Importe `teams_manifest/build/bot-azure.zip` no Teams

## Proxy HTTPS

O `docker-compose.yml` sobe o servico `teams_https_proxy` com nginx:

- escuta em `sabidao.maximatech.com.br:8443`
- usa certificados em `docker/nginx/certs/fullchain.pem` e `docker/nginx/certs/privkey.pem`
- encaminha `/api/messages` e `/api/health` para `127.0.0.1:3978`
- publica o bot Teams em `127.0.0.1:3978`, sem expor a porta 3978 diretamente na rede

Antes de subir o proxy, coloque um certificado TLS valido para o dominio/endpoint nesses arquivos:

```text
docker/nginx/certs/fullchain.pem
docker/nginx/certs/privkey.pem
```

Para subir o Teams com HTTPS:

```powershell
docker compose up -d teams_bot teams_https_proxy
```

Para testar no servidor:

```powershell
curl -k https://sabidao.maximatech.com.br:8443/api/health
```

## Observacoes

- O `TEAMS_APP_ID` e usado tanto no runtime quanto no `manifest.id` e no `bots[].botId`
- O fluxo novo usa `teams_manifest/manifest.template.json` como fonte versionada
- Os artefatos gerados em `teams_manifest/build/` sao os arquivos para publicar
- Mudancas de codigo devem ser versionadas e aplicadas no servidor via `git pull`
