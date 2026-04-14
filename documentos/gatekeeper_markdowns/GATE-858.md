# GATE-858 - Clientes duplicados no banco nuvem

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - Banco de Dados
- Natureza: Dúvida
- Atualizado em: 2025-02-25T12:12:29.131-0300

## Contexto do Problema

## Passos para reproduzir
Bom dia,

Estou com uma situação que, alguns clientes da 969 - SUPERELIZEU estão com registros "duplicados" na MXSCLIENT, exemplo os clientes 77892, 77893, 78002, 78003.

Verifiquei no banco do Winthor que esses registros duplicados na nuvem não existem no banco local, no caso no banco local existem somente os clientes 77892 e 78002 dos 4 citados.

Ao conversar com o cliente o mesmo informou que recentemente foi realizada uma migração vindo do Pedido de Vendas para o maxPedido, o que pode ter sido o causador da duplicidade desses registros.

Segundo o cliente, o problema afeta outros RCAs.

>>>
>>ELIZEU.claudioaraujo
>Acessar APK (base do zero)
>Clientes
>Observar os clientes que possuem registros duplicados (ex: 77892, 77893, 78002, 78003)

## Resultado apresentado
Alguns clientes estão com registros "duplicados" na MXSCLIENT, exemplo os clientes 77892, 77893, 78002, 78003.

## Resultado esperado
Normalizar os registros.

## Comentarios do Gatekeeper

### 1. 2025-02-25T12:12:29.130-0300 | Filipe do Amaral Padilha

Foi feita normalização dos dados da tabela MXSCLIENT, durante o processo eu normalizei 190 de cadastros duplicados de clientes;

A normalização consiste em igualar as informações com o banco do Winthor PCCLIENT = MXSCLIENT. E a integração está funcionando normalmente.

Para os RCAs receberem a correção nos dispositivos, basta realizar a sincronização do maxPedido

## Resposta Canonica

Foi realizada a normalização dos dados da tabela **MXSCLIENT**, com correção de **190 cadastros duplicados de clientes**.

A análise consistiu em **igualar as informações da MXSCLIENT com o banco Winthor**, considerando a correspondência **PCCLIENT = MXSCLIENT**. Após o ajuste, a **integração está funcionando normalmente**.

**Ação necessária:** realizar a **sincronização do maxPedido nos dispositivos dos RCAs**, para que a correção seja aplicada e os dados atualizados sejam recebidos.

## Qualidade

- Flags: missing_context_sections
- Comentarios primarios: 426437
- Secoes ausentes: Descrição
- Groundedness aprovado: sim
