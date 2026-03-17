# Validação de Produtos Próximos ao Vencimento

## Visão Geral

A funcionalidade implementa uma validação parametrizável de produtos próximos ao vencimento, realizando a análise automática da data de validade no momento da inclusão do item no pedido.

## Objetivos da Solução

- Analisar automaticamente a data de validade do produto;
- Exibir alertas claros e objetivos conforme o status:
  - Produto vencido;
  - Produto próximo ao vencimento;
- Adicionar legenda visual para identificação rápida na listagem;
- Permitir utilização da informação como filtro na busca de produtos;
- Não gerar impacto negativo na performance do aplicativo.

Essa funcionalidade proporciona mais segurança ao vendedor e melhora a experiência do cliente.

---

## Campos de Validade Considerados

A validação pode utilizar um dos seguintes campos:

- **P** = `MXSPRODUT.DTVENC`  
  Validade do produto

- **W** = `MXSVALIDADEWMS.DATA`  
  Validade via WMS

- **L** = `MXSLOTE.DTVALIDADE`  
  Validade por lote

---

## Parametrização

### DIAS_PRODUTO_PROXIMO_VENCIMENTO
- Define a quantidade de dias considerada para geração da legenda (≤).

### TIPO_LEGENDA_DATA_VENCIMENTO
- Define qual data de vencimento será considerada para gerar a legenda.
- Valores possíveis: `P`, `W` ou `L`.

### HABILITA_ALERTA_PROD_PROXIMO_VENCIMENTO
- Habilita o alerta ao adicionar um produto próximo ao vencimento.

---

## Funcionamento

Com os parâmetros:
- `DIAS_PRODUTO_PROXIMO_VENCIMENTO` preenchido;
- `TIPO_LEGENDA_DATA_VENCIMENTO` definido;
- `HABILITA_ALERTA_PROD_PROXIMO_VENCIMENTO` ativo;

O sistema passa a:

- Exibir o produto na aba tabela com ícone identificador de proximidade de vencimento;
- Permitir uso da informação como filtro na busca;
- Exibir alerta ao tentar adicionar o produto ao pedido, informando:
  - Quantos dias faltam para o vencimento; ou
  - Se o produto já está vencido.

---

## Pré-requisito

- O aplicativo deve estar na versão mais recente (versão ponta).
- A versão já foi disponibilizada no ambiente para validação.