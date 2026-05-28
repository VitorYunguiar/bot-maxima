# Comissao no maxPedido

## Metadados

**Palavras-chave**: comissao, maxPedido, PCNFSAID, PCESTCOM, PCNFENT, PCPEDC, PCEMPR, IGNORARTV5TV11APURACAOMETAS, PERC_COMISSAO_RATEADA, CRITERIOVENDAFDEDUZIRDEV

**Sistema**: maxPedido / Winthor

**Area**: Vendas, Comissao, Relatorios

---

## Visao Geral

No maxPedido, o calculo de comissao usa a coluna `COMISSAO` da tabela `PCNFSAID` (notas fiscais). O valor e apurado por periodo, filial e RCA, somando o valor informado nessa coluna.

A coluna `PCNFSAID.COMISSAO` e populada pelo Winthor no momento da geracao da nota fiscal. Por isso, o cliente precisa configurar corretamente o cenario de comissao do RCA no Winthor.

Para validar divergencias, comparar:

- Valor faturado mostrado na rotina 111, que representa o valor real vendido pelo RCA.
- Valor base retornado na rotina de comissao.
- Parametros de apuracao usados no maxPedido.

Qualquer regra de comissao fora desse cenario deve ter a forma de calculo entendida e tratada como melhoria.

---

## Parametrizacoes

| Parametro | Regra |
|-----------|-------|
| `IGNORARTV5TV11APURACAOMETAS` | Informar `N` para considerar as condicoes de venda 5 e 11. Informar `S` para nao usar essas condicoes no calculo. |
| `PERC_COMISSAO_RATEADA` | Se nulo ou igual a 0, o calculo usa apenas `PCNFSAID.COMISSAO`. Se tiver valor diferente de 0 e `PCEMPR.USARATEIOCOMISSAOOPERADOR = 'S'` para a matricula de `PCNFSAID.CODEMITENTEPEDIDO`, o calculo usa `PCNFSAID.COMISSAO * PERC_COMISSAO_RATEADA / 100`. |
| `CRITERIOVENDAFDEDUZIRDEV` | Se nulo ou `N`, nao abate devolucoes da comissao. Se `S`, abate devolucoes e a comissao fica como SQL1 menos SQL2, alem de abatimentos de impostos que nao estao detalhados neste documento. |
| `CODFILIAL` | Filial ou filiais que devem ser consideradas na consulta. |
| `DATAINICIO` | Data inicial da consulta. |
| `DATAFIM` | Data final da consulta. |

---

## SQL 1: Valor de Comissao de Venda

```sql
SELECT
    CODUSUR,
    SUM(COMISSAO) AS VLCOMISSAOVENDA
FROM (
    SELECT DISTINCT
        PCNFSAID.CODFILIAL,
        PCNFSAID.DTSAIDA,
        PCNFSAID.NUMNOTA,
        PCNFSAID.CODCLI,
        PCPEDC.NUMTRANSVENDA,
        DECODE(
            NVL(TO_NUMBER(NVL({PERC_COMISSAO_RATEADA}, 0)), 0),
            0,
            PCNFSAID.COMISSAO,
            CASE
                WHEN (
                    PCPEDC.CODEMITENTE = 8888
                    OR NVL(PCEMPR.USARATEIOCOMISSAOOPERADOR, 'N') = 'N'
                ) THEN PCNFSAID.COMISSAO
                ELSE (PCNFSAID.COMISSAO * TO_NUMBER(NVL({PERC_COMISSAO_RATEADA}, 0)) / 100)
            END
        ) AS COMISSAO,
        PCUSUARI.CODUSUR
    FROM
        PCNFSAID,
        PCPEDC,
        PCCLIENT,
        PCUSUARI,
        PCCOB,
        PCEMPR,
        PCSUPERV
    WHERE PCNFSAID.CODUSUR = PCUSUARI.CODUSUR
      AND PCNFSAID.NUMPED = PCPEDC.NUMPED
      AND PCNFSAID.CODCLI = PCCLIENT.CODCLI
      AND PCNFSAID.CODCOB = PCCOB.CODCOB
      AND PCNFSAID.CODUSUR = {CODUSUR}
      AND PCNFSAID.DTCANCEL IS NULL
      AND PCNFSAID.CONDVENDA IN (1, 2, 3, 7, 14, 9)
      AND (
          {IGNORARTV5TV11APURACAOMETAS} = 'N'
          OR (
              {IGNORARTV5TV11APURACAOMETAS} = 'S'
              AND PCNFSAID.CONDVENDA NOT IN (5, 11)
          )
      )
      AND PCNFSAID.DTSAIDA BETWEEN TRUNC({DATAINICIO}) AND TRUNC({DATAFIM})
      AND NVL(PCNFSAID.CODEMITENTEPEDIDO, PCNFSAID.CODEMITENTE) = PCEMPR.MATRICULA(+)
      AND PCNFSAID.CODFILIAL IN ({CODFILIAL})
)
GROUP BY CODUSUR;
```

