# Revisao de Documento Local: MAXIMA_RAG_UNIFICADO.md

## Fonte
- C:\revive-claude\bot-maxima\documentos\rag_unificado\MAXIMA_RAG_UNIFICADO.md

## Metadados
- Tipo detectado: `md`
- Gerado em: `2026-02-12T17:06:01.605312+00:00`
- Fatos extraidos (LangExtract): `0`
- Caracteres extraidos da fonte: `45851`

## Conhecimento Extraido
_Nenhum fato estruturado extraido._

## Texto Bruto Extraido
```text
# MAXIMA RAG UNIFICADO - Service Desk, Configuracao, Operacao e SQL

Documento mestre unificado para ingestao RAG do projeto.

Data de consolidacao: 2026-02-12  
Idioma: Portugues tecnico (ASCII)  
Politica de seguranca: sem segredos (senhas, tokens e credenciais reais removidos)

---

## 0. Escopo, Seguranca e Como Consultar

- section_id: SEC-00
- dominio: governanca_rag
- intencao_de_busca:
  - "Qual o escopo deste documento?"
  - "Como ingerir no banco vetorial sem duplicidade?"
  - "Qual a regra para dados sensiveis?"
- entidades:
  - documentos/rag_unificado/MAXIMA_RAG_UNIFICADO.md
  - ingest.py
  - config.py
- fontes:
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/SERVICE_DESK_MAXIMA_ORGANIZADO.md
  - documentos/organizacao/01-PARAMETROS-E-CONFIGURACAO.md
  - documentos/organizacao/02-PEDIDOS-E-VENDAS.md
  - documentos/organizacao/03-CAMPANHAS-E-DESCONTOS.md
  - documentos/organizacao/04-ROTAS-VISITAS-E-CONSULTAS.md
  - documentos/organizacao/05-SQL-BANCO-E-INTEGRACAO.md
  - documentos/organizacao/ARTIGOS_BASE.md
  - documentos/organizacao/maxPag.md
  - documentos/organizacao/GLOSSARIO.MD
  - documentos/organizacao/CARGATOTAL.MD
  - documentos/organizacao/CONTROLE_FERIAS.md

### Contexto

Este documento substitui a consulta distribuida em multiplos arquivos de `documentos/organizacao` para uso no RAG.  
Precedencia aplicada na consolidacao:

1. Fonte primaria: `SERVICE-DESK-PROCESSOS.md`
2. Fontes secundarias: `01` a `05`, `ARTIGOS_BASE.md`, `maxPag.md`, `GLOSSARIO.MD`, `CARGATOTAL.MD`, `CONTROLE_FERIAS.md`
3. Em divergencia: manter fluxo mais completo e consistente com o conjunto de fontes; registrar observacao quando necessario.

### Procedimento

1. Para perguntas operacionais, consultar primeiro "Camada 1" de cada secao.
2. Para diagnostico tecnico, usar "Camada 2" (queries, tabelas e parametros).
3. Para rastreabilidade, usar a secao 11.

### Validacao (SQL/tabelas/parametros)

- Ingestao recomendada somente do documento unificado:

```powershell
py ingest.py ./documentos/rag_unificado --force
```

- Observacao: nao alterar ou apagar os originais de `documentos/organizacao`; apenas nao ingerir juntos com este documento para evitar redundancia vetorial.

---

## 1. Ecossistema e Fluxos E2E

- section_id: SEC-01
- dominio: ecossistema_integracao
- intencao_de_busca:
  - "O que e maxPedido no contexto do Service Desk?"
  - "Qual o fluxo E2E do pedido?"
  - "Onde termina a responsabilidade da Maxima e onde inicia a do ERP?"
- entidades:
  - maxPedido
  - maxGestao
  - maxPromotor
  - maxCatalogo
  - maxPag
  - MXSINTEGRACAOPEDIDO
  - MXSHISTORICOPEDC
- fontes:
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/SERVICE_DESK_MAXIMA_ORGANIZADO.md
  - documentos/organizacao/maxPag.md

### Contexto

Secao de entrada para entendimento do ecossistema Maxima e do fluxo ponta a ponta entre app, nuvem e ERP.

### Procedimento

1. Ler Camada 1 para entendimento funcional rapido.
2. Ler Camada 2 para diagnostico por responsabilidade e ponto de falha.

### Camada 1 - Guia operacional rapido

Produtos do ecossistema:

- maxPedido: app de forca de vendas (espelha rotina 316 Winthor)
- maxGestao: portal/app gerencial, acompanhamento de equipe e rotas
- maxPromotor: pesquisas, dashboards e relatorios
- maxCatalogo: exibicao de produtos
- maxPag: pagamentos PIX/cartao integrados ao fluxo de pedidos

Arquitetura de alto nivel:

1. APK maxPedido envia pedido para nuvem.
2. Pedido e gravado na `MXSINTEGRACAOPEDIDO`.
3. ERP consome via API (GET), processa internamente e retorna status (PUT).
4. Historico de posicoes retorna via `MXSHISTORICOPEDC`.
5. APK sincroniza e atualiza timeline.

### Camada 2 - Fluxo detalhado e responsabilidades

Fluxo canonico de pedido:

1. APK envia pedido para nuvem (Maxima).
2. Server grava na `MXSINTEGRACAOPEDIDO` status 0 (Maxima).
3. ERP realiza GET no endpoint de pedidos (ERP).
4. API marca status 2 "EnviadoParaErp" (Maxima).
5. ERP processa regras locais (ERP).
6. ERP realiza PUT de retorno status 4 (sucesso) ou 5 (erro) (ERP).
7. ERP envia historico de posicao (L, F, M, C etc.) (ERP).
8. APK sincroniza timeline (Maxima).

Pontos de fronteira de responsabilidade:

- Maxima: envio/recepcao API, persistencia nuvem, sincronizacao APK.
- ERP cliente/integradora: regra fiscal/comercial local, retorno de status/critica, historico de posicao.

### Validacao (SQL/tabelas/parametros)

Tabelas-chave do fluxo:

- `MXSINTEGRACAOPEDIDO`
- `MXSINTEGRACAOPEDIDO_LOGST`
- `MXSINTEGRACAOPEDIDOLOG`
- `MXSHISTORICOCRITICA`
- `MXSHISTORICOPEDC`
- `PCPEDCFV`, `PCPEDIFV`, `PCPEDC`, `PCPEDI`

Query de verificacao inicial:

```sql
SELECT * FROM MXSINTEGRACAOPEDIDO ORDER BY DTINCLUSAO DESC;
```

---

## 2. Parametros e Configuracao

- section_id: SEC-02
- dominio: parametros_permissoes
- intencao_de_busca:
  - "Qual parametro controla cada comportamento no app?"
  - "Quais configuracoes sao criticas para bloqueios, estoque e financeiro?"
  - "Como habilitar ferias de vendedor?"
- entidades:
  - MXSPARAMETRO
  - MXSPARAMETROVALOR
  - MXSPARAMFILIAL
  - MXSACESSODADOS
  - MXSACESSOENTIDADES
- fontes:
  - documentos/organizacao/01-PARAMETROS-E-CONFIGURACAO.md
  - documentos/organizacao/02-PEDIDOS-E-VENDAS.md
  - documentos/organizacao/03-CAMPANHAS-E-DESCONTOS.md
  - documentos/organizacao/04-ROTAS-VISITAS-E-CONSULTAS.md
  - documentos/organizacao/CONTROLE_FERIAS.md
  - documentos/organizacao/GLOSSARIO.MD
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md

### Contexto

Consolidacao de parametros de maior impacto operacional e do catalogo por categoria para consulta rapida no suporte.

### Camada 1 - Matriz de parametros criticos por cenario

| Cenario | Parametros principais | Efeito esperado |
|---|---|---|
| Bloquear item sem estoque | `BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE`, `BLOQUEAR_VENDA_ACIMA_DO_ESTOQUE` | Impede inserir/vender sem disponibilidade |
| Cliente bloqueado | `BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ`, `BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ`, `ACEITAVENDAAVISTACLIBLOQ`, `CON_ACEITAVENDABLOQ` | Permite ou bloqueia venda conforme politica |
| Limite de credito | `BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE`, `ATUALIZAR_LIMCRED_CLIENTE_POS_PEDIDO`, `EXIBIR_ALERTA_CREDITO_CLIENTE` | Controla bloqueio e exibicao de limite |
| Conta corrente (CC/Flex) | `CON_USACREDRCA`, `EXIBIR_SALDOCC_DISPONIVEL`, `GERAR_DADOS_CC_RCA`, `IMPEDIR_ABATIMENTO_SEMSALDORCA` | Habilita saldo CC e trava desconto sem saldo |
| Check-in e rota | `UTILIZA_CHECKIN_CHECKOUT`, `PERMITIR_PEDIDO_SEM_CHECKIN`, `OBRIGA_CHECKIN_CLIENTE_FORA_ROTA`, `BLOQ_RCA_COM_ROTA_PENDENTE` | Governanca de visita e pedido em rota |
| Visita avulsa | `OBRIGA_CHECKIN_VISITA_AVULSA` + permissao de usuario | Define obrigatoriedade de check-in em visita avulsa |
| Roteiro no cadastro de cliente | `HABILITA_CADASTRO_ROTA_CLIENTE` | Exibe aba de roteiro no cadastro/edicao |
| Mapa de oportunidades | `HABILITA_MAPA_OPORTUNIDADE` | Habilita menu e uso de prospeccao por mapa |
| Filial retira | `DEFINE_FILIAL_RETIRA_PADRAO`, `DESMEMBRAR_PED_FILIAL_RETIRA` | Define filial de retirada e desmembramento |
| Campanha progressiva | `USAR_CAMPANHA_DESCONTO_PROGRESSIVO`, `TIPO_DESC_PROGRESSIVO`, `APLICAR_CAMPANHA_DESCONTO_PRIORITARIA` | Regras de campanha progressiva |
| Lucratividade | `MOSTRAR_LUCRATIVIDADE_TOTAL_NEGOCIACAO`, `OCULTAR_LUCRATIVIDADE_PRODUTO` | Exibe/oculta indicadores na negociacao |
| Titulos e boleto | `ENVIAR_APENAS_TITULOS_VENCIDOS`, `EXIBIRTITULOSPAGOS`, `EXIBE_LINHA_DIGITAVEL`, `SOMAR_JUROS_TITULOS` | Controle de consulta/segunda via e calculo |
| MaxPag | `ATIVAR_JOBMAXPAG_EXTRATOR`, `PERMITIR_VENDA_CARTAO_CREDITO`, `AMBIENTE_MAXPAYMENT` | Controla extracao e ambiente financeiro |
| Ferias de vendedor | `HABILITA_FERIAS_VENDEDOR` + permissao "Ferias" | Inativa uso do app durante periodo cadastrado |

### Camada 2 - Catalogo estruturado por categoria

#### Parametros de GPS e rastreamento

- `GPS_TRACKING_ENABLED`
- `GPS_TRACKING_INTERVAL`
- `CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE`
- `GPS_IS_REQUIRED_CONFEC_PEDIDO`
- `GPS_UPDATE_COORDENADAS_SOMENTE_SE_NAO_PREENCHIDO`
- `GPS_EDGE_BLOCK`
- `GPS_EDGE_METERS_SIZE`
- `GPS_TRACKING_STARTTIME`
- `GPS_TRACKING_STOPTIME`

#### Parametros de check-in, visitas e rota

- `UTILIZA_CHECKIN_CHECKOUT`
- `PERMITIR_PEDIDO_SEM_CHECKIN`
- `OBRIGA_CHECKIN_CLIENTE_FORA_ROTA`
- `LIMITE_RAIO_CHECK_IN_OUT`
- `TEMPO_MIN_PERMANENCIA`
- `OBRIGAR_ATENDIMENTO_PARA_CHECKOUT`
- `QTD_MAX_PED_FORA_ROTA`
- `PERIODO_PED_FORA_ROTA`
- `BLOQ_RCA_COM_ROTA_PENDENTE`
- `BLOQ_RETRO_DIAS_ROTEIRO`
- `BLK_SYNC_ROTEIRO_PENDENTE`
- `DIAS_ATENDI_ROTEIRO_SEMANAL`
- `DIAS_ADIAMENTO_VISITA`
- `PERMITIR_DELETE_HISTORICOCOMP`
- `HABILITA_CADASTRO_ROTA_CLIENTE`
- `OBRIGA_CHECKIN_VISITA_AVULSA`
- `HABILITA_MAPA_OPORTUNIDADE`

#### Parametros de pedidos e bloqueios

- `UTILIZA_PRE_PEDIDO`
- `VERIFICAR_QTD_MAX_ITENS_PEDIDO`
- `VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO`
- `PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO`
- `HABILITAR_DADOS_ENTREGA`
- `DIAS_EDICAO_PEDIDO`
- `HABILITA_PED_CLI_NAO_SINC`
- `HABILITA_PED_CLI_RECEM_CADASTRADO`
- `TRUNCAR_ITEM_PCPEDI`
- `PERMITE_INICIAR_PEDIDO_COMO_ORCAMENTO_NAO_MOV_CC`
- `BLOQUEIA_ENVIO_ORCAMENTO_ERP`
- `INTERVALO_ENVIO_PEDIDOS_APK`
- `ENVIA_PEDIDOS_BALCAO`
- `ENVIA_PEDIDOS_CALL_CENTER`
- `ENVIA_PEDIDOS_TELEMARKETING`
- `BLK_CONN_CONSIDERAORCBLOQCOMOPEND`
- `BLK_CONN_CONSIDERAPEDBLOQCOMOPEND`
- `BLK_CONN_INTERVALOCONEXAO`
- `BLK_CONN_PRIMEIRACONEXAO`
- `BLK_CONN_QTDEORCPENDENTE`
- `BLK_CONN_QTDEPEDPENDENTE`

#### Parametros de credito, bloqueio e financeiro

- `BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ`
- `BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ`
- `ALERTAR_TIT_VENCIDO`
- `NUMERO_DIAS_CLIENTE_INADIMPLENTE`
- `BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE`
- `ALERTAR_TIT_INADIMPLENTE`
- `BLOQUEIA_PEDIDO_CLIENTE_SEMLIMITE`
- `ACEITAVENDAAVISTACLIBLOQ`
- `ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO`
- `CON_ACEITAVENDABLOQ`
- `BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE`
- `CON_PEREXCEDELIMCRED`
- `ATUALIZAR_LIMCRED_CLIENTE_POS_PEDIDO`
- `EXIBIR_ALERTA_CREDITO_CLIENTE`

#### Parametros de conta corrente (CC/Flex)

- `CON_USACREDRCA`
- `EXIBIR_SALDOCC_DISPONIVEL`
- `APRESENTAR_CARD_CC`
- `GERAR_DADOS_CC_RCA`
- `DESCONTA_SALDOCCRCA_OFFLINE`
- `IMPEDIR_ABATIMENTO_SEMSALDORCA`
- `BLOQUEAR_SALVAR_PEDIDO_SEMSALDORCA`
- `DESABILITA_INSERCAO_ITEM_ACIMALIMITECREDITORCA`
- `EXIBIR_TODA_MOVIMENTACAO_CC`
- `CON_BONIFICALTDEBCREDRCA`
- `PERMITE_DESCONTAR_BONIF_CC_NEGATIVA`

#### Parametros de estoque, embalagem e catalogo

- `BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE`
- `BLOQUEAR_VENDA_ACIMA_DO_ESTOQUE`
- `DESABILITA_ALERTA_ESTOQUE`
- `EXIBE_ESTOQUE_FILIAL`
- `ENVIA_ESTOQUE_TODAS_FILIAIS`
- `ENVIA_NOTIFICACAO_ESTOQUE_TODAS_FILIAIS`
- `EXIBIR_ESTOQUE_BLOQUEADO`
- `EXIBIR_ESTOQUE_CONTABIL`
- `EXIBE_VALIDADE_PRODUTO_WMS`
- `USA_EMBALAGEM_UNIDADE_PADRAO`
- `USAR_MULTIPLO_QTDE`
- `INICIA_QTDE_UM`
- `HABILITAR_ARREDONDAMENTO_MULTIPLO`
- `EXIBIR_QUANTIDADE_SEM_FATOR_EMBALAGEM`
- `ATIVAR_NOTIFICACAO_EMBALAGEM_MASTER`
- `LISTAR_PRODUTOS_POR_EMBALAGENS`
- `VALIDARMULTIPLOVENDA`

#### Parametros de desconto, campanha e lucratividade

- `CON_ACEITADESCPRECOFIXO`
- `USAR_CAMPANHA_DESCONTO_PROGRESSIVO`
- `TIPO_DESC_PROGRESSIVO`
- `APLICAR_CAMPANHA_DESCONTO_PRIORITARIA`
- `NOTIFICAR_PRODUTO_CAMPANHA_3306`
- `EXIBIR_SUGESTAO_PRECO_COMISSAO`
- `HABILITA_LUCRATIVIDADE_ALTERNATIVA`
- `MOSTRAR_LUCRATIVIDADE_TOTAL_NEGOCIACAO`
- `OCULTAR_LUCRATIVIDADE_PRODUTO`

#### Parametros de pagamento, cobranca, titulos e espelho

- `LISTAR_TODOS_PLANOS_PAGAMENTO`
- `ORDENACAO_PLANO_PAGAMENTO`
- `VALIDAR_PRAZOMEDIO_COBRANCA_DH`
- `CON_CODPLPAGINICIAL`
- `CONFIRMAR_ALTERACAO_PLANO_PAGTO`
- `SOMAR_JUROS_TITULOS`
- `ENVIAR_APENAS_TITULOS_VENCIDOS`
- `EXIBIRTITULOSPAGOS`
- `EXIBE_PREV_COMISSAO`
- `EXIBIR_TAXABOLETO`
- `HABILITAR_SOMA_MULTA_TITULO`
- `APENAS_TITULOS_FILIAIS_PERM`
- `FILTRAR_DADOS_TITULOS_RCA`
- `EXIBE_LINHA_DIGITAVEL`
- `EXIBIR_PRECO_UNIT_EMB`
- `APRESENTAR_DESCONTOS_PEDIDO_EMAIL`
- `OCULTAR_IMPOSTOS_PEDIDO_EMAIL`
- `OCULTAR_VALIDADE_PROPOSTA`
- `EXIBIR_FOTO_DO_PRODUTO_PDF`
- `EXIBIR_FOTO_DO_PRODUTO_PERSONALIZADO_PDF`
- `DESABILITAR_ESPELHO_PED_PADRAO`

#### Parametros de filial, tributacao e cadastro

- `PERMITE_FILIAL_NF_NULA`
- `GRAVAR_FILIAL_NF_NULO`
- `USA_FILIALNF_CLIENTE_PARA_DEFINIR_TRIBUTACAO`
- `COMPORTAMENTO_WHINTOR_FILIAL`
- `DEFINE_FILIAL_RETIRA_PADRAO`
- `FILIALNF_DEFINE_FILIAL_PEDIDO`
- `CALCULAR_ST_SAIDA`
- `DESATIVA_VALIDACAO_CNPJ_CADASTRADO`
- `CLIENTESIMPLESNACIONAL_SIM`
- `CLIENTECONTRIBUINTE_SIM`
- `DESABILITA_CADASTRO_PESSOA_FISICA`
- `ENVIAR_CLIENTES_RCA_9999`
- `LIST_CLI_CPFCNPJ`
- `FILTRAR_CLIENTES_CONSUMIDOR_FINAL`
- `HABILITA_CLIENTES_BLOQUEIO_DEFINITIVO`
- `BLOQUEIA_PRACA_PADRAO`
- `COD_PRACA_PADRAO`
- `HABILITA_ENVIAR_TODAS_AS_PRACAS_PARA_RCA`
- `DIAS_ATUALIZACAO_CADASTRO_CLIENTE`
- `FORCAR_ATUALIZACAO_CADASTRO_CLIENTE`
- `HABILITA_ALERTA_CLIENTE_OBS`
- `CON_VLMAXVENDAPF`

#### Parametros de mix, consulta e comunicacao

- `GERAR_DADOS_MIX_CLIENTES`
- `GERAR_DADOS_MIX_CLIENTES_DIAS`
- `FILTRAR_DADOS_RCA_MIXVENDIDO`
- `FILTRAR_FILIAL_MIX`
- `GERAR_DADOS_POS_CLIENTES`
- `GERAR_DADOS_POS_PRODUTOS`
- `AGRUPAR_RELPOSITIVCLIENTE_FORNEC`
- `HABILITA_RECOMENDACAO_PRODUTOS`
- `EXIBE_SUGESTAO_VENDA`
- `FILTRAR_HISTCOMPRAS_RCA`
- `FILTRAR_DADOS_RCA`
- `FILTRAR_DADOS_CONSULTA_POSITIVACAO_RCA`
- `CATALOGO_PEDIDOS_DIAS_SYNC`
- `CONFIRMAR_PROCESSO_SYNC`
- `HABILITAR_CONEXAO_SINC`
- `BAIXAR_FOTOSPROD_APENAS_WIFI`
- `APRESENTAR_MSG_POS_ENVIO`
- `BLOQ_MARCAR_MSG_COMO_LIDA`
- `EXCLUIR_SOMENTE_LIDAS`
- `HABILITAR_GERADOR_RELATORIOS`
- `OCULTAR_COMISSAO_MENU`
- `BLOQ_PERIODO_MENU_RCA`

#### Parametros de metas, integracoes e outros

- `CRITERIOVENDAFDEDUZIRDEV`
- `CRITERIOVENDAFCONSIDERADEVAVULSA`
- `OBRIGAR_PREVISAO_FATURAMENTO`
- `PRAZO_VALIDADE_PREVISAOFATURAMENTO`
- `PREVISAO_FATURAMENTO_DIA_MAIS_UM`
- `CONSIDERAR_DATA_ATUAL_PREV_FAT`
- `HABILITA_MAXPESQUISA`
- `HABILITA_VENDA_ASSISTIDA`
- `VALIDAR_FILTRO_BRINDEX`
- `CON_USATROCACOMPRECOVENDA`
- `EDITAR_VALOR_FRETE`
- `HABILITA_CHKBOX_AGRUPAMENTO`
- `HABILITAR_VISUALIZACAO_COD_FAB_PROD_TAB`
- `HABILITA_FERIAS_VENDEDOR`

### Procedimento

Padrao para habilitacao na central:

1. Acessar `Configuracoes -> Parametros`.
2. Pesquisar parametro exato.
3. Editar e atribuir escopo correto (geral/usuario/filial).
4. Salvar.
5. Sincronizar APK.
6. Validar efeito no app e via SQL.

### Validacao (SQL/tabelas/parametros)

```sql
SELECT NOME, TIPODADO, TIPOPARAMETRO FROM MXSPARAMETRO WHERE NOME = :nome_parametro;
SELECT NOME, VALOR, CODUSUARIO FROM MXSPARAMETROVALOR WHERE NOME = :nome_parametro;
SELECT NOME, VALOR, CODFILIAL FROM MXSPARAMFILIAL WHERE NOME = :nome_parametro;
```

---

## 3. Pedidos, Status e Timeline

- section_id: SEC-03
- dominio: pedidos_timeline
- intencao_de_busca:
  - "Qual o significado de cada status do pedido?"
  - "Por que o pedido ficou preso em status 0/5?"
  - "Como corrigir timeline sem atualizacao?"
- entidades:
  - MXSINTEGRACAOPEDIDO
  - MXSHISTORICOPEDC
  - MXSINTEGRACAOCLIENTE
  - MXSINTEGRACAOPEDIDO_LOGST
- fontes:
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/02-PEDIDOS-E-VENDAS.md
  - documentos/organizacao/05-SQL-BANCO-E-INTEGRACAO.md
  - documentos/organizacao/SERVICE_DESK_MAXIMA_ORGANIZADO.md

### Contexto

Secao de referencia para leitura de status do ciclo de pedido e diagnostico de travamentos de timeline/integracao.

### Procedimento

1. Identificar status atual da `MXSINTEGRACAOPEDIDO`.
2. Correlacionar com status de timeline e historico (`MXSHISTORICOPEDC`).
3. Executar queries da secao de validacao.

### Camada 1 - Tabela canonica de status

#### Status MXSINTEGRACAOPEDIDO

| Status | Descricao |
|---|---|
| 0 | RecebidoPeloServer |
| 1 | EnviadoParaApi |
| 2 | EnviadoParaErp |
| 3 | RecebidoPeloErp |
| 4 | ProcessadoPeloErp |
| 5 | ErroProcessamentoErp |
| 6 | PedidoBloqueadoEnvioErp |
| 7 | PedidoBloqueadoCancelado |
| 8 | PedidoPendenteAutorizacao |
| 9 | PedidoAprovado |
| 10 | PedidoNegado |
| 11 | PedidoGravadoFV (job Winthor) |
| 12 | CancelamentoPedido |
| 13 | CarregamentoNaoImportado |
| 14 | ErroIntegracaoErp |
| 15 | CancelamentoPedidoERP |
| 16 | Aguardando geracao do link maxPayment |
| 17 | Erro ao gerar link maxPayment |
| 18 | Aguardando utilizacao do link maxPayment |
| 19 | Falta de colunas para utilizacao do maxPayment |
| 20 | Erro ao processar solicitacao no maxPayment |
| 21 | Em processamento no maxPayment |
| 22 | Solicitacao cancelada no maxPayment |
| 23 | Validade do link incorreta no maxPayment |

#### Status da timeline APK (resumo)

| Timeline | Significado |
|---|---|
| 0 | Pedido salvo no aparelho |
| 1 | Pedido gravado na nuvem |
| 2 | Pedido bloqueado na nuvem |
| 3 | Aguardando autorizacao |
| 4 | Cancelado pelo usuario |
| 5 | Gravado no ERP |
| 6 | Rejeitado pelo ERP |
| 7-13 | Posicoes de historico (P, L, B, M, F, C, O) |
| 14 | Autorizacao rejeitada |

### Camada 2 - Diagnostico e correcoes

#### Timeline nao atualiza (Outros ERPs)

Regra obrigatoria:

1. `MXSINTEGRACAOPEDIDO.DTABERTURAPEDPALM` deve existir no envio.
2. ERP deve devolver o mesmo `DTABERTURAPEDPALM` em `MXSHISTORICOPEDC`.
3. Sem esse retorno, a timeline nao consolida corretamente.

#### Pedido preso na APK / nao chega ao ERP

Checar:

1. `BLOQUEIA_PEDIDO_CLIENTE_SEMLIMITE` (pedido pode ficar preso por limite).
2. Status da `MXSINTEGRACAOPEDIDO` em (0, 5, 11).
3. Saude de extrator/jobs e fila.

#### Reenvio de critica (quando aplicavel)

- Validar integracao de `MXSHISTORICOCRITICA`.
- Reenviar retorno via endpoint de status conforme rotina do integrador.

### Validacao (SQL/tabelas/parametros)

```sql
-- Pedidos pendentes por status
SELECT * FROM MXSINTEGRACAOPEDIDO
WHERE DTINCLUSAO IS NOT NULL
  AND STATUS IN (0,1,2,5);

