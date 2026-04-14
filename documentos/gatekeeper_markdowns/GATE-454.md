# GATE-454 - Conta Corrente está com o saldo negativo.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Conta Corrente
- Natureza: Dúvida
- Atualizado em: 2024-12-05T08:40:03.591-0300

## Contexto do Problema

## Passos para reproduzir
Login: megamix.matheus (codUsur: 3)
1 - Abrir o maxPedido
2 - Ver a CC negativa

## Resultado apresentado
CC ao invés de estar zerada, está com saldo negativo

## Resultado esperado
CC com o valor padrão correto.

## Descrição
O cliente relata que está com o saldo da conta corrente negativo, mesmo depois de atualizar a versão do aplicativo.

## Comentarios do Gatekeeper

### 1. 2024-12-05T08:40:03.587-0300 | Filipe do Amaral Padilha

Se você importar a base do RCA, como ele tem pedidos na base, que transmitiu e que consumiram conta corrente, então o parâmetro DESCONTA_SALDOCCRCA_OFFLINE da MXSPARAMETRO faz o cálculo somente a nível de maxPedido para exibir para o RCA já uma prévia da conta corrente que ele movimentou.

Esse parâmetro causa propositalmente divergência das informações do ERP e dos endpoints MXSSALDOCCRCA e MXSUSUARI.

Então para resolver, será necessário entender com o cliente se ele quer trabalhar com conta corrente nesse RCA. Se ele quiser trabalhar então esteja ciente que esse parâmetro DESCONTA_SALDOCCRCA_OFFLINE realmente gera esse comportamento, para reter o saldo de conta corrente conforme o RCA já for negociando usando o maxPedido.

Ele pode usar conta corrente, mas não trabalhar com o DESCONTA_SALDOCCRCA_OFFLINE, o caso, é que se ele estiver ativo, como expliquei o cálculo já ocorre conforme o RCA negocia os pedidos no maxPedido. Então se ele usar conta corrente, porém o parâmetro DESCONTA_SALDOCCRCA_OFFLINE = N; O maxPedido vai fazer a leitura do MXSSALDOCCRCA.

Se ele não quiser trabalhar com o Conta Corrente e quiser que fique totalmente zerado, então teria que desativar esse parâmetro DESCONTA_SALDOCCRCA_OFFLINE.

Na base do zero, como não tem nenhum pedido ainda transmitido, que alimente a tabela mxspedido (salvou ou bloqueado, ou salvo e enviado) então o conta corrente fica R$0,0.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410448
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "o que pode resultar em saldo negativo"
