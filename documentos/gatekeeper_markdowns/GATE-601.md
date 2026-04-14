# GATE-601 - Valores do resumo de venda não batem com o ERP

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: N/A
- Assunto: MXPED - Resumo de Vendas
- Natureza: Dúvida
- Atualizado em: 2025-01-09T08:04:02.351-0300

## Contexto do Problema

## Passos para reproduzir
Login - meta.rca
Acessa resumo de venda, ir pesquisar vendas do mes de dezembro

## Resultado apresentado
Valor não esta batendo com o valor do ERP

## Resultado esperado
Que os valores batem com o ERP

## Descrição
Cliente - VENDA DO VENDEDOR CLAUDIO NÃO ESTÁ BATENDO O VALOR TOTAL DO MÊS DE DEZEMBRO COM O VALOR TOTAL NO MEU ERP, VERIFICA POR FAVOR
-----------------------------------
Verifiquei nas tabelas historicopedc e pedi e os valores não batem.

## Comentarios do Gatekeeper

### 1. 2025-01-09T08:01:23.316-0300 | Filipe do Amaral Padilha

Primeiramente é importante citar que o cálculo realizado no resumo de vendas da Máxima utiliza informações que nós recebemos nos endpoints, ou seja, informações provenientes da integração com o ERP.

No caso deles, a venda faturada está sendo calculada por meio do uso das informações nos endpoints: MXSHISTORICOPEDC(HistoricosPedidosCapas), MXSHISTORICOPEDI(HistoricosPedidosItens), MXSUSUARI(Usuaris) e MXSPRODUT(Produtos).

Então para resolver o problema deles, eles precisam focar em "concertar" as informações que eles nos enviam em alguns desses endpoints que citei acima.

*Abaixo NÃO passar para o cliente, tem o script da venda faturada que retorna o resultado no resumo de vendas. Eu coloquei ele para você realizar a leitura, até testar se quiser e entender como funciona a apuração, observe os critérios, datas, filiais, a posição = 'F', isso que filtra os dados para chegar no resultado.*

--Resumo dos parametros
--CODUSUR = 7348
--DATAINICIO = '01/01/2025'
--DATAINICIO = '31/01/2025'
--FILIAIS = '1','5','7'
--DEDUZDEVOL_VENDA_TRANSMITIDA = N
--DEDUZOUTRASDESP_VENDA_TRANSMITIDA = N
--IGNORARTV5TV11APURACAOMETAS = N
--CRITERIOVENDAFDEDUZIRDEV = N
--CRITERIOVENDALUCROLIQ = N
--REDUZIRST_DADOS_RELATORIO = N
--REDUZIRIPI_DADOS_RELATORIO = N
--CRITERIOVENDAFCONSIDERADEVAVULSA = N
--PERC_COMISSAO_RATEADA = 0
--VALIDAR_APURACAO_NF = N
--CRITERIOVENDA = F
--APURACAO_RESUMO_DTFAT = N

--Consulta:

SELECT
MXSHISTORICOPEDC.CODUSUR,
SUM((MXSHISTORICOPEDI.QT * MXSHISTORICOPEDI.PVENDA)
- (DECODE (OBTER_PARAMETRO('REDUZIRST_DADOS_RELATORIO', NULL, 'N'),'S', MXSHISTORICOPEDI.QT * NVL(MXSHISTORICOPEDI.ST,0),0))
- (DECODE (OBTER_PARAMETRO('REDUZIRIPI_DADOS_RELATORIO', NULL, 'N'), 'S', NVL (MXSHISTORICOPEDI.QT * NVL(MXSHISTORICOPEDI.VLIPI,0), 0), 0))) VLVENDAFATURADA
FROM
MXSHISTORICOPEDC,
MXSHISTORICOPEDI,
MXSUSUARI,
MXSPRODUT
WHERE
MXSHISTORICOPEDI.NUMPED = MXSHISTORICOPEDC.NUMPED
AND MXSHISTORICOPEDC.CODUSUR = MXSUSUARI.CODUSUR
AND MXSHISTORICOPEDI.CODPROD = MXSPRODUT.CODPROD
AND MXSHISTORICOPEDC.DTCANCEL IS NULL
AND DECODE(OBTER_PARAMETRO('APURACAO_RESUMO_DTFAT', NULL, 'N'), 'S', TRUNC(NVL(MXSHISTORICOPEDC.DTFAT, MXSHISTORICOPEDC.DATA)), MXSHISTORICOPEDC.DATA) BETWEEN TRUNC(TO_DATE('01/12/2024', 'DD/MM/YYYY')) AND TRUNC(TO_DATE('31/12/2024', 'DD/MM/YYYY'))
AND MXSHISTORICOPEDC.CODFILIAL IN ('1', '5', '7')
AND MXSHISTORICOPEDC.CODUSUR = 7348
AND MXSHISTORICOPEDC.POSICAO = 'F'
AND NVL(MXSHISTORICOPEDI.POSICAO, MXSHISTORICOPEDC.POSICAO) = 'F'
AND MXSHISTORICOPEDC.CODOPERACAO != 2
AND MXSHISTORICOPEDI.CODOPERACAO != 2
AND MXSUSUARI.CODOPERACAO != 2
AND (OBTER_PARAMETRO('IGNORARTV5TV11APURACAOMETAS',
NULL,
'N') = 'N'
OR OBTER_PARAMETRO('IGNORARTV5TV11APURACAOMETAS',
NULL,
'N') = 'S'
AND MXSHISTORICOPEDC.CONDVENDA NOT IN (5, 11))
AND OBTER_PARAMETRO('VALIDAR_APURACAO_NF',
NULL,
'N') = 'N'
GROUP BY
MXSHISTORICOPEDC.CODUSUR;

