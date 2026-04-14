# GATE-833 - Roteiro anterior gerado incorretamente.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: Dúvida
- Atualizado em: 2025-02-25T10:20:40.754-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do RCA, verificar o roteiro de visitas do dia 19/02/2025.
Em seguida, realizar os seguintes selects no banco nuvem do cliente:

SELECT * FROM ERP_MXSROTACLI WHERE CODUSUR = 120 AND DTPROXVISITA >= '19/02/2025';

SELECT * FROM MXMI_AGENDA_RCA WHERE ID_RCA = 120 AND INICIO_VISITA BETWEEN TO_DATE('19/02/2025', 'DD/MM/YYYY') AND TO_DATE('20/02/2025', 'DD/MM/YYYY') ORDER BY INICIO_VISITA ASC;

SELECT * FROM MXSCOMPROMISSOS WHERE CODUSUARIO = 64596 AND CODOPERACAO != 2 AND DTINICIO BETWEEN TO_DATE('19/02/2025', 'DD/MM/YYYY') AND TO_DATE('20/02/2025', 'DD/MM/YYYY') ORDER BY DTINICIO ASC;

SELECT * FROM MXSUSUARIOS WHERE CODUSUR = 120;

SELECT * FROM MXSVERSAOBD ORDER BY DTATUALIZACAO DESC;

SELECT * FROM MXSHISTORICOCOMPROMISSOS WHERE CODUSUARIO = 64596 AND CODOPERACAO != 2 AND DTINICIO BETWEEN TO_DATE('19/02/2025', 'DD/MM/YYYY') AND TO_DATE('20/02/2025', 'DD/MM/YYYY') ORDER BY DTINICIO ASC;

## Resultado apresentado
É verificado que nos dias anteriores ao dia atual (20/02/2025), são geradas visitas de forma inconsistente e aleatórias, impactando no fluxo de justificativa de roteiro.

## Resultado esperado
É esperado que os roteiros anteriores sejam gerados corretamente na MXSHISTORICOSCOMPROMISSOS e que o vendedor consiga iniciar novos pedidos corretamente.

## Descrição
Cliente relata que os compromissos de roteiros dos RCAs estão sendo apresentados incorretamente no apk.
Foi verificado no codusur 120, ao consultar o roteiro de visita do dia anterior na base do rca, que os compromissos constavam de forma incoerente e desorganizados quando comparados com o roteiro gerado pelo roteirizador na tabela MXMI_AGENDA_RCA. No dia analisado ('19/02/2025') foram verificados mais de 100 compromissos para o RCA, sendo que o mesmo possuía apenas 10 clientes roteirizados no dia.
Foi verificado também que não existem rotas geradas na ERP_MXSROTACLI.
Foi verificado que para o dia atual, os compromissos são gerados corretamente conforme registros na MXSCOMPROMISSOS, entretanto ao observar os dias anteriores é verificado que são gerados compromissos duplicados na MXSHISTORICOCOMPROMISSOS.
Com esse fluxo em mente, o cliente utiliza os parâmetros de justificativa de roteiro anterior, e devido ao problema que está sendo apresentado os rcas ficam impedidos de realizar vendas pois os compromissos gerados de forma incorreta do dia anterior ficam pendentes e o RCA não consegue acessar os clientes para justificar ou digitar um novo pedido.

Login para teste:
mix.120

## Comentarios do Gatekeeper

### 1. 2025-02-21T11:07:17.779-0300 | Filipe do Amaral Padilha

Os dados do cliente estava errados na tabela MXSHISTORICOCOMPROMISSOS, gerando vários compromissos de clientes não atendidos no roteiro anterior de forma inconsistente.

Isso ocorria segundo o nosso dev backend devido a problemas de versões antigas do banco de dados.

Então para resolver a situação foi feito o seguinte:

Foi gerada uma normalização de todos os registros de históricos de compromissos baseando os dados nos compromissos ativos do dia 20/01/2025 até o dia 03/01/2025.

Por que foi feito isso? Porque eles trabalham com o roteiro pendente somente do dia anterior, então se hoje é dia 21/02/2025, então eu só preciso do histórico normalizado do dia 20/02/2025 em diante.

Até o dia 03/01/2025, provavelmente não ocorrerá mais nenhum problema, porque foi feita normalização de todos esses dados que era o máximo da data que havia compromisso gerado pela nossa job.

Agora para resolver nos RCAs, eles apenas precisam estar sincronizando o maxPedido, ao fazer isso é esperado que eles recebam somente os compromissos pendentes do dia 20/02/2025 corretamente.

É necessário monitorar se ocorrer algum problema, enviar outro gate, mas como expliquei, provavelmente, problema com os roteiros anteriores pode ocorrer só depois do dia 03/01/2025, (não é esperado que ocorra) porque houveram correções no backend, então a gente espera que os históricos sejam gerados corretamente daqui em diante, mas é necessário acompanhar.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 425814
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Isso explica a divergência entre os compromissos apresentados no APK e o comportamento esperado para justificativa de roteiro e liberação de novos pedidos."
