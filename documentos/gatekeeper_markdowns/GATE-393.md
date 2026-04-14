# GATE-393 - Verificar motivo do extrator Tcloud ter caído

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Extrator
- Natureza: Dúvida
- Atualizado em: 2024-11-27T11:11:08.388-0300

## Contexto do Problema

## Passos para reproduzir
>>Verificar no banco nuvem os LOGS do pedido ID_PEDIDO 5706
>>Verificar nos Logs do grafana durante este período

## Resultado apresentado
>>O pedido demorou 38 min para ser integrado
>>Nos Logs do grafana o extrator apresentou erros durante este tempo

## Resultado esperado
>>O extrator não deveria cair novamente.

## Descrição
>>O cliente reclamou de demora na integração de pedidos

>>Verificado juntamente ao gate Filipe nos LOGS do grafana que o extrator ficou Ofline durante as 14:17 e 14:57 de hoje 26/11

>>Subindo gate para que seja verificado o motivo do extrator ter ficado ofline

## Comentarios do Gatekeeper

### 1. 2024-11-27T11:11:08.385-0300 | Filipe do Amaral Padilha

Não passar para o cliente: {

Foram verificados os logs do Extrator e foi constatado que de fato houve uma instabilidade que ocasionou a paralisação da integração com o força de vendas do cliente entre 14:19 e 14:56 do dia 26/11/2024.

Segundo o pessoal mais experiente do desenvolvimento backend essa é uma verificação que precisa ser feita em parceria com a TECH, porque até então não há indícios de problemas no código do Extrator ou das aplicações backend do maxPedido, que poderiam ocasionar o problema.

Então eu conversei com o Pedro Bernardes, que é da TECH e ele informou que o "Healthcheck estava habilitado e funcionando, ele disse que teve vários logs e que precisaria entender melhor o log, porém era muito conteúdo para analisar.

Então dito isso, não tem o que o pessoal do maxpedido backend analisar, teria de ser com a TECH, mas ele me fez um pedido, que se acontecer novamente a mesma situação, a gente analisar na hora do problema, para que assim possa seguir o fluxo >> Gate e depois acionar a TECH;

}

Para o cliente: Você pode dizer basicamente que houve uma instabilidade, que nossos mecanismos automaticamente corrigiram esse problema e por isso voltou a funcionar depois de um tempo sozinho. Porém que vamos continuar acompanhando e caso ocorra novamente algum caso de demora assim na integração ele pode por favor nos informar via ticket que a gente gostaria de tentar analisar o problema acontecendo em tempo real. No momento ele não precisa se preocupar porque está em funcionamento e estável.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 408967
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "período compatível com a demora relatada na integração do pedido" — o texto-fonte não menciona 'pedido' nem afirma compatibilidade com uma demora relatada específica. | "Houve grande volume de logs, o que limita uma conclusão mais precisa sobre a origem da instabilidade apenas com a massa já disponível." — o texto-fonte diz que a TECH informou que havia vários logs e que precisaria entender melhor o log, mas não afirma explicitamente essa limitação/conclusão nessa formulação. | "Manter o acompanhamento do caso em parceria com a TECH." — o texto-fonte diz que a verificação precisa ser feita em parceria com a TECH e que, se ocorrer novamente, seguir o fluxo e acionar a TECH, mas não afirma explicitamente esse próximo passo contínuo de acompanhamento do caso nessa redação.
