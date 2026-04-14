# GATE-711 - Pedido não atualiza na timeline

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Timeline
- Natureza: Dúvida
- Atualizado em: 2025-01-30T08:36:15.739-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar a base do RCA em anexo
>>Ir na timeline de pedidos
>>Fazer swipe

Login:DISPAN.JOAMILE
Senha:Hash

## Resultado apresentado
>>Mesmo após realizar swipe o pedido ainda não aparece como enviado para o ERP, mesmo o pedido estando como faturado na MXSHISTORICOPEDC
>>A útima crítica enviada é que o pedido foi de 'Sucesso'.

## Resultado esperado
>>Os pedidos devem aparecer assim como o status da MXSHISTORICOPEDC

## Descrição
>>O pedido 39003011 de exemplo (possuem outros), não aparece como enviado para o ERP, mesmo já tendo sido faturado.

## Comentarios do Gatekeeper

### 1. 2025-01-29T15:52:54.240-0300 | Filipe do Amaral Padilha

39003011, 39003020, 39003005, 39002955, 39002957, 39002969, 39002999

Todos os pedidos que não tem a timeline atualizada são do tipo ORIGEMPED = R

E o parâmetro ENVIA_PEDIDOS_BALCAORESERVA do backend estava igual = N desde 2024-10-29 17:29:43.000

Para resolver foi feita ativação do parâmetro e carga dos pedidos dessa origem referente ao mês atual.

Essa situação independe de versão era questão do parâmetro.

O RCA deve sincronizar o maxPedido e depois verificar na timeline que tudo estará nos conformes

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 419995
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "o que impediu o envio/atualização desses pedidos na timeline" | "A carga realizada considera somente o mês atual"
