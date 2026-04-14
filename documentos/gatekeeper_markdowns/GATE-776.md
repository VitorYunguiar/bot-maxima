# GATE-776 - Acréscimo máximo

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Preço Divergente
- Natureza: Dúvida
- Atualizado em: 2025-02-12T13:26:30.605-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do rca, iniciar o pedido em qualquer cliente, inserir o produto 40455 com um acréscimo maior que 1%, conforme definido na MXSTABPR.

## Resultado apresentado
Ao inserir um acréscimo maior, é verificado que a aplicação não barra o produto de ser inserido.

## Resultado esperado
É esperado que a aplicação valide o acréscimo máximo dos produtos

## Descrição
Cliente deseja trabalhar com acréscimo máximo por produto no maxPedido.
Foi verificado inicialmente por parte do cliente o cadastro de um percentual máximo de acréscimo pela Central de Configurações, em Inteligência de Negócios > Detalhes de produtos. Entretanto, em conversa interna com o gatekeeper, foi verificado que a opção desejada pelo cliente não se aplica em cenários de cliente Winthor.
Dessa forma, foi realizado teste no suporte, onde foi realizada a alteração do campo MXSTABPR.PERACRESCMAX para o produto 40455 via inspect em uma base zero, mas ao simular a inserção do produto com um acréscimo maior que o definido na tabela, a aplicação não recusou a inserção do produto devido ao acréscimo indevido.
Foram verificadas as tabelas MXSUSUARI.PERCACRESFV, MXSCLIENT.PERDESC, MXSATIVI.PERCDESC, o parâmetro ACEITADESCTMKFV na MXSPARAMFILIAL e as políticas de desconto, onde não foram verificados registros que impactassem na simulação realizada.

login para teste:
cetap.3103

## Comentarios do Gatekeeper

### 1. 2025-02-12T13:26:30.602-0300 | Filipe do Amaral Padilha

O maxPedido atualmente está pegando o acréscimo da configuração desse parâmetro CON_PERMAXVENDA que na CETAP está configurado como 9999.

A regra é a seguinte:

a) mxsprodut.peracrescmax (cenário atual está preenchido)
b) mxsusuari.PERCACRESFV (não está preenchido)
c) CON_PERMAXVENDA

Se mxsprodut.peracrescmax e mxsusuari.PERCACRESFV não estiverem zerados, usa o maior percentual, senão usa o CON_PERMAXVENDA.

Como o mxsusuari.PERCACRESFV está nulo então ele pega do parâmetro configurado.

A alteração que faz isso no código é desse ticket -> MXPEDDV-38957

Então para resolver, eles teriam que, ou configurar o mxsusuari.PERCACRESFV do RCA, ou, zerar o parâmetro CON_PERMAXVENDA na Rotina 132.

Se o cliente questionar, não quiser realizar alterações, então ele teria que validar na 316 e nos mostrar o comportamento atual deles na 316, considerando os parâmetros e a forma que está configurado atualmente.

Se existir divergência entre 316 e maxPedido, pode encaminhar para desenvolvimento N3. Mas aqui o caso eu acredito que seja falta de conhecimento sobre essas configurações citadas.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 423378
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Por isso, o produto não é bloqueado ao informar acréscimo superior ao percentual definido no produto."
