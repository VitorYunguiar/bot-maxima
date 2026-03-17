# Service Desk Maxima Tech — Processos e Procedimentos

> Documento para ingestao em banco vetorial (RAG).
> Ultima atualizacao: 2026-02-11
> Fonte original: SERVICE DESK MAXIMA TECH PROCESSOS.pdf (214 paginas)

---

## Sobre este documento

Este documento cobre os processos operacionais do Service Desk da Maxima Tech, incluindo procedimentos de suporte N1/N2/N3 para maxPedido, maxGestao, maxCatalogo, maxPromotor e maxPag. Contem troubleshooting, parametrizacoes, consultas SQL, fluxos de integracao e procedimentos de manutencao de ambiente.

**Palavras-chave**: service desk, suporte, maxPedido, maxGestao, maxCatalogo, maxPromotor, maxPag, Winthor, ERP, integracao, troubleshooting, parametros, banco nuvem, extrator, portainer, hangfire
**Sistema**: maxPedido | Winthor | maxGestao | maxCatalogo | maxPromotor | maxPag
**Area**: Service Desk | Parametros | Pedidos | Integracao | Campanhas | Rotas

---

## 1. Visao Geral do Ecossistema Maxima

### 1.1 Produtos

- **maxPedido**: App mobile para vendas. Espelha a rotina 316 do Winthor (Pedido de Vendas) e funciona baseado nas funcionalidades dessa rotina.
- **maxGestao**: Portal Web e APP onde gestores e administradores do maxPedido podem acompanhar, tracar rotas e imprimir relatorios de performance referente aos RCAs.
- **maxPromotor**: Portal Web e APP para pesquisas, dashboards e relatorios. Exibe views/graficos/relatorios para usuarios com acesso.
- **maxCatalogo**: APP para exibir os produtos do cliente.
- **maxPag**: Sistema de pagamentos integrado ao maxPedido (PIX, cartao).

### 1.2 Conceito de ERP

Winthor e um ERP (Enterprise Resource Planning). ERPs sao softwares que empresas usam para gerenciar vendas. A integracao com ERPs permite que um vendedor faca uma venda diretamente de seu aparelho celular.

### 1.3 Tabelas de Gravacao do FV (Forca de Vendas)

O maxPedido grava nas tabelas FV e a integradora valida e envia para as tabelas do ERP:
- **PCCLIENTFV**: Clientes do Forca de Vendas
- **PCPEDCFV**: Cabecalho de pedidos do FV
- **PCPEDIFV**: Itens de pedidos do FV

---

## 2. Tabelas Uteis do Banco

### 2.1 Pedidos feitos na APK

| Tabela | Descricao |
|--------|-----------|
| MXSINTEGRACAOPEDIDO | Consulta todos os pedidos que ficam na timeline de pedidos da APK |
| MXSINTEGRACAOPEDIDO_LOGST | Log dos pedidos da APK. Util para verificar status do pedido e tempo de envio, integracao e retorno |
| MXSINTEGRACAOPEDIDOLOG | Log do JSON dos pedidos. Vem do JSON da APK |
| MXSHISTORICOCRITICA | Historicos da critica dos pedidos. Possibilita ver todas as criticas, nao so a ultima |

### 2.2 Configuracoes

| Tabela | Descricao |
|--------|-----------|
| MXSCONFIGERP | Configuracoes do ERP, geralmente presentes na PARAMFILIAL |
| MXSPARAMETRO | Parametros da Central de Configuracoes do maxPedido |
| MXSPARAMETROVALOR | Parametros da Central atribuidos a usuarios individuais |

### 2.3 Sincronizacao e Usuarios

| Tabela | Descricao |
|--------|-----------|
| MXSAPARELHOSCONNLOG | Ultima sincronizacao realizada pelo RCA |
| MXSCONEXOES | Informacoes de conexoes |
| MXSCLIENT.CODUSUR1/2/3 | Verifica vinculo RCA/Cliente |
| ERP_MXSUSURCLI | Vinculo RCA/Cliente no ERP |
| MXSUSUARIOS | Cadastro de usuarios Maxima |
| SYNC_D_MXSCLIENT | Amarra o usuario da Maxima com codigo do cliente |

### 2.4 Roteiro de Visitas

| Tabela | Descricao |
|--------|-----------|
| MXSCOMPROMISSOS | Roteiro de visitas dos RCAs (Rotina 354 / maxGestao Plus) |
| MXSHISTORICOCOMPROMISSOS | Backup do roteiro |
| ERP_MXSROTACLI | Roteiro no ERP |

### 2.5 Titulos e Financeiro

| Tabela | Descricao |
|--------|-----------|
| ERP_MXSPREST | Titulos abertos. Verificar campos VPAG e DTPAG |
| MXSTITULOSABERTOS | Titulos abertos na nuvem |

### 2.6 Outras Tabelas Importantes

| Tabela | Descricao |
|--------|-----------|
| MXSCPARAMETRO | Parametros do maxCatalogo |
| MXSAPARELHOSDEBLOQLOG | Logs de desbloqueio de usuarios |
| MXSPARAMETROINDUSTRIA | Parametros para Pepsico |
| MXLOGTRANSFERENCIACC | Logs de transferencia de Conta Corrente (maxGestao) |
| ERP_MXSLOGRCA | Logs de transferencia de CC (ERP) |
| MXSGRRELATORIO | Relatorios da Central de Configuracoes |
| MXSLOCATION | Registros de checkin/checkout na base local do RCA (somente SQLite) |
| MXMI_AGENDA_RCA | View para ver roteiros cadastrados pelo roteirizador |
| MXSMAXPAYMENTMOV | Movimentacoes do maxPag |
| MXSDESCESCALONADOC / MXSDESCESCALONADOI / MXSDESCESCALONADORESTRI | Desconto escalonado |
| MXSTABELA | Informacoes de tabelas que podem ser sincronizadas para o aparelho |
| LOGJSON | Tabela do SQLite que mostra se o usuario excluiu ou nao o pedido da base |

### 2.7 JSON do pedido APK para ERP

Quando a APK envia o pedido para a nuvem, o JSON que sai da aplicacao e gravado na tabela MXSINTEGRACAOPEDIDOLOG. O JSON na tabela MXSINTEGRACAOPEDIDO e processado pelo backend e recebe mais informacoes quando o ERP retorna a critica. A tabela de log dos JSONs processados pelo ERP e a MXSINTEGRACAOPEDIDO_LOG.

---

## 3. Status dos Pedidos

### 3.1 Status na Timeline da APK

| Status | Descricao |
|--------|-----------|
| 0 | Pedido salvo no aparelho |
| 1 | Pedido gravado no banco nuvem com ID_pedido |
| 2 | Pedido bloqueado na nuvem |
| 3 | Aguardando autorizacao preco/lucratividade/bonificacao (status 8 ou 9 na MXSINTEGRACAOPEDIDO) |
| 4 | Pedido cancelado pelo usuario (status 7 na MXSINTEGRACAOPEDIDO) |
| 5 | Pedido gravado no ERP com NUMPED_ERP (status 2,3,11 ou 4 na MXSINTEGRACAOPEDIDO) |
| 6 | Pedido rejeitado pelo ERP (tipo 1 e 2 com critica preenchida, status 4 sem NUMPEDERP) |
| P/7 | Posicao Pendente na MXSHISTORICOPEDC |
| L/8 | Posicao Liberado na MXSHISTORICOPEDC |
| B/9 | Posicao Bloqueado na MXSHISTORICOPEDC |
| M/10 | Posicao Montado na MXSHISTORICOPEDC |
| F/11 | Posicao Faturado na MXSHISTORICOPEDC |
| C/12 | Posicao Cancelado na MXSHISTORICOPEDC ou MXSINTEGRACAO = 12 |
| O/13 | Orcamento gravado no ERP (tipo pedido 2, status 2,3,11 ou 4 com NUMPEDERP) |
| 14 | Autorizacao rejeitada pelo Gestao (status 10 na MXSINTEGRACAOPEDIDO) |

### 3.2 Status na MXSINTEGRACAOCLIENTE

| Status | Descricao |
|--------|-----------|
| 0 | GRAVADO_APARELHO |
| 1 | NUVEM_GRAVADO |
| 2 | NUVEM_BLOQUEADO |
| 3 | NUVEM_AGUARDANDO_AUTORIZACAO |
| 4 | NUVEM_CANCELADO |
| 5 | ERP_ENVIADO |
| 6 | ERP_REJEITADO |
| 7 | ERP_PENDENTE |
| 8 | ERP_LIBERADO |
| 9 | ERP_BLOQUEADO |
| 10 | ERP_MONTADO |
| 11 | ERP_FATURADO |
| 12 | ERP_CANCELADO |
| 13 | ERP_ORCAMENTO_ENVIADO |
| 14 | NUVEM_AUTORIZACAO_REJEITADA |

### 3.3 Status na MXSINTEGRACAOPEDIDO

| Status | Descricao |
|--------|-----------|
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

### 3.4 Status maxPag na MXSINTEGRACAOPEDIDO

| Status | Descricao |
|--------|-----------|
| 16 | Aguardando geracao do link maxPayment |
| 17 | Erro ao gerar link maxPayment |
| 18 | Aguardando utilizacao do link maxPayment |
| 19 | Falta de colunas para utilizacao do maxPayment |
| 20 | Erro ao processar solicitacao no maxPayment |
| 21 | Em processamento no maxPayment |
| 22 | Solicitacao cancelada no maxPayment |
| 23 | Validade do link incorreta para utilizacao do maxPayment |

