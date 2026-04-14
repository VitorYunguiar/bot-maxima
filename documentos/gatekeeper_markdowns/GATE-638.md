# GATE-638 - ordenação de criticas sendo exibidas de forma adequada

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido - Crítica
- Natureza: Dúvida
- Atualizado em: 2025-01-15T10:04:59.032-0300

## Contexto do Problema

## Passos para reproduzir
efetuar o login no aplicatico com o login wbcomp.ti ;
acessar a tela de pedidos e observar as legendas do pedido, bem como as criticas do pedido presente e a ordem com que são apresentadas;

## Resultado apresentado
a aplicação está apresentando criticas sem seguir a ordem temporal dos eventos que o pedido passou e com isso gerando legendas que não condizem com a condição atual do pedido.

## Resultado esperado
é esperado que a ordem de criticas presentes siga os registros de data e hora com que foram realizados, tranzendo o real status dos pedidos.

## Descrição
Senhores, ao analisar o cenário relatado pelo cliente no ticket citado, estou identificando que está ocorrendo uma ordenação inadequada de criticas no pedido, onde o ID critica foi gerado fora da sequencia esperada para a ocorrência dos eventos que foram aplicados pedido. No cenário que analisei, observa-se que a critica com o maior ID é uma critica anterior a critica mais atual presente para o pedido.

!image-2025-01-14-16-17-40-724.png!

Essa situação gera um comportamento inadequado no app, exibindo legendas que não condizem com a realidade do pedido levando a uma interpretação inadequada da real posição e status do pedido.

É possivel constatar isso via integração do pedido, que demonstra uma critica de erro:

!image-2025-01-14-16-20-32-735.png!

mas o app exibe uma legenda de falha parcial:

!image-2025-01-14-16-21-03-683.png!

## Comentarios do Gatekeeper

### 1. 2025-01-15T10:04:59.030-0300 | Filipe do Amaral Padilha

Foi inserido o parâmetro USAR_STATUS_ULTIMACRITICA para garantir que o sequenciamento está sendo feito conforme a última crítica.

Realizada a normalização e redefinição do sequenciador MXSPROXNUMCRITICA no banco local e nuvem do cliente.

Para normalizar para os RCAs eles precisam sincronizar o maxPedido.

Podem realizar o swipe também que a timeline deverá atualizar corretamente os pedidos retroativos, pois o número da crítica foi aumentado e reprocessado.

Também encaminhei para N3 porque a solução definitiva depende da correção que está sendo feita no ticket MXPEDDV-72797

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 416884
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificada ordenação/sequenciamento inadequado das críticas do pedido, o que impacta a legenda e a timeline exibidas no aplicativo." — o texto-fonte não menciona legenda nem afirma explicitamente que havia ordenação inadequada; apenas descreve ações/correções realizadas. | "A análise confirmou que o problema está relacionado ao uso da última crítica para definição do status" — o texto-fonte diz que foi inserido o parâmetro para garantir o sequenciamento conforme a última crítica, mas não afirma que houve uma análise confirmando a causa do problema. | "ajustado o cenário" — o texto-fonte não usa essa formulação; informa que o número da crítica foi aumentado e reprocessado, permitindo que a timeline atualize corretamente. | "manter acompanhamento com o N3" — o texto-fonte apenas diz que foi encaminhado para N3, não que se deva manter acompanhamento. | "Limitação atual" — a estrutura é interpretativa; embora a dependência do ticket MXPEDDV-72797 esteja no texto-fonte, a classificação como 'limitação atual' não está explicitamente dita.
