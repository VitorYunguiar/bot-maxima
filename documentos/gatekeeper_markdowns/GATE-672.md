# GATE-672 - Divergencia de preço entre clientes

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Protheus
- Assunto: MXPED - Produto - Preço Divergente
- Natureza: Dúvida
- Atualizado em: 2025-01-22T10:54:41.094-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxPedido;
>> Reproduzir os dois cenários nos dois clientes;

## Resultado apresentado
Mesmo com os cenários iguais existe uma divergencia de preço no produto 62120001 entre os dois clientes.

## Resultado esperado
Preços iguais.

## Descrição
Está ocorrendo uma divergencia de preço entre dois clientes operando sob a mesma tabela de preço, região, plano de pagamento, cobrança, filial, tributação, sem politicas de desconto.

Ambos os clientes são PJ, do mesmo estado e mesma praça.

Verifiquei as tabelas de preço, tributação, politicas, e os cadastros dos dois clientes, porem está ambos sob o mesmo cenário exato e não consegui encontrar motivo para a diferença nos preços.

Login: GUARAVES.Karollyne.Pinto
Clientes: 02934601, 02596801
CODPROD: 62120001
Filial 03
PLPAG: 0012
COB: BOLETO BANCARIO

## Comentarios do Gatekeeper

### 1. 2025-01-22T10:54:41.092-0300 | Filipe do Amaral Padilha

CODCLI 02934601 DE PB
62120001 PVENDA 1.69 CX R$243.12

CODCLI 02596801 DE PB
62120001 PVENDA 1.60 CX R$231.00

Cliente 02934601 possui um acréscimo na tabela MXSACRESCIMOSCLIENTES de 5.263158 e é isso que causa a diferença no valor de venda dos itens entre um e o outro cliente.

Cliente 02596801 não possui acréscimo nessa tabela MXSACRESCIMOSCLIENTES

Para resolver a questão da diferença basta o cliente entender esse acréscimo que estamos recebendo via integração e alterar corretamente nos clientes

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 418302
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que a diferença de preço 'não está relacionada aos demais parâmetros informados no cenário comparado' não está explicitamente suportada pelo texto-fonte. | A recomendação de 'eliminar a divergência de preço' ao ajustar o acréscimo é mais forte do que o texto-fonte, que diz apenas para o cliente entender o acréscimo recebido via integração e alterar corretamente nos clientes. | A seção 'Limitação' afirma que 'Não há detalhamento sobre a origem da integração nem sobre o procedimento técnico exato para alteração desse acréscimo', o que é uma inferência/metacomentário não presente explicitamente no texto-fonte.
