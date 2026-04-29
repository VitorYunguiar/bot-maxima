# Fluxo de pedidos com sistema GERA

> Documento preparado para ingestao em banco vetorial (RAG).
> Sistema: maxPedido | GERA | maxPag | APIVendas | APIResumo | APITimeline
> Area: Integracao de pedidos | Campanhas progressivas | Logs | maxPayment

---

## Sobre este documento

Este documento descreve a melhoria para permitir a implementacao do fluxo de pedidos usando o sistema GERA, incluindo bloqueio do pedido enquanto aguarda processamento, liberacao posterior, tratamento de pedidos maxPag e armazenamento de logs de retorno.

Palavras-chave: GERA, sistema GERA, Pedido.UsandoSistemaGera, AguardandoPedidoGERA, PedidoProcessamentoGERA, SalvarPedidos, SalvarPedidosGERA, SalvarLOGGERA, MXSPEDIDOGERALOG, MXSRELATORIOCAMPANHAS, AplicouDescontoGera, HABILITA_SISTEMA_GERA, GUID_DISTRIBUIDOR_GERA, FUNCTION_KEY_GERA, AguardandoLinkMaxPayment, vendaCartaoCredito, maxPag, campanhas progressivas.

---

## Necessidade

Objetivos do fluxo:

- Possibilitar a integracao entre maxPedido e sistema GERA.
- Registrar logs estruturados para analises futuras.
- Garantir controle adequado do fluxo de pedidos enquanto aguardam processamento no GERA.
- Garantir processamento correto de pedidos maxPag apos aplicacao de desconto pelo sistema GERA.

---

## Fluxo de integracao do pedido

1. O aplicativo envia o pedido contendo a flag:

```text
Pedido.UsandoSistemaGera = true
```

2. Quando essa flag esta habilitada, o pedido e salvo pelo endpoint `SalvarPedidos` com:

```text
Status: AguardandoPedidoGERA = 27
Critica: PedidoProcessamentoGERA = 54
```

3. O pedido permanece bloqueado ate a finalizacao do processamento no sistema GERA.

4. Apos o processamento, o aplicativo envia `ID_PEDIDO` e a flag `vendaCartaoCredito` para liberacao pelo endpoint:

```text
SalvarPedidosGERA
```

## Excecoes em que o pedido com GERA nao fica com status 27

Mesmo com a flag habilitada, o pedido nao e salvo como `AguardandoPedidoGERA = 27` nos seguintes casos:

- Aguardando autorizacao de preco: status `8`.
- Envio bloqueado: status `6`.
- Reenvio por algum motivo apos ja ter sido integrado no ERP: status `4`.

---

## Liberacao apos retorno do GERA

### Venda normal

Quando:

```text
vendaCartaoCredito = false
```

O endpoint define o status do pedido como `0`, permitindo o fluxo normal de integracao.

### Venda com maxPag

Quando:

```text
vendaCartaoCredito = true
```

O fluxo deve:

1. Gerar o link de pagamento do pedido.
2. Salvar o pedido com status:

```text
AguardandoLinkMaxPayment = 16
```

3. Seguir o fluxo normal de integracao para pedidos maxPag.

### Registro de campanhas progressivas

Produtos com:

```text
AplicouDescontoGera = true
```

devem ter seus dados registrados na tabela:

```text
MXSRELATORIOCAMPANHAS
```

Essa tabela e usada para apuracao de campanhas progressivas.

---

## Fluxo de salvamento dos logs

O aplicativo chama o endpoint:

```text
SalvarLOGGERA
```

O endpoint insere o JSON recebido na tabela:

```text
MXSPEDIDOGERALOG
```

Essa tabela serve para analises futuras e auditoria.

### Estrutura da MXSPEDIDOGERALOG

| Coluna | Descricao |
| --- | --- |
| ID | Identificador do registro gerado automaticamente |
| CODUSUARIO | Codigo do usuario que enviou o JSON de log |
| CODPEDIDO | `ID_PEDIDO` ou `NUMPEDRCA` do pedido enviado para o sistema GERA |
| LOG_JSON | JSON recebido pela APK pelo GERA |
| DATA | Data de insercao do registro na nuvem |

---

## Parametros do fluxo

Ambos os fluxos sao habilitados pelo parametro:

```text
HABILITA_SISTEMA_GERA
```

Demais parametros:

| Parametro | Uso |
| --- | --- |
| HABILITA_SISTEMA_GERA | Permite habilitar o fluxo na APK |
| GUID_DISTRIBUIDOR_GERA | Identificador GUID do cliente no sistema GERA; usado pela APK |
| FUNCTION_KEY_GERA | Key do cliente no sistema GERA; usada pela APK |

---

## Regras de negocio

- Somente pedidos com a flag `UsandoSistemaGera` habilitada devem seguir este fluxo.
- Pedidos aguardando retorno do GERA devem permanecer bloqueados na nuvem.
- Todos os retornos do GERA devem ser armazenados para referencia e auditoria.
- Pedidos com maxPag e que utilizaram sistema GERA devem ser integrados corretamente apos o retorno.

