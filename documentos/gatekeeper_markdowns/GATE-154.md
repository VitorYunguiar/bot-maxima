# GATE-154 - Histórico de compras não está batendo resultados

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Histórico
- Natureza: Dúvida
- Atualizado em: 2025-06-11T17:35:06.001-0300

## Contexto do Problema

## Passos para reproduzir
RCA 62: login: exporfrios.62 | Cliente 216

## Resultado apresentado
Há uma divergência nos valores dos bancos de dados (local e nuvem), em que os valores estão iguais, porém, em relação aos dados que o cliente apresentou em anexos estão diferentes.

## Resultado esperado
Um resultado sem divergências naquilo que o cliente apresentou

## Descrição
Foi feita uma análise no banco de dados nuvem primeiro, fizemos um Select para saber o valor(SUM (Pvenda*qt)) que daria junto dos filtros que foram dados pelo cliente (codcli 216/codusur 62/posicao F/codfilial 1), levando ao valor "87.129,99775", olhando a tabela do zero (Segunda foto), o valor mesmo com uma divergência mínima(87.130,00), bate com o valor que apresenta no aplicativo, diferente do valor na base do cliente que deu 23.495,72, tendo uma divergência enorme, junto também do relátorio que ele mandou do mesmo cliente e mesmo RCA que deu 107.326,10.

A gente foi analisar no banco de dados local do cliente assim procurando saber se havia uma divergência de bancos, porém, os valores do banco nuvem e banco local também bate seus valores, excluindo essa possibilidade.

## Comentarios do Gatekeeper

### 1. 2024-10-07T17:10:51.158-0300 | Filipe do Amaral Padilha

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSPARAMETRO{color} {color:#739eca}WHERE{color} {color:#00b8b8}NOME{color} {color:#739eca}LIKE{color} {color:#cac580}'%SYNC%'{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSUSUARIOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}LOGIN{color} = {color:#cac580}'exporfrios.62'{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color}

{color:#c1aa6c}SUM{color}({color:#00b8b8}PVENDA{color} * {color:#00b8b8}QT{color})

{color:#739eca}FROM{color}

{color:#b788d3}MXSHISTORICOPEDI{color}

{color:#739eca}WHERE{color}

{color:#00b8b8}NUMPED{color} {color:#739eca}IN{color}(

{color:#739eca}SELECT{color}

{color:#00b8b8}NUMPED{color}

{color:#739eca}FROM{color}

{color:#b788d3}MXSHISTORICOPEDC{color}

{color:#739eca}WHERE{color}

{color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TRUNC{color}({color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/09/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'30/09/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})

{color:#739eca}AND{color} {color:#00b8b8}CODUSUR{color} {color:#739eca}IN{color}({color:#c0c0c0}62{color})

{color:#739eca}AND{color} {color:#00b8b8}CODCLI{color} {color:#739eca}IN{color}({color:#c0c0c0}216{color})

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color}({color:#c0c0c0}1{color})

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} = {color:#cac580}'F'{color}

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}

{color:#739eca}AND{color} {color:#00b8b8}CONDVENDA{color} = {color:#c0c0c0}1{color})

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} = {color:#cac580}'F'{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSPARAMETRO{color} {color:#739eca}WHERE{color} {color:#00b8b8}NOME{color} {color:#739eca}LIKE{color} {color:#cac580}'%CRITERIOVENDA%'{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCLIENTCHARTHISTVENDA{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODCLI{color} {color:#739eca}IN{color}({color:#c0c0c0}216{color}) {color:#739eca}AND{color} {color:#00b8b8}CODUSUR{color} {color:#739eca}IN{color}({color:#c0c0c0}62{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TRUNC{color}({color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/09/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'30/09/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}sync_d_mxsclient{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODCLI{color} {color:#739eca}IN{color}({color:#c0c0c0}216{color}) {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}53739{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSAPARELHOSCONNLOG{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}53739{color}) {color:#739eca}ORDER{color} {color:#739eca}BY{color} {color:#00b8b8}DTATUALIZ{color} {color:#739eca}DESC{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCONEXOESLOG{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}53739{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA_INICIO{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TRUNC{color}({color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/07/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'30/07/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color}){color:#eecc64};{color}

### 2. 2024-10-08T07:28:50.227-0300 | Filipe do Amaral Padilha

*Não passar essas informações em negrito para o cliente*

*A nossa funcionalidade é alimentada por uma job nossa da Máxima que possui regras próprias para apurar e apresentar essa informação no maxPedido.*

*A tabela que alimenta a informação no maxPedido é a MXSCLIENTCHARTHISTVENDA*

*Não foi possível identificar a causa da informação não ter descido sozinha via sincronização para a base da RCA porque é um dado de Setembro que deveria ter descido com sicnronização realizada na época, mas a gente não guarda logs dessa data para analisar então não tem evidência para analisar nos restando realizar a carga.*

A informação na base do maxPedido do RCA de fato estava incorreta, para resolver esse cenário a gente realizou uma carga da tabela MXSCLIENTCHARTHISTVENDA desde Setembro até o dia atual. Para ela e outros RCAs com possíveis divergências receberem a informação, eles precisam estar sincronizando o maxPedido, somente.

O valor que vai constar na base do RCA referente ao mês de Setembro é R$87129.99775 ~= 87130.

O valor que o Winthor dela apura é referente a Data de Faturamento de pedidos, por isso a informação diverge bastante, porque você pode ter pedidos faturados que não correspondem a data de emissão do pedido.

Em outras palavras o Winthor, na rotina que ela apurou, faz de um jeito, e a nossa funcionalidade faz de outro, os dados nunca vão ser compatíveis da forma que ela apurou.

O valor que a nossa aplicação está apresentando pode ser considerado correto, é o esperado pela nossa funcionalidade. Se a cliente quiser mudar esse conceito (o valor que é exibido) seria uma melhoria, dai você pode entender com a cliente a necessidade que ela tem e subir diretamente um ticket de N3 épico.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 399327, 399362
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que 'a divergência não foi causada por diferença entre banco local e nuvem' não aparece no texto-fonte. | A afirmação de que a análise foi para o cenário 'LOGIN exporfrios.62, CODCLI 216, CODUSUR 62, CODFILIAL 1, POSICAO F, período de 01/09/2024 a 30/09/2024' como um cenário consolidado é parcialmente inferida; o texto-fonte mostra consultas com esses filtros, mas não declara explicitamente esse resumo como 'cenário analisado'. | A orientação 'Garantir que o RCA synchronize o maxPedido' usa linguagem normativa não literal; o texto-fonte diz que 'eles precisam estar sincronizando o maxPedido, somente', o que é próximo, mas não exatamente essa formulação. | A recomendação de 'abrir um ticket de N3 épico como melhoria' está próxima do texto-fonte, porém a resposta omite a condição explícita 'você pode entender com a cliente a necessidade que ela tem' antes de subir o ticket.
