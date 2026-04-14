# GATE-362 - Acréscimo indevido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: N/A
- Assunto: MXPED - Produto - Preço Divergente
- Natureza: Erro
- Atualizado em: 2024-12-04T17:08:03.861-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do vendedor, duplicar o pedido 3408341986, alterar o plano de pagamento para PGTO 14/21/28 DIAS e enviar o pedido (sob autorização do cliente).

## Resultado apresentado
É verificado que após o envio, os itens sofrem um desconto de 7% e em alguns casos os itens do fornecedor 0023000298 podem apresentar um acréscimo de 200%.

## Resultado esperado
É esperado que esse comportamento não seja apresentado na aplicação.

## Descrição
Cliente relata que pontualmente na aplicação, ocorre um fato onde os pedidos são enviados e é adicionado um acréscimo de 200% nos produtos do fornecedor 0023000298. É verificado que a situação é apresentada em alguns casos após o pedido ser enviado no plano de pagamento PGTO 14/21/28 DIAS, pois é adicionado um desconto de 7% em todos os produtos.
Foram realizadas diversas tentativas de simulação do cenário apresentado, entretanto em nenhum foi possível replicar o mesmo cenário que é recorrente no ambiente do cliente.

Login para teste:
destro.22004365

## Comentarios do Gatekeeper

### 1. 2024-11-22T11:09:52.296-0300 | Filipe do Amaral Padilha

Enviado para N3 para eles verificarem a exibição do desconto na aba de consulta dos itens inseridos no pedido, porque é como foi dito, aparentemente não existe problema com os preços e a negocição, o que ocorre é que a exibição do desconto fica incoerente, por algum motivo que não consegui identificar

## Resposta Canonica

**Conclusão canônica**

Não foram identificados indícios de problema nos **preços** ou na **negociação** do pedido. A análise aponta que a ocorrência está relacionada à **exibição incoerente do desconto** na aba de consulta dos itens inseridos no pedido.

**Síntese da análise**
- Aparentemente, **não existe problema com os preços e a negociação**.
- A inconsistência observada está na **forma como o desconto é exibido** na consulta dos itens do pedido.
- **O motivo da incoerência não foi identificado** na análise realizada.

**Limitação**
- A causa técnica da incoerência de exibição **não foi determinada**.

**Encaminhamento**
- Direcionar para o **N3** avaliar a **exibição do desconto na aba de consulta dos itens inseridos no pedido**.

**Próximo passo**
- O **N3** deve verificar especificamente a camada de **exibição do desconto** nessa aba.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 408160
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
