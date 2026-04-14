# GATE-737 - divergencia em base do zero e base anexada

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2025-02-04T12:43:26.851-0300

## Contexto do Problema

## Passos para reproduzir
efetuar o login na aplicação;
iniciar a negociação para o cliente 309799;
buscar os produtos na tabela;
comparar o mesmo fluxo na base anexada

## Resultado apresentado
mesmo sincronizando, o RCA não consegue ver os produtos

## Resultado esperado
é esperado que o app tenha o mesmo comportamento que ocorra na base do zero.

## Descrição
Senhores ao analisar o cenário relatado pelo cliente, está sendo observado divergência de comportamento entre base do zero e a base anexada, onde mesmo o RCA sincronizando o app não normaliza a exibição dos produtos. Esse cenário acontece com vários vendedores do cliente.

login: Martminas.x_luciano

## Comentarios do Gatekeeper

### 1. 2025-02-04T08:18:05.783-0300 | Filipe do Amaral Padilha

Foi realizada a carga para as filiais 235, 251, 261, 271 que foram encontradas na base do RCA anexado. Dito isso, todos os RCAs que trabalham também com essas filiais terão como realizar a sincronização dos dados.

Eu optei por fazer diretamente a carga porque eu entendi que esse cliente precisava de uma ação imediata para liberar os RCAs para venda.

Eu vou continuar investigando para tentar encontrar a cauza raiz. A resolução definitiva, não é com a gente suporte/N2 isso é com o N3. Por isso eu vou encaminhar para desenvolvimento.

--Sugestões de perguntas para esse cliente:

>> Questionar que horas eles realizam a integração dos dados, e se eles fazem modificações em massa, porque a Máxima realiza manutenção no nosso bd nuvem de madrugada e se isso for concorrer com a integração do cliente, a integração simplesmente é parada.

>> Questionar que horas os RCAs se dão conta que os itens sumiram.

>> Questionar para o cliente se ele costuma trocar as filiais de venda dos RCAs com frequência através da Central.
(No vídeo que chegou para mim no GATE o RCA Luciano possui acesso a 4 filiais e no momento, olhando pela central do RCA, ele possui acesso somente a 1 então isso comprova a teoria que o cliente fica alterando as filiais dos RCAs já em produção).

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 421136
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificamos divergência entre as filiais associadas ao RCA no momento da análise, o que explica o comportamento inconsistente na exibição dos produtos" — o texto-fonte sugere uma teoria sobre alteração de filiais e menciona sincronização dos dados, mas não afirma como fato que isso explica o comportamento inconsistente na exibição dos produtos. | "O mesmo comportamento foi informado para vários vendedores do cliente" — não há menção no texto-fonte a vários vendedores terem apresentado o mesmo comportamento. | "...o que reforça a suspeita de alteração recorrente de filiais ou interferência no processo." — a parte de "interferência no processo" não é afirmada no texto-fonte dessa forma; há apenas sugestões de investigação e hipótese de concorrência com manutenção. | "Parâmetros analisados: - Cliente: 309799" — o texto-fonte não informa esse cliente. | "Parâmetros analisados: - Login: Martminas.x_luciano" — o texto-fonte não informa esse login.
