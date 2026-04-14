# GATE-557 - Filtro de comissão diferenciada

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Comissão
- Natureza: Dúvida
- Atualizado em: 2024-12-27T14:35:01.333-0300

## Contexto do Problema

## Passos para reproduzir
>> Iniciar pedido para qualquer cliente.
>> Na aba tabela, marcar o filtro "Comissão diferenciada";

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Cliente deseja usar o filtro de comissão diferenciada no maxPedido, porem a única informação que temos é um artigo da base de conhecimento do pedido de venda.

Esse filtro funciona no maxPedido?

Como é feito o cadastro da comissão diferenciada?

[https://basedeconhecimento.maximatech.com.br/pages/viewpage.action?pageId=14811323]

Login de exemplo: mba.2099

## Comentarios do Gatekeeper

### 1. 2024-12-27T12:23:45.627-0300 | Filipe do Amaral Padilha

No maxPedido, basicamente quando os parâmetros OPERADOR_COMISSAO_DIFERENCIADA e PERCENTUAL_COMISSAO_DIFERENCIADA não estão cadastrados, ele tenta buscar os dados da tabela MXSCOMISSAODIFERENCIADA.

Essa tabela MXSCOMISSAODIFERENCIADA no maxPedido não é alimentada em nenhum momento porque provavelmente é uma funcionalidade que veio herdada do pedido de vendas. Embora tenhamos esse detalhe, a comissão diferenciada funciona no maxPedido e abaixo vou explicar como atualmente:

Você pode preencher o parâmetro OPERADOR_COMISSAO_DIFERENCIADA (Ele é do tipo String "1") utilizando os seguintes operadores e condições:

> (maior que): Verifica se o valor é maior que o percentual definido.
< (menor que): Verifica se o valor é menor que o percentual definido.
>= (maior ou igual a): Verifica se o valor é maior ou igual ao percentual definido.
<= (menor ou igual a): Verifica se o valor é menor ou igual ao percentual definido.
== (igual a): Verifica se o valor é exatamente igual ao percentual definido.
= (igual a): Também verifica se o valor é exatamente igual ao percentual definido (mesma lógica do operador ==).

Exemplos:
Operador > e Percentual 10:

O sistema verificará se o valor é maior que 10.

Operador < e Percentual 5:

O sistema verificará se o valor é menor que 5.

Operador >= e Percentual 8:

O sistema verificará se o valor é maior ou igual a 8.

Operador = e Percentual 12:

O sistema verificará se o valor é exatamente igual a 12.

Essas condições serão aplicadas automaticamente no sistema com base nos parâmetros que você informar.

O parâmetro PERCENTUAL_COMISSAO_DIFERENCIADA é do tipo string (1) também e deverá ser preenchido com o valor da comissão que você deseja definir como critério de comparação (por exemplo, "10" ou "15.5").

O percentual definido é comparado com os campos de comissão cadastrados no produto (MXSPRODUT) Rotina 203. São os campos (comissão cadastrada para o produto) SELECT PCOMREP1, PCOMINT1, PCOMEXT1, CODPROD FROM MXSPRODUT WHERE CODPROD IN();

### 2. 2024-12-27T14:35:01.333-0300 | Filipe do Amaral Padilha

O filtro de comissão diferenciada basicamente faz a leitura dos parâmetros, assim ele entende o critério de comparação e apresenta somente os produtos que se encaixarem no critério de avaliação. Por exemplo, se você configurar o parâmetro OPERADOR_COMISSAO_DIFERENCIADA = ">" e PERCENTUAL_COMISSAO_DIFERENCIADA = 2, então o filtro ao ser ativado, irá mostrar somente produtos com a comissão cadastrada > que 2 cadastro esse que vem da MXSPRODUT.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414124, 414148
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "sua operação depende exclusivamente da configuração dos parâmetros abaixo" — o texto-fonte diz que quando os parâmetros não estão cadastrados ele tenta buscar dados na tabela MXSCOMISSAODIFERENCIADA, então 'exclusivamente' não está totalmente suportado. | "Validar ou preencher os campos de comissão dos produtos na MXSPRODUT" — o texto-fonte diz que o percentual é comparado com os campos de comissão cadastrados no produto, mas não afirma como instrução necessária 'validar ou preencher' esses campos. | "não é esse o mecanismo que deve ser usado no maxPedido" — o texto-fonte diz que a tabela não é alimentada e explica como funciona atualmente via parâmetros, mas não afirma explicitamente em termos normativos que esse mecanismo 'não deve ser usado'.
