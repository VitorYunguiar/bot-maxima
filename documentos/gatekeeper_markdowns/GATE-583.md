# GATE-583 - Integradora OERPs

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Não se Aplica
- Assunto: MXPED - Integração - Integrador OERPs
- Natureza: Dúvida
- Atualizado em: 2025-01-07T08:48:05.046-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Foi verificado que a integradora do ERP está retornando status de erro/não está realizando o fluxo de integração dos pedidos. Ao analisar o retorno do ERP, foi verificado que a integração dos pedidos está comprometida devido ao campo Representante no objeto_json estar sendo enviado nulo. Foi orientado ao cliente que a integração deveria trazer o campo codusur fora do objeto do json, uma vez que não é um campo variável.
A integração do cliente será alterada, entretanto o cliente busca uma maneira de resolver de forma paliativa o problema apresentado, pois diversos vendedores estão com pedidos parados na nuvem.

## Comentarios do Gatekeeper

Nenhum comentario elegivel do assignee foi identificado.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
