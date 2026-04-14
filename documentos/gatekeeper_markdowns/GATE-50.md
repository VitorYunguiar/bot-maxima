# GATE-50 - Relatorio de conta corrente puxando pedidos de março

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: STORM SYSTEM
- Assunto: MXGESN - Conta Corrente - Relatórios
- Natureza: Dúvida
- Atualizado em: 2024-09-12T08:47:38.323-0300

## Contexto do Problema

## Passos para reproduzir
Verificar pedidos do relatório em anexo;
Verificar MXSHISTORICOPEC numped 216631

## Descrição
O relatório de conta corrente para o RCA Pedro (28) com filtro de data 10/09/2024 - 10/09/2024 está puxando pedidos feitos em março.

Na segunda houve uma situação onde foi validado que registros da MXSHISTORICOPEDC estava com CODOPERACAO = 2 e tiveram que ser reenviados pelo ERP. Verifiquei que alguns dos pedidos com datas de março estao com DTATUALIZ = 10/09/2024.

É possivel que o reenvio desses registros para a MXSHISTORICOPEDC estejam causando o erro no filtro da data do relatório? Cliente OERPs

## Comentarios do Gatekeeper

### 1. 2024-09-12T08:47:38.322-0300 | Filipe do Amaral Padilha

O que acontece é o seguinte, quando o ERP mandou os registros ativos no dia 10/09/2024 e isso foi no dia 10/09/2024 (na vida real), a nossa JOB nossa de movimentação de conta corrente, que esse cliente usa, movimentou fazendo a leitura do histórico desse 216631 e outros pedidos na mesma condição.

Então a JOB fez a leitura da MXSHISTORICOPEDC e MXSHISTORICOPEDI devido ao dtatualiz e também porque o pedido está Faturado e movimentou o conta corrente para esse pedido (e isso pode acontecer com outros pedidos);

Quando a JOB é movimentada, gravamos um log na ERP_MXSLOGRCA, você até consegue consultar nessa tabela: SELECT * FROM ERP_MXSLOGRCA WHERE NUMPED IN(216631);

Como a JOB rodou no dia 10/09/2024, ela grava o histórico de movimentação do conta corrente nessa data. E o maxGestão usa uma consulta que busca dados nessa tabela para construir o relatório, por isso que, filtrando no mês de Setembro, traz dados do pedido de março, porque os registros foram atualizados em Setembro com posição de Faturado e houve uso de Conta Corrente nesses pedidos. O histórico do Conta Corrente é referente a movimentção de Setembro por isso é exibido no relatório.

*Não passar ao cliente*

Obs: Se o cliente não aceitar essa história, a gente pode mandar para N3, porém ele precisa fazer um levantamento com o Integrador deles, para nos passar a lista com os pedidos que eles reenviaram os históricos. E ainda não é garantido que nós façamos ajuste desses registros; A gente teria que verificar se tem como alterar as datas no histórico de conta corrente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, grounding_failed, needs_review
- Comentarios primarios: 394144
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Causa confirmada" — o texto-fonte explica o que aconteceu, mas não usa a expressão de confirmação conclusiva. | "ao filtrar o relatório de conta corrente de 10/09/2024 a 10/09/2024" — o texto-fonte menciona filtro no mês de setembro, não um intervalo específico de 10/09/2024 a 10/09/2024. | "o relatório não está exibindo a data original do pedido" — essa formulação interpretativa não aparece explicitamente no texto-fonte. | "Evidências apuradas" — rotulação não presente no texto-fonte. | "Próximo passo: 1. Consultar a ERP_MXSLOGRCA para o pedido 216631." — o texto-fonte diz que é possível consultar a tabela, mas não prescreve isso como próximo passo. | "Próximo passo: 2. Se necessário, solicitar ao cliente que levante com o Integrador a lista dos pedidos que tiveram históricos reenviados." — o texto-fonte condiciona isso ao caso de o cliente não aceitar a explicação. | "Próximo passo: 3. Caso o cliente não aceite a explicação ou seja necessária avaliação de ajuste, encaminhar para N3 para análise da possibilidade de alterar as datas no histórico de conta corrente." — parcialmente suportado, mas a resposta transforma uma possibilidade não garantida em plano de ação mais assertivo.
