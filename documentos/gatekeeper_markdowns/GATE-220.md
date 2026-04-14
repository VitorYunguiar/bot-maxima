# GATE-220 - RCAs não aparecem nos filtros de Visitas Previstas x Realizadas

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXGESN - Vendas Prevista x Realizada
- Natureza: Dúvida
- Atualizado em: 2024-10-23T15:10:48.680-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar maxGestão da TROIA
>Geolocalização
>Visitas Previstas x Realizadas
>Filtrar mês atual
>Todos supervisores
>Verificar que só aparece um representante

## Resultado apresentado
Os outros RCAs deixaram de aparecer nos filtros

## Resultado esperado
Voltar a aparecer todos os RCAs.

## Descrição
Bom dia Filipe,"

Estou subindo o ticket agora devido o cliente só ter criado agora, o problema é o que comentamos anteriormente, por algum motivo os RCAs sumiram dos filtros de visitas prevista x realizada, estava funcionando até semana passada mas agora só aparece 1 representante.

Tentei verificar as questões mais básicas como codsupervisor, codfilial, se estão ativos, etc... mas não consegui identificar o motivo do problema.

## Comentarios do Gatekeeper

### 1. 2024-10-23T12:48:12.496-0300 | Filipe do Amaral Padilha

--Na apuração de dados do Visitas Previstas Versus Realizadas
--São executadas várias consultas para trazer os dados:
--Primeiro por filial, sendo o CODUSUARIO do Sysmax 18304 (para usar na consulta):
SELECT
CODFILIAL AS CODIGO,
CASE
WHEN CODFILIAL = '99' THEN 'FILIAL 99'
ELSE RAZAOSOCIAL
END AS RAZAOSOCIAL,
FANTASIA,
COUNT (DISTINCT (MXSUSUARI.CODSUPERVISOR)) QTSUPERV,
0 VLVENDA,
0 AS VLVENDAPREV,
0 INATIVOS,
('0') EQUIPES
FROM
MXSUSUARI
INNER JOIN MXSSUPERV S ON
MXSUSUARI.CODSUPERVISOR = S.CODSUPERVISOR
LEFT JOIN MXSFILIAL ON
MXSFILIAL.CODIGO = MXSUSUARI.CODFILIAL
WHERE
CODFILIAL IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = '6'
AND CODUSUARIO = :codusuario)
AND MXSUSUARI.CODSUPERVISOR IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = '5'
AND CODUSUARIO = :codusuario )
AND CODFILIAL <> '0'
AND Funcao_indice (codfilial) IS NOT NULL
AND Funcao_indice (dttermino) IS NULL
AND MXSUSUARI.BLOQUEIO = 'N'
AND S.COD_CADRCA IS NOT NULL
AND S.POSICAO <> 'I'
GROUP BY
CODFILIAL,
RAZAOSOCIAL,
FANTASIA;
--Retorna só a filial 1
--Depois você busca pelos supervisores:

