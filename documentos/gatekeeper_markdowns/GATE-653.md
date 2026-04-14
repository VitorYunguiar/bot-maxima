# GATE-653 - Análise do comportamento do Flex e acréscimos na conta corrente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: N/A
- Assunto: MXPED - Conta Corrente
- Natureza: Dúvida
- Atualizado em: 2025-01-20T15:58:21.029-0300

## Contexto do Problema

## Passos para reproduzir
>> Usuário: meta.arthur1627
>> Verificar pedidos feito na data 11/01 a 13/01

## Resultado apresentado
N/A

## Resultado esperado
N;A

## Descrição
O cliente relatou que, no período de 11/01 a 13/01, a conta corrente do vendedor Arthur apresenta valores como se houvesse acréscimos aplicados ao Flex. Contudo, segundo informado, os pedidos realizados no ERP do cliente não utilizam a funcionalidade Flex.

Verifiquei na tabela ERP_MXSLOGRCA e só achei um pedido desse usuário no dia 11/01

## Comentarios do Gatekeeper

### 1. 2025-01-20T15:58:21.025-0300 | Filipe do Amaral Padilha

Verifiquei o pedido que o cliente informou e foi comprovado que de fato veio do ERP porque possui ORIGEMPED = 'B' e não existe nenhuma relação com pedido na nuvem.

Numéro 517706 não existe na MXSINTEGRACAOPEDIDO
e na MXSHSITORICOPEDC o numped = 517706

Nesse caso a nossa PKG por padrão sempre movimenta conta corrente de pedidos que vem do histórico, ou seja se vem direto do ERP a gente movimenta.

Então para resolver, considerando o relato do cliente, foi feito o cadastrado e desativado o parâmetro USAR_PEDIDOS_ERP_CALCULO_CC. (USAR_PEDIDOS_ERP_CALCULO_CC = 'N');

Com isso, se o pedido vir direto com histórico do ERP, nós não faremos em hipótese alguma, movimentação do conta corrente dele. Será feita movimentação somente em pedidos confeccionados no Força de Vendas e que vierem histórico de pedidos que já existem processados no banco nuvem.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 417823
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A movimentação observada na conta corrente não está relacionada ao uso de Flex. | Cadastrar e ativar o controle do parâmetro `USAR_PEDIDOS_ERP_CALCULO_CC`. | Após a alteração do parâmetro, validar se pedidos vindos direto do ERP com histórico deixam de gerar movimentação de conta corrente. | Não foi informada relação do pedido com pedido na nuvem.
