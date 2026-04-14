# GATE-803 - lentidão para acessar historico de pedido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Lentidão - APK
- Natureza: Dúvida
- Atualizado em: 2025-02-14T16:41:59.737-0300

## Contexto do Problema

## Passos para reproduzir
login: macomerc.rca6
importar a base em anexo;
ir a tela de pedidos e clicar no pedido de exemplo
observar o resultado

## Resultado apresentado
o app leva cerca de 35 segundos para abrir o historico do pedido

## Resultado esperado
é esperado que a abertura do pedido seja mais rapida.

## Descrição
APK com lentidão acima do esperado para acessar o historico de um pedido (video em anexo). O pedido em si contém 55 itens, mas está demorando mais que o esperado para acessa-lo

numped 6017899:

!image-2025-02-14-12-19-45-645.png!

## Comentarios do Gatekeeper

### 1. 2025-02-14T15:53:54.135-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 onde os desenvolvedores vão ter mais tempo para analisar o fluxo inteiro de carregamento desses dados e identificar o ponto que gera lentidão

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 424183
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Foi constatado que a abertura do histórico do pedido apresenta lentidão acima do esperado no cenário informado.' não está totalmente suportado; o texto-fonte menciona lentidão no carregamento desses dados, mas não especifica 'abertura do histórico do pedido' nem 'acima do esperado' ou 'no cenário informado'. | 'Com base nos fatos disponíveis, a causa ainda não foi identificada.' não está explicitamente dito no texto-fonte; apenas se informa que o ponto que gera lentidão será identificado. | 'A tratativa indicada é o encaminhamento para o time N3 / desenvolvedores' adiciona 'time', embora o encaminhamento para N3 e desenvolvedores esteja alinhado em essência. | 'análise detalhada de todo o fluxo de carregamento dos dados' extrapola levemente 'analisar o fluxo inteiro de carregamento desses dados'. | 'identificação objetiva do ponto responsável pela lentidão' acrescenta 'objetiva', termo não presente no texto-fonte.
