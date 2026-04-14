# GATE-617 - Restrições não sendo validadas

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXPED - Restrições
- Natureza: Dúvida
- Atualizado em: 2025-01-10T15:08:53.745-0300

## Contexto do Problema

## Passos para reproduzir
>>gsa.422
>Acessar APK
>Importar base
>Observar o pedido 64220005
>Observar valor do pedido
>Consultar restrição 3648 da MXSRESTRICAOVENDA
>Tentar fazer o mesmo pedido em uma base do zero

## Resultado apresentado
Alguns RCAs estão conseguindo enviar pedidos com valores abaixo do limite definido na restrição de R$300.

Não consegui simular esse problema na base do RCA devido o limite de credito vencido do cliente do problema.

## Resultado esperado
Entender como isso aconteceu.

## Descrição
Bom dia, Carlos e Filipe,

Preciso de ajuda para entender uma situação que está ocorrendo na GSA e verificar se pode se tratar de um erro.

O time de TI da empresa me informou que alguns RCAs estão conseguindo enviar pedidos com valores abaixo do limite definido na restrição de R$300. No entanto, ao tentar reproduzir o cenário em uma base do zero, não consegui replicar o comportamento. No meu teste, o sistema bloqueou o envio do pedido no final, apresentando a mensagem correspondente à restrição que impedia o processamento.

Gostaria de entender como alguns RCAs estão conseguindo superar essa limitação e, se possível, identificar a causa do problema.

## Comentarios do Gatekeeper

### 1. 2025-01-10T15:08:53.743-0300 | Filipe do Amaral Padilha

No momento, é conforme foi descrito no ticket, não é possível simular o problema, porém através de logs dos jsons dos pedidos foi possível identificar a causa:

Nos pedidos 64220005 e 64220007 o número da região no objeto está = 0, então provavelmente quando o RCA fez o pedido ocorreu algum problema com a região do cliente, porque se estivesse na mesma região da restrição cadastrada, teria barrado no valor de R$300.

Em pedidos mais recentes que verifiquei, todos estão vindo com o número da região. Se voltar a ocorrer, eu oriento a pegar a base já na mesma hora, identificou que o pedido saiu errado, já pedir para o RCA mandar a base do maxPedido, porque nesses casos, teria de ter um cenário com o problema ocorrendo para debugar e identificar o motivo da região não gravar no JSON do pedido.

Caso ocorra também com muita frequência e esteja impactando, mesmo sem cenário podemos tentar enviar para o nosso desenvolvimento pensar numa forma de rastrear o problema.

## Resposta Canonica

**Conclusão canônica**

A análise dos pedidos **64220005** e **64220007** indica que o problema ocorreu porque o **número da região no objeto do pedido estava igual a 0** no momento do envio. Com isso, há forte indicativo de que houve um problema na informação de **região do cliente** quando o RCA gerou o pedido.

Nessa condição, a **restrição de valor mínimo de R$300** não foi aplicada como seria esperado. Se o pedido estivesse com a mesma região da restrição cadastrada, ele teria sido barrado pelo limite.

**Evidências analisadas**
- Não foi possível simular o problema no momento.
- A identificação da causa foi feita pela análise textual dos logs dos objetos dos pedidos.
- Nos pedidos **64220005** e **64220007**, o campo de **região** estava com valor **0**.
- Em pedidos mais recentes verificados, o número da região está sendo gravado normalmente.

**Limitação atual**
- Sem um cenário ativo com o problema ocorrendo, não é possível debugar e determinar por que a região deixou de ser gravada no objeto do pedido.

**Ação recomendada**
- Se o problema voltar a ocorrer, coletar imediatamente a **base do maxPedido** do RCA no momento do erro.
- Solicitar ao RCA o envio dessa base assim que identificar que o pedido saiu incorretamente.
- Com o cenário ativo, realizar o debug para identificar por que a região não está sendo gravada no pedido.
- Se a recorrência aumentar e houver impacto operacional, encaminhar para o desenvolvimento avaliar uma forma de rastreamento do problema.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 416274
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
