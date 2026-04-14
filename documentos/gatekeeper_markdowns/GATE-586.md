# GATE-586 - Erro ao aumentar comissão dos pedidos na versão PWA mobile

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXGESN - Autorização de Pedidos - Desconto
- Natureza: Dúvida
- Atualizado em: 2025-01-07T15:07:33.494-0300

## Contexto do Problema

## Passos para reproduzir
>>O RCA deve enviar um pedido que exija aprovação do maxGestao
>>Entrar no aplicativo maxGestão PWA no emulador ou no celular
>>Ir em 'aprovação de pedidos'
>>Clicar sobre o pedido enviado
>>Alterar a comissão do pedido para uma maior que a atual

Login maxGestao: lubrimax.admti
Senha maxGestao: Lubrimax123

Login maxPedido: LUBRIMAX.MAICON
Senha maxPedido: Tenporária

## Resultado apresentado
>>O sistema exibe uma mensagem que diz que o usuários não pode alterar a comissão para uma maior do que a atual.

## Resultado esperado
>>O usuário deve poder alterar a comissão normalmente

## Descrição
>>Ao tentar alterar a comissão no app mobile do maxGestao PWA o sistema mostra o seguinte erro: 'O percentual de desconto autorizado para o produto (Produto) está maior do que o percentual atual do produto. Você não pode realizar esta autorização.'

## Comentarios do Gatekeeper

### 1. 2025-01-07T14:11:01.558-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 porque o comportamento entre PWA mobile e maxGestão web na alteração de comissão está divergente

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 415311
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: No cenário reportado, a alteração de comissão no PWA mobile apresenta bloqueio com mensagem de validação. | A evidência disponível indica que esse comportamento está divergente em relação ao maxGestão web para a mesma operação. | Responsável: N3