---

## 4. SQL Uteis

### 4.1 Verificar relacionamentos de tabelas

```sql
SELECT * FROM ALL_TAB_COLUMNS WHERE COLUMN_NAME = 'NOME_DA_COLUNA';
```

### 4.2 Limite do cliente

```sql
-- Consulta completa de limite de credito do cliente
-- Substituir 10343 pelo CODCLI desejado
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
    LEFT JOIN (
        SELECT PCCLIENT_INNER.CODCLI,
            SUM(NVL(PCCLIENT_INNER.LIMCRED, 0)) VLLIMITE,
            SUM(NVL(PCCLIENT_INNER.LIMITECREDSUPPLI, 0)) LIMITECREDSUPPLI
        FROM PCCLIENT PCCLIENT_INNER
        WHERE PCCLIENT_INNER.CODCLI = 10343
        GROUP BY PCCLIENT_INNER.CODCLI
    ) TBLIMITE ON TBLIMITE.CODCLI = PCCLIENT.CODCLI
    -- ... (query completa no documento original)
    WHERE (PCCLIENT.LIMCRED >= 0 OR NVL(PCCLIENT.LIMITECREDSUPPLI, 0) > 0)
      AND PCCLIENT.CODCLI = 10343
)
SELECT * FROM CLIENTE;
```

---

## 5. Chamados Sankhya

### 5.1 Procedimento

1. Criar chamado na DEV STUDIO para integrador Sankhya
2. Colocar seu nome, numero corporativo e e-mail para contato
3. Deixar o chamado original em N1 com tipo: Integracao (nao conta SLA)
4. Vincular o chamado da DEV Studio ao chamado original
5. No chamado Sankhya: colocar email e telefone corporativo Maxima
6. Prioridade: Lowest

---

## 6. MaxPedido — Acesso e Instalacao

### 6.1 Requisitos Minimos

Pagina de requisitos minimos (compartilhavel com o cliente): https://maximatech.com.br/requisitos

### 6.2 Como Baixar o MaxPedido

O maxSolucoes funciona como uma loja de aplicativos da Maxima. Devido restricao do Google, existe nova forma de download: http://maxsolucoes-web.solucoesmaxima.com.br/

### 6.3 Troubleshooting de Instalacao

**Problema**: Erro "APP nao foi instalado" (maxSolucoes)
- Principal causa: Falta de ARMAZENAMENTO no dispositivo
- Segunda causa: Falta de permissoes do navegador
- Verificar Google Play Protect (pode bloquear instalacoes)
- Outras acoes: Reiniciar aparelho, verificar antivirus

**Problema**: Erro "O item nao foi encontrado"
- Causa provavel: Versao do Android Go Edition (nao esta nos requisitos minimos)

**Problema**: Falha ao acessar o aplicativo
- Verificar liberacao de versao
- Resetar senha
- Verificar Internet, Cache, Memoria, condicoes do aparelho

### 6.4 Erro "Buscar dados usuario"

- Verificar se cadastro do RCA na central esta vinculado a perfil no ERP
- Deslogar do maxSolucoes e logar novamente

---

## 7. Sincronizacao

### 7.1 Sincronizacao Manual (Truque)

Para forcar sincronizacao sem afetar dados do cliente: alterar qualquer registro na tabela de usuarios, dar commit, voltar ao original, dar commit, pedir para sincronizar. Isso atualiza o ATUALIZAID e libera nova sincronizacao.

### 7.2 Sincronizacao Automatica

Para ativar, e necessario atualizar o ambiente nuvem e abrir chamado para N3 (DEV backend).

Parametro: **HABILITA_SINC_AUTOMATICA**

Funcionalidades de sync automatica disponiveis:
- Estoque (Sprint 29/01)
- Limite de cliente (Sprint 16/04)
- Desbloqueio de cliente (Sprint 16/04)
- Timeline de pedidos (Sprint 02/05)
- Preco (Sprint 05/09)

Quando habilitado e houver alteracao na rotina 1203 (Extrato de clientes) referente a limite e bloqueio, o app sincroniza automaticamente. Nao sincroniza se o vendedor estiver realizando um pedido, porem ao sair dele os dados serao sincronizados.

### 7.3 Carga de ATUALIZID para Sincronizacao

Quando e preciso renovar diferenca de dados entre banco nuvem e aparelho do RCA. Recomendado para menos de 400 mil registros.

```sql
-- Verificar ATUALIZID atual
SELECT C.ATUALIZID, C.* FROM MXSCLIENT C;

-- Atualizar ATUALIZID (forcar sincronizacao)
DECLARE
BEGIN
    UPDATE MXSCLIENT
    SET ATUALIZID = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS')),
        DTATUALIZ = sysdate
    WHERE CODOPERACAO != 2;
    COMMIT;
END;

-- Com filtro de data
DECLARE
BEGIN
    UPDATE MXSHISTORICOPEDC
    SET ATUALIZID = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS')),
        DTATUALIZ = sysdate
    WHERE CODOPERACAO != 2
    AND TRUNC(DATA) BETWEEN TO_DATE('09/07/2025') AND TO_DATE('09/07/2025');
    COMMIT;
END;
```

---

## 8. Cadastro de Usuario / RCA

### 8.1 Como Cadastrar Usuario no maxPedido

- O cliente nao possui permissao para criar usuario administrador
- Para criar usuarios administrador, o suporte deve criar no Gestao Nuvem

### 8.2 Liberar Versao do App

Acessar portal Gestao Nuvem > menu lateral CADASTRO > item 303 (Versoes) > Botao "Novo" > Selecionar CLIENTE e AMBIENTE (Producao ou Homologacao).

Dados para preenchimento:
- **Rotina maxPedido**: 21
- **Link de acesso**: https://maxpedido-base-novasync.solucoesmaxima.com.br/v1
- **Link de acesso 2**: https://maxpedido-api-unificado-04.solucoesmaxima.com.br/v1
- **Link de download**: https://versoes.maximatech.com.br (requer VPN)

Package Names:
- maxPedido: br.com.maximasistemas.maxpedido
- maxGestao: br.com.maximasistemas.maxgestao
- maxCatalogo: br.com.maximasistemas.maxcatalogo

E recomendado atualizar versoes dos ambientes local e nuvem ao liberar nova versao da APK.

### 8.3 Inativar Usuario

1. Definir/Verificar valores INATIVO e INUTILIZADO no cadastro no Gestao Nuvem
2. Se apenas INATIVO, ainda consome licenca. E necessario estar INUTILIZAVEL tambem para remover licencas automaticamente
3. Serve tanto para maxPedido quanto maxGestao

```sql
-- Script para inativar usuario na central quando ja inativo no Gestao
-- Rodar linha por linha
SELECT * FROM MXSUSUARIOS WHERE CODUSUR = _____
SELECT * FROM MXSUSUARIOS WHERE NOME = _____
UPDATE MXSUSUARIOS SET STATUS = 'I' WHERE CODUSUR = _____
UPDATE MXSUSUARIOS SET CODOPERACAO = 2 WHERE CODUSUR = _____
UPDATE MXSUSUARIOS SET CODUSUR = 0 WHERE CODUSUR = _____
-- Rodar a linha 2 novamente e confirmar os registros alterados
COMMIT
```

### 8.4 Usuario Inutilizado

Verificar no ambiente nuvem:
- INUTILIZAVEL = N
- STATUS = Ativo
- Verificar se tem versao liberada

---

## 9. Timeline de Pedidos

### 9.1 Historico de Pedidos na Timeline

Os pedidos que ficam no historico em CONSULTAS aparecem na TIMELINE de pedidos.

Parametro: **PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO**

### 9.2 Pedidos com mesmo valor na Timeline

- Acontece quando tem algum NUMPED = 0 no SQLite
- Nao tem como recuperar a base, necessario limpar a base do RCA

### 9.3 Status de Entrega (maxMotorista)

Para habilitar status de entrega na timeline:
- Necessario ter o produto maxMotorista
- Ativar parametro: **HABILITAR_DADOS_ENTREGA** = 'S'

### 9.4 Timeline nao atualiza status

A informacao de posicao e obtida na seguinte hierarquia:
1. MXSHISTORICOPEDC (campo posicao) — sempre prioridade
2. MXSINTEGRACAOPEDIDO (critica do pedido, vem da MXSHISTORICOCRITICA)

A HISTORICOPEDC so e validada quando todos os campos obrigatorios sao enviados. Se faltar o campo DTABERTURAPEDPALM, o pedido pode nao atualizar na timeline.

---

## 10. Fluxo de Processamento de Pedido

### 10.1 Fluxo Completo

1. APK envia pedido para nuvem (Responsabilidade Maxima)
2. Server grava na MXSINTEGRACAOPEDIDO com status = 0 (Responsabilidade Maxima)
3. ERP faz GET (endpoint statuspedidos) buscando pedidos com status desejados (Responsabilidade ERP)
4. API retorna GET, automaticamente seta status 2 (ENVIADO PARA O ERP) (Responsabilidade Maxima)
5. ERP processa pedido internamente
6. ERP faz PUT (endpoint statuspedidos) com critica e status 4 (sucesso) ou 5 (erro) (Responsabilidade ERP)
7. ERP envia historico com posicao (L-liberado, F-faturado etc.) (Responsabilidade ERP)
8. APK faz swipe para atualizacao da timeline (Responsabilidade Maxima)
9. Server envia dados para timeline com base no historico + status da MXSINTEGRACAOPEDIDO (Responsabilidade Maxima)

