# GATE-487 - Erro desconto progressivo

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: N/A
- Assunto: MXPED - Campanha - Desconto Progressivo
- Natureza: Dúvida
- Atualizado em: 2024-12-11T16:35:45.030-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do vendedor, duplicar o pedido 22022728 inserindo os itens que atendem à campanha progressiva e enviar o pedido.

## Resultado apresentado
Ao enviar, é verificado no JSON do pedido que os descontos estão desordenados e irreais quando comparados com os valores dos itens do pedido, além de que o valor geral do pedido é alterado.

## Resultado esperado
É esperado que os valores de desconto retornados no aplicativo estejam de acordo com os valores dos itens.

## Descrição
Vendedor relata que ao enviar pedidos que possuam itens que fazem parte de uma campanha de desconto progressivo, os valores de descontos dos itens ficam irreais quando o pedido é enviado do APK.
Foi analisado o pedido 22022728, onde foram inseridos itens como o codprod 1914319, que ao ser enviado é verificado que consta um desconto de 66,67%, mas o desconto não existe no valor do item, uma vez que o item possui o preço unitário de tabela de 12,46 com embalagem múltiplo 3, totalizando os 37,38 que são exibidos no aplicativo.
A situação ocasiona num pedido que o valor de tabela é de quase 3x o valor original do pedido.
A situação ocorre apenas em pedidos que possuem desconto progressivo.

Login para teste:
destro.22004365

## Comentarios do Gatekeeper

### 1. 2024-12-11T16:16:43.478-0300 | Filipe do Amaral Padilha

Abaixo vou estar esclarecendo o que de fato está ocorrendo com o pedido NUMPEDERP IN(3408381204).

Primeiramente, o % de 66,67% de desconto está sendo exibido no histórico de itens do pedido devido ao cálculo do preço de tabela e do preço de venda da tabela MXSHISTORICOPEDI:

O maxPedido basicamente acessa a MXSHISTORICOPEDI do pedido 3408381204 e pega por exemplo, o preço de tabela do item (1914319) R$37.38 campo PTABELA e a partir dele calcula o desconto que foi dado, comparando com o PVENDA do produto (1914319) R$12.46. Então porque mostra os 66,67%? Porque 66,67% de 37.38 é igual a 12.46. E esses dados o ERP está nos enviando no histórico do endpoint MXSHISTORICOPEDI.

Então para resolver essa questão da exibição do desconto no histórico de itens dos pedidos, o integrador do SAP precisa verificar de onde eles estão tirando o preço de tabela e enviando para a gente no campo PTABELA da MXSHISTORICOPEDI. O correto nesse caso seria eles terem enviado por exemplo, o valor de "12.46" porque não teve desconto no pedido digitado manualmente pelo RCA.

--------------------------

Existe um segundo cenário que eu acredito que seja um erro pré-existente (ou seja, que não tem relação com o relato acima) que seria o seguinte:

Se você pegar o aplicativo antes de enviar o pedido para o ERP e simular:
--CODCLI 53436
--CODFILIAL DE04
--PLPAG P018
--CODPROD 1914319
--CODPROD 1953546

E aplicar o desconto progressivo, não vai ser aplicado o desconto progressivo no item e segundo o log do maxPedido diz que tem desconto flex aplicado no item (O que não é verdade)

Então esse cenário que eu levantei de erro pré-existente eu vou mandar para N3, para eles verificarem o que está ocorrendo. Já o relato acima, é o caso de eles verificarem com a integração porque como vimos, nem desconto aplicado teve e a integração deles tá mandando o PTABELA diferente do PVENDA, assim o aplicativo na hora de calcular o desconto fica com a informação errada.

Será enviado para N3 ticket: https://suporte.maximatech.com.br/browse/MXPEDDV-86344

## Resposta Canonica

Foi identificada a existência de dois cenários distintos:

1. **Percentual de 66,67% exibido no histórico do pedido**
   No pedido **3408381204**, o histórico de itens utiliza os dados enviados pelo ERP no endpoint **MXSHISTORICOPEDI**. Para o item **1914319**, foram enviados:
   - **PTABELA = R$ 37,38**
   - **PVENDA = R$ 12,46**

   Com esses valores, o aplicativo calcula o desconto exibido no histórico, resultando em **66,67%**, pois **12,46 corresponde a 33,33% de 37,38**. Portanto, o percentual apresentado decorre diretamente da relação entre **PTABELA** e **PVENDA** recebidos da integração.

2. **Possível erro pré-existente na simulação antes do envio**
   No cenário simulado antes do envio ao ERP, foi observado que o **desconto progressivo não é aplicado no item**, enquanto o log do **maxPedido** indica **desconto flex aplicado**, o que foi apontado como incorreto. Até o momento, este ponto está tratado como **possível erro pré-existente**, sem conclusão definitiva.

### Parâmetros analisados
- **NUMPEDERP:** 3408381204  
- **CODCLI:** 53436  
- **CODFILIAL:** DE04  
- **PLPAG:** P018  
- **CODPROD:** 1914319  
- **CODPROD:** 1953546  

### Conclusão
No primeiro cenário, a origem do percentual exibido está nos dados enviados pelo ERP, especificamente no campo **PTABELA** da **MXSHISTORICOPEDI**. No caso analisado, o valor esperado para **PTABELA** seria **R$ 12,46**, pois não houve desconto no pedido digitado manualmente pelo RCA.

### Ação recomendada
- O **integrador do SAP** deve validar a origem do valor enviado em **PTABELA** na **MXSHISTORICOPEDI**.
- O segundo cenário será encaminhado ao **N3** por meio do ticket **MXPEDDV-86344** para apuração do possível erro pré-existente.

### Limitações da análise
- Não há conclusão definitiva sobre o segundo cenário.
- Não foram apresentados comandos SQL.
- A análise do primeiro cenário depende dos valores enviados pela integração no campo **PTABELA**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 411704
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