-- Processados no dia com critica
SELECT * FROM MXSINTEGRACAOPEDIDO
WHERE STATUS = 4
  AND TRUNC(DATA) = TRUNC(SYSDATE)
  AND CRITICA NOT LIKE '%{}%';

-- Verificar retorno da data de abertura para timeline (Outros ERPs)
SELECT DTABERTURAPEDPALM, NUMPEDPALM, NUMPED
FROM MXSHISTORICOPEDC
WHERE NUMPEDPALM = :numpedpalm;

SELECT DTABERTURAPEDPALM, NUMPEDPALM, CODCLI
FROM MXSINTEGRACAOPEDIDO
WHERE NUMPEDPALM = :numpedpalm;
```

---

## 4. Campanhas, Descontos e Lucratividade

- section_id: SEC-04
- dominio: campanhas_descontos_lucratividade
- intencao_de_busca:
  - "Qual a diferenca entre MQT, SQP, MIQ e FPU?"
  - "Como funciona desconto progressivo?"
  - "Como validar margem/lucratividade?"
- entidades:
  - MXSDESCONTOC
  - MXSDESCONTOI
  - MXSCAMPANHAFAMILIA
  - MXSCAMPANHAFAIXAS
  - MXSTABPR
  - PCEST
- fontes:
  - documentos/organizacao/03-CAMPANHAS-E-DESCONTOS.md
  - documentos/organizacao/ARTIGOS_BASE.md
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/GLOSSARIO.MD

### Contexto

Consolidacao das campanhas de desconto, regras progressivas e validacoes de lucratividade usadas no app.

### Procedimento

1. Classificar o tipo de campanha (MQT, SQP, MIQ, FPU).
2. Validar parametros de desconto/lucratividade.
3. Confirmar carga de tabelas da campanha e sincronizacao.

### Camada 1 - Comparativo de campanhas

| Tipo | Objetivo | Regra-base |
|---|---|---|
| MQT | Mix por quantidade minima | Desconto apos atingir quantidade minima em grupo de itens |
| SQP | Quantidade por subcategoria | Faixas de desconto por volume em subcategorias |
| MIQ | Intervalo de quantidade | Desconto valido dentro de minimo e maximo por item |
| FPU | Faixa unica de pedido | Regras/faixas unicas, podendo exigir produtos obrigatorios |

Regras operacionais comuns no app:

1. Itens de campanha aparecem com destaque visual.
2. Edicao/exclusao deve ser feita na aba de campanhas.
3. Em FPU, todas as validacoes necessarias devem estar atendidas para incluir itens.

### Camada 2 - Desconto progressivo e lucratividade

#### Desconto progressivo

- Parametros centrais:
  - `USAR_CAMPANHA_DESCONTO_PROGRESSIVO`
  - `TIPO_DESC_PROGRESSIVO`
  - `APLICAR_CAMPANHA_DESCONTO_PRIORITARIA`
- Tabelas comuns:
  - `MXSCAMPANHAFAMILIA`
  - `MXSCAMPANHAFAIXAS`
  - `MXSDESCESCALONADOC`, `MXSDESCESCALONADOI`, `MXSDESCESCALONADORESTRI`

#### Lucratividade

Formula padrao por item:

```text
((PVENDA - VLCUSTOFIN) / PVENDA) * 100
```

Formula por pedido (resumo):

```text
((VLATEND - VLCUSTOFIN) / VLATEND) * 100
```

Variacao alternativa:

- Pode usar `VALORULTENT` (origem PCEST) em vez de `CUSTOFIN` quando habilitado no modelo alternativo.

Parametros de exibicao:

- `MOSTRAR_LUCRATIVIDADE_TOTAL_NEGOCIACAO`
- `OCULTAR_LUCRATIVIDADE_PRODUTO`

Desconto maximo:

- Validar `PERDESCMAX` em `MXSTABPR` e em regras por cliente/regiao.

### Validacao (SQL/tabelas/parametros)

```sql
SELECT PERDESCMAX, CODCLI, CODTAB FROM MXSTABPR WHERE CODPROD = :codprod;
SELECT * FROM MXSDESCONTOC WHERE CODIGO = :codigo;
SELECT * FROM MXSDESCONTOI WHERE CODIGO = :codigo;
SELECT * FROM MXSCAMPANHAFAMILIA WHERE CODIGO = :codigo;
SELECT * FROM MXSCAMPANHAFAIXAS WHERE CODIGO = :codigo;
```

---

## 5. Rotas, Visitas e Consultas

- section_id: SEC-05
- dominio: roteiro_visita_consultas
- intencao_de_busca:
  - "Como habilitar roteiro no cadastro de cliente?"
  - "Como configurar visita avulsa?"
  - "Como usar consultas (positivacao, titulos, historico)?"
- entidades:
  - MXSCOMPROMISSOS
  - MXSHISTORICOCOMPROMISSOS
  - ERP_MXSROTACLI
  - HABILITA_CADASTRO_ROTA_CLIENTE
  - OBRIGA_CHECKIN_VISITA_AVULSA
  - HABILITA_MAPA_OPORTUNIDADE
- fontes:
  - documentos/organizacao/04-ROTAS-VISITAS-E-CONSULTAS.md
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/05-SQL-BANCO-E-INTEGRACAO.md
  - documentos/organizacao/CONTROLE_FERIAS.md

### Contexto

Reune o fluxo de roteiro, visitas avulsas, consultas operacionais do app e bloqueio por ferias.

### Procedimento

1. Validar permissao/perfil.
2. Validar parametro relacionado ao fluxo.
3. Validar dados de roteiro/cadastro no ERP e nuvem.

### Camada 1 - Fluxos operacionais

#### Cadastro/edicao de rota no app

1. Habilitar `HABILITA_CADASTRO_ROTA_CLIENTE`.
2. Garantir que formulario de cliente nao esteja ocultando roteiro.
3. No app, acessar cliente e usar aba "Roteiro de Visitas".

#### Roteiro de visita

- Roteiro e configurado no ERP e validado no app.
- App permite visualizar agenda do dia e outros dias.
- Acoes por cliente no roteiro incluem justificativa de visita.

#### Visita avulsa

1. Habilitar permissao do usuario para visita avulsa.
2. Ajustar `OBRIGA_CHECKIN_VISITA_AVULSA` conforme regra do cliente.

#### Mapa de oportunidades

1. Habilitar `HABILITA_MAPA_OPORTUNIDADE`.
2. Configurar perfil (CNAE, distancia e filtros).
3. Usar menu de mapa no app para prospeccao e tracar rota.

#### Consultas no aplicativo

- Positivacao de clientes
- Titulos
- Notificacao de estoque
- Politicas comerciais
- Historico de pedidos
- Aniversarios

### Camada 2 - Ferias de vendedor

Permissao e parametro:

1. Em cadastro de usuarios, habilitar rotina "Ferias" no acesso a rotinas.
2. Em parametros, habilitar `HABILITA_FERIAS_VENDEDOR`.
3. Cadastrar periodo de ferias no menu de cadastro.

Efeito esperado:

- Inativa uso do maxPedido, captura de geolocalizacao e acesso durante o periodo.

### Validacao (SQL/tabelas/parametros)

```sql
-- Roteiro ERP
SELECT * FROM PCROTACLI
WHERE DTPROXVISITA BETWEEN TO_DATE(:dt_inicio,'DD/MM/YYYY') AND TO_DATE(:dt_fim,'DD/MM/YYYY')
  AND CODUSUR = :codusur;

