# GATE-281 - Análise no relatório do maxGestão

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatórios - Dados Inconsistentes
- Natureza: Dúvida
- Atualizado em: 2024-11-06T16:32:07.459-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar relatórios maxGestão
>Procurar pelo relatório "Roteiro de Visita de RCAs por Seção"
>Selecionar dia 04 ao dia 04
>Todas filiais
>Equipe 33
>Seção  "Cigarros"
>Pesquisar

## Resultado apresentado
Ao consultar ele retorna 0 em todas as linhas da coluna "Previsto".

## Resultado esperado
O cliente gostaria de entender por que o valor retornado é 0 nessa coluna se no Winthor o campo é preenchido para alguns RCAs.

## Descrição
Bom dia Filipe, o Glesio da Donizete abriu essa demanda informando que as informações do relatório de visita por seção não estão batendo com o Winthor. Esse mesmo relatório não tem rotina correspondente no Winthor porém não sei como validar esse cenário e de onde o relatório puxa as informações para montar um resultado.

## Comentarios do Gatekeeper

### 1. 2024-11-06T16:32:07.458-0300 | Filipe do Amaral Padilha

Eu vou enviar para N3 para eles verificarem e explicarem essa questão porque eu não consegui identificar o motivo de não exibir dados.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 405377
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma especificamente que a coluna “Previsto” está sendo retornada com valor 0. | A resposta afirma especificamente que o problema ocorre no relatório “Roteiro de Visita de RCAs por Seção”. | A resposta menciona “divergência informada em relação ao preenchimento observado no Winthor”, o que não aparece no texto-fonte. | A resposta afirma que o N3 deve esclarecer “a origem dos valores retornados no relatório”, detalhamento não presente no texto-fonte.
