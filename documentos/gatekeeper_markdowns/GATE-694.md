# GATE-694 - Erro de processamento de pedidos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Banco de Dados
- Natureza: N/A
- Atualizado em: 2025-01-27T11:04:41.607-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Conforme informado via Discord, será realizada a tentativa de reprocessamento dos pedidos mediante análise do erro ORA600 por parte do dba responsável pelo banco do cliente.

## Comentarios do Gatekeeper

### 1. 2025-01-27T11:04:41.606-0300 | Filipe do Amaral Padilha

O problema ocorreu devido a uma informação corrompida dentro do banco Oracle, na tabela PCPEDCFV provavelmente no campo DADOSPED CLOB.

A causa raíz para isso nós não temos como identificar porque ocorreu dentro do banco Oracle localmente, e para identificar essa causa teria de ter analisado junto ao DBA o alert log do Oracle.

Porém para resolver o problema a gente fez o drop da coluna DADOSPED e em seguida, recriou ela no schema da LDF.

Recompilou o objeto e reenviou os pedidos com status 5, para status 0 para que eles fossem reintegrados.

No momento os pedidos estão integrando normalmente

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 419166
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Como encaminhamento, foi definida a análise do erro `ORA600` pelo DBA do cliente." | "Se necessário, o reprocessamento poderá ser realizado com as seguintes ações:" | A apresentação das ações como possibilidade futura/condicional ("poderá ser realizado") em vez de algo já executado. | A menção explícita a "DBA responsável pelo banco do cliente" extrapola o texto-fonte, que só cita "junto ao DBA". | A menção específica ao erro "ORA600" não aparece no texto-fonte.