-- Roteiro nuvem
SELECT CODUSUARIO, CODCLI, DTINICIO, DTTERMINO
FROM MXSCOMPROMISSOS
WHERE CODUSUARIO = :codusuario
  AND CODCLI = :codcli;
```

---

## 6. MaxPag (Fluxo Financeiro e Integracao)

- section_id: SEC-06
- dominio: maxpag_financeiro
- intencao_de_busca:
  - "Como funciona o fluxo maxPedido + maxPag?"
  - "O que significa status 18 no maxPayment?"
  - "Como diagnosticar falhas de link, captura e estorno?"
- entidades:
  - MXSMAXPAYMENTMOV
  - MXSINTEGRACAOPEDIDO_LOGST
  - ATIVAR_JOBMAXPAG_EXTRATOR
  - PERMITIR_VENDA_CARTAO_CREDITO
  - AMBIENTE_MAXPAYMENT
- fontes:
  - documentos/organizacao/maxPag.md
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/ARTIGOS_BASE.md
  - documentos/organizacao/05-SQL-BANCO-E-INTEGRACAO.md

### Contexto

Consolidacao do fluxo assincrono de pagamento com mensageria, extrator e fechamento financeiro pos-ERP.

### Procedimento

1. Validar etapa atual do fluxo (link, pagamento, integracao, pos-ERP).
2. Correlacionar evento tecnico com status de pedido.
3. Conferir tabelas de movimento financeiro e log de status.

### Camada 1 - Fluxo operacional resumido

1. Pedido criado na APK com cobranca vinculada ao maxPag (PIX/cartao).
2. Server PDV valida regras comerciais e fiscais.
3. Se exigido, ocorre autorizacao previa (ex: desconto).
4. Server solicita geracao de link ao maxPag.
5. maxPag publica evento em fila; server consome e devolve status.
6. Cliente paga pelo link (PIX/cartao).
7. Confirmacao financeira volta por mensageria.
8. JOB extrator integra pedido no ERP.
9. Pos-ERP: faturamento/cancelamento dispara captura/estorno adequado.

### Camada 2 - Diagnostico tecnico

#### Parametros de controle

- `ATIVAR_JOBMAXPAG_EXTRATOR`
- `PERMITIR_VENDA_CARTAO_CREDITO`
- `AMBIENTE_MAXPAYMENT` (0 homologacao, 1 producao)

#### Pontos de diagnostico por ticket

1. Pedido foi autorizado no maxGestao?
2. Link foi gerado?
3. Evento entrou na fila?
4. Server consumiu evento?
5. Confirmacao de pagamento foi publicada?
6. JOB extrator esta ativo?
7. Pedido chegou ao ERP?
8. ERP retornou faturado ou cancelado?
9. Captura/estorno foi executado?

#### Cenarios pos-ERP

- Cancelado: cancelamento/estorno ou cancelamento de pre-autorizacao.
- Faturado sem corte: captura total (cartao) ou conclusao sem estorno (PIX).
- Faturado com corte: captura parcial + cancelamento de saldo pre-autorizado (cartao), estorno parcial (PIX).

### Validacao (SQL/tabelas/parametros)

```sql
SELECT * FROM MXSMAXPAYMENTMOV
WHERE ID_PEDIDO = :id_pedido
ORDER BY DATA_MOVIMENTACAO DESC;

