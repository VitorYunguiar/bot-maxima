# GATE-361 - maxCatalogo - Clientes não aparecem

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: João Pedro Faria Cabral [X]
- ERP do cliente: Winthor
- Assunto: MAXCTN - Cliente - Não Aparece
- Natureza: Erro
- Atualizado em: 2024-11-21T17:34:12.824-0300

## Contexto do Problema

## Passos para reproduzir
ACESSO
quallypet.quallypet.simone

ACESSAR MAXPEDIDO
ACESSAR MAXCATALOGO

divergencia quanto a quantidade de clientes

## Resultado apresentado
PROBLEMA PRINCIPAL
não ver clientes que não são consumidores final

cuidado ao testar o maxCatalogo na versão que o cliente utiliza (2.12.1), esta versão não comunica os pedidos entre si.

Testei na 2.12.15 e ja liberei para ele atualizar, o problema de não ver os clientes permanece na 2.12.15.

## Resultado esperado
Identificar a causa e devolver os clientes ao maxCatalogo do cliente

## Descrição
O usuario 44 está com acesso ao maxCatalogo na versão 2.12.1
nesta versão ele tinha problemas com iniciar pedidos e transmitir para o maxPedido e tambem para ver os clientes sem ser os CONSUMIDORES FINAL, como o cliente CODCLI 997

Assim que atualizei para a versão 2.12.15 o maxCatalogo se comunica com o maxPedido ao realizar o pre-pedido, no entanto, COM EXCESSÃO DOS CONSUMIDORES FINAIS, OS DEMAIS CLIENTES AINDA NÃO APARECEM

## Comentarios do Gatekeeper

### 1. 2024-11-21T17:34:12.823-0300 | Filipe do Amaral Padilha

Enviado para N3 não identifiquei motivo lógico para não exibir os clientes no maxCatálogo

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 408032
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "incluindo os clientes que não são consumidores finais" não consta no texto-fonte. | "A análise realizada não encontrou causa lógica para a falha informada no comentário" extrapola o texto-fonte ao mencionar análise realizada e falha informada. | "que passa a ser o responsável pela continuidade da investigação" não consta no texto-fonte. | "Não foi identificada causa para o comportamento reportado" usa formulação não presente literalmente no texto-fonte. | "Não há evidência, até o momento, que explique logicamente a não exibição dos clientes no MaxCatálogo" menciona ausência de evidência, o que não consta no texto-fonte. | "Próximo passo - Prosseguir com a análise pelo N3" não está explicitamente stated no texto-fonte, embora o envio para N3 sugira escalonamento.