### 10.2 Fluxo de Integracao OERPs

1. Status 0: Pedido chega no banco nuvem, disponibilizado na API para GET
2. Status 2: Integradora deu GET na API, aguardando retorno
3. Status 4: Integradora enviou JSON de retorno informando sucesso

### 10.3 Pedidos Presos na Timeline (nao chega na MXSINTEGRACAOPEDIDO)

Verificar parametro **BLOQUEIA_PEDIDO_CLIENTE_SEMLIMITE**. Se habilitado e o RCA fizer pedido com cliente sem limite de credito, o maxPedido vai deixar o pedido preso na APK. Quando regularizado no ERP, sincronizar e duplicar o pedido.

### 10.4 Pedido nao integrando — Reinicio de Extrator

Verificar status do pedido na MXSINTEGRACAOPEDIDO. Se for status 0, 5 ou 11, pode ser necessario reiniciar o extrator.

---

## 11. Central de Configuracoes

### 11.1 Tipos de Dados de Parametros

| TIPODADO | Descricao |
|----------|-----------|
| 1 | Literal (texto) |
| 2 | Inteiro (numero) |
| 3 | Logico (S/N) |

### 11.2 Cadastro de Preposto

Preposto e um tipo de usuario sem cadastro no ERP, vinculado a um RCA. Pedidos do preposto sao atribuidos ao RCA.

Passo a passo:
1. Criar novo usuario no APPSV (Gestao Nuvem) e vincular ao do ERP
2. Acessar Central de Configuracoes > Cadastro de usuarios
3. Editar usuario e marcar flag "e preposto ou proponente?"
4. Definir REPRESENTANTE DO ERP que este usuario e preposto-de
5. Dar as mesmas permissoes de usuario que o representante "pai"

Erro "Geracao de dados preposto": Ocorre porque cadastro do preposto nao tem representante do ERP vinculado.

### 11.3 Fotos na Central de Configuracoes

Para adicionar fotos de produtos: Central de Configuracoes > Extras > Upload de fotos. O nome da imagem deve ser igual ao codigo do produto. E possivel fazer upload de pasta com varias fotos ao mesmo tempo.

---

## 12. Espelho do Pedido — Personalizacao

### 12.1 Parametros de Personalizacao

| Parametro | Descricao | Tipo |
|-----------|-----------|------|
| EXIBIR_PRECO_UNIT_EMB | Exibir preco unitario no PDF compartilhado | S/N |
| APRESENTAR_DESCONTOS_PEDIDO_EMAIL | Exibir campos de desconto no PDF (VL DESC, % DESC) | S/N |
| OCULTAR_IMPOSTOS_PEDIDO_EMAIL | Ocultar impostos no PDF compartilhado | S/N |
| OCULTAR_VALIDADE_PROPOSTA | Ocultar datas de impressao e validade | S/N |
| EXIBIR_FOTO_DO_PRODUTO_PDF | Exibir fotos ao lado dos produtos no PDF | S/N |
| EXIBIR_FOTO_DO_PRODUTO_PERSONALIZADO_PDF | Exibir fotos personalizadas no PDF | S/N |
| EXIBIR_CAMPO_CA_COMPART_PED_ORC | Certificado de autorizacao nos relatorios PDF e Excel | S/N |
| LINK_LOGO_MARCA | Link da logo exibida no relatorio | URL |
| DESABILITAR_ESPELHO_PED_PADRAO | Desabilita espelho padrao (quando cliente tem personalizado) | S/N |

---

## 13. Conta Corrente (CC) do RCA

### 13.1 Conceito

Saldo conta corrente funciona como carteira virtual do cliente dentro do maxPedido. O RCA pode dar desconto acima do normal, e a diferenca e descontada do saldo CC do RCA dado pelo gestor.

Para ocultar saldo CC da tela inicial (V4): parametro **OCULTAR_COMISSAO_MENU**

### 13.2 Parametros de Conta Corrente

| Parametro | Tipo | Descricao | Ambiente |
|-----------|------|-----------|----------|
| CON_TROCAALTDEBCREDRCA | S/N | Vendas bonificadas alteram saldo debito/credito do RCA | Winthor/ERP |
| CON_ACEITADESCPRECOFIXO | S/N | Cliente utiliza preco fixo ou percentual maximo de desconto no preco fixo | Winthor/ERP |
| CON_USACREDRCA | S/N | Usa saldo conta corrente (MXSPARAMFILIAL) | Winthor/ERP |
| MXSUSUARI.USADEBCREDRCA | S/N | Coluna da tabela de cadastro de usuario, deve estar como 'S' | Banco Nuvem |
| USAR_CCRCA_MAXIMA | S/N | Usa CC Maxima | Central Config |
| EXIBIR_SALDOCC_DISPONIVEL | S/N | Exibe saldo CC disponivel | Central Config |
| APRESENTAR_CARD_CC | S/N | Exibir card de conta corrente | Central Config |
| GERAR_DADOS_CC_RCA | S/N | Sincroniza movimentacoes CC (ultimos 7 dias) | Central Config |
| EXIBIR_TODA_MOVIMENTACAO_CC | S/N | Exibe todo saldo previsto na aba de totais | Central Config |
| DEFINE_CC_MENU | 0/1/2 | 0: saldo, 1: saldo-credito, 2: credito | Central Config |
| DESCONTA_SALDOCCRCA_OFFLINE | S/N | Uso de saldo CC offline | Central Config |
| IMPEDDIR_ABATIMENTO_SEMSALDORCA | S/N | Impedir abatimento sem saldo | Central Config |
| ABATIMENTODEBITARCCRCA | S/N | Debitar abatimentos de CC mesmo com saldo negativo | Central Config |

### 13.3 Se o saldo exibir "--"

Quando parametros nao forem validados corretamente, informacoes de CC sao removidas da tela e campos mostram "2 tracos". Se somente EXIBIR_SALDOCC_DISPONIVEL = 'N' e demais 'S', campos tambem mostram "2 tracos". Solucao: ativar tudo como 'S'.

### 13.4 Como gerar saldo de CC

Para gerar saldo, o RCA deve aplicar um desconto negativo no aplicativo (acrescimo). Para limitar, colocar percentual maximo de acrescimo na rotina 132 ou 201.

### 13.5 Tipos de Movimentacao CC (MXSCONFIGERP.TIPOMOVCCRCA)

| Codigo | Descricao |
|--------|-----------|
| FF | Debito/Credito no faturamento |
| VA | Debito na venda, credito no acerto |
| VF | Debito na venda, credito no faturamento |
| VV | Debito/Credito na venda |

---

## 14. Descontos e Politicas

### 14.1 Campanha de Desconto

Tabelas:
- **MXSDESCONTOC**: Cabecalho da campanha
- **MXSDESCONTOI**: Itens da campanha

```sql
-- Buscar campanha por codigo
SELECT * FROM MXSDESCONTOC WHERE CODIGO = ??;
-- Buscar itens da campanha
SELECT * FROM MXSDESCONTOI WHERE CODIGO = ??;
```

Campanha sem produtos pode ser causada por:
- RCA nao tem acesso ao produto
- Campanha enviada incorreta
- Divergencias de base RCA e banco

### 14.2 Checando Desconto Maximo de Produto

```sql
SELECT PERDESCMAX, MXSTABPR.* FROM MXSTABPR WHERE CODPROD = ??;
```

Para "desconto livre", o campo PERDESCMAX deve ser NULL/VAZIO.

### 14.3 Desconto Progressivo

**Parametros**:
- USAR_CAMPANHA_DESCONTO_PROGRESSIVO = 'S'
- TIPO_DESC_PROGRESSIVO: 'PRG' (Campanha Progressiva) ou 'PEG' (Desconto Progressivo)

**Tabelas relacionadas**:
| Tabela | Descricao |
|--------|-----------|
| MXSCAMPANHAFAIXAS | Faixas de desconto da campanha |
| MXSCAMPANHAFAMILIA | Cabecalho da campanha |
| MXSCAMPANHAFAMILIAGRUPOS | Grupos da campanha |
| MXSCAMPANHAPROPORCAO | Proporcoes |
| MXSFAMILIAITENS | Itens da familia |
| MXSFILTROCAMPANHA | Restricoes de cliente: TIPORESTRICAO=1 (restrito), TIPORESTRICAO=2 (exclusivo) |

### 14.4 Tipos de Campanha Progressiva

- **MIQ**: Mix por quantidade minima individual. Todos os produtos do grupo precisam ter quantidade minima para ativar desconto.
- **MQT**: Mix por quantidade total. Basta atingir quantidade total entre todos os produtos do grupo.
- **SQP**: Sem quantidade por produto. Agrupamento por fornecedor, produto etc. Nao obriga inserir todos os produtos.
- **FPU**: Full product usage. Todos os produtos precisam ser incluidos (similar ao MIQ mas com agrupamento flexivel).

### 14.5 Prioridade de Desconto

| Nivel | Tabela | Observacao |
|-------|--------|------------|
| 1 | MXSPRECOPROM | Preco Fixo |
| 2 | MXSDESCONTO / MXSDESCONTOC | Campanha de Desconto |
| 3 | MXSTABPR | Se PERDESCMAX > desconto da campanha, prioriza TABPR |
| 4 | MXSUSUARI | PERMAXVENDA |
| 5 | MXSCONFIGERP | PERMAXVENDA |