SELECT
CODSUPERVISOR,
NOME,
EQUIPES,
ATIVOS,
AUSENTES,
INATIVOS,
AGENDADOS,
VISITADOS,
POSITIVADOS,
VLVENDA,
VLPREVENDA,
PERCVISITADOS,
PERCPOSITIVADOS,
PERCEFICIENCIA,
VISITADOSA,
POSITIVADOSA,
EFICIENCIAA,
CODIGOGRUPOFILIAL,
CODIGOGRUPOGERENTE,
CODIGOGRUPOCOORDENADOR
FROM
(
SELECT
MX.CODSUPERVISOR,
MX.NOME,
0 EQUIPES,
0 ATIVOS,
0 AUSENTES,
0 INATIVOS,
0 AGENDADOS,
0 VISITADOS,
0 POSITIVADOS,
0 VLVENDA,
0 AS VLPREVENDA,
0 PERCVISITADOS,
0 PERCPOSITIVADOS,
0 PERCEFICIENCIA,
('') VISITADOSA,
('') POSITIVADOSA,
('') EFICIENCIAA,
NVL(F.CODIGO, MXU.CODFILIAL) CODIGOGRUPOFILIAL,
NVL(G.CODGERENTE, '0') CODIGOGRUPOGERENTE,
NVL(C.CODIGO, '0') CODIGOGRUPOCOORDENADOR
FROM
MXSSUPERV MX
LEFT JOIN ERP_MXSCOORDENADORVENDA C
ON
C.CODIGO = MX.CODCOORDENADOR
LEFT JOIN ERP_MXSGERENTE G
ON
G.CODGERENTE = NVL (C.CODGERENTE,
MX.CODGERENTE)
INNER JOIN MXSUSUARI USU
ON
USU.CODUSUR = MX.COD_CADRCA
LEFT JOIN MXSFILIAL F
ON
USU.CODFILIAL = F.CODIGO
LEFT JOIN MXUSUARIOS MXU
ON
MX.CODSUPERVISOR = MXU.CODSUPERV
WHERE
MX.CODSUPERVISOR IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = 5
AND CODUSUARIO = :CODUSUARIO)
AND MX.POSICAO <> 'I'
UNION
SELECT
MX.CODSUPERVISOR,
MX.NOME,
0 EQUIPES,
0 ATIVOS,
0 AUSENTES,
0 INATIVOS,
0 AGENDADOS,
0 VISITADOS,
0 POSITIVADOS,
0 VLVENDA,
0 AS VLPREVENDA,
0 PERCVISITADOS,
0 PERCPOSITIVADOS,
0 PERCEFICIENCIA,
('') VISITADOSA,
('') POSITIVADOSA,
('') EFICIENCIAA,
F.CODIGO CODIGOGRUPOFILIAL,
NVL(G.CODGERENTE, '0') CODIGOGRUPOGERENTE,
NVL(C.CODIGO, '0') CODIGOGRUPOCOORDENADOR
FROM
MXSSUPERV MX
INNER JOIN MXUSUARIOS MXU
ON
MX.CODSUPERVISOR = MXU.CODSUPERV
AND MXU.CODUSUARIO = :CODUSUARIO
LEFT JOIN ERP_MXSCOORDENADORVENDA C
ON
C.CODIGO = MX.CODCOORDENADOR
LEFT JOIN ERP_MXSGERENTE G
ON
G.CODGERENTE = NVL (C.CODGERENTE,
MX.CODGERENTE)
LEFT JOIN MXSFILIAL F
ON
F.CODIGO = MXU.CODFILIAL
WHERE
MX.CODSUPERVISOR IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = 5
AND CODUSUARIO = :CODUSUARIO )
AND MXU.CODFILIAL IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = 6
AND CODUSUARIO = :CODUSUARIO )
AND MX.POSICAO <> 'I'

) V
GROUP BY
CODSUPERVISOR,
NOME,
EQUIPES,
ATIVOS,
AUSENTES,
INATIVOS,
AGENDADOS,
VISITADOS,
POSITIVADOS,
VLVENDA,
VLPREVENDA,
PERCVISITADOS,
PERCPOSITIVADOS,
PERCEFICIENCIA,
VISITADOSA,
POSITIVADOSA,
EFICIENCIAA,
CODIGOGRUPOFILIAL,
CODIGOGRUPOGERENTE,
CODIGOGRUPOCOORDENADOR
ORDER BY
CODSUPERVISOR;

--Vai retornar os 3 supervisores;

--Por fim vai carregar os RCAs (Esse sql eu não ajustei para rodar pq é muitro trabalhoso mas é ele que o maxGestão faz):
WITH USUARIO AS
(SELECT * FROM
(SELECT MXSUSUARI.codusur,(:PDATAINICIAL) as data,nvl(MXSUSUARI.codfilial,0) codfilial,
--usa este sql para não trazer duplicidade quando esta amarrado em mais de 1 usuario
nvl((SELECT MIN(codusuario) FROM mxsusuarios WHERE codusur = MXSUSUARI.codusur and status <> 'I'),0) codusuario
FROM MXSUSUARI
INNER JOIN MXSSUPERV ON MXSSUPERV.codsupervisor = MXSUSUARI.codsupervisor and MXSSUPERV.posicao = 'A' and MXSUSUARI.bloqueio = 'N'
{PARAMFILTRARPORSUPERV}
INNER JOIN mxacessodados z ON  MXSSUPERV.codsupervisor = z.keydados
and z.coddados = 5
and z.codusuario = :codusuario
WHERE codfilial <> '0' and codfilial is not null and (trunc(MXSUSUARI.dttermino) > trunc(:PDATAINICIAL) OR dttermino is null)
GROUP BY MXSUSUARI.codusur, codfilial)
WHERE codusuario >0), --filtra apenas os que tiverem ligação com a mxsusuarios

LOCALIZACAO AS
(SELECT   "CODUSUARIO",
"CODUSUR",
"DATA",
"CODFILIAL",
"RNK"
FROM   (SELECT   mxs.codusuario,
US.codusur,
US.codfilial,
mxs.data,
RANK () OVER (PARTITION BY mxs.codusuario ORDER BY mxs.data DESC) AS rnk
FROM USUARIO US
LEFT JOIN mxslocation mxs ON mxs.codusuario = US.codusuario AND mxs.DATA <= SYSDATE and trunc(mxs.data) = trunc(US.data))
WHERE   rnk = 1)

