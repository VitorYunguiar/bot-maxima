# GATE-697 - Movimentação na Flex.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Não Informado
- Assunto: MXPED - Conta Corrente
- Natureza: Dúvida
- Atualizado em: 2025-01-28T13:09:17.606-0300

## Contexto do Problema

## Passos para reproduzir
Pedido numped 518094
Verificar o por que teve desconto na FLEX.

## Resultado apresentado
Cliente informou que o RCA não utilizou a FLEX e mesmo assim teve desconto.

## Resultado esperado
Que não tenha desconto quando nao utilizar a flex

## Descrição
Cliente - esse exemplo aqui do flex do vendedor Arthur, ele não usou flex nesse pedido hoje e mesmo assim movimentou, parece que esse pequeno acréscimo veio do ERP.

## Comentarios do Gatekeeper

### 1. 2025-01-28T13:02:14.611-0300 | Filipe do Amaral Padilha

Para a Máxima, conforme já conversamos, é irrelevante configurações se debita/credita conta corrente. A gente não faz esse tipo de validação. Se ocorreu divergência entre o preço de venda e o preço base do item, ocorrerá débito ou crédito de conta corrente.

Analisei dois itens desse pedido, o código 30 e 5299 ambos nós recebemos um valor divergente na MXSHISTORICOPEDI, que é alimentada pelo ERP, onde o preço de venda foi maior que o preço base dos produtos, por isso houve movimentação de conta corrente.

Eu contatei o Renan integrador do ERP deles e repassei o mesmo cenário e pedi para ele verificar, agora precisamos aguardar retorno do Integrador.

A nossa parte você já pode passar para o cliente.

Consultas utilizadas

Cenário 1:

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518094);
SELECT NUMPEDERP,NUMPED FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518094);

--"PrecoVenda": 5.45,
--"PrecoBase": 5.45,

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518094);
SELECT SUM(ROUND(PVENDA,2) * QT - ROUND(PBASERCA,2) * QT) AS CC ,PVENDA,PBASERCA  FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 30 GROUP BY PVENDA, PBASERCA;
SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 30;

--PVENDA--5.472
--PBASERCA--5.45
SELECT SUM(VLCORRENTE - VLCORRENTEANT) FROM ERP_MXSLOGRCA WHERE NUMPEDRCA = 3322 AND CODPROD = 30;
SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA = 3322 AND CODPROD = 30;

SELECT * FROM MXSUSUARI WHERE CODUSUR IN(1627);

"ListaPoliticasDescontoPorQuantidade": [
{
"CodigoPolitica": "3051",
"QuantidadeInicial": 6,
"QuantidadeFinal": 9999,
"PercentualDesconto": 0.05505,
"PercentualDescontoMaximo": 0.0,
"AplicacaoAutomatica": true,
"Prioritaria": false,
"CreditaSobrePrecoTabela": true,
"BaseDebCredRCA": true,
"DataInicio": "2000-01-01T00:00:00",
"DataTermino": "5000-01-01T00:00:00",
"AlteraPrecoTabela": false
}
],

Cenário 2:

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%CON_NUMCASASDECVENDA%';

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518094);
SELECT NUMPEDERP,NUMPED FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518094);

--     "PrecoVenda": 1.45,
--      "PrecoBase": 1.45,
--      "PrecoOriginal": 1.65,
--       "Quantidade": 192.0,

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518094);
SELECT SUM(ROUND(PVENDA,2) * QT - ROUND(PBASERCA,2) * QT) AS ,ROUND(PVENDA,2),PBASERCA  FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 5299 GROUP BY PVENDA, PBASERCA;
SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 5299;

--PVENDA--1.455
--PBASERCA--1.45
SELECT SUM(VLCORRENTE - VLCORRENTEANT) FROM ERP_MXSLOGRCA WHERE NUMPEDRCA = 3322 AND CODPROD = 5299;
SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA = 3322 AND CODPROD = 5299;

SELECT * FROM MXSUSUARI WHERE CODUSUR IN(1627);

--política 529952

-- "PoliticaDescontoPorQuantidade": {
--          "CodigoPolitica": "529952",
--          "QuantidadeInicial": 16,
--          "QuantidadeFinal": 9999,
--          "PercentualDesconto": 0.12121,
--          "PercentualDescontoMaximo": 0.0,
--          "AplicacaoAutomatica": true,
--          "Prioritaria": false,
--          "CreditaSobrePrecoTabela": true,
--          "BaseDebCredRCA": true,
--          "DataInicio": "2000-01-01T00:00:00",
--          "DataTermino": "5000-01-01T00:00:00",
--          "AlteraPrecoTabela": true
--        },

### 2. 2025-01-28T13:05:10.107-0300 | Filipe do Amaral Padilha

Pedido: 518094
CODCLI: 4195
CODUSUR: 1627 (RCA)
CODFILIAL: 5
Cenário 1:
Produto 30
Preço enviado no JSON da Máxima:
--"PrecoVenda": 5.45,
--"PrecoBase": 5.45
Preço enviado pelo ERP no nosso endpoint MXSHISTORICOPEDIO:
--PVENDA--5.472
--PBASERCA--5.45
Movimentação de conta corrente: 0.08
SELECT SUM(ROUND(PVENDA,2) * QT - ROUND(PBASERCA,2) * QT) AS ,ROUND(PVENDA,2),PBASERCA  FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 30 GROUP BY PVENDA, PBASERCA;

### 3. 2025-01-28T13:07:51.097-0300 | Filipe do Amaral Padilha

Pedido: 518094
CODCLI: 4195
CODUSUR: 1627 (RCA)
CODFILIAL: 5
Cenário 2:
Produto 5299
Preço enviado no JSON da Máxima:
--     "PrecoVenda": 1.45,
--      "PrecoBase": 1.45
Preço enviado pelo ERP no nosso endpoint MXSHISTORICOPEDIO:
--PVENDA--1.455
--PBASERCA--1.45
Movimentação de conta corrente: 1.92
SELECT SUM(ROUND(PVENDA,2) * QT - ROUND(PBASERCA,2) * QT) AS ,ROUND(PVENDA,2),PBASERCA  FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 30 GROUP BY PVENDA, PBASERCA;
O preço sofre um arredondamento 2 casas decimais sempre, de 1.455 passa a ser 1.46

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 419573, 419575, 419578
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "MXSHISTORICOPEDI/MXSHISTORICOPEDIO" como se fossem equivalentes: o texto-fonte cita MXSHISTORICOPEDI e também menciona "endpoint MXSHISTORICOPEDIO", mas não estabelece formalmente essa equivalência com barra. | "Assim, a análise da parte Máxima indica que o desconto/movimentação não foi gerado por uso de FLEX no app" — o texto-fonte não menciona FLEX nem app.
