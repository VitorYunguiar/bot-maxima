# GATE-783 - Não permite transferir o saldo de conta corrente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXGESN - Conta Corrente - Transferência de Saldo
- Natureza: N/A
- Atualizado em: 2025-02-13T08:34:11.172-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o MaxGestão
>>Ir na parte de transferir o saldo de conta corrente
>>Tentar transferir o saldo de qualquer vendedor
>>E assim irá ver que não deixa transferir e retorna erro.

Login: vandal.vanderlei
Senha:   V/v4ndin

## Resultado apresentado
Não permite transferir saldo de conta corrente

## Resultado esperado
Que permita transferir o saldo de conta corrente

## Descrição
Não está permitindo transferir o saldo de conta corrente tanto no PWA quanto no web.

## Comentarios do Gatekeeper

### 1. 2025-02-13T08:34:11.169-0300 | Filipe do Amaral Padilha

Identificado que o extrator do cliente estava apontando para a API antiga, por esse motivo não ocorria a movimentação de conta corrente.

Então foi feita alteração no Extrator do cliente para a API intpdv-unificado e após isso, realizados os testes e a tranferência voltou a funcionar com sucesso.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 423602
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma especificamente 'transferência de saldo de conta corrente', mas o texto-fonte menciona apenas 'movimentação de conta corrente' e depois 'a transferência voltou a funcionar', sem citar 'saldo'. | 'Ação recomendada: Alterar o extrator do cliente para a API intpdv-unificado.' é apresentada como recomendação, mas o texto-fonte descreve isso como ação já realizada, não como recomendação. | 'Responsável: Extrator do cliente.' não está explicitamente informado no texto-fonte. | 'Próximo passo: Validar que o extrator do cliente permaneça apontando para a API intpdv-unificado e confirmar o funcionamento da transferência de conta corrente.' não consta no texto-fonte.
