# GATE-94 - Valor divergente do ERP

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral - Dados Divergentes do ERP
- Natureza: N/A
- Atualizado em: 2024-09-24T15:48:31.127-0300

## Contexto do Problema

## Passos para reproduzir
>> Entrar no maxGestão;
>> Buscar indicadores de acordo com os filtros mostrados.

## Resultado apresentado
Valor divergente da rotina 146

## Resultado esperado
Valor igual ao Winthor

## Descrição
O valor apresentado usando os mesmo filtros está divergente da rotina 146. Verifiquei o acesso a todos os fornecedores, porem quando são aplicados os mesmos filtros o valor sempre apresenta divergencia.

## Comentarios do Gatekeeper

### 1. 2024-09-24T14:29:33.080-0300 | Filipe do Amaral Padilha

OBS *Não passar essa parte para o cliente, é só para você estar ciente*:

*O comportamento do maxGestão sempre foi assim, quando o cliente tem uma divergência entre histórico de itens e pedidos, os valores do maxGestão para venda transmitida não batem com a 146. Isso não se aplica a 111, a 111 tem que bater 100% em todos os casos porque lá a apuração é diferente; Se o cliente quiser que mesmo com essas condições que expliquei, os dados sejam compatíveis, então terá de solicitar melhoria para porque o maxGestão não faz o cálculo apurando por histórico de capas de pedidos.*

O que ocorre, referente a essa divergência é que a Rotina 146 realiza a apuração baseada no Histórico de Capas dos Pedidos (PCPEDC) fazendo a soma dos valores atendidos dos pedidos e que não foram cancelados.

Não é exatamente como vou colocar abaixo que a 146 faz, mas serve de base para nos ajudar nas análises:
{color:#739eca}SELECT{color}

{color:#c1aa6c}COUNT{color}(*),{color:#c1aa6c}SUM{color}({color:#00b8b8}VLTOTAL{color}),{color:#c1aa6c}SUM{color}({color:#00b8b8}VLATEND{color}),{color:#c1aa6c}SUM{color}({color:#00b8b8}VLTABELA{color})

{color:#739eca}FROM{color}

{color:#b788d3}MXSHISTORICOPEDC{color}

{color:#739eca}WHERE{color}

{color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/08/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color}) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'31/08/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} != {color:#cac580}'C'{color}

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color}({color:#c0c0c0}3{color})

{color:#739eca}AND{color} {color:#00b8b8}CONDVENDA{color} {color:#739eca}IN{color}({color:#c0c0c0}1{color},{color:#c0c0c0}5{color},{color:#c0c0c0}14{color},{color:#c0c0c0}9{color}){color:#eecc64};{color}

{color:#669768}--R$16797441.02 (VLATEND) {color}

Já o maxGestão por padrão, sempre fez por histórico de itens dos pedidos, porque a gente entende nesse conceito que traz uma informação mais real referente a apuração de pedidos.
{color:#739eca}SELECT{color}

{color:#c1aa6c}COUNT{color}({color:#739eca}DISTINCT{color} {color:#00b8b8}NUMPED{color}),{color:#c1aa6c}SUM{color}({color:#00b8b8}QT{color} * {color:#00b8b8}PVENDA{color})

{color:#739eca}FROM{color}

{color:#b788d3}MXSHISTORICOPEDI{color}

{color:#739eca}WHERE{color}

{color:#00b8b8}NUMPED{color} {color:#739eca}IN{color}({color:#739eca}SELECT{color} {color:#00b8b8}NUMPED{color} {color:#739eca}FROM{color} {color:#b788d3}MXSHISTORICOPEDC{color} {color:#739eca}WHERE{color}

{color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/08/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color}) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'31/08/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} != {color:#cac580}'C'{color}

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color}({color:#c0c0c0}3{color})

{color:#739eca}AND{color} {color:#00b8b8}CONDVENDA{color} {color:#739eca}IN{color}({color:#c0c0c0}1{color},{color:#c0c0c0}14{color},{color:#c0c0c0}9{color},{color:#c0c0c0}5{color}))

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} != {color:#cac580}'C'{color}

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}{color:#eecc64};{color}

{color:#669768}--R$17055721.76 maxGestão {color}

## Resposta Canonica

A divergência é esperada neste cenário porque as apurações são feitas por bases diferentes:

- **Rotina 146**: apura pelos **históricos de capas dos pedidos** (`PCPEDC/MXSHISTORICOPEDC`), somando os valores atendidos de pedidos **não cancelados**.
- **maxGestão**: apura pelo **histórico de itens dos pedidos** (`MXSHISTORICOPEDI`).

Assim, quando existe divergência entre o histórico de itens e o histórico de pedidos, o valor de **venda transmitida** no maxGestão pode ficar diferente do valor apresentado na rotina 146.

Com os filtros informados:
- Período: **01/08/2024 a 31/08/2024**
- `POSICAO != 'C'`
- `CODOPERACAO != 2`
- `CODFILIAL IN (3)`
- `CONDVENDA IN (1,5,14,9)`

Os resultados de referência foram:
- **Base por capas (`MXSHISTORICOPEDC`)**: **R$ 16.797.441,02** (`VLATEND`)
- **Base por itens (`MXSHISTORICOPEDI`) / maxGestão**: **R$ 17.055.721,76**

Consultas usadas como base da análise:

```sql
SELECT COUNT(*), SUM(VLTOTAL), SUM(VLATEND), SUM(VLTABELA)
FROM MXSHISTORICOPEDC
WHERE TRUNC(DATA) BETWEEN TO_DATE('01/08/2024', 'DD/MM/YYYY') AND TO_DATE('31/08/2024', 'DD/MM/YYYY')
  AND POSICAO != 'C'
  AND CODOPERACAO != 2
  AND CODFILIAL IN(3)
  AND CONDVENDA IN(1,5,14,9);
```

```sql
SELECT COUNT(DISTINCT NUMPED), SUM(QT * PVENDA)
FROM MXSHISTORICOPEDI
WHERE NUMPED IN(
    SELECT NUMPED
    FROM MXSHISTORICOPEDC
    WHERE TRUNC(DATA) BETWEEN TO_DATE('01/08/2024', 'DD/MM/YYYY') AND TO_DATE('31/08/2024', 'DD/MM/YYYY')
      AND POSICAO != 'C'
      AND CODOPERACAO != 2
      AND CODFILIAL IN(3)
      AND CONDVENDA IN(1,14,9,5)
)
AND POSICAO != 'C'
AND CODOPERACAO != 2;
```

Conclusão: a origem da divergência está na **diferença de critério de apuração** entre a rotina 146 e o maxGestão. Se for necessário que os valores fiquem compatíveis também nesse cenário, a orientação é **solicitar uma melhoria**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 396610
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
