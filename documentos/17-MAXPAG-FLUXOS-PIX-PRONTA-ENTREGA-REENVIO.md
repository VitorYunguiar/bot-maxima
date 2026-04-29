# Fluxos maxPag - PIX, Pronta Entrega e Reenvio de Pedidos Pagos

> Documento preparado para ingestao em banco vetorial (RAG).
> Fontes originais:
> - `C:\Users\vitor\Downloads\MXPEDDV-101181 - Baixa automatica de titulos PIX não sendo realizada.pdf`
> - `C:\Users\vitor\Downloads\MXPEDDV-111871 - Fluxo reenvio de pedidos maxPag já pagos.pdf`
> - `C:\Users\vitor\Downloads\MXPEDDV-112014 - Movimentação de estoque Pronta Entrega com MaxPag.pdf`
> Tickets: MXPEDDV-101181 | MXPEDDV-111871 | MXPEDDV-112014
> Data de extracao: 2026-04-29
> Sistema: maxPag | maxPayment | maxPedido | Extrator | IntPDV | Winthor
> Area: Pagamentos | PIX | Titulos | Estoque | Pronta Entrega | Reenvio de pedidos

---

## Sobre este documento

Este documento consolida tres fluxos relacionados a maxPag/maxPayment:

- Baixa automatica de titulos PIX do maxPedido.
- Reenvio de pedidos maxPag ja pagos que foram barrados por horario de importacao.
- Movimentacao de estoque de Pronta Entrega apenas apos pagamento pelo maxPayment.

Palavras-chave: maxPag, maxPayment, PIX, baixa automatica, JOB_BAIXA_TITULOS, MXSBAIXATITULOS, MXSBAIXATITULOSCONF, PCPREST, PCMXSMAXPAYMENT, PCMOVCR, PCESTCR, PCMXSLOGERROS, VALIDAR_HORARIO_IMPORTACAO_PEDIDO, VALIDAR_MAXPAG_HORARIO_IMPORTACAO, PCPERIODOIMPORTACAOPEDIDOS, AguardandoLinkMaxPayment, Pronta Entrega, MXSCONTROLEVENDAS, DATAMAXPAYMENT, DadosProntaEntrega.

---

## 1. Baixa automatica de titulos PIX nao realizada

Ticket: MXPEDDV-101181.

### Causa

Havia validacao incorreta dos vinculos necessarios para dar baixa automatica nos titulos PIX do maxPedido.

O extrator tinha uma restricao em que os titulos so seriam baixados caso o codigo do banco do titulo ja estivesse preenchido. Essa validacao estava incorreta, porque a propria baixa e responsavel por preencher o codigo do banco.

Como consequencia, o fluxo nao era executado e a baixa automatica nao era realizada.

### Projetos alterados

- Central de Configuracoes.
- Atualizador.
- IntPDV.
- Extrator.

---

## 1.1 Configuracao de cobranca para baixa automatica

Para o fluxo funcionar, deve-se configurar a cobranca do maxPag que sera usada para baixa automatica.

Caminho:

```text
Central de Configuracoes > maxPag > Cobrancas > Cadastrar a cobranca
```

Observacoes:

- O campo filial token se refere as filiais que possuem token do maxPag configurado.
- Os dados de configuracao sao salvos na tabela `MXSBAIXATITULOSCONF` na nuvem.
- O cadastro e de apenas uma cobranca por filial.
- Todos os campos sao obrigatorios no cadastro.

### Parametro obrigatorio

Depois de configurar a cobranca, habilitar o parametro:

```text
JOB_BAIXA_TITULOS
```

Apos habilitar o parametro, reiniciar o extrator do cliente para que ele obtenha a nova configuracao e habilite a job.

### Evidencia visual do PDF

O print da Central mostra a tela de cobrancas com a area maxPag, campos de configuracao e indicacao visual para habilitar o parametro `JOB_BAIXA_TITULOS`.

---

## 1.2 Fluxo da baixa automatica PIX

O processo e feito via job executada a cada 5 minutos.

Fluxo:

1. O extrator monitora titulos para baixa.
2. O extrator obtem os titulos elegiveis para baixa.
3. O IntPDV insere os titulos na tabela `MXSBAIXATITULOS` na nuvem.
4. Os registros ficam disponiveis para baixa.
5. O processo de baixa tambem e executado pelo extrator via job a cada 5 minutos.
6. Ao buscar titulos para baixa, o extrator procura registros na `MXSBAIXATITULOS` com status `0` ou `2`.
7. Quando a baixa automatica e realizada, sao preenchidas as colunas `CODBANCO`, `CODMOEDA`, `VPAGO` e `DTPAG` da `PCPREST`.

### Status da MXSBAIXATITULOS

| Status | Significado |
| --- | --- |
| 0 | Titulo pendente para baixa |
| 2 | Titulo pendente recebido no ERP |
| 4 | Titulo baixado com sucesso |
| 5 | Erro ao baixar titulo |

---