---

## Sugestao de testes

Testar:

- Pedidos com uso do sistema GERA.
- Pedidos sem uso do sistema GERA.
- Se o pedido permanece bloqueado enquanto aguarda processamento.
- Inserts na tabela de log do JSON obtido pelo sistema GERA.
- Salvamento dos produtos com flag habilitada na tabela `MXSRELATORIOCAMPANHAS`.
- Pedidos com maxPag.
- Pedidos sem maxPag.
- Para pedidos maxPag, testar tambem pedidos com e sem itens bonificados.

---

## Projetos envolvidos

- ServerPDV / APIVendas.
- APIResumo.
- APITimeline.

---

## Exemplo de JSON de log - estrutura geral

A estrutura abaixo representa um exemplo de payload para armazenamento em `MXSPEDIDOGERALOG`. Os principais campos sao:

```json
{
  "gatewayOrder": 77,
  "erpOrderCode": null,
  "creatorSystemOrderCode": "16000730",
  "creatorSystemOrderVersion": "62e282d4-8726-48c7-b3ee-efb80fa36ca1",
  "totalOriginalPriceValue": 400.0,
  "totalFinalPriceValue": 370.0,
  "items": [],
  "gifts": [],
  "industryPromotionDetails": [],
  "promotions": {},
  "blacklistProducts": [],
  "industryItemsOutsidePortfolios": null,
  "industryItemsOutsidePrices": null,
  "industryItemsOutsideQuota": null,
  "statusDetail": [],
  "messages": []
}
```

### Itens do pedido no exemplo

O exemplo possui quatro itens no pedido:

| distributorItemNumber | EAN | Quantidade | Preco original | Preco final |
| --- | --- | --- | --- | --- |
| 8 | 87891024021637 | 1 | 100.0 | 100.0 |
| 6 | 87891528016504 | 1 | 100.0 | 90.0 |
| 4 | 87891528016498 | 1 | 100.0 | 90.0 |
| 2 | 87891528016511 | 1 | 100.0 | 90.0 |

### Descontos por item no exemplo

O exemplo mostra descontos de `10%` com `promotionCode = 109` para:

| distributorItemNumber | EAN | Tipo | Valor | Codigo da promocao |
| --- | --- | --- | --- | --- |
| 6 | 87891528016504 | `%` | 10.0 | 109 |
| 4 | 87891528016498 | `%` | 10.0 | 109 |
| 2 | 87891528016511 | `%` | 10.0 | 109 |

---

## Promocao adquirida - codigo 109

Codigo:

```text
109
```

Nome:

```text
[Demo] Lancamento Escova Dental - Compre e ganhe 10% de desconto na familia Higiene Oral
```

Descricao:

```text
Ao comprar as escovas dentais Original Macia, Original Media e Original Dura no pedido, ganhe 10% de desconto em qualquer produto da familia Higiene Oral.
Desconto sera aplicado ate R$500 em compras de produtos da familia Higiene Oral.
```

Requisitos:

```text
requirementsMinimum = 3
requirementsTotal = 3
```

Produtos exigidos:

| targetCode | targetType | targetName | value | valueType | acquired |
| --- | --- | --- | --- | --- | --- |
| 87891528016498 | Product | ESCOVA DENTAL ORIGINAL MACIA 1x | 1.0 | Items | true |
| 87891528016504 | Product | ESCOVA DENTAL ORIGINAL MEDIA 1x | 1.0 | Items | true |
| 87891528016511 | Product | ESCOVA DENTAL ORIGINAL DURA 1x | 1.0 | Items | true |

Premio/desconto:

| Campo | Valor |
| --- | --- |
| awards.value | 10.0 |
| awards.valueType | `%` |
| awards.type | Discount |
| awards.targetType | ProductLine |
| awards.targetCode | 3 |
| awards.targetName | Higiene Oral |
| discountLimit | 500.0 |
| discountLimitOrderValue | 300.0 |

---

## Promocoes progressivas do exemplo

O JSON contem tres faixas progressivas.

| Codigo | Nome | Requisito minimo | Total de requisitos | Desconto | Limite minimo | Limite maximo |
| --- | --- | --- | --- | --- | --- | --- |
| 105 | Desconto Progressivo - ative a faixa de 7% de desconto | 10 | 10 | 7% | 300.0 | 10000.0 |
| 106 | Desconto Progressivo - ative a faixa de 5% de desconto | 8 | 10 | 5% | 300.0 | 10000.0 |
| 107 | Desconto Progressivo - ative a faixa de 3% de desconto | 6 | 10 | 3% | 300.0 | 10000.0 |

Descricoes:

- Codigo 105: ao ativar as 10 familias participantes da campanha, ganha 7% de desconto em produtos Gera. Campanha valida a partir de R$300,00 em compras de produtos das familias ate o limite de R$10.000.
- Codigo 106: ao ativar 8 familias participantes da campanha, ganha 5% de desconto em produtos Gera. Campanha valida a partir de R$300,00 em compras de produtos das familias ate o limite de R$10.000.
- Codigo 107: ao ativar 6 familias participantes da campanha, ganha 3% de desconto em produtos Gera. Campanha valida a partir de R$300,00 em compras de produtos das familias ate o limite de R$10.000.