SELECT * FROM MXSINTEGRACAOPEDIDO_LOGST
WHERE ID_PEDIDO = :id_pedido
ORDER BY DATA_STATUS DESC;
```

---

## 7. SQL, Banco e Infra (Runbooks)

- section_id: SEC-07
- dominio: sql_banco_infra
- intencao_de_busca:
  - "Qual SQL usar para cada incidente?"
  - "Como validar locks no Oracle?"
  - "Quais runbooks de extrator/portainer/hangfire?"
- entidades:
  - MXSINTEGRACAOPEDIDO
  - PCMXSINTEGRACAO
  - MXSAPARELHOSCONNLOG
  - V$SESSION
  - DBA_WAITERS
  - Portainer
  - Hangfire
- fontes:
  - documentos/organizacao/05-SQL-BANCO-E-INTEGRACAO.md
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/SERVICE_DESK_MAXIMA_ORGANIZADO.md

### Contexto

Indice de runbooks SQL para atendimento e bloco de queries canonicas para incidentes recorrentes.

### Procedimento

1. Selecionar o runbook pelo sintoma.
2. Rodar query canonica em ambiente correto.
3. Comparar resultado com esperado e registrar evidencia.

### Camada 1 - Indice de runbooks SQL (74 cenarios)

- ATUALIZID PADRAO
- STATUS DOS PEDIDOS NA MXSINTEGRACAOPEDIDOS
- PEDIDOS NUVEM
- SINCRONIZACAO
- CONEXOES E APARELHOS
- CONSULTAR SUPERVISORES
- QUANTIDADE DE RCA QUE JA CONECTARAM
- RCAS QUE JA PASSARAM PEDIDOS
- RCA ATIVOS/INATIVOS
- RELACAO DE LOGIN
- CONSULTAR FOTOS DE PRODUTOS
- ITENS DO PEDIDO PELO JSON
- TITULOS ABERTOS COM STATUS 51
- DEIXAR APENAS TITULOS VENCIDOS NA APK
- DATA DOS PEDIDOS
- USUARIOS COM VERSAO DIFERENTE
- DESCONTO PROGRESSIVO (CAMPANHA COLGATE / P&G)
- LIMPAR REGISTRO PCMXSINTEGRACAO
- CONSULTAR PEDIDO JSON (SCHEMA ESPECIFICO)
- JOBS DO BANCO ORACLE
- PROCURAR TABELA E COLUNA NO ORACLE
- SERVICE NAME DO ORACLE
- SESSOES BLOQUEADAS (LOCKED)
- SESSAO ABERTA DE USUARIO ORACLE
- CRIAR USUARIO NO ORACLE
- GRANTS MAXSOLUCOES
- VERIFICAR PRODUTOS DUPLICADOS
- VERIFICAR CLIENTES DUPLICADOS NA PCCLIENTFV
- ENVIAR INFORMACOES COMPLETAS DE UMA TABELA AOS VENDEDORES
- MIX DE PRODUTOS VENDIDOS NO MES
- REGISTROS DO HISTORICO
- NORMALIZAR INFORMACOES MXSMOV
- CONSULTAR PEDIDO E FILIAL
- PEDIDOS PENDENTES NO APARELHO
- CONSULTAR MARGEM DE LUCRATIVIDADE
- COMPARAR MXSTABPR COM PCTABPR
- CONSULTAR REGIAO E PRACA DO CLIENTE
- IMPOSTO DO PRODUTO
- IMPOSTO PELO CLIENTE
- CONSULTAR PLANO DE PAGAMENTO
- VERIFICAR METAS
- CONSULTAR CLIENTE PARA RCA
- VALIDAR COMPRAS
- NORMALIZACAO AO ALTERAR PARAMETRO DE HISTORICO DE PEDIDOS
- CONSULTAR PARAMETRO 132
- CONSULTAR LIMITE DE CREDITO
- CONSULTAR COMISSAO
- CERCA ELETRONICA
- CONSULTAR ORCAMENTO
- CONSULTAR VERSAO WINTHOR
- ULTIMOS PRODUTOS VENDIDOS (12 MESES)
- VERIFICAR VALIDADE DO PRODUTO
- VERIFICAR HISTORICO DE PEDIDOS DO RCA COM CLIENTE
- VERIFICAR SE O CLIENTE ESTA BLOQUEADO
- REGIAO DO CLIENTE
- CONSULTAR CESTA
- PRODUTO NAO APARECE
- AUTORIZACAO DE PRECO
- VERIFICAR ROTEIRO
- CAMPANHA NAO APARECE AO RCA
- NUMERO PEDIDO RCA
- PEDIDOS NA INTEGRADORA
- INDENIZACAO
- PROCESSAMENTO DO CADASTRO DE CLIENTE
- RECRIAR JOB
- UPDATE PARA MAIS DE UMA TABELA
- CRIAR TABLESPACE
- TV7 - COMPORTAMENTO INTEGRADORA
- AJUSTAR PROBLEMA DE ROTA DNS LINUX
- TIMEZONE LINUX
- MIGRACAO RANCHER PARA PORTAINER
- COMPOSE DO EXTRATOR NO PORTAINER
- RELATORIO DA ROTINA 800
- RELATORIO DE PRODUTO COM CLASSIFICACAO DE PRECO

### Camada 2 - Queries canonicas por tema

#### Reenvio e sincronizacao

```sql
-- Padrao de reenvio
-- usar na tabela alvo conforme caso
UPDATE TABELA_ALVO SET ATUALIZID = '-9999999999' WHERE CONDICAO;
COMMIT;

