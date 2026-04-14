# GATE-371 - Cliente não aparece

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Não Aparece
- Natureza: Erro
- Atualizado em: 2024-11-22T12:53:51.336-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do vendedor, procurar o cliente 102548.

## Resultado apresentado
É verificado que o cliente não é apresentado na base do RCA.

## Resultado esperado
É esperado que o cliente seja apresentado para o vendedor.

## Descrição
Cliente relata que ao vincular clientes (ex.: 102548) ao usuário 325, os mesmos não são exibidos na apk.
Foi realizada consulta na MXSCLIENT, observando os campos CODUSUR1, CODUSUR2 (possui vínculo com o RCA), CODUSUR3, DTEXCLUSAO, CODOPERACAO, e as tabelas ERP_MXSUSURCLI e MXSRESTRICAO/MXSRESTRICAOVENDA. Foi verificado que apenas na tabela MXSVCLIENTESRCA existe o vínculo do cliente com o vendedor, entretanto ao sincronizar/baixar a base do vendedor, o cliente em questão não é baixado para a base.

Login para teste:
jwarmazem.roberto

## Comentarios do Gatekeeper

### 1. 2024-11-22T12:53:51.334-0300 | Filipe do Amaral Padilha

Suporte identificou que era diverGência no CODUSUR da MXSCLIENT e já resolveu

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