### 14.6 Desconto Maior que Permitido

Ao aplicar desconto maior que cadastrado, aparece popup pedindo autorizacao de preco. Supervisor pode aprovar via maxGestao ou ERP.

**Parametrizacao Winthor**: CON_ACEITADESCTMK / ACEITADESCTMKFV
**Parametrizacao Maxima**: Permissao "Permitir solicitacao de autorizacao de preco no aplicativo" no cadastro do vendedor/perfil

---

## 15. Promocao de Preco Fixo

### 15.1 Campos Obrigatorios na MXSPRECOPROM

CODPRECOPROM, ACEITAACRESCIMOPRECOFIXO, ACEITADESCPRECOFIXO, AGREGARST, CODFILIAL, CODPROD, CONSIDERAPRECOAEMIMPOSTO, DTFIMVIGENCIA, DTINICIO VIGENCIA, NUMREGIAO

### 15.2 Familia de Produtos no Preco Fixo

- Criar familia de produtos na rotina 203 (PCPRODUT)
- Na MXSPRODUT, CODPRODPRINC = codigo da familia
- Inserir CODPRODPRINC no campo CODPROD da MXSPRECOPROM
- Coluna UTILIZAPRECOFIXOFAMILIA deve ser 'S'

---

## 16. Resumo de Vendas

### 16.1 Resumo nao atualiza

Possiveis causas:
1. Bloqueio da porta de acesso ao Hangfire (normalmente 9002)
2. Ambiente muito desatualizado
3. Bloqueio de GEOLOCATION aos EUA (IPs da AWS vem da Virginia)

IPs da Maxima para liberacao no Firewall: 3.81.180.245, 34.236.34.79, 3.81.180.2, 18.215.65.25

### 16.2 Metas por Fornecedores

Parametro: **META_FOR** = 'S'

Para mostrar valor F+L+M no campo "Alcancado": **CRITERIOVENDA** = 'P'

### 16.3 Parametros de Aba de Meta

Cada aba do resumo de vendas (META_CAT, META_DEP, META_FOR, META_FRP, META_CLI, META_PROD, META_SEC) possui sub-parametros:
- _CLIPOS: Positivacao de clientes
- _MIX: Mix
- _QTPESO: Peso
- _QTVENDA: Quantidade vendida
- _VLVENDA: Valor de venda

Exemplo: META_DEP_MIX = 'N' oculta linha de MIX da aba de Departamentos.

### 16.4 Grafico de Metas — Pre-requisitos

- Metas cadastradas (rotina 353 ou 309)
- Tabelas: MXSMETAS, ERP_MXSMETARCA
- Dias uteis cadastrados:
  - OERPs: ERP_MXSDATAS (via script) e MXDIASUTEIS (via central)
  - Winthor: ERP_MXSDATAS e MXSDIASUTEIS (rotina 589)
- Cadastro da filial 99
- Rodar Atualizador

### 16.5 Tendencia de Vendas (V4)

Aparece somente quando filtro de data for do mes atual.

Formula: (faturado / qtd_dias_uteis_passaram) * (qtd_dias_uteis - qtd_dias_uteis_passaram + faturado)

Parametro para desabilitar: **RV_TENDENCIA_VENDA** = 'N'

### 16.6 Valor de Venda nao aparece na tela inicial (V4)

Na V4 e necessario ter dias uteis para apresentar valor de venda.

Tabela: ERP_MXSDATAS

- OERPs: Cadastrar dias uteis na Central de Configuracoes
- Winthor: Cadastrar dias uteis no Winthor

---

## 17. I.A. de Recomendacao de Produtos

### 17.1 Parametrizacao

Parametro: **HABILITA_RECOMENDACAO_PRODUTOS**

- Leva 48 horas para gerar dados analisando todas as vendas
- Minimo 2 produtos no pedido para ver recomendacao
- Versao minima: 3.219.4
- Nao funciona com TIPO "Por filial"

Fluxo:
1. Habilitar parametro
2. Aguardar 48 horas
3. Certificar versao acima de 3.219.4
4. Inserir itens no pedido
5. Clicar em "salvar e enviar pedido"
6. Tela de recomendacao da IA aparece

Tabela: **MXSRECOMENDACAO** (registra recomendacoes de produtos vendidos em conjunto)

---

## 18. Check-In e Check-Out

### 18.1 Parametros Principais

| Parametro | Descricao |
|-----------|-----------|
| UTILIZA_CHECKIN_CHECKOUT | Ativa checkin/checkout. Trabalha com GPS_IS_REQUIRED_CONFEC_PEDIDO = 'S' |
| PERMITIR_PEDIDO_SEM_CHECKIN | Se 'N', nao permite pedido sem checkin |
| OBRIGAR_ATENDIMENTO_PARA_CHECKOUT | Obriga pedido ou justificativa ao fazer checkout |
| OBRIGA_MOSTRAR_MOTIVO_NAO_VENDA | Se existirem pedidos bloqueados, apresenta mensagem na sincronizacao |
| OBRIGA_CHECKIN_CLIENTE_FORA_ROTA | Se habilitado, nao solicita checkin para clientes fora de rota |

### 18.2 Parametros de GPS Relacionados

| Parametro | Descricao |
|-----------|-----------|
| GPS_TRACKING_ENABLED | Ativa rastreio via GPS |
| GPS_IS_REQUIRED_CONFEC_PEDIDO | RCA nao consegue iniciar/salvar pedido sem GPS |
| ATIVAR_GPS_PEDIDO | Ativa validacao de localizacao, exibindo alerta |

### 18.3 Justificar Visita sem Checkin/Checkout

Parametros necessarios:
- BLOQ_RCA_COM_ROTA_PENDENTE = 'S'
- ROTEIRO_PENDENTE_ONTEM = 'S'
- DIAS_VERIFICACAO_ROTEIRO_PENDENTE = 1
- JUSTIFICAR_ROTEIRO_ANTERIOR = 'S'
- BLK_SYNC_ROTEIRO_PENDENTE = 'S'
- Permissao: "Permitir justificativas de clientes fora da rota"

### 18.4 Cerca Eletronica

| Parametro | Descricao |
|-----------|-----------|
| GPS_TRACKING_ENABLED | Habilita acompanhamento GPS e geracao da base maxTracking |
| GPS_EDGE_METERS_SIZE | Area de permissao (metros) para gerar pedido ao redor do cliente |
| GPS_EDGE_BLOCK | Valida a cerca eletronica |

### 18.5 Historico de Check-In/Check-Out no Winthor

Informacoes aparecem na rotina 344. Parametro **UTILIZA_HORA_APARELHO_JUSTIFICATIVA_VISITA**: se desabilitado, grava horario dos compromissos justificados ao inves do horario do aparelho.

**Tabelas de Justificativa de Visita**:
- SQLite: MXSVISITAS (status 1 para justificativa)
- Banco Nuvem: ERP_MXSVISITAFV
- Banco Winthor: PCVISITAFV

---

## 19. Data de Faturamento e Previsao

### 19.1 Parametrizacao Completa

| Parametro | Descricao |
|-----------|-----------|
| OBRIGAR_PREVISAO_FATURAMENTO | 'N' para nao obrigar. Ativar e desativar na central para deixar como 'N' |
| PREVISAO_FATURAMENTO_DIA_MAIS_UM | Gravar previsao sempre com data de amanha (dia+1) |
| CONSIDERAR_DATA_ATUAL_PREV_FAT | Se 'S': conta a partir da data de edicao. Se 'N': conta a partir da data de criacao |
| PRAZO_VALIDADE_PREVISAOFATURAMENTO | Numero que define data maxima para previsao. Tipo NUMBER |
| PRAZO_VALIDADE_PEDIDO | Prazo de validade para envio de pedido salvo e bloqueado |

Apos alteracao, pedidos existentes devem ser duplicados — parametrizacao so aplica em pedidos novos.

---

## 20. Bonificacao

### 20.1 TV5 vinculado a TV1

Parametros:
- **OBRIGATORIVINCULARTV5COMTV1** / **MXS_OBRIGATORIOVINCULARTV5COMTV1**: Obrigar vinculo
- **PEDIR_AUTORIZACAO_TV5_VINCULADO_TV1**: Enviar para aprovacao no maxGestao
- **QTDE_DIAS_VINCULO_TV1_COM_TV5**: Dias que o TV1 pode ser vinculado ao TV5
- **PERC_LIMITE_TV5_RCA**: Porcentagem aceita do pedido bonificado em relacao ao TV1

### 20.2 Chave Tripla (mesmo item normal + bonificado no mesmo pedido)

- **TRUNCAR_ITEM_PCPEDI**: Se 'N', permite insercao duplicada
- **CON_USACHAVETRIPLAPCPEDI**: Habilita chave tripla (MXSPARAMFILIAL)

### 20.3 Bonificacao nao aparece para cliente (TV5)

1. Verificar coluna CONDVENDA5 na MXSCLIENT
2. Verificar vinculo com Plano de Pagamento de Bonificacao na MXSPLPAGCLI
3. Verificar vinculo com cobranca de Bonificacao na MXSCOBCLI
4. Verificar coluna TIPOPRAZO do Plano de Bonificacao (deve ser 'B')

### 20.4 Cobrancas aceitas na Bonificacao

Codigos validos: BNF, BNFR, BNTR, BNFT, BNRP, BNFM

---

## 21. Tributacao e Impostos