--A partir daqui pode passar se quiser, cuidado com as palavras que vai usar com o cliente:

Em anexo eu também coloquei o agrupamento por pedido, dos itens e das quantidades vendidas dentro do período estipulado do RCA 7348. Se você realizar a soma da venda faturada agrupada no Excel vai resultar também no valor total faturado do script.

Então analisando essas informações a gente conclui que não há falhas no cálculo que realizamos. Ele simplesmente é um cálculo que apura venda faturada e é utilizado por vários clientes nossos, ele é bastante consistente, possui uma regra de negócios própria e não precisa de correções.

Então, por que o número fica errado ao comparar com o ERP?
Essa é uma pergunta difícil de responder porque depende de vários fatores a serem analisados:
--É importante saber se o ERP está deduzindo devoluções e bonificações;
--É importante saber se o valor de venda faturada é com ou sem impostos;
--É importante saber se, eles fazem a apuração por DATA de lançamento do pedido ou por DTFAT (Data de Faturamento do pedido);
--Eles precisam revisar a planilha em anexo no quesito dos preços que foram enviados dos itens e quantidades por pedido, para que em comparação com o ERP, saibam se estão nos enviando os mesmos dados que eles tem lá no ERP via API nos nossos endpoints.

Quem deve realizar essa análise?
No momento a Máxima esgotou as possibilidades de análise das informações em nosso ambiente, nós não temos o dever e nem temos acesso a informações confidenciais do ERP para comparar com os nossos endpoints.

Nesse caso, o correto é que o Integrador ou algum responsável capacitado, extraia informações do ERP para comparar com os dados que disponibilizamos dos nossos endpoints em formato Excel. Dessa forma, será possível indentificar a causa da divergência, para que então a Integração do ERP possa realizar a correção no envio das informações.

No final, quando os dados forem corretamente enviados para a Máxima, a apuração do Resumo de Vendas baterá com a do ERP, porém entenda, que isso não depende da Máxima, isso depende da integração do seu ERP nos enviar os dados corretos referentes às vendas realizadas por item, pedido, RCA e data.

## Resposta Canonica

**Conclusão canônica**

Não foi identificada falha no cálculo do **Resumo de Vendas** da Máxima. A apuração da **venda faturada** é feita com base nos dados recebidos da integração do ERP pelos endpoints **MXSHISTORICOPEDC**, **MXSHISTORICOPEDI**, **MXSUSUARI** e **MXSPRODUT**. Na validação realizada, foi informado que a **soma da venda faturada agrupada por pedido em Excel resultou no mesmo valor total retornado pelo script**, o que sustenta que a divergência está, **possivelmente**, nas informações enviadas pelo ERP para esses endpoints.

Os fatores apontados para a diferença entre o valor exibido e o valor do ERP incluem:
- dedução de devoluções e bonificações;
- valor considerado com ou sem impostos;
- apuração por **DATA** ou por **DTFAT**;
- divergências de **preço** e **quantidade** enviados via API.

