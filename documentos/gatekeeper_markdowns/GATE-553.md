# GATE-553 - Problema na autorização de pedidos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: João Pedro Faria Cabral [X]
- ERP do cliente: Winthor
- Assunto: MXGESN - Autorização de Pedidos - Lucratividade
- Natureza: Erro
- Atualizado em: 2024-12-27T07:53:38.550-0300

## Contexto do Problema

## Passos para reproduzir
BASE DE DADOS ANEXADA
ACESSO: fcd.teste_ti
______________________________________

SELECT * FROM MXSUSUARIOS WHERE CODUSUR = 1; -- fcd.teste_ti  ||  CODUSUR 1
-- Usuario que fez o pedido

SELECT * FROM mxsautori WHERE NRAUTORIZACAO IN (7621,7622,7623,7620,7619);
-- Teste na versão 2.260.4 > Produtos aprovados na data do teste, O PRODUTO 1041 não consta
-- Teste na versão 3.251.3 > (7613,7614,7612,7611,7610);

SELECT * FROM MXSPRODUT WHERE CODPROD IN (1041);
-- Produto com erro

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP =100509 ;
-- Teste na versão 3.251.3 numpederp = 100508
______________________________________

## Resultado apresentado
Na aprovação do maxGestão PWA é alterada a comissão dos produtos de 4% para 2%

A maioria dos produtos funciona no entanto o produto 1041 não aplica as modificaçoes.

Verificado no JSON do pedido que  "SolicitandoAutorizacaoPreco": false para o produto 1041, e TRUE para os demais

## Resultado esperado
Identificar o problema

## Descrição
O pedido está com um dos itens indo com o valor de "Gerar autorização no gestão: FALSE"

e isso causa com que o produto não reflita as edições no campo de comissão, quando o produto vai para o winthor

## Comentarios do Gatekeeper

### 1. 2024-12-27T07:53:38.543-0300 | Filipe do Amaral Padilha

Eu vou encaminhar para N3 para validar se os desenvolvedores podem fazer algo a respeito, mas a princípio, não se trata de um erro. A funcionalidade do maxGestão apenas não explica todos os fatos que podem ocorrer durante a autorização de pedidos com alteração da comissão dos produtos. Abaixo vou explicar como funciona e o caso do cliente:

No maxPedido quando você está inserindo itens no pedido, você tem a opção de negociar um preço acima do permitido. Quando isso ocorre aparece a msg no maxPedido, informando ao usuário que o ITEM em específico, será enviado para a aprovação de pedidos do maxGestão. Apesar do pedido todo ir para o maxGestão apenas alguns itens vão configurados com SolicitandoAutorizacaoPreco = true e isso é normal já que está sinalizando para o backend do maxPedido, que apenas alguns itens dentro do pedido sofreram de desconto acima do permitido.

Então quando o supervisor ou usuário vai autorizar no maxGestão, o sistema está permitindo ele alterar a comissão de todos os itens, o que define o campo ComissaoAlteradaPorAutorizacao = true para todos os itens. Porém a autorização só será gerada de fato para os itens com SolicitandoAutorizacaoPreco = true.

É isso que ocorre no caso do Ruddy, nos pedidos que ele testou, em todos ele sempre adicionou o item 1041 sem negociar um preço acima do permitido. Por esse motivo, mesmo alterando a comissão do item, a autorização não é gerada e por isso a comissão chega no Winthor dele com o valor default de 4%. E é isso que o maxGestão não informa que pode ocorrer com o produto, nem no PWA e nem na versão Web.

Isso é regra de negócios do sistema. Só para você imaginar, pense que no maxPedido nunca existiu a opção "enviar para a alteração de comissão", o RCA não consegue simplesmente mandar o pedido para que seja alterada a comissão, essa é uma condição que só pode ser alterada se o produto estiver sob solicitação de alteração de preço, porque é assim que ele sobe para a autorização de pedidos e por isso só gera autorização também dos itens que estão flagados com SolicitandoAutorizacaoPreco = true.

Então eu vou enviar para N3 do maxGestão como eu disse, mas pode ocorrer de eles dizerem que se trata de melhoria e não erro.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414044
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: No pedido analisado, o produto 1041 está com SolicitandoAutorizacaoPreco = false, enquanto os demais itens estão com true.