### 21.1 Erro "Nao foi possivel carregar a tributacao"

Verificar:
- Se cliente possui filial NF
- Se processo na 316 esta operacional
- Se existe tributacao para produto naquela filial

```sql
-- Verificar tributacao
SELECT * FROM MXSTABTRIB; -- olhar filiais e CODST
SELECT * FROM MXSTABPR WHERE CODPROD = ??; -- campo CODST preenchido
SELECT * FROM MXSTRIBUT; -- CODST existente e CODOPERACAO
```

---

## 22. Titulos Abertos e Pagos

### 22.1 Fluxo de dados

PCPREST > ERP_MXSPREST > MXSTITULOSABERTOS

Campos necessarios para APK entender que titulos foram pagos: VPAGO e DTPAG

```sql
SELECT * FROM ERP_MXSPREST WHERE CODCLI = ?;
SELECT * FROM MXSTITULOSABERTOS WHERE CODCLI = ?;
```

### 22.2 Parametros

| Parametro | Descricao |
|-----------|-----------|
| SOMAR_JUROS_TITULOS | Mostra valor de juros no valor total de titulos |
| HABILITAR_SOMA_MULTA_TITULO | Habilita soma da multa no saldo |
| EXIBIRTITULOSPAGOS | Exibir titulos pagos |
| ENVIARTITULOSPAGO | Enviar titulos pagos |

### 22.3 Bloquear Pedido para Clientes Inadimplentes

- **BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE** = 'S': Bloqueia independente do tempo se NUMERO_DIAS = 0
- **NUMERO_DIAS_CLIENTE_INADIMPLENTE**: Dias maximos (MXSPARAMETRO)
- **CON_NUMDIASMAXVENDACLIINADIMPLENTE**: Dias maximos (MXSPARAMFILIAL)
- MaxPedido considera o MAIOR valor entre os dois parametros

---

## 23. Plano de Pagamento

### 23.1 Tabelas Relacionadas

```sql
SELECT * FROM MXSCOB;        -- tipos de cobranca (CODCOB)
SELECT * FROM MXSPLPAG;      -- plano de pagamento (CODPLPAG)
SELECT * FROM MXSPLPAGCLI;   -- vinculo cliente/plano
SELECT * FROM MXSCOBPLPAG;   -- vinculo cobranca/plano
```

### 23.2 Erro ao Alterar Plano

- Verificar permissoes do RCA para aquele tipo de venda
- Verificar requisicao no banco de dados
- Caso de venda bonificacao: TIPOPRAZO na MXSPLPAG deve ser 'B' (nao 'N')

---

## 24. Margem de Lucratividade

### 24.1 Verificar Permissao

Na Central de Configuracoes: "Habilitar visualizacao de margem/lucratividade"

### 24.2 Calculo

- **Por pedido**: ((VLATEND - VLCUSTOFIN) / VLATEND) * 100
- **Por item**: ((PVENDA - VLCUSTOFIN) / PVENDA) * 100

### 24.3 Niveis de Validacao

1. **Por PEDIDO**: Parametro 1370 do Winthor (% de margem minima)
2. **Por PLANO DE PAGAMENTO**: Coluna MXSPLPAG.MARGEMMIN
3. **Por ITEM**: Coluna MXSPRODFILIAL.PERCMARGEMMIN
4. **Por ERP**: Parametro CON_MARGEMMIN na MXSPARAMFILIAL

---

## 25. Estoque

### 25.1 Bloquear Venda sem Estoque

| Parametro | Descricao |
|-----------|-----------|
| BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE | Bloqueia insercao de item sem estoque |
| BLOQUEAR_VENDA_ACIMA_DO_ESTOQUE | Bloqueia venda acima do estoque |
| BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE_CAMPANHA | Bloqueia para campanhas |
| VALIDA_RESTRICAO_ESTOQUE | Valida restricao de estoque |
| OCULTAR_PROD_FL_SEM_ESTOQUE | Oculta produtos sem estoque da lista |

---

## 26. Embalagens e Multiplos

### 26.1 Multiplo da Embalagem

Para OERPs:
1. Desabilitar parametro USAR_MULTIPLO_QTDE
2. Enviar coluna VALIDARMULTIPLOVENDA da MXSCLIENT como 'S'
3. Enviar quantidade de multiplo na coluna MULTIPLO da MXSPRODFILIAL ou MXSPRODUT

Para nao obrigar multiplo: VALIDARMULTIPLOVENDA = 'N'

Para produtos Frios: TIPOESTOQUE = 'FR', UNIDADE = 'FR', com PESOPECA e PESOBRUTOMASTER preenchidos.

### 26.2 Mostrar todas as Embalagens

- OCULTAR_EMBALAGEM_LISTAGEM = 'N'
- LISTAR_PRODUTOS_POR_EMBALAGENS = 'S'

---

## 27. Cadastro de Cliente

### 27.1 Cadastro Duplicado

Verificar parametro **HABILITA_PED_CLI_NAO_SINC**. Se habilitado, fazer swipe na tela de gerenciar clientes. Problema ocorre porque cliente recém-cadastrado fica na MXSCADCLIENTES da base do RCA (nao na MXSCLIENT). Apos sincronizar sem swipe, aparece em ambas.

### 27.2 Erro de Aprovacao de Cadastro

Erro: "Nao foi possivel confeccionar pedidos para clientes sem que antes seu cadastro seja aprovado pela empresa"

Causa: Coluna CODFUNCULTALTER com valor nulo.

Solucao:
- Winthor: Entrar no cadastro do cliente e clicar em "Salvar"
- Outros ERPs: Enviar endpoint "Clientes" com coluna CODFUNCULTALTER preenchida

### 27.3 Forcar Atualizacao de Cadastro

- **FORCAR_ATUALIZACAO_CADASTRO_CLIENTE** = 'S'
- **DIAS_ATUALIZACAO_CADASTRO_CLIENTE**: Numero de dias para verificar ultima atualizacao (se 0, nao valida)

### 27.4 Cliente nao Aparece

Verificar CODUSUR do usuario nas tabelas MXSCLIENT e ERP_MXSUSURCLI. Se nada exibido, orientar configurar vinculo dos clientes pelo ERP.

### 27.5 Endereco de Entrega Diferente

1. Configurar permissao do usuario na Central de Configuracoes
2. Para OERPs: enviar enderecos no endpoint "ClientesEnderecos" (tabela MXSCLIENTENDENT)
3. Na aba TOTAIS do pedido, e possivel alterar endereco de entrega

---

## 28. Mix do Cliente

### 28.1 Mix nao aparece

Tabelas: MXSMIXCLIENTES, MXSPARAMETRO, PCMXSCONFIGURACOES

**Se o mix nao estiver no banco nuvem:**
- GERAR_DADOS_MIX_CLIENTES = 'S' (nuvem e local)
- GERAR_DADOS_MIX_CLIENTES_DIAS: valor maximo 90 dias
- Se nao funcionar: testar GERAR_MIXCLIENTE_HISTORICO

**Se o mix estiver no SQLite mas nao no app:**
Verificar filtros:
- OCULTAR_PROD_ABAMIX_SEMESTOQUE
- FILTRAR_DADOS_RCA_MIXVENDIDO
- FILTRAR_FILIAL_MIX

---

## 29. Filial Retira

### 29.1 Conceito

Filial Retira permite fazer pedidos em uma filial e retirar/ter estoque em outra filial.

### 29.2 Parametrizacao

| Parametro | Descricao |
|-----------|-----------|
| DEFINE_FILIAL_RETIRA_PADRAO | Numero da filial retira padrao (tipo NUMBER) |
| UTILIZAFILIALRETIRAFILIALESTOQUE | Obrigatorio para utilizar filial retira |
| LISTAR_PROD_EST_RETIRA | Lista produtos da filial retira definida na MXSFILIALRETIRA |
| TOTALIZA_ESTOQUE_LISTAGEM_PRODUTO | Totaliza estoque na listagem |
| USA_DESMEMBRAMENTO_PEDIDO | Desmembramento por filial |
| VALIDAR_FILIALRETIRADIFERENTE | Valida filial retira diferente |

### 29.3 Filial nova nao aparece

Verificar:
- MXSEST: se tem estoque naquela filial
- PCPRODFILIAL: se ENVIAFORCADEVENDA/ENVIAFV = 'S'
- Se tem precificacao para os produtos (PCTABPR)
- Permissoes do RCA na central (acesso a filial para VENDA e ESTOQUE)

---

## 30. Tabela de Preco

### 30.1 Tabelas de Precos Diferentes no Mesmo RCA

Pre-requisito: Cliente deve ter cadastro na MXSTABPRCLI com filialnf e regiao desejada.

Parametros:
- PERMITE_FILIAL_NF_NULA = 'S'
- COMPORTAMENTO_WHINTOR_FILIAL = 'S'
- IGUALAR_FILIALNF_AO_ALTERAR_FILIAL = 'N'

Para acessar tabela de preco da regiao na PCTABPRCLI: selecionar Filial NF cadastrada.
Para acessar tabela de preco da regiao na PCTABPR: selecionar Filial NF nula.

### 30.2 Tipos de Precificacao

- MXSTABPR
- MXSPRECOPROM
- MXSEMBALAGEM
- MXSTABPRCESTA
- MXSTABPR e MXSEMBALAGEM possuem coluna PVENDAATAC

### 30.3 Cliente com Precos Diferentes (mesma regiao e praca)

