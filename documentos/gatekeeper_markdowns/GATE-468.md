# GATE-468 - Trajeto incorreto do RCA aos clientes

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXGESN - Mapas - Dados Incorretos
- Natureza: Dúvida
- Atualizado em: 2024-12-06T10:07:55.883-0300

## Contexto do Problema

## Passos para reproduzir
>>Entrar em geolocalização
>>Mapas
>>Clicar no RCA
>>Clientes
>>Colocar qualquer data (Aparecem acima do dia 18)

## Resultado apresentado
>>No trajeto do RCA mostrado, a localização do RCA "pula" para um ponto específico no mapa de tempos em tempos, gerando assim um transtorno.
>>Os parâmetros  "GPS_TRACKING_ENABLED" e "HABILITA_EVENTOS" estão ativos simultâneamente

## Resultado esperado
>>A localização apresentada deve ser a mesma feita pelo RCA.

## Descrição
>>O trajeto do RCA 70 (Codusuario: 104860) mostra uma rota incorreta do RCA onde ele de tempos em tempos retorna a um ponto específico do mapa

>>Os parâmetros "GPS_TRACKING_ENABLED" e "HABILITA_EVENTOS" ativos simultâneamente

>>Base maxTracking em anexo

## Comentarios do Gatekeeper

### 1. 2024-12-06T09:37:29.438-0300 | Filipe do Amaral Padilha

Vamos fazer o seguinte, na tentativa de resolver para que não ocorram casos futuramente do mesmo problema:

Desativa o parâmetro HABILITA_EVENTOS = N para todos os RCAs.
Deixa ativado somente o GPS_TRACKING_ENABLED = S; (do jeito que já está)

E solicita para todos os RCAs atualizarem para a última versão, Libera no portal deles a última versão.

Feito isso, pede para acompanhar se, depois de atualizado, parou de ocorrer o problema. Caso ocorra o problema, mesmo atualizado, dai pode mandar outro GATE; Se ocorrer em versão desatualizada, cobra fazer a atualização do RCA.

Referente ao cenário já apresentando (dos rastros picotados) eu não sei se tem como converter, então eu vou mandar para N3 do maxgestão para eles darem uma olhada.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 410753
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "A causa provável está relacionada ao uso simultâneo dos parâmetros HABILITA_EVENTOS e GPS_TRACKING_ENABLED" não está afirmado no texto-fonte. | "condição identificada no ambiente" não está afirmado no texto-fonte. | "deve ser aberto outro GATE" extrapola levemente o texto, que diz "pode mandar outro GATE".
