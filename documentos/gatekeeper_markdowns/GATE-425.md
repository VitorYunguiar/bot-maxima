# GATE-425 - Mensagem de conta corrente mesmo não utilizando conta corrente.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Sankhya
- Assunto: MXPED - Conta Corrente
- Natureza: Dúvida
- Atualizado em: 2024-12-02T17:33:44.965-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar a base do RCA em anexo 'stk.durval'
>>Entrar em algum cliente, exemplo o 53973 e clicar em um produto por exemplo o 10222, tentar dar desconto, qualquer valor (Testei com 6 %)

## Resultado apresentado
>>Aparece a mensagem "O saldo da conta corrente é insuficiente"
>>Testei desabilitando os parâmetros de conta corrente, colocando o "MXSUSUARI.USADEBCREDRCA" como "N, mas mesmo assim a mensagem permanece.

## Resultado esperado
>>Como o RCA não utiliza mais conta corrente, não deve aparecer esta mensagem.

## Descrição
>>Mesmo configurando para que não utilize conta corrente os RCA's continuam com a mensagem de conta corrente insuficiente

>>Parâmetros testados: DESCONTA_SALDOCCRCA_OFFLINE, IMPEDIR_ABATIMENTO_SEMSALDORCA

>>"MXSUSUARI.USADEBCREDRCA" como "N"

Mesmo assim a mensagem continua aparecendo

## Comentarios do Gatekeeper

### 1. 2024-12-02T11:08:31.120-0300 | Filipe do Amaral Padilha

Será encaminhado para N3

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review, requires_attachment_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