-- Pendencias na integracao
SELECT TABELA, COUNT(1)
FROM PCMXSINTEGRACAO
WHERE STATUS = '-1'
GROUP BY TABELA
ORDER BY COUNT(1) DESC;
```

#### Pedidos e status

```sql
SELECT * FROM MXSINTEGRACAOPEDIDO ORDER BY 3 DESC;

SELECT * FROM MXSINTEGRACAOPEDIDO
WHERE DTINCLUSAO IS NOT NULL
  AND STATUS IN (0,1,2,5);

SELECT ID_PEDIDO || ','
FROM MXSINTEGRACAOPEDIDO
WHERE STATUS NOT IN (4,6,7)
ORDER BY DTINCLUSAO ASC;
```

#### Conexoes e uso de aplicativo

```sql
SELECT CODUSUARIO, DTTERMINOCONEXAO, ERROR, APPVERSION
FROM MXSAPARELHOSCONNLOG
ORDER BY DTTERMINOCONEXAO DESC;

SELECT DISTINCT A.DEVICEINSTALLKEY, A.MARCA_APARELHO, A.MODELO_APARELHO,
       A.CODUSUARIO, U.NOME, U.LOGIN
FROM MXSAPARELHOSCONNLOG A
JOIN MXSUSUARIOS U ON U.CODUSUARIO = A.CODUSUARIO
WHERE DTINICIOCONEXAO > TRUNC(SYSDATE) - 1
ORDER BY U.NOME;
```

#### Locks Oracle

```sql
SELECT DISTINCT SID FROM V$MYSTAT;

