# GATE-44 - Caso em uma REDE DE CLIENTE, um deles for bloqueado, impedir pedidos na rede toda

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: João Pedro Faria Cabral [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Parametrização
- Natureza: Dúvida
- Atualizado em: 2024-09-12T07:33:19.517-0300

## Contexto do Problema

## Passos para reproduzir
Acesso
CHOCOSUL.RCA

Ao realizar pedidos para o cliente bloqueado, ele permite continuar e emitir um orçamento.

## Descrição
O cliente quer que bloqueie realizar pedidos quando o cliente PRINCIPAL ou algum cliente SECUNDARIO de uma rede de clientes, estiver bloqueado.

Exemplo: Drogasil e uma rede de clientes, codcli 333,334,335,336,337 e 338
se o 334 ta bloqueado, o cliente quer que NENHUM dos outros clientes possam realizar pedidos.

## Comentarios do Gatekeeper

### 1. 2024-09-10T17:07:25.969-0300 | Filipe do Amaral Padilha

A parametrização a seguir vai forçar o sistema a validar cliente bloqueado no código principal e impedir o RCA de confeccionar o pedido.

BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ = S
ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO = N

PERMITE_ORCAMENTO_CLIENTE_BLOQ = N
PERMITE_ORCAR_CLIENT_BLOQ = N

ACEITAVENDAAVISTACLIBLOQ = N

### 2. 2024-09-12T07:29:49.010-0300 | Filipe do Amaral Padilha

Versão analisada 3.248.1 – Porém funciona praticamente em qualquer versão porque a última alteração foi em 2021 nesse fluxo.

Foi possível solucionar o caso sem precisar de correção. Abaixo vou passar os detalhes:

Parametrizações maxPedido:
ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO = N
ACEITAVENDAAVISTACLIBLOQ = N
BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ = S
PERMITE_ORCAMENTO_CLIENTE_BLOQ = S

Parâmetros da 132:
CON_ACEITAVENDABLOQ tanto faz se S ou N
CON_VERIFICARCLIENTESREDE = S (já está)

No cenário verificamos 3 clientes da mesma rede sendo o 2258 o principal:

SELECT CODREDE, CODCLI, CODCLIPRINC, CLIENTE, FANTASIA, BLOQUEIO, BLOQUEIOSEFAZ, BLOQUEIODEFINITIVO, CODUSUR1, CODUSUR2, CODUSUR3
FROM MXSCLIENT WHERE CODCLI in (2258,8922,114809) ORDER BY CODCLIPRINC DESC;

O que ocorre, quando o principal está bloqueado, não é validado o parâmetro ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO de forma a impedir a venda e permitir somente orçamento.

Para barrar quando o principal está bloqueado, o parâmetro BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ entra na atuação.

Então com isso precisamos dos dois parâmetros trabalhando juntos.
BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ e ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO.

Quando pelo Winthor o cliente bloqueia um cliente do RCA, além da MXSCLIENT BLOQUEIO = 'S', é gerada uma tabela com o registro do bloqueio que é a MXSCLIENTESBLOQUEADOS. O maxPedido usa a informação nessa tabela para validar clientes da mesma rede bloqueados, por isso você não conseguiu a validação antes, porque como a gente tá fazendo aqui manualmente, então precisei fazer um insert nessa tabela que citei.

Então quando você tem qualquer outro cliente da rede, que não seja o principal bloqueado, por exemplo, o 114809, o sistema valida o parâmetro ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO, e então ocorre o comportamento que o cliente quer. Nenhum cliente da mesma rede, ligados pelo codcliprinc, podem transmitir pedido enquanto um estiver bloqueado.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, needs_review
- Comentarios primarios: 393820, 394125
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
