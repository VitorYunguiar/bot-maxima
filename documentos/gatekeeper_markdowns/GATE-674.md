# GATE-674 - Estorno repetido no maxPag

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - MaxTrack
- Natureza: Dúvida
- Atualizado em: 2025-01-23T08:04:50.739-0300

## Contexto do Problema

## Passos para reproduzir
Bom dia Carlos / Filipe,

Gostaria de ajuda pra entender o que aconteceu com o pedido 1220002190 (NUMPEDERP) que houveram 3 estornos no valor de R$ 860, somando os 3 chegamos praticamente no valor do pedido. Porém, o VLATEND gravado na MXSHISTORICOPEDC é de R$ 1.724,04 e está com a posição F.

>>Acessar maxPag
>Transações
>Filtrar data 07/01/25 até 07/01/25
>Filtrar todas filiais, gateways, status e ambientes
>Em "campo extra" inserir 805369
>Pesquisar
>Clicar nas movimentações do pedido
>Observar em "Histórico de Movimentações" a quantidade de estornos

>>Consultar na MXSHISTORICOPEDC:
SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED = 1220002190;
>Observar as colunas VLATEND e POSICAO

## Resultado apresentado
O pedido 1220002190 (NUMPEDERP) teve 3 estornos no valor de R$ 860 realizados em um intervalo de 3 minutos de um estorno para o outro, durante a madrugada.

## Resultado esperado
Entender o por que do maxPag ter estornado esses valores se o pedido foi atendido com um valor e R$ 1.724,04

## Comentarios do Gatekeeper

### 1. 2025-01-23T08:04:50.739-0300 | Filipe do Amaral Padilha

Ticket foi enviado para N3, aguardar retorno -> https://suporte.maximatech.com.br/browse/MXPEDDV-88160

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, grounding_failed, needs_review
- Comentarios primarios: 418523
- Secoes ausentes: Descrição
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Não há causa confirmada para o comportamento do pedido 1220002190. | A análise técnica está em andamento com o N3, por meio do ticket MXPEDDV-88160. | Até o momento, não foram disponibilizadas evidências conclusivas, parâmetros adicionais ou SQL complementar. | Isso permitiria afirmar o motivo dos 3 estornos observados. | Responsável: N3.
