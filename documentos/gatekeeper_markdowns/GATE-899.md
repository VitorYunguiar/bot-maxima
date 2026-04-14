# GATE-899 - Validar cálculo do painel geral

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: PROTON
- Assunto: MXGESN - Painel Geral - Dados Divergentes do ERP
- Natureza: Dúvida
- Atualizado em: 2025-03-07T10:26:40.964-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar maxGestão
>Painel Geral
>Filtrar 01/02/2025 até 28/02/2025
>Todos tipos de venda, pedidos e clientes
>Deduzir devoluções
>Observar o valor apresentado no painel geral
>Observar no anexo o valor apresentado no ERP

--OBS: Segundo o cliente, o valor que mais se aproxima é quando o filtro é feito por data de faturamento do pedido

## Resultado apresentado
O valor do painel geral do Gestão está maior do que no ERP.

Validei o valor das devoluções e a diferença entre o ERP e o painel geral é de apenas R$ 560.

Já a diferença no valor das vendas é em torno de R$ 72 mil.

## Resultado esperado
Gostaria de ajuda para que fosse validado se o cálculo feito pelo maxGestão para exibir o Painel Geral está correto, uma vez que o cliente mostrou não estar batendo com o ERP.

## Descrição
Bom dia Gatekeepers,

Gostaria de ajuda para que fosse validado se o cálculo feito pelo maxGestão para exibir o Painel Geral está correto, uma vez que o cliente mostrou não estar batendo com o ERP.

Tentei rodar o SQL do painel geral porém mesmo trocando o CODUSUARIO e as datas o SQL retorna 0 pra mim.

Com o cálculo estando correto e batendo com o maxGestão podemos evidenciar ao cliente que estamos apenas exibindo o que chegou do ERP via API de integração.

## Comentarios do Gatekeeper

### 1. 2025-03-07T10:26:07.504-0300 | Filipe do Amaral Padilha

--Nos anexos eu coloquei as planilhas com os cálculos por pedido dentro do período selecionado, esperamos que com esses dados o ERP faça uma apuração dos dados internos do banco do ERP e também consiga comparar com os dados enviados para o nosso banco via API, para que assim possam identifiar as divergências e realizar o entendimento de como calculamos

--OBS: não passar as consultas inteiras da Máxima, só alguns detalhes, as consultas são propriedades intelectuais da Máxima.

--VALOR SEM DEDUZIR = 2006552.19
--VALOR DAS DEVOLUCOES = 6.984.31
Você pode fazer assim SELECT (2006552.19 - 6984.31) FROM DUAL; (terá o resultado do painel de auditoria)

--Como apuramos para chegar nessa informação consulta somente da parte de venda transmitida:

