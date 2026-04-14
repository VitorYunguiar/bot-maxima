# GATE-876 - Pedido bloqueado não pode ser editado

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Editar
- Natureza: Dúvida
- Atualizado em: 2025-02-27T14:12:38.504-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do rca, procurar o pedido NUMPEDRCA 253003848 e tentar editá-lo.

## Resultado apresentado
Ao realizar a ação, a apk retorna a mensagem de que não é possível editar um pedido já enviado, entretanto o pedido consta como bloqueado no apk.
Ao habilitar a permissão 'Permite editar pedido já enviado' na Central de Configurações.

## Resultado esperado
É esperado que o vendedor consiga realizar a edição do pedido bloqueado sem a permissão em questão.

## Descrição
Cliente relata que o vendedor 253, ao editar o pedido NUMPEDRCA 253003848 a apk retorna a mensagem de que não é possível editar pedido já enviado. Entretanto, ao olhar o pedido na integração, é verificado que o pedido consta com o status 6 (bloqueado).
Foi realizado teste na base do rca, onde foi verificado que ao liberar a permissão 'Permite editar pedidos já enviados' na Central de Configurações, a aplicação permitiu editar o pedido normalmente
À priori, trata-se de uma falha da apk, pois o pedido em questão ainda não foi enviado para o ERP, e pelo fato do cliente trabalhar com a API de cancelamento pode causar problemas nos fluxos e regras internas do cliente.

Verificado com o P.O Cleyton que trata-se de um erro, encaminhado ao gate para análise.

Login para teste:
amorix.253

## Comentarios do Gatekeeper

### 1. 2025-02-27T11:33:47.143-0300 | Filipe do Amaral Padilha

--Ao atualizar a versão do aplicativo identifiquei que o funcionamento está normalizado, ao editar pedidos, não ocorre a mensagem impedindo

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
