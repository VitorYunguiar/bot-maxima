# GATE-384 - Porcentagem do positivado muito alta

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Dados Incorretos
- Natureza: Dúvida
- Atualizado em: 2024-11-28T16:52:38.861-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar painel de auditoria;
>> Replicar buscar de acordo com o print em anexo.

## Resultado apresentado
Valores não batem com a quantidade de pedidos enviados.

## Resultado esperado
Valores de acordo com a quantidade de pedidos enviados.

## Descrição
No dia 22/11 o RCA em questão atendeu 5 clientes: 1 dentro de rota e 4 fora de rota, enviando pedido para todos os 5.

Porem no painel de auditoria está reportando 14 clientes positivados fora de rota.

Cliente está questionando de onde vem essa positivação, ja que so é considerado cliente positivado o que cliente que recebeu pedido no período, porem somente 5 clientes deveria ter sido positivados no dia 22.

## Comentarios do Gatekeeper

### 1. 2024-11-26T11:16:05.009-0300 | Filipe do Amaral Padilha

Foi enviado para N3 porque está ocorrendo uma inconsistência nas informações de compromissos e visitas positivadas por cliente;

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review, requires_attachment_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
