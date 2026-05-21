# Docker

Este projeto pode rodar em Docker com dois containers separados:

- `discord_bot`
- `teams_bot`

Tambem existem dois servicos utilitarios:

- `ingest`
- `teams_package`

## 1. Preparar a maquina

Instale:

- Docker Desktop ou Docker Engine com Compose
- acesso a internet para baixar a imagem base e dependencias

Confirme:

```sh
docker --version
docker compose version
```

## 2. Clonar o repositorio

```sh
git clone https://github.com/VitorYunguiar/bot-maxima.git
cd bot-maxima
```

## 3. Criar o `.env`

Se ainda nao existir:

```sh
cp .env.example .env
```

Preencha no minimo:

- Discord:
  - `DISCORD_TOKEN`
- LLM/embeddings:
  - `LLM_PROVIDER`
  - `OPENAI_API_KEY` ou `GEMINI_API_KEY`
- Banco:
  - `DATABASE_URL`
- Teams:
  - `TEAMS_APP_ID` ou `MicrosoftAppId`
  - `TEAMS_APP_PASSWORD` ou `MicrosoftAppPassword`
  - `TEAMS_TENANT_ID` ou `MicrosoftAppTenantId`
  - `TEAMS_APP_TYPE` ou `MicrosoftAppType`
  - `TEAMS_MANIFEST_*`

## 4. Copiar os documentos

Se a base documental for local, copie a pasta `documentos/` para o clone.

O compose monta essa pasta em modo leitura dentro dos containers:

- host: `./documentos`
- container: `/app/documentos`

## 5. Build da imagem

```sh
docker compose build
```

## 6. Subir o PostgreSQL local

O servico `postgres` cria extensoes, tabelas e funcoes automaticamente
na primeira inicializacao, usando os scripts da pasta `sql/` na ordem
definida pelo bootstrap do container.

```sh
docker compose up -d postgres
```

Para acompanhar a inicializacao:

```sh
docker compose logs -f postgres
```

## 7. Ingestao inicial

Depois que o `postgres` estiver saudavel, indexe os documentos da pasta local no banco vetorial:

```sh
docker compose --profile tools run --rm ingest
```

## 8. Gerar o pacote do Teams

```sh
docker compose --profile tools run --rm teams_package
```

Arquivos gerados:

- `teams_manifest/build/manifest.json`
- `teams_manifest/build/bot-azure.zip`

## 9. Subir os bots

Discord + Teams:

```sh
docker compose up -d discord_bot teams_bot
```

So Discord:

```sh
docker compose up -d discord_bot
```

So Teams:

```sh
docker compose up -d teams_bot
```

## 10. Ver logs

Discord:

```sh
docker compose logs -f discord_bot
```

Teams:

```sh
docker compose logs -f teams_bot
```

## 11. Testar o bot do Teams

Healthcheck local:

```sh
curl http://localhost:3978/api/health
```

Resultado esperado:

```json
{"status":"ok","platform":"teams"}
```

O `Messaging endpoint` do Azure Bot deve apontar para:

```text
https://sabidao.maximatech.com.br:7443/api/messages
```

O container do bot Teams fica publicado apenas no loopback do servidor em
`127.0.0.1:3978`. O HTTPS publico fica no servico `teams_https_proxy`, que escuta
em `sabidao.maximatech.com.br:7443` e encaminha para `127.0.0.1:3978`. Coloque os certificados
TLS em:

```text
docker/nginx/certs/fullchain.pem
docker/nginx/certs/privkey.pem
```

## 12. Parar tudo

```sh
docker compose down
```

## 13. Atualizar o projeto

```sh
git pull
docker compose build
docker compose up -d discord_bot teams_bot
```

## Observacoes

- `runtime/` guarda o `ingest_failures.json` persistido fora do container
- `postgres_data` guarda o banco local em volume nomeado
- `documentos/` nao vai para a imagem; ele e montado como volume
- o Docker reduz variacao de ambiente, mas nao impede totalmente que um admin do host inspecione a imagem
