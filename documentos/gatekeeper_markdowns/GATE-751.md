# GATE-751 - Clientes positivados zerados mesmo com pdidos na base do RCA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Histórico
- Natureza: Dúvida
- Atualizado em: 2025-02-06T15:43:25.311-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar a base do RCA em anexo
>>Ir até o gráfico 'Clientes positivados'
>>Ir nos pedidos enviados

## Resultado apresentado
>>Mesmo com pedidos na base do RCA o gráfico ainda permanece como '0'
>>A parte de meta também permanece zerada, mas pelo que vi a meta é de 1 milhão e os pdidos somaram R$1.485,26 o que não chega perto de 1 % da meta que seria de R$10.000,00

## Resultado esperado
>>Os clientes devem aparecer no gráfico de clientes positivados.

## Descrição
>>Mesmo com registro na MXSDIASUTEIS e na ERP_MXSDATAS e com pedidos na base do RCA o maxPedido ainda mostra o gráfico 'Clientes positivados' em branco

Login: innovar.ti

Senha: Hash

## Comentarios do Gatekeeper

### 1. 2025-02-06T15:43:25.308-0300 | Filipe do Amaral Padilha

Foi verificado que o maxPedido v4 busca as informações no backend por padrão do script REQ_MXSVENDA_MIX;

E na consulta do script, se tratando de positivação de clientes, ela sempre ocorrerá somente se o pedido for faturado, porque nós buscamos e validamos dados da PCNFSAID.

Como os pedidos do RCA CODUSUR 2, que é atualmente o RCA vinculado ao usuário não estão FATURADOS e não possuem nota, então o gráfico permanece zerado na positivação de clientes.

(O comportamento é diferente na positivação de produtos, tem parâmetro para considerar só por positivação no faturamento ou na transmissão de pedidos).

Referente ao gráfico de vendas, realmente, como a meta é 1 milhão e o valor vendido não ultrapassou os R$10000 que seria correspondente à 1%, então o valor atual seria 0.53% (Nem 1% ainda) então o gráfico não mostra a porcentagem abaixo de 1%.

Esses gráficos são novos então se o cliente quiser alterar a regra de negócios eu recomendo enviar como melhoria.

## Resposta Canonica

**Conclusão canônica**

O comportamento observado está aderente à regra atual do **maxPedido v4**.

A positivação de clientes no gráfico **Clientes positivados** ocorre apenas quando o pedido está **faturado**, porque o backend consulta o script `REQ_MXSVENDA_MIX`, que valida a informação com base na tabela `PCNFSAID`. No caso analisado, os pedidos do **RCA CODUSUR 2**, vinculado ao usuário informado, **não estão faturados** e **não possuem nota**. Por isso, esses pedidos **não entram na positivação** e o gráfico permanece zerado.

No gráfico de vendas, a **meta é de 1.000.000** e o valor atual representa **0,53%** dessa meta. Como o gráfico **não exibe percentuais abaixo de 1%**, a informação também permanece zerada visualmente.

```sql
REQ_MXSVENDA_MIX
PCNFSAID
```

**Limitações/regras atuais**
- A positivação de clientes considera somente pedidos faturados.
- Pedidos sem faturamento e sem nota não compõem a positivação.
- O gráfico de vendas não mostra percentual inferior a 1%.
- Os gráficos são novos.

**Próximo passo**
Se houver necessidade de alterar essa regra de negócio, a demanda deve ser registrada como **melhoria**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 422130
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
