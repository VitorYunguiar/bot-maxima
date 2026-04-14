# GATE-451 - divergencia de precificação entre app e 316

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Preço Divergente
- Natureza: Dúvida
- Atualizado em: 2024-12-05T15:12:20.353-0300

## Contexto do Problema

## Passos para reproduzir
login: efx.rogerioferreira
cliente: 26309
filial 2
produto 101002
tentar negociar o item com o preço de venda da MXSTABPR para a região do cliente e observar os resultados

## Resultado apresentado
o app, aparentemente, está acrescendo um valor de forma inesperada diretamente no preço de tabela do item

## Resultado esperado
é esperado que a negociação ocorra de forma adequada da mesma forma que ocorre na 316.

## Descrição
Senhores, ao analisar o cenário da demanda citada, estamos observando que o aplicativo está apresentando uma precificação divergente da apresentada na rotina 316 do cliente. Ao negociar um pedido para o seguinte cliente:

!image-2024-12-04-12-26-25-805.png!

Vejam o comparativo de comportamento entre os dois cenários abaixo:

!image-2024-12-04-12-09-29-821.png!

!image-2024-12-04-12-11-03-447.png!

essa situação gera o bloqueio para inserção aqui observado:

!image-2024-12-04-12-12-11-318.png!

porém essa situação não deveria ocorrer, pois não há politicas comerciais para o produto:

!image-2024-12-04-12-29-23-341.png!

e baseado no preço de venda do item, o valor negociado não deve ter desconto:

!image-2024-12-04-12-13-50-180.png!

em validações de comparativo da origem de preço, observei que a 316 traz uma origem de preço com alguns valores de codigo de tributação diferentes do que há no app:

!image-2024-12-04-12-18-19-695.png!

!image-2024-12-04-12-18-44-102.png!

consultando os valores que constam na mxstribut para o codst 43, há alguns registros que divergem do que há para a origem de preço da 316:

!image-2024-12-04-12-23-07-105.png!

Nesse cenário e com base nessas evidencias, o que pode estar gerando essa divergência de precificação? Ao que tudo indica há uma situação de divergência de aplicação de tributação sendo apresentada, isso é gerado por qual motivo? O que deve ser feito para que o aplicado se comporte de forma a trazer os preços da mesma forma que há na 316?

login:

## Comentarios do Gatekeeper

### 1. 2024-12-05T15:05:52.276-0300 | Filipe do Amaral Padilha

Foi feita carga de algumas tabelas que envolvem cenário de tributação e preço (MXSTABPR, MXSTABPRCLI, MXSTRIBUT, MXSTRIBUTEXCECAO, MXSTRIBUTEXCECAOREGRA e MXSTABTRIB) porém, mesmo assim o maxPedido continua apresentando o preço de venda com divergência da 316.

Será enviado para N3 para verificarem se é problema de cálculo ou se ainda tem alguma divergência.

## Resposta Canonica

Após análise do cenário, foi realizada a carga das tabelas envolvidas na formação de preço e tributação:

- MXSTABPR  
- MXSTABPRCLI  
- MXSTRIBUT  
- MXSTRIBUTEXCECAO  
- MXSTRIBUTEXCECAOREGRA  
- MXSTABTRIB  

Mesmo após essa atualização, o maxPedido continua apresentando divergência no preço de venda em relação ao comportamento observado na rotina 316.

No momento, a causa raiz ainda não está confirmada. Com os fatos levantados até aqui, não foi possível concluir se a divergência decorre de problema de cálculo no aplicativo ou de alguma outra inconsistência remanescente no cenário.

Dessa forma, o encaminhamento recomendado é para o N3, para validação técnica da origem da divergência e confirmação se o desvio está no cálculo ou em outra diferença de configuração/dados.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 410590
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
