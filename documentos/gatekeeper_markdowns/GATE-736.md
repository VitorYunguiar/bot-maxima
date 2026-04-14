# GATE-736 - Posição dos pedidos não atualizam na timeline

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Timeline
- Natureza: Dúvida
- Atualizado em: 2025-02-03T16:55:20.377-0300

## Contexto do Problema

## Passos para reproduzir
>> Verificar pedidos na MXSHISTORICOPEDC

## Resultado apresentado
Status dos pedidos não atualizam.

## Resultado esperado
Status atualizando na sync automática corretamente.

## Descrição
Posição dos pedidos não atualizam na timeline.

Login: ttslz.gefran1238

Base em anexo, ocorrendo com multiplos RCAs.

## Comentarios do Gatekeeper

### 1. 2025-02-03T15:41:09.584-0300 | Filipe do Amaral Padilha

Foi realizada a carga dos dados retroativos que não haviam descido naturalmente para atualização da timeline através de sincronização automática.

Foi realizada carga somente nesse caso porque já foi alinhado com o desenvolvimento sobre a última correção necessária que saiu na versão 4.

Então os RCAs que estiverem usando o maxSync automática devem estar atualizados para a versão de ponta da V4 e então já podem conferir se os status foram atualizados automaticamente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 421012
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Identificada a causa de que os dados retroativos não haviam descido naturalmente para atualização da timeline pela sincronização automática | o que impedia a atualização do status dos pedidos | dados retroativos pendentes | para recompor a timeline | Responsável pela correção de referência: desenvolvimento
