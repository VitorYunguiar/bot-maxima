# GATE-38 - Margem de lucratividade não altera

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXPED - Produto - Margem de Lucratividade
- Natureza: Dúvida
- Atualizado em: 2024-09-11T08:02:48.436-0300

## Contexto do Problema

## Passos para reproduzir
>liane.540
>Acessar APK
>Iniciar pedido
>Adicionar um item
>Observar como a lucratividade do item se comporta inserindo desconto/acréscimo no produto.

## Descrição
Após parametrizar para exibir os campos de lucratividade foi verificado que os campos estão apresentando uma margem de lucratividade que inicialmente não faz sentido. Ocorre que ao inserir um produto, independente da quantidade de desconto aplicada, a margem de lucratividade permanece em 92.98% ou 92.99%.

Gostaria de entender qual cálculo está sendo feito.

## Comentarios do Gatekeeper

### 1. 2024-09-10T16:56:16.280-0300 | Filipe do Amaral Padilha

Cenário utilizado:

Cliente: 103786

Produto: 5400100

O cálculo de lucratividade aplicado ao produto é o seguinte: ((61.74 - 4.3318) / 61.74) * 100 resultando nos 92,98% de lucratividade. Esses 4.3318 são referentes ao custo financeiro do produto que é calculado da seguinte forma: MXSTABPR.PVENDA1 * (MXSTRIBUT.CODICMTAB / 100). Atualmente, esse é o cáculo em todos os produtos deles e ele ocorre devido a esse parâmetro estar desativado (DESCONSIDERAR_IMPOSTOS_CALCULO_LUCRATIVIDADE = N), com esse parâmetro desativado, validamos a tributação para calcular o custo finanaceiro que é utilizado no cáculo de lucratividade do item.

O que acontece se ativar o parâmetro DESCONSIDERAR_IMPOSTOS_CALCULO_LUCRATIVIDADE?

Então a gente simplifica o cáluclo de lucratividade e passa a buscar o custofinanceiro diretamente da MXSEST.CUSTOFIN, como está 0,01, então o resultado da lucratividade seria 99,98%

Quando é colocado desconto, então, ocorre o seguinte:

Por exemplo: 80% de desc.

PVENDA = 12.35

Lucratividade: (PVENDA - CUSTOFIN) / PVENDA

(12.35 - (12.35 * 0.07 + 0.01)) / 12.35
Sendo: 0.07 o CODICMTAB e 0.01 o custo real original CUSTOREP da MXSEST

(12.35 - 0.8745) / 12.35

11,4755 / 12.35
Esse cálculo vai resultar no 92.92%

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, needs_review
- Comentarios primarios: 393816
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