```sql
-- Comparar regioes de clientes
SELECT NUMREGIAO FROM MXSPRACA
WHERE CODPRACA IN (SELECT CODPRACA FROM MXSCLIENT WHERE CODCLI IN (CODCLI1, CODCLI2));
```

Tabelas relacionadas: MXSPLPAGREGIAO (VINCULO_REGIAO_PLANO), MXSCLIENTREGIAO, MXSFILIALREGIAO

---

## 31. Validade de Produto / WMS

### 31.1 Validade WMS

Parametro: **EXIBE_VALIDADE_PRODUTO_WMS** = 'S'

Se "Nao cadastrado":
1. Verificar tabela nuvem: MXSVALIDADEWMS (Endpoint MXSLOTE)
2. Verificar parametro EXIBIR_VALIDADE_WMS_VENCIDA
3. Verificar parametro EXIBE_VALIDADE_PRODUTO_WMS

Tabelas Winthor: PCESTENDECOI, PCESTENDERECO, PCVIEWVALIDADEWMS

### 31.2 Validade/Vencimento do Produto

- Tela "Informacoes adicionais": vem da coluna DTVENC da MXSPRODUT
- Tela "Listar Lotes": vem da MXSLOTE (parametro LISTAR_INFO_LOTES habilitado)

---

## 32. Segunda Via de Boleto

### 32.1 Requisitos

- Versao minima: 2.223.9
- Ambiente nuvem atualizado
- Para editar layout do boleto: HABILITAR_GERADOR_RELATORIOS = 'S'

### 32.2 Fluxo na APK

1. Acessar CONSULTAS no menu
2. Acessar opcao "Titulos"
3. Clicar e segurar no titulo do cliente > "Gostaria de compartilhar o boleto?" > "Sim"

Parametro EXIBE_LINHA_DIGITAVEL = 'N' faz a sessao de compartilhar boleto nao aparecer.

### 32.3 Erro ao compartilhar boleto

Verificar:
- Coluna NOSSONUMBCO da ERP_MXSPREST e MXSTITULOSABERTOS deve estar preenchida
- Coluna LINHADIG das mesmas tabelas deve estar preenchida

---

## 33. Carga de Filial Nova

### 33.1 Procedimento

1. Verificar filiais de importacao:
```sql
SELECT * FROM PCMXSCONFIGURACOES WHERE NOME LIKE '%FILIAL%';
```

2. Adicionar nova filial nos parametros:
```sql
UPDATE PCMXSCONFIGURACOES SET VALOR = 'xxxxxxxx' WHERE NOME = 'CODFILIAL_PREST';
UPDATE PCMXSCONFIGURACOES SET VALOR = 'xxxxxxxx' WHERE NOME = 'CODFILIAL_IMPORTACAO';
```

3. Rodar script de carga no SQLDeveloper (usar F5)
4. Acessar Carga Total via website (HTTP, nao HTTPS)
5. Selecionar cliente, marcar nova filial na aba FILIAIS
6. Na aba GRUPO DE TABELAS selecionar as 10 categorias necessarias
7. Na aba PERIODOS colocar periodo de 3 meses

```sql
-- Acompanhar carga (banco nuvem)
SELECT tabela, COUNT(1) FROM maxsolucoes.pcmxsintegracao
WHERE status='-1' GROUP BY tabela ORDER BY COUNT(1) DESC;
```

### 33.2 Filial nova nao aparece para RCA

- Verificar permissao na Central de Configuracoes
- Dar carga de ATUALIZAID nas tabelas: MXSEST, MXSFILIAL, MXSPRODFILIAL, MXSEMBALAGEM, MXSTABPR, MXSPRODUT

---

## 34. Solicitacao de Autorizacao de Pedidos

### 34.1 Via maxGestao

Tabelas:
- MXSINTEGRACAOPEDIDO: JSON contem info de autorizacao
- MXSAUTORI: Armazena autorizacoes do maxGestao
- PCAUTORI: Autorizacao salva no Winthor com observacao do maxGestao

Permissoes necessarias na Central:
- Permitir solicitacao de autorizacao de preco
- Solicitar aprovacao para pedidos com limite excedido
- Solicitar aprovacao para pedidos com cliente bloqueado

### 34.2 Via Winthor

Rotina 336 ou 301. Desabilitar permissoes na Central para que o pedido va para PCPEDC e caia na rotina 336.

---

## 35. Bloqueios de Pedido

### 35.1 Bloquear Pedidos Fora do Horario

Parametro principal: **BLOQ_VENDA_FORA_HORARIO_COM** = 'S'

Parametros de horario (tipo NUMERICO, formato sem dois pontos):
- BLOQ_VENDA_FORA_HORARIO_COM_IM: Hora inicio manha (ex: 0830)
- BLOQ_VENDA_FORA_HORARIO_COM_TM: Hora termino manha
- BLOQ_VENDA_FORA_HORARIO_COM_IT: Hora inicio tarde
- BLOQ_VENDA_FORA_HORARIO_COM_TT: Hora termino tarde

Para Winthor: usar rotina 535 com "Valida horario de trabalho" (pedidos ficam em espera na API).

### 35.2 Bloquear Pedidos Fora de Rota

- Permissao "Bloquear venda de clientes fora da rota" na Central
- **QTD_MAX_PED_FORA_ROTA**: Numero maximo (nao pode ser zero)
- **PERIODO_PED_FORA_ROTA**: Periodo de validacao (0 = so dia atual, 1 = atual + anterior)

### 35.3 Bloquear Envio acima do Limite do Cliente

| Prioridade | Parametro | Descricao |
|------------|-----------|-----------|
| 1 | BLOQ_SALVAR_PEDIDO_ACIMA_LIMITE_CLI_APK | Bloqueia salvamento na APK independente do Winthor |
| 2 | BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE | Se CON_ACEITAVENDABLOQ = N: nao envia. Se = S: aceita |

---

## 36. Erro de Custo Financeiro

### 36.1 Descricao

Erro: "Custo Financeiro, Custo Real ou Custo Real + Credito de ICM invalidos"

Geralmente acontece quando valores MXSEST.CUSTOREAL, MXSEST.CUSTOFIN ou MXSEST.CUSTOREP sao iguais a zero (devem ser MAIOR que zero).

```sql
SELECT CUSTOREAL, CUSTOFIN, CUSTOREP, E.* FROM MXSEST E WHERE CODPROD = (:codprod);
```

Se valores estao corretos, verificar filial retira padrao no MXSPRODUT.CODFILIALRETIRA. Se cliente nao tem acesso a filial retira, o maxPedido tenta buscar custo dessa filial e falha.

---

## 37. Erro Trigger Banco Local

### 37.1 Procedimento

Geralmente faltas de views/trigger no banco local se devem ao Atualizador ter sido rodado mas Jobs do Hangfire nao terem sido rodadas.

1. Atualizar EXTRATOR/EXTRATOR-EKS para ultima versao
2. Rodar o Atualizador
3. Rodar Jobs no Hangfire:
   - Pagina 1: ProcessamentosWebApi.ObterScripts
   - Pagina 2: Atualizacao de Banco de Dados

Se persistir:
```sql
-- No banco NUVEM: ativar PRIMEIRA_IMPLANTACAO
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%PRIMEIRA_IM%';
UPDATE MXSPARAMETRO SET VALOR = 'S' WHERE CODPARAMETRO = 390;
-- Verificar no banco local se trigger nao tem mais erro
-- Depois voltar o valor
UPDATE MXSPARAMETRO SET VALOR = 'N' WHERE CODPARAMETRO = 390;
-- Parar e ligar o extrator
```

### 37.2 Objetos Invalidos no Banco Local

```sql
SELECT OWNER, OBJECT_TYPE, OBJECT_NAME, STATUS,
    'alter ' || DECODE(OBJECT_TYPE, 'PACKAGE BODY', 'PACKAGE', OBJECT_TYPE)
    || ' ' || OWNER || '.' || OBJECT_NAME
    || DECODE(OBJECT_TYPE, 'PACKAGE BODY', ' compile body;', ' compile;') COMPILE
FROM ALL_OBJECTS
WHERE STATUS != 'VALID'
ORDER BY OWNER, OBJECT_TYPE, OBJECT_NAME;
```

Se houver objetos invalidos, cliente deve contatar Suporte TOTvs ou DBA.

### 37.3 Tabela com Lock no Banco Local

```sql
SELECT DISTINCT SES.PROGRAM EXECUTAVEL,
    OBJ.OBJECT_NAME TABELA,
    SES.STATUS,
    'alter system kill session ''' || SID || ',' || SERIAL# || ''' immediate;' COMANDO_DESCONEXAO,
    SQL.SQL_TEXT TEXTO_SQL
FROM V$SESSION SES, V$LOCKED_OBJECT LOC, DBA_OBJECTS OBJ, V$SQL SQL
WHERE SES.SID = LOC.SESSION_ID
  AND LOC.OBJECT_ID = OBJ.OBJECT_ID
  AND SES.SQL_ADDRESS = SQL.ADDRESS(+)
ORDER BY SES.LAST_CALL_ET DESC;
```

---

## 38. Extrator / Portainer / Hangfire

### 38.1 Atualizar Ambiente do Cliente

1. Acessar portal GERIR > menu lateral > Monitoramento (4003) > buscar cliente
2. Rodar atualizacao do Portainer (ver ultima versao no Discord canal MaxPedido)
3. Rodar Atualizador (aguardar "sucesso")
4. Acessar Hangfire e disparar 2 jobs:
   - Pagina 1: Job de web scripts
   - Pagina 2: Job de atualizacao de banco de dados
