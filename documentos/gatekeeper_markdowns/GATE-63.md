# GATE-63 - Bloquear pedido acima do limite

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Parametrização
- Natureza: Dúvida
- Atualizado em: 2024-09-16T16:52:16.018-0300

## Contexto do Problema

## Passos para reproduzir
Alterar os parâmetros na base da APK e verificar se o pedido é impedido de ser enviado.

## Resultado apresentado
Pedido é enviado normalmente.

## Resultado esperado
APK impedindo RCA de salvar e enviar o pedido caso o limite do cliente seja menor do que o valor total do pedido.

## Descrição
Cliente deseja impedir o RCA de salvar pedido que tem valor acima do limite de crédito do cliente. Foi criado o parâmetro BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE e feito as alterações informadas na tela de parametros. Tambem foi criado o parâmetro PERMITI_VENDA_AVISTA_SEMLIMITE, porem o pedido segue sendo enviado normalmente. Abaixo os parâmetros utilizados.

BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE = S
CON_ACEITAVENDABLOQ = N
BLOQPEDLIMCRED = N
PERMITI_VENDA_AVISTA_SEMLIMITE = N

CODCLI = 26658
Login: pcm.ronaldo

## Comentarios do Gatekeeper

### 1. 2024-09-16T16:52:16.016-0300 | Filipe do Amaral Padilha

Compreendi que o cliente gostaria que não deixasse nem salvar o pedido caso o limite de crédito fosse excedido e a cobrança utilizada fosse DH com plano de pagamento A VISTA.

Verificando o comportamento do código atualmente, para cliente Winthor, que é o caso da PCM, sempre vai deixar salvar e bloquear ou salvar e enviar o pedido.

Por padrão o parâmetro PEFRMITI_VENDA_AVISTA_SEMLIMITE vem = Não; E ele sempre entra no fluxo de validar o limite do cliente e passar a mensagem: "Cliente sem limite de crédito. Esse pedido será salvo mas poderá não ser processado no ERP."

Conclusão, não tem configuração atualmente, para impedir o RCA de salvar o pedido. Pelo menos eu não consegui rastrear e fiz vários testes e leitura das configurações.

Tem um caminho para seguir, existe uma configuração no Winthor que fala exatamente sobre esse ponto. Então eu recomendo validar com esse cliente na 316 com essa configuração do parâmetro dessa base de conhecimento ->: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026046831-WINT-O-que-fazer-para-que-o-pedido-n%C3%A3o-seja-gravado-quando-o-cliente-n%C3%A3o-possuir-limite-de-cr%C3%A9dito]

Se o Winthor deles não deixar salvar o pedido então pode subir uma demanda de erro para o maxPedido N3. Por que no caso nós estamos deixando e existe a possibilidade de eles não estarem deixando.

## Resposta Canonica

**Conclusão canônica**

Para cliente **Winthor**, que é o caso da **PCM**, o comportamento atual do código **sempre permite salvar e bloquear ou salvar e enviar o pedido**, inclusive quando o **limite de crédito é excedido**. Pela análise realizada, **não há configuração atualmente para impedir o RCA de salvar o pedido**.

No fluxo analisado, com o parâmetro **PEFRMITI_VENDA_AVISTA_SEMLIMITE = Não**, o sistema entra na validação de limite do cliente e apresenta a mensagem:

> "Cliente sem limite de crédito. Esse pedido será salvo mas poderá não ser processado no ERP."

Foram realizados testes e leitura das configurações, sem identificação de opção que impeça o salvamento do pedido no APK.

**Ação recomendada**
1. Validar com o cliente, na **316**, a configuração do parâmetro mencionada na base de conhecimento informada.
2. Se no **Winthor** do cliente o pedido **não** estiver sendo salvo nesse cenário, abrir **demanda de erro para o maxPedido N3**.

**Limitação da análise**
A conclusão está baseada no comportamento atual do código, nos testes realizados e na leitura das configurações. Há indicação de que o comportamento no Winthor do cliente deve ser validado.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 394922
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
