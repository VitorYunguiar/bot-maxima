# GATE-781 - divergencia de comportamento de exibição de preço min/max entre tipos de venda

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Sankhya
- Assunto: MXPED - Produto - Preço Divergente
- Natureza: Dúvida
- Atualizado em: 2025-02-13T17:02:41.896-0300

## Contexto do Problema

## Passos para reproduzir
Login: bispo.vendedort
cliente: 1328
cobrança: dinheiro
plano de pagamento: 75
produto 50
iniciar um pedido normal, buscar pelo item e observar o valor presente no campo Preço Min/Max
iniciar um pedido balcão reserva e fazer o mesmo fluxo(em anexo há dois videos desse fluxo)

## Resultado apresentado
divergencia de preço min/max entre versões e entre tipo de venda normal e balcão reserva

## Resultado esperado
segundo o cliente, o valor correto que deve ser exibido são os 11,50 que constam no pedido normal da V2

## Descrição
Ao validarmos o relato do cliente abaixo:

"boa tarde ao alternar entre os tipos de venda (Normal e Balcão Reserva) os valores do produto estão sendo apresentados diferença nos valores. Esse comportamento é devido a algum parâmetro?"

Ocorre a seguinte situação ao emularmos esse cenário:

Tipo normal:

!image-2025-02-12-16-09-51-519.png|width=296,height=527!

Tipo balcão reserva:

!image-2025-02-12-16-13-39-786.png!

Se perceberem ao comparar as 4 imagens, apenas na V2 pedido normal que é exibido os valores de 11.50, porém o cliente retorna que esse é o valor correto que deve ser ai apresentado. A unica politica presente para o item é essa:

!image-2025-02-12-15-53-33-086.png!

!image-2025-02-12-15-53-49-577.png!

Nesse cenário, o que pode estar gerando aquele valor diferente de 11,50 que o cliente informa ser o valor correto a ser exibido, uma vez que não identifiquei registros de configuração ou parâmetro que criem aquele valor? mesmo a V2 não traz outra politica presente, mas apenas a politica do print acima

## Comentarios do Gatekeeper

### 1. 2025-02-13T17:02:41.894-0300 | Filipe do Amaral Padilha

Preco Min/%

O preço mínimo que está sendo apresentado na forma de Pedido Normal está vindo de uma permissão de desconto que o RCA possui na tabela MXSTABPR no campo PERDESCMAX no valor de desconto de 3.17.

No caso do balcão reserva o sistema valida o campo PERDESCMAXBALCAO. Isso o sistema sempre fez desde 2016 tem isso no fonte. Então como esse campo na MXSTABPR está vazio, ele pega o percentual de desconto da política 0.78% para aplicar e considerar como preço mínimo.

Para resolver eles teriam que mandar esse campo preenchido via integração para a gente (PERDESCMAXBALCAO).

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 423870
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "O valor diferente de 11,50 no fluxo Balcão Reserva" — o texto-fonte não menciona o valor 11,50. | "não está sendo gerado por outra política" — o texto-fonte não faz essa comparação nem menciona 'outra política'. | "A divergência ocorre" — embora compatível com o texto, a palavra 'divergência' é uma interpretação; o fonte apenas explica a diferença de cálculo entre os fluxos. | "no cenário analisado" — essa contextualização não aparece no texto-fonte.