## 1.3 Regras para titulo ficar disponivel para baixa

So ficam disponiveis titulos para baixa quando todas as condicoes abaixo forem atendidas:

- Pedido foi faturado: `PCPEDC.POSICAO = 'F'`.
- Forma de pagamento foi Pix do maxPag: `PCMXSMAXPAYMENT.FORMAPAGTO = 3`.
- Possui apenas uma prestacao: `PCPREST.PREST = 1`.
- Valor do titulo e igual ao valor da nota: `SAID.VLTOTAL = PCPREST.VALOR`.
- Titulo ainda nao foi baixado: `PCPREST.DTPAG IS NULL`.

### Consulta executada pelo extrator

Execute no banco local para validar as regras:

```sql
SELECT
  PAY.ID_PEDIDO,
  PREST.NUMTRANSVENDA,
  PREST.PREST,
  PREST.CODBANCO,
  COB.CODMOEDA,
  PAY.CODNSU,
  CAPA.CODFILIAL,
  PREST.VALORMULTA,
  PREST.VALOR,
  CAPA.CODCOB
FROM PCMXSMAXPAYMENT PAY
INNER JOIN PCPEDC CAPA ON PAY.NUMPED = CAPA.NUMPED
INNER JOIN PCPREST PREST ON PREST.NUMTRANSVENDA = CAPA.NUMTRANSVENDA
INNER JOIN PCCOB COB ON COB.CODCOB = CAPA.CODCOB
INNER JOIN PCNFSAID SAID ON CAPA.NUMTRANSVENDA = SAID.NUMTRANSVENDA
WHERE PAY.FORMAPAGTO = 3
  AND NVL(ERRO, 'N') = 'N'
  AND PREST.PREST = 1
  AND CAPA.POSICAO = 'F'
  AND SAID.VLTOTAL = PREST.VALOR
  AND PREST.DTPAG IS NULL;
```

---

## 1.4 Consultas de verificacao da baixa

Use as consultas abaixo para verificar se o processo ocorreu com sucesso ao salvar.

### Verificar PCESTCR

```sql
SELECT VALOR, PCESTCR.*
FROM PCESTCR
WHERE CODBANCO = :CODBANCO
  AND CODCOB = :CODCOB;
```

### Verificar PCMOVCR

```sql
SELECT *
FROM PCMOVCR
WHERE CODBANCO = :CODBANCO
  AND CODCOB = :CODCOB
ORDER BY DATA DESC;
```

### Verificar PCPREST

```sql
SELECT VPAGO, DTPAG, CODBANCO, PCPREST.*
FROM PCPREST
WHERE NUMTRANSVENDA = :NUMTRANSVENDA;
```

### Verificar logs

```sql
SELECT *
FROM PCMXSLOGERROS
WHERE TRGNAME = 'BAIXA TITULOS'
ORDER BY DTERRO DESC;
```

---

## 1.5 Campos da MXSBAIXATITULOS

A tabela `MXSBAIXATITULOS` e preenchida pelo IntPDV com os dados enviados pelo extrator e vinculados aos dados salvos pela Central.

| Campo | Descricao |
| --- | --- |
| ID | Valor gerado automaticamente |
| STATUS | Status do titulo para baixa; por padrao salva 0; em erro preenche 5 e `MSG_RETORNO` |
| APP_MAXIMA | Aplicativo que preencheu a linha; no cenario, `MAXPEDIDO-INTPDV` |
| IDMAXPAYMENT | Id do pagamento via maxPag do pedido |
| CODFILIAL | Codigo da filial do pedido |
| NUMTRANSVENDA | Numero da transacao do titulo |
| PREST | Prestacao |
| CODBANCO | Codigo do banco configurado na Central baseado na cobranca e filial |
| CODMOEDA | Codigo da moeda configurado na Central baseado na cobranca e filial |
| NSU | NSU do pagamento |
| DATA | Data em que o registro foi enviado |
| DATA_TRANSFERENCIA | Data em que o registro foi enviado |
| VALOR_JUROS | Valor de juros |
| VALOR_MULTA | Valor da multa |
| VALOR_PAGO | Valor pago no titulo |
| MSG_RETORNO | Mensagem de retorno em caso de erro ao baixar |
| TOKENMAXPAYMENT | Token do maxPay usado para passar o pedido |
| CODCOB_BAIXA | Codigo da cobranca que sera dado baixa no titulo |

### Causas comuns quando o titulo nao baixa

- Parametro `JOB_BAIXA_TITULOS` nao foi habilitado.
- Parametro `JOB_BAIXA_TITULOS` foi habilitado, mas o extrator nao foi reiniciado.
- Titulo nao passou nas regras do extrator.
- Nao existe configuracao de cobranca cadastrada.

---

## 2. Reenvio de pedidos maxPag ja pagos

Ticket: MXPEDDV-111871.

### Causa

Antes, ao reenviar um pedido maxPag, sempre era gerado um novo link de pagamento, mesmo quando o pagamento ja havia sido realizado.