SELECT
-- Soma do QT * PVENDA, excluindo certas condições de venda e arredondando para 2 casas decimais
SUM(NVL(DECODE(VENDAS.CONDVENDA, 6, 0, 11, 0, 12, 0, ROUND((ITEMPED.QT * ITEMPED.PVENDA), 2) - 0 - 0), 0)) - 0 AS VALORTOTAL
FROM
MXSHISTORICOPEDC VENDAS
-- Faz a junção com a tabela de itens do pedido, garantindo que o pedido exista na MXSHISTORICOPEDC
INNER JOIN MXSHISTORICOPEDI ITEMPED ON VENDAS.NUMPED = ITEMPED.NUMPED
-- Faz a junção com a tabela de usuários para validar a existência do RCA
INNER JOIN MXSUSUARI US ON VENDAS.CODUSUR = US.CODUSUR
-- Faz um LEFT JOIN para trazer dados da MXSINTEGRACAOPEDIDO se houver correspondência
LEFT JOIN (
-- Seleciona pedidos distintos da MXSINTEGRACAOPEDIDO com supervisores válidos dentro do período
SELECT DISTINCT NUMPEDERP, CODSUPERVISOR, CODUSUR
FROM MXSINTEGRACAOPEDIDO
WHERE CODSUPERVISOR IS NOT NULL
-- Filtra por datas dentro do mês de fevereiro de 2025
AND TRUNC(DATA) BETWEEN TO_DATE('01/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
AND TO_DATE('28/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
-- Garante que o usuário tenha permissão de acesso aos dados do supervisor e filial
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '80445' AND CODDADOS = '5' AND MXSINTEGRACAOPEDIDO.CODSUPERVISOR = KEYDADOS)
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '80445' AND CODDADOS = '6' AND MXSINTEGRACAOPEDIDO.CODFILIAL = KEYDADOS)
AND CODSUPERVISOR IS NOT NULL
) MXSI ON MXSI.NUMPEDERP = VENDAS.NUMPED AND MXSI.CODUSUR = VENDAS.CODUSUR
WHERE
-- Exclui certos tipos de condição de venda
VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)
-- Considera apenas pedidos que não foram cancelados
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
-- Filtra pedidos criados dentro do período de fevereiro de 2025
AND TRUNC(VENDAS.DATA) BETWEEN TO_DATE('01/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
AND TO_DATE('28/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
-- Garante que o usuário tenha acesso à filial do pedido
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '80445' AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)
-- Valida acesso ao supervisor do pedido
AND EXISTS(
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445' AND KEYDADOS = VENDAS.CODSUPERVISOR
UNION ALL
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445' AND KEYDADOS = MXSI.CODSUPERVISOR AND VENDAS.CODSUPERVISOR IS NULL
)
-- Exclui operações canceladas
AND VENDAS.CODOPERACAO <> 2
AND ITEMPED.CODOPERACAO <> 2
-- Exclui pedidos e itens com posição cancelada
AND VENDAS.POSICAO <> 'C'
AND NVL(ITEMPED.POSICAO, 'L') <> 'C'
-- Filtra apenas pedidos com condição de venda igual a 1
AND VENDAS.CONDVENDA IN (1);

--Basicamente pegamos a soma dos itens dos pedidos da MXSHISTORICOPEDI e fazendo validações com a MXSHISTORICOPEDC sendo:
--MXSHISTORICOPEDI a soma do QT * PVENDA com arredondamento de 2 casas decimais
--Validando se o pedido existe na MXSHISTORICOPEDC
--Apura só os dados que foram filtrados e que o usuário possui acesso quanto à equipes e Filiais

--Reduzi ela para ficar mais fácil de entender:

SELECT VENDAS.NUMPED,
SUM(NVL(DECODE(VENDAS.CONDVENDA, 6, 0, 11, 0, 12, 0, ROUND((ITEMPED.QT * ITEMPED.PVENDA), 2) - 0 - 0), 0)) - 0 AS VALORTOTAL
FROM
MXSHISTORICOPEDC VENDAS
INNER JOIN MXSHISTORICOPEDI ITEMPED ON VENDAS.NUMPED = ITEMPED.NUMPED
INNER JOIN MXSUSUARI US ON VENDAS.CODUSUR = US.CODUSUR
WHERE
VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND TRUNC(VENDAS.DATA) BETWEEN TO_DATE('01/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
AND TO_DATE('28/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '80445' AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)
AND EXISTS(
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445' AND KEYDADOS = VENDAS.CODSUPERVISOR
)
AND VENDAS.CODOPERACAO <> 2
AND ITEMPED.CODOPERACAO <> 2
AND VENDAS.POSICAO <> 'C'
AND NVL(ITEMPED.POSICAO, 'L') <> 'C'
AND VENDAS.CONDVENDA IN (1)
GROUP BY VENDAS.NUMPED;

--Eles teriam que pegar esses pedidos e fazer um cálculo interno NO ERP agrupando por pedido assim para comparar com o que eles enviam para a gente via integração e assim identificar os pontos de divergência para mandar a correção dos envios dos dados para a nossa nuvem

--Para o cálculo das devoluções considera as datas da DTENT da ERP_MXSNFENT

Considera pedidos com CONDVENDA que não sejam de 6 e 11 da tabela

Considera a QT * PUNIT do endpoint ERP_MXSMOV

Também só apura dados de devolução através do conceito

AND ERP_MXSMOV.CODOPER = 'ED'

Se precisar de mais detalhes de como é apurada a devolução tem no script explicando ponto a ponto, mas basicamente eles já fazem o envio desses dados da integração deles, eles só precisam verificar se tem alguma informação que não está sendo enviada para a nossa nuvem em conformidade.

Se eles precisarem de como a informação está gravada em algum endpoint específico você pode consultar e mandar para eles, às vezes a divergência pode estar sendo causada porque uma devolução está sem, por exemplo, o conceito de AND ERP_MXSMOV.CODOPER = 'ED' definido no registro.

Se precisar ainda tirar mais dúvidas comigo sobre esse assunto e analisar mais algum detalhe pode me chamar diretamente que eu analiso.

WITH AA AS (
-- Seleciona os dias úteis dentro do período especificado
SELECT A.DATA
FROM MXDIASUTEIS A
WHERE DATA BETWEEN TO_DATE('01/02/2025', 'dd/mm/yyyy') AND TO_DATE('28/02/2025', 'dd/mm/yyyy')
GROUP BY A.DATA
),

B AS (
-- Relaciona cada dia útil ao seu respectivo mês/ano
SELECT DIAUTIL, TO_CHAR(A.DATA,'MM/YYYY') AS DATA
FROM MXDIASUTEIS A
JOIN AA ON A.DATA = AA.DATA
),

A AS (
-- Calcula o valor total das devoluções dentro do período
SELECT
DEVOL.DATA AS DATA,
DECODE('S','N',0,SUM(DEVOL.VLDEVOLUCAO -  0 - 0 - DEVOL.VLREPASSE)) VLTOTAL
FROM (
-- Obtém valores das notas fiscais de entrada (devoluções)
SELECT TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY') AS DATA,
NVL(
SUM(
CASE
-- Exclui certas condições de venda
WHEN ERP_MXSNFSAID.CONDVENDA IN (6,11) THEN 0
ELSE
( NVL (ERP_MXSMOV.QT, 0) * (  NVL (ERP_MXSMOV.PUNIT, 0) +
NVL (ERP_MXSMOV.VLFRETE, 0) +
NVL (ERP_MXSMOV.VLOUTRASDESP, 0) +
NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) +
NVL (ERP_MXSMOV.VLOUTROS, 0) -
NVL (ERP_MXSMOV.VLREPASSE, 0) ))
END
),
0
) AS VLDEVOLUCAO,
-- Calcula valores de ST, IPI e repasse
NVL(SUM(NVL (ERP_MXSMOV.QT, 0) * NVL (ERP_MXSMOV.ST, 0)),0) VLST,
NVL(SUM(NVL(ERP_MXSMOV.VLIPI, 0) * NVL (ERP_MXSMOV.QT, 0)),0) VLIPI,
NVL(ROUND(SUM(ERP_MXSMOV.QT * ERP_MXSMOV.VLREPASSE), 2), 0) VLREPASSE
FROM ERP_MXSNFENT,
ERP_MXSESTCOM,
ERP_MXSTABDEV,
MXSCLIENT,
MXSEMPR,
MXSUSUARI,
MXSSUPERV,
MXSFORNEC F,
ERP_MXSNFSAID,
ERP_MXSMOV,
MXSPRODUT,
ERP_MXSDEVCONSUM,
MXSHISTORICOPEDC VENDAS
WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT(+)
-- Relaciona a devolução com a tabela de devoluções cadastradas
AND ERP_MXSNFENT.CODDEVOL = ERP_MXSTABDEV.CODDEVOL(+)
AND MXSCLIENT.CODCLI = ERP_MXSNFENT.CODFORNEC
AND ERP_MXSNFENT.NUMTRANSENT = ERP_MXSDEVCONSUM.NUMTRANSENT(+)
-- Relaciona com motorista, usuários e supervisores
AND ERP_MXSNFENT.CODMOTORISTADEVOL = MXSEMPR.MATRICULA(+)
AND ERP_MXSNFENT.CODUSURDEVOL = MXSUSUARI.CODUSUR
AND MXSUSUARI.CODSUPERVISOR = MXSSUPERV.CODSUPERVISOR(+)
-- Relaciona movimentações de estoque com os produtos
AND TO_NUMBER(ERP_MXSESTCOM.NUMTRANSENT) = ERP_MXSMOV.NUMTRANSENT
AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD(+)
-- Exclui registros cancelados
AND NVL(TO_CHAR(ERP_MXSMOV.DTCANCEL,'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND NVL (ERP_MXSMOV.CODOPER, 'ED') = 'ED'
-- Filtra apenas registros dentro do período de fevereiro de 2025
AND TRUNC(ERP_MXSNFENT.DTENT) BETWEEN TO_DATE('01/02/2025', 'dd/mm/yyyy') AND TO_DATE('28/02/2025', 'dd/mm/yyyy')
-- Considera apenas determinados tipos de descarga e notas fiscais
AND ERP_MXSNFENT.TIPODESCARGA IN ('6','7','T')
AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA'
AND ERP_MXSNFENT.CODFISCAL IN ('131','132','231','232','199','299')
-- Relaciona vendas e condições de venda
AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+)
AND NVL(ERP_MXSNFSAID.CONDVENDA,0) NOT IN (4, 8, 10, 13, 20, 98, 99)
-- Filtra acesso do usuário a supervisores e filiais
AND MXSUSUARI.CODSUPERVISOR IN (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445')
AND ERP_MXSESTCOM.NUMTRANSVENDA = VENDAS.NUMTRANSVENDA(+)
AND ERP_MXSNFENT.CODFILIAL IN (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '6' AND CODUSUARIO = '80445')
-- Relaciona fornecedor
AND F.CODFORNEC(+) = ERP_MXSNFENT.CODFORNEC
-- Considera apenas pedidos com condição de venda igual a 1
AND ERP_MXSNFSAID.CONDVENDA IN (1)
GROUP BY TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY')
) DEVOL
GROUP BY DEVOL.DATA
)

-- Seleciona os dados finais
SELECT
'DEVOL' SERIE,
NVL(B.DATA, A.DATA) DATA,
B.DIAUTIL DIAUTIL,
NVL(A.VLTOTAL,0) VLTOTAL
FROM A
LEFT JOIN B ON A.DATA = B.DATA
GROUP BY NVL(B.DATA, A.DATA), B.DIAUTIL, VLTOTAL, 'DEVOL'

--------------------

A baixo agrupado por pedido e a consulta reduzida para melhor entendimento

SELECT
DEVOL.DATA AS DATA,
DEVOL.NUMPED,
DECODE('S','N',0,SUM(DEVOL.VLDEVOLUCAO -  0 - 0 - DEVOL.VLREPASSE)) VLTOTAL
FROM (
-- Obtém valores das notas fiscais de entrada (devoluções)
SELECT TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY') AS DATA,
VENDAS.NUMPED,
NVL(
SUM(
CASE
-- Exclui certas condições de venda
WHEN ERP_MXSNFSAID.CONDVENDA IN (6,11) THEN 0
ELSE
( NVL (ERP_MXSMOV.QT, 0) * (  NVL (ERP_MXSMOV.PUNIT, 0) +
NVL (ERP_MXSMOV.VLFRETE, 0) +
NVL (ERP_MXSMOV.VLOUTRASDESP, 0) +
NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) +
NVL (ERP_MXSMOV.VLOUTROS, 0) -
NVL (ERP_MXSMOV.VLREPASSE, 0) ))
END
),
0
) AS VLDEVOLUCAO,
-- Calcula valores de ST, IPI e repasse
NVL(SUM(NVL (ERP_MXSMOV.QT, 0) * NVL (ERP_MXSMOV.ST, 0)),0) VLST,
NVL(SUM(NVL(ERP_MXSMOV.VLIPI, 0) * NVL (ERP_MXSMOV.QT, 0)),0) VLIPI,
NVL(ROUND(SUM(ERP_MXSMOV.QT * ERP_MXSMOV.VLREPASSE), 2), 0) VLREPASSE
FROM ERP_MXSNFENT,
ERP_MXSESTCOM,
ERP_MXSTABDEV,
MXSCLIENT,
MXSEMPR,
MXSUSUARI,
MXSSUPERV,
MXSFORNEC F,
ERP_MXSNFSAID,
ERP_MXSMOV,
MXSPRODUT,
ERP_MXSDEVCONSUM,
MXSHISTORICOPEDC VENDAS
WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT(+)
-- Relaciona a devolução com a tabela de devoluções cadastradas
AND ERP_MXSNFENT.CODDEVOL = ERP_MXSTABDEV.CODDEVOL(+)
AND MXSCLIENT.CODCLI = ERP_MXSNFENT.CODFORNEC
AND ERP_MXSNFENT.NUMTRANSENT = ERP_MXSDEVCONSUM.NUMTRANSENT(+)
-- Relaciona com motorista, usuários e supervisores
AND ERP_MXSNFENT.CODMOTORISTADEVOL = MXSEMPR.MATRICULA(+)
AND ERP_MXSNFENT.CODUSURDEVOL = MXSUSUARI.CODUSUR
AND MXSUSUARI.CODSUPERVISOR = MXSSUPERV.CODSUPERVISOR(+)
-- Relaciona movimentações de estoque com os produtos
AND TO_NUMBER(ERP_MXSESTCOM.NUMTRANSENT) = ERP_MXSMOV.NUMTRANSENT
AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD(+)
-- Exclui registros cancelados
AND NVL(TO_CHAR(ERP_MXSMOV.DTCANCEL,'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND NVL (ERP_MXSMOV.CODOPER, 'ED') = 'ED'
-- Filtra apenas registros dentro do período de fevereiro de 2025
AND TRUNC(ERP_MXSNFENT.DTENT) BETWEEN TO_DATE('01/02/2025', 'dd/mm/yyyy') AND TO_DATE('28/02/2025', 'dd/mm/yyyy')
-- Considera apenas determinados tipos de descarga e notas fiscais
AND ERP_MXSNFENT.TIPODESCARGA IN ('6','7','T')
AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA'
AND ERP_MXSNFENT.CODFISCAL IN ('131','132','231','232','199','299')
-- Relaciona vendas e condições de venda
AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+)
AND NVL(ERP_MXSNFSAID.CONDVENDA,0) NOT IN (4, 8, 10, 13, 20, 98, 99)
-- Filtra acesso do usuário a supervisores e filiais
AND MXSUSUARI.CODSUPERVISOR IN (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445')
AND ERP_MXSESTCOM.NUMTRANSVENDA = VENDAS.NUMTRANSVENDA(+)
AND ERP_MXSNFENT.CODFILIAL IN (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '6' AND CODUSUARIO = '80445')
-- Relaciona fornecedor
AND F.CODFORNEC(+) = ERP_MXSNFENT.CODFORNEC
-- Considera apenas pedidos com condição de venda igual a 1
AND ERP_MXSNFSAID.CONDVENDA IN (1)
GROUP BY TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY'), VENDAS.NUMPED
) DEVOL
GROUP BY DEVOL.DATA, DEVOL.NUMPED

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 428291
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Validação realizada com base na lógica de apuração do Painel Geral e nos cálculos comparativos por pedido do período informado." — o texto-fonte não usa a expressão "Painel Geral". | "Conclusão técnica: a divergência é compatível com diferença entre os dados internos do ERP e os dados enviados para a nuvem via API de integração, tanto em vendas quanto em devoluções." — o texto-fonte diz que a comparação deve ser feita para identificar divergências, mas não afirma como conclusão que a divergência de fato é essa. | "Há indicação específica de que uma devolução pode estar sem o conceito `CODOPER = 'ED'` no registro, o que impediria sua apuração no cálculo do Gestão." — o texto-fonte dá isso apenas como exemplo possível ("por exemplo"), e não como indicação específica confirmada; também não menciona "cálculo do Gestão". | "Responsável pela validação e correção: ERP." — o texto-fonte não atribui formalmente essa responsabilidade. | "Se ainda restarem dúvidas, o caso deve ser direcionado ao gatekeeper." — o texto-fonte diz apenas "pode me chamar diretamente", sem mencionar gatekeeper.
