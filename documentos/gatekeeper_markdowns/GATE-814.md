# GATE-814 - alteração de data final de campanhas de desconto escalonado

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Campanha - MQT/SQP/MIQ
- Natureza: Dúvida
- Atualizado em: 2025-02-18T09:57:19.636-0300

## Contexto do Problema

## Passos para reproduzir
Conforme descrição

## Resultado apresentado
o cliente tentou alterar a data final das campanhas de desconto escalonado para uma data menor da data atual, mas a central não permite essa ação

## Resultado esperado
ele espera que seja efetuada a alteração dessa data via banco.

## Descrição
Segue solicitação do cliente:

"Preciso que todos os DESCONTOS ESCALONADOS, com vigência ou data final que estão até 31/12/2025, fiquem com a data final igual a 17/02/2025.
Hoje iniciamos novas escalonadas que estão com vigência de hoje, 18/03/2025 até 03/03/2025 e estas devem ser mantidas.
O motivo desta solicitação é para não gerar conflitos nos descontos escalonados."

!image-2025-02-18-08-53-23-104.png!

!image-2025-02-18-08-53-51-887.png!

Com base nisso, o cliente solicita que seja realizada alteração manual em banco, alterando as campanhas de desconto escalonada que tem uma data final de 31/12/2025 para a data de 17/02/2025. O mesmo precisa manter essas campanhas na base, mas que tenham uma data final menor que a data atual e essa operação a central não permite a execução.

## Comentarios do Gatekeeper

### 1. 2025-02-18T09:33:03.318-0300 | Filipe do Amaral Padilha

Foi feita a inativação por data de vigência das campanhas seguindo esse critério para o UPDATE:

SELECT * FROM MXSDESCESCALONADOC WHERE TRUNC(DTFIM) = TO_DATE('17/02/2025','DD/MM/YYYY');

Assim as campanhas deixam de ser enviadas para o maxPedido pois uma job nossa lê as vigências e atualiza o campo enviafv para = 'N'.

Para validar os RCAs devem estar sincronizando o maxPedido.

Se o cliente quiser alguma alteração da regra de negócios do sistema, se encaixa em cenário de melhoria

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 424692
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "a Central não permite manter campanhas com data final menor que a data atual" | "O parâmetro aplicado foi `DTFIM = 17/02/2025`"
