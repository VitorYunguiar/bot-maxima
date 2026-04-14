# GATE-444 - Carga de dados - itens em promoção

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Não Informado
- Assunto: MXPED - Política de Desconto - Preço Fixo
- Natureza: Dúvida
- Atualizado em: 2024-12-04T13:34:05.788-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do vendedor, iniciar um pedido no cliente 37258, filial 1, plano de pagamento 8 , cobrança BOLETO. Na aba 'tabela', selecionar o filtro 'Em promoção'.

## Resultado apresentado
É verificado que o item 22156 consta em promoção na base do rca, mas em base zero o item é apresentado normalmente.

## Resultado esperado
É esperado que o item em questão não seja apresentado em promoção.

## Descrição
Cliente relata que na base do RCA em questão, ao acessar a aba 'Tabela' e selecionar o filtro de produtos em promoção, a aplicação retorna alguns itens incluindo o 22156, entretanto esse item não consta em promoção. Foi realizado teste em base zero e verificado que o produto não é apresentado como 'Em promoção', entretanto ao realizar o mesmo teste na base do RCA o produto é apresentado como 'Em promoção'.
Favor realizar a carga no usuário em questão.

Login para teste:
5estrelas.145

## Comentarios do Gatekeeper

### 1. 2024-12-04T13:34:05.787-0300 | Filipe do Amaral Padilha

Foi feita a carga de dados da tabela MXSPRODUTMSK para normalizar a base do maxPedido;

Para validar os RCAs só precisam estar sincronziando o sistema. Eu mandei uma normalização geral para já evitar qualquer outro caso em outros RCAs.

--Não passar ao cliente:

Só para você ficar ciente e ficar também documentado:

--Como o registro não existe mais no banco de dados nuvem na tabela MXSPRODUTMSK , então não tem como investigar o motivo de não ter descido naturalmente via sincronismo parcial do maxPedido.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410296
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Identificada inconsistência de dados' não está explicitamente afirmado no texto-fonte. | 'no usuário informado (login 5estrelas.145)' não consta no texto-fonte. | 'impede determinar a causa de ele não ter sido atualizado naturalmente' altera o texto-fonte, que fala especificamente em 'não ter descido naturalmente via sincronismo parcial do maxPedido'. | A recomendação 'realizar/confirmar a carga de dados da tabela MXSPRODUTMSK no usuário em questão' não está no texto-fonte. | A recomendação 'aplicar a normalização geral nos RCAs' não está explicitamente orientada no texto-fonte; apenas informa que ela já foi enviada. | 'validar o comportamento após a sincronização dos RCAs, considerando a carga e a normalização já executadas' não está explicitamente no texto-fonte.
