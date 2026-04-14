# GATE-379 - Valores incorretos no histórico

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Não se Aplica
- Assunto: MXPED - Pedido/Orçamento - Histórico
- Natureza: Erro
- Atualizado em: 2024-11-25T14:09:45.200-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do vendedor, verificar os pedidos 159427, 159173 e 159126 no histórico de pedidos.

## Resultado apresentado
É verificado que os pedidos constam com o valor de R$5502,00, mas esse valor não é apresentado em nenhum pedido.

## Resultado esperado
É esperado que a aplicação apresente os valores corretos dos pedidos.

## Descrição
Cliente relata que no usuário CODUSUR 000372, os pedidos recentes (numped 159427, 159173 e 159126) estão com o mesmo valor de R$5502. O usuário estava na versão 3.256.1, foi realizada a atualização da base do vendedor para a versão 3.258.8 e verificado que os valores não foram corrigidos. Foi verificado também que ao reestruturar a base do apk não houve correção dos valores.
Ao consultar os valores do pedido na MXSINTEGRACAOPEDIDO e na MXSHISTORICOPEDC/PEDI, os valores dos pedidos estavam corretos.
Foi verificado que na tabela MXSPEDIDO, na base do RCA, o valor dos pedidos é de R$5502,00, o que torna o fluxo de apresentação desse valor incorreto uma vez que nem no envio do pedido quanto no retorno do ERP esse valor foi apresentado.

Login para teste:
GUARAVES.Sebastiao.Nascimento

## Comentarios do Gatekeeper

### 1. 2024-11-25T14:09:45.198-0300 | Filipe do Amaral Padilha

É erro de duplicação de pedidos, consegui fazer uma simulação do problema usando o cenário descrito e um pedido da base do RCA (pedido 6326) será enviado para N3.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
