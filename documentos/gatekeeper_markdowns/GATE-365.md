# GATE-365 - Vendedor está conseguindo passar mais pedidos fora de rota do que está definido no parâmetro QTD_MAX_PED_FORA_ROTA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor Cloud
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: Dúvida
- Atualizado em: 2024-11-22T18:01:44.282-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Iniciar um pedido em qualquer cliente fora de rota gerando uma visita avulsa
>>E assim não retorna a mensagem que só pode realizar 6 pedidos fora de rota.

Então acredito que como ele gera visita avulsa para os cliente fora de rota não está contabilizando como pedido fora de rota, e o cliente quer que bloqueio somente 6 pedidos fora de rota mesmo gerando uma visita avulsa no cliente fora de rota.

Login: jfrios.amauri
senha: acesso temporário

## Resultado apresentado
Vendedor conseguindo realizar mais pedidos fora de rota do que está definido no parâmetro QTD_MAX_PED_FORA_ROTA.

## Resultado esperado
Que o vendedor consiga realizar somente os 6 pedidos fora de rota definidos no parâmetro QTD_MAX_PED_FORA_ROTA, mesmo que seja gerando uma visita avulsa.

## Descrição
O vendedor com codusur 229 conseguiu passar 8 pedidos fora de rota, mesmo estando definido no parâmetro QTD_MAX_PED_FORA_ROTA que é possível passar somente 6 pedidos fora de rota.

Os pedidos foram nos clientes 28322,27627,27646,27203,8086,28138,28610,20434, e nenhum desses clientes constam no roteiro do dia 20/11 na ERP_MXSROTACLI, e na MXSCOMPROMISSOS.

Mais vemos que na MXSINTEGRACAOPEDIDO tem os pedidos com ID_PEDIDO 28322,27627,27646,27203,8086,28138,28610,20434 que foram realizados nesses clientes fora de rota no dia 20/11.

Para a tabela MXSPEDIDOFORAROTA subiu somente 5 pedidos constando como fora de rota, mais na realidade esse vendedor realizou 8 pedidos para clientes fora de rota.
Pedidos que constam na MXSPEDIDOFORAROTA são os pedidos com ID_PEDIDO: 345685, 345688, 345804, 345806 e 345910.

Identifiquei que só retorna a mensagem que pode realizar 6 pedidos fora de rota nos clientes que não fazem parte do roteiro do dia se arrastar para o lado iniciando um pedido, se gerar uma visita avulsa parece não fazer a contagem como fora de rota.

Link com a base do RCA devido o tamanho precisei subir no drive: https://drive.google.com/file/d/1IBSt4Cr97elsJJxEiayQAHmVNQZoBZ_V/view?usp=sharing

## Comentarios do Gatekeeper

### 1. 2024-11-22T18:01:44.280-0300 | Filipe do Amaral Padilha

Referente ao fluxo que você mesma identificou:

"Então acredito que como ele gera visita avulsa para os cliente fora de rota não está contabilizando como pedido fora de rota, e o cliente quer que bloqueio somente 6 pedidos fora de rota mesmo gerando uma visita avulsa no cliente fora de rota."

É exatamente assim que funciona atualmente, quando o RCA faz uma manda gerar uma visita avulsa, ele inclui esse cliente no roteiro, e como ele inclui no roteiro, não conta como pedido fora de rota, e por isso não cai no contador do parâmetro 'QTD_MAX_PED_FORA_ROTA';

Esse é o comportamento atual da aplicação mesmo, para trabalhar de uma forma diferente, eles teriam duas opções que eu pensei:

1° Seria uma melhoria para contar a "visita avulsa" que entra para o roteiro como fora de rota; Não sei se faz muito sentido, mas teria que criar uma regra difernte ai específica;

2° eles poderiam tirar a permissão de gerar visita avulsa e trabalhar só com o roteiro e com os atendimentos fora de rota pela listagem geral, assim sempre entraria para o contador do parâmetro QTD_MAX_PED_FORA_ROTA. Assim para mim faz mais sentido deles trabalharem, mas dai teria que fazer o repasse para entender com eles se seria viável.

## Resposta Canonica

**Conclusão canônica**

O comportamento reportado procede e está aderente à lógica atual da aplicação: quando o RCA gera uma **visita avulsa**, esse cliente passa a ser **incluído no roteiro**. Por esse motivo, o atendimento **não é tratado como pedido fora de rota** e **não entra na contagem** do parâmetro **QTD_MAX_PED_FORA_ROTA**.

Assim, o limite definido em **QTD_MAX_PED_FORA_ROTA** é aplicado apenas aos atendimentos que permanecem efetivamente como **fora de rota**. Se o pedido for iniciado a partir de uma visita avulsa, ele deixa de se enquadrar nessa condição para fins de contagem.

**Causa**
- Visita avulsa inclui o cliente no roteiro.
- Cliente incluído no roteiro não é contabilizado como fora de rota.
- Consequentemente, o pedido não incrementa o contador do parâmetro **QTD_MAX_PED_FORA_ROTA**.

**Limitação atual**
- Esse é o comportamento atual da aplicação.
- Para que uma visita avulsa também seja contada como fora de rota, seria necessária uma **regra específica** de negócio.

**Ação recomendada**
- Avaliar uma melhoria para que visita avulsa incluída no roteiro também seja contada como fora de rota.
- Como alternativa operacional, avaliar com o cliente a remoção da permissão de **gerar visita avulsa**, trabalhando apenas com o roteiro e com os atendimentos fora de rota pela listagem geral.

**Próximo passo**
- Realizar o repasse para validar com o cliente se é viável retirar a permissão de visita avulsa ou se será necessária uma customização/regra específica para atender esse cenário.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 408313
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
