# GATE-730 - Relatório geolocalização

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Check-In/Check-Out
- Natureza: Dúvida
- Atualizado em: 2025-02-03T16:56:46.670-0300

## Contexto do Problema

## Passos para reproduzir
Na MXSVISITAFV consta apenas um atendimento para cada cliente, porem no maxGestão constam multiplos atendimentos para o mesmo cliente

## Resultado apresentado
Mostram múltiplos atendimentos para o mesmo cliente sendo que teve apenas 1

## Resultado esperado
Mostrar apenas 1 atendimento.

## Descrição
Na MXSVISITAFV consta apenas um atendimento para cada cliente, porem no maxGestão constam multiplos atendimentos para o mesmo cliente

## Comentarios do Gatekeeper

### 1. 2025-02-03T15:04:50.740-0300 | Filipe do Amaral Padilha

Será encaminhado para N3, porém abaixo é importante realizar o entendimento sobre o que foi analisado:

Cenário:
CODUSUARIO: 93229 LOGIN: larbos.rodolfo

Segundo a base de dados maxTracking, ocorreu o evento de justificativa de não venda no cliente 5446 duas vezes (2x).

Foram registradas essas duas de forma correta:
{"codigoVinculacao":-1,"dataAbertura":"Jan 22, 2025 10:23:23","dataFechamento":"Jan 22, 2025 10:23:28","motivoJustificativa":"Cliente Abastecido"}

{"codigoVinculacao":-1,"dataAbertura":"Jan 22, 2025 10:05:48","dataFechamento":"Jan 22, 2025 10:06:02","motivoJustificativa":"Cliente Abastecido"}

A princípio, isso foi uma ação manual do vendedor, de registrar duas vezes a justificativa.

Referente às quatro informações de justificativa do cliente 5446 que constam no relatório do dia 22/01/2025, será encaminhado para N3 do maxPedido, porque foi o maxPedido que gerou a informação em duplicidade. Será solicitado que realizem a normalização e investiguem possíveis problemas com a geração dos dados.

######################################################################

Sobre o questionamento do pedido do cliente 557841 no dia 22/01/2025

Ele na verdade é um pedido complementar, e de fato o RCA digitou fora do raio do cliente.

Limite do raio do cliente para checkin e checkout: 100 (só valida se o RCA realizar o Checkin)

Tolerancia da cerca eletrônica(GPS_EDGE_METERS_SIZE): NULL

GPS_EDGE_BLOCK = N, não está fazendo validação sempre da localização ao realizar Checkin, pedidos ou justificativas.

O sistema deles não está configurado para sempre solicitar Checkin, por isso ele conseguiu enviar um pedido mesmo sem estar na localização. Ele não precisou fazer Checkin para digitar o pedido.

O parâmetro PERMITIR_PEDIDO_SEM_CHECKIN está configurado = Sim no RCA 543

Para sempre solicitar Checkin configurar os parâmetros:
PERMITIR_PEDIDO_SEM_CHECKIN = N
OBRIGA_CHECKIN_CLIENTE_FORA_ROTA = S

## Resposta Canonica

Identificada divergência em dois cenários distintos no dia 22/01/2025, para o usuário **CODUSUARIO 93229 / login larbos.rodolfo**:

- **Cliente 5446**: na base **maxTracking** constam **dois registros** de justificativa de não venda, ambos com motivo **“Cliente Abastecido”**, nos horários:
  - 10:05:48 a 10:06:02
  - 10:23:23 a 10:23:28

  Além disso, as **quatro informações de justificativa** exibidas no relatório desse cliente em **22/01/2025** foram informadas como **geradas em duplicidade pelo maxPedido**. A análise inicial aponta também registro manual em duplicidade da justificativa pelo vendedor, porém essa conclusão é **preliminar**.

- **Cliente 557841**: o registro corresponde a **pedido complementar**. Foi informado que o **RCA digitou fora do raio do cliente**, e isso foi permitido porque o ambiente **não exige check-in para envio do pedido** na configuração atual.

Parâmetros observados no cenário:
- **Limite do raio**: 100
- **GPS_EDGE_METERS_SIZE**: NULL
- **GPS_EDGE_BLOCK**: N
- **PERMITIR_PEDIDO_SEM_CHECKIN**: Sim no **RCA 543**

Conclusão:
- No **cliente 5446**, a duplicidade decorre de registros duplicados de justificativa e de geração duplicada no **maxPedido**.
- No **cliente 557841**, não se trata da mesma origem de duplicidade, mas de comportamento permitido pela configuração atual, que não obriga check-in.

Ação recomendada:
- **Encaminhar para o N3 do maxPedido** para:
  - normalização das informações duplicadas;
  - investigação da geração dos dados.
- Caso seja desejado obrigar check-in sempre, ajustar:
  - **PERMITIR_PEDIDO_SEM_CHECKIN = N**
  - **OBRIGA_CHECKIN_CLIENTE_FORA_ROTA = S**

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 420988
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
