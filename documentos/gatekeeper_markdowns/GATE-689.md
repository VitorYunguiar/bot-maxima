# GATE-689 - PREÇO DE TABELA PRODUTO 801695 DIFERENTE DO WINTHOR

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Preço Divergente
- Natureza: Dúvida
- Atualizado em: 2025-01-27T16:58:39.698-0300

## Contexto do Problema

## Passos para reproduzir
efetuar as consultas e validações conforme o cenário citado

## Resultado apresentado
a principio, está sendo identificada que foi efetuada uma aplicação dupla de desconto no item com o mesmo percentual, de forma inesperada.

## Resultado esperado
é esperado que apenas a uma validação e inserção do desconto de 7% tenha sido aplicada.

## Descrição
Senhores, ao analisar o cenário abaixo:

"Boa tarde,
O pedido RCA 1862212947, teve o produto 801695 RUFFLES SAL C/PRECO 1X32G com um preço de tabela inferior da tabela no winthor, o preço de tabela do produto no prazo de 14 dias é de R$3,03 e no maxpedido ficou R$2,82 e com 7% de desconto de um combo chegou a R$2,62 onde o correto seria o valor mínimo de R$2,82, ficou como se o sistema deixou colocar o desconto duas vezes de 7%. Por favor verificar."

Eu não consegui identificar o que aconteceu com esse pedido que gerou esse cenário que o cliente relata. O produto citado, teve um preço de tabela informado no JSON de 2,82:  !image-2025-01-24-10-17-42-060.png!

Porém o preço original do item é de 2,99:

!image-2025-01-24-10-19-22-759.png!

que condiz com o preço presente na mxstapr para a região do cliente do pedido:

!image-2025-01-24-10-20-19-170.png!

o produto possui 2 politicas comerciais aplicadas(uma de desconto e outra acréscimo), mas que não alteram o preço de tabela:

!image-2025-01-24-10-21-52-395.png!

Mas há um cenário anormal registrado, nas campanhas de desconto, onde o JSON foi gerado com um registro duplicado da mesma campanha:

!image-2025-01-24-10-23-01-893.png!

com isso, essa situação é o que gerou o cenário em questão? ou é esperado que ocorra a negociação do item da forma que foi apresentada?

