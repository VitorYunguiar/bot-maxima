# GATE-708 - Painel de auditoria-Tempo de atendimento incorreto.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Dados Incorretos
- Natureza: Dúvida
- Atualizado em: 2025-01-29T09:49:03.645-0300

## Contexto do Problema

## Passos para reproduzir
>> Usuário: meggadist.510
>> Ir no maxGestão, painel de auditoria, realizar pesquisa, filial 2, supervisor Douglas, RCA Gledson., dia 27/01 a 27/01
>> Verificar tempo de atendimento

## Resultado apresentado
>> Tempo de atendimento de quase todos clientes esta de 10 minutos

## Resultado esperado
>> Que seja mostrado o tempo correto de atendimento

## Descrição
Ao pesquisa no painel de auditoria RCA GLESON no dia 27/01, é informado que em quase todos os clientes o atendimento foi de 10 minutos.

## Comentarios do Gatekeeper

### 1. 2025-01-29T09:49:03.642-0300 | Filipe do Amaral Padilha

Foi analisado a base maxTracking do RCA e constatado que foram gravados os eventos com diferença de 10 minutos.

Eu enviei para desenvolvimento para verificarem se estou correto na minha análise:

A princípio o problema é gerado por uma versão antiga do maxPedido. Para resolver essa questão do tempo registrado nos eventos, recomendo atualizar a versão do maxPedido e habilitar o parâmetro BLOQUEAR_UTILIZACAO_BATERIA_OTIMIZADA que garante uma apuração mais precisa das informações de rastro.

Mesmo atualizando a versõa, os dados retroativos não serão resolvidos, após atualizar esperamos que os novos registros não fiquem assim inconsistentes.

Os dados retroativos não tem mais como serem corrigidos.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 419824
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A inconsistência no tempo de atendimento exibido no painel de auditoria para o RCA informado, no dia 27/01, está associada inicialmente a uma versão antiga do maxPedido. | No painel de auditoria, em quase todos os clientes, o atendimento foi apresentado como 10 minutos na pesquisa realizada para o RCA citado. | Na base maxTracking do RCA, foi constatado que os eventos foram gravados com diferença de 10 minutos, o que explica o valor apresentado na tela. | Após isso, atualizar o maxPedido e habilitar o parâmetro para evitar inconsistências em novos registros.
