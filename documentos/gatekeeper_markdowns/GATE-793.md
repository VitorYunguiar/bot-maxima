# GATE-793 - Pedidos salvo e bloqueado entrando no fluxo da API de cancelamento no momento de editar

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor Cloud
- Assunto: MXPED - Pedido/Orçamento - Editar
- Natureza: Dúvida
- Atualizado em: 2025-02-14T11:09:41.059-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Iniciar um pedido em qualquer cliente
>>Salvar e bloquear pedido
>>Ir na tela de pedidos
>>Editar o pedido que está salvo e bloqueado
>>Salvar e enviar o pedido
>>E assim irá ver que ao enviar o pedido retorna uma crítica informando que não foi possível autenticar na API de cancelamento do winthor

Login: jfrios.markes
senha: acesso temporário

## Resultado apresentado
Pedido salvo e bloqueado ao ser editado está entrando no fluxo da API de cancelamento do winthor.

## Resultado esperado
Que o pedido salvo e bloqueado ao ser editado não entre no fluxo da API de cancelamento

## Descrição
Pedidos que estão salvos e bloqueados ao editar está entrando no fluxo da API de cancelamento. Se o pedido está salvo e bloqueado e ele for editado não deveria entrar no fluxo da API de cancelamento.

## Comentarios do Gatekeeper

### 1. 2025-02-14T10:53:07.065-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 porque está induzindo o usuário ao erro. O comportamento correto seria ao editar um pedido salvo e bloqueado, se o usuário salvar e enviar o pedido, ele entra em fluxo normal de envio, sem passar pelo WTA.

Só deve entrar em fluxo de WTA caso o pedido já esteja salvo e enviado e respeitando demais regras (não pode editar/cancelar pedido faturado ou montado)

## Resposta Canonica

**Conclusão canônica**

Identificado comportamento incorreto no fluxo de edição de pedido **salvo e bloqueado**. Ao editar esse pedido e executar **Salvar e Enviar**, o sistema está direcionando indevidamente para fluxo relacionado ao **WTA**, quando o esperado é seguir o **fluxo normal de envio**.

**Regra correta identificada**
- Pedido **salvo e bloqueado**, ao ser editado e posteriormente **salvo e enviado**, **não deve** entrar no fluxo de WTA.
- O fluxo de **WTA** deve ocorrer **somente** quando o pedido já estiver **salvo e enviado**.
- Devem continuar sendo respeitadas as regras existentes:
  - **não pode editar/cancelar pedido faturado**
  - **não pode editar/cancelar pedido montado**

**Causa**
O comportamento atual está induzindo o usuário ao erro, pois um pedido salvo e bloqueado está sendo tratado por um fluxo incorreto relacionado ao WTA, em vez de seguir o envio normal.

**Ação recomendada**
Encaminhar para **N3**.

**Próximo passo**
Tratamento do comportamento incorreto pelo **N3**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 424044
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
