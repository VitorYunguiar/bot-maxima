# GATE-573 - Ajuste de conta corrente incorreto.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: SINTEC SISTEMAS
- Assunto: MXPED - Conta Corrente
- Natureza: Dúvida
- Atualizado em: 2025-01-03T11:19:45.302-0300

## Contexto do Problema

## Passos para reproduzir
>>Verificar a MXSHISTORICOPEDI e a ERP_MXSLOGRCA com os selects enviados
>>Verificar relatório da central de configurações enviado ou retirar um novo

## Resultado apresentado
>>Mesmo não havendo nenhum desconto ou acrescimo nos pedidos, o sistema está fazendo alterações no conta corrente do RCA

## Resultado esperado
>>Como não existe acrescimo ou desconto, o conta corrente deve permanecer com o mesmo valor.

## Descrição
>>Na MXSHISTORICOPEDI do pedido 517261 de exemplo (Existem outros) os valores do PTABELA e PVENDA são iguais, porém mesmo assim na ERP_MXSLOGRCA e no sistema foi adicionado o valor de 220, sendo 2,20 para cada unidade do produto 176

Selects utilizados:

SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED = 517261;

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPED = 517261 ORDER BY DATA DESC;

## Comentarios do Gatekeeper

### 1. 2025-01-03T11:19:45.300-0300 | Filipe do Amaral Padilha

O sistema utiliza o parâmetro USAR_CCRCA_MAXIMA = S na tabela MXSPARAMETRO, de modo que a movimentação é realizada na nossa PKG, baseada nas informações do sistema.

Contexto do Pedido
Pedido:
NUMPEDRCA: 137
NUMPED: 517261
Item: 176
Preço Base: 13,80
Informações no JSON e Histórico
No JSON enviado, o campo "PrecoVendaInformado" tinha o valor de 13,80;
No JSON enviado, o preço base do campo "PrecoBase": 13.8" também confirmava esse preço de base;
Nesse dia, também havia uma política de descontos que creditava sob a política e era aplicada ao preço de tabela do produto 176. A política com aplicação automática "DESCONTOROMA176" incidia 13.75% de desconto no preço de 16 reais, resultando nos 13.80. Por esse motivo houve movimentação de conta corrente.

Entretanto, segundo o ERP deles e o preço de tabela, o preço de venda registrado no histórico do pedido (tabela MXSHISTORICOPEDC) foi de 16,00.

Datas relevantes:
Pedido aberto: 2024-12-30 15:49:29.000
Última atualização do histórico: 2024-12-31 03:04:18.000

Conclusão:
Se confirmado que o preço correto do item na época era R$13,80, o problema provavelmente se originou na integração, que registrou erroneamente o preço de venda como R$16,00 no histórico. Isso requer análise do cliente com a integração do ERP dele para alinhar os sistemas e evitar futuros problemas com movimentação de conta corrente. Se não era para ter movimentado, então o ERP deles deveria ter enviado o preço de venda no endpoint MXSHISTORICOPEDC = 13.80. Se era para ter movimentado então a justificativa já está citada acima e o ERP mandou o preço corretamente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414653
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "essa diferença entre o valor enviado (13,80) e o valor registrado no histórico (16,00) explica a movimentação observada" — o texto-fonte diz que isso é uma causa provável/condicional, não uma explicação confirmada. | "Com isso, e considerando o parâmetro `USAR_CCRCA_MAXIMA = S` junto da política automática de desconto, houve a movimentação no conta corrente." — o texto-fonte não atribui de forma conclusiva a movimentação a essa combinação; apresenta cenário condicional e menciona que a política foi o motivo da movimentação em um contexto específico, mas a conclusão geral permanece condicional. | "Responsável pela correção: Cliente, por meio da integração do ERP." — o texto-fonte recomenda análise do cliente com a integração do ERP para alinhar os sistemas, mas não afirma explicitamente responsabilidade pela correção.
