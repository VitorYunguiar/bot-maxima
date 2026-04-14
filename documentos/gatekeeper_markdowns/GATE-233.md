# GATE-233 - divergencia de painel de indicadores e rotina do winthor.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral - Indicadores
- Natureza: Dúvida
- Atualizado em: 2024-10-28T17:12:44.102-0300

## Contexto do Problema

## Passos para reproduzir
Acessar o ambiente do cliente e realizar os filtros conforme os prints, em seguida realizar a consulta equivalente na rotina do winthor.

## Resultado apresentado
divergencia de valores de venda sendo retornados.

## Resultado esperado
é esperado queos

## Descrição
Senhores, estamos observando uma divergência de valores entre o painel de indicadores e rotina 146 que não é esperada. A principio, o painel abaixo deveria apresentar o mesmo valor que é retornado na rotina:
!image-2024-10-28-09-57-39-495.png!

!image-2024-10-28-09-57-59-949.png!

Uma vez que o filtro utilizado no painel geral, é o filtro equivalente ao que está sendo usado na rotina, porém os valores tem essa divergência:

!image-2024-10-28-09-59-18-654.png!

## Comentarios do Gatekeeper

### 1. 2024-10-28T13:11:17.805-0300 | Filipe do Amaral Padilha

A rotina 146 do Winthor considera o valor de venda dos históricos das capas dos pedidos (VLATEND) da PCPEDC e o maxGestão considera o valor dos históricos de vendas dos itens.

Por esse motivo ocorre essa diferença na apresentação da informação.

SELECT SUM(VLATEND) FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('22/10/2024', 'dd/MM/yyyy') AND TO_DATE('22/10/2024', 'dd/MM/yyyy') AND POSICAO <> 'C' AND CODSUPERVISOR = 16;
Resulta em R$120389.53

SELECT SUM(QT*PVENDA) FROM PCPEDI WHERE NUMPED IN(SELECT NUMPED FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('22/10/2024', 'dd/MM/yyyy') AND TO_DATE('22/10/2024', 'dd/MM/yyyy') AND POSICAO <> 'C' AND CODSUPERVISOR = 16 AND CODFILIAL = 'T3') AND POSICAO <> 'C'
Resulta em R$120597.3185851 ~= 120597.33

Como o cliente tem uma divergência nos históricos do próprio banco local referente a essa informação da venda dos itens, então os valores não batem.

Importante pontuar também que a maioria dos clientes essa informação não bate mesmo. O maxGestão tem essa apuração a parte das informações, mas que também garante mais precisão na informação. No caso específico da venda transmitida, é considerado normal e está no escopo do produto que não é compatível com a 146, porque o ERP faz de um jeito e a nossa aplicação de outro, simplesmente.

Já referente a Rotina 111 sim (Venda Faturada), os dados devem bater, essa explicação acima é uma especificidade da venda transmitida no maxGestão em relação à 146.

Por fim, se o cliente quiser um comportamento divergente do atual, seria considerado uma sugestão de melhoria do sistema.

## Resposta Canonica

A divergência identificada entre o painel de indicadores e a rotina 146 é esperada pelo critério de apuração utilizado por cada fonte.

A rotina 146 do Winthor considera o valor de venda a partir do histórico das capas dos pedidos, campo `VLATEND` da tabela `PCPEDC`. Já o maxGestão considera o valor com base no histórico de vendas dos itens. Por isso, especialmente no caso de venda transmitida, os valores não são compatíveis com a rotina 146. Esse comportamento está dentro do escopo atual do produto.

Na validação informada, com os filtros:
- Data inicial/final: 22/10/2024
- `POSICAO <> 'C'`
- `CODSUPERVISOR = 16`
- `CODFILIAL = 'T3'`

foram obtidos os seguintes resultados:

```sql
SELECT SUM(VLATEND)
FROM PCPEDC
WHERE TRUNC(DATA) BETWEEN TO_DATE('22/10/2024', 'dd/MM/yyyy')
                      AND TO_DATE('22/10/2024', 'dd/MM/yyyy')
  AND POSICAO <> 'C'
  AND CODSUPERVISOR = 16;
```

Resultado na `PCPEDC`: **R$ 120389,53**

```sql
SELECT SUM(QT*PVENDA)
FROM PCPEDI
WHERE NUMPED IN (
    SELECT NUMPED
    FROM PCPEDC
    WHERE TRUNC(DATA) BETWEEN TO_DATE('22/10/2024', 'dd/MM/yyyy')
                          AND TO_DATE('22/10/2024', 'dd/MM/yyyy')
      AND POSICAO <> 'C'
      AND CODSUPERVISOR = 16
      AND CODFILIAL = 'T3'
)
AND POSICAO <> 'C';
```

Resultado na `PCPEDI`: **R$ 120597,3185851** (aprox. **R$ 120597,33**)

Também foi informado que o cliente possui divergência nos históricos do próprio banco local referente à informação de venda dos itens.

Conclusão:
- **Não se trata de erro do painel**, mas de diferença de regra de cálculo entre a rotina 146 e o maxGestão.
- **Para a Rotina 111 (Venda Faturada), os dados devem bater.**
- Caso o cliente deseje comportamento diferente do atual, a tratativa deve ser registrada como **sugestão de melhoria**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 403388
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
