# GATE-705 - API de cancelamento

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - API de Cancelamento
- Natureza: Dúvida
- Atualizado em: 2025-01-28T16:09:27.901-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base zero do RCA, digitar um pedido qualquer e solicitar o cancelamento

## Resultado apresentado
Ao solicitar e retornar a crítica, é verificado que é retornado uma falha de autenticação na API do Winthor.

## Resultado esperado
É esperado que o rca consiga cancelar o pedido normalmente.

## Descrição
Cliente relata que ao solicitar o cancelamento de um pedido qualquer, a aplicação retorna uma falha de autenticação da api do winthor. Foi verificado que o problema só ocorre com todos os RCAS, e ao consultar os dados de autenticação do usuário do WTA e comparar com os dados na stack do portainer, não foram verificadas irregularidades.

Dados usuário WTA:
MAXPEDIDO
@@MAX2332.

http://177.69.254.49:8246/

Login para teste:
bhatac.189

## Comentarios do Gatekeeper

### 1. 2025-01-28T16:09:27.899-0300 | Filipe do Amaral Padilha

O IP estava errado no cadastro da stack para utilizar a API de cancelamentos.

IP correto
LINK_API_WINTHOR_CANCELAMENTO: http://192.168.1.246:8246/
USUARIO_API_WINTHOR_CANCELAMENTO: MAXPEDIDO
SENHA_API_WINTHOR_CANCELAMENTO: xiqkk9xEEGxh3vkqhYwYlQ==

Como ele é cliente on-primise ele usa o IP que vai configurado na rotina 132 do Winthor. E a gente importa esse IP na coluna IPMOBILE

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%MOBILE%';

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 419675
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A falha de autenticação no cancelamento ocorria porque o IP cadastrado na stack para uso da API de cancelamentos estava incorreto. | Assim, o erro apresentado como falha de autenticação decorre de configuração incorreta do endpoint de cancelamento na stack.
