# GATE-841 - Mesmo com o novo cadastro, o cadastro temporário dos clientes não somem

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: SOFTPOOL
- Assunto: MXPED - Cadastro de Cliente - APK
- Natureza: N/A
- Atualizado em: 2025-02-21T13:15:48.341-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar a base do RCA 355 em anexo
>>Ir até a aba clientes

>>Usuário: tozzi.euler
>>Senha: hash

## Resultado apresentado
>>Mesmo ao sincronizar, ou fazer swipe na tela de pedidos e no gerenciar clientes os clientes ficam duplicados.

## Resultado esperado
>>Os clientes temporários deveriam sumir assim que o cadastro permanente fosse aceito pelo ERP.

## Descrição
>>Mesmo com o campo CODFUNCULTALTER da MXSCLIENT preenchido e com os parâmetros HABILITA_PED_CLI_NAO_SINC e HABILITA_PED_CLI_RECEM_CADASTRADO ativos, os cadastros temporários de clientes não somem fazendo com que os clientes fiquem duplicados.

## Comentarios do Gatekeeper

### 1. 2025-02-21T13:14:10.672-0300 | Filipe do Amaral Padilha

Foi feito um paliativo somente para o RCA do ticket codusuario (106237), quando ele sincronizar, os clientes temporários serão deletados da base do aplicativo dele assim ocultando os clientes recém cadastrados.

Eu vou encaminhar o chamado para N3 de qualquer forma, para ser verificado o motivo para mostrar duplicado e esses clientes não estarem sumindo da base após receber o cadastro efetivo na MXSCLIENT.

## Resposta Canonica

Identificou-se que há clientes temporários sendo exibidos em duplicidade e que esses registros não estão sendo removidos da base após o recebimento do cadastro efetivo na `MXSCLIENT`.

Foi aplicado um paliativo exclusivamente para o RCA do ticket, `codusuario 106237`. Após a próxima sincronização desse usuário, os clientes temporários serão deletados da base do aplicativo, o que ocultará os clientes recém-cadastrados.

Como a causa não foi determinada, o chamado deve ser encaminhado ao N3 para:
- verificar o motivo da duplicidade dos clientes;
- verificar por que os clientes temporários não estão sendo removidos da base após o recebimento do cadastro efetivo na `MXSCLIENT`.

Limitação conhecida:
- o paliativo realizado atende somente o RCA `106237`.

## Qualidade

- Flags: requires_attachment_review
- Comentarios primarios: 425829
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
