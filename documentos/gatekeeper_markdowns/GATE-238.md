# GATE-238 - Divergência relatório portal com a rotina 146

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor Cloud
- Assunto: MXGESN - Relatórios - Dados Divergentes do ERP
- Natureza: Dúvida
- Atualizado em: 2024-10-29T15:06:46.498-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o MaxGestão
>>Ir em relatórios
>>E no portal executivos ir na aba de vendas
>>Acessar o relatório Posição, Tipos de Venda e Origem de Pedidos
>>Filtrar pelas filias: 1,2,3,4,5,6,7,8,9,10 e 11, Posição dos pedidos: Não faturados, Posição do pedido: Todos os tipos de venda, Origem do pedido: Todas as origens
>>E filtrar
>>E assim pegando por exemplo a Equipe EMBALACENTER - FALCAO, seu valor de venda retornado é de 100.508,14, enquanto na rotina 146 o valor de venda retornada para essa equipe é de 42.889,13

Peguei somente essa equipe de exemplo, mais ocorre também nas demais equipes.

## Resultado apresentado
Divergência nos valores de venda do relatório Posição, Tipos de Venda e Origem de Pedidos com a rotina 146

## Resultado esperado
Que os valores de venda do relatório fique conforme a rotina 146

## Descrição
Analisando o relatório Posição, Tipos de Venda e Origem de Pedidos o mesmo está com divergência com a rotina 146.

## Comentarios do Gatekeeper

### 1. 2024-10-29T14:56:00.661-0300 | Filipe do Amaral Padilha

Enviado para N3 para verificação de possível problema na apuração dos dados de filtros "Não faturados"

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 403685
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Foi identificada divergência entre os valores de venda do relatório **Posição, Tipos de Venda e Origem de Pedidos** e a **rotina 146**. | Nos parâmetros informados: | **Filiais:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 e 11 | **Posição dos pedidos:** Não faturados | **Posição do pedido:** Todos os tipos de venda | **Origem do pedido:** Todas as origens | Exemplo analisado: | **Equipe EMBALACENTER - FALCAO** | Relatório: **100.508,14** | Rotina 146: **42.889,13** | Foi informado que a divergência também ocorre nas demais equipes. | A análise registrada aponta **possível problema na apuração dos dados do filtro "Não faturados"**, sem conclusão definitiva até o momento. | **Ação recomendada:** encaminhar para o **N3** para validação da apuração dos dados relacionados ao filtro **"Não faturados"**. | **Próximo passo:** acompanhar com o **N3** a verificação dessa possível falha.
