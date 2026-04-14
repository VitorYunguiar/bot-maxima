# GATE-255 - Pedido com status 6, mas está como aguardando autorização

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXGESN - Autorização de Pedidos - Pedidos não aparecem para autorização
- Natureza: Dúvida
- Atualizado em: 2024-10-31T14:08:30.038-0300

## Contexto do Problema

## Passos para reproduzir
>>Verificar na MXSINTEGRACAOPEDIDO o Status e a crítica do pedido 807188
>>Verificar na base enviada o mesmo pedido

## Resultado apresentado
>>Na MXSINTEGRACAOPEDIDO o pedido está com status 6 e crítica bloqueado
>>Na base do RCA aparece como aguardando autorização

## Resultado esperado
>>O pedido deve aparecer no aparelho como bloqueado

## Descrição
>>Pedido 807188 com STATUS 6 na MXSINTEGRACAOPEDIDO

>>Crítica do pedido como bloqueado

>>Na base do RCA aparece como aguardando autorização do maxGestao

## Comentarios do Gatekeeper

### 1. 2024-10-31T14:07:46.512-0300 | Filipe do Amaral Padilha

--O ID_PEDIDO 230193 é um orçamento e não foi enviado para autorização

--O ID_PEDIDO que foi enviado é o 231200 e ele passou por autorização de pedidos normalmente, sendo a data de autorização 2024-10-29 17:18:11.000

--E uma questão aqui que ocorreu é que o pedido já foi autorizado e ele não foi integrado ao Winthor devido a parametrização que impede a integração: "A data de emissão desse pedido não é válida. Data do pedido: 2024-10-22. Validade parametrizada no sistema: 7 dia(s). Esse pedido não será processado."

--Então nesse caso, não tem cenário onde os pedidos não estejam entrando no maxGestão

--Sobre o pedido atualizar a posição no maxPedido, basta que o RCA realize o swipe na timeline, que as críticas dos pedidos serão atualizadas corretamente.

No caso a posição do correta do pedido é a crítica de 'Erro' conforme no vídeo que anexei

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 404184
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A divergência de status ocorre porque o pedido 231200 foi autorizado normalmente em 2024-10-29 17:18:11.000, porém não foi integrado ao Winthor devido à parametrização de validade da data de emissão. | Não há evidência de falha de entrada no maxGestão; o apontamento é de que não existe cenário em que os pedidos não estejam entrando no maxGestão. | Avaliar e ajustar a parametrização de validade da data de emissão que está impedindo a integração ao Winthor. | Não há vínculo explícito, nos fatos recebidos, entre o pedido 807188 e os IDs 230193 ou 231200.
