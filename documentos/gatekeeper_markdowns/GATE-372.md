# GATE-372 - Valores de meta divergentes da central de configurações

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: STORM SYSTEM
- Assunto: MXGESN - Vendas Prevista x Realizada
- Natureza: Dúvida
- Atualizado em: 2024-11-25T09:19:00.982-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar MaxGestão
>Vendas
>Acompanhamento Vendas Previstas X Realizadas
>Filtrar conforme anexo
>Ver os departamentos
>Verificar o campo "Valor Venda Prevista" do departamento HASKELL

## Resultado apresentado
Quando no maxGestão, ao acessar a tela de "Acompanhamento Venda Prevista versus Realizada", filtrar conforme anexo, e clicar para ver os departamentos, podemos ver que
é exibido a venda prevista pra esse departamento no valor de R$220.000.

Anexei no ticket um video explicando a demanda e a análise que eu fiz.

## Resultado esperado
Entender de onde está vindo o valor de R$220.000

## Descrição
Boa tarde,

Estou com esse cenário da D.M PINDANGA onde no acompanhamento de vendas previstas versus realizada o valor das metas por departamento aparece divergente do que está cadastrado na central de conigurações.

Na central a meta da HASKELL tem uma meta no valor de R$100.000 cadastrada para a RCA 135 - CAROLINE na filial 1.

Quando no maxGestão, ao acessar a tela de "Acompanhamento Venda Prevista versus Realizada", filtrar conforme anexo, e clicar para ver os departamentos, podemos ver que
é exibido a venda prevista pra esse departamento no valor de R$220.000.

## Comentarios do Gatekeeper

### 1. 2024-11-25T09:19:00.980-0300 | Filipe do Amaral Padilha

Será enviado para N3 porque pelo código, não tem nada que impeça de metas já apagadas, de serem exibidas na apuração da venda prevista, porém esse conceito precisa ser revisado em N3 entre os devs e o P.O;

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review, requires_attachment_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