o seguinte script de consultas abaixo efetuei para fazer a validação que citei:
{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsintegracaopedido{color} {color:#739eca}WHERE{color} {color:#00b8b8}numped{color} = {color:#c0c0c0}1862212947{color}{color:#eecc64};{color} {color:#669768}--politicas 1011960 1011904{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsdesconto{color} {color:#739eca}WHERE{color} {color:#00b8b8}coddesconto{color} {color:#739eca}IN{color} ({color:#c0c0c0}1011960{color},{color:#c0c0c0}1011904{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsusuarios{color} {color:#739eca}WHERE{color} {color:#00b8b8}codusuario{color} = {color:#c0c0c0}81812{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsaparelhosconnlog{color} {color:#739eca}WHERE{color} {color:#00b8b8}codusuario{color} = {color:#c0c0c0}81812{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} {color:#00b8b8}ptabela{color}, {color:#b788d3}c{color}. * {color:#739eca}FROM{color} {color:#b788d3}mxstabpr{color} {color:#b788d3}c{color} {color:#739eca}WHERE{color} {color:#00b8b8}codprod{color} = {color:#c0c0c0}801695{color} {color:#739eca}AND{color} {color:#00b8b8}numregiao{color} = {color:#c0c0c0}15{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsplpag{color} {color:#739eca}WHERE{color} {color:#00b8b8}codplpag{color} = {color:#c0c0c0}3{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} {color:#b788d3}C{color}.{color:#00b8b8}CLIENTE{color},{color:#b788d3}C{color}.{color:#00b8b8}CODCLI{color},{color:#b788d3}C{color}.{color:#00b8b8}CODPRACA{color},{color:#b788d3}N{color}.{color:#00b8b8}NUMREGIAO{color},{color:#b788d3}R{color}.{color:#00b8b8}REGIAO{color} {color:#739eca}FROM{color} {color:#b788d3}MXSCLIENT{color} {color:#b788d3}C{color}

{color:#739eca}JOIN{color} {color:#b788d3}MXSPRACA{color} {color:#b788d3}N{color} {color:#739eca}ON{color} {color:#b788d3}C{color}.{color:#00b8b8}CODPRACA{color} = {color:#b788d3}N{color}.{color:#00b8b8}CODPRACA{color}

{color:#739eca}JOIN{color} {color:#b788d3}MXSREGIAO{color} {color:#b788d3}R{color} {color:#739eca}ON{color} {color:#b788d3}R{color}.{color:#00b8b8}NUMREGIAO{color} = {color:#b788d3}N{color}.{color:#00b8b8}NUMREGIAO{color}

{color:#739eca}WHERE{color} {color:#00b8b8}CODCLI{color} = {color:#c0c0c0}206472{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsfilial{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsdescontoc{color} {color:#739eca}WHERE{color} {color:#00b8b8}codigo{color} = {color:#c0c0c0}11079{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsdescontoi{color} {color:#739eca}WHERE{color} {color:#00b8b8}codigo{color} = {color:#c0c0c0}11079{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} {color:#b788d3}PED_TAB{color}.{color:#00b8b8}ID_PEDIDO{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}NUMPED{color} {color:#00b8b8}NUMPEDRCA{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}CODCLI{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}CODUSUR{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}CODFILIAL{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}CONDVENDA{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}TIPOPEDIDO{color}, {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}CODPROD{color}, {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}QUANTIDADE{color},{color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}APLICOUDESCONTOESCALONADO{color},

{color:#c1aa6c}ROUND{color}({color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}PRECOVENDA{color},{color:#c0c0c0}2{color}) {color:#00b8b8}PRECOVENDA{color}, {color:#c1aa6c}ROUND{color}({color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}PRECOBASE{color},{color:#c0c0c0}2{color}) {color:#00b8b8}PRECOBASE{color}, {color:#739eca}CASE{color} {color:#739eca}WHEN{color} {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}PRECOVENDA{color} > {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}PRECOBASE{color} {color:#739eca}THEN{color} {color:#cac580}'C'{color} {color:#739eca}ELSE{color} {color:#cac580}'D'{color} {color:#739eca}END{color} {color:#00b8b8}TIPOOPER{color}, {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}SEQUENCIA{color} {color:#739eca}FROM{color} {color:#b788d3}MXSINTEGRACAOPEDIDO{color} {color:#b788d3}PED_TAB{color}, {color:#b19b9b}JSON_TABLE{color}({color:#9e9e9e}OBJETO_JSON{color}, {color:#cac580}'$.Produtos[*]'{color} {color:#9e9e9e}COLUMNS{color} ({color:#739eca}ROW_NUMBER{color} {color:#739eca}FOR{color} {color:#739eca}ORDINALITY{color}, {color:#9e9e9e}CODPROD{color} {color:#c1aa6c}VARCHAR2{color}({color:#c0c0c0}4000{color}) {color:#739eca}PATH{color} {color:#cac580}'$.Codigo'{color}, {color:#9e9e9e}PRECOBASE{color} {color:#c1aa6c}NUMBER{color} {color:#739eca}PATH{color} {color:#cac580}'$.PrecoBase'{color}, {color:#9e9e9e}PRECOVENDA{color} {color:#c1aa6c}NUMBER{color} {color:#739eca}PATH{color} {color:#cac580}'$.PrecoVenda'{color}, {color:#9e9e9e}QUANTIDADE{color} {color:#c1aa6c}NUMBER{color} {color:#739eca}PATH{color} {color:#cac580}'$.Quantidade'{color},{color:#9e9e9e}APLICOUDESCONTOESCALONADO{color} {color:#c1aa6c}VARCHAR2{color}({color:#c0c0c0}4000{color}) {color:#739eca}PATH{color} {color:#cac580}'$.AplicouDescontoEscalonado'{color}, {color:#9e9e9e}SEQUENCIA{color} {color:#c1aa6c}VARCHAR2{color}({color:#c0c0c0}4000{color}) {color:#739eca}PATH{color} {color:#cac580}'$.Sequencia'{color} )) {color:#9e9e9e}PJSONPROD{color} {color:#739eca}WHERE{color} {color:#9e9e9e}PED_TAB{color}.{color:#9e9e9e}ID_PEDIDO{color} = {color:#c0c0c0}350702{color} {color:#739eca}ORDER{color} {color:#739eca}BY{color} {color:#9e9e9e}SEQUENCIA{color}

## Comentarios do Gatekeeper

### 1. 2025-01-27T16:21:30.581-0300 | Filipe do Amaral Padilha

Login: gd7j.1862
FILIAL 3
CODPLPAG 3
CODCLI 206472
CODPROD: 801695

Crítica do pedido:

"Descricao": ">>PEDIDO      : 1862212947\n206472 - MARIA ANGELICA RODRIGUES DA SILVA\nTotal        : 181.03\n--------------------------------------------\nPedido Winthor  Normal : 1862006104\nVlr. Total    : 181.03\nVlr. Atendido : 181.03\nQt Tot.Itens(Ped.Principal): 8\nQt Itens Atend: 8\n\n"

Informações que temos no log do JSON do pedido:
"PrecoVenda": 2.62226
"PercDescontoInformadoTela": 0.07
"Tributacao": {
"CodIcmPF": 0.2,
"CodIcmRural": 0.2,
"CodIcmPJ": 0.2,
"CodIcmTAB": 0.0925,
"SitTributaria": "90",
"CodFiscal": "5403",
"CodFiscalInterestadual": "6102"
"PrecoBase": 2.62226,
"PrecoOriginal": 2.99,

repetido 2x:

"ListaCampanhasDesconto": [
{
"Codigo": "11079",
"Descricao": "COMBO PARTE 01 - ITENS PRIORITARIOS ELMA",
"TipoPatrocinio": "E",
"TipoCampanha": "MIQ",
"DataInicio": "2025-01-03T00:00:00",
"DataTermino": "2025-01-31T23:59:59",
"CodigoProduto": "801695",
"QtMinima": 2.0,
"QtMaxima": 560.0,
"PercDesconto": 0.07,
"QtPedido": 0.0,
"UtilizaCodProdPrincipal": false,
"DescricaoProduto": null,
"Sequencia": 87,
"Chave": null,
"ComboContinuo": true
}
],
"PoliticaCampanhaDesconto": {
"Codigo": "11079",
"Descricao": "COMBO PARTE 01 - ITENS PRIORITARIOS ELMA",
"TipoPatrocinio": "E",
"TipoCampanha": "MIQ",
"DataInicio": "2025-01-03T00:00:00",
"DataTermino": "2025-01-31T23:59:59",
"CodigoProduto": "801695",
"QtMinima": 2.0,
"QtMaxima": 560.0,
"PercDesconto": 0.07,
"QtPedido": 0.0,
"UtilizaCodProdPrincipal": false,
"DescricaoProduto": null,
"Sequencia": 87,
"Chave": null,
"ComboContinuo": true
},

"PrecoVendaInformado": 2.62226,
"PrecoTabelaInformado": 2.81963

-----------------
Produto já não faz mais parte da campanha, para validar inserir:
INSERT INTO MXSDESCONTOI (CODIGO, SEQUENCIA, CODPROD, QTMINIMA, PERDESC, TIPOPRODUTO, QTMAXIMA, SYNCFV, TIPODESCONTO, CODAUXILIAR) VALUES (11079, 87, 801695, 2.0, 7.0, NULL, 560.0, 'S', 'A', '7892840822996')

Em base do zero na mesma versão que o cliente está usando, não houve problemas nem com pedido normal, nem duplicado.

Cenário do pedido dele passou por status 6 salvo e bloq e depois reenviado.
6	2025-01-16 15:02:49.000
0	2025-01-16 15:10:46.000
2	2025-01-16 15:10:50.000
11	2025-01-16 15:10:53.000
4	2025-01-16 15:11:01.000

-------------------------
Comentários sobre a análise, não é possível replicar o problema. Aparentemente houve sim duas apliações de 7% de desconto no item do pedido. Pode ter sido fruto de algum bug de duplicação de pedidos ou então de importação de base que o RCA pode ter feito.

Na própria base do RCA não é póssível simular. Se você tentar iniciar um pedido novo nem na base do zero, não é possível reproduzir nem na versão ponta do maxPedido e nem na versão do cliente.

Nesse caso recomendo habilitar o parâmetro de log:

GRAVA_LOG_ENVIO_PEDIDO

E utilizar a versão de ponta do maxPedido que já passou por correções no fluxo de duplicação e mudanças no uso de campanhas de Desconto.

O pedido que foi passado com preço divergente apesar do problema, a Integradora da TOTVs não recusou a entrada do item.

O desenvolvimento não tem como realizar uma correção retroativa do item que foi enviado com preço errado e como não é possível reproduzir o problema, e também não está utilizando versão de ponta, então não temos como realizar uma correção, é necessário o cliente utilizar as versões atualizadas do sistema para quando o problema ocorrer novamente (se ocorrer) a gente conseguir enviar para desenvolvimento N3

## Resposta Canonica

Análise canônica:

Foi identificado no pedido um cenário compatível com dupla aplicação de 7% de desconto no item. Pelos registros analisados, no log do pedido constam `PrecoVenda = 2.62226`, `PercDescontoInformadoTela = 0.07`, `PrecoBase = 2.62226`, `PrecoOriginal = 2.99`, além de `PrecoVendaInformado = 2.62226` e `PrecoTabelaInformado = 2.81963`. Também foi verificado que a campanha de desconto código `11079` aparece repetida duas vezes no conteúdo do pedido, o que é aderente ao comportamento relatado.

A causa exata não pôde ser determinada com reprodução controlada. A avaliação técnica é de que o cenário pode ter sido provocado por algum bug de duplicação de pedidos ou por importação de base realizada pelo RCA. Esse entendimento é reforçado pelo fato de que:
- não foi possível reproduzir o problema;
- na própria base do RCA não foi possível simular;
- em base limpa, na mesma versão do cliente, não houve falha nem em pedido normal nem em pedido duplicado;
- o problema também não foi reproduzido nem na versão ponta do maxPedido nem na versão do cliente.

Adicionalmente, a Integradora da TOTVs não recusou a entrada do item mesmo com preço divergente. O pedido passou pelos status `6, 0, 2, 11 e 4`, nos horários já registrados no atendimento.

Como limitação, o desenvolvimento não consegue realizar correção retroativa do item já enviado com preço incorreto. Como o problema não é reproduzível e o ambiente não está em versão de ponta, não há ação corretiva imediata aplicável.

Recomendação:
1. Habilitar o parâmetro `GRAVA_LOG_ENVIO_PEDIDO`.
2. Atualizar o maxPedido para a versão de ponta, que já possui correções no fluxo de duplicação e em mudanças no uso de campanhas de desconto.
3. Caso o problema volte a ocorrer, coletar os logs e encaminhar para o desenvolvimento N3.

SQL relacionado à campanha identificada no cenário:
```sql
INSERT INTO MXSDESCONTOI (CODIGO, SEQUENCIA, CODPROD, QTMINIMA, PERDESC, TIPOPRODUTO, QTMAXIMA, SYNCFV, TIPODESCONTO, CODAUXILIAR)
VALUES (11079, 87, 801695, 2.0, 7.0, NULL, 560.0, 'S', 'A', '7892840822996');
```

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 419344
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
