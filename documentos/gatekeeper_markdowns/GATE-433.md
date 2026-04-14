# GATE-433 - Carga atualizid para historico de pedidos dos clientes

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: PROTON
- Assunto: MXPED - Pedido/Orçamento - Histórico
- Natureza: Dúvida
- Atualizado em: 2024-12-03T10:15:56.432-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar a base do RCA 19 em anexo
>>Abrir os clientes por exemplo o cliente 198870170

## Resultado apresentado
>>No momento não aparece o histórico de pedidos dos clientes recém transferidos do antigo RCA

## Resultado esperado
>>O Histórico de pedidos dos clientes deve aparecer para o RCA

## Descrição
>>O RCA 18 entrou de férias e o cliente passou os clientes para o RCA 19, por isso ele quer que façamos carga no RCA 19 para que o histórico de pedidos dos cliente apareçam para ele.

## Comentarios do Gatekeeper

### 1. 2024-12-03T10:15:56.429-0300 | Filipe do Amaral Padilha

Foi realizada a carga de dados das tabelas MXSHISTORICOPEDC e MXSHISTORICOPEDI para as vendas realizadas dos RCAS 18 e 19 dos últimos 100 dias, porém o parâmetro de histórico deles está para 30 dias, então vai exibir histórico dos últimos 30 dias de compras.
CATALOGO_PEDIDOS_DIAS_SYNC = 30

Se eles quiserem mais dias, ai teria que mudar o parâmetro e fazer a carga de novo.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409987
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma especificamente que a ação recomendada é 'Se for necessário exibir mais dias de histórico para o RCA 19', mas o texto-fonte fala dos RCAs 18 e 19, sem restringir apenas ao RCA 19.
