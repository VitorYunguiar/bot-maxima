# Regras de Negocio Canonicas - maxPedido (N1)

Este documento e um contexto fixo para o bot N1. Ele resume regras estaveis de negocio ja presentes na base.

## 1) Escopo do produto
- O maxPedido e um app mobile de forca de vendas integrado ao ERP do cliente.
- O fluxo de pedido depende de configuracoes do maxPedido e, em alguns cenarios, de parametros do ERP (ex.: Winthor).
- O bot N1 deve priorizar orientacoes praticas: configuracao, validacao de dados e trilha de troubleshooting.

## 2) Fluxo macro de pedido e integracao
- O pedido sai do app para a nuvem da Maxima.
- A integracao com ERP consome o pedido e devolve status/critica.
- A timeline do pedido depende do retorno correto do ERP para as estruturas de historico.
- Em cenarios de "status nao atualiza", validar cadeia completa: envio, processamento ERP, retorno de status.

## 3) Tabelas frequentemente envolvidas (consulta operacional)
- MXSINTEGRACAOPEDIDO: registro de integracao do pedido.
- MXSHISTORICOPEDC: historico/status usado na timeline.
- MXSINTEGRACAOPEDIDOLOG e MXSINTEGRACAOPEDIDO_LOGST: logs de integracao.
- MXSHISTORICOCRITICA: historico de criticas.

Observacao:
- Nome de tabela/campo deve sempre ser confirmado nos trechos recuperados.
- Se a pergunta pedir SQL, priorizar consultas ja documentadas na base.

## 4) Regras recorrentes de negocio
- Cliente bloqueado: comportamento depende de combinacao de parametros no maxPedido e, em Winthor, tambem no ERP.
- Filial retira/desmembramento: pode gerar multiplos pedidos por filial quando configurado.
- Pedido em autorizacao pode impedir ou alterar fluxo esperado de desmembramento/processamento.
- Parametros de check-in/check-out/GPS podem bloquear confeccao do pedido quando exigidos.

## 5) Regra de atendimento N1
- Responder com base no que estiver documentado.
- Se faltar informacao critica para fechar diagnostico, listar verificacoes objetivas e indicar escalonamento para N2.
- Evitar recomendacoes genericas sem validacao de parametro/tabela/processo.

## 6) Fontes canonicas usadas neste resumo
- 01-PARAMETROS-E-CONFIGURACAO.md
- 02-PEDIDOS-E-VENDAS.md
- 05-SQL-BANCO-E-INTEGRACAO.md
- SERVICE-DESK-PROCESSOS.md
- SERVICE_DESK_MAXIMA_ORGANIZADO.md
