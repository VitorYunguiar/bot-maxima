# GATE-648 - Status dos pedidos não atualizam

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Sismic
- Assunto: MXPED - Pedido/Orçamento - Timeline
- Natureza: Dúvida
- Atualizado em: 2025-01-16T14:03:55.528-0300

## Contexto do Problema

## Passos para reproduzir
Verificar pedido NUMPED = 5956

## Resultado apresentado
Status dos pedidos não atualizam

## Resultado esperado
Status dos pedidos atualizando na sync automática.

## Descrição
Status do pedido não atualiza na sync automática mesmo com os pedidos ja integrados.

Login: safari.safari

## Comentarios do Gatekeeper

### 1. 2025-01-16T13:19:35.401-0300 | Filipe do Amaral Padilha

Primeiro gostaria de esclarescer um ponto: Somente o pedido 5696 foi integrado a nuvem por enquanto, porque o pedido 5697 possui uma dependência de receber os dados primeiro do 5696 para depois ser enviado ao ERP.

Sobre o pedido 5696, ele foi para a nuvem e ficou disponível para o ERP realizar a integração dele:
>> O ERP integrou e nos gerou a informação da numeração do pedido ERP como "010122119700". Conforme reunião já realizadas com o responsável da integração do cliente.
>> Acordamos que, para usar sincronização automática, eles precisariam enviar essa informação do pedido sem o "0" na frente.
>> Também foi passado, mas vamos reforçar que o tamanho máximo é NUMBER (10) para o campo do pedido

>> Eles devem enviar o numPedidoERP sem o "0" na frente como expliquei, e essa informação se repete no mesmo endpoint (MXSINTEGRACAOPEDIDO):
1° A gente usa e registra ela vindo do ERP no campo numPedidoERP.CRITICA.NUMPEDERP como uma string JSON
2° A gente armazena ela também exclusivamente no campo NUMPEDERP.MXSINTEGRACAOPEDIDO

Eles também não retornaram ainda o histórico do pedido 5696. Que seria o nosso endpoint MXSHISTORICOPEDC(HistoricosPedidosCapas) com as inforamções do pedido.

Aqui bem importante também, regras devem ser respeitadas na hora de eles nos enviarem o endpoint MXSHISTORICOPEDC.

Eles devem copiar o DTABERTURAPEDPALM da MXSINTEGRACAOPEDIDO e mandar igual na MXSHISTORICOPEDC.

Devem mandar o NUMPEDRCA e NUMPED corretamente na MXSHISTORICOPEDC, sendo a regra:

MXSINTEGRACAOPEDIDO.NUMPED = MXSHISTORICOPEDC.NUMPEDRCA
e
MXSINTEGRACAOPEDIDO.NUMPEDERP = MXSHISTORICOPEDC.NUMPED.

Devem mandar o mesmo CODUSUR, CODCLI, CODFILIAL, CONDVENDA que foi digitado (MXSINTEGRACAOPEDIDO). O endpoint deve ter exclusivamente esses dados batendo na (MXSHISTORICOPEDC e MXSINTEGRACAOPEDIDO).,

--Mais um detalhe, o fluxo do maxSync está desligado na Safari porque da última vez a gente acordou que para testar, teria que solicitar ao Integrador verificar o fluxo no ERP e a gente na Máxima habilitar o fluxo internamente. Por esses motivos esse teste não foi 100% efetivo, seria necessário habilitar os fluxos e realizar um pedido novo do zero

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 417241
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'A atualização automática de status não ocorre' — o texto-fonte não afirma explicitamente que a atualização automática de status não ocorre; apenas diz que o fluxo maxSync está desligado e que o teste não foi 100% efetivo. | 'existem pendências nas regras de integração do ERP' — o texto-fonte traz regras a serem respeitadas e itens não retornados, mas não usa essa formulação causal ampla. | 'Responsáveis: Integrador/ERP do cliente; Equipe Máxima' — o texto-fonte menciona o integrador do cliente e que a Máxima habilitaria o fluxo internamente, mas não apresenta uma seção de responsáveis nem atribui formalmente essa responsabilidade dessa forma. | 'Login analisado: safari.safari' — não consta no texto-fonte.