### Familias de produto usadas nas promocoes progressivas

| targetCode | targetType | targetName | value | valueType |
| --- | --- | --- | --- | --- |
| 5 | ProductLine | Desinfetante | 1.0 | Items |
| 6 | ProductLine | Lava Roupas | 1.0 | Items |
| 7 | ProductLine | Limpadores Gerais | 1.0 | Items |
| 8 | ProductLine | Creme dental | 1.0 | Items |
| 9 | ProductLine | Enxaguante bucal | 1.0 | Items |
| 10 | ProductLine | Escovas | 1.0 | Items |
| 12 | ProductLine | Sabonetes | 1.0 | Items |
| 14 | ProductLine | Cuidado Feminino | 1.0 | Items |
| 15 | ProductLine | Shampoo | 1.0 | Items |
| 16 | ProductLine | Condicionadores | 1.0 | Items |

### Itens adquiridos nas promocoes progressivas do exemplo

O exemplo marca como adquiridos:

- `targetCode = 5`, `targetName = Desinfetante`, com produto `87891024021637`, preco original `100.0`, preco final `100.0`.
- `targetCode = 10`, `targetName = Escovas`, com produto `87891528016511`, preco original `100.0`, preco final `90.0`.

Os demais targetCodes aparecem como `acquired = false` em pelo menos uma das faixas.

### Requisitos faltantes no exemplo

O JSON possui blocos `partial.missingRequirements` com `missingValue = 1.0`, `valueType = Items` e `logicOperator = And` para familias nao adquiridas.

Para a faixa de codigo 105, os requisitos faltantes indicam `minimumNecessaryRequiriments = null` para:

- `6` Lava Roupas.
- `7` Limpadores Gerais.
- `8` Creme dental.
- `9` Enxaguante bucal.
- `12` Sabonetes.
- `14` Cuidado Feminino.
- `15` Shampoo.
- `16` Condicionadores.

Para a faixa de codigo 106, os requisitos faltantes indicam `minimumNecessaryRequiriments = 6` para:

- `6` Lava Roupas.
- `7` Limpadores Gerais.
- `8` Creme dental.
- `9` Enxaguante bucal.
- `12` Sabonetes.
- `14` Cuidado Feminino.
- `15` Shampoo.
- `16` Condicionadores.

Para a faixa de codigo 107, os requisitos faltantes indicam `minimumNecessaryRequiriments = 4` para:

- `6` Lava Roupas.
- `7` Limpadores Gerais.
- `8` Creme dental.
- `9` Enxaguante bucal.
- `12` Sabonetes.
- `14` Cuidado Feminino.
- `15` Shampoo.
- `16` Condicionadores.

---

## Dados de industria e retorno

O exemplo mostra:

```json
{
  "industryId": 8,
  "industry": "Industria Gera VI",
  "industryType": 0,
  "industryDocument": {
    "type": 5,
    "document": ""
  }
}
```

Em `statusDetail`, o retorno possui:

```json
{
  "httpStatusCode": 200,
  "message": "",
  "industryId": 8,
  "industry": "Industria Gera VI",
  "industryType": 0,
  "industryDocument": {
    "type": 5,
    "document": "07168005000177"
  }
}
```

Em `messages`, o retorno possui:

```json
{
  "messageCode": "PROCESSED",
  "message": null,
  "messageParameter": null
}
```

---

## Campos tecnicos relevantes do JSON

Campos e significados para busca no RAG:

| Campo | Significado |
| --- | --- |
| gatewayOrder | Pedido no gateway GERA |
| erpOrderCode | Codigo do pedido no ERP; exemplo nulo |
| creatorSystemOrderCode | Codigo do pedido no sistema criador |
| creatorSystemOrderVersion | Versao/id de controle do pedido enviado |
| totalOriginalPriceValue | Valor original total do pedido |
| totalFinalPriceValue | Valor final total apos desconto |
| items | Itens do pedido |
| gifts | Brindes |
| giftsToChoose | Brindes disponiveis para escolha |
| industryPromotionDetails | Detalhes de promocao por industria |
| promotions.acquired | Promocoes adquiridas |
| promotions.partial | Promocoes parcialmente atendidas |
| promotions.notAcquired | Promocoes nao adquiridas |
| acquiredProducts | Produtos que atenderam o requisito |
| missingRequirements | Requisitos faltantes |
| awards | Premios/descontos concedidos |
| blacklistProducts | Produtos bloqueados |
| industryItemsOutsidePortfolios | Itens fora de portfolio |
| industryItemsOutsidePrices | Itens fora de preco |
| industryItemsOutsideQuota | Itens fora de cota |
| statusDetail | Status detalhado do retorno por industria |
| messages | Mensagens gerais do retorno |
