# GATE-718 - divergencia valores de grafico comissão v4 e v3

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Comissão
- Natureza: Dúvida
- Atualizado em: 2025-01-31T16:58:53.834-0300

## Contexto do Problema

## Passos para reproduzir
login: vjr.call.thais
efetuar o login na aplicação e atualizar os graficos da tela inicial e atualização de menu.
Comparar os resultados entre V3 e V4

## Resultado apresentado
a versão ponta tras dados divergentes dos valores retornados no winthor e ná V3

## Resultado esperado
é esperado que o valor retornado na V4 seja equivalente o que é exibido na V3

## Descrição
Senhores, estamos identificando divergências de comportamento nos valores que estão sendo retornados nos gráficos da V4. Enquanto a versão 3.269.2 retorna valores adequados para o que está presente na 1249:

!image-2025-01-29-13-19-27-179.png!

A versão 4.000.4 trás valores completamente diferentes:

!image-2025-01-29-13-20-09-404.png!

Observei que além da comissão, essa situação é apresentada em outros cenários, onde o valor de venda transmitida tbm tem essa divergência. Ocorreu alguma alteração no formato de calculo que a V4 tem para retornar esses valores ou há algum erro na aplicação que gera essa situação?

## Comentarios do Gatekeeper

### 1. 2025-01-31T16:08:17.458-0300 | Filipe do Amaral Padilha

A comissão atualiza na tela conforme o botão que você pode alterar no gráfico 1 de:

"últimos 7 dias"
"última semana"
"Semana atual"
"Mês atual"

E na tela inicial, considerando principalmente a questão da versão, o parâmetro "CRITERIO_VENDA_CARD_PEDIDO" atua. Por padrão ele mostra no gráfico 1 a apuração por venda Transmitida.

Então eles poderiam mudar o parâmetro para CRITERIO_VENDA_CARD_PEDIDO = F.

InformacoesRepresentanteResumo -> REQ_MXSRESUMOVENDAS

InformacoesRepresentanteResumoDetalhado -> REQ_MXSRESUMOVENDASDETALHE

obterInformacoesRepresentanteMix -> REQ_MXSVENDA_MIX

Eu fiz uma análise prévia, porém, não consegui resolver a divergência entre v3 e v4 é evidente, vou encaminhar para dev porque exige um tempo de análise muito maior, de analisar scripts do backend que carregams os dados para depois carregarem no maxPedido e serem exibidos

## Resposta Canonica

Foi identificada divergência entre os valores exibidos nos gráficos da V3 e da V4, sem conclusão definitiva na análise prévia.

### Conclusão da análise
- A divergência entre V3 e V4 é evidente.
- A comissão é recalculada na tela conforme o botão selecionado no gráfico 1:
  - últimos 7 dias
  - última semana
  - semana atual
  - mês atual
- Por padrão, o gráfico 1 apresenta a apuração por venda **Transmitida**.
- Na tela inicial, o parâmetro **CRITERIO_VENDA_CARD_PEDIDO** influencia o comportamento, principalmente em relação à versão.

### Ação recomendada
1. Alterar o parâmetro para:
   - **CRITERIO_VENDA_CARD_PEDIDO = F**
2. Encaminhar para **dev** para análise aprofundada dos scripts de backend responsáveis por carregar os dados antes da exibição no maxPedido.

### Limitações da análise
- A análise realizada foi apenas prévia.
- Não foi possível determinar a causa exata da divergência entre V3 e V4.
- A investigação requer análise adicional dos scripts de backend envolvidos na carga e exibição dos dados.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 420645
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