---

## SQL 2: Valor de Devolucao de Comissao

Quando `CRITERIOVENDAFDEDUZIRDEV = S`, o valor de devolucao pode ser abatido da comissao.

```sql
SELECT
    SUM(VLESTORNO) AS VLDEVOLUCAOCOMISSAO,
    CODUSUR
FROM (
    SELECT
        PCESTCOM.CODUSUR,
        CASE
            WHEN (
                PCPEDC.CODEMITENTE = 8888
                OR NVL(PCEMPR.USARATEIOCOMISSAOOPERADOR, 'N') = 'N'
            ) THEN PCESTCOM.VLESTORNO
            ELSE (PCESTCOM.VLESTORNO * TO_NUMBER(NVL({PERC_COMISSAO_RATEADA}, 0)) / 100)
        END AS VLESTORNO,
        PCESTCOM.NUMTRANSVENDA
    FROM
        PCESTCOM,
        PCNFENT,
        PCNFSAID,
        PCMOV,
        PCPEDC,
        PCEMPR
    WHERE PCESTCOM.NUMTRANSVENDA = PCPEDC.NUMTRANSVENDA(+)
      AND PCESTCOM.NUMTRANSENT = PCNFENT.NUMTRANSENT
      AND PCESTCOM.NUMTRANSENT = PCMOV.NUMTRANSENT
      AND PCESTCOM.NUMTRANSVENDA = PCNFSAID.NUMTRANSVENDA(+)
      AND PCESTCOM.CODFUNC = PCEMPR.MATRICULA
      AND PCESTCOM.CODUSUR = {CODUSUR}
      AND PCMOV.DTMOV BETWEEN TRUNC({DATAINICIO}) AND TRUNC({DATAFIM})
    GROUP BY
        PCESTCOM.CODUSUR,
        VLESTORNO,
        PCPEDC.CODEMITENTE,
        PCESTCOM.NUMTRANSVENDA,
        PCEMPR.USARATEIOCOMISSAOOPERADOR
)
GROUP BY CODUSUR;
```

---

## Diagnostico de Divergencia

1. Conferir se `PCNFSAID.COMISSAO` foi populada no faturamento.
2. Conferir o periodo usado na consulta.
3. Conferir `CODUSUR` e `CODFILIAL`.
4. Conferir se `IGNORARTV5TV11APURACAOMETAS` esta incluindo ou excluindo TV5 e TV11 conforme esperado.
5. Conferir se existe rateio via `PERC_COMISSAO_RATEADA` e `PCEMPR.USARATEIOCOMISSAOOPERADOR`.
6. Conferir se `CRITERIOVENDAFDEDUZIRDEV` esta abatendo devolucoes.
7. Comparar o resultado com a rotina 111 e com a rotina de comissao do Winthor, considerando que cada rotina pode usar criterio diferente.
