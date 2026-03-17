# Revisão de Fluxo: MaxPedido + MaxPag

## Fonte
- Fluxograma técnico apresentado pelo time de desenvolvimento (Back-end MaxPedido)
- Documento interno consolidado para suporte e desenvolvimento
- Bibliotecas:
  - https://biblioteca.maximatech.com.br/display/MS/Documento+de+suporte+maxPag
  - https://basedeconhecimento.maximatech.com.br/display/BMX/Como+trabalhar+com+o+maxPag

---

## Metadados

- Tipo detectado: `documentação funcional + técnica`
- Domínio: `Financeiro / Integração ERP / Mensageria`
- Natureza do fluxo: `Assíncrono`
- Dependências:
  - Mensageria (fila)
  - JOBs de Extração
  - Banco Local
  - Banco Nuvem
  - Operadora de pagamento
- Ambiente executado em: `Cluster de servidores`

---

## Objetivo do Documento

Este documento consolida o fluxo completo do MaxPag desde a criação do pedido até:

- Faturamento no ERP
- Cancelamento do pedido
- Estorno ou captura financeira

A visão é estruturada para:

- Diagnóstico de tickets
- Identificação de falhas (local, nuvem ou mensageria)
- Entendimento técnico do fluxo assíncrono

---

# Conhecimento Extraído

---

# 1. Início do Fluxo – APK (MaxPedido)

[etapa] O pedido é criado na APK.

[condição] Deve ser selecionado o tipo de cobrança vinculado ao MaxPag:

- PIX (vinculado ao MaxPag)
- Cartão de Crédito (vinculado ao MaxPag)

⚠️ Observação:
Existem formas de pagamento PIX e Cartão que **não utilizam o MaxPag**.  
A configuração correta deve estar vinculada à biblioteca do MaxPag.

---

# 2. Validação no Server PDV

[processo] O pedido é enviado ao Server PDV.

[validações]
- Regras comerciais
- Horário de operação
- Limite de crédito
- Regras fiscais

---

## 2.1 Autorização Prévia (Antes do MaxPag)

Se o pedido exigir autorização (ex: desconto):

- Server envia pedido ao MaxGestão
- Aguarda retorno
- Se autorizado → fluxo continua
- Se bloqueado → fluxo interrompido

⚠️ Essa etapa ocorre antes da geração do link de pagamento.

---

# 3. Geração do Link – MaxPag

[etapa] Server PDV solicita geração do link ao MaxPag.

[integracao]
- MaxPag comunica-se com a operadora
- Operadora valida e retorna
- MaxPag gera link

[mensageria]
- Evento é publicado em fila
- Qualquer servidor do cluster pode consumir

⚠️ O ambiente roda em cluster.
O consumo da fila pode ocorrer por qualquer instância ativa.

---

# 4. Crítica do Link – Server PDV

[processamento]
- Server consome evento da fila
- Registra link
- Envia crítica para APK
- Atualiza status para:

    Aguardando Pagamento

---

# 5. Pagamento pelo Cliente

[ação]
- RCA realiza swipe na APK
- Cliente recebe link
- Efetua pagamento

[estado]
A partir deste momento, o sistema apenas aguarda retorno da operadora.

---

# 6. Confirmação de Pagamento – MaxPag

Após pagamento:

[PIX]
- Autorização direta

[Cartão]
- Pré-autorização

[evento]
- MaxPag publica evento na mensageria
- Server PDV processa confirmação

[efeitos]
- Atualiza status do pedido
- Gera registros financeiros
- Notifica APK

Estado final desta etapa:

    Aguardando integração no ERP

---

# 7. JOB Extrator – Integração ERP

## Parâmetros de Controle

- ATIVAR_JOBMAXPAG_EXTRATOR
- PERMITIR_VENDA_CARTAO_CREDITO
- AMBIENTE_MAXPAYMENT (0=Hmg / 1=Prod)

---

## Função do JOB

[job]
Busca pedidos:

- Autorizados
- Pré-autorizados
- Ainda não integrados

---

## Integração Técnica

[consulta]
Int-PDV acessa:

- Banco de Dados Nuvem

⚠️ Diagnóstico importante:
Erros podem estar em:

- Banco Local
- Banco Nuvem
- Endpoint de integração
- Fila de mensageria

---

## Envio ao ERP

[processo]
- Extrator envia pedidos
- ERP passa a reconhecer pedido oficialmente

---

# 8. Monitoramento Pós-ERP

Um novo JOB monitora:

- Pedidos faturados
- Pedidos cancelados

Verifica se fluxo financeiro no MaxPag foi finalizado.

---

# 9. Cenários Pós-ERP

---

## 9.1 Pedido Cancelado

[ação]
Extrator solicita via Int-PDV:

- Cancelamento
- Estorno
- Cancelamento de pré-autorização

[MaxPag executa]
- Estorno total
ou
- Cancelamento de pré-autorização

[evento]
Atualização publicada via mensageria.

---

## 9.2 Pedido Faturado

Verifica:

Houve corte?

---

### Não Houve Corte

PIX:
- Finaliza sem estorno

Cartão:
- Captura total
- Pré-autorizado → Autorizado

---

### Houve Corte

PIX:
- Estorno parcial dos itens cortados

Cartão:
Se valor atendido < valor total:

- Captura parcial
- Cancelamento do saldo da pré-autorização

Observação importante:

No cartão de crédito, quando ocorre captura parcial, o valor excedente é liberado automaticamente pela operadora no limite do cliente.  
Não existe estorno adicional.

---

# 10. Pontos de Diagnóstico (Suporte / Dev)

Ao analisar um ticket, verificar:

1. Pedido foi autorizado no MaxGestão?
2. Link foi gerado pelo MaxPag?
3. Evento entrou na fila?
4. Server consumiu evento?
5. Confirmação de pagamento foi publicada?
6. JOB Extrator está ativo?
7. Pedido foi enviado ao ERP?
8. ERP retornou faturado ou cancelado?
9. Estorno/captura foi executado?

---

# 11. Tabelas para Análise

- MXSMAXPAYMENTMOV
- MXSINTEGRACAOPEDIDO_LOGST

Boa prática:

Comparar:

- Data da movimentação financeira
- Data de mudança de status do pedido

---

# 12. Resumo Executivo do Fluxo

1. Pedido criado
2. Validação
3. Autorização (se necessário)
4. Geração de link
5. Pagamento
6. Confirmação financeira
7. Integração ERP
8. Faturamento ou cancelamento
9. Ajuste financeiro (captura ou estorno)

---

# 13. Encerramento

O fluxo é finalizado quando:

- Server PDV registra as últimas movimentações
- MaxPag conclui captura ou estorno
- ERP consolida status final
