# GATE-743 - Acréscimo Flex.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Não Informado
- Assunto: MXPED - Conta Corrente
- Natureza: Dúvida
- Atualizado em: 2025-02-05T10:57:25.466-0300

## Contexto do Problema

## Passos para reproduzir
>> Analisar os pedido em anexo (518354,518362)

## Resultado apresentado
>>está sendo mandando um acréscimo do sintec para o max, sem o vendedor ter movimentado a conta corrente

## Resultado esperado
>> Não mandar o acréscimo para ERP

## Descrição
*_Cliente _*- Ainda está sendo mandando um acréscimo do sintec para o max, sem o vendedor ter movimentado a conta corrente.

Esses 2 ai já foi depois que eu havia zerado a conta e ia fazer o teste

## Comentarios do Gatekeeper

### 1. 2025-02-04T18:13:51.039-0300 | Filipe do Amaral Padilha

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518354,518362);

SELECT ROUND(PBASERCA,2), ROUND(PVENDA,2),CODPROD FROM MXSHISTORICOPEDI WHERE NUMPED = 518354;

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA IN(3371);

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518354,518362);

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%CON_TIPOMOVCCRCA%';

SELECT C.NUMPED,
NVL(C.NUMPEDRCA,'0') NUMPEDRCA,
C.CODCLI,
C.CODUSUR,
C.CODFILIAL,
C.POSICAO,
C.CONDVENDA
FROM MXSHISTORICOPEDC C
INNER JOIN MXSUSUARI U
ON U.CODUSUR = C.CODUSUR AND U.CODOPERACAO != 2
WHERE C.DTATUALIZ >= TRUNC(SYSDATE) - 1
AND NVL(C.NUMPED,0) != 0
/* FLAG PROCESSARCC CRIADA PARA N¿O FICAR REPROCESSANDO QUANDO O PEDIDO FOR FATURADO OU CANCELADO */
AND NVL(C.PROCESSARCC,'S') = 'S'
AND NUMPED = 518354
ORDER BY C.NUMPED

SELECT
I.CODPROD,
NVL(I.QT, 0) QUANTIDADE,
ROUND(NVL(I.PBASERCA, I.PTABELA), 2) PRECOBASE,
ROUND(I.PVENDA, 2) PRECOVENDA,
CASE
WHEN I.PVENDA > I.PTABELA THEN 'C'
ELSE 'D'
END TIPOOPER,
NVL(I.NUMSEQ, 1) SEQUENCIA
FROM
MXSHISTORICOPEDI I
WHERE
NUMPED = 518354
ORDER BY
I.NUMSEQ

### 2. 2025-02-05T10:57:25.463-0300 | Filipe do Amaral Padilha

Foi analisado o cenário do cliente referente aos pedidos citados e constatado que atualmente a Máxima não atende ao cenário de movimentação de Conta Corrente através da PKG.

Porque o Preço de base deles é utilizado e salvo para comparação do preço de venda ao faturar o pedido. Porém nesse preço base, não ocorre o cálculo do acréscimo de boleto que eles fazem posteriormente dentro do ERP.

Atualmente eu pensei em duas alternativas, mas não sei sobre a viabilidade, são apenas ideias:

1° Eles teriam que integrar com a gente esse acréscimo especificamente para boletos de forma que isso vá calculado no PrecoBase do maxPedido e também no PrecoVenda. Assim na hora da PKG movimentar já estaria considerando o acréscimo. Porém isso mexe também na regra de negócios deles, porque os RCAs estariam já informando diratamente o preço final para os clientes durante a venda.

2° A gente teria que fazer uma melhoria na PKG, parametrizável, para quando o houver recálculo no ERP, eles nos mandam isso já na MXSHISTORICOPEDI, o PBASERCA e PVENDA corretos, a gente pegaria da MXSHISTORICOPEDI as informaçõs do ERP para realizar a comparação e mover conta corrente. Atualmente a gente pega da ERP_MXSLOGRCA que ficou gravado já na transmissão do pedido (maxPedido), por isso dá divergência entre pvenda e pbase e movimenta conta corrente.
======================
OBS IMPORTANTE: Por enquanto pausa o ticket dele e informa que está sendo analisado pelo desenvolvimento o assunto. (Na verdade está rolando o e-mail interno que eu escalei o assunto) .

Não informa nem o Integrador deles e nem o cliente por enquanto, que a nossa PKG não atende o cenário deles.

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518354,518362);

