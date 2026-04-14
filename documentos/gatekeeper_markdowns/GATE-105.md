# GATE-105 - maxGestão com divergência do ERP

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: PROTON
- Assunto: MXGESN - Painel Geral - Dados Divergentes do ERP
- Natureza: Dúvida
- Atualizado em: 2024-09-30T11:25:10.219-0300

## Contexto do Problema

## Passos para reproduzir
>>Segue em anexo os dados do ERP do cliente, assim como os cenários
>>Validar os valores no maxGestao seguindo as datas dos relatórios

## Resultado apresentado
>>O valor quando se retira as devoluções, bate com o valor total do cliente.
>>Quando se pega os relatórios onde não existe devolução, o valor bate

## Resultado esperado
>>Os valores do ERP e do maxGestao devem bater

## Descrição
O cliente reclama de divergencia no maxPedido com o ERP, segue em anexo analise do DEV, onde o maxGestão bate com o ERP nas sem devoluções, porém no geral, o maxGestão permanece incorreto.

## Comentarios do Gatekeeper

### 1. 2024-09-27T17:03:20.097-0300 | Filipe do Amaral Padilha

Em anexo eu disponibilizei, um txt com o sql que a Máxima realiza para apurar os dados, com as mesmas condições do maxGestão. Te mandei para você ter uma ideia de como são apurados os dados. OBS *NÃO PASSAR o arquivo 'SQL_FATURADOS'* para o cliente.

### 2. 2024-09-30T07:50:14.773-0300 | Filipe do Amaral Padilha

No arquivo "Faturamento_Total_maxGestao_com_TV1_e_TV5" a gente extraiu os pedidos, os valores atendidos deles por item e quantidade que o ERP nos enviou e também o valor das devoluções por pedido somados.

Quando somarem o campo VLATEND do excel em anexo, vão chegar no número R$943.740 que siginificam todas as vendas, incluindo bonificações e pedidos normais sem deduzir devolução.

Essa apuração a gente faz baseada nos dados que a integração do ERP nos manda para a nuvem via API. Os principais endpoints que nós recebemos os dados são esses: ERP_MXSNFENT, ERP_MXSESTCOM, ERP_MXSNFSAID, ERP_MXSMOV, noMXSHISTORICOPEDC

Acredito que no caso de vocês, se corrigirem os dados no endpoint ERP_MXSMOV verificando nota a nota e os valores apresentados nelas, também cuidando com a data que foi incluída de faturamento delas, provavelmente resolve a informação divergente. Porque nós fazemos a soma do PUNIT * QT desse endpoint para obter o valor dos faturados.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 397695, 397732
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificamos que a divergência ocorre" — o texto-fonte apenas diz que corrigir o endpoint ERP_MXSMOV provavelmente resolve a informação divergente, não afirma de forma conclusiva que a divergência ocorre ali. | "Responsável pela correção: time responsável pelos dados enviados pelo ERP no endpoint `ERP_MXSMOV`." — o texto-fonte não identifica explicitamente um responsável pela correção.