SELECT SID, SERIAL#, STATUS, USERNAME, OSUSER, PROGRAM, BLOCKING_SESSION, EVENT
FROM V$SESSION
WHERE BLOCKING_SESSION IS NOT NULL;

SELECT WAITING_SESSION, HOLDING_SESSION FROM DBA_WAITERS;
SELECT * FROM V$LOCK WHERE BLOCK <> 0;
```

#### Plano de pagamento e bloqueios

```sql
SELECT * FROM PCPLPAGCLI WHERE CODCLI = :codcli ORDER BY CODPLPAG;
SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%FIL_BLOQUEARPEDIDOSABAIXOVLMINIMO%';
```

#### Produto nao aparece

```sql
UPDATE MXSPRODUT
SET ATUALIZID = 0
WHERE CODOPERACAO <> 2
  AND CODPROD IN (:codprod);
COMMIT;

SELECT OBS, OBS2, REVENDA, ENVIARFORCAVENDAS, DTEXCLUSAO, P.*
FROM PCPRODUT P
WHERE CODPROD IN (:codprod);
```

#### Roteiro e campanha

```sql
SELECT * FROM PCROTACLI
WHERE CODUSUR IN (:codusur)
  AND DTPROXVISITA = :data
ORDER BY SEQUENCIA;

