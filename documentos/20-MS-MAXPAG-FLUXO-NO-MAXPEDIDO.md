# Fluxo maxPag no maxPedido

> Documento preparado para ingestao em banco vetorial (RAG).
> Sistema: maxPedido | maxPag | maxPayment | Server PDV | maxGestao | IntPDV | Extrator | ERP
> Area: Pagamento | PIX | Cartao de credito | Mensageria | Jobs | Estorno | Captura

---

## Objetivo

Documentar o fluxo completo de pedidos do maxPedido com pagamento via maxPag, cobrindo geracao de link, confirmacao de pagamento, integracao com ERP, monitoramento posterior, cancelamento, faturamento, captura e estorno.

O fluxo e assincrono e depende de mensageria e jobs.

---

## Componentes envolvidos

| Componente | Responsabilidade |
| --- | --- |
| maxPedido APK | Criacao do pedido e exibicao do link de pagamento |
| Server PDV | Validacao do pedido, registro da cobranca e consumo de mensagens |
| maxGestao | Autorizacao ou bloqueio comercial quando aplicavel |
| maxPag/maxPayment | Comunicacao com operadora, link e confirmacao de pagamento |
| Mensageria | Transporte dos eventos de link e pagamento |
| IntPDV | Consulta em banco nuvem e retorno de pedidos ao extrator |
| Extrator | Busca pedidos pagos/autorizados, integra ERP e monitora faturamento/cancelamento |
| ERP | Recebe o pedido integrado e processa faturamento/cancelamento |

---

## Visao geral do fluxo

1. Pedido e criado no maxPedido APK.
2. Server PDV valida dados, regras comerciais e regras fiscais.
3. Se houver necessidade, pedido passa por autorizacao no maxGestao.
4. Pedido autorizado gera solicitacao de link ao maxPag.
5. maxPag comunica a operadora e publica o link por mensageria.
6. Server PDV consome o link e registra a cobranca.
7. Pedido permanece em status de aguardando pagamento.
8. maxPedido APK apresenta o link ao cliente.
9. Cliente paga por PIX ou cartao.
10. maxPag recebe confirmacao da operadora e publica evento por mensageria.
11. Server PDV processa confirmacao, atualiza status e gera registros financeiros.
12. Extrator busca pedidos pagos/autorizados ainda nao integrados.
13. IntPDV consulta banco nuvem e retorna pedidos validos ao extrator.
14. Extrator envia pedido para FV/ERP.
15. ERP passa a ter o pedido oficialmente.
16. Novo job monitora se o pedido foi faturado ou cancelado.
17. maxPag e finalizado com captura, estorno ou cancelamento de pre-autorizacao conforme o resultado do ERP.

---

## Confeccao e validacao do pedido

No maxPedido, o vendedor informa a forma de pagamento:

- PIX.
- Cartao de credito.

O pedido e enviado ao Server PDV, que:

- Valida os dados do pedido.
- Executa regras comerciais.
- Executa regras fiscais.
- Envia para autorizacao no maxGestao quando o fluxo exigir.

Pedidos autorizados seguem para a geracao de cobranca no maxPag.

---

## Geracao e critica do link

Apos autorizacao:

1. Server PDV solicita ao maxPag a geracao do link de pagamento.
2. maxPag comunica a operadora do cliente.
3. O link gerado e publicado na mensageria.
4. Server PDV consome a mensagem.
5. Server PDV valida o link recebido.
6. Server PDV registra a cobranca.
7. Pedido permanece aguardando pagamento.

O maxPedido APK recebe o link e permite que o cliente pague via PIX ou cartao.

---

## Confirmacao de pagamento

Apos o pagamento:

- maxPag recebe a confirmacao da operadora.
- O tipo de retorno depende da forma de pagamento.

| Forma | Comportamento |
| --- | --- |
| PIX | Autorizacao direta |
| Cartao de credito | Pre-autorizacao |

