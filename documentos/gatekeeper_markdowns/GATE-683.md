# GATE-683 - Carga na MXSHISTORICOPEDC E MXSHISTORICOPEDI

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral
- Natureza: Dúvida
- Atualizado em: 2025-01-23T16:31:01.021-0300

## Contexto do Problema

## Passos para reproduzir
Carga nas tabelas PCPEDC E PCPEDI para as tabelas MXSHISTORICOPEDC e MXSHISTORICOPEDI para o período de todo o ano de 2024.

## Resultado apresentado
Atualmente constam registros na MXSHISTORICOPEDC somente a partir de 01/12/2024 00:00:00.

## Resultado esperado
Apresentado os dados referentes a todo 2024.

## Descrição
Cliente deseja que seja apresentado os dados referentes a 2024.

Atualmente constam registros na MXSHISTORICOPEDC somente a partir de 01/12/2024 00:00:00.

Alinhado com o DBA Lucas Silva e o Gatekeeper Filipe Padilha.

## Comentarios do Gatekeeper

### 1. 2025-01-23T16:31:01.020-0300 | Filipe do Amaral Padilha

Realizada a carga dos históricos de pedidos PEDC e PEDI referente ao ano passado inteiro 01/01/2024 a 31/12/2024 .

O histórico dos itens ainda está descendo via integração, para acompanhar você pode acessar
https://innovar.extratormaxima.com.br/registrospendentes

A carga foi feita somente na filial que eles já estão configurados para importar: Filial 1

Somente quando finalizar a baixa de todos os registros é que pode ser dado como finalizado. Lembre se que no maxGestão rotina 146 para comparar venda transmitida não bate em todos os casos e a Rotina 111 deve bater.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 418725
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Havia registros na MXSHISTORICOPEDC somente a partir de 01/12/2024' não consta no texto-fonte. | 'Os históricos de pedidos PEDC e PEDI de todo o ano de 2024 não estavam totalmente disponíveis' extrapola o texto-fonte; o texto apenas informa que a carga foi realizada e que o histórico dos itens ainda está descendo via integração. | 'A rotina 146 no maxGestão não é confiável para todos os casos' é uma reformulação interpretativa; o texto-fonte diz apenas que 'rotina 146 para comparar venda transmitida não bate em todos os casos'. | 'a conferência deve ser feita preferencialmente pela rotina 111' adiciona interpretação normativa; o texto-fonte diz que 'a Rotina 111 deve bater'.
