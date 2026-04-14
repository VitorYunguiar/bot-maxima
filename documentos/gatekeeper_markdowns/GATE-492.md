# GATE-492 - Produtos Frios sendo cortado no força de vendas

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Pesquisa
- Natureza: Dúvida
- Atualizado em: 2024-12-12T16:08:06.448-0300

## Contexto do Problema

## Passos para reproduzir
Login: exporfrios.91
1 - entrar no maxPedido e tentar fazer um pedido com produtos frios

## Resultado apresentado
Estão sendo cortado no força de vendas e retornando uma crítica

## Resultado esperado
Pedido fluir normalmente sem cortes

## Descrição
Produto frios estão sendo cortado no força de vendas. Mesmo depois de ter mudado na rotina PA (padrão) para FR (frios)

## Comentarios do Gatekeeper

### 1. 2024-12-12T16:08:06.447-0300 | Filipe do Amaral Padilha

Realizei atualização do ambiente nuvem, extrator.
Para simular a situação, seria necessário enviar um pedido utilizando a última versão do maxPedido.
Além disso, a gente precisa olhar na 316 deles a simulação do pedido, para ver se os valores batem, valor total e líquido do item no pedido.

Nesse sentido, recomendo fazer um teste na versão ponta do maxPedido e também testar um pedido via 316 para ver o valor total do pedido com o cenário:
RCA: 91
CODIFILIAL 1
CODPLPAG 9
CODCLI 11156
CODPROD 3604 2 unidades
Pegar a origem de preço do produto na 316 também.

Caso o problema continue persistindo nas versões atualizadas do sistema, então reabrir o chamado do Gate com as evidências solicitadas

## Resposta Canonica

Não foi possível concluir a causa com os elementos atuais, pois a validação depende de simulação do cenário em versão atualizada e conferência dos valores na rotina 316.

Para análise correta, é necessário:
- enviar um pedido utilizando a última versão do maxPedido;
- simular o pedido na 316;
- verificar se os valores conferem na 316, principalmente:
  - valor total do pedido;
  - valor líquido do item;
- identificar também a origem de preço do produto na 316.

Parâmetros informados para o teste:
- RCA: 91
- CODIFILIAL: 1
- CODPLPAG: 9
- CODCLI: 11156
- CODPROD: 3604
- Quantidade: 2 unidades

Próximo passo:
- testar o cenário na versão ponta do maxPedido e via 316 com os parâmetros acima;
- se o problema persistir mesmo nas versões atualizadas, reabrir o chamado com as evidências da simulação e da conferência dos valores na 316.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 411983
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
