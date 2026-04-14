# GATE-54 - Preço de produto diferente na mesma região

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Protheus
- Assunto: MXPED - Produto - Preço Divergente
- Natureza: Dúvida
- Atualizado em: 2024-09-16T08:43:20.337-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do vendedor, iniciar um pedido nos clientes 02318906 e 02318923, comparando o preço de tabela do produto 62120001 no plano de pagamento à vista (sem taxas).

## Descrição
Cliente relata que os clientes 02318906 e 02318923 apresentam cálculo de preço diferente para o produto 62120001 na campanha de desconto 3909.
Foi verificado que a questão é apresentada também fora da campanha de desconto.

Foram verificados os seguintes dados:
>Cliente não utiliza tabela de impostos MXSTABTRIB, enviando diretamente pela tabela de preço
>Os dois clientes citados, embora sejam de praças diferentes, as praças estão vínculadas na mesma região (MXSPRACA, MXSCLIENTREGIAO)
>Na MXSTABR possui o mesmo preço para todas as regiões
>Não possui acréscimo por atividade (MXSATIVI)
>Não utilizam preço por embalagem
>Verificado que o cliente 02318906 possui um desconto ativo na MXSDESCONTO, entretanto ao realizar o delete na tabela em questão não houve alteração do preço.

Login para teste:
guaraves.rodrigo.resende

## Comentarios do Gatekeeper

Nenhum comentario elegivel do assignee foi identificado.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