SELECT mxs.codusuario,mxs.nome,(mxs.nome) nomerca,
ativos, agendados,visitados,positivados,vlvenda,vlprevenda,
round(get_percentual(visitados, agendados) * 100,2) percvisitados,
round(get_percentual(positivados , agendados) * 100,2) percpositivados,
round(get_percentual(positivados , visitados) * 100,2) perceficiencia,
('') visitadosA,('') positivadosA,('') eficienciaA,('')indexmapa,
ultposicao,primeirocliente,ultcliente,versao,
US.codusur,
ROUND((select sum(distancia) from mxslocation where codusuario = US.codusuario
AND DATA <= SYSDATE
and  trunc(data) = trunc(US.data)) / 1000,2) kmrodado --encontrada em metro e convertido para km
FROM mxsusuarios mxs,usuario US, (
SELECT pcu.codusur,pcu.nome,
sum(nvl(tbequipes.ativos,0)) ativos,
sum(nvl(tbdadoscli.agendados,0)) agendados,
sum(nvl(tbdadoscli.visitado,0) + nvl(tbdadoscli.visitado1,0) + nvl(tbdadoscli.visitado2,0)) visitados,
sum(nvl(tbpositivados.qtpositivados,0) + nvl(0,0)) positivados,
sum(nvl(tbpositivados.vlatend,0)) vlvenda,
sum(nvl(0,0)) vlprevenda,
max(DECODE(nvl(ultposicao,0),'0','00:00',ultposicao)) ultposicao,
min(DECODE(nvl(primeirocliente,0),'0','00:00',primeirocliente)) primeirocliente,
max(DECODE(nvl(ultcliente,0),'0','00:00',ultcliente)) ultcliente,
min(primeirocliente) primeiro,max(ultcliente) ultimo,
max(versao) versao
FROM MXSUSUARI pcu,
(SELECT codusur, ativos, ultposicao, versao
FROM
(SELECT codusur,
(CASE WHEN NVL(codusuario,0) = 0 THEN 2 --0 - ativo 1 - inativo 2 - ausente
WHEN (SYSDATE - data) * 1440 < 30  THEN 0 ELSE 1 END) ativos,
to_char(data, 'HH24:MI') as ultposicao,
data,
(select appversion FROM ((SELECT appversion,codusuario from mxsaparelhosconnlog WHERE trunc(dtinicioconexao) BETWEEN  trunc(:PDATAINICIAL) AND trunc(:PDATAFINAL)  order by numconexao desc))
where rownum = 1 and codusuario = US.codusuario) as versao
FROM LOCALIZACAO US
WHERE 1=1)
group by codusur, ativos, ultposicao, versao) tbequipes,
(SELECT codusur,
sum((SELECT count(codcli) FROM mxscompromissosmov mxs WHERE mxs.CODUSUARIO = US.CODUSUARIO AND trunc(mxs.data) = trunc(US.data))) Agendados,
sum((SELECT count(DISTINCT codcli)
FROM MXSHISTORICOPEDC
WHERE MXSHISTORICOPEDC.codusur = US.codusur  AND TRUNC (MXSHISTORICOPEDC.dtaberturapedpalm)= trunc(US.data)
{PARAMEMITIDORCA}
AND MXSHISTORICOPEDC.CODOPERACAO <> 2
and MXSHISTORICOPEDC.codcli NOT IN
(SELECT distinct pfv.codcli
FROM ERP_MXSVISITAFV pfv, MXSCLIENT
WHERE MXSCLIENT.codcli = pfv.codcli and pfv.CODUSUR = US.codusur
and trunc(pfv.DATA) =  trunc(US.data))))  as visitado,
sum((SELECT count(pfv.codcli)
FROM ERP_MXSVISITAFV pfv, MXSCLIENT
WHERE MXSCLIENT.codcli = pfv.codcli and pfv.CODUSUR = US.codusur
and trunc(pfv.DATA) =  trunc(US.data) GROUP BY pfv.codusur)) as visitado1,

SUM ((SELECT count(MXSINTEGRACAOPEDIDO.codcli) FROM MXSINTEGRACAOPEDIDO, MXSCLIENT
WHERE MXSINTEGRACAOPEDIDO.status = 6
AND MXSCLIENT.CODCLI = MXSINTEGRACAOPEDIDO.CODCLI
AND MXSINTEGRACAOPEDIDO.CODUSUR = US.cod_usur
AND TRUNC(MXSINTEGRACAOPEDIDO.DATA) = trunc(US.data)
GROUP BY MXSINTEGRACAOPEDIDO.codusur))
/*
sum((SELECT count(mxsgeo.codcli)
FROM mxsgeopedido mxsgeo, MXSCLIENT
WHERE MXSCLIENT.codcli = mxsgeo.codcli and mxsgeo.CODUSUR = US.codusur
and trunc(mxsgeo.DATA) =  trunc(US.data) GROUP BY mxsgeo.codusur))
*/
as visitado2,
MIN((SELECT min(primeirocliente) FROM
(SELECT TO_CHAR(TO_DATE('01/01/1900 ' || pfv.horainicial || ':' || pfv.minutoinicial,'DD/MM/YYYY HH24:MI:SS'),'HH24:MI') PrimeiroCliente,codusur
FROM ERP_MXSVISITAFV pfv, MXSCLIENT WHERE MXSCLIENT.codcli = pfv.codcli and (CODUSUR,trunc(DATA)) in (select codusur,trunc(data) from usuario)
UNION
SELECT TO_CHAR(data,'HH24:MI'), codusur
FROM mxslocation WHERE tipo = 'Checkin' AND DATA <= SYSDATE and (CODUSUR,trunc(DATA)) in (select codusur,trunc(data) from usuario)) where codusur = US.codusur GROUP BY codusur )) PrimeiroCliente,
MAX((SELECT max(ultimocliente) FROM
(SELECT TO_CHAR(TO_DATE('01/01/1900 ' || pfv.horafinal || ':' || pfv.minutofinal,'DD/MM/YYYY HH24:MI:SS'),'HH24:MI') ultimocliente,codusur
FROM ERP_MXSVISITAFV pfv,MXSCLIENT WHERE MXSCLIENT.codcli = pfv.codcli and  (CODUSUR,trunc(DATA)) in (select codusur,trunc(data) from usuario)
UNION
SELECT TO_CHAR(data,'HH24:MI'), codusur
FROM mxslocation WHERE tipo = 'Checkout' AND DATA <= SYSDATE and (CODUSUR,trunc(DATA)) in (select codusur,trunc(data) from usuario)) where codusur = US.codusur GROUP BY codusur )) ultcliente
FROM USUARIO US
WHERE 1 = 1
GROUP BY codusur) tbdadoscli,
(SELECT MXSHISTORICOPEDC.codusur, SUM (Decode (MXSHISTORICOPEDC.condvenda, 5, 0,
6, 0,
11, 0,
12, 0,
MXSHISTORICOPEDC.vlatend))  AS vlatend,
count(DISTINCT MXSHISTORICOPEDC.codcli) qtpositivados
FROM MXSHISTORICOPEDC, USUARIO US
WHERE MXSHISTORICOPEDC.CONDVENDA NOT IN (4,5,6,8,10,11,12,13,20,98,99)
AND MXSHISTORICOPEDC.DTCANCEL IS NULL
AND TRUNC (MXSHISTORICOPEDC.dtaberturapedpalm)= trunc(US.data)
AND MXSHISTORICOPEDC.codusur = US.codusur
AND MXSHISTORICOPEDC.CODOPERACAO <> 2
{PARAMEMITIDORCA}
GROUP BY MXSHISTORICOPEDC.codusur) tbpositivados
WHERE tbequipes.codusur (+) = pcu.codusur
and tbdadoscli.codusur (+) = pcu.codusur
and tbpositivados.codusur(+) = pcu.codusur
group by pcu.codusur, pcu.nome) DADOS
WHERE US.codusur = DADOS.codusur
AND mxs.codusuario = US.codusuario
{PARAMFILTRARPORRCA}
ORDER BY codusuario ASC

