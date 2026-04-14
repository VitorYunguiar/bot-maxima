# GATE-465 - Pedido estornado após faturamento

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXPED - maxPag
- Natureza: Dúvida
- Atualizado em: 2024-12-06T08:55:40.785-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar maxPag, verificar pedido estornado no valor R$ 2.088,50, NSU 415022. 28/11/2024 16:49.

## Resultado apresentado
>> pedido 2160003614  foi estornado após faturamento.

## Resultado esperado
>> Caso tenha corte de itens no pedido, estorna somente o valor do corte e não o valor total

## Descrição
Foi identificado que o pedido *2160003614* teve corte de itens no *WinThor*, resultando em uma divergência de valores em relação ao valor original enviado pelo *maxPedido*. Nesse cenário, o comportamento esperado seria o estorno apenas do valor referente ao corte, e não do valor total do pedido.

Conversei com o Divino, que mencionou o seguinte:
{quote}_"O problema deve estar nesse valor (imagem em anexo). Tem uma regra que, quando passa 0, o maxPag estorna o valor total. Tem que verificar isso aí com o pessoal do maxPedido. Se bloquear isso, pode afetar no fluxo deles lá."_
{quote}

## Comentarios do Gatekeeper

### 1. 2024-12-06T08:55:40.780-0300 | Filipe do Amaral Padilha

Analisei os dados do chamado anterior MXPED-62118 que foi citado pelo cliente e aparentemente o problema é o mesmo.

O pedido foi na verdade estornado totalmente quando houve corte de apenas um item no pedido no dia 2024-12-02 20:36:47. E depois de estornado ele foi Faturado.

Nesse pedido 21601735, não vai ter mais o que a gente fazer, no sentido que, como o PIX já foi estornado, então agora eles teriam que conferir com esse cliente se foi mesmo estornado e solicitar o pagamento novamente.

Referente o problema ter ocorrido, a correção foi feita no último ticket e foi lançada a versão de extrator 3.1.2.446. Porém o cliente não foi atualizado e estava na versão 3.1.2.440. Então hoje eu atualizei eles para a 3.1.2.449 e também atualizei o banco nuvem e local. Isso deve estar resolvendo o problema, evitando que ocorra novamente. Então a correção é válida para os novos pedidos transmitidos a partir de hoje.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410736
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que a ocorrência foi 'causada pela ausência da correção no ambiente do cliente' não está totalmente explícita no texto-fonte; o texto diz que o cliente não foi atualizado e que isso deve resolver/evitar recorrência, mas não estabelece causalidade de forma definitiva. | A recomendação de 'manter o cliente na versão atualizada do extrator e acompanhar os novos pedidos para confirmar que o problema não se repete' não aparece no texto-fonte.