A Máxima esgotou a análise possível em seu ambiente e não possui acesso às informações internas/confidenciais do ERP para validar a origem da divergência no sistema de origem.

**Parâmetros considerados na apuração**
- `CODUSUR = 7348`
- período: **01/12/2024 a 31/12/2024**
- filiais: `1, 5, 7`
- `CRITERIOVENDA = F`
- `APURACAO_RESUMO_DTFAT = N`
- `DEDUZDEVOL_VENDA_TRANSMITIDA = N`
- `DEDUZOUTRASDESP_VENDA_TRANSMITIDA = N`
- `IGNORARTV5TV11APURACAOMETAS = N`
- `CRITERIOVENDAFDEDUZIRDEV = N`
- `CRITERIOVENDALUCROLIQ = N`
- `REDUZIRST_DADOS_RELATORIO = N`
- `REDUZIRIPI_DADOS_RELATORIO = N`
- `CRITERIOVENDAFCONSIDERADEVAVULSA = N`
- `PERC_COMISSAO_RATEADA = 0`
- `VALIDAR_APURACAO_NF = N`

```sql
SELECT MXSHISTORICOPEDC.CODUSUR,
       SUM((MXSHISTORICOPEDI.QT * MXSHISTORICOPEDI.PVENDA)
           - (DECODE(OBTER_PARAMETRO('REDUZIRST_DADOS_RELATORIO', NULL, 'N'),
                     'S', MXSHISTORICOPEDI.QT * NVL(MXSHISTORICOPEDI.ST,0), 0))
           - (DECODE(OBTER_PARAMETRO('REDUZIRIPI_DADOS_RELATORIO', NULL, 'N'),
                     'S', NVL(MXSHISTORICOPEDI.QT * NVL(MXSHISTORICOPEDI.VLIPI,0), 0), 0))) VLVENDAFATURADA
  FROM MXSHISTORICOPEDC,
       MXSHISTORICOPEDI,
       MXSUSUARI,
       MXSPRODUT
 WHERE MXSHISTORICOPEDI.NUMPED = MXSHISTORICOPEDC.NUMPED
   AND MXSHISTORICOPEDC.CODUSUR = MXSUSUARI.CODUSUR
   AND MXSHISTORICOPEDI.CODPROD = MXSPRODUT.CODPROD
   AND MXSHISTORICOPEDC.DTCANCEL IS NULL
   AND DECODE(OBTER_PARAMETRO('APURACAO_RESUMO_DTFAT', NULL, 'N'),
              'S', TRUNC(NVL(MXSHISTORICOPEDC.DTFAT, MXSHISTORICOPEDC.DATA)),
              MXSHISTORICOPEDC.DATA)
       BETWEEN TRUNC(TO_DATE('01/12/2024', 'DD/MM/YYYY'))
           AND TRUNC(TO_DATE('31/12/2024', 'DD/MM/YYYY'))
   AND MXSHISTORICOPEDC.CODFILIAL IN ('1', '5', '7')
   AND MXSHISTORICOPEDC.CODUSUR = 7348
   AND MXSHISTORICOPEDC.POSICAO = 'F'
   AND NVL(MXSHISTORICOPEDI.POSICAO, MXSHISTORICOPEDC.POSICAO) = 'F'
   AND MXSHISTORICOPEDC.CODOPERACAO != 2
   AND MXSHISTORICOPEDI.CODOPERACAO != 2
   AND MXSUSUARI.CODOPERACAO != 2
   AND (OBTER_PARAMETRO('IGNORARTV5TV11APURACAOMETAS', NULL, 'N') = 'N'
        OR OBTER_PARAMETRO('IGNORARTV5TV11APURACAOMETAS', NULL, 'N') = 'S'
       AND MXSHISTORICOPEDC.CONDVENDA NOT IN (5, 11))
   AND OBTER_PARAMETRO('VALIDAR_APURACAO_NF', NULL, 'N') = 'N'
 GROUP BY MXSHISTORICOPEDC.CODUSUR;
```

**Próximo passo**
O responsável pela integração/ERP deve:
1. extrair os dados do ERP do mesmo período e contexto;
2. comparar com os dados disponibilizados pelos endpoints, preferencialmente agrupando por pedido;
3. revisar preços e quantidades por item/pedido;
4. identificar a causa da divergência;
5. corrigir o envio das informações na integração do ERP, se confirmado desvio nos dados transmitidos.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 415828
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
