# GATE-901 - Venda broker não carrega em nova filial

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Sankhya
- Assunto: MXPED - Integração - Integrador OERPs
- Natureza: Dúvida
- Atualizado em: 2025-03-05T12:36:29.388-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do rca, iniciar um pedido no cliente 226972 como venda broker.

## Resultado apresentado
Ao iniciar, a aplicação retorna a mensagem de inconsistência de dados.

## Resultado esperado
É esperado que os vendedores possam iniciar pedidos de venda broker na filial 18.

## Descrição
Cliente realizou a alteração da filial de venda principal de um perfil de vendedor da filial 2 para a filial 18.
Cliente relata que ao iniciar um pedido na filial 18 como venda broker, a aplicação retorna a mensagem de inconsistência de dados devido à permissão de coleção de filiais do vendedor. O teste foi realizado no cliente 226972 e em base zero.
Ao iniciar um pedido em um perfil que vende na filial 2 como venda broker, a aplicação inicia o pedido normalmente.
Foi realizada a conferência dos parâmetros:
FIL_BROKER
FIL_PERCOMFILIALBROKER
FIL_PERCOMMOTBROKER
FIL_PERCOMRCABROKER
FIL_PERFRETEBROKER
FIL_TIPOBROKER

E também as permissões de filiais dos vendedores, e os campos CONDVENDA4.MXSCLIENT, BROKER.MXSFILIAL e TIPOBROKER.MXSFILIAL

Login para teste:
copinisan.emanoel

## Comentarios do Gatekeeper

### 1. 2025-03-05T12:36:29.384-0300 | Filipe do Amaral Padilha

Para trabalhar com o processo de filial Broker a configuração do campo TIPOBROKER da MXSFILIAL, deve ser enviada com a informação 'MAB';

Na hora de listar as filiais o código do maxPedido valida se essa informação está sendo enviada.

Então para resolver o cenário do ticket, ele só precisa enviar essa informação 'MAB', na filial 18, assim como na filial 1 por exemplo, nesse campo da MXSFILIAL. Se o cliente não tiver essa intrergação programada a gente pode fazer via banco nuvem.

Feito isso os RCAs precisam sincronizar para validar

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 427729
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A inconsistência ocorre porque a filial 18 não está enviando a informação `MAB` no campo `TIPOBROKER` da `MXSFILIAL`. | Responsável pelo ajuste: Cliente, ou a equipe responsável por realizar o ajuste via banco nuvem, caso não exista integração programada. | Próximo passo: ... sincronizar os RCAs para confirmar o funcionamento da venda broker.
