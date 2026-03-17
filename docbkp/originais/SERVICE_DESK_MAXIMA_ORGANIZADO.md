# SERVICE DESK MAXIMA TECH - PROCESSOS MAXPEDIDO

**Data de Criação:** 12 de fevereiro de 2026  
**Documento Original:** SERVICE DESK MAXIMA TECH PROCESSOS.docx  
**Status:** Reorganizado e estruturado

---

## 📋 SUMÁRIO

1. [Visão Geral do MaxPedido](#visão-geral)
2. [Tabelas Úteis do Banco](#tabelas-úteis)
3. [Status e Fluxo de Pedidos](#status-e-fluxo)
4. [Integração de Pedidos](#integração)
5. [Parametrização Central](#parametrização)
6. [Gestão de Clientes](#gestão-de-clientes)
7. [Descontos e Políticas](#descontos-políticas)
8. [Conta Corrente](#conta-corrente)
9. [Produtos e Catálogo](#produtos-catálogo)
10. [Relatórios](#relatórios)
11. [Checkin/Checkout e Localização](#checkin-checkout)
12. [Erros e Resoluções](#erros-resoluções)
13. [Infra: Docker, Portainer e Hangfire](#infra)
14. [Referências e Links](#referências)

---

<a name="visão-geral"></a>
## 1️⃣ VISÃO GERAL DO MAXPEDIDO

### O que é MaxPedido?

MaxPedido é um aplicativo mobile de força de vendas que se espelha na **rotina 316 do Winthor** (Pedido de Vendas). Funciona baseado nas funcionalidades dessa rotina, permitindo que vendedores façam vendas diretamente do aparelho celular com integração ao ERP.

### Ecossistema Maxima

| Ferramenta | Descrição | Tipo |
|-----------|-----------|------|
| **MaxPedido** | App mobile para vendas | APK |
| **MaxGestão** | Portal Web e APP para gestores/administradores | Web + APP |
| **MaxPromotor** | Portal Web e APP para pesquisas e dashboards | Web + APP |
| **MaxCatalogo** | APP para exibir produtos | APK |
| **Winthor** | ERP para gestão de vendas | Software |

### Arquitetura de Integração

```
MaxPedido (APK)
    ↓
Nuvem (MXSINTEGRACAOPEDIDO)
    ↓
ERP (Winthor ou O'ERP)
    ↓
Banco Local
```

### Requisitos Mínimos do MaxPedido

📌 [Veja documentação oficial](https://maximatech.com.br/requisitos)

---

<a name="tabelas-úteis"></a>
## 2️⃣ TABELAS ÚTEIS DO BANCO

### Tabelas Principais de Pedidos

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSINTEGRACAOPEDIDO** | Pedidos feitos na APK | Nuvem |
| **MXSINTEGRACAOPEDIDO_LOGST** | Log dos pedidos (status e tempo) | Nuvem |
| **MXSINTEGRACAOPEDIDOLOG** | Log do JSON dos pedidos | Nuvem |
| **MXSHISTORICOCRITICA** | Históricos de críticas dos pedidos | Nuvem |
| **MXSPEDIDO** | Pedidos na nuvem | Nuvem |
| **PCPEDI** / **PCPEDC** | Pedidos no Winthor | Local |

### Tabelas de Configuração e Parâmetros

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSPARAMETRO** | Parâmetros da Central de Configurações | Nuvem |
| **MXSPARAMETROVALOR** | Parâmetros por usuário | Nuvem |
| **MXSCONFIGERP** | Configurações do ERP | Nuvem |
| **PCMXSCONFIGURACOES** | Configurações do banco local | Local |

### Tabelas de Cadastro

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSCLIENT** | Clientes | Nuvem |
| **MXSUSUARIOS** | Usuários Máxima | Nuvem |
| **MXSUSURCLI** | Vínculo RCA/Cliente | Nuvem |
| **ERP_MXSUSURCLI** | Vínculo RCA/Cliente (ERP) | Nuvem |
| **MXSATIVI** | Ramo de atividade | Nuvem |

### Tabelas de Estoque

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSEST** | Estoque | Nuvem |
| **MXSESTCESTA** | Estoque por cesta | Nuvem |
| **MXSESTFILIAL** | Estoque por filial | Nuvem |
| **MXSVALIDADEWMS** | Validade WMS dos produtos | Nuvem |
| **MXSLOTE** | Lotes de produtos | Nuvem |

### Tabelas de Preço

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSTABPR** | Tabela de preços | Nuvem |
| **MXSPRECOPROM** | Promoção de preço fixo | Nuvem |
| **MXSTABPRCLI** | Tabela de preço por cliente | Nuvem |
| **MXSTABPRCESTA** | Tabela de preço cesta | Nuvem |
| **MXSEMBALAGEM** | Embalagem dos produtos | Nuvem |

### Tabelas de Campanhas e Descontos

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSDESCONTOC** | Campanha desconto (cabeçalho) | Nuvem |
| **MXSDESCONTOI** | Campanha desconto (itens) | Nuvem |
| **MXSCAMPANHAFAMILIA** | Campanha de desconto progressivo | Nuvem |
| **MXSCAMPANHAFAIXAS** | Faixas de desconto da campanha | Nuvem |

### Tabelas de Financeiro

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSTITULOSABERTOS** | Títulos abertos do cliente | Nuvem |
| **ERP_MXSPREST** | Títulos abertos (sync ERP) | Nuvem |
| **MXSMAXPAYMENTMOV** | Movimentações do maxPag | Nuvem |

### Tabelas de Conta Corrente

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSCONFIGERP** | Configuração de tipo de movimentação CC | Nuvem |

### Tabelas de Localização e Roteiros

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSCOMPROMISSOS** | Roteiro de visitas | Nuvem |
| **MXSHISTORICOCOMPROMISSOS** | Backup de compromissos | Nuvem |
| **ERP_MXSROTACLI** | Roteiro cliente (ERP) | Nuvem |
| **MXSLOCATION** | Checkin/checkout (SQLite) | Local |

### Tabelas de Sincronização

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSAPARELHOSCONNLOG** | Última sincronização RCA | Nuvem |
| **MXSCONEXOES** | Conexões do RCA | Nuvem |
| **MXSTABELA** | Tabelas sincronizáveis | Nuvem |

---

<a name="status-e-fluxo"></a>
## 3️⃣ STATUS E FLUXO DE PEDIDOS

### Status da MXSINTEGRACAOPEDIDO

| Status | Código | Descrição | Contexto |
|--------|--------|-----------|----------|
| **Recebido pelo Server** | 0 | Pedido na nuvem | Inicial |
| **Enviado para API** | 1 | Enviado para processamento | Transição |
| **Enviado para ERP** | 2 | Realizado GET na API | Transição |
| **Recebido pelo ERP** | 3 | ERP recebeu o pedido | Transição |
| **Processado pelo ERP** | 4 | Processamento sucesso | Sucesso |
| **Erro no Processamento** | 5 | Erro durante processamento | Erro |
| **Bloqueado para Envio** | 6 | Bloqueado no ERP | Bloqueio |
| **Cancelado Bloqueado** | 7 | Cancelamento do pedido bloqueado | Cancelamento |
| **Pendente Autorização** | 8 | Aguardando aprovação | Autorização |
| **Aprovado** | 9 | Pedido aprovado | Autorização |
| **Negado** | 10 | Pedido rejeitado | Autorização |
| **Gravado FV** | 11 | Job Winthor executado | Sucesso |
| **Cancelamento** | 12 | Cancelamento do pedido | Cancelamento |
| **Carregamento Não Importado** | 13 | Erro na importação | Erro |
| **Erro Integração ERP** | 14 | Erro na integração | Erro |
| **Cancelamento ERP** | 15 | Cancelamento no ERP | Cancelamento |

#### Status MaxPayment

| Status | Código | Descrição |
|--------|--------|-----------|
| Aguardando geração do link maxPayment | 16 | Processamento inicial |
| Erro ao gerar link | 17 | Erro |
| Aguardando utilização do link | 18 | Pendente |
| Falta de colunas para utilização | 19 | Validação |
| Erro ao processar solicitação | 20 | Erro |
| Em processamento | 21 | Processamento |
| Solicitação cancelada | 22 | Cancelamento |
| Validade do link incorreta | 23 | Validação |

### Status da MXSHISTORICOPEDC (Posição do Pedido)

| Posição | Código | Descrição | Status Associado |
|---------|--------|-----------|------------------|
| Pendente | P | Pendente no ERP | 7 |
| Liberado | L | Liberado no ERP | 8 |
| Bloqueado | B | Bloqueado no ERP | 9 |
| Montado | M | Montado no ERP | 10 |
| Faturado | F | Faturado no ERP | 11 |
| Cancelado | C | Cancelado no ERP | 12 |
| Orçamento | O | Orçamento no ERP | 13 |

### Fluxo Completo de Processamento

```
1. APK envia o pedido para a nuvem
   ↓
2. Server grava na MXSINTEGRACAOPEDIDO com status = 0
   ↓
3. ERP realiza GET (endpoint statuspedidos) para buscar pedidos
   ↓
4. API retorna GET → setamos status = 2 (ENVIADO PARA ERP)
   ↓
5. ERP realiza processamento internamente
   ↓
6. ERP realiza PUT com status 4 (sucesso) ou 5 (erro)
   ↓
7. ERP envia histórico com posição (L, F, M, etc.)
   ↓
8. APK faz swipe para atualizar timeline
   ↓
9. Server envia dados para atualização da timeline
```

---

<a name="integração"></a>
## 4️⃣ INTEGRAÇÃO DE PEDIDOS

### Layout de Integração

- **Winthor:** [Veja documentação TOTVS](https://tdn.totvs.com/pages/releaseview.action?pageId=348295209)
- **MaxPedido:** [Veja base de conhecimento](https://basedeconhecimento.maximatech.com.br/pages/viewpage.action?pageId=12189810)

### Tabelas de Gravação (FV)

Quando o MaxPedido grava um pedido, utiliza as seguintes tabelas:

| Tabela | Descrição |
|--------|-----------|
| **PCCLIENTFV** | Clientes FV |
| **PCPEDCFV** | Pedidos FV |
| **PCPEDIFV** | Itens do pedido FV |

Após validação, a integradora manda para as tabelas do ERP (PCCLIENT, PCPEDC, PCPEDI).

### Crítica da Integradora do Winthor

#### Cenário Comum

Cliente cadastra restrição de venda na rotina 391 com valor mínimo para plano de pagamento.

**Indicadores de Bloqueio:**
- Verifique o campo `OBSERVACAO_PC` na `PCPEDIFV`
- Se preenchido = pedido foi processado pela integradora e barrado
- Consulte `MXSHISTORICOCRITICA` para detalhes da rejeição

#### Campo Obrigatório: NOSSONUMBCO

Necessário para compartilhamento de boleto:
- Coluna `NOSSONUMBCO` na `ERP_MXSPREST` deve estar preenchida
- Coluna `LINHADIG` também deve estar preenchida

---

<a name="parametrização"></a>
## 5️⃣ PARAMETRIZAÇÃO CENTRAL

### Tipos de Dado dos Parâmetros

| Tipo | Código | Exemplo |
|------|--------|---------|
| Literal (Texto) | 1 | 'S', 'N', 'PRG' |
| Inteiro (Número) | 2 | 30, 100, 1800 |
| Lógico (Boolean) | 3 | 'S'/'N' |

### Parâmetros Essenciais por Funcionalidade

#### 🔐 Autenticação e Acesso

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `PRIMEIRA_IMPLANTACAO` | Lógico | Força envio de triggers ao banco local |

#### 📱 Sincronização

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `HABILITA_SINC_AUTOMATICA` | Lógico | Sincronização automática de dados |
| `BLOQUEIA_PED_FORA_JORNADA` | Lógico | Bloqueia pedidos fora da jornada |
| `VALIDA_FUSO_DATAAUTOMATICO` | Lógico | Valida fuso horário |
| `UTILIZA_CHECKIN_CHECKOUT` | Lógico | Habilita check-in/checkout |
| `GPS_EDGE_BLOCK` | Lógico | Valida cerca eletrônica |
| `GPS_EDGE_METERS_SIZE` | Inteiro | Raio da cerca eletrônica em metros |

#### 💰 Limite de Crédito

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `BLOQUEIA_PEDIDO_CLIENTE_SEMLIMITE` | Lógico | Bloqueia venda sem limite |
| `BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE` | Lógico | Bloqueia para inadimplentes |
| `NUMERO_DIAS_CLIENTE_INADIMPLENTE` | Inteiro | Dias máximos de inadimplência |
| `SOMACREDITOCLIPRINCIPAL` | Lógico | Soma crédito cliente principal |

#### 🏪 Cliente

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `HABILITA_PED_CLI_NAO_SINC` | Lógico | Permite pedido cliente não sincronizado |
| `HABILITA_PED_CLI_RECEM_CADASTRADO` | Lógico | Permite pedido cliente recém cadastrado |
| `FORCAR_ATUALIZACAO_CADASTRO_CLIENTE` | Lógico | Força atualização do cadastro |
| `DIAS_ATUALIZACAO_CADASTRO_CLIENTE` | Inteiro | Dias para validar atualização |
| `DESABILITA_CADASTRO_PESSOA_FISICA` | Lógico | Impede cadastro de CPF |
| `CLIENTECONTRIBUINTE_SIM` | Lógico | Cliente padrão contribuinte |
| `CLIENTESIMPLESNACIONAL_SIM` | Lógico | Cliente padrão simples nacional |

#### 📊 Relatórios

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `HABILITAR_GERADOR_RELATORIOS` | Lógico | Ativa aba de relatórios |
| `RELATORIO_800` | - | Relatório 800 do MaxPedido |

#### 🎯 Metas e Performance

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `META_FOR` | Lógico | Habilita aba metas por fornecedor |
| `META_PROD` | Lógico | Habilita aba metas por produto |
| `META_MENSAL` | Lógico | Habilita aba metas mensais |
| `CRITERIO_VENDA` | Literal | P = Faturado + Liberado + Montado |

#### 📦 Produtos

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `EXIBE_VALIDADE_PRODUTO_WMS` | Lógico | Mostra validade WMS |
| `LISTAR_INFO_LOTES` | Lógico | Mostra informações de lotes |
| `BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE` | Lógico | Bloqueia venda sem estoque |
| `OCULTAR_PROD_FORA_LINHA` | Lógico | Oculta produtos fora de linha |
| `USAR_MULTIPLO_QTDE` | Lógico | Usa múltiplo de quantidade |

#### 💳 Conta Corrente

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `USAR_CCRCA_MAXIMA` | Lógico | Habilita conta corrente |
| `EXIBIR_SALDOCC_DISPONIVEL` | Lógico | Exibe saldo CC disponível |
| `APRESENTAR_CARD_CC` | Lógico | Exibe card de CC |
| `DESCONTA_SALDOCCRCA_OFFLINE` | Lógico | Usa CC offline |
| `DEFINE_CC_MENU` | Inteiro | Define qual saldo aparece (0=saldo, 1=saldo-crédito, 2=crédito) |

#### 🎁 Promoções e Descontos

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `USAR_CAMPANHA_DESCONTO_PROGRESSIVO` | Lógico | Ativa desconto progressivo |
| `TIPO_DESC_PROGRESSIVO` | Literal | PRG = Campanha / PEG = Desconto |
| `EXIBIR_PRECO_UNIT_EMB` | Lógico | Exibe preço unitário embalagem |
| `APRESENTAR_DESCONTOS_PEDIDO_EMAIL` | Lógico | Exibe descontos no PDF |

#### 🚚 Entrega e Localização

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `HABILITAR_DADOS_ENTREGA` | Lógico | Habilita status maxMotorista |
| `GPS_TRACKING_ENABLED` | Lógico | Ativa rastreio GPS |
| `GPS_IS_REQUIRED_CONFEC_PEDIDO` | Lógico | Obriga GPS para fazer pedido |
| `ATIVAR_GPS_PEDIDO` | Lógico | Alerta se GPS desativado |

#### 📅 Datas e Horários

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `OBRIGAR_PREVISAO_FATURAMENTO` | Lógico | Obriga data previsão faturamento |
| `PREVISAO_FATURAMENTO_DIA_MAIS_UM` | Lógico | Grava sempre com dia+1 |
| `CONSIDERAR_DATA_ATUAL_PREV_FAT` | Lógico | Conta data atual na previsão |
| `PRAZO_VALIDADE_PREVISAOFATURAMENTO` | Inteiro | Dias máximos para previsão |
| `PRAZO_VALIDADE_PEDIDO` | Inteiro | Validade do pedido salvo |

#### ⏰ Horário de Funcionamento

| Parâmetro | Tipo | Descrição | Valor |
|-----------|------|-----------|-------|
| `BLOQ_VENDA_FORA_HORARIO_COM` | Lógico | Bloqueia pedidos fora hora | S/N |
| `BLOQ_VENDA_FORA_HORARIO_COM_IM` | Inteiro | Hora início manhã | 0830 |
| `BLOQ_VENDA_FORA_HORARIO_COM_TM` | Inteiro | Hora término manhã | 1200 |
| `BLOQ_VENDA_FORA_HORARIO_COM_IT` | Inteiro | Hora início tarde | 1330 |
| `BLOQ_VENDA_FORA_HORARIO_COM_TT` | Inteiro | Hora término tarde | 1800 |

### Parâmetros do Winthor (PCMXSCONFIGURACOES)

```sql
SELECT * FROM PCMXSCONFIGURACOES WHERE NOME LIKE '%FILIAL%';
```

**Parâmetros Importantes:**
- `CODFILIAL_PREST` - Filiais para prestação
- `CODFILIAL_IMPORTACAO` - Filiais para importação

---

<a name="gestão-de-clientes"></a>
## 6️⃣ GESTÃO DE CLIENTES

### Cadastro de Clientes

#### Validações Obrigatórias

| Campo | Tabela | Descrição | Banco |
|-------|--------|-----------|-------|
| **CODCLI** | MXSCLIENT | Código do cliente | Nuvem |
| **NOME** | MXSCLIENT | Nome do cliente | Nuvem |
| **CNPJ/CPF** | MXSCLIENT | CNPJ ou CPF | Nuvem |
| **CODATV1** | MXSCLIENT | Ramo de atividade | Nuvem |
| **CODCOB** | MXSCLIENT | Cobrança padrão | Nuvem |

#### Campos Importantes

| Campo | Descrição | Validação |
|-------|-----------|-----------|
| `LIMCRED` | Limite de crédito | Deve ser >= 0 |
| `LIMITECREDSUPPLI` | Limite crédito suplementar | Opcional |
| `CONDVENDA1` | Venda normal (TV1) | 'S' ou 'N' |
| `CONDVENDA4` | Venda tipo 4 (Simples Fatura) | 'S' ou 'N' |
| `CONDVENDA5` | Bonificação (TV5) | 'S' ou 'N' |
| `CODCLIPRINC` | Cliente principal | Para consolidação |
| `CODPRACA` | Praça do cliente | Vinculação regional |
| `DTEXCLUSAO` | Data exclusão | NULL = ativo |
| `CODOPERACAO` | Operação | 2 = excluído |

### Vínculo RCA/Cliente

#### Tabelas

| Tabela | Descrição | Banco |
|--------|-----------|-------|
| **MXSCLIENT.CODUSUR1** | RCA 1 | Nuvem |
| **MXSCLIENT.CODUSUR2** | RCA 2 | Nuvem |
| **MXSCLIENT.CODUSUR3** | RCA 3 | Nuvem |
| **ERP_MXSUSURCLI** | Vínculo RCA/Cliente (ERP) | Nuvem |

#### Verificar Vínculo

```sql
SELECT * FROM MXSCLIENT 
WHERE CODCLI = [CODCLI]
AND CODUSUR1 = [CODUSUARIO];
```

### Endereço de Entrega Diferente

#### Configuração Winthor
Feita no próprio Winthor, sincronize após configurar.

#### Configuração O'ERP's
Envie no endpoint `ClientesEnderecos` (tabela `MXSCLIENTENDENT`)

#### Permissão Central
"Permissão de Usuário Para o Endereço de Entrega"

#### Uso no MaxPedido
Na aba **TOTAIS** é possível alterar o endereço de entrega.

### Cadastro Duplicado

#### Problema
Mesmo cliente aparece duas vezes na lista.

#### Causa
Parâmetro `HABILITA_PED_CLI_NAO_SINC` habilitado + cliente em duas tabelas:
- `MXSCADCLIENTES` (pré-cadastro)
- `MXSCLIENT` (cadastro principal)

#### Solução
1. Desabilitar parâmetro `HABILITA_PED_CLI_NAO_SINC` OU
2. Fazer swipe na tela de gerenciar clientes

### Erro: "Cadastro precisa de aprovação"

#### Sintoma
"Não foi possível confeccionar pedidos para clientes sem que antes seu cadastro seja aprovado pela empresa"

#### Causa
Coluna `CODFUNCULTALTER` está **NULL** na MXSCLIENT.

#### Solução
- **Winthor:** Abra o cadastro do cliente e clique em "Salvar"
- **O'ERP:** Envie o endpoint "Clientes" com `CODFUNCULTALTER` preenchido

### Consumidor Final

Para ocultar consumidor final do aplicativo:

```sql
UPDATE MXSPARAMETRO 
SET VALOR = 'N' 
WHERE NOME IN (
  'FILTRAR_CLIENTES_CONSUMIDOR_FINAL',
  'FILTRAR_CLIENTES_CONSUMIDOR_FINAL_ENTRE_UM_TRES'
);
```

### Anexo de Clientes

#### O'ERP's
Tabela: `MXSANEXOCLIENTES`

#### Winthor
- Fotos não são enviadas para o Winthor
- Fotos só ficam disponíveis quando cadastro é integrado

---

<a name="descontos-políticas"></a>
## 7️⃣ DESCONTOS E POLÍTICAS

### Prioridade de Desconto

| Nível | Tabela | Tipo | Observação |
|-------|--------|------|-----------|
| 1 | MXSPRECOPROM | Preço Fixo | Maior prioridade |
| 2 | MXSDESCONTOC | Campanha de Desconto | - |
| 3 | MXSTABPR | Tabela de Preço | Compara com PERDESCMAX |
| 4 | MXSUSUARI | Permissão Usuário | PERMAXVENDA |
| 5 | MXSCONFIGERP | Configuração ERP | PERMAXVENDA |

### Campanha de Desconto

#### Estrutura

```sql
-- Buscar campanha
SELECT * FROM MXSDESCONTOC WHERE CODIGO = [COD];

-- Buscar itens da campanha
SELECT * FROM MXSDESCONTOI WHERE CODIGO = [COD];
```

#### Problemas Comuns

**Campanha sem produtos:**
- RCA não tem acesso ao produto
- Campanha foi enviada incorretamente
- Divergências de base entre RCA e banco

#### Verificar Desconto Máximo

```sql
SELECT PERDESCMAX, * FROM MXSTABPR 
WHERE CODPROD = [CODPROD];
```

**Regra:** Se `PERDESCMAX` for NULL/VAZIO = desconto livre

### Desconto Progressivo

#### Tipos

| Tipo | Código | Descrição |
|------|--------|-----------|
| **Campanha Progressiva** | PRG | Desconto progressivo em campanha |
| **Desconto Progressivo** | PEG | Desconto progressivo simples |

#### Parametrização

```
USAR_CAMPANHA_DESCONTO_PROGRESSIVO = S
TIPO_DESC_PROGRESSIVO = 'PRG'
```

#### Tabelas

| Tabela | Descrição |
|--------|-----------|
| MXSCAMPANHAFAMILIA | Cabeçalho campanha |
| MXSCAMPANHAFAIXAS | Faixas de desconto |
| MXSCAMPANHAFAMILIAGRUPOS | Grupos |
| MXSCAMPANHAPROPORCAO | Proporção |
| MXSFAMILIAITENS | Itens da família |
| MXSFILTROCAMPANHA | Restrições (TIPORESTRICAO: 1=restrito, 2=exclusivo) |

#### Fluxo no App

1. Aba "Tabela" → Filtro "Produtos com desconto progressivo"
2. Adicionar produto da campanha
3. Clicar em "..." → "Acompanhar campanha progressiva"
4. Visualizar requisitos para ativar

#### Modelos de Desconto

| Modelo | Descrição | Obrigatório |
|--------|-----------|-------------|
| **MIQ** | Mix de produtos com intervalo mínimo | Todos os produtos necessários |
| **MQT** | Mix quantidade total | Quantidade mínima de qualquer produto |
| **SQP** | Alguns de qualquer produto | Não obrigatório todos |
| **FPU** | Família/fornecedor/categoria com todos | Obrigatório todos |

### Desconto Acima do Permitido

#### Parametrização Winthor

```
CON_ACEITADESCTMKFV (Rotina 132)
```

#### Parametrização Máxima

Permissão no usuário:
**"Permitir solicitação de autorização de preço no aplicativo"**

#### Fluxo

1. RCA aplica desconto > PERDESCMAX
2. Sistema solicita autorização de preço
3. Supervisor aprova via MaxGestão ou ERP (Rotina 301/336)
4. Se aprovado, saldo CC é consumido

### Promoção de Preço Fixo

#### Campos Obrigatórios (MXSPRECOPROM)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| CODPRECOPROM | TEXT | Código da promoção |
| CODFILIAL | INT | Filial |
| CODPROD | INT | Código do produto |
| DTINICIOVIGENCIA | DATE | Data início |
| DTFIMVIGENCIA | DATE | Data fim |
| NUMREGIAO | INT | Região |
| CODPRACA | INT | Praça |
| ACEITAACRESCIMOPRECOFIXO | BOOL | Permite acréscimo? |
| ACEITADESCPRECOFIXO | BOOL | Permite desconto? |
| CONSIDERAPRECOSEMIMPOSTO | BOOL | Considera sem imposto? |
| AGREGARST | BOOL | Agrega ST? |

#### Família de Produtos

Para usar promoção por família:

1. Criar família na Rotina 203 (PCPRODUT)
2. Campo `CODPRODPRINC` = código da família
3. Na MXSPRECOPROM, colocar `CODPRODPRINC` em `CODPROD`
4. Ativar `UTILIZAPRECOFIXOFAMILIA = 'S'`

---

<a name="conta-corrente"></a>
## 8️⃣ CONTA CORRENTE (SALDO CC)

### O que é?

Carteira virtual do cliente dentro do MaxPedido. Permite descontos especiais acima do normal, sendo a diferença debitada do saldo CC do RCA.

### Parametrização Necessária

#### Winthor/ERP

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| CON_USACREDRCA | BOOL | Usa saldo CC? |
| CON_TROCAALTDEBCREDRCA | BOOL | Vendas bonificadas alteram saldo? |
| CON_ACEITADESCPRECOFIXO | BOOL | Aceita desconto preço fixo? |

#### Máxima (Central de Configurações)

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| USAR_CCRCA_MAXIMA | BOOL | Habilita CC |
| EXIBIR_SALDOCC_DISPONIVEL | BOOL | Exibe saldo disponível |
| APRESENTAR_CARD_CC | BOOL | Exibe card de CC |
| GERAR_DADOS_CC_RCA | BOOL | Sincroniza movimentações (últimos 7 dias) |
| EXIBIR_TODA_MOVIMENTACAO_CC | BOOL | Exibe movimentação completa |
| DEFINE_CC_MENU | INT | Qual saldo no menu (0=saldo, 1=saldo-crédito, 2=crédito) |
| DESCONTA_SALDOCCRCA_OFFLINE | BOOL | Usa CC offline |
| IMPEDIR_ABATIMENTO_SEMSALDORCA | BOOL | Bloqueia uso sem saldo |
| ABATIMENTODEBITARCCRCA | BOOL | Permite abatimento negativo? |

#### Banco de Dados

| Campo | Tabela | Descrição |
|-------|--------|-----------|
| USADEBCREDRCA | MXSUSUARI | Coluna: Usuário usa CC? ('S'/'N') |
| TIPOMOVCCRCA | MXSCONFIGERP | Tipo de movimentação CC |

#### Tipos de Movimentação CC

| Tipo | Descrição |
|------|-----------|
| FF | Débito/Crédito no faturamento |
| VA | Débito na venda, crédito no acerto |
| VF | Débito na venda, crédito no faturamento |
| VV | Débito/Crédito na venda |

### Como Gerar Saldo CC?

RCA aplica **desconto negativo** (acréscimo):
- Se produto custa R$ 10 para o vendedor e ele coloca R$ 13, a diferença (R$ 3) gera saldo CC

### Limite de Acréscimo

Configure na Rotina 132 ou 201 do Winthor:
**Percentual máximo de acréscimo**

### Se Exibir "--" na Tela

**Causa:** Parâmetros não validados corretamente

**Solução:** Ativar todos os parâmetros como 'S':
- USAR_CCRCA_MAXIMA = S
- EXIBIR_SALDOCC_DISPONIVEL = S
- APRESENTAR_CARD_CC = S
- GERAR_DADOS_CC_RCA = S

---

<a name="produtos-catálogo"></a>
## 9️⃣ PRODUTOS E CATÁLOGO

### Cadastro de Produtos

#### Campos Importantes (MXSPRODUT)

| Campo | Descrição | Validação |
|-------|-----------|-----------|
| CODPROD | Código produto | PK |
| NOME | Nome produto | Obrigatório |
| CODDISTRIB | Código distribuição | Deve igualar MXSFORNEC.CODDISTRIB |
| OBS2 | Observação | FL = Fora de Linha |
| REVENDA | É para revenda? | 'S'/'N' |
| ENVIARFORCAVENDAS | Envia para FV? | 'S'/'N' |
| DTVENC | Validade/Vencimento | Data |
| PESOPECA | Peso peça | Números frios |
| PESOBRUTOMASTER | Peso bruto master | Números frios |
| TIPOESTOQUE | Tipo | FR = Frios |
| UNIDADE | Unidade | UN, FR, etc. |
| UTILIZAPRECOFIXOFAMILIA | Usa preço fixo família? | 'S'/'N' |
| CODPRODPRINC | Código família | Para produtos relacionados |

### Produto Não Aparece

#### Causas e Soluções

| Causa | Verificar | Solução |
|-------|-----------|--------|
| **Fora de linha** | OBS2 = 'FL' | Desabilitar `OCULTAR_PROD_FORA_LINHA` |
| **Código distribuição divergente** | CODDISTRIB ≠ MXSFORNEC.CODDISTRIB | Igualar códigos |
| **Restrição 391** | PCRESTRICAOVENDA (Rotina 391) | Desabilitar `RESTRINGIR_PRODUTOS_391 = 'N'` |
| **Sem revenda** | REVENDA = 'N' | Ativar `ENVIAR_PRODUTO_SEM_REVENDA = 'S'` |
| **Sem tabela preço** | MXSTABPR vazio | Cadastrar tabela de preço |
| **Sem estoque** | MXSEST.QT = 0 | Considerar parâmetro `BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE` |

### Embalagem

#### Tipos de Embalagem

```sql
SELECT * FROM MXSEMBALAGEM WHERE CODPROD = [CODPROD];
```

#### Configuração Múltiplas Embalagens

```
OCULTAR_EMBALAGEM_LISTAGEM = 'N' 
LISTAR_PRODUTOS_POR_EMBALAGENS = 'S'
```

#### Validar Múltiplo de Venda

**Para O'ERP's:**

```sql
UPDATE MXSPRODFILIAL SET MULTIPLO = 15 
WHERE CODPROD = [CODPROD];

UPDATE MXSCLIENT SET VALIDARMULTIPLOVENDA = 'S' 
WHERE CODCLI = [CODCLI];

UPDATE MXSPARAMETRO SET VALOR = 'N' 
WHERE NOME = 'USAR_MULTIPLO_QTDE';
```

**Parâmetro:** `USAR_MULTIPLO_QTDE = 'N'`

### Validade WMS

#### Habilitar

```
EXIBE_VALIDADE_PRODUTO_WMS = 'S'
```

#### Visualizar no App

1. Clicar no produto
2. Canto superior direito → Botão azul "+ infos"

#### Se Não Aparecer

Verificar:
- Tabela MXSVALIDADEWMS (nuvem)
- Endpoint MXSLOTE
- Parâmetro `EXIBIR_VALIDADE_WMS_VENCIDA`

#### Script Validação Validade WMS

```sql
SELECT S.CODPROD, A.CODFILIAL, SUM(S.QT) QTDE, S.DTVAL DATA
FROM PCESTENDERECO S, PCENDERECO A, PCPRODUT P
WHERE S.QT > 0
AND A.CODENDERECO = S.CODENDERECO
AND P.CODPROD = S.CODPROD
AND NVL(P.OBS, 'XX') NOT IN ('PV','SU','EQ') 
AND (NVL(P.REVENDA, 'S') = 'S' 
     OR (SELECT NVL(VALOR,'N') FROM PCMXSCONFIGURACOES 
         WHERE NOME = 'ENVIAR_PRODUTO_SEM_REVENDA') = 'S')
AND P.DTEXCLUSAO IS NULL 
AND NVL(P.ENVIARFORCAVENDAS, 'S') = 'S'
AND NVL(A.BLOQUEIO,'N') != 'S'
AND NVL(A.STATUS,'N') NOT IN ('A', 'F')
AND (NVL(ESTOQUEPORDTVALIDADE, 'S') = 'S' 
     AND NVL(ESTOQUEPORLOTE,'N') = 'N')
AND S.DTVAL IS NOT NULL
GROUP BY S.CODPROD, A.CODFILIAL, S.DTVAL;
```

### Lotes

#### Cadastro

Tabela: MXSLOTE
Parâmetro: `LISTAR_INFO_LOTES = 'S'`

#### Visualizar no App

Aba "Informações adicionais" → Seção "Listar Lotes"

### Fotografia de Produtos

#### Upload pela Central

Configurações → Extras → Upload de Fotos

**Regras:**
- Nome da imagem = Código do produto
- Pode fazer upload de pasta com várias fotos

#### Ponto de Montagem Linux

Necessário para clientes em repositórios.

**Arquivo:** `mount.sh`

```bash
#!/bin/bash

proc=$(mount -l | grep //192.168.10.104/wntadm/IMG | wc -l)

if [ $proc -le 0 ]
then
  mount -t cifs //192.168.10.104/wntadm/IMG /app/maxima/MXS_Extrator/imagens_data_dispan \
    -o username=forca.vendas,password=@51201,vers=1.0
fi
```

**Configuração Crontab:**
```bash
*/1 * * * * root $SHELL /mount.sh
```

**Verificar montagem:**
```bash
df -h
```

### Positivação de Produtos e Clientes

#### O que é?

- **Cliente positivado:** Cliente que teve pedido faturado naquele mês
- **Produto positivado:** Produto que fez parte de pedido faturado

#### Requisitos

Tabela **PCDATA** deve conter dados

#### Parâmetros

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| GERAR_DADOS_POS_PRODUTOS | BOOL | Habilita geração |
| CONSIDERA_POS_CLIENTE | BOOL | Considera positivação por cliente |
| FILTRAR_DADOS_CONSULTA_POSITIVACAO_RCA | BOOL | Filtra por RCA individual |
| CONSULTA_PRODUTO_POSITIVADO_PRODUTPOS | BOOL | Exibe numericamente |

#### Tipos

| Tipo | Descrição |
|------|-----------|
| D | Tipo D |
| T | Tipo T |

### MIX de Produtos

#### Geração

Parâmetros na Central e no banco local:
```
GERAR_DADOS_MIX_CLIENTES = 'S'
GERAR_DADOS_MIX_CLIENTES_DIAS = [valor, máx 90]
```

#### Tabelas

| Tabela | Descrição |
|--------|-----------|
| MXSMIXCLIENTES | Mix do cliente |
| MXSCLIENTCHARTHISTVENDA | Histórico de compras (SQLite) |

#### Se Não Aparecer

Verificar:
- Parâmetro `GERAR_DADOS_MIX_CLIENTES = 'S'`
- Parâmetro `GERAR_DADOS_MIX_CLIENTES_DIAS` (máx 90)
- Filtros: `OCULTAR_PROD_ABAMIX_SEMESTOQUE`, `FILTRAR_DADOS_RCA_MIXVENDIDO`

---

<a name="relatórios"></a>
## 🔟 RELATÓRIOS

### Relatório 800

Relatório de desempenho do MaxPedido.

#### Requisitos

- **Servidor IIS** instalado na máquina do cliente
- **Link externo** para acesso

#### Como Configurar

1. Verificar IIS instalado:
   ```bash
   iisreset  # Se der erro, não está instalado
   ```
   
   Ou: Painel de Controle → Sistema e Segurança → Ferramentas Administrativas → Internet Information Services (IIS) Manager

2. Acessar IIS:
   ```
   Win+R → inetmgr
   ```

3. [Seguir documentação na Biblioteca](https://basedeconhecimento.maximatech.com.br/)

#### Configuração appsettings.json

Formato correto do caminho:
```json
{
  "caminhoRelatorios": "\\\\192.186.110\\sistema\\mod-008"
}
```

#### Filtros de Relatórios

Tabelas para análise:
- `PCPARAMETROS`
- `MXSRELATORIOPARAM`

**Abrir chamado de GATE** para problemas com filtros.

#### Parâmetro para Habilitar

```
HABILITAR_GERADOR_RELATORIOS = 'S'
```

### Espelho do Pedido (Personalização)

#### Parâmetros de Exibição

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| EXIBIR_PRECO_UNIT_EMB | BOOL | Preço unitário embalagem |
| APRESENTAR_DESCONTOS_PEDIDO_EMAIL | BOOL | Descontos no PDF |
| OCULTAR_IMPOSTOS_PEDIDO_EMAIL | BOOL | Oculta impostos |
| OCULTAR_VALIDADE_PROPOSTA | BOOL | Oculta datas |
| EXIBIR_FOTO_DO_PRODUTO_PDF | BOOL | Fotos no PDF |
| EXIBIR_CAMPO_CA_COMPART_PED_ORC | BOOL | Campo CA |
| LINK_LOGO_MARCA | TEXT | Logo URL |

#### Desabilitar Espelho Padrão

```
DESABILITAR_ESPELHO_PED_PADRAO = 'S'
```

(Use quando cliente tem espelho personalizado)

### Relatório Boleto (Segunda Via)

#### Requisitos

- Versão MaxPedido >= 2.223.9
- Ambiente nuvem atualizado

#### Acesso no App

1. Consultas → Títulos
2. Clicar e segurar no título
3. "Gostaria de compartilhar o boleto?" → Sim

#### Campos Obrigatórios

Tabelas: `ERP_MXSPREST` ou `MXSTITULOSABERTOS`

| Campo | Descrição |
|-------|-----------|
| NOSSONUMBCO | Número nossa cobrança |
| LINHADIG | Linha digitável |

#### Erros Comuns

**Erro:** "Não foi possível gerar o relatório!"

**Verificar:**
- Campos NOSSONUMBCO e LINHADIG preenchidos
- Parâmetro `EXIBE_LINHA_DIGITAVEL = 'S'`
- Permissão app "Acesso a todos os arquivos"

---

<a name="checkin-checkout"></a>
## 1️⃣1️⃣ CHECKIN/CHECKOUT E LOCALIZAÇÃO

### Ativar Funcionalidade

```
UTILIZA_CHECKIN_CHECKOUT = 'S'
GPS_IS_REQUIRED_CONFEC_PEDIDO = 'S'
```

### Parâmetros Relacionados

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| PERMITIR_PEDIDO_SEM_CHECKIN | BOOL | Permite pedido sem check-in? |
| OBRIGAR_ATENDIMENTO_PARA_CHECKOUT | BOOL | Obriga pedido/justificativa |
| OBRIGA_MOSTRAR_MOTIVO_NAO_VENDA | BOOL | Mostra motivo não venda |
| OBRIGA_CHECKIN_CLIENTE_FORA_ROTA | BOOL | Check-in mesmo fora de rota |
| UTILIZA_HORA_APARELHO_JUSTIFICATIVA_VISITA | BOOL | Usa hora do aparelho |

### GPS

#### Ativação

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| GPS_TRACKING_ENABLED | BOOL | Ativa rastreio GPS |
| GPS_IS_REQUIRED_CONFEC_PEDIDO | BOOL | Obriga GPS para pedido |
| ATIVAR_GPS_PEDIDO | BOOL | Alerta se GPS desativado |

#### Cerca Eletrônica

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| GPS_EDGE_BLOCK | BOOL | Valida cerca eletrônica |
| GPS_EDGE_METERS_SIZE | INT | Raio em metros |

### Histórico de Checkin/Checkout/Justificativa

#### Ver no Winthor

Rotina 344 (Justificativa de Visita)

#### Tabelas

| Banco | Tabela |
|-------|--------|
| SQLite | MXSLOCATION |
| Nuvem | ERP_MXSVISITAFV |
| Winthor | PCVISITAFV |

#### Observação

Se justificativas aparecem com horários errados:
```
UTILIZA_HORA_APARELHO_JUSTIFICATIVA_VISITA = 'N'
```

### Justificar Visita Anterior (Roteiro Pendente)

Para bloquear novos pedidos se cliente anterior não foi justificado:

```
BLOQ_RCA_COM_ROTA_PENDENTE = 'S'
ROTEIRO_PENDENTE_ONTEM = 'S'
DIAS_VERIFICACAO_ROTEIRO_PENDENTE = 1
JUSTIFICAR_ROTEIRO_ANTERIOR = 'S'
BLK_SYNC_ROTEIRO_PENDENTE = 'S'
```

**Permissão:** "Permitir justificativas de clientes fora da rota"

---

<a name="erros-resoluções"></a>
## 1️⃣2️⃣ ERROS E RESOLUÇÕES COMUNS

### Limite de Cliente

#### Erro: Limite não atualiza na APK

**Causa:** Parâmetro `CONSIDERAR_CLIENTE_EXCLUIDO_LIMITE = 'N'`

**Verificar:**
```sql
SELECT * FROM MXSCLIENT 
WHERE CODCLI = [CODCLI]
AND (DTEXCLUSAO IS NOT NULL OR CODOPERACAO = 2);
```

### Crédito Disponível

#### Cálculo

```sql
WITH CLIENTE AS (
    SELECT 
        PCCLIENT.CODCLI,
        PCCLIENT.CODCLIPRINC,
        NVL(TBLIMITE.VLLIMITE, 0) AS VLLIMITE,
        NVL(TBPEDIDOS.VLPEDIDOS, 0) AS VLPEDIDOS,
        NVL(TBTITULOS.VLTITULOS, 0) * -1 AS VLTITULOS,
        NVL(TBCREDITO.VLCREDITO, 0) AS VLCREDITO,
        NVL(TBCHEQUE.VLCHEQUES, 0) * -1 AS VLCHEQUES,
        NVL(TBLIMITE.LIMITECREDSUPPLI, 0) AS VLLIMITECREDSUPPLI
    FROM PCCLIENT
    -- JOINs aqui
)
SELECT 
    CLIENTE.CODCLI,
    DECODE(PARAMETRO.VALOR, 'N', CLIENTE.VLLIMITE, NVL(LIMINTE_PRINCIPAL.VLLIMITE, CLIENTE.VLLIMITE)) VLLIMITE
FROM CLIENTE
-- Restante da query
```

### Tributação do Produto

#### Erro: "Não foi possível carregar a tributação"

**Verificar:**
1. Cliente não possui filial NF
2. Processo na 316 está operacional
3. Existe tributação para produto/filial

```sql
SELECT * FROM MXSTABTRIB WHERE CODPROD = [CODPROD];
SELECT * FROM MXSTABPR WHERE CODPROD = [CODPROD] 
  AND CODST IS NOT NULL;
SELECT * FROM MXSTRIBUT WHERE CODST = [CODST];
```

### Código IBGE (Cadastro Cliente)

#### Erro: CNPJ não encontrado na Receita Federal

**Causa:** CNPJ novo (Máxima usa RECEITAWS, não Receita Federal)

**Solução:**
- Aguardar alguns meses (RECEITAWS sincroniza em pacotes)
- Solicitar inclusão em contato@receitaws.com.br

#### IBGE não aparece para OERP's

```
ENVIAR_TODAS_CIDADES_IBGE = 'S'
```

### Custo Financeiro Inválido

#### Erro: "Custo Financeiro, Custo Real ou Custo Real + Crédito de ICM inválidos"

**Causa:** Valores zerados ou não encontrados

```sql
SELECT CUSTOREAL, CUSTOFIN, CUSTOREP, E.* 
FROM MXSEST E 
WHERE CODPROD = [CODPROD];
```

**Todos devem ser > 0**

### Nível de Venda

#### Erro: "NÍVEL DE VENDA"

**Regra:**
Cliente com nível de venda 1 pode acessar todos os níveis. Cliente nível 5 só pode usar níveis >= 5.

```sql
SELECT * FROM MXSCOB WHERE CODCOB = [CODCOB];
```

Verificar campo de nível de venda.

### Bonificação (TV5)

#### Não aparece opção de bonificação

**Verificar:**
1. `MXSCLIENT.CONDVENDA5 = 'S'`
2. Vínculo com Plano de Pagamento (MXSPLPAGCLI)
3. Vínculo com Cobrança (MXSCOBCLI)
4. `MXSPLPAG.TIPOPRAZO = 'B'`

#### Cobrança não é aceita

Cobraças válidas para bonificação:
```
BNF, BNFR, BNTR, BNFT, BNRP, BNFM
```

#### TV5 vinculado a TV1

```
OBRIGATORIOVINCULARTV5COMTV1 = 'S'
MXS_OBRIGATORIOVINCULARTV5COMTV1 = 'S'
PEDIR_AUTORIZACAO_TV5_VINCULADO_TV1 = 'S'
QTDE_DIAS_VINCULO_TV1_COM_TV5 = [dias]
PERC_LIMITE_TV5_RCA = [percentual]
```

### Margem de Lucratividade

#### Fórmula por Pedido

```
((VLATEND – VLCUSTOFIN) / VLATEND) * 100
```

#### Fórmula por Item

```
((PVENDA – VLCUSTOFIN) / PVENDA) * 100
```

#### Validações

| Nível | Fonte | Campo |
|-------|-------|-------|
| Pedido | Winthor Rotina 1370 | % mínima |
| Plano Pagamento | MXSPLPAG | MARGEMMIN |
| Item | MXSPRODFILIAL | PERCMARGEMMIN |
| ERP | MXSPARAMFILIAL | CON_MARGEMMIN |

### Títulos Abertos

#### Campo obrigatório para marcar como pago

| Campo | Descrição |
|-------|-----------|
| VPAG | Valor de pagamento |
| DTPAG | Data de pagamento |

#### Fluxo de Sincronização

```
PCPREST (Local)
    ↓
ERP_MXSPREST (Nuvem)
    ↓
MXSTITULOSABERTOS (Nuvem)
    ↓
MaxPedido (APK)
```

#### Somar Juros e Multa

```
SOMAR_JUROS_TITULOS = 'S'
HABILITAR_SOMA_MULTA_TITULO = 'S'
```

### Bloquear Pedido Cliente Acima do Limite

**Prioridade:**

1. **`BLOQ_SALVAR_PEDIDO_ACIMA_LIMITE_CLI_APK`** (Máxima)
   - Bloqueia salvamento do pedido
   
2. **`BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE`** (Máxima)
   - Bloqueia envio do pedido
   
3. **`CON_ACEITAVENDABLOQ`** (Winthor)
   - Se = 'N': Não deixa enviar
   - Se = 'S': Deixa enviar

### Pedidos Presos na Timeline

#### Causa: Cliente sem limite

```
BLOQUEIA_PEDIDO_CLIENTE_SEMLIMITE = 'S'
```

**Solução:**
1. Regularizar situação no ERP
2. Sincronizar app
3. Duplicar pedido (correção MXPEDDV-88601)

### Timeline não atualiza status

#### Hierarquia de Validação

1. **MXSHISTORICOPEDC** (posição do pedido) - Maior prioridade
2. **MXSINTEGRACAOPEDIDO** (crítica do pedido)

**Problema comum:** Campo `DTABERTURAPEDPALM` vazio na MXSHISTORICOPEDC

**Solução:** Preencher campo obrigatório

#### Para reenviar crítica

Endpoint: `https://intpdv-unificado.solucoesmaxima.com.br/api/v1/StatusPedidos/AtualizarPedidos`

```json
{
  "PosicaoPedidoERP": "Faturado"
}
```

Veja itens 6.1 e 6.2 do Layout de integração.

---

<a name="infra"></a>
## 1️⃣3️⃣ INFRAESTRUTURA: DOCKER, PORTAINER E HANGFIRE

### Instalação Docker

#### Verificar se está instalado

```bash
docker ps -a
```

#### Desinstalar

```bash
sudo apt-get purge -y docker* ; \
sudo apt-get autoremove -y --purge docker* ; \
sudo rm -rf /var/lib/docker /etc/docker ; \
sudo rm /etc/apparmor.d/docker ; \
sudo groupdel docker ; \
sudo rm -rf /var/run/docker.sock
```

#### Instalar

```bash
sudo apt update ; \
sudo apt-get remove docker docker-engine docker.io containerd runc -y ; \
sudo apt-get update; \
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y ; \
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - ; \
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"; \
sudo apt-get update ; \
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

### Instalação Portainer

#### Comando

```bash
docker run -d -p 9000:9000 \
  --name MXS_Portainer \
  --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce \
  --admin-password '$2y$05$Xb5IB53HjCQqfD/7k9F2d.thkVspomm/2udcI6/dg8Q6nKJ9ZOZda' \
  --logo "https://maxsolucoes-versoes.s3.amazonaws.com/extrator/v1/logo/logo-maxima.png"
```

#### Acessar

```
http://localhost:9000
Usuário: admin
Senha: maxsolucoes@portainer
```

### Stack Extrator (docker-compose)

```yaml
version: '3'

services:
  MXS-Extrator_NomeCliente:
    privileged: true
    image: dockermaxima/extrator:VERSAO
    healthcheck:
      test: ["CMD-SHELL", "/bin/healthcheck.sh"]
      interval: 1m30s
      timeout: 10s
      retries: 5
    environment:
      USUARIO_EXTRATOR_NUVEM: [USUARIO]
      SENHA_EXTRATOR_NUVEM: [SENHA_CRIPTOGRAFADA]
      USUARIO_SYSTEM_WINTHOR: [USUARIO]
      SENHA_SYSTEM_WINTHOR: [SENHA_CRIPTOGRAFADA]
      TZ: America/Sao_Paulo
    container_name: MXS-Extrator_NomeCliente
    restart: always
    network_mode: bridge
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /app/maxima/MXS_Extrator/imagens_data:/mnt/maxima/produtos_fotos
      - /app/maxima/MXS_Extrator/extrator_prd_data/Conf:/app/maxima_extrator/extrator_prd/Conf
      - /app/maxima/MXS_Extrator/extrator_prd_data/LOGS:/app/maxima_extrator/extrator_prd/LOGS
      - /app/maxima/MXS_Extrator/extrator_prd_data/id:/app/maxima
    tty: true
    ports:
      - 9002:81
```

### Hangfire

#### Acessar

```
http://localhost:9002
Usuário: admin
Senha: maxsolucoes@extrator
```

#### Jobs Recorrentes Importantes

1. **Página 1:** ProcessamentosWebApi.ObterScripts
2. **Página 2:** Atualização de Banco de Dados

### Atualizar Ambiente do Cliente

#### Passos

1. **Atualizar Portainer**
   - Usuário: admin
   - Senha: maxsolucoes@portainer
   - Ver versão no Discord (#maxpedido)

2. **Rodar Atualizador** (após Portainer)
   - Acessar Portainer
   - Executar atualizador
   - Aguardar até "Sucesso"

3. **Rodar Jobs Hangfire** (após Atualizador)
   - Acessar Hangfire (porta 9002)
   - Aba "Tarefas recorrentes"
   - Executar ambas as páginas

### Erro de Bloqueio APPSV no Extrator

#### Teste de Conectividade

```bash
telnet intext-hmg.solucoesmaxima.com.br 81
telnet intpdv-hmg.solucoesmaxima.com.br 81
telnet appsv.solucoesmaxima.com.br 8081
```

**Causa comum:** Firewall bloqueando porta 8081 para appsv

#### IPs Máxima que vêm da AWS

Solicitar liberação no firewall:
```
3.81.180.245
34.236.34.79
3.81.180.2
18.215.65.25
```

[Veja documentação de requisitos](https://maximatech.com.br/requisitos/cloud-tipo-erp/cloud-winthor/)

### Banco Local - Objetos Inválidos

#### Script para Verificar

```sql
SELECT OWNER,
       OBJECT_TYPE,
       OBJECT_NAME,
       STATUS,
       'alter ' || DECODE(OBJECT_TYPE, 'PACKAGE BODY', 'PACKAGE', OBJECT_TYPE) || ' ' || OWNER 
       || '.' || OBJECT_NAME || DECODE(OBJECT_TYPE, 'PACKAGE BODY', ' compile body;', ' compile;') COMPILE
FROM ALL_OBJECTS
WHERE STATUS != 'VALID'
ORDER BY OWNER, OBJECT_TYPE, OBJECT_NAME;
```

**Solução:** Contatar Suporte TOTVS ou DBA

### Banco Local - Tabela com Lock

#### Verificar Locks

```sql
SELECT DISTINCT SES.PROGRAM EXECUTAVEL,
                OBJ.OBJECT_NAME TABELA,
                DECODE(LOC.LOCKED_MODE, 2, 'ROW SHARE', 3, 'ROW EXCLUSIVE',
                       4, 'SHARE', 5, 'SHARE ROW EXCL', 6, 'EXCLUSIVE', NULL) LOCKED_MODE,
                'alter system kill session ''' || SID || ',' || SERIAL# || ''' immediate;' COMANDO,
                SES.SID, SES.SERIAL#, SQL.SQL_TEXT
FROM V$SESSION SES, V$LOCKED_OBJECT LOC, DBA_OBJECTS OBJ, V$SQL SQL
WHERE SES.SID = LOC.SESSION_ID
AND LOC.OBJECT_ID = OBJ.OBJECT_ID
AND SES.SQL_ADDRESS = SQL.ADDRESS(+)
ORDER BY SES.LAST_CALL_ET DESC;
```

### Carga de Filial Nova

#### Pré-requisitos

1. **Avisar DBA** antes de qualquer carga
2. **Verificar configuração filiais:**

```sql
SELECT * FROM PCMXSCONFIGURACOES WHERE NOME LIKE '%FILIAL%';
```

Adicionar nova filial em:
- `CODFILIAL_PREST`
- `CODFILIAL_IMPORTACAO`

```sql
UPDATE PCMXSCONFIGURACOES 
SET VALOR = '[FILIAIS_ATUALIZADAS]' 
WHERE NOME = 'CODFILIAL_IMPORTACAO';
```

#### Script de Contagem

[Script em SQL/PL disponível na documentação]

#### Usar Website CARGATOTAL

📌 [http://cargatotal.maximatech.com.br](http://cargatotal.maximatech.com.br)

**Nota:** Use HTTP, não HTTPS

#### Passos

1. Selecionar cliente correto
2. Marcar nova filial na aba FILIAIS
3. Na aba GRUPOS DE TABELAS: selecionar 10 itens
4. Na aba PERÍODOS: colocar 3 meses atrás
5. Aguardar processamento

#### Acompanhar Carga

```sql
SELECT tabela, COUNT(1) 
FROM maxsolucoes.pcmxsintegracao 
WHERE status = '-1' 
GROUP BY tabela 
ORDER BY COUNT(1) DESC;
```

#### Se Filial Não Aparecer para RCA

1. Verificar permissão na Central
2. Executar carga de ATUALIZAID:

```sql
UPDATE MXSEST SET ATUALIZAID = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS')) 
WHERE CODFILIAL = [NOVA_FILIAL];
UPDATE MXSFILIAL SET ATUALIZAID = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS'));
UPDATE MXSPRODFILIAL SET ATUALIZAID = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS'));
UPDATE MXSEMBALAGEM SET ATUALIZAID = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS'));
UPDATE MXSTABPR SET ATUALIZAID = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS'));
UPDATE MXSPRODUT SET ATUALIZADI = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS'));
COMMIT;
```

---

<a name="referências"></a>
## 1️⃣4️⃣ REFERÊNCIAS E LINKS

### Documentação Oficial

| Recurso | Link |
|---------|------|
| Base de Conhecimento Máxima | https://basedeconhecimento.maximatech.com.br |
| Biblioteca Máxima | https://biblioteca.maximatech.com.br |
| Requisitos MinMáxima | https://maximatech.com.br/requisitos |
| Versões para Download | https://versoes.maximatech.com.br |

### Integração e APIs

| Recurso | Link |
|---------|------|
| Layout Integração Winthor | https://tdn.totvs.com/pages/releaseview.action?pageId=348295209 |
| Layout Integração MaxPedido | https://basedeconhecimento.maximatech.com.br/pages/viewpage.action?pageId=12189810 |
| Relatório 800 | https://biblioteca.maximatech.com.br/pages/viewpage.action?pageId=28311751 |

### Requisitos de Infraestrutura

| Serviço | Link |
|---------|------|
| Requisitos Cloud Winthor | https://maximatech.com.br/requisitos/cloud-tipo-erp/cloud-winthor/ |
| Testes de Porta | https://testedeportas.com/ |
| Ferramenta Port Check | https://www.yougetsignal.com/tools/open-ports/ |

### Downloads e Ferramentas

| Ferramenta | Link |
|-----------|------|
| MaxViewer Desktop | https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer_clientes.exe |
| MaxViewer APK | https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer.apk |
| MaxViewer Windows | https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer.exe |
| MaxViewer Linux (Debian/Ubuntu) | https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer-linux-installer-v1-x86_64.deb |
| MaxViewer Web | http://maxviewer.maximatech.com.br:21114 |

### MaxGestão

| Recurso | Link |
|---------|------|
| MaxGestão PWA | https://maxgestao-pwa.solucoesmaxima.com.br |
| Alternative Link | https://maxgestao-pwa.solucoesmaxima.com.br/login?callbackPath=%2F |

### TOTVS / Winthor

| Recurso | Link |
|---------|------|
| Central TOTVS | https://centraldeatendimento.totvs.com.br |
| TDN (TOTVS Developer Network) | https://tdn.totvs.com |

### Suporte

| Canal | Contato |
|-------|---------|
| Suporte Máxima | https://suporte.maximatech.com.br |
| Sankhya (DEV Studio) | https://dev-studios.atlassian.net/servicedesk/customer/portals |
| E-mail Integração | maxima.integracao@maximatech.com.br |
| ReceitaWS Support | contato@receitaws.com.br |

### Senhas Padrão (Apenas Interno)

⚠️ **CONFIDENCIAL - Apenas para suporte autorizado**

| Serviço | Senha |
|---------|-------|
| Banco Nuvem | mxma#maxpedidonuvem |
| Banco Local (Winthor) | mxMa#soluc1727 |
| Banco OTIO | M@xima#EfSlLDF |
| Banco Consulta | Con$ult@#0981 |
| Banco MaxSoluções | mxMa#soluc1727 |
| Portainer | maxsolucoes@portainer |
| Hangfire | maxsolucoes@extrator |

### Contatos Técnicos

| Pessoa | Especialidade | Contato |
|--------|--------------|---------|
| Felipe Integração | Sankhya | +55 27 98843-1292 |

---

## 📝 Notas Importantes

### Sobre Senhas e Segurança

- **Senhas padrão** devem ser alteradas em ambiente produção
- Nunca compartilhe credenciais por e-mail
- Use VPN quando acessar ambientes remotos

### Sobre Parâmetros

- Sempre testar em ambiente de homologação antes de produção
- Documentar todas as alterações realizadas
- Fazer backup antes de mudanças em massa

### Sobre Sincronização

- Após alterar parâmetros, sempre sincronizar o app
- Carga de ATUALIZAID pode ser necessária
- Aguardar os jobs do Hangfire completarem

### Sobre Integrações

- Validar sempre que banco local está atualizado
- Verificar triggers e procedures estão compiladas
- Monitorar logs do extrator

---

## 📞 Histórico de Revisões

| Data | Versão | Descrição |
|------|--------|-----------|
| 12/02/2026 | 1.0 | Documento reorganizado e estruturado |

---

**Documento preparado por:** Sistema de Suporte Máxima Tech  
**Última atualização:** 12 de fevereiro de 2026

---
