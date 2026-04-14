# GATE-469 - Sequenciamento de visitas

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: Dúvida
- Atualizado em: 2024-12-06T12:01:23.235-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do rca, iniciar um pedido e realizar checkin no primeiro cliente do dia, realizar o pedido e checkout. Em seguida, realizar o checkin no último cliente do dia.

## Resultado apresentado
É verificado que o fluxo citado na reprodução é possível, mesmo com a permissão obrigando o sequenciamento de visitas ativa.

## Resultado esperado
É esperado que a aplicação respeite o sequenciamento de visitas.

## Descrição
Cliente relata que a aplicação não está obrigando o RCA a realizar a sequência de visitas, mesmo com a permissão 'Obrigar sequenciamento de visitas' ativa para o RCA e o parâmetro UTILIZA_CHECKIN_CHECKOUT ativo para o RCA.

Foi verificado que o rca em questão possui roteiro cadastrado no dia.

Além disso, os testes foram realizados em base zero na versão de ponta.

Login para teste:

jfrios.olavo

## Comentarios do Gatekeeper

### 1. 2024-12-06T12:01:23.234-0300 | Filipe do Amaral Padilha

Seria uma melhoria por causa do seguinte, para usar sequenciamento de visitas, é obrigatório habilitar a permissão "Bloquear venda de clientes fora da rota".

E eu observei que eles trabalham com visita fora de rota, então eles não poderiam ligar essa configuração.

Eles teriam a seguinte opção no momento:

>> Eles teriam que trabalhar com sequenciamento de visitas e visita avulsa bloqueando venda fora de rota, dai só conseguiria vender fora de rota gerando visita avulsa. Porém na visita avulsa não é validada sequência de visitas.

O que eles estão querendo é trabalhar com visita fora de rota e com sequenciamento de visitas e essa opção atualmente não existe no maxPedido.

## Resposta Canonica

**Conclusão canônica**

O comportamento relatado não caracteriza erro de funcionamento do maxPedido nas condições informadas. Atualmente, **não existe suporte para trabalhar simultaneamente com visita fora de rota e com sequenciamento de visitas**.

Para que o **sequenciamento de visitas** seja aplicado, é **obrigatório habilitar a permissão _“Bloquear venda de clientes fora da rota”_**. Porém, foi identificado que o cenário em uso **trabalha com visita fora de rota**, o que inviabiliza essa configuração no processo atual.

Além disso, **na visita avulsa não é validada a sequência de visitas**.

**Síntese técnica**
- O maxPedido **não permite hoje** combinar:
  - **visita fora de rota**
  - **sequenciamento de visitas**
- Para usar **sequenciamento de visitas**, é obrigatório ativar:
  - **“Bloquear venda de clientes fora da rota”**
- Como o processo observado **utiliza visita fora de rota**, a regra de sequenciamento **não será garantida nesse contexto**
- Em **visita avulsa**, **não há validação de sequência**

**Ação recomendada**
- Operar com **sequenciamento de visitas** juntamente com o bloqueio de venda fora da rota.
- Quando houver necessidade de vender fora da rota, **gerar visita avulsa**.

**Limitação atual**
- Se houver necessidade de suportar **visita fora de rota com sequenciamento de visitas ao mesmo tempo**, o tratamento deve seguir como **melhoria de produto**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 410814
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
