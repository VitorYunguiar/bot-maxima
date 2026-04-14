# GATE-295 - Erro no Mix Ideal dando erro

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido - Mix Ideal
- Natureza: Erro
- Atualizado em: 2024-11-13T14:45:58.015-0300

## Contexto do Problema

## Passos para reproduzir
1- Tentar cadastrar politica de desconto
2- Tentar Salvar

## Resultado apresentado
Erro descrito na imagem anexada

## Resultado esperado
Conseguir salvar normalmente sem apresentar erros

## Descrição
Cliente relatou sobre um erro em que quando cadastra políticas de desconto e tenta salvar, acaba aparecendo um erro que impede dele de salvar qualquer coisa. O ambiente já foi atualizado (extrator e banco de dados), porém, não houve mudanças

## Comentarios do Gatekeeper

### 1. 2024-11-07T14:41:47.479-0300 | Filipe do Amaral Padilha

Se trata de uma falha de sistema porque a gente não está exibindo uma mensagem intuitiva para o usuário; Vamos encaminhar essa questão da mensagem para N3, eu vou assumir o ticket temporariamente e devolver depois.

No entanto, é bem importante informar o cliente que, o problema é o cadastro de código auxiliar do produto 1572 na rotina 203 de cadastro de produto. Essa informação está faltando nesse produto, que seria o código auxiliar do produto que é compatível ao cadastro da embalagem. No caso para resolver a situação e ele conseguir cadastrar o produto no mix ideal, ele precisará cadastrar o código auxiliar desse produto.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 405577
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'erro ao salvar a política de desconto' não é mencionado no texto-fonte. | 'essa ausência impede o avanço da operação' extrapola o texto-fonte; o texto diz especificamente que ele não conseguirá cadastrar o produto no mix ideal sem o código auxiliar. | 'O erro não está relacionado à atualização de extrator ou banco' não consta no texto-fonte. | 'Após esse cadastro na rotina 203, o cliente deverá conseguir prosseguir com o cadastro normalmente' generaliza além do texto-fonte; o texto afirma especificamente que ele conseguirá cadastrar o produto no mix ideal.
