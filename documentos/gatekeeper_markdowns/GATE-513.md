# GATE-513 - Autorização de desconto rotina 301

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Autorização de Preço
- Natureza: Dúvida
- Atualizado em: 2024-12-17T09:20:08.578-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Importar a base anexada
>>Ir na tela de pedidos
>>Ir no pedido 304055816 e editar esse pedido
>>Ir na aba de itens e clicar para acessar a tela de negociação do item 24053
>>Clicar em mais informações --> Políticas comerciais
>>E assim irá ver que não carregou a autorização com número 1582906, onde a partir de 12 unidades o RCA pode conceder 16% de desconto
>>Ainda no mesmo pedido, remover do pedido o item 24053
>>Ir na aba tabela e adicionar novamente o item 24053
>>Na tela de negociação informar a quantidade de 12 unidades e conceder um desconto de 16% e assim não deixa adicionar o item com esse desconto.

Se iniciar um pedido do zero irá conseguir aplicar o desconto de 16 normalmente, basta realizar o teste no cliente 114153 e plano de pagamento 5, colocando 12 unidades do item 24053 permite aplicar o desconto.

Login: megabrasil.304
senha: acesso temporário

## Resultado apresentado
Em pedidos que já estão salvos e bloqueado não carrega a informação da autorização de preço, mesmo removendo o item do pedido e adicionando novamente.

## Resultado esperado
Que nos pedidos que já estão salvos e bloqueados carregue a informação da autorização de preço, sem que precise do RCA ter que duplicar um pedido que está salvo e bloqueado ou precise iniciar um pedido do zero novamente.

## Descrição
O cliente trabalha da seguinte forma, ele autoriza alguns descontos pela rotina 301 e com isso os vendedores sincronizam para obter aquela autorização e conseguir aplicar o desconto no MaxPedido, esse fluxo funciona corretamente em cenários que inicia um pedido do zero, mas acontece que no cenário onde o pedido já está salvo e bloqueado no aparelho do RCA para envio ao ERP mesmo sincronizando o MaxPedido no pedido não consta a autorização de preço com isso não deixa o RCA adicionar o item com o desconto autorizado na 301, mesmo excluindo o item do pedido e adicionando novamente, para funcionar precisa duplicar o pedido que está salvo e bloqueado.

Gostaria de entender se é o comportamento correto

## Comentarios do Gatekeeper

### 1. 2024-12-17T09:20:08.577-0300 | Filipe do Amaral Padilha

Será enviado para N3, esse comportamento está errado, foi alinhado com o P.O e ocorre em versão ponta.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 412583
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'a autorização de preço deveria ser considerada também em pedidos já salvos e bloqueados' não consta no texto-fonte. | 'necessidade de análise técnica mais aprofundada' não consta no texto-fonte. | 'N3 é responsável pela investigação deste comportamento incorreto' não consta no texto-fonte.