SELECT ROUND(PBASERCA,2), ROUND(PVENDA,2),CODPROD FROM MXSHISTORICOPEDI WHERE NUMPED = 518354;

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA IN(3371);

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518354,518362);

SELECT ROUND(PBASERCA,2), ROUND(PVENDA,2),CODPROD, DTATUALIZ FROM MXSHISTORICOPEDI WHERE NUMPED = 518362;

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA IN(3373);

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%CON_TIPOMOVCCRCA%';
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%NAO_MOVIMENTAR_CC_PED_BLOQUEADO%';

## Resposta Canonica

**Conclusão canônica**

Foi analisado o cenário dos pedidos **518354** e **518362** e a causa identificada é que, **atualmente, a Máxima não atende ao cenário de movimentação de Conta Corrente via PKG quando existe acréscimo de boleto calculado posteriormente no ERP**.

### Análise técnica
- No faturamento, a comparação é feita com o **preço base** previamente salvo.
- Esse **preço base não contempla o acréscimo de boleto** calculado posteriormente no ERP.
- Atualmente, a referência utilizada vem do que foi gravado na transmissão do pedido na **ERP_MXSLOGRCA** (`maxPedido`).
- Com isso, ocorre **divergência entre `PVENDA` e `PBASE`**, o que leva à **movimentação de conta corrente**, mesmo sem nova movimentação manual do vendedor.

### Consultas utilizadas na análise
```sql
SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518354,518362);

SELECT ROUND(PBASERCA,2), ROUND(PVENDA,2),CODPROD FROM MXSHISTORICOPEDI WHERE NUMPED = 518354;

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA IN(3371);

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518354,518362);

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%CON_TIPOMOVCCRCA%';

SELECT C.NUMPED,
NVL(C.NUMPEDRCA,'0') NUMPEDRCA,
C.CODCLI,
C.CODUSUR,
C.CODFILIAL,
C.POSICAO,
C.CONDVENDA
FROM MXSHISTORICOPEDC C
INNER JOIN MXSUSUARI U
ON U.CODUSUR = C.CODUSUR AND U.CODOPERACAO != 2
WHERE C.DTATUALIZ >= TRUNC(SYSDATE) - 1
AND NVL(C.NUMPED,0) != 0
/* FLAG PROCESSARCC CRIADA PARA N¿O FICAR REPROCESSANDO QUANDO O PEDIDO FOR FATURADO OU CANCELADO */
AND NVL(C.PROCESSARCC,'S') = 'S'
AND NUMPED = 518354
ORDER BY C.NUMPED;

SELECT
I.CODPROD,
NVL(I.QT, 0) QUANTIDADE,
ROUND(NVL(I.PBASERCA, I.PTABELA), 2) PRECOBASE,
ROUND(I.PVENDA, 2) PRECOVENDA,
CASE
WHEN I.PVENDA > I.PTABELA THEN 'C'
ELSE 'D'
END TIPOOPER,
NVL(I.NUMSEQ, 1) SEQUENCIA
FROM
MXSHISTORICOPEDI I
WHERE
NUMPED = 518354
ORDER BY
I.NUMSEQ;

SELECT ROUND(PBASERCA,2), ROUND(PVENDA,2),CODPROD, DTATUALIZ FROM MXSHISTORICOPEDI WHERE NUMPED = 518362;

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA IN(3373);

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%NAO_MOVIMENTAR_CC_PED_BLOQUEADO%';
```

### Parâmetros verificados
- `CON_TIPOMOVCCRCA`
- `NAO_MOVIMENTAR_CC_PED_BLOQUEADO`

### Encaminhamento
- **Manter o ticket pausado**, pois o tema está em análise pelo **desenvolvimento**.
- Há um escalonamento interno já realizado por e-mail.

### Alternativas levantadas para avaliação do desenvolvimento
- Integrar o acréscimo específico de boletos para que ele seja calculado tanto no **PrecoBase do maxPedido** quanto no **PrecoVenda**.
- Criar uma melhoria parametrizável na PKG para, quando houver recálculo no ERP e essas informações forem enviadas na `MXSHISTORICOPEDI` com `PBASERCA` e `PVENDA` corretos, utilizar esses dados do ERP na comparação e na movimentação de conta corrente.

### Observação
As alternativas acima foram registradas **como sugestões iniciais**, **sem validação de viabilidade** até o momento.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 421441, 421715
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
