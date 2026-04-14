# GATE-612 - Divergencia entre valores exibidos entre maxgestão e rotina 146

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral - Indicadores
- Natureza: Dúvida
- Atualizado em: 2025-01-10T10:04:28.378-0300

## Contexto do Problema

## Passos para reproduzir
efetuar o acesso ao portal do maxgestão do cliente e realizar a consulta conforme os filtros nos prints apresentados

## Resultado apresentado
divergencias de valores entre rotina 146 e o que é exibido no gestão

## Resultado esperado
o cliente espera que sejam exibidos valores equivalentes.

## Descrição
Senhores, ao analisar o cenário relatado pelo cliente, não consegui identificar o que tem gerado a situação de divergência relatada, uma vez que observei a seguinte situação:

Portal MaxGestão apresenta o seguinte valor:

!image-2025-01-09-15-55-30-337.png!

Para a 146 está exibindo o seguinte valor:

!image-2025-01-09-15-56-36-487.png!

MXSHISTORICOPEDC:

!image-2025-01-09-15-57-33-910.png!

MXSHISTORICOPEDI

!image-2025-01-09-15-58-19-303.png!

Nesse cenário, o que está incorreto para que esteja sendo apresentado tal divergencia? existem alguns outros parametros na consulta que devem ser considerados para se chegar ao valor esperado?

## Comentarios do Gatekeeper

### 1. 2025-01-10T10:04:28.378-0300 | Filipe do Amaral Padilha

A rotina 146 do Winthor considera o valor de venda dos históricos das capas dos pedidos (VLATEND) da PCPEDC e o maxGestão considera o valor dos históricos de vendas dos itens.

Por esse motivo ocorre essa diferença na apresentação da informação.

SELECT SUM(VLATEND) FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('07/01/2025', 'dd/MM/yyyy') AND TO_DATE('07/01/2025', 'dd/MM/yyyy') AND POSICAO <> 'C' AND CODSUPERVISOR = 14;
Resulta em R$198689.3

SELECT SUM(QT*PVENDA) FROM PCPEDI WHERE NUMPED IN(SELECT NUMPED FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('07/01/2025', 'dd/MM/yyyy') AND TO_DATE('07/01/2025', 'dd/MM/yyyy') AND POSICAO <> 'C' AND CODSUPERVISOR = 14) AND POSICAO <> 'C'
Resulta em R$201231.48

Como o cliente tem uma divergência nos históricos do próprio banco local referente a essa informação da venda dos itens, então os valores não batem.

Importante pontuar também que a maioria dos clientes essa informação não bate mesmo. O maxGestão tem essa apuração a parte das informações, mas que também garante mais precisão na informação. No caso específico da venda transmitida, é considerado normal e está no escopo do produto que não é compatível com a 146, porque o ERP faz de um jeito e a nossa aplicação de outro, simplesmente.

Já referente a Rotina 111 sim (Venda Faturada), os dados devem bater, essa explicação acima é uma especificidade da venda transmitida no maxGestão em relação à 146.

Por fim, se o cliente quiser um comportamento divergente do atual, seria considerado uma sugestão de melhoria do sistema.

## Resposta Canonica

A divergência é causada por diferença de critério de apuração entre o maxGestão e a rotina 146, especificamente para **venda transmitida**.

- A **rotina 146** considera o valor de venda a partir do histórico da **capa do pedido**, usando o campo **VLATEND** da **PCPEDC**.
- O **maxGestão** considera o valor a partir do histórico de venda dos **itens do pedido**.

Na análise do cenário informado, com os parâmetros:

- **Período:** 07/01/2025 a 07/01/2025  
- **POSICAO <> 'C'**
- **CODSUPERVISOR = 14**

foram apurados os seguintes valores:

```sql
SELECT SUM(VLATEND)
FROM PCPEDC
WHERE TRUNC(DATA) BETWEEN TO_DATE('07/01/2025', 'dd/MM/yyyy')
                      AND TO_DATE('07/01/2025', 'dd/MM/yyyy')
  AND POSICAO <> 'C'
  AND CODSUPERVISOR = 14;
```

**Resultado:** R$ 198.689,30

```sql
SELECT SUM(QT*PVENDA)
FROM PCPEDI
WHERE NUMPED IN (
    SELECT NUMPED
    FROM PCPEDC
    WHERE TRUNC(DATA) BETWEEN TO_DATE('07/01/2025', 'dd/MM/yyyy')
                          AND TO_DATE('07/01/2025', 'dd/MM/yyyy')
      AND POSICAO <> 'C'
      AND CODSUPERVISOR = 14
)
AND POSICAO <> 'C';
```

**Resultado:** R$ 201.231,48

Conclusão: a divergência ocorre porque os históricos de venda no banco local do cliente, no nível dos itens, não correspondem ao valor considerado na capa do pedido. Para **venda transmitida**, essa diferença entre maxGestão e rotina 146 é **esperada**, está **no escopo do produto** e decorre do fato de que o **ERP apura de uma forma e a aplicação de outra**.

Observação: para a **Rotina 111 (Venda Faturada)**, os dados **devem bater**.

**Orientação:** informar ao cliente que, para venda transmitida, a divergência em relação à rotina 146 é prevista. Se o cliente precisar de comportamento diferente do atual, o tratamento deve ser feito como **sugestão de melhoria do sistema**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 416164
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
