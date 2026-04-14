# GATE-489 - Checkin do cliente não subiu para a API

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Check-In/Check-Out
- Natureza: Dúvida
- Atualizado em: 2024-12-12T08:37:34.615-0300

## Contexto do Problema

## Passos para reproduzir
>>Abrir o mapa do maxGestão
>>Geolocalização> Painel de auditoria
>>Verificar o RCA 104 codusuario 91281

## Resultado apresentado
>>O cliente 245601 consta como 'apenas CHECKOUT'
>>Não consta na API o checkin
>>Na base MAXTRACK consta tanto o checkin quanto o checkout

## Resultado esperado
>>Deve aparecer no maxSolucoes  tanto o checkin como o checkout do RCA neste cliente

## Descrição
>>O checkin do RCA 104 não apareceu no maxGestão nem na API de rastro mesmo estando na base Maxtrack do RCA

## Comentarios do Gatekeeper

### 1. 2024-12-12T08:37:34.613-0300 | Filipe do Amaral Padilha

Devido a versão que o RCA estava utilizando, ocorreu um problema com a subida do rastro para a API e por este motivo, não estava sendo apresentado no maxGestão. Para resolver eu fiz a normalização dos dados, reenviando somente as informações que estavam presentes na base maxTracking, mas não na API de rastros.

Recomenda-se atualizar a versão do maxPedido para a mais recente (observei que já está 3.262.0) e monitorar se resolve definitivamente.

Para validar basta ir no maxGestão e filtrar os dados do dia 11/12/2024.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 411802
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma que 'o check-in não foi apresentado no maxGestão', mas o texto-fonte menciona apenas 'rastro', não especificamente check-in. | A resposta introduz o parâmetro 'RCA: 104', que não aparece no texto-fonte. | A resposta recomenda validar 'se o check-in e o check-out passam a ser apresentados corretamente', mas o texto-fonte não menciona check-in nem check-out.
