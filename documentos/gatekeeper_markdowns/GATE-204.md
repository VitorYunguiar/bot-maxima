# GATE-204 - MXSPRODUTPOS não gera registro

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXPED - Produto - Positivação
- Natureza: Dúvida
- Atualizado em: 2024-10-18T12:25:20.636-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar APK
>dztm.ce3315
>Iniciar pedido no cliente 135838
>Aba tabela
>Olhar os produtos 134857, 134752, 111169, '099003', '009891', 104691
>Verificar que consta como se os produtos não estivessem positivados no mês de Outubro.

##SELECTS UTILIZADOS##

SELECT * FROM MXSHISTORICOPEDI WHERE CODPROD IN(134857, 134752, 111169, '099003', '009891', 104691) AND NUMPED IN(SELECT NUMPED FROM MXSHISTORICOPEDC WHERE CODCLI = 135838);

SELECT * FROM MXSPRODUTPOS m WHERE CODPROD IN(134857, 134752, 111169, '099003', '009891', 104691) AND CODCLI = 135838;

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%GERAR_DADOS_POS_PRODUTOS%';

SELECT * FROM MXSVERSAOBD ORDER BY DTATUALIZACAO DESC;

## Resultado apresentado
Os produtos foram vendidos no mês de Outubro para esse cliente porém não gerou registros na MXSPRODUTPOS, tendo somente 4 com status de deletado.

## Resultado esperado
Gerar os registros.

## Descrição
Foi verificado que vários produtos foram positivados para um cliente nesse mesmo mês mas não gerou registro na MXSPRODUTPOS, alguns dos produtos já foram faturados porém também não gera na MXSPRODUTPOS.

## Comentarios do Gatekeeper

### 1. 2024-10-18T12:25:20.634-0300 | Filipe do Amaral Padilha

Basicamente o problema deles é que eles tem uma configuração no parâmetro da MXSPARAMETRO, (VALIDAR_APURACAO_NF = S) e com isso, o nosso sistema valida informações dos endpoints ERP_MXSMOV e ERP_MXSNFSAID. E eles não estão enviando os dados dos pedidos corretamente para gerar a positivação dos pedidos do RCA 3315 no cliente 135838 que seria o do cenário.

--Então para resolver o cliente teria duas opções:

--Ou o cliente vai precisar ou desligar o parâmetro VALIDAR_APURACAO_NF, colocando ele = N, assim não vai validar mais a questão de nota fiscal e movimentações que eles estão deixando de enviar corretamente para a gente;

--Dai amanhã quando a JOB rodar novamente vai apurar os dados somente validando se o pedido tá com posicao = 'F' na MXSHISTORICOPEDC (que eles já estão enviando certo)

--Ou 2° opção, o cliente envia corretamente via integração os dados dos pedidos relacionando eles na MXSHISTORICOPEDC, ERP_MXSMOV e ERP_MXSNFSAID considerando as propriedades NUMPED e NUMTRANSVENDA;

--Se o cliente perguntar por que não funcionou quando faturou o pedido e antes funcionava, é porque antes a integração fazia certo e agora parou de fazer e então ele teria que mostrar todas essas evidências e verificar com o integrador dele.

--Eu recomendo eles só desligarem o parâmetro VALIDAR_APURACAO_NF;

*Abaixo vou colocar os detalhes da análise caso você queira entender também tudo que foi feito e verificado*

--O cliente usa o parâmetro CRITERIOVENDA = 'F'

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%CRITERIOVENDA%'; -- = F

--Então a gente valida a MXSHISTORICOPEDC se a POSICAO = 'F' e a positivação ela é referente somente ao mês 10

SELECT * FROM MXSHISTORICOPEDC WHERE CODUSUR IN(3315) AND CODCLI IN(135838) AND POSICAO IN('F') AND CODOPERACAO <> 2 AND TRUNC(DATA) BETWEEN TO_DATE('01/10/2024', 'DD/MM/YYYY') AND TO_DATE('18/10/2024', 'DD/MM/YYYY');

--Retorna os 3 pedidos certo? 8817136, 8817105, 8828379

--Então agora a gente valida o parâmetro VALIDAR_APURACAO_NF que está ativo desde 2023 na Donizete então não é novidade para eles

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%VALIDAR_APURACAO_NF%'; -- = S

--Então agora a gente valida o NUMTRANSVENDA dos pedidos

SELECT NUMTRANSVENDA FROM MXSHISTORICOPEDC WHERE CODUSUR IN(3315) AND CODCLI IN(135838) AND POSICAO IN('F') AND CODOPERACAO <> 2 AND TRUNC(DATA) BETWEEN TO_DATE('01/10/2024', 'DD/MM/YYYY') AND TO_DATE('18/10/2024', 'DD/MM/YYYY');

--Estão nulos, eles teriam de estar preenchidos pelo menos no NUMTRANSVENDA da ERP_MXSMOV que se relaciona com a ERP_MXSNFSAID

--O que a consulta faz é o que está abaixo, no caso olha se tem o numtransvenda para o rca

SELECT US.CODUSUARIO,

PI.CODPROD,

NVL(PI.CODAUXILIAR, 0) AS CODAUXILIAR,

'P' AS TIPOPOSITIVACAO,

MIN(PC.DTSAIDA) DTPOSITIVACAO,

NULL QTDEPOSITIVACAO,

NULL HASH

FROM MXSUSUARIOS US, ERP_MXSNFSAID PC, ERP_MXSMOV PI

WHERE PI.NUMTRANSVENDA = PC.NUMTRANSVENDA

AND PC.CODUSUR = US.CODUSUR

AND PC.DTCANCEL IS NULL

AND PC.CODFILIAL IN (SELECT CHAVEDADOS FROM MXSACESSODADOS WHERE CODDADOS = 6 AND CODUSUARIO = US.CODUSUARIO)

AND PC.DTSAIDA BETWEEN TO_DATE('01/10/2024', 'DD/MM/YYYY') AND TO_DATE('18/10/2024', 'DD/MM/YYYY')

AND PC.CODOPERACAO != 2

AND PI.CODOPERACAO != 2

AND US.CODOPERACAO != 2

AND US.CODUSUR = '3315'

GROUP BY US.CODUSUARIO, PI.CODPROD, NVL(PI.CODAUXILIAR, 0);

--Não retorna nada, significa que os pedidos foram faturados 8817136, 8817105, 8828379, mas não recebemos da integração as notas fiscais e nem as movimentações referentes a esses pedidos

--Se quiser conferir direto nos endpoints também:

SELECT * FROM ERP_MXSMOV WHERE CODUSUR IN(3315);--Dos pedidos 8817136, 8817105 e 8828379 não consta a movimentação

SELECT * FROM ERP_MXSNFSAID WHERE NUMPED IN(8817136, 8817105, 8828379); --do 8828379 não recebemos a nota

SELECT * FROM ERP_MXSMOV WHERE NUMTRANSVENDA IN(4884757, 4884758); -- Não tem esses numtransvenda

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 401651
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Sem o vínculo entre NUMPED e NUMTRANSVENDA, a positivação não é gerada." — o texto-fonte afirma que os dados precisam ser relacionados considerando NUMPED e NUMTRANSVENDA e que NUMTRANSVENDA está nulo, mas não formula exatamente essa regra causal nesses termos. | "O comportamento é compatível com falha na integração de responsabilidade do cliente/integrador" — o texto-fonte recomenda verificar com o integrador e diz que a integração parou de fazer certo, mas não atribui explicitamente responsabilidade de forma categórica. | "não com erro de geração interna da positivação" — essa negação não aparece explicitamente no texto-fonte.
