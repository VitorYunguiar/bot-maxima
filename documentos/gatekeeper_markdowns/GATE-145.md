# GATE-145 - Oscilação na margem de lucratividade

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: João Pedro Faria Cabral [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido - Margem de Lucratividade
- Natureza: Erro
- Atualizado em: 2024-10-04T10:49:41.540-0300

## Contexto do Problema

## Passos para reproduzir
ACESSO
OPCAOATAC.82

BASE DO ZERO
- realizar um orçamento
- plano de pagamento e cobrança ( A VISTA e PIX )
- Adicionar um valor acima de 300 (Valor minimo da integradora)
- Checar a aba de totais do ORÇAMENTO
- Ir na timeline de pedidos e transformar o orçamento em pedido
- Checar a aba de totais do PEDIDO

## Resultado apresentado
BASE DO ZERO NA VERSÃO 3.251.9
Crash de apk ao transformar o orçamento em pedido

BASE DO ZERO NA VERSÃO 3.251.8
Crash de apk ao transformar o orçamento em pedido

BASE DO ZERO NA VERSÃO 3.251.6
o problema não acontece

BASE DO CLIENTE NA VERSÃO 3.251.6
Diferença drastica na margem de lucratividade, onde no meu caso saiu de 30 pra 615.

O video anexo enviado pelo cliente tambem mostra a situação

## Resultado esperado
Identificar o motivo da margem de lucratividade oscilar tanto ao transformar o orçamento em pedido

Identificar o motivo do crash nas versões mais atualizadas

## Descrição
O Cliente enviou um problema relacionado a transformar orçamento em pedidos

Toda vez que essa transição acontece a margem de lucratividade muda drasticamente.

Um video anexo foi enviado.

Testes realizados + resultados nas versões
*3.251.9* -> Crash de apk ao transformar orçamento bloqueado em pedido
*3.251.8* -> Crash de apk ao transformar orçamento bloqueado em pedido
*3.251.6* -> Problema não encontrado em BASE DO ZERO
*3.251.6* -> Problema foi simulado exatamente como descrito BASE RCA

## Comentarios do Gatekeeper

### 1. 2024-10-04T10:49:41.538-0300 | Filipe do Amaral Padilha

A lucratividade muda porque a gente tem uma funcionalidade no maxPedido que recalcula os preços dos produtos conforme a informação mais atual na base do RCA.

Significa que no dia 03/10/2024 o orçamento tinha um custo e preço nos produtos. E no dia 04/10/2024, depois de sincronizar, já é outro preço e custo. Por isso ocorre um recálculo e muda drasticamente.

Não cheguei a validar se a informação está correta a nível de cálculo, somente que ocorre um recálculo. E isso é devido ao parâmetro QTDE_DIAS_VALIDAR_ORC_IMPORTACAO por default ser 0, então ao importar de orçamento para pedido sempre recalcula. Ao editar não, somente ao importar. E isso pode ser mudado, por exemplo se você colocar QTDE_DIAS_VALIDAR_ORC_IMPORTACAO = 7, então até 7 dias de validade no orçamento ele não recalcula os preços e o custo.

Um paliativo por enquanto, seria cadastrar o parâmetro QTDE_DIAS_VALIDAR_ORC_IMPORTACAO = 7, dai não ocorre aquele recálculo de comissão.

Sobre o crash eu mandei para N3 para correção e pedi para no teste eles verificarem também se o valor de comissão está correto no recálculo.

## Resposta Canonica

**Causa identificada**

A oscilação da margem de lucratividade ao transformar orçamento em pedido ocorre porque o **maxPedido recalcula os preços e custos dos produtos na importação do orçamento para o pedido**, usando a informação mais atual disponível na base do RCA.

Isso acontece porque o parâmetro **`QTDE_DIAS_VALIDAR_ORC_IMPORTACAO`** está por padrão com valor **0**. Nessa condição, **toda importação de orçamento para pedido recalcula** preços e custos.

**Evidências analisadas**

- Em **03/10/2024**, o orçamento possuía um determinado custo e preço nos produtos.
- Em **04/10/2024**, após sincronização, os produtos já estavam com **outro preço e custo**.
- Assim, na importação de orçamento para pedido, ocorre **recálculo**, o que explica a mudança drástica da lucratividade.
- O comportamento foi observado **somente na importação**; **na edição não ocorre**.
- Se **`QTDE_DIAS_VALIDAR_ORC_IMPORTACAO = 7`**, então, dentro de **até 7 dias de validade do orçamento**, **não há recálculo** de preços e custos.

**Sobre o crash**

O **crash ao transformar orçamento em pedido** foi **encaminhado ao N3 para correção**.

**Ação recomendada**

- Como paliativo, **cadastrar `QTDE_DIAS_VALIDAR_ORC_IMPORTACAO = 7`** para evitar o recálculo durante a importação dentro desse prazo.
- Aguardar a **correção do crash pelo N3**.
- Nos testes da correção, **validar também se o valor de comissão está correto no recálculo**.

**Limitações da análise**

- Não foi validado se o cálculo resultante está correto do ponto de vista de regra de negócio; foi validado apenas que **há recálculo**.
- O ajuste do parâmetro para **7 dias** é um **paliativo**, não a correção definitiva.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 398975
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
