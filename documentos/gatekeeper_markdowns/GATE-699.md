# GATE-699 - API de cancelamento

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - API de Cancelamento
- Natureza: Dúvida
- Atualizado em: 2025-01-28T10:13:44.667-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base zero do RCA, digitar um pedido qualquer e solicitar o cancelamento

## Resultado apresentado
Ao solicitar e retornar a crítica, é verificado que é retornado uma falha de autenticação na API do Winthor.

## Resultado esperado
É esperado que o rca consiga cancelar o pedido normalmente.

## Descrição
Cliente relata que no rca masterfrios.felipe, ao solicitar o cancelamento de um pedido qualquer, a aplicação retorna uma falha de autenticação da api do winthor. Foi verificado que o problema só ocorre com o RCA em questão, e ao consultar os dados de autenticação do usuário do WTA e comparar com os dados na stack do portainer, não foram verificadas irregularidades.

Dados usuário WTA:
SUPORTE
MASTERFRIOS

http://SRVMASTER.MASTERFRIOS.LOCAL:8181/

## Comentarios do Gatekeeper

### 1. 2025-01-28T10:13:44.666-0300 | Filipe do Amaral Padilha

Fiz o teste com o usuário: masterfrios.FELIPE

Pedido enviado: SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP = 41055078;

Pedido cancelado com sucesso na crítica e na PEDC: SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED = 41055078;

Forma correta de cadastrar a stack:

LINK_API_WINTHOR_CANCELAMENTO: http://192.168.10.201:8181/
USUARIO_API_WINTHOR_CANCELAMENTO: SUPORTE
SENHA_API_WINTHOR_CANCELAMENTO: FD03cHDMTmGBco1Dkv57Tw==

Como ele é cliente com extrator on-primise então eu peguei o IP direto da MXSPARAMFILIAL:
SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%MOBILE%';

Ele clientes com extrator on-primise, ou seja, que não são t-cloud, deve ser utilizado o IP interno do WTA para utilizar a API de cancelamento de pedidos.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 419489
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A falha de autenticação no cancelamento de pedidos ocorre por configuração incorreta da stack em cliente com extrator on-premise. | Durante a validação, o pedido 41055078 foi consultado na integração e no histórico de cancelamento, com retorno de cancelamento efetuado com sucesso na crítica e na PEDC, indicando que o fluxo funciona quando a configuração está correta. | Ação recomendada: Validar os parâmetros de cancelamento informados e retestar com o usuário masterfrios.FELIPE.
