# GATE-177 - Obrigar sequenciamento de visitas

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor Cloud
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: N/A
- Atualizado em: 2024-10-14T09:58:01.506-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Ir na tela de clientes
>>Iniciar um pedido no primeiro cliente do roteiro
>>Fazer check-in, justificativa de não venda e gravar o check-out
>>Seguir para o terceiro cliente do roteiro
>>E assim o aplicativo não barra nada, ou seja não obriga o RCA seguir o sequenciamento das visitas

Login: jfrios.ti
senha: acesso temporário

## Resultado apresentado
Aplicativo não obriga o RCA  a seguir o sequenciamento de visitas.

## Resultado esperado
O que o cliente precisa é que o RCA siga com todas as suas visitas na sequencia, sem pular de fazer check-in/out, justificativa de não venda ou pedido nos clientes do roteiro do dia.

## Descrição
O cliente gostaria de obrigar um sequenciamento das visitas no MaxPedido.

Exemplo o RCA tem no seu roteiro do dia 11/10 os clientes:
Cliente 1
Cliente 2
Cliente 3
RCA realizou o atendimento no cliente 1, e já seguiu para o cliente 3, nesse momento o cliente quer que o aplicativo barre o atendimento ao cliente 3, obrigando o RCA a fazer o atendimento do cliente 1 primeiro. Com essa ideia o cliente obriga o RCA a seguir todo o seu roteiro naquele dia, entendo que temos parametrizações para bloquear a rota pendente, mas o bloqueio ocorre somente no outro dia.

O que o cliente precisa é que o RCA siga com todas as suas visitas na sequencia, sem pular de fazer check-in/out, justificativa de não venda ou pedido nos clientes do roteiro do dia.

Testamos isso habilitando a permissão: Obrigar sequenciamento de visitas e habilitando o parâmetro OBRIGAR_ATENDIMENTO_PARA_CHECKOUT, mais o RCA conseguiu não seguir o sequenciamento das visitas.

## Comentarios do Gatekeeper

### 1. 2024-10-14T09:46:58.080-0300 | Filipe do Amaral Padilha

--Foi feita análise na versão ponta 3.253.3

Para obrigar o sequenciamento nos clientes do Roteiro:

Permissões na Central:
Bloquear venda de clientes fora da rota = V
Obrigar sequenciamento de visitas = V

Parâmetro: UTILIZA_CHECKIN_CHECKOUT = S

Com essas permissões para fazer um atendimento fora de rota o RCA sempre vai precisar gerar uma visita avulsa, pressionando em cima do cliente que não é do roteiro atual. Dai ao gerar a visita avulsa ele vai conseguir atender fora de rota e sem seguir sequência. Porém os clientes da Rota, ele vai ser forçado a seguir a sequência.

Se você quiser testar antes de entregar ao cliente, eu deixei o usuário jfrios.TI pronto com essas configurações.

*Obs: Não passar ao cliente, analisando eu não encontrei outra forma de configurar, para obrigar a sequência no roteiro precisa ter as duas permissões que citei acima*

!image-2024-10-14-09-42-44-204.png!

Se quiser atender fora de rota (só para clientes fora do roteiro atual):

!image-2024-10-14-09-43-21-078.png!

!image-2024-10-14-09-43-38-077.png!

!image-2024-10-14-09-44-01-263.png!

!image-2024-10-14-09-44-55-864.png!

!image-2024-10-14-09-45-34-608.png!

## Resposta Canonica

Para obrigar o sequenciamento das visitas nos clientes do roteiro, é necessário configurar em conjunto:

- **Bloquear venda de clientes fora da rota = V**
- **Obrigar sequenciamento de visitas = V**
- **UTILIZA_CHECKIN_CHECKOUT = S**

Na análise realizada na versão **3.253.3**, foi validado que, com essas configurações, **os clientes da rota ficam sujeitos ao sequenciamento**.

Ponto importante: o atendimento fora de rota ainda pode ocorrer por meio de **visita avulsa**. Nesse caso, o RCA precisa gerar manualmente essa visita ao selecionar um cliente que não pertence ao roteiro atual, e assim conseguirá atender **fora de rota e sem seguir a sequência**. Portanto, o sequenciamento é forçado para os **clientes do roteiro**, mas não impede atendimento fora de rota via visita avulsa.

Também foi informado que o usuário **jfrios.TI** foi deixado configurado para teste.

### Ação recomendada
- Configurar na Central:
  - **Bloquear venda de clientes fora da rota = V**
  - **Obrigar sequenciamento de visitas = V**
- Configurar o parâmetro:
  - **UTILIZA_CHECKIN_CHECKOUT = S**
- Validar o comportamento com o usuário **jfrios.TI** antes de retornar ao cliente.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 400631
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
