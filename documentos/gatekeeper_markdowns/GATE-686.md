# GATE-686 - Erro Estoque Maxpedido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Estoque
- Natureza: Dúvida
- Atualizado em: 2025-01-24T15:36:47.779-0300

## Contexto do Problema

## Passos para reproduzir
>> Login: efx.testeefx
>> Iniciar pedido para qualquer cliente, colocar filial 2 no cabeçalho do pedido, busca pelo produto 101016

## Resultado apresentado
>> Nas versões atuais, quando pesquisa pela produto 101016 incialmente mostra estoque, mas quando clica no produto mostra que o estoque esta zerado.

>> Na versão v3.218, quando coloca filial 2 no cabeçalho do pedido, ao clicar no produto já e informado o estoque do produto

## Resultado esperado
>> Mostre o estoque da filial 2

## Descrição
*Cliente* - Estamos tentando implantar os pedido, mas o aplicativo está acusando que não tem saldo de estoque, sendo que o estoque dos produtos estão normais.

acusando a mensagem de erro, permitindo implantar o pedido, o pedido chega no WT como bloqueado, não permitindo desbloquear e cancelando o pedido.
-------------------------------
Fiz teste na versão de ponta do maxPedido v4, e ao realizar teste foi visto que o sistema não busca a filial com estoque que no caso seria a filila 2, produto 101016 . Cliente disse que na versão v3.218 busca o estoque normalmente (produto 101016).

Fiz teste na versão v3.218 e realmente quando coloca a filial 2 no cabeçalho do pedido já busca a filial com estoque no caso a filial 2.

## Comentarios do Gatekeeper

### 1. 2025-01-24T15:36:47.775-0300 | Filipe do Amaral Padilha

A versão que o cliente utiliza para comparação é muito antiga 3.218. E pode apresnetar erros já corrigidos em outras versões.

A versão 3.269.2 que é a última antes da V4 já não possui mais o comportamento da 3.218.

Nesse sentido vamos avaliar o cenário direto com base na V4 do maxPedido:

Na V4, como ele possui registro na tabela MXSFILIALRETIRA, a apk realiza a seguinte consulta para buscar o estoque:
SELECT mxsfilial.codigo, mxsfilial.razaosocial, MAX(IFNULL(mxsest.qtestger, 0) - IFNULL(mxsest.qtreserv, 0) - IFNULL(mxsest.qtbloqueada, 0)  , 0) AS estoquedisp
FROM mxsfilial,mxsest,mxsacessodados,mxsfilialretira
WHERE
mxsfilialretira.codfilialvenda = '2'
AND mxsacessodados.coddados = 6
AND mxsacessodados.codusuario = 19120
AND mxsest.codfilial = mxsfilial.codigo
AND mxsfilial.codigo = mxsfilialretira.codfilialretira
AND mxsfilialretira.codfilialretira = mxsacessodados.chavedados
AND mxsest.codprod = '101016';

Atualmente a MXSFILIALRETIRA deles está divergente da PCFILIALRETIRA, esse é o motivo de estar tendo problema no carregamento do estoque, porque quando vende na filial 2, sempre retira na 2, segundo a regra da PCFILIALRETIRA deles.

Hoje a MXSFILIALRETIRA está assim:

3	1
1	3
1	2
1	1
3	2
2	2

E a PCFILIALRETIRA deles está assim:

2	2
1	1
3	1

Nesse sentido, da forma que está hoje a nossa tabela, o SQL que citei acima sempre retorna primeiro o estoque da filial retira 1 que é estoque zero = (0).

Para resolver o cenário deles eu estarei realizando a normalização da divergência dos registros. Com isso, eu testei e o maxPedido pega o estoque da filial retira 2, mostrando corretamente e inserindo também a quantidade certa no pedido.

Dito isso, agora é necessário que o cliente utilizando a última versão sincronize e realize o teste até o faturamento se fica tudo ok com o pedido.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 418982
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Gatekeeper realizará a normalização dos registros divergentes" — o texto-fonte diz apenas "eu estarei realizando a normalização da divergência dos registros", sem mencionar Gatekeeper.
