# GATE-420 - maxPag - Pedido ja pago, reenviado por engano, não chega ao winthor

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: João Pedro Faria Cabral [X]
- ERP do cliente: Winthor
- Assunto: MXPED - maxPag - PIX
- Natureza: Dúvida
- Atualizado em: 2024-11-29T12:28:40.132-0300

## Contexto do Problema

## Passos para reproduzir
ACESSO
disjoirs.1947.marilia

BASE DE DADOS ANEXADA
TIMELINE DE PEDIDOS, NUMPED 19471392  não envia ao ERP

## Resultado apresentado
O pedido está preso em um loop do maxPag de geração de um novo link de pagamento, e apesar de já ter sido pago via PIX o pedido não chega ao ERP para ser montado.

## Resultado esperado
Conseguir passar o pedido de modo que chegue ao Winthor

## Descrição
O numped 19471392  é um pedido de 16.000 que foi pago, porem não chegou no ERP
O motivo original era que a data que a previsão de faturamento que havia sido selecionada era inconpativel com o parametrizado no ambiente do cliente

Tentei alterar a data para permitir que o pedido chegasse ao erp mas ao seguir o curso de reenviar o pedido, acabou que o pedido entrou novamente no fluxo do maxPag e gerou um novo link e ficou preso no limbo de aguardando pagamento.
-----------------------------------
SQL's realizados

SELECT * FROM MXSINTEGRACAOPEDIDO ORDER BY DATA DESC;
SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPED =19471392  AND CODUSUR = 1947;
SELECT * FROM MXSINTEGRACAOPEDIDO_LOGST WHERE ID_PEDIDO = 597520;
SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED = ;

SELECT * FROM MXSHISTORICOCRITICA WHERE ID_PEDIDO = 597520;

SELECT * FROM MXSMAXPAYMENTMOV WHERE ID_PEDIDO = 597520;

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%PRAZO_VALIDADE_PEDIDO%';
SELECT * FROM MXSPARAMETRO ORDER BY CODPARAMETRO DESC;

## Comentarios do Gatekeeper

### 1. 2024-11-29T12:28:40.131-0300 | Filipe do Amaral Padilha

Funciona assim: Quando o pagamento é aprovado, tem uma função no nosso backend que valida esses dados do pagamento e seta o pedido para status 0 para ele ser enviado ao ERP e processado.

Então o que eu fiz foi isso setei para 0 e já acompanhei que foi integrado normalmente no Winthor e gerou a crítica:

"Descricao": ">>PEDIDO : 19471392\n594910 - MOUSTACHE BEAMS LTDA\nTotal : 16441.42\n--------------------------------------------\nPedido Winthor Normal : 1947002945\nVlr. Total : 16441.42\nVlr. Atendido : 16371.91\nQt Tot.Itens(Ped.Principal): 58\nQt Itens Atend: 57\n\n\nProduto: 16570 - ALGODAO 1X25G COTTONBABY CAIXA-Qt. Pedida: 27 Qt. Atendida: 0\n\nAtenção! A quantidade solicitada de um dos produtos foi menor que a quantidade faturada. Verifique se houve falta em um dos produtos do seu pedido. \n\nAtenção! A integradora informou que houve corte em um ou mais produtos do seu pedido. \n"

E posição Liberado. O corte a gente vai estornar o PIX automaticamente quando o pedido for faturado. Já sobre o parâmetro PRAZO_VALIDADE_PEDIDO, ele fez diferença porque ao colocar 30 dias ele permitiu que o pedido fosse integrado.

Porém é melhor colocar ele para 7 dias depois que acabar essa novela desse pedido.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409538
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "A causa do problema foi que, após a aprovação do pagamento, o fluxo esperado no backend — responsável por validar os dados do pagamento e setar o pedido para status 0 para envio ao ERP — não resultou na continuidade da integração até o Winthor." | "Ação recomendada - Manter o pedido em status 0 quando o pagamento for aprovado e validado, para permitir o envio ao ERP."