5. Atualizar versao do maxPedido

### 38.2 Atualizar Extrator Mantendo Versao

1. Parametro PRIMEIRA_IMPLANTACAO = 'S'
2. Reiniciar extrator
3. Atualizar ambiente e hangfire

### 38.3 Reinstalacao do Docker / Extrator

Comandos para desinstalar Docker:
```bash
sudo apt-get purge -y docker*
sudo apt-get autoremove -y --purge docker*
sudo rm -rf /var/lib/docker /etc/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/run/docker.sock
```

Comandos para instalar Docker:
```bash
sudo apt update
sudo apt-get remove docker docker-engine docker.io containerd runc -y
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

Instalar Portainer:
```bash
docker run -d -p 9000:9000 --name MXS_Portainer --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data portainer/portainer-ce
```

### 38.4 Stack do Extrator (Docker Compose)

Estrutura basica do compose:
- Image: dockermaxima/extrator:VERSAO
- Variaveis de ambiente: USUARIO_EXTRATOR_NUVEM, SENHA_EXTRATOR_NUVEM, USUARIO_SYSTEM_WINTHOR, SENHA_SYSTEM_WINTHOR, TZ
- Volumes para: docker.sock, imagens, configuracao, logs
- Porta padrao: 9002:81

### 38.5 Problema de Bloqueio no APPSV

Testar conectividade via console Linux:
```bash
telnet intext-hmg.solucoesmaxima.com.br 81
telnet intpdv-hmg.solucoesmaxima.com.br 81
telnet appsv.solucoesmaxima.com.br 8081
```

Se bloqueado: cliente deve verificar firewall para portas e links.

### 38.6 T-Cloud

Atualizacao pelo Jenkins:
- Extrator EKS PROD
- Ler Variaveis
- Build with Parameters (nome do ambiente em minusculo, codigo do extrator do Gestao Nuvem menu 302)
- Trocar IP e Porta: 443 no menu 302

---

## 39. Fotos de Produtos

### 39.1 Problemas com Download de Fotos

- Nao utilizar economia de energia (previne servicos em segundo plano)
- APK busca novas fotos a cada 6 horas

### 39.2 Ponto de Montagem (Linux)

Para compartilhar pasta de fotos do Winthor com o extrator no Linux:

1. Acessar maquina Linux via Putty
2. Instalar ferramentas: `sudo apt install cifs-utils -y`
3. Criar arquivo mount.sh na pasta raiz com configuracao do ponto de montagem
4. Dar permissao: `chmod +x mount.sh`
5. Adicionar ao crontab: `*/1 * * * * root $SHELL /mount.sh`
6. Executar: `sh mount.sh`
7. Verificar: `df -h`
8. Configurar volume na stack do extrator
9. Reiniciar extrator

Importante: No Linux nao e possivel reconhecer mapeamento do Windows por nome, usar IP.

---

## 40. Pedido Complementar

### 40.1 Conceito

Pedido que complementa o pedido principal. Permite adicionar itens a um pedido ja feito (com NUMPEDERP gerado) para sair tudo na mesma nota fiscal.

Parametro: **HABILITAR_OPCAO_PEDIDO_COMPLEMENTAR**

Restricoes:
- Nao e possivel inserir no complementar um produto ja inserido no principal
- TV1 nao pode estar na posicao "Faturado" no ERP

### 40.2 Fluxo

1. Fazer pedido TV1
2. Clicar no checkbox "E complementar" no cabecalho do novo pedido
3. Selecionar pedido original na listagem

---

## 41. Positivacao de Produtos e Clientes

### 41.1 Definicoes

- **Cliente positivado**: Cliente com pedido faturado naquele mes
- **Produto positivado**: Produto de pedido faturado por cliente naquele mes

Necessario dados na tabela PCDATA. Consultar pela MXSPRODUTPOS.

### 41.2 Parametros

| Parametro | Descricao |
|-----------|-----------|
| GERAR_DADOS_POS_PRODUTOS | Habilita gerar e exibir produtos positivados |
| CONSIDERA_POS_CLIENTE | Define se positivacao de itens considera clientes |
| FILTRAR_DADOS_CONSULTA_POSITIVACAO_RCA | Filtra positivados ao RCA individual |
| CONSULTA_PRODUTO_POSITIVADO_PRODUTPOS | Exibe numericamente quantidade positivada nos cards |

---

## 42. Comissoes

### 42.1 Para OERPs

Enviar por endpoints: ComissoesRegioes (MXSCOMISSAOREGIAO) ou ComissoesUsuarios (MXSCOMISSAOUSUR)

### 42.2 Parametro

**EXIBIR_SUGESTAO_PRECO_COMISSAO**: Apresenta diferenca em reais da comissao que o RCA recebera com determinado desconto. Depende da coluna PERDESCMAX da MXSTABPR.

### 42.3 Tabelas

- MXSCOMISSAOREGIAO: Coluna TIPOVENDEDOR deve conter mesmo valor que MXSUSUARI.TIPOVEND
- MXSCOMISSAOUSUR: Coluna TIPO deve ser sempre 'RP'

---

## 43. WTA — API de Cancelamento

### 43.1 Configuracao

Parametro: **UTILIZA_API_CANCEL_WINTHOR** = 'S'

Validar acesso da API na rotina 132 (WTA). Informacoes preenchidas no portainer/compose/docker:
- LINK_API_WINTHOR_CANCELAMENTO
- USUARIO_API_WINTHOR_CANCELAMENTO
- SENHA_API_WINTHOR_CANCELAMENTO (criptografada)

```sql
-- Ver IP e porta do WTA do cliente
SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%MOBILE%';
```

Versao minima: 3 do aplicativo

---

## 44. Nivel de Venda

### 44.1 Regra

Cliente com cobranca de nivel de venda 1 tem acesso a todos os niveis. Cliente com nivel 5 so pode usar cobranças com niveis de restricao menor.

Exemplo: Se CODCLI vinculado a cobranca de nivel 5, e cobranca de Bonificacao tem nivel 3, o cliente NAO pode fazer venda com essa cobranca.

---

## 45. Sugestao de Venda

### 45.1 Requisitos

Para funcionar, o cliente deve cumprir uma condicao:
1. Comprar um produto repetidamente
2. Possuir historico de compra repetidamente nos ultimos 3-6 meses

Processo ocorre na APK usando dados da MXSHISTORICOPEDC e MXSHISTORICOPEDI.

Se parametro **CATALOGO_PEDIDOS_DIAS_SYNC** = 30, improvavel haver sugestao. Recomendado minimo 90 dias (ideal 180 dias).

Apos alteracao de dias, necessario dar carga de dados na HISTORICOPEDC e HISTORICOPEDI.

---

## 46. Coordenadas do Cliente

### 46.1 Parametros de Atualizacao

| Parametro | Descricao |
|-----------|-----------|
| GPS_UPDATE_COORDENADAS_ON_PEDIDO | Atualizar coordenadas ao fazer pedido |
| GPS_UPDATE_COORDENADAS_ON_JUSTIFICATIVA_VISITA | Atualizar ao justificar visita |
| GPS_UPDATE_COORDENADAS_ON_ALTERACAO_CADASTRO_CLIENTE | Atualizar ao alterar cadastro |
| CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE | Questiona usuario se deseja atualizar GPS (com GPS_TRACKING_ENABLED) |

---

## 47. DANFE — Compartilhar Nota Fiscal

### 47.1 Requisitos

- Banco atualizado
- Ter informacoes na tabela ERP_MXSDOCELETRONICO
- Versao V4

### 47.2 Possiveis Problemas

- Pedido com POSICAO diferente de Faturado: opcoes DANFE e XML ficam desabilitadas
- Coluna NUMTRANSVENDA da MXSHISTORICOPEDC nao desceu para APK
- Opcao de compartilhar boleto so aparece se MXSCOB.BOLETO = 'S' e EXIBE_LINHA_DIGITAVEL habilitado
- Erro "Nao foi possivel gerar o XLS": verificar permissoes do app "Acesso a todos os arquivos"

---

## 48. MaxGestao

### 48.1 Acesso

PWA: https://maxgestao-pwa.solucoesmaxima.com.br

### 48.2 Dashboard — Indicadores

Rotinas: 146 (Emissao), 111 (Faturamento)

Parametros que devem estar ativos no ERP (PCMXSCONFIGURACOES):
- UTILIZA_GESTAO_LOGISTICA
- ENVIA_PEDIDOS_TELEMARKETING
- ENVIA_PEDIDOS_BROKER
- ENVIA_PEDIDOS_CALL_CENTER
- ENVIA_PEDIDOS_BALCAO
- ENVIA_PEDIDOS_AUTOSERVICO
- ENVIAR_PRODUTO_SEM_REVENDA

### 48.3 RCA vinculado nao aparece ao Supervisor

- Verificar MXSUSUARI.CODSUPERVISOR do usuario
- Verificar MXSSUPERV se e o supervisor correto

### 48.4 Localizacao — maxTrack

Parametro basico: **GPS_TRACKING_ENABLE**

Consideracoes:
- Nem todo RCA pode ser rastreado (so CLT ou PJ com contrato)
- Fornecer acesso a localizacao o tempo todo nas permissoes do app
- Pode ser ligado POR USUARIO (util para PF e PJ)
- Modo aviao e economia de energia NAO podem estar ativados

Parametros GPS:
- GPS_TRACKING_INTERVAL: intervalo de captura em segundos (recomendado 30s)
- GPS_TRACKING_STARTTIME: quando o servico inicia (ex: 0700)

### 48.5 Painel de Auditoria — API de Rastro

A API guarda informacoes em ate 45 dias.

Para analise de divergencias:
1. Coletar Login/Senha maxPedido, Base maxPedido (Exportar Banco), Base maxTrack
2. Consultar Painel de Auditoria com filtros
3. Analisar base maxTrack com SQLite:
```sql
SELECT * FROM MXS_EVENTS E
WHERE DATA_HORA_EVENTO BETWEEN '2023-12-14T00:00:00' AND '2023-12-14T23:59:59';
```

### 48.6 Roteirizacao de Vendedores

Disponivel somente no maxGestao PLUS. Passo a passo:
1. Cadastrar carteira de clientes para o vendedor
2. Cadastrar coordenadas para clientes e vendedor
3. Criar rota para o RCA
4. Cadastrar regioes
5. Cadastrar dias da semana
6. Montar Agenda de Visita

### 48.7 Rota nao Aparece

Verificar MXSCOMPROMISSOS filtrando por CODUSUARIO. Comparar DTPROXIMAVISITA com data reclamada. Se existe rota na ERP_MXSROTACLI mas nao na MXSCOMPROMISSO, verificar parametro **GERAR_VISITAS_MES** = 'S'. Rodar atualizador e hangfire.

```sql
-- Verificar rota no banco local
SELECT * FROM PCROTACLI WHERE CODUSUR = 94 ORDER BY DTPROXVISITA DESC;
```

### 48.8 Metas nao Aparecem no maxGestao

Verificar:
- Dias uteis na ERP_MXSDATAS e MXSMETA
- Para Winthor: parametro OUTROS_ERP nao cadastrado ou = 'N'
- UTILIZA_GESTAO_LOGISTICA na PCMXSCONFIGURACOES = 'S'

### 48.9 Supervisor nao aparece no Painel de Auditoria

Possivel falta de vinculo de filial. Verificar MXSUSUARI.CODFILIAL. Se supervisor de todas as filiais, usar filial 99.

---

## 49. MaxCatalogo

### 49.1 Liberacao de Versao

- maxPedido deve estar ACIMA da versao 3.246.0
- Rotina: 9
- Link de acesso: https://maxcatalogoapi.solucoesmaxima.com.br/api/v1/
- Package: br.maximasistemas.catalogo

---

## 50. MaxPromotor

### 50.1 Conceito

Trade Marketing: Varejistas, Fabricante e Distribuidor trabalham entre si para impulsionar retorno financeiro.

### 50.2 Funcionalidades

- **Agenda**: Tarefas planejadas para o dia
- **Tempo Produtivo**: Tempo dentro do PDV (Check-In ate Check-Out)
- **Treinamentos e Incentivos**: Arquivos PDF/TXT com instrucoes
- **Cadastro de clientes**: Simbolo de 2 pessoas com + no menu superior
- **Mapa**: Localizacao do promotor e clientes do roteiro
- **Roteiro**: Clientes que o promotor devera visitar
- **Pesquisas**: Dentro do card do cliente
- **Pedidos**: Historico de pedidos do maxPedido aparece na aba pedidos

### 50.3 Padrao para Ticket N3

Incluir:
- Versao da APK do Promotor
- Versao da Web e Sincronizacao (obter via Jenkins > MAXPROMOTOR-EKS_PRODUCAO-listarClientesVersoes)
- Backup da APK
- Link do Portal Web
- Acesso WEB (Login e Senha)
- Acesso APK (se problema na APK)

### 50.4 Erro de Sincronizacao

**Cliente OnPremise**: Verificar se servico esta ativo no servidor. Acessar http://localhost:8186/maxpromotor localmente. Se nao abrir, verificar servico no gerenciador de tarefas.

**Cliente EKS**: Verificar link de conexao no formato: Nome-Do-Cliente.maxpromotor.com.br (sem HTTP, sem nada apos .com.br). Tentar reiniciar servico SYNC pela pipeline.

---

## 51. MaxPag

### 51.1 Anti-Fraude

Ativar sistema de Anti-Fraude nas configuracoes do maxPag.

### 51.2 Cadastro de Cobranca

**Cobranca PIX**: Pelo menos uma condicao verdadeira:
- MXSCOB.CODMOEDA = 'PIX'
- MXSCOB.CODCOB = 'PIX'

**Cobranca Cartao**:
- Parametro PERMITIR_VENDA_CARTAO_CREDITO = 'S'
- MXSCOB.TIPOCOBRANCA = 'C'

---

## 52. Parametros Diversos

### 52.1 Consumidor Final

- FILTRAR_CLIENTES_CONSUMIDOR_FINAL
- FILTRAR_CLIENTES_CONSUMIDOR_FINAL_ENTRE_UM_TRES
- Desativar para que cliente apareca

### 52.2 Simples Nacional e Contribuinte

- CLIENTECONTRIBUINTE_SIM: Valor padrao de contribuinte no cadastro
- CLIENTESIMPLESNACIONAL_SIM: Valor padrao de simples nacional

### 52.3 CNPJ nao encontrado na Receita Federal

A Maxima usa o portal RECEITAWS (nao consulta diretamente na Receita Federal). CNPJs novos podem demorar meses para serem incluidos. Se necessario, solicitar inclusao via contato@receitaws.com.br. Verificar na tabela MXSCIDADE se dado existe.

### 52.4 Ramo de Atividade

Erro "Nenhum ramo de atividade encontrado":
- Verificar na MXSCLIENT se CODATV1 nao esta NULL
- Verificar na MXSATIVI

### 52.5 Quantidade Maxima de Itens por Pedido

- VERIFICAR_QTD_MAX_ITENS_PEDIDO = 'S'
- VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO = numero maximo

### 52.6 Campanha por Pontuacao

Tabelas: MXSPROMOI, MXSPROMOC
Parametro: EXIBIR_PONTOS_PROD_LISTAGEM

### 52.7 Mensagem de Endereco Secundario

Erro: "E necessario escolher um endereco secundario para buscar tributacao"
Causa: Parametro UTILIZATRIBENDENT da rotina 132 habilitado para a filial. Desabilitar.

### 52.8 Importacao de Arquivo de Negociacao

Na Central de Configuracoes, as colunas devem ser cadastradas como INTEIRO (numerico), nao como String.

### 52.9 Dados de Entrega no maxPedido

Data entrega: DTENTREGA na PCPEDC
Data emissao: DTSAIDA na PCNFSAID

---

## Troubleshooting Rapido

### Problema: Produto nao aparece no maxPedido

**Sintoma**: RCA nao ve determinado produto
**Causas possiveis**:
1. MXSPRODUT.OBS2 = 'FL' (Fora de Linha) e parametro OCULTAR_PROD_FORA_LINHA habilitado
2. MXSPRODUT.CODDISTRIB diferente do MXSFORNEC.CODDISTRIB (divergencia de codigo de distribuicao)
3. Restricao na 391 — parametro RESTRINGIR_PRODUTOS_391 = 'N' para resolver

### Problema: Filial nao aparece para cliente especifico

**Solucao**: Verificar tabela de preco, MXSTABPRCLI, divergencias de base e restricoes de venda.

### Problema: Preco na listagem diferente da tela de negociacao

**Causa 1**: Campo CALCULAST da MXSCLIENT = 'N' (nao calcula ST)
**Causa 2**: Campo PERACRESCISMOPF da MXSTRIBUT preenchido sem parametro VALIDAR_ACRESCIMO_PF_LISTAGEM

### Problema: Credito disponivel nao atualiza na APK

**Causa**: Parametro CONSIDERAR_CLIENTE_EXCLUIDO_LIMITE na PCMXSCONFIGURACOES = 'N' e cliente principal com DTEXCLUSAO preenchido ou CODOPERACAO = 2.

---

## Referencias

- Fonte original: SERVICE DESK MAXIMA TECH PROCESSOS.pdf (documento interno de 214 paginas)
- Requisitos minimos: https://maximatech.com.br/requisitos
- Layout integracao Winthor: https://tdn.totvs.com/pages/releaseview.action?pageId=348295209
- Layout integracao maxPedido: https://basedeconhecimento.maximatech.com.br/pages/viewpage.action?pageId=12189810
- IPs para liberacao no Firewall: https://maximatech.com.br/requisitos/cloud-tipo-erp/cloud-winthor/

---

<!--
REGRAS PARA CRIACAO DE DOCUMENTOS PARA O RAG:
1. NUNCA incluir senhas, tokens, credenciais ou dados sensiveis
2. Usar titulos claros e descritivos (## e ###)
3. Separar secoes com --- (horizontal rule)
4. Incluir palavras-chave no inicio para melhorar a busca semantica
5. Usar tabelas para parametros e configuracoes
6. Incluir SQLs uteis em blocos de codigo
7. Manter linguagem objetiva e tecnica
8. Cada secao deve ser auto-contida
9. Evitar abreviacoes sem explicacao
10. Sempre citar a fonte original
11. Nao usar imagens (RAG nao processa imagens)
12. Substituir referencias a imagens por descricoes textuais
13. Usar listas numeradas para procedimentos passo-a-passo
14. Usar listas com marcadores para requisitos e observacoes
NOTA: Senhas e credenciais foram propositalmente removidas deste documento.
-->