--Então por isso que ao executar ela retorna somente 1 RCA.

--Abaixo eu dividi as regras por tabela para melhor entendimento:

--Então por exemplo, primeiro a gente desconsidera os Supervisores inativos e também que não possuem COD_CADRCA no cadastro:

SELECT * FROM MXSSUPERV WHERE CODOPERACAO != 2 AND POSICAO IN('A') AND COD_CADRCA IS NOT NULL;
--Ficamos somente com os supervisores 1,6,8

--Depois a gente vai trazer os vendedores que estão ativos, ou seja DTTERMINO IS NULL e que estão vinculados nesses 3 supervisores.
SELECT * FROM MXSUSUARI WHERE CODSUPERVISOR IN(1,6,8) AND DTTERMINO IS NULL AND CODOPERACAO != 2;
--Obtemos 4 RCAs;
--Por fim vamos buscar na MXSUSUARIOS usuários com licença do maxPedido ativa:
SELECT * FROM MXSUSUARIOS WHERE CODUSUR IN(29, 1, 95, 120) AND STATUS IN('A');
--Obtemos somente a RCA MANUELA R DA SILVA no código de usuário 18373

--Então o que ele precisa fazer para resolver e ver mais RCAs lá?
--1° Ele precisa colocar todos os supervisores vinculados a algum COD_CADRCA na Rotina 516
--2° Ele precisa verificar se os RCAs que ele associou aos supervisores, se eles possuem CODFILIAL vinculado 99 ou alguma outra filial específica.
--3° Os RCAs que ele deseja visualizar precisam ter uma licença do maxPedido e estarem ativos

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: llm_processing_failed
- Comentarios primarios: 402599
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Unterminated string starting at: line 1 column 4588 (char 4587)