SELECT * FROM MXSDESCONTOC WHERE CODIGO = :codigo;
SELECT * FROM MXSDESCONTOI WHERE CODIGO = :codigo;
```

### Infraestrutura e operacao

Runbook de verificacao:

1. Validar containers de extrator e Portainer em execucao.
2. Validar jobs recorrentes no Hangfire.
3. Validar conectividade com banco/endpoint.
4. Validar timezone e DNS em Linux quando houver divergencia de horario/rota.

Seguranca de infraestrutura:

- Qualquer referencia a senha/token deve usar placeholder.
- Exemplo: `[SENHA_REMOVIDA]`, `[TOKEN_REMOVIDO]`, `[CREDENCIAL_REMOVIDA]`.

### Validacao (SQL/tabelas/parametros)

```sql
SELECT NAME, VALUE FROM V$PARAMETER WHERE NAME LIKE '%job_queue_processes%';
SELECT VALUE FROM V$PARAMETER WHERE NAME = 'SERVICE_NAMES';
```

---

## 8. Tabelas por Dominio

- section_id: SEC-08
- dominio: modelo_dados
- intencao_de_busca:
  - "Qual tabela consultar por assunto?"
  - "Quais tabelas sao Winthor e quais sao nuvem Maxima?"
- entidades:
  - CARGATOTAL
  - tabelas MXS
  - tabelas PC
- fontes:
  - documentos/organizacao/CARGATOTAL.MD
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/SERVICE_DESK_MAXIMA_ORGANIZADO.md

### Contexto

Catalogo de tabelas por dominio para acelerar triagem tecnica e montagem de SQL por assunto.

### Procedimento

1. Identificar dominio funcional (pedido, cliente, estoque, financeiro etc.).
2. Selecionar tabelas da Camada 1 (nuvem) ou Camada 2 (Winthor/ERP).
3. Executar validacoes SQL na secao de referencia correspondente.

### Camada 1 - Tabelas-chave de nuvem Maxima

- Pedidos: `MXSINTEGRACAOPEDIDO`, `MXSINTEGRACAOPEDIDO_LOGST`, `MXSINTEGRACAOPEDIDOLOG`
- Historico/critica: `MXSHISTORICOCRITICA`, `MXSHISTORICOPEDC`, `MXSHISTORICOPEDI`
- Parametros: `MXSPARAMETRO`, `MXSPARAMETROVALOR`, `MXSPARAMFILIAL`, `MXSCONFIGERP`
- Usuarios/acesso: `MXSUSUARIOS`, `MXSACESSODADOS`, `MXSACESSOENTIDADES`, `MXSACESSOROTINAS`
- Clientes/rota: `MXSCLIENT`, `MXSUSURCLI`, `MXSCOMPROMISSOS`, `MXSHISTORICOCOMPROMISSOS`
- Produtos/preco: `MXSPRODUT`, `MXSTABPR`, `MXSPRECOPROM`, `MXSEMBALAGEM`, `MXSLOTE`
- Estoque: `MXSEST`, `MXSESTFILIAL`, `MXSESTCESTA`, `MXSVALIDADEWMS`
- Financeiro/maxPag: `MXSTITULOSABERTOS`, `MXSMAXPAYMENTMOV`

### Camada 2 - Base de tabelas por dominio (Winthor/ERP)

#### Brindes

- PCBRINDEEX
- PCBRINDEEXPREMIO
- PCBRINDEEXRESTRICOES
- PCBRINDEEXVALIDACOES

#### Campanhas

- PCDESCONTO
- PCDESCONTOC
- PCDESCONTOCATEGORIA
- PCDESCONTOCPRODRELAC
- PCDESCONTOI
- PCDESCONTORESTRICAO
- PCDESCQUANT
- PCGRUPOCOMBOCLIC
- PCGRUPOCOMBOCLII
- PCGRUPOCOMBOSKUC
- PCGRUPOCOMBOSKUCOMBO
- PCGRUPOCOMBOSKUFAIXA
- PCGRUPOCOMBOSKUFAIXAATIV
- PCGRUPOCOMBOSKUFAIXADESC
- PCGRUPOSCAMPANHAC
- PCGRUPOSCAMPANHAI
- PCPROMC
- PCPROMI
- PCPROMOC
- PCPROMOI
- PCDESCONTOITEM
- PCDESCONTOITEMLOG

#### Cliente

- PCATIVI
- PCCIDADE
- PCCLIENT
- PCCLIENTENDENT
- PCCLIREF
- PCCNAE
- PCCOBCLI
- PCCOMBOCLI
- PCCONTATO
- PCCRECLI
- PCMXSCLIENTECREDDISP
- PCMXSMIXCLIENTES
- PCPLPAGCLI
- PCPRACA
- PCPROFISSIONALCLI
- PCREDECLIENTE
- PCREGIAO
- PCSUPERV
- PCSUPPLICLIENTE
- PCSUPPLIPARAMFAT
- PCTABPRCLI
- PCUSURCLI

#### Comissoes

- PCCOMISSAOPLPAG
- PCCOMISSAOREGIAO
- PCCOMISSAOTERCEIROS
- PCCOMISSAOUSUR
- PCORDEMAPURACAOCOMIS
- PCTABCOMISS

#### Condicoes comerciais

- PCCOB
- PCCOBPLPAG
- PCFRETE
- PCPLPAG
- PCPLPAGFILIAL
- PCPLPAGI
- PCPRAZOADICIONAL
- PCTIPOBONIFIC
- PCPLPAGPARCELAS

#### Estoque

- PCMXSEST
- PCMXSESTCESTA
- PCMXSESTFILIAL
- PCMXSESTFUT
- PCMXSESTPEND

#### Filiais

- PCDATAS
- PCDIASUTEIS
- PCEMPR
- PCFILIAL
- PCFILIALRETIRA

#### Financeiro

- PCPLPAGVARIAVELJUROS
- PCPREST

#### Parametros

- PCPARAMETROS
- PCPARAMFILIAL
- PCCONSUM

#### Pedidos

- PCAUTORI
- PCAUTORNF
- PCCFO
- PCCONCOR
- PCMANASSUNTO
- PCMANIF
- PCMIXMINIMO
- PCMOTNAOCOMPRA
- PCMOTVISITA
- PCPEDC
- PCPEDI

#### Perfil e parametros (nuvem)

- MXSACESSODADOS
- MXSACESSOENTIDADES
- MXSACESSOROTINAS
- MXSCONFIG
- MXSCONFIGDATA
- MXSDADOS
- MXSMODULOS
- MXSPARAMETRO
- MXSPARAMETROVALOR
- MXSPERFILACESSO
- MXSPERFILDADOS
- MXSPERFILENTIDADES
- MXSPERFILROTINAS
- MXSROTINAS
- MXSROTINASI
- MXSUSUARIOS
- MXSPREPEDIDO
- MXSPREPEDIDOCLIENT
- MXSPREPEDIDOFILIAL
- MXSPREPEDIDOITENS
- MXSPREPEDIDORAMO
- MXSPREPEDIDOREGIAO
- MXSPREPEDIDOSUPERV

#### Positivacao

- PCMXSPRODUTMSK
- PCMXSPRODUTPOS
- PCMXSQTDEPRODVENDA

#### Preco

- PCMXSPRECOCESTAC
- PCMXSPRECOCESTAI
- PCMXSTABPRCESTA
- PCPRECOPROM
- PCTABPR

#### Produtos

- PCCATEGORIA
- PCDEPTO
- PCEMBALAGEM
- PCFORMPROD
- PCFORNEC
- PCLINHAPROD
- PCLOTE
- PCMARCA
- PCMXSVALIDADEWMS
- PCPRINCIPATIVO
- PCPRODFILIAL
- PCPRODSIMIL
- PCPRODUT
- PCPRODUTPICKING
- PCSECAO
- PCSETOR
- PCSUBCATEGORIA
- PCPRODMIXIDEAL

#### Restricoes de venda

- PCPLPAGRESTRICAO
- PCPRODUSUR
- PCRESTRICAOVENDA
- PCUSURDEPSEC
- PCUSURFORNEC

#### Roteirizacao

- PCROTACLI
- PCROTACLIFIXAC
- PCROTACLIFIXAI
- PCROTAEXP

#### Tributacao

- PCTABTRIB
- PCTRIBUT
- PCTRIBUTPARTILHA

#### Vendedor

- PCROTINA
- PCUSUARI

#### Logistica e gestao

- PCPARAMPLANOVOO
- PCBAIRRO
- PCCONFIGCAMPANHA
- PCCOORDENADORVENDA
- PCCORREN
- PCCORTE
- PCCORTEI
- PCESTADO
- PCESTCOM
- PCFALTA
- PCGERENTE
- PCGRUPOFILIAL
- PCHIST
- PCMETAC
- PCMETAFAIXA
- PCMETARCA
- PCNFCANITEM
- PCNFENT
- PCSUBMODULO
- PCVISITAFV
- PCDOCELETRONICO
- PCMOVSALDORCA
- PCCARREG
- PCDISTRIB
- PCINDC
- PCMOV
- PCMOVENDPEND
- PCNFSAID
- PCVEICUL
- PCVOLUMEOS
- PCTABDEV
- PCLOGRCA

### Validacao (SQL/tabelas/parametros)

```sql
SELECT * FROM ALL_TABLES WHERE TABLE_NAME IN ('MXSINTEGRACAOPEDIDO','MXSPARAMETRO','PCPEDC','PCCLIENT');
```

---

## 9. Troubleshooting por Sintoma

- section_id: SEC-09
- dominio: troubleshooting
- intencao_de_busca:
  - "Tenho erro X no app, o que validar primeiro?"
  - "Qual parametro e query devo usar por sintoma?"
- entidades:
  - MXSINTEGRACAOPEDIDO
  - MXSHISTORICOPEDC
  - MXSPARAMETRO
  - PCPARAMETROS
- fontes:
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md
  - documentos/organizacao/02-PEDIDOS-E-VENDAS.md
  - documentos/organizacao/03-CAMPANHAS-E-DESCONTOS.md
  - documentos/organizacao/04-ROTAS-VISITAS-E-CONSULTAS.md
  - documentos/organizacao/maxPag.md
  - documentos/organizacao/05-SQL-BANCO-E-INTEGRACAO.md

### Contexto

Base de resposta rapida para incidentes comuns, com mapeamento sintoma -> causa -> validacao -> acao.

### Procedimento

1. Encontrar sintoma na matriz.
2. Rodar validacao rapida indicada.
3. Executar acao recomendada e registrar resultado.

### Camada 1 - Matriz de incidente

| Sintoma | Causas comuns | Validacao rapida | Acao recomendada |
|---|---|---|---|
| Produto nao aparece | Fora de linha, restricao, distribuicao divergente | Checar `PCPRODUT`, `PCPRODFILIAL`, restricoes | Ajustar cadastro/restricao e forcar `ATUALIZID` |
| Campanha nao aparece | Regra/restricao/carga ausente | Checar `MXSDESCONTOC/I` e sync | Revisar vigencia/restricao e sincronizar |
| Timeline nao atualiza | Campo de data nao retornado pelo ERP | Comparar `DTABERTURAPEDPALM` entre tabelas | Corrigir retorno do integrador |
| Pedido preso status 0/5 | Extrator/job/fila ou bloqueio de credito | Checar status, jobs, limite cliente | Normalizar causa e reenfileirar fluxo |
| Erro tributacao produto | Filial NF ou regra tributaria incoerente | Checar filial/tributacao cliente/produto | Corrigir cadastro tributario |
| Custo financeiro invalido | Campos de custo inconsistentes | Checar custo em tabelas de produto/estoque | Ajustar custo base no ERP |
| Limite nao atualiza no app | Parametro/processo de limite incompleto | Checar params de limite e query de credito | Ajustar params e sincronizar |
| Cliente bloqueado com comportamento errado | Parametros conflitantes | Revisar matriz de bloqueio | Uniformizar politica em maxPedido + ERP |
| Filial retira nao desmembra | Parametro ou fluxo em autorizacao | Checar `DESMEMBRAR_PED_FILIAL_RETIRA` | Ajustar parametro e fluxo operacional |
| PDF/XLS nao gera | WebView desatualizado | Validacao no dispositivo Android | Atualizar/reinstalar WebView |
| Boleto nao abre/imprime | Linha digitavel indisponivel | Validar `EXIBE_LINHA_DIGITAVEL` e campos de titulo | Ajustar parametros e dados de titulo |
| Roteiro nao aparece | Sem roteiro no ERP ou parametro desabilitado | Checar `PCROTACLI` e `HABILITA_CADASTRO_ROTA_CLIENTE` | Corrigir roteiro/carteira e sincronizar |
| Visita avulsa nao cria | Sem permissao ou check-in bloqueando | Validar permissao e `OBRIGA_CHECKIN_VISITA_AVULSA` | Ajustar perfil/parametro |
| Mapa de oportunidades vazio | Filtros restritivos ou parametro off | Checar `HABILITA_MAPA_OPORTUNIDADE` e perfil | Ajustar raio/CNAE/perfil |
| Link maxPag nao gera | Token/vinculo/ambiente/filial | Validar token por filial e status 16/17 | Corrigir vinculo e ambiente |
| Ferias nao bloqueia acesso | Permissao/parametro/cadastro incompleto | Checar permissao "Ferias" + `HABILITA_FERIAS_VENDEDOR` | Ajustar cadastro e periodo |

### Camada 2 - Checklist padrao de atendimento N1/N2

1. Confirmar ambiente (producao/homologacao), usuario, filial e versao app.
2. Confirmar sincronizacao recente e horario do incidente.
3. Validar parametro no escopo correto (geral/usuario/filial).
4. Validar dados-base em tabela nuvem e ERP.
5. Executar query canonica do cenario.
6. Registrar evidencia: parametro, query, status e horario.
7. Se integracao externa/ERP: escalar com payload e retorno de status.

### Validacao (SQL/tabelas/parametros)

```sql
SELECT STATUS, COUNT(1)
FROM MXSINTEGRACAOPEDIDO
WHERE TRUNC(DTINCLUSAO) = TRUNC(SYSDATE)
GROUP BY STATUS;
```

---

## 10. Glossario Tecnico

- section_id: SEC-10
- dominio: glossario
- intencao_de_busca:
  - "O que significa termo X no contexto maxPedido?"
  - "Qual conceito operacional por tras de CC, bonificacao, meta e historico?"
- entidades:
  - CC/Flex
  - PERDESCMAX
  - EXIBE_LINHA_DIGITAVEL
  - MXSACESSODADOS
  - MXSACESSOENTIDADES
- fontes:
  - documentos/organizacao/GLOSSARIO.MD
  - documentos/organizacao/01-PARAMETROS-E-CONFIGURACAO.md
  - documentos/organizacao/SERVICE-DESK-PROCESSOS.md

### Contexto

Termos recorrentes no suporte:

- RCA: representante de vendas.
- CC/Flex: conta corrente do RCA para politica de desconto/acrescimo.
- Pre-pedido: modelo de pedido preconfigurado para direcionar venda.
- Filial retira: filial de estoque/retirada diferente da filial de venda.
- Timeline: historico de status de pedido no app.

### Procedimento

Definicoes funcionais consolidadas:

- Bloqueio de bonificacao sem saldo CC:
  - `CON_USACREDRCA = S`
  - `CON_BONIFICALTDEBCREDRCA = S`
  - `IMPEDIR_ABATIMENTO_SEMSALDORCA = S`
  - `PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N`
- Desconto maximo:
  - validar `PERDESCMAX` em tabela de preco e restricoes de cliente/regiao.
- Espelho do pedido:
  - `EXIBIR_PRECO_UNIT_EMB`, `EXIBIR_CAMPOS_ESPELHO_POR_EMBALAGEM`.
- Boleto:
  - `EXIBE_LINHA_DIGITAVEL = S`.
- Previsao de faturamento:
  - `OBRIGAR_PREVISAO_FATURAMENTO`
  - `PRAZO_VALIDADE_PREVISAOFATURAMENTO`
  - `PREVISAO_FATURAMENTO_DIA_MAIS_UM`
  - `CONSIDERAR_DATA_ATUAL_PREV_FAT`
- Permissoes inspect:
  - `MXSACESSODADOS`
  - `MXSACESSOENTIDADES`

### Validacao (SQL/tabelas/parametros)

```sql
SELECT SID, SERIAL#, USERNAME, PROGRAM, MODULE
FROM V$SESSION
WHERE PROGRAM LIKE 'CJQ%' OR PROGRAM LIKE 'J0%';
```

---

## 11. Rastreabilidade de Fontes

- section_id: SEC-11
- dominio: rastreabilidade
- intencao_de_busca:
  - "De qual arquivo veio cada bloco do documento unificado?"
  - "Quais conteudos foram sanitizados?"
  - "Quais testes de recuperacao RAG devem ser executados?"
- entidades:
  - matriz de fontes
  - casos de teste RAG
  - politica de sanitizacao
- fontes:
  - todos os arquivos de `documentos/organizacao`

### Contexto

Garante rastreabilidade de origem, controle de sanitizacao e criterio de aceite para uso no RAG.

### Procedimento

1. Usar matriz secao -> fontes para auditoria de conteudo.
2. Revisar politica de sanitizacao antes de nova ingestao.
3. Executar casos de teste de recuperacao para validar cobertura semantica.

### 11.1 Matriz secao -> fontes

| Secao unificada | Fontes principais |
|---|---|
| 0. Escopo e seguranca | SERVICE-DESK-PROCESSOS, ingest.py, config.py |
| 1. Ecossistema e fluxos E2E | SERVICE-DESK-PROCESSOS, SERVICE_DESK_MAXIMA_ORGANIZADO, maxPag |
| 2. Parametros e configuracao | 01-PARAMETROS-E-CONFIGURACAO, 02, 03, 04, CONTROLE_FERIAS, GLOSSARIO |
| 3. Pedidos, status e timeline | SERVICE-DESK-PROCESSOS, 02-PEDIDOS-E-VENDAS, 05-SQL |
| 4. Campanhas e lucratividade | 03-CAMPANHAS-E-DESCONTOS, ARTIGOS_BASE, SERVICE-DESK-PROCESSOS |
| 5. Rotas, visitas e consultas | 04-ROTAS-VISITAS-E-CONSULTAS, SERVICE-DESK-PROCESSOS, CONTROLE_FERIAS |
| 6. MaxPag | maxPag, SERVICE-DESK-PROCESSOS, ARTIGOS_BASE |
| 7. SQL, banco e infra | 05-SQL-BANCO-E-INTEGRACAO, SERVICE-DESK-PROCESSOS, SERVICE_DESK_MAXIMA_ORGANIZADO |
| 8. Tabelas por dominio | CARGATOTAL, SERVICE-DESK-PROCESSOS, SERVICE_DESK_MAXIMA_ORGANIZADO |
| 9. Troubleshooting | SERVICE-DESK-PROCESSOS, 02, 03, 04, 05, maxPag |
| 10. Glossario tecnico | GLOSSARIO, 01-PARAMETROS-E-CONFIGURACAO |
| 11. Rastreabilidade | consolidacao de todas as fontes |

### 11.2 Politica de sanitizacao aplicada

Conteudos removidos/mascarados:

- Senhas em texto claro.
- Hashes/sigilos operacionais de autenticacao.
- Tokens reais.
- Credenciais de banco/servicos.

Padrao de substituicao:

- `[SENHA_REMOVIDA]`
- `[TOKEN_REMOVIDO]`
- `[CREDENCIAL_REMOVIDA]`

### 11.3 Divergencias consolidadas

- Lista de status da `MXSINTEGRACAOPEDIDO`: adotada versao completa com status 0-23.
- Fluxo de maxPag: priorizado fluxo assincrono consolidado com validacao por jobs e mensageria.
- Parametrizacao de bloqueio de cliente: consolidada matriz com combinacoes de permitir/bloquear e alinhamento ERP.

### 11.4 Casos de teste de recuperacao RAG

1. Pergunta: "Qual parametro bloqueia item sem estoque?"  
   Resultado esperado: `BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE` com contexto e categoria.
2. Pergunta: "Pedido preso status 0/5, o que validar?"  
   Resultado esperado: fluxo, causas e SQL de pendencia.
3. Pergunta: "Status 18 no maxPag significa o que?"  
   Resultado esperado: "Aguardando utilizacao do link maxPayment".
4. Pergunta: "Como habilitar ferias vendedor?"  
   Resultado esperado: permissao de rotina + `HABILITA_FERIAS_VENDEDOR`.
5. Pergunta: "SQL para locks Oracle"  
   Resultado esperado: queries de `V$SESSION`, `DBA_WAITERS`, `V$LOCK`.
6. Pergunta: "Como configurar filial retira?"  
   Resultado esperado: parametros, permissao e comportamento de desmembramento.
7. Pergunta: "Diferenca entre MQT, SQP, MIQ e FPU"  
   Resultado esperado: tabela comparativa de campanhas.
8. Pergunta: "Como diagnosticar cliente bloqueado no pedido?"  
   Resultado esperado: matriz de parametros de bloqueio + validacao ERP.

### Validacao (SQL/tabelas/parametros)

```sql
SELECT FILENAME, CHUNK_COUNT FROM DOCUMENTS WHERE FILENAME = 'MAXIMA_RAG_UNIFICADO.md';
```

---
```
