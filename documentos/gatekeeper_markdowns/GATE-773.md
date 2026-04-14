# GATE-773 - divergencia de comportamentos entre V3 e V4 - check - in/out fora do raio

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Central de Configurações
- Natureza: Dúvida
- Atualizado em: 2025-02-11T12:44:49.993-0300

## Contexto do Problema

## Passos para reproduzir
login: gd7j.1068
efetuar o login na aplicação, acessar a tela de clientes, buscar pelo primeiro cliente fora de rota que for exibido e tentar iniciar um pedido.

## Resultado apresentado
a V4 gera uma unica solicitação de desbloqueio quando o cliente se encaixa no cenario de ser fora de rota e fora de raio.

## Resultado esperado
o cliente espera que a V4 gere as mesmas requisições de desbloqueio que ele observa acontecer na V3

## Descrição
Senhores, ao analisar e replicar o comportamento citado pela cliente na demanda aqui linkada, estou observando um comportamento onde a V4 não está validando de forma esperada as permissões de "Solicitar autorização para checkin fora do raio" e "Requer autorização para checkout fora do raio do cliente" que estão marcadas no usuário:

!image-2025-02-11-10-25-17-702.png!

Em anexo, há 2 videos que gravei simulando o mesmo fluxo nas duas versões de tentar iniciar um pedido para um cliente fora de rota e fora do raio de check-in/check-out, onde exibem essa diferenças de comportamento. Enquanto a V3 gera 3 requisições de desbloqueio para: visita avulsa, check-in fora do raio e check-out fora do raio, a V4 solicita apenas um desbloqueio.

Esse comportamento é um erro ou o fluxo teve alguma alteração nessas validações devido as alterações de estrutura e de regras de negocio do aplicativo?

## Comentarios do Gatekeeper

### 1. 2025-02-11T12:44:49.992-0300 | Filipe do Amaral Padilha

O comportamento na versão nova realmente foi alterado, a alteração é do ticket:
Resolve: MXPEDDV-81774

Falha: Ao realizar uma visita avulsa, sequenciamento de visitas e cerca eletronica estão sendo validados, dificultando experiência do rca.

Defeito: Pela regra, entende-se que o rca ao realizar uma visita avulsa, não há intenção de validação de raio e sequenciamento de visitas, haja visto que ele deverá realizar conseguir realizar o pedido avulso de onde estiver, e não necessariamente dentro do cliente avulso da rota.

Solução: inserida validação, onde caso haja criação de visita avulsa, este rca não terá necessidade de validar cerca e sequenciamento dentro do processo de checkin, ao terminar o atendimento, deverá continuar com as validações inerentes aos clientes dentro do roteiro.

Nesse caso, a configuração atual deles, que funcionava na versão antiga, não vai mais atender ao cenário.

O que eles poderiam fazer, seria adotar um novo fluxo de trabalho com os parâmetros:

PERIODO_PED_FORA_ROTA = 0 (para validar o dia atual)
QTD_MAX_PED_FORA_ROTA = 1 (A quantidade que o RCA for ter de permissão para pedido fora de rota); --Não pode ser 0, quando é zero não valida esse bloqueio de pedidos para clientes fora de Rota

Ambos parâmetros funcionam por RCA.

Bloquear venda de clientes fora da rota [] desmarcar (assim poderá fazer pedido fora de rota)

A autorização de atender fora de rota nesse caso, pode desmarcar também, porque ela sempre valida junto com a de Bloquear venda de clientes fora de rota, não valida em nenhum outro fluxo de forma avulsa.

Com a configuração que sugeri, a "permissão" de fazer pedido fora de rota será controlada pelo parâmetro QTD_MAX_PED_FORA_ROTA, e nesse fluxo, sempre valida Checkin/Checkout e o Raio do Checkin/Checkout.

Qualquer fluxo diferente desse nas versões novas, pode ser considerado melhoria

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 422983
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "V4" / "V3": o texto-fonte fala em "versão nova" e "versão antiga", mas não identifica essas versões como V4 e V3. | "não caracteriza erro": o texto-fonte diz que o comportamento foi alterado e que fluxos diferentes podem ser considerados melhoria, mas não afirma explicitamente que o caso observado "não caracteriza erro". | "Próximo passo: validar com o cliente a adoção do novo fluxo de trabalho sugerido": isso é recomendação adicional e não está no texto-fonte.
