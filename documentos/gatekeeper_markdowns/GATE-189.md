# GATE-189 - Mesmo cumprindo o roteiro do dia anterior, está pedindo desbloqueio no outro dia

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: Dúvida
- Atualizado em: 2024-10-16T17:00:54.055-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Importar a base anexada
>>Tentar iniciar um pedido em qualquer cliente do roteiro de hoje dia 16/10
>>E assim retorna a mensagem informando que não cumpriu todo o roteiro do dia anterior

Login: ORCA.iago
senha: acesso temporário

## Resultado apresentado
Mesmo que o RCA tenha concluído todo o roteiro do dia anterior, ao iniciar o roteiro no dia atual, é solicitado o desbloqueio, informando que o roteiro do dia anterior não foi cumprido.

## Resultado esperado
Que quando o RCA tenha cumprido todo o roteiro do dia anterior, não fique bloqueando de iniciar o pedido no roteiro atual.

## Descrição
Conforme alinhado via Discord com o Filipe, esse é um assunto recorrente com o cliente. Eles utilizam um parâmetro que bloqueia a rota do dia seguinte caso o roteiro do dia anterior não tenha sido concluído. No entanto, o cliente continua abrindo diversos tickets informando que, mesmo o RCA cumprindo todo o roteiro do dia, a rota do dia seguinte ainda é bloqueada.

Essa questão já foi encaminhada para o desenvolvimento e tratada no ticket MXPEDDV-80135, no qual foi habilitado o parâmetro PERMITIR_DELETE_HISTORICOCOMP, mas a situação ainda persiste.

Na análise realizada, foi verificado que o RCA cumpriu todo o roteiro no dia 15/10. No entanto, hoje (16/10), foi solicitada a liberação da rota, pois o sistema bloqueou o acesso, alegando que o roteiro do dia anterior não foi cumprido.

O roteiro de visitas criado pelo roteirizador de vendedores incluía 17 clientes. No sistema ERP_MXSVISITAFV, constam 16 visitas realizadas e 3 pedidos integrados em clientes dentro do roteiro. Além disso, o relatório extraído do painel de auditoria do sistema de gestão também confirma que o RCA completou todas as visitas planejadas para o dia 15/10.

## Comentarios do Gatekeeper

### 1. 2024-10-16T16:58:51.005-0300 | Filipe do Amaral Padilha

Para o cliente você pode dizer que foi feita somente uma normalização dos registros, de forma que ajustamos os compromissos para validar corretamente de agora em diante quando o RCA cumprir todo o roteiro não ficar apresentando no aplicativo como se não tivesse cumprido.

*Não passar ao cliente detalhes abaixo, vou explicar só para você entender o que houve e ficar registrado:*

Basicamente o registro no banco nuvem da MXSHISTORICOCOMPROMISSOS foi deletado com codoperacao = 2, porém essa deleção não chegou via sincronismo para o RCA. E então na base do RCA haviam registros não deletados de forma incorreta.

Alguns dos registros que eu analisei eram por exemplo, dos dias 15,16 e 17 de Outubro de 2024, e eles foram apagados no dia 27/09/2024. Então no dia 30/09/2024 quando o RCA fez o primeiro sincronismo eles deveriam ter descido, mas não desceram deletando e o motivo não temos mais como saber porque essa evidência se perdeu a nível de desenvolvimento.

A gente guarda até 10 dias desse registro de sincronizações de informações que descem, então como era para ter descido no dia 30/09, já não temos mais a evidências do problema em si para analisar.

Para resolver então eu fiz uma carga reenviando os registros de compromissos deletados para todos os RCAs do cliente, então conforme eles sincronizarem vai normalizar as bases. Amanhã, por exemplo, não vai ocorrer o problema e daqui em diante não é para ocorrer mais teoricamente. Porém se tiver algum caso, o procedimento é o mesmo, analisar se cumpriu a rota anterir e pegar a base do maxPedido para analisarmos.

### 2. 2024-10-16T17:00:54.055-0300 | Filipe do Amaral Padilha

--Eu testei essa solução sicronizando e vai resolver o caso deles, hoje mesmo se ele quiser testar já vai dar certo depois de sincronizar.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 401217
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "a causa do bloqueio" | "resultou no bloqueio incorreto da rota seguinte"