### Analise

O reenvio de pedidos maxPag gerava automaticamente um novo link sempre que a flag `VendaCartaoCredito` estava habilitada, independentemente do pagamento ja ter sido realizado.

Consequencia:

1. Pedido pago era barrado pelo Winthor por estar fora do horario permitido.
2. RCA tentava reenviar o pedido.
3. Um novo link era criado desnecessariamente.
4. O cliente precisaria pagar novamente para que o pedido fosse integrado.
5. O valor anterior ficaria sem estorno.

### Parametros do fluxo

Habilitar:

```text
VALIDAR_HORARIO_IMPORTACAO_PEDIDO
```

Parametro ja existente no fluxo de validacao do extrator. E necessario reiniciar o extrator.

Habilitar tambem:

```text
VALIDAR_MAXPAG_HORARIO_IMPORTACAO
```

Parametro novo usado para definir se o fluxo sera habilitado e garantir retrocompatibilidade na APK. E necessario reiniciar o extrator.

### Configuracao de horarios no Winthor

Configurar horarios de envio de pedido no Winthor, tabela:

```text
PCPERIODOIMPORTACAOPEDIDOS
```

Tambem existe validacao na `PCFILIAL`, mas ela ocorre apenas se houver erro na leitura da `PCPERIODOIMPORTACAOPEDIDOS`, por exemplo:

- Tabela nao existe.
- Valores invalidos.

Observacao: a configuracao deve ser feita no Winthor. Na configuracao da Maxima, o pedido nao chega a ser salvo e, portanto, nao entra no fluxo.

### Fluxo de teste e comportamento

1. Enviar um pedido maxPag, Pix ou cartao, fora do horario configurado.
2. Pagar o pedido fora do horario configurado.
3. O pedido sera integrado.
4. Por estar fora do horario, retornara a critica:

```text
Atencao. O horario de recebimento de pedidos e XX:XX as YY:YY. O pedido nao foi salvo no sistema. Por favor, reenvie o pedido em um horario valido.
```

5. A critica retorna com `TipoCritica = 51`.
6. Em um horario permitido, reenviar o pedido.
7. O pedido entra novamente no fluxo de integracao.
8. O pedido reenviado deve usar o mesmo link de pagamento ja pago.

### Regra de negocio

- Utilizar o mesmo link de pagamento para o pedido reenviado em horario valido.
- Garantir que o pedido seja integrado corretamente.
- Validar pedido enviado fora do horario configurado no Winthor.
- Aplicar apenas a este cenario.

### Projetos envolvidos

- ServerPDV / APIVendas.
- IntPDV.
- Extrator.
- ApiTimeline.
- ApiResumo.

---

## 3. Movimentacao de estoque Pronta Entrega com maxPayment

Ticket: MXPEDDV-112014.

### Causa

Ao enviar um pedido Pronta Entrega com pagamento realizado por maxPayment, o estoque de Pronta Entrega era movimentado antes do pagamento. Se o pedido fosse cancelado ou o link expirasse, o estoque nunca era estornado.

### Analise

O estoque era movimentado no salvamento do pedido, e nao quando o pedido era pago.

O fluxo foi alterado para que o estoque seja movimentado somente quando o pedido for pago, garantindo movimentacao correta e evitando estoque baixado para pedido nao pago.

### Fluxo correto

1. Criar pedido Pronta Entrega com `tipos/condvenda` igual a `14`, `15` ou `24`.
2. Enviar o pedido com pagamento pelo maxPayment.
3. Salvar o pedido.
4. Ate esse momento nao deve ocorrer movimentacao do estoque em `MXSCONTROLEVENDAS`.
5. Pagar o pedido pelo link.
6. Somente apos o pagamento, o estoque sera movimentado.
7. Se o link expirar ou for cancelado, o estoque nao deve ser movimentado.

### Validade e cancelamento de link

- A validade do link maxPayment e definida pelo parametro `VALIDADE_LINK_MAXPAYMENT`, em horas.
- O padrao e 7 dias de validade.
- O link pode ser cancelado pelo painel do maxPag quando o link esta apenas gerado.

### Detalhes tecnicos

Os dados dos produtos que serao movimentados no Pronta Entrega estao salvos na coluna `DATAMAXPAYMENT`, que esta criptografada.

As informacoes estao na propriedade `DadosProntaEntrega` e sao recuperadas apos o pedido ser pago, evento recebido via mensageria.

### Regra de negocio

- Movimentar estoque quando pedido com maxPag for pago.
- Evitar movimentacoes incorretas do estoque do Pronta Entrega.

### Sugestao de testes

- Pedidos Pronta Entrega.
- Pedidos normais.
- Pedidos com link maxPag.
- Pedidos sem link maxPag.
- Cancelamento de links maxPag.
- Expiracao de links maxPag.
- Validar tanto pedidos Pronta Entrega quanto pedidos normais.

### Projeto envolvido

- ServerPDV / APIVendas.

