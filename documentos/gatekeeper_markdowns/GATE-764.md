# GATE-764 - Locks no banco local do cliente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Banco de Dados
- Natureza: Dúvida
- Atualizado em: 2025-02-07T13:01:02.124-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o banco local do cliente ou a rotina 551 - Lock de banco
>>Verificar a fila de processos

## Resultado apresentado
>>Os processos do maxSolucoes estão todos funcionando, porém existem LOCKs no banco que não são causados pelo maxSolucoes.

## Resultado esperado
>>Os locks do banco do cliente deveriam deixar de ocorrer, mas isso independe de nós.

## Descrição
>>O cliente entrou em contato dizendo que nossas aplicações estavam gerando muitos processos e que isso estaria travando o Winthor deles

>>Ao verificar notamos que na verdade não era nossa aplicação que estava causando o LOCK, porém como consequencia do LOCK de outra aplicações nossos procesos ficavam travados na fila.

>>Passamos para que o DBA criasse

## Comentarios do Gatekeeper

### 1. 2025-02-07T13:00:30.507-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 porque o desenvolvimento identificou a necessidade de melhorar o script que faz a apuração dos limites de créditos dos clientes no banco do Winthor

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 422362
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificação técnica apontou que a causa do comportamento observado está na necessidade de melhorar o script..." — o texto-fonte não menciona "causa do comportamento observado" nem "identificação técnica". | "Ação recomendada - Realizar a melhoria do script..." — o texto-fonte informa a necessidade de melhorar e o encaminhamento para N3, mas não explicita essa ação como recomendação formal. | "Responsável - N3." — o texto-fonte diz que será encaminhado para N3, mas não afirma que N3 é o responsável.