O maxPag publica o evento de pagamento na mensageria. O Server PDV processa a confirmacao, atualiza o status do pedido e gera registros financeiros.

---

## Job do Extrator para pedidos pagos

Parametros de controle:

```text
ATIVAR_JOBMAXPAG_EXTRATOR = S
PERMITIR_VENDA_CARTAO_CREDITO = S
AMBIENTE_MAXPAYMENT = 0 para HMG, 1 para PROD
```

Responsabilidades:

- Buscar pedidos autorizados ou pre-autorizados que ainda nao foram integrados.
- Consultar pedidos pendentes via IntPDV.
- Enviar pedidos validos para FV/ERP.
- Monitorar resultado posterior do ERP.

---

## Integracao com ERP

O IntPDV:

- Acessa banco de dados na nuvem.
- Recupera pedidos pendentes de integracao.
- Retorna pedidos validos ao Extrator.

O Extrator:

- Envia os pedidos para FV/ERP.
- Realiza a integracao com o ERP.

Quando o pedido passa a existir no ERP, ele entra na etapa de monitoramento.

---

## Monitoramento apos integracao

Apos a integracao, outro job acompanha o status no ERP.

O Extrator:

- Busca pedidos faturados.
- Busca pedidos cancelados.
- Verifica se o fluxo financeiro no maxPag foi finalizado.

---

## Cenario de pedido cancelado

Quando o pedido e cancelado:

1. Extrator solicita ao IntPDV o cancelamento/estorno da autorizacao ou pre-autorizacao.
2. maxPag realiza estorno total ou cancela a pre-autorizacao.
3. Atualizacoes sao enviadas por mensageria.
4. Server PDV registra as movimentacoes.

---

## Cenario de pedido faturado

Quando o pedido e faturado, o IntPDV finaliza o processo maxPag.

### Sem cortes

| Forma | Acao |
| --- | --- |
| PIX | Finaliza sem estorno |
| Cartao | Captura total do valor pre-autorizado |

### Com cortes

| Forma | Acao |
| --- | --- |
| PIX | Estorno parcial dos itens cortados |
| Cartao | Captura parcial do valor atendido e cancela o restante da pre-autorizacao |

Observacao: em cartao de credito, quando a captura e menor que o valor original da pre-autorizacao, nao ha estorno adicional. O valor excedente e liberado automaticamente no limite do cliente.

---

## Tabelas para analise

```text
MXSMAXPAYMENTMOV
MXSINTEGRACAOPEDIDO_LOGST
```

Use essas tabelas para comparar:

- Datas das movimentacoes maxPag.
- Datas de mudanca de status do pedido.
- Etapa em que o fluxo parou.

---

## Checklist de diagnostico

1. Verificar se os parametros `ATIVAR_JOBMAXPAG_EXTRATOR` e `PERMITIR_VENDA_CARTAO_CREDITO` estao ativos.
2. Confirmar ambiente maxPayment: HMG ou PROD.
3. Validar se o pedido foi autorizado para cobranca.
4. Confirmar se o link foi gerado no maxPag.
5. Verificar se a mensagem do link foi consumida pelo Server PDV.
6. Validar se o cliente pagou o link.
7. Verificar retorno de pagamento na mensageria.
8. Conferir se o Extrator buscou o pedido pago.
9. Conferir se o IntPDV retornou o pedido ao Extrator.
10. Validar integracao no ERP.
11. Para cancelamento, validar estorno/cancelamento de pre-autorizacao.
12. Para faturamento com corte, validar captura parcial/estorno parcial.

---

## Resumo operacional

1. Pedido e criado no APK.
2. Pedido e validado/autorizado.
3. Link de pagamento e gerado.
4. Cliente realiza pagamento.
5. maxPag confirma pagamento.
6. Extrator integra pedido no ERP.
7. ERP fatura ou cancela.
8. maxPag finaliza financeiro com captura, estorno ou cancelamento.
