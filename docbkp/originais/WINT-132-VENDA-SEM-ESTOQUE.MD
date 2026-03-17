# Revisao de Fonte Web: WINT

## Fonte
- https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030488274-WINT-Quais-s%C3%A3o-os-par%C3%A2metros-da-rotina-132-utilizados-para-n%C3%A3o-realizar-venda-sem-estoque

## Metadados
- Tipo detectado: `html`
- Gerado em: `2026-02-11T17:39:25.507041+00:00`
- Fatos extraidos (LangExtract): `14`

## Conhecimento Extraido
[LangExtract] Fatos estruturados extraidos:
- [procedimento] Acessar a rotina 132 para configurar parâmetros de venda sem estoque (modulo=132; acao=configurar parametros)
- [requisito] Parâmetro 1630 - Aceitar venda sem estoque deve estar marcado como Não (campo=1630)
- [requisito] Parâmetro 1420 - Aceitar venda sem estoque deve estar marcado como Não (campo=1420)
- [requisito] Parâmetro 2457 - Validar estoque ao Gravar o Pedido deve estar marcado como Sim (campo=2457)
- [requisito] Parâmetro 1116 - Aceita venda balcão com estoque negativo deve estar marcado como Não (campo=1116)
- [requisito] Parâmetro 1619 - Autosserviço deve estar marcado como Não (campo=1619)
- [requisito] Parâmetro 1950 - Verifica estoque no momento da venda deve estar marcado como Sim (campo=1950)
- [requisito] Parâmetro 2373 - Validar estoque ao Gravar o Pedido deve estar marcado como Sim (campo=2373)
- [requisito] Parâmetro 1429 - Aceitar pedido de venda Bloqueado deve estar marcado como Não (campo=1429)
- [requisito] Parâmetro 1413 - Avisar Falta de estoque deve estar marcado como Sim (campo=1413)
- [requisito] Parâmetro 2548 - Aceita venda sem estoque FV deve estar marcado como Não (campo=2548)
- [procedimento] Clicar no botão Salvar e fechar após as alterações (modulo=132; acao=salvar)
- [procedimento] Validar origem de pedido B (Balcão) e R (Balcão Reserva) na rotina 316 via parâmetros 1116 e 1619 (modulo=316 - Digitar Pedido de Venda; acao=validar origem de pedido)
- [requisito] Parâmetros configurados como Sim faturam o pedido sem estoque negativando-o (campo=1116 e 1619)
