# GATE-516 - Pedido duplicado na MXSINTEGRACAOPEDIDO

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: JPLM
- Assunto: MXPED - Integração - API Máxima
- Natureza: Dúvida
- Atualizado em: 2024-12-17T12:05:59.163-0300

## Contexto do Problema

## Passos para reproduzir
Verificar base do RCA e MXSINTEGRACAOPEDIDO.

## Resultado apresentado
Na tabela de integração constam os pedidos duplicados enquanto na base do RCA consta apenas um pedido.

## Resultado esperado
Pedidos enviados sem duplicação.

## Descrição
Pedidos estão sendo enviados duplicados para a MXSINTEGRACAOPEDIDO, enquanto na base do RCA consta somente um.

Ex: NUMPEDRCA = 944016728 e 944016709

Na base do RCA consta somente um pedido, sem reenvio, porem na MXSINTEGRACAOPEDIDO constam dois pedidos com o mesmo NUMPED e horários com apenas um segundo de diferença, ocasionando dois pedidos idênticos na integração do cliente. Não existe evidencia de reenvio manual por parte do RCA.

Ocorrendo esporadicamente, sem apresentar um padrão.

Ocorreu outras vezes na versão 3.240.1, cliente orientado a migrar para a versão ponta disponivel no momento, porem voltou a ocorrer agora.

Login: donizete.0944
Base em anexo.

## Comentarios do Gatekeeper

### 1. 2024-12-17T12:04:25.150-0300 | Filipe do Amaral Padilha

Será enviado para N3, foi identificado na MXSINTEGRACAOPEDIDOLOG que esses pedidos estão entrando duplicados no nosso bakend, o que pode significar que o aplicativo está fazendo requisições duplicadas para salvar os pedidos da APK para a API

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 412638
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'pela análise textual dos registros' — o texto-fonte apenas diz que foi identificado na MXSINTEGRACAOPEDIDOLOG, não menciona 'análise textual'. | 'deve analisar' — o texto-fonte diz apenas 'Será enviado para N3', sem explicitar que o N3 deve analisar a possível duplicidade de requisições.
