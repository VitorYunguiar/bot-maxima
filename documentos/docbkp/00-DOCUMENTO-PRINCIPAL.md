# SERVICE DESK MAXIMA TECH PROCESSOS — Base de Conhecimento maxPedido

**Palavras-chave**: maxPedido, Winthor, ERP, RCA, parâmetros, tabelas, MXSPARAMETRO, MXSCLIENT, MXSINTEGRACAOPEDIDO, check-in, check-out, sincronização, pedidos, SQL, banco de dados, integração, status, suporte

**Sistema**: maxPedido / Winthor / maxGestão

**Área**: Service Desk / Processos / Configuração

---

## Introdução e Visão Geral

### Sobre este documento

Este documento consolida informações técnicas e processuais relacionadas ao suporte e configuração dos produtos Máxima, com foco em maxPedido, integração com Winthor, banco de dados, parametrizações e resolução de problemas comuns. É destinado à equipe de Service Desk e suporte técnico.

### Fluxo Geral dos Produtos Máxima

- **maxPedido**: Aplicativo mobile para vendas, espelhado na rotina 316 do Winthor (Pedido de Vendas). Funciona baseado nas funcionalidades dessa rotina.
- **maxGestão**: Portal Web e APP para gestores acompanharem rotas, desempenho de RCA's e imprimirem relatórios.
- **maxPromotor**: Portal Web e APP para pesquisas e dashboards, voltado a promotores.
- **maxCatálogo**: APP para exibição de produtos do cliente.

Os pedidos feitos no maxPedido são gravados nas tabelas PCCLIENTFV, PCPEDCFV, PCPEDIFV (tabelas de gravação do Força de Vendas) e posteriormente integrados ao ERP.

---

## Tabelas Úteis do Banco de Dados

### MXSINTEGRACAOPEDIDO_LOG — Log de Integração de Pedidos

**Descrição**: Armazena os logs dos pedidos enviados pela APK, incluindo o JSON enviado e o status da integração. Útil para rastrear o processamento do pedido desde o envio até o retorno do ERP.

**Campos principais**:
- **ID_LOG**: identificador único do log
- **ID_PEDIDO**: referência ao pedido na MXSINTEGRACAOPEDIDO
- **JSON_ENVIO**: conteúdo JSON enviado pela APK
- **JSON_RETORNO**: conteúdo JSON retornado pelo ERP
- **STATUS**: código do status atual (0-salvo, 1-gravado nuvem, 2-bloqueado, etc)
- **DATA_HORA**: timestamp do log

**Relacionamentos**: FK para MXSINTEGRACAOPEDIDO (ID_PEDIDO).

### MXSHISTORICOCRITICA — Histórico de Críticas dos Pedidos

**Descrição**: Registra todas as críticas (erros, alertas) de cada pedido ao longo do tempo, permitindo consultar o histórico completo, não apenas a última crítica.

**Campos principais**:
- **ID_HISTORICO**: identificador único
- **ID_PEDIDO**: referência ao pedido
- **CRITICA**: texto da crítica
- **DATA_HORA**: data e hora da ocorrência

**Relacionamentos**: FK para MXSINTEGRACAOPEDIDO.

### MXSCONFIGERP — Configurações do ERP

**Descrição**: Contém parâmetros do ERP (Winthor) que influenciam o comportamento do maxPedido. Geralmente espelha configurações da rotina 132 (PARAMFILIAL).

**Campos principais**:
- **NOME**: nome do parâmetro (ex: CON_USATRIBUTACAOPORUF)
- **VALOR**: valor atribuído
- **CODFILIAL**: filial a qual se aplica

### MXSPARAMETRO — Parâmetros da Central de Configurações

**Descrição**: Armazena parâmetros configuráveis na Central de Configurações do maxPedido, aplicáveis globalmente ou por usuário.

**Campos principais**:
- **CODPARAMETRO**: código interno
- **NOME**: nome do parâmetro
- **VALOR**: valor definido
- **TIPODADO**: 1 - Literal, 2 - Inteiro, 3 - Lógico
- **TIPO_PARAMETRO**: GERAL / USUARIO / FILIAL

### MXSPARAMETROVALOR — Parâmetros da Central por Usuário

**Descrição**: Parâmetros atribuídos a usuários específicos, sobrescrevendo os valores globais quando necessário.

**Campos principais**:
- **CODPARAMETRO**: referência ao MXSPARAMETRO
- **CODUSUARIO**: código do usuário
- **VALOR**: valor específico para o usuário

### MXSAPARELHOSCONNLOG — Última Sincronização do RCA

**Descrição**: Registra a data e hora da última sincronização realizada pelo aparelho do RCA.

**Campos principais**:
- **CODUSUARIO**: código do usuário
- **ULTIMA_SINCRONIZACAO**: timestamp da última sincronização
- **STATUS**: status da conexão

### MXSCLIENT — Cadastro de Clientes

**Descrição**: Tabela principal de clientes no ambiente nuvem. Contém dados cadastrais, limites de crédito, vínculos com RCA, etc.

**Campos principais**:
- **CODCLI**: código do cliente
- **CODUSUR1, CODUSUR2, CODUSUR3**: códigos dos RCA's vinculados (até 3)
- **LIMCRED**: limite de crédito
- **DTULTCOMP**: data da última compra
- **ATUALIZID**: número usado para controle de sincronização (incrementado em alterações)
- **CODOPERACAO**: 1 = ativo, 2 = excluído

### ERP_MXSUSURCLI — Vinculo RCA/Cliente (ERP)

**Descrição**: Tabela de vínculo entre RCA (vendedor) e cliente, originada do ERP. Complementa os vínculos definidos no cadastro do cliente.

**Campos principais**:
- **CODUSUR**: código do RCA
- **CODCLI**: código do cliente

### MXSCOMPROMISSOS — Roteiro de Visitas (Agenda do RCA)

**Descrição**: Armazena os compromissos (visitas agendadas) dos RCA's, baseados na rota definida no maxGestão Plus (rotina 354) ou roteirizador.

**Campos principais**:
- **CODUSUARIO**: código do RCA
- **CODCLI**: código do cliente
- **DATA_COMPROMISSO**: data prevista da visita
- **STATUS**: realizado, pendente, justificado, etc.

**Relacionamentos**: Os dados são gerados a partir da ERP_MXSROTACLI.

### MXSHISTORICOCOMPROMISSOS — Backup de Compromissos

**Descrição**: Histórico de compromissos antigos, usado para auditoria e backup.

### ERP_MXSROTACLI — Rotas de Clientes (origem ERP)

**Descrição**: Tabela que alimenta a MXSCOMPROMISSOS. Contém as datas de próxima visita para cada cliente, conforme cadastro no Winthor (rotina 354).

### MXSTITULOSABERTOS / ERP_MXSPREST — Títulos Abertos

**Descrição**: Tabelas que armazenam os títulos (contas a receber) em aberto dos clientes. A MXSTITULOSABERTOS é a versão nuvem, alimentada pela ERP_MXSPREST (dados do ERP).

**Campos importantes**:
- **CODCLI**: código do cliente
- **VALOR**: valor do título
- **VPAGO**: valor pago
- **DTPAG**: data de pagamento
- **NOSSONUMBCO**: nosso número do boleto
- **LINHADIG**: linha digitável do boleto

### MXSCPARAMETRO — Parâmetros do MaxCatálogo

**Descrição**: Similar à MXSPARAMETRO, mas específica para o produto MaxCatálogo.

### MXSAPARELHOSDESBLOQLOG — Logs de Desbloqueio de Usuários

**Descrição**: Armazena logs de desbloqueio de usuários realizados na Central de Configurações ou no maxGestão mobile por supervisores.

### SYNC_D_MXSCLIENT — Amarração Usuário Máxima × Cliente

**Descrição**: Tabela que relaciona o usuário da Máxima (MXSUSUARIOS.CODUSUARIO) com o código do cliente (MXSCLIENT.CODCLI).

### MXSGRRELATORIO — Relatórios da Central de Configurações

**Descrição**: Armazena definições de relatórios personalizados criados na Central de Configurações.

### MXSLOCATION — Registros de Check-in/Check-out (SQLite)

**Descrição**: Tabela local no aparelho do RCA (SQLite) que guarda os registros de check-in e check-out nos clientes.

### MXMI_AGENDA_RCA — View de Cadastro de Roteiros

**Descrição**: View para visualizar os roteiros cadastrados pelo roteirizador de vendedores.

### MXSMAXPAYMENTMOV — Movimentações do maxPag

**Descrição**: Registra transações realizadas via maxPag (pagamentos eletrônicos).

### MXSDESCESCALONADOC, MXSDESCESCALONADOI, MXSDESCESCALONADORESTRI — Tabelas de Desconto Escalonado

**Descrição**: Armazenam configurações de descontos progressivos ou escalonados, com cabeçalho (C), itens (I) e restrições.

### MXSINTEGRACAOPEDIDOLOG — Log JSON dos Pedidos (APK → ERP)

**Descrição**: Quando a APK envia o pedido para a nuvem, o JSON é gravado nesta tabela. Após processamento pelo backend e retorno do ERP, o JSON final é atualizado na MXSINTEGRACAOPEDIDO, mas o log original permanece aqui.

### MXSTABELA — Informações de Tabelas Sincronizáveis

**Descrição**: Guarda informações sobre quais tabelas podem ser sincronizadas para o aparelho e seus metadados.

---

## Status de Pedidos e Tabelas de Processamento

### Status na MXSINTEGRACAOPEDIDO

**Descrição**: Códigos de status que indicam a etapa do pedido no fluxo de integração.

- **0** – Pedido salvo no aparelho (GRAVADO_APARELHO)
- **1** – Pedido gravado no banco nuvem (NUVEM_GRAVADO)
- **2** – Bloqueado na nuvem (NUVEM_BLOQUEADO)
- **3** – Aguardando autorização de preço/lucratividade/bonificação (NUVEM_AGUARDANDO_AUTORIZACAO)
- **4** – Pedido cancelado na nuvem (NUVEM_CANCELADO)
- **5** – Pedido enviado para o ERP (ERP_ENVIADO)
- **6** – Erro no processamento pelo ERP (ERP_REJEITADO)
- **7** – Pendente no ERP (MXSINTEGRACAOCLIENTEERP_PENDENTE)
- **8** – Liberado no ERP (ERP_LIBERADO)
- **9** – Bloqueado no ERP (ERP_BLOQUEADO)
- **10** – Montado no ERP (ERP_MONTADO)
- **11** – Faturado no ERP (ERP_FATURADO)
- **12** – Cancelado no ERP (ERP_CANCELADO)
- **13** – Orçamento enviado (ERP_ORCAMENTO_ENVIADO)
- **14** – Autorização rejeitada (NUVEM_AUTORIZACAO_REJEITADA)

### Status de Processamento Interno (Envio)

**Descrição**: Status utilizados no fluxo de comunicação entre a nuvem e o ERP.

- **RecebidoPeloServer** = 0
- **EnviadoParaApi** = 1
- **EnviadoParaErp** = 2
- **RecebidoPeloErp** = 3
- **ProcessadoPeloErp** = 4
- **ErroProcessamentoErp** = 5
- **PedidoBloqueadoEnvioErp** = 6
- **PedidoBloqueadoCancelado** = 7
- **PedidoPendenteAutorizacao** = 8
- **PedidoAprovado** = 9
- **PedidoNegado** = 10
- **PedidoGravadoFV** = 11 (job Winthor)
- **CancelamentoPedido** = 12
- **CarregamentoNaoImportado** = 13
- **ErroIntegracaoErp** = 14
- **CancelamentoPedidoERP** = 15
- **Objeto aguardando link maxPayment** = 16
- **Erro ao gerar link maxPayment** = 17
- **Objeto aguardando utilização do link** = 18
- **Falta colunas para maxPayment** = 19
- **Erro ao processar solicitação maxPayment** = 20
- **Em processamento maxPayment** = 21
- **Solicitação cancelada maxPayment** = 22
- **Validade do link incorreta** = 23

### Status de Posição do Pedido no ERP

**Descrição**: Códigos de posição (campo POSICAO) que refletem a situação do pedido no Winthor.

- **P** – Pendente
- **L** – Liberado
- **B** – Bloqueado
- **M** – Montado
- **F** – Faturado
- **C** – Cancelado
- **O** – Orçamento

Essas posições são armazenadas na MXSHISTORICOPEDC.

---

## Sincronização

### Forçar Sincronização do RCA

**Descrição**: Para forçar uma sincronização imediata sem depender do agendamento do cliente, pode-se alterar um registro na tabela de usuários, incrementando o campo ATUALIZID.

**Procedimento**:
1. Identificar o RCA na MXSUSUARIOS.
2. Executar um UPDATE em qualquer campo (ex: alterar um valor e reverter) para que o ATUALIZID seja atualizado.
3. Isso fará com que na próxima sincronização o sistema identifique mudanças e baixe os dados atualizados.

### Sincronização Automática

**Descrição**: A funcionalidade de sincronização automática permite que o aplicativo atualize dados em segundo plano sem intervenção do usuário.

**Parâmetro**: `HABILITA_SINC_AUTOMATICA` (Central de Configurações)

**Comportamento**: Quando habilitado, alterações na rotina 1203 (extrato de clientes) – como limite e bloqueio – disparam sincronização automática, exceto se o RCA estiver no meio de um pedido. Após finalizar o pedido, a sincronização ocorre.

**Versões relacionadas**:
- Sprint 29/01: sincronização automática de estoque
- Sprint 16/04: limite de cliente e desbloqueio
- Sprint 02/05: timeline de pedidos
- Sprint 05/09: preço

### Carga de Atualização Forçada (ATUALIZID)

**Descrição**: Para forçar que todos os dados de uma tabela sejam sincronizados novamente pelos aparelhos, pode-se atualizar em massa o campo ATUALIZID e DTATUALIZ nas tabelas nuvem.

**Exemplo para MXSCLIENT**:

```sql
DECLARE
BEGIN
    UPDATE MXSCLIENT
    SET ATUALIZID = TO_NUMBER(TO_CHAR(SYSDATE, 'RRRRMMDDHH24MISS')),
        DTATUALIZ = SYSDATE
    WHERE CODOPERACAO != 2;
    COMMIT;
END;
```

**Exemplo com filtro de data**:

```sql
DECLARE
BEGIN
    UPDATE MXSHISTORICOPEDC
    SET ATUALIZID = TO_NUMBER(TO_CHAR(SYSDATE, 'RRRRMMDDHH24MISS')),
        DTATUALIZ = SYSDATE
    WHERE CODOPERACAO != 2
      AND TRUNC(DATA) BETWEEN TO_DATE('09/07/2025', 'DD/MM/YYYY') AND TO_DATE('09/07/2025', 'DD/MM/YYYY');
    COMMIT;
END;
```

**Observação**: Recomendado para menos de 400 mil registros para evitar lentidão.

---

## Cadastro e Gestão de Usuários (RCA)

### Como Cadastrar um RCA no maxPedido

**Pre-requisitos**:
- Cliente deve ter licenças disponíveis.
- Usuário deve existir no ERP (Winthor) com perfil de vendedor.

**Passo a passo**:
1. Acessar o **Portal Gestão Nuvem** (central.solucoesmaxima.com.br).
2. Ir em **Cadastro de Usuários**.
3. Clicar em **Novo** e preencher os dados do RCA (nome, login, e-mail, etc).
4. Vincular o usuário ao **código do representante (CODUSUR)** do ERP.
5. Atribuir as permissões necessárias (acesso a produtos, clientes, etc).
6. Definir as configurações de versão e sincronização.
7. Salvar.

**Observação**: O cliente não tem permissão para criar usuários administradores; esse tipo de usuário só pode ser criado pelo suporte Máxima.

### Liberar Versão do Aplicativo (Gerenciar Versão)

**Descrição**: Controla qual versão do aplicativo (APK) está liberada para os usuários. É necessário manter o ambiente local (extrator) e nuvem atualizados para compatibilidade.

**Procedimento**:
1. Acessar **Gestão Nuvem > Cadastro > 303 - Versões**.
2. Clicar em **Novo**.
3. Selecionar o **cliente** e o **ambiente** (Produção/Homologação).
4. Preencher a **rotina**: 21 (para maxPedido).
5. Marcar os checkboxes de **Link de acesso** conforme o ambiente.
6. Obter o **Link de Download** em [versoes.maximatech.com.br](https://versoes.maximatech.com.br) (com VPN ativa).
7. Informar o **Package Name**: `br.com.maximasistemas.maxpedido` (para maxPedido).
8. Definir a **Versão** (ex: 3.243.5).
9. Salvar.

**Atenção**: A versão do ambiente local (extrator) deve ser compatível com a versão do aplicativo liberada. Sempre atualizar ambos.

### Inativar Usuário (RCA)

**Descrição**: Para desativar o acesso de um RCA, deve-se marcá-lo como inativo e inutilizável para liberar a licença.

**Passo a passo**:
1. No Gestão Nuvem, acessar o cadastro do usuário.
2. Marcar **Inativo** e **Inutilizável**.
3. Opcionalmente, executar os seguintes scripts no banco nuvem:

```sql
-- Verificar o usuário
SELECT * FROM MXSUSUARIOS WHERE CODUSUR = <codigo>;
SELECT * FROM MXSUSUARIOS WHERE NOME = '<nome>';

-- Inativar
UPDATE MXSUSUARIOS SET STATUS = 'I' WHERE CODUSUR = <codigo>;
UPDATE MXSUSUARIOS SET CODOPERACAO = 2 WHERE CODUSUR = <codigo>;
UPDATE MXSUSUARIOS SET CODUSUR = 0 WHERE CODUSUR = <codigo>;

-- Confirmar
SELECT * FROM MXSUSUARIOS WHERE CODUSUR = <codigo>;

COMMIT;
```

**Observação**: Se o usuário estiver apenas inativo, ainda consome licença. É necessário inutilizá-lo.

### Preposto (Representante Auxiliar)

**Descrição**: Um preposto é um usuário que não tem cadastro no ERP, mas está vinculado a um RCA. Todos os pedidos feitos pelo preposto são atribuídos ao RCA principal.

**Cadastro**:
1. Criar o usuário no Gestão Nuvem normalmente.
2. No cadastro do usuário, marcar a flag **"É preposto ou proponente"**.
3. No campo **"Representante do ERP"**, selecionar o RCA (vendedor) ao qual estará vinculado.
4. Atribuir as mesmas permissões do RCA principal.

**Erro comum**: "Erro de geração de dados preposto" ocorre quando o preposto não tem um representante do ERP vinculado.

---

## Configurações de Aplicativo (Parâmetros)

### Tipo de Dado do Parâmetro

**Descrição**: Na Central de Configurações, ao cadastrar um novo parâmetro, o tipo de dado é definido pela coluna TIPODADO na MXSPARAMETRO:

- **TIPODADO = 1** – Literal (texto)
- **TIPODADO = 2** – Inteiro (número)
- **TIPODADO = 3** – Lógico (S/N, booleano)

### Personalização do Espelho do Pedido

**Descrição**: Parâmetros que controlam a aparência e informações exibidas no PDF/Excel gerado ao compartilhar um pedido.

- **EXIBIR_PRECO_UNIT_EMB** – Exibe o preço unitário do pedido no layout.
- **APRESENTAR_DESCONTOS_PEDIDO_EMAIL** – Exibe campos de desconto (VL DESC, % DESC) no PDF.
- **OCULTAR_IMPOSTOS_PEDIDO_EMAIL** – Oculta impostos do pedido.
- **OCULTAR_VALIDADE_PROPOSTA** – Oculta datas de impressão e validade.
- **EXIBIR_FOTO_DO_PRODUTO_PDF** – Exibe fotos dos produtos ao lado dos itens.
- **EXIBIR_FOTO_DO_PRODUTO_PERSONALIZADO_PDF** – Exibe fotos em relatórios personalizados.
- **EXIBIR_CAMPO_CA_COMPART_PED_ORC** – Ativa campo de certificado de autorização.
- **LINK_LOGO_MARCA** – URL da logo a ser exibida no relatório.
- **DESABILITAR_ESPELHO_PED_PADRAO** – Desabilita o espelho padrão (usado quando há personalizado).

### Check-in e Check-out

**Parâmetros relacionados**:

- **UTILIZA_CHECKIN_CHECKOUT** – Habilita o uso de check-in/check-out. Trabalha em conjunto com GPS_IS_REQUIRED_CONFEC_PEDIDO.
- **PERMITIR_PEDIDO_SEM_CHECKIN** – Se 'N', não permite fazer pedido sem check-in no cliente.
- **OBRIGAR_ATENDIMENTO_PARA_CHECKOUT** – Obriga realizar um pedido ou justificativa de não venda antes do checkout.
- **OBRIGA_MOSTRAR_MOTIVO_NAO_VENDA** – Exibe mensagem se houver pedidos bloqueados para envio na sincronização.
- **OBRIGA_CHECKIN_CLIENTE_FORA_ROTA** – Se habilitado, solicita check-in para clientes fora da rota (caso contrário, não solicita).
- **GPS_TRACKING_ENABLED** – Ativa o rastreio GPS.
- **GPS_IS_REQUIRED_CONFEC_PEDIDO** – Exige GPS ligado para iniciar/salvar pedido.
- **ATIVAR_GPS_PEDIDO** – Ativa validação de localização no APP.

**Cerca eletrônica**:
- **GPS_EDGE_METERS_SIZE** – Tamanho da área (em metros) ao redor do cliente onde o pedido é permitido.
- **GPS_EDGE_BLOCK** – Habilita a validação da cerca eletrônica.

### Bloqueio por Rota Pendente

**Descrição**: Bloqueia novos pedidos se no dia anterior existirem clientes da rota sem justificativa.

**Parâmetros**:
- **BLOQ_RCA_COM_ROTA_PENDENTE** = 'S'
- **ROTEIRO_PENDENTE_ONTEM** = 'S'
- **DIAS_VERIFICACAO_ROTEIRO_PENDENTE** = 1 (ou mais dias)
- **JUSTIFICAR_ROTEIRO_ANTERIOR** = 'S'
- **BLK_SYNC_ROTEIRO_PENDENTE** = 'S'
- Permissão: **"Permitir justificativas de clientes fora da rota"**

### Obrigar/Desobrigar Previsão de Faturamento

**Parâmetros**:
- **OBRIGAR_PREVISAO_FATURAMENTO** = 'N' (desabilita obrigatoriedade)
- **PREVISAO_FATURAMENTO_DIA_MAIS_UM** = 'S' (grava previsão como amanhã)
- **CONSIDERAR_DATA_ATUAL_PREV_FAT** – Se 'S', conta a data de previsão a partir da edição do pedido; se 'N', a partir da criação.
- **PRAZO_VALIDADE_PREVISAOFATURAMENTO** – Número máximo de dias para previsão.

### Validade para Enviar Pedido Salvo e Bloqueado

**Parâmetro**: `PRAZO_VALIDADE_PEDIDO` (MXSPARAMETRO, tipo número). Define o prazo (em dias) para que um pedido salvo e bloqueado no aparelho possa ser enviado ao Winthor.

### Margem de Lucratividade

**Descrição**: Validações de margem mínima podem ocorrer em três níveis:

1. **Por pedido** – Parâmetro 1370 do Winthor (% de margem mínima). Mensagem: "Pedido com % de lucratividade menor que o definido pela presidência".
2. **Por plano de pagamento** – Campo `MARGEMMIN` na MXSPLPAG.
3. **Por item (produto/filial)** – Campo `PERCMARGEMMIN` na MXSPRODFILIAL.

**Parâmetro do Winthor**: `CON_MARGEMMIN` (rotina 132) exibe mensagem: "A lucratividade do pedido (...) está abaixo da lucratividade mínima (...) definida no ERP".

**Permissão**: "Habilitar visualização de margem/lucratividade" na Central de Configurações.

### Plano de Pagamento e Bonificação

**Descrição**: Para utilizar bonificação (TV5), é necessário que o plano de pagamento tenha `TIPOPRAZO = 'B'` e a cobrança seja uma das: BNF, BNFR, BNTR, BNFT, BNRP, BNFM.

**Parâmetros**:
- **OBRIGATORIOVINCULARTV5COMTV1** / **MXS_OBRIGATORIOVINCULARTV5COMTV1** – Obriga vínculo do pedido bonificado com um pedido normal (TV1).
- **PEDIR_AUTORIZACAO_TV5_VINCULADO_TV1** – Envia para aprovação no maxGestão.
- **QTDE_DIAS_VINCULO_TV1_COM_TV5** – Dias máximos para vincular TV1 a TV5.
- **PERC_LIMITE_TV5_RCA** – Percentual limite da bonificação em relação ao TV1.

### Chave Tripla / Bonificação para o Mesmo Item no Mesmo Pedido

**Regra**: Permite inserir um item no pedido TV1 e depois o mesmo item como bonificado no mesmo pedido.

**Configuração**:
1. Verificar `CONDVENDA5` na MXSCLIENT (deve estar 'S').
2. Verificar vínculo do cliente com plano de pagamento de bonificação na MXSPLPAGCLI.
3. Verificar vínculo com cobrança de bonificação na MXSCOBCLI.
4. Verificar `TIPOPRAZO` do plano (deve ser 'B').

---

## Processamento de Pedidos e Integração

### Fluxo de Processamento de Pedidos

**Descrição**: Etapas desde o envio pela APK até o retorno do ERP.

1. **APK** envia pedido → **Nuvem Máxima**.
2. Server grava na `MXSINTEGRACAOPEDIDO` com status = 0.
3. **ERP** faz um GET no endpoint `/api/v1/StatusPedidos` para buscar pedidos pendentes (status 0,1,2,3,5,11).
4. Ao retornar o GET, a API seta status = 2 (ENVIADO PARA O ERP).
5. **ERP** processa internamente.
6. **ERP** faz um PUT no mesmo endpoint para enviar crítica e informa status 4 (sucesso) ou 5 (erro).
7. **ERP** envia histórico do pedido com posição (L, F, etc.).
8. **APK** faz "swipe" para atualizar timeline (baseado no histórico + status da MXSINTEGRACAOPEDIDO).

### Crítica da Integradora do Winthor

**Cenário**: Restrição de venda (ex: valor mínimo para plano de pagamento) barrando itens.

**Diagnóstico**: Verificar na `PCPEDIFV` o campo `OBSERVACAO_PC`. Se preenchido, significa que passou pela integradora e foi barrado.

### Pedido Já Existe (Crítica de Duplicidade)

**Cenário**: Integradora retorna crítica de pedido já existente. Ocorre quando o número de pedido gerado pelo força de vendas já está vinculado a um pedido no ERP.

**Solução**:
1. Verificar na Central de Configurações (ou MXSUSUARI) o próximo número de pedido.
2. Comparar com o numerador da rotina 517 do Winthor.
3. Ajustar o numerador no Winthor (rotina 517) para o próximo número correto.
4. O pedido barrado deve ser duplicado no maxPedido.

### Timeline de Pedidos Não Atualiza

**Causa**: A `MXSHISTORICOPEDC` tem prioridade na timeline, mas só é considerada se todos os campos obrigatórios estiverem preenchidos. Frequentemente falta o campo `DTABERTURAPEDPALM`.

**Alternativa**: Se necessário, pode-se reenviar a crítica via endpoint:

```
POST /api/v1/StatusPedidos/AtualizarPedidos
```

### Pedido com Status Diferente na Timeline

**Descrição**: Exemplo: pedido faturado (F) mas timeline mostra liberado (L). A hierarquia de informações é:
1. `MXSHISTORICOPEDC` (posição)
2. `MXSINTEGRACAOPEDIDO` (crítica)

Se a MXSHISTORICOPEDC não estiver completa, prevalece a MXSINTEGRACAOPEDIDO.

---

## Configurações Específicas

### Tributação

**Erro**: "Não foi possível carregar a tributação para esse produto".

**Verificações**:
- Cliente possui filial NF?
- Processo na 316 está operacional?
- Existe tributação para o produto na filial? Consultar:
  - `MXSTABTRIB` – verificar CODST
  - `MXSTABPR` – campo CODST deve estar preenchido com código existente em `MXSTRIBUT`
  - `MXSTRIBUT` – validar CODOPERACAO

### Simples Nacional e Contribuinte

**Parâmetros**:
- `CLIENTECONTRIBUINTE_SIM` – Define valor padrão para "Contribuinte" no cadastro de clientes.
- `CLIENTESIMPLESNACIONAL_SIM` – Define valor padrão para "Simples Nacional".

### Código IBGE

**Descrição**: Obrigatório para clientes Winthor. Se faltar, pode impedir cadastro ou gerar críticas.

**Verificações**:
- Verificar na `MXSCIDADE` se o código IBGE existe.
- Parâmetro `ENVIAR_TODAS_CIDADES_IBGE = 'S'` para forçar envio de todas as cidades.

**Onde configurar**: Em **Configurações > Formulários** é possível definir obrigatoriedade do campo.

### Filial Retira

**Descrição**: Permite que o pedido seja feito em uma filial, mas a retirada do estoque seja em outra filial.

**Parâmetros**:
- `DEFINE_FILIAL_RETIRA_PADRAO` (número) – filial retira padrão.
- `UTILIZAFILIALRETIRAFILIALESTOQUE` – obrigatório para usar filial retira.
- `LISTAR_PROD_EST_RETIRA` – lista produtos da filial retira definida para o cliente.
- `TOTALIZA_ESTOQUE_LISTAGEM_PRODUTO`, `VALIDAR_FILIALRETIRADIFERENTE`, `USA_DESMEMBRAMENTO_PEDIDO` – opcionais.

**Configuração**:
1. Definir no Winthor as filiais retira (rotina apropriada).
2. Na Central de Configurações, garantir que o RCA tenha permissão de acesso à filial retira (tanto para venda quanto para estoque).
3. Se a filial for nova, pode ser necessário carga de dados.

### Tabela de Preço

**Como utilizar tabelas de preço diferentes para o mesmo RCA**:

- **Requisitos**: Cliente deve estar cadastrado na `MXSTABPRCLI` (rotina 3314) com filial NF e região desejada.
- **Parâmetros**:
  - `PERMITE_FILIAL_NF_NULA = 'S'`
  - `COMPORTAMENTO_WHINTOR_FILIAL = 'S'`
  - `IGUALAR_FILIALNF_AO_ALTERAR_FILIAL = 'N'`
- **Fluxo**:
  - Para usar a tabela da região da `PCTABPRCLI`, selecionar a filial NF correspondente no pedido.
  - Para usar a tabela da região do cadastro do cliente (PCTABPR), deixar filial NF nula.

### Preço na Listagem vs. Tela de Negociação

**Cenário**: Valor do produto aparece diferente na aba "Tabela" e na tela de negociação.

**Possíveis causas**:
- Campo `CALCULAST` na MXSCLIENT: se 'S', calcula ST e aplica na negociação; se 'N', pode divergir.
- Campo `PERACRESCISMOPF` na MXSTRIBUT: se preenchido e parâmetro `VALIDAR_ACRESCIMO_PF_LISTAGEM` não habilitado, o preço da listagem pode incluir acréscimo enquanto a negociação não.

### Bloquear Pedido para Cliente Inadimplente

**Parâmetros**:
- `BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE` (MXSPARAMETRO)
- Se = 'N', busca o número de dias máximo para inadimplência em:
  - `NUMERO_DIAS_CLIENTE_INADIMPLENTE` (MXSPARAMETRO)
  - `CON_NUMDIASMAXVENDACLIINADIMPLENTE` (MXSPARAMFILIAL) – o maior entre os dois é considerado.
- Se = 'S' e os dias máximos forem 0, bloqueia independentemente do tempo.

### Não Permitir Vender sem Estoque

**Parâmetros**:
- `BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE`
- `BLOQUEAR_VENDA_ACIMA_DO_ESTOQUE`
- `BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE_CAMPANHA`
- `VALIDA_RESTRICAO_ESTOQUE`
- `OCULTAR_PROD_FL_SEM_ESTOQUE`

### Quantidade Múltipla (Embalagem)

**Descrição**: Obrigar que a quantidade inserida seja múltipla do valor definido para o produto.

**Configuração**:
1. Desabilitar parâmetro `USAR_MULTIPLO_QTDE`.
2. Na MXSCLIENT, campo `VALIDARMULTIPLOVENDA = 'S'`.
3. Na MXSPRODFILIAL, campo `MULTIPLO` preenchido com o número da quantidade múltipla. (Se não funcionar, usar MXSPRODUT.MULTIPLO).

**Observação**: Se `VALIDARMULTIPLOVENDA = 'N'`, o produto inicia com a quantidade múltipla, mas não obriga; se a unidade for 'UN', pode iniciar com 1.

---

## Resumo de Vendas (Dashboard)

### Resumo de Vendas Não Atualiza

**Possíveis causas**:
1. Bloqueio da porta 9002 (Hangfire) no firewall.
2. Ambiente muito desatualizado (necessário atualizar extrator e nuvem).
3. Bloqueio de geolocalização aos EUA (nossa nuvem AWS tem IPs nos EUA). Liberar os IPs: 3.81.180.245, 34.236.34.79, 3.81.180.2, 18.215.65.25.

### Habilitar Aba de Metas por Fornecedores

**Parâmetro**: `META_FOR = S`

### Mostrar Valor Faturado + Liberado + Montado no Campo "Alcançado"

**Parâmetro**: `CRITERIOVENDA = 'P'` (valor 'P' significa considerar posições F, L, M). Também há `CRITERIO_VENDA_CARD_PEDIDO` e `CRITERIO_VENDA_GRAFICO` com opções 'L' (líquido), 'F' (faturado), 'T' (transmitido).

### Configurar Linhas das Tabelas de Meta

Cada aba do resumo de vendas pode ter linhas controladas por parâmetros com prefixo da aba:

- `META_PROD` – Habilita aba PRODUTO
- `META_PROD_CLIPOS` – Linha de positivação de clientes
- `META_PROD_MIX` – Linha de MIX
- `META_PROD_QTPESO` – Linha de Peso
- `META_PROD_QTVENDA` – Linha de Quant. Vendida
- `META_PROD_VLVENDA` – Linha de Venda

O mesmo padrão se aplica a outras abas: META_CAT, META_DEP, META_FOR, etc.

### Tendência de Vendas (V4)

**Descrição**: Aparece apenas quando o filtro de data é o mês atual. Cálculo: (faturado / dias úteis passados) * (total dias úteis - dias úteis passados) + faturado.

**Desabilitar**: Parâmetro `RV_TENDENCIA_VENDA = 'N'`.

### IA de Recomendação de Produtos

**Parâmetro**: `HABILITA_RECOMENDACAO_PRODUTOS`

**Requisitos**:
- Versão mínima: 3.219.4
- Aguardar 48 horas para geração dos dados (análise de vendas).
- Pelo menos 2 produtos no pedido para que a recomendação apareça.
- Ao salvar/enviar o pedido, a tela de recomendação da IA é exibida.

**Tabela**: `MXSRECOMENDACAO` armazena pares de produtos vendidos juntos.

---

## Títulos e Boletos

### Segunda Via de Boleto no maxPedido

**Requisitos**:
- Versão do app >= 2.223.9.
- Ambiente nuvem atualizado.
- Parâmetro `EXIBE_LINHA_DIGITAVEL = 'S'` (se 'N', a opção não aparece).
- Parâmetro `HABILITAR_GERADOR_RELATORIOS` (para editar layout do boleto na Central).

**Passos no app**:
1. Acessar **Consultas > Títulos**.
2. Clicar e segurar sobre o título desejado.
3. Confirmar "Gostaria de compartilhar o boleto?".

**Erro "Não foi possível gerar o relatório!"**:
- Verificar se as colunas `NOSSONUMBCO` e `LINHADIG` estão preenchidas na `ERP_MXSPREST` e `MXSTITULOSABERTOS`.

### Compartilhar DANFE (Nota Fiscal)

**Requisitos**:
- Banco atualizado.
- Dados na `ERP_MXSDOCELETRONICO` (endpoint Doceletronico para OERPs).
- Pedido com posição "Faturado" (caso contrário, opção desabilitada).
- Coluna `NUMTRANSVENDA` na `MXSHISTORICOPEDC` deve estar preenchida.

**Problema comum**: "Não foi possível gerar o XLS" – verificar permissão do app "Acesso a todos os arquivos".

---

## Validade de Produtos / WMS

### Validade WMS

**Parâmetros**:
- `EXIBE_VALIDADE_PRODUTO_WMS` – Habilita exibição da validade.
- `EXIBIR_VALIDADE_WMS_VENCIDA` – Exibe produtos vencidos.

**Tabelas envolvidas**:
- `MXSVALIDADEWMS` (nuvem) – contém as informações de validade.
- No Winthor: `PCESTENDECOI`, `PCESTENDERECO`, `PCVIEWVALIDADEWMS` (view que alimenta a MXSVALIDADEWMS).

**Como funciona**: Uma view no banco local do cliente (PCVIEWVALIDADEWMS) consulta as tabelas de estoque e envia os dados para a nuvem.

### Validade/Vencimento (sem WMS)

- **Tela de Informações Adicionais**: validade vem da coluna `DTVENC` da `MXSPRODUT`.
- **Tela de Listar Lotes**: depende do parâmetro `LISTAR_INFO_LOTES` habilitado e da tabela `MXSLOTE`.

---

## Procedimentos de Suporte e Manutenção

### Retirar Restrições do maxPedido em Base do Zero

**Script para SQLite (Inspect)** – Remove restrições de horário, jornada, check-in/out, etc:

```sql
DELETE FROM MXSCONFIGDATA WHERE NOME IN ('BLK_CONN_PRIMEIRACONEXAO', 'BLK_CONN_INTERVALOCONEXAO', 'BLK_CONN_PRIMEIRACONEXAO_TZ', 'BLK_CONN_QTDEPEDPENDENTE', 'BLK_CONN_QTDEORCPENDENTE', 'FORCAR_JORNADA', 'VALIDA_FUSO_DATAAUTOMATICO', 'BLOQUEIA PED_FORA_JORNADA', 'UTILIZA_CHECKOUT', 'VALIDA_FUSO_DATA_AUTOMATICO', 'GPS_EDGE_BLOCK', 'GPS_EDGE_METERS_SIZE');
DELETE FROM MXSPARAMETRO WHERE NOME IN ('BLK_CONN_PRIMEIRACONEXAO', 'BLK_CONN_INTERVALOCONEXAO', 'BLK_CONN_PRIMEIRACONEXAO_TZ', 'BLK_CONN_QTDEPEDPENDENTE', 'BLK_CONN_QTDEORCPENDENTE', 'FORCAR_JORNADA', 'VALIDA_FUSO_DATAAUTOMATICO', 'BLOQUEIA PED_FORA_JORNADA', 'UTILIZA_CHECKIN_CHECKOUT', 'VALIDA_FUSO_DATA_AUTOMATICO', 'GPS_EDGE_BLOCK', 'GPS_EDGE_METERS_SIZE', 'BLOQ_VENDA_FORA_HORARIO_COM', 'HABILITA_SYNC_AUTOMATICA');
```

### Erro "Buscar Dados Usuário"

**Causa**: Cadastro do RCA na Central de Configurações não vinculado a um perfil no ERP.

**Solução**: Verificar vínculo e deslogar/relogar do maxSoluções.

### Senhas do Suporte

- Banco nuvem: `mxma#maxpedidonuvem`
- Banco local Winthor: `mxMa#soluc1727`
- Banco OTI: `M@xima#EfSILDF`
- Banco consulta (quando der erro de login): usuário `CONSULTA`, senha `Con$ult@#0981`
- Banco local MAXSOLUCOES: `mxMa#soluc1727`
- Portainer: `maxsolucoes@portainer` (alternativa: `Maxsolucoes@portainer`)
- Hangfire: `maxsolucoes@extrator` (para T-Cloud, senha é gerada no Jenkins)

### Erro Trigger no Banco Local

**Procedimento**:
1. Atualizar extrator para última versão.
2. Rodar o Atualizador.
3. Executar as jobs no Hangfire:
   - Página 1: ProcessamentosWebApi.ObterScripts
   - Página 2: Atualização de Banco de Dados
4. Se persistir, ativar parâmetro `PRIMEIRA_IMPLANTACAO = 'S'` na MXSPARAMETRO (força reenvio de triggers). Após normalizar, retornar para 'N'.

### Objetos Inválidos no Banco Local

**Script para verificar objetos inválidos**:

```sql
SELECT OWNER, OBJECT_TYPE, OBJECT_NAME, STATUS
FROM ALL_OBJECTS
WHERE STATUS = 'INVALID'
ORDER BY OWNER, OBJECT_TYPE, OBJECT_NAME;
```

**Para recompilar**: Gerar comandos `ALTER ... COMPILE;`.

### Consulta de Locks no Banco

```sql
SELECT
    OBJ.OBJECT_NAME,
    LOC.SESSION_ID,
    LOC.ORACLE_USERNAME,
    LOC.LOCKED_MODE,
    SES.SID,
    SES.SERIAL#,
    SQL.SQL_TEXT,
    SES.MACHINE,
    SES.OSUSER
FROM V$LOCKED_OBJECT LOC
JOIN DBA_OBJECTS OBJ ON LOC.OBJECT_ID = OBJ.OBJECT_ID
JOIN V$SESSION SES ON LOC.SESSION_ID = SES.SID
LEFT JOIN V$SQL SQL ON SES.SQL_ADDRESS = SQL.ADDRESS;
```

### Como Analisar o Extrator no Linux

**Comandos úteis**:
- Verificar se Docker está instalado: `docker ps -a`
- Atualizar ambiente: `sudo apt update && sudo apt upgrade`
- Testar conectividade com URLs da Máxima:
  ```
  telnet intext-hmg.solucoesmaxima.com.br 81
  telnet intpdv-hmg.solucoesmaxima.com.br 81
  telnet appsy.solucoesmaxima.com.br 8081
  ```

**Erro de bloqueio**: Se houver bloqueio, cliente deve liberar as portas no firewall.

### Atualização de Ambiente do Cliente

1. Acessar **Portal Gerir > Monitoramento (4003)**.
2. Buscar pelo extrator do cliente.
3. Atualizar o **Portainer** com a última versão disponível (ver no Discord #maxpedido).
4. Rodar o **Atualizador** (jobs no Hangfire).
5. Opcional: atualizar versão do maxPedido liberada.

### Cliente T-Cloud (Jenkins)

- Acessar Jenkins > EXTRATOR-EKS.
- Pipeline "Build with Parameters" com código e nome do cliente.
- Senhas temporárias são obtidas no arquivo INFORMAÇÕES.txt.

---

## Endpoints de Integração

### Endpoint: /api/v1/StatusPedidos — MXSINTEGRACAOPEDIDO

**Método**: GET / PUT

**Direção**: ERP → Máxima (GET para buscar pedidos) / Máxima → ERP (PUT para retornar críticas)

**Descrição**: Responsável pela troca de status e críticas entre o ERP e a nuvem Máxima.

**Campos obrigatórios no PUT**:
- `idPedido`: identificador do pedido na MXSINTEGRACAOPEDIDO
- `status`: código do status (4 = sucesso, 5 = erro, etc.)
- `critica`: texto da crítica (em caso de erro)
- `posicao`: posição do pedido no ERP (L, F, etc.)

**Erros comuns**:
- **Erro 500**: Verificar se o JSON enviado está no formato esperado.
- **Timeout**: Verificar conectividade e tamanho do payload.

### Endpoint: Clientes — MXSCLIENT

**Método**: POST / PUT

**Direção**: ERP → Máxima

**Descrição**: Envia dados cadastrais de clientes do ERP para a nuvem.

**Campos principais**:
- `codcli`: código do cliente
- `nome`: nome/razão social
- `codusur1`, `codusur2`, `codusur3`: RCA's vinculados
- `limcred`: limite de crédito
- `dtultcomp`: data da última compra

**Validações**:
- `codcli` único
- `codusur` deve existir na MXSUSUARIOS

### Endpoint: ClientesEnderecos — MXSCLIENTENDENT

**Método**: POST / PUT

**Direção**: ERP → Máxima

**Descrição**: Envia endereços de entrega adicionais para clientes.

**Relacionamentos**: FK para MXSCLIENT via `codcli`.

**Obrigatório**: Não, mas necessário para funcionalidade de endereço alternativo.

---

## Ferramentas Auxiliares

### maxViewer

**Descrição**: Ferramenta de suporte para acesso remoto à tela do cliente.

**Links de download**:
- Cliente Windows: [maxviewer_clientes.exe](https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer_clientes.exe)
- APK Android: [maxviewer.apk](https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer.apk)
- EXE Windows (stand-alone): [maxviewer.exe](https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer.exe)
- Debian/Ubuntu: [maxviewer-linux-installer-v1-x86_64.deb](https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer-linux-installer-v1-x86_64.deb)
- Acesso web: [http://maxviewer.maximatech.com.br:21114/](http://maxviewer.maximatech.com.br:21114/)

### Carga Total (para inclusão de nova filial)

**Quando usar**: Quando uma nova filial é criada no ERP e precisa ser carregada no ambiente nuvem.

**Passo a passo**:
1. Acessar [Carga Total](http://cargatotal.solucoesmaxima.com.br/) (HTTP, não HTTPS).
2. Selecionar o cliente.
3. Na aba **Filiais**, marcar a nova filial.
4. Na aba **Grupo de Tabelas**, selecionar:
   - Condições Comerciais
   - Logística/Gestão
   - Campanhas
   - Estoque
   - Preço
   - Tributação
5. Na aba **Períodos**, definir 3 meses retroativos.
6. Executar a carga.

**Acompanhamento**:

```sql
SELECT tabela, COUNT(1)
FROM maxsolucoes.pcmxsintegracao
WHERE status = '-1'
GROUP BY tabela
ORDER BY COUNT(1) DESC;
```

**Possível erro**: "Extrator inacessível" – verificar liberação de IPs e portas (incluindo geolocalização dos EUA).

---

## Procedimentos Específicos

### Como Configurar API de Cancelamento (WTA)

**Parâmetro**: `UTILIZA_API_CANCEL_WINTHOR = 'S'` na Central de Configurações.

**Configuração no extrator** (Portainer/compose):
- `LINK_API_WINTHOR_CANCELAMENTO`: http://IP:porta
- `USUARIO_API_WINTHOR_CANCELAMENTO`: geralmente pcadmin / implantacao
- `SENHA_API_WINTHOR_CANCELAMENTO`: criptografada (em maiúsculo)

**Verificar no banco nuvem**:
```sql
SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%MOBILE%';
```

### Criação de Ponto de Montagem para Fotos de Produtos

**Descrição**: Montar diretório de imagens do Winthor no servidor Linux onde roda o extrator.

**Exemplo de script mount.sh**:

```bash
#!/bin/bash
proc=$(mount -l | grep //192.168.10.104/wntadm/IMG | wc -l)
if [ $proc -le 0 ]
then
    mount -t cifs //192.168.10.104/wntadm/IMG /app/maxima/MXS_Extrator/imagens_data_cliente -o username=forca.vendas,password=@51201,vers=1.0
fi
```

**Passos**:
1. Instalar `cifs-utils`: `sudo apt install cifs-utils -y`
2. Criar o script em `/mount.sh`
3. Dar permissão: `chmod +x /mount.sh`
4. Adicionar no crontab: `*/1 * * * * root $SHELL /mount.sh`
5. Executar: `sh /mount.sh`
6. Verificar com `df -h`

**No Portainer**: Adicionar volume mapeando o diretório montado para `/mnt/maxima/produtos_fotos` no container do extrator.

### Consultar Quais Tabelas Possuem um Campo

**Útil para descobrir onde está um determinado campo**.

```sql
SELECT * FROM ALL_TAB_COLUMNS WHERE COLUMN_NAME = 'PERDESCMAX';
```

---

## Anexos e Links Úteis

- **Biblioteca de conhecimento Máxima**: [basedeconhecimento.maximatech.com.br](https://basedeconhecimento.maximatech.com.br)
- **Requisitos mínimos do maxPedido**: [maximatech.com.br/requisitos](https://maximatech.com.br/requisitos)
- **Layout de integração Winthor**: [TDN TOTVS](https://tdn.totvs.com)
- **Layout de integração maxPedido**: [Base de Conhecimento](https://basedeconhecimento.maximatech.com.br/pages/viewpage.action?pageld=12189810)
- **Treinamento maxPedido V4**: [Link do treinamento](https://drive.google.com/file/d/1ARa7bcumYQSQvv91xogHFEABE1m8qVf/view?ts=670025f8)
- **Relatório 800**: [Biblioteca](https://biblioteca.maximatech.com.br/pages/viewpage.action?pageId=28311751)

---

## Glossário

- **RCA**: Representante Comercial Autônomo
- **ERP**: Enterprise Resource Planning (Sistema de Gestão)
- **Winthor**: ERP da TOTVS, comumente integrado ao maxPedido
- **FV**: Força de Vendas
- **ST**: Substituição Tributária
- **WTA**: Winthor Anywhere
- **API**: Application Programming Interface
- **JSON**: JavaScript Object Notation
- **SQL**: Structured Query Language
- **NF**: Nota Fiscal
- **DANFE**: Documento Auxiliar da Nota Fiscal Eletrônica
- **PDV**: Ponto de Venda
- **CC**: Conta Corrente

---

## Roteirizador de Vendedores (maxGestão Plus)

### Quantidade de Clientes na Carteira do RCA Divergente do Winthor

**Descrição**: A quantidade de clientes exibida no Roteirizador pode ser menor que a constante na rotina 313 do Winthor.

**Possíveis causas**:
- Divergência entre `PCCLIENT` e `MXSCLIENT`.
- Divergência entre `PCUSURCLI` e `ERP_MXSUSURCLI`.
- Problemas na view `MXSVCLIENTESRCA`.
- Se houver registros na `MXMP_CARTEIRIZACAO`, significa que a carteirização foi feita dentro do Roteirizador e não subiu para o ERP.

**Resolução**:
- Se divergência de tabelas do ERP com a nuvem, solicitar carga de dados via Gatekeeper.
- Se a carteirização foi feita no Roteirizador, os dados não sobem automaticamente para o ERP; é necessário ajuste manual ou integração.

### Visitados e Agendados Aparecem Zerados no Painel de Auditoria

**Problema**: RCA ou supervisor têm visitas agendadas no roteiro, mas o Painel de Auditoria mostra zero na coluna de Agendados.

**Resolução**:
- Verificar se o roteiro foi cadastrado no Winthor (rotina 354) ou no Roteirizador de Vendedores. Se cadastrado no Winthor, a configuração pode estar mostrando informações do Roteirizador. Desmarcar a configuração que mistura as fontes.

### Script para Verificar Clientes por RCA

**Quando usar**: Para conferir a quantidade de clientes vinculados a um RCA.

```sql
SELECT COUNT(DISTINCT CODCLI) AS TOTAL
FROM (
    SELECT CODCLI
    FROM MXSCLIENT C
    WHERE EXISTS (
        SELECT 1
        FROM MXSUSUARI U
        WHERE U.CODUSUR = 1061 -- substituir pelo código do RCA
          AND U.CODUSUR IN (C.CODUSUR1, C.CODUSUR2, C.CODUSUR3)
          AND C.CODOPERACAO != 2
          AND C.DTEXCLUSAO IS NULL
    )
    UNION ALL
    SELECT CODCLI
    FROM ERP_MXSUSURCLI UC
    WHERE UC.CODUSUR = 1061 -- substituir
      AND UC.CODOPERACAO != 2
      AND UC.CODCLI IN (SELECT CODCLI FROM MXSCLIENT WHERE CODOPERACAO != 2)
) SUBQUERY;
```

---

## MAX-PROMOTOR

### Visão Geral do MAX-PROMOTOR

**Descrição**: O maxPromotor é uma solução voltada para Trade Marketing, composta por um aplicativo mobile e um portal web. Ele atende fabricantes, distribuidores e varejistas, permitindo o planejamento e acompanhamento de ações em ponto de venda (PDV).

**Principais funcionalidades**:
- **Agenda**: Tarefas planejadas para o promotor no dia.
- **Acompanhamento**: Monitoramento das atividades.
- **Tempo Produtivo**: Mede o tempo que o promotor permanece no PDV (entre check-in e check-out).
- **Treinamentos e Incentivos**: Arquivos PDF/TXT com instruções.
- **Legendas**: Dicionário de status das pesquisas e PDVs.
- **Cadastro e Edição de Clientes**: Permite cadastrar novos clientes e editar dados, com permissões controladas.
- **Mapa**: Visualização da localização do promotor e dos clientes do roteiro.
- **Roteiro**: Clientes a serem visitados no dia, com possibilidade de justificativas.
- **Pesquisas**: Questionários aplicados nos PDVs.
- **Mix**: Informações sobre mix de produtos.
- **Pedidos**: Se integrado com maxPedido, histórico de pedidos do cliente aparece na aba "pedidos".

### Padrão para Abertura de Ticket N3 no MAX-PROMOTOR

**Informações obrigatórias**:
- Versão da APK do Promotor (menu lateral do app).
- Versões Web e Sync (obter no Jenkins: MAXPROMOTOR-EKS_PRODUCAO-listarClientesVersoes).
- Backup da base do Promotor (ver tutorial específico).
- Link do Portal Web (ex: `cliente.maxpromotor.com.br`).
- Acesso WEB (login/senha) e acesso APK (se aplicável).
- Se for problema de integração, adicionar informações sobre o fluxo.
- Prints, vídeos e descrição detalhada do cenário.

**Exemplos de tickets**:
- Melhoria: MXPRODV-9061
- Erro APK: MXPRODV-8905
- Erro WEB: MXPRODV-8729

### Acesso ao Promotor com Login da Máxima

**Credenciais de teste**:
- Usuário: `maxpromotor`
- Senha: `promotor123`

**Acesso ao portal**:
- `[nome_cliente].maxpromotor.com.br/web/login.xhtml`
- Swagger da API de sincronização: `[nome_cliente].maxpromotor.com.br/sincronizacao/promosinc/swagger-ui.html`

### Como Obter a Base de Dados do Promotor

**Passo a passo**:
1. No portal do Promotor, acessar o cadastro do promotor e obter o **ID real** (número que aparece na URL da página de perfil).
2. Acessar o Swagger da API: `[cliente].maxpromotor.com.br/sincronizacao/promosinc/swagger-ui.html`.
3. Navegar até o endpoint de **backup** e clicar em "Try it out".
4. Inserir o ID do promotor e executar.
5. O arquivo de backup será gerado e estará disponível no **S3 Browser**.
   - Procurar pela pasta do cliente (nome ou ID).
   - O arquivo estará em `/backups` com a data atual.

**Alternativa**: Obter a versão da APK, Android e modelo do promotor pelo relatório "Informações do aparelho" no portal.

### Perfil: Usuários Vinculados e Informações Desaparecendo

**Problema**: Quando o usuário vincula RCA's ao supervisor pelo portal do Promotor, mas a integração automática está ligada, os dados podem ser sobrescritos pelos dados do Winthor na próxima job.

**Solução**: O cadastro de vínculos deve ser feito diretamente no Winthor para não ser sobrescrito.

### Erro de Sincronização no Promotor (On-Premise)

**Para clientes On-Premise** (servidor Windows dentro da infraestrutura do cliente, geralmente porta 8186):

1. Solicitar acesso ao servidor onde o serviço do Promotor está instalado.
2. Acessar via navegador: `http://localhost:8186/maxpromotor`. Se abrir, o serviço está ativo, mas o IP pode ter mudado.
3. Se não abrir, verificar no Gerenciador de Tarefas se o serviço está rodando. Se estiver, reiniciá-lo. Caso contrário, iniciar o serviço.
4. Se o IP mudou, atualizar o link de acesso na configuração do aplicativo.

**Para clientes EKS (nuvem)**:
1. Pedir ao promotor para deslogar e acessar a engrenagem no canto superior direito da tela de login.
2. Na seção "Dados da Conexão", clicar em "Configurar" e verificar se o link está no formato `nome-do-cliente.maxpromotor.com.br` (sem HTTP).
3. Se o problema persistir, reiniciar o serviço SYNC pela pipeline apropriada.

### De Onde Vêm os Dados de Data de Entrega e Emissão?

- **Data de entrega**: campo `DTENTREGA` na `PCPEDC`.
- **Data de emissão**: campo `DTSAIDA` na `PCNFSAID`.

### Análise de Pesquisa Não Aparece

**Verificações**:
1. Cabeçalho da pesquisa: ativa, dentro do período de validade.
2. Filtros da pesquisa: verificar se há restrições de cliente, região, etc.
3. Se a opção "Mix Cliente" estiver marcada, o item da pesquisa deve estar no mix do cliente; caso contrário, a pesquisa não será exibida.

### Dados Retroativos (Versões .008 e .013)

**Descrição**: Versões específicas que corrigem problemas com dados retroativos no Promotor.
- Versão .008: [link]
- Versão .013: [link]

---

## MAX-PAG

### Como Ativar o Sistema de Anti-Fraude no MAX-PAG

**Descrição**: O maxPag possui um módulo de anti-fraude que pode ser ativado para transações com cartão de crédito.

**Procedimento**:
1. Acessar a Central de Configurações.
2. Navegar até **Configurações > maxPag**.
3. Habilitar o parâmetro `ANTI_FRAUDE_ATIVO = 'S'`.
4. Configurar as regras de fraude (limites, bloqueios, etc.) conforme necessidade.
5. Salvar e sincronizar.

### Como Cadastrar Cobrança para o MAX-PAG

**Para cobrança PIX**:
A APK do maxPedido considera que uma cobrança é do tipo PIX para o maxPag se pelo menos uma das condições for verdadeira:
- `MXSCOB.TIPOCOBRANCA = 'PIX'` (observação: campo pode ter tamanho 2, então pode não ser válido)
- `MXSCOB.CODMOEDA = 'PIX'`
- `MXSCOB.CODCOB = 'PIX'`

**Para cobrança Cartão**:
- Parâmetro `PERMITIR_VENDA_CARTAO_CREDITO` deve estar habilitado.
- A APK considera cartão se `MXSCOB.TIPOCOBRANCA = 'C'`.

### Provedores Integrados com o MAX-PAG

**Lista de provedores**: (consultar documentação oficial para lista atualizada, inclui adquirentes como Cielo, Rede, Stone, etc.)

### GRAVAR_NSUTEF_PCPREST

**Descrição**: Parâmetro que, quando ativado, faz com que o número do comprovante (NSU/TEF) seja gravado na tabela `PCPREST` para rastreabilidade.

**Valor**: `GRAVAR_NSUTEF_PCPREST = sim`

### Máquina REPOSIT com Vários Clientes

**Observação**: Em ambientes REPOSIT (servidores compartilhados), vários clientes podem estar rodando no mesmo servidor. Para identificar o Portainer de um cliente específico, consultar a lista de IPs e portas fornecida pela infraestrutura.

**Exemplo**:
- PORTAINER 187.108.193.15:49570 (clientes: ASA, CEMA, CENTAURO, etc.)
- PORTAINER CLOUD-5093 (clientes: VOVO DELMA, DISBAL, CLIMAX, etc.)

---

## Políticas de Benefícios

**Descrição**: Módulo para configuração de políticas de benefícios (ex: bonificação por meta, incentivos). Para mais detalhes, consultar a documentação específica (LINK).

---

## Consulta de Locks no Banco (SQL)

**Link para consulta de locks**: [OneDrive - Consulta Locks SQL]

**Script útil para identificar bloqueios**:

```sql
SELECT
    OBJECT_NAME,
    SESSION_ID,
    ORACLE_USERNAME,
    LOCKED_MODE,
    'ALTER SYSTEM KILL SESSION ''' || SID || ',' || SERIAL# || ''' IMMEDIATE;' AS KILL_COMMAND
FROM V$LOCKED_OBJECT LO
JOIN DBA_OBJECTS OBJ ON LO.OBJECT_ID = OBJ.OBJECT_ID
JOIN V$SESSION SES ON LO.SESSION_ID = SES.SID;
```

---

## Casos Específicos de Produto Não Aparece

### Produto Fora de Linha

**Cenário**: Produto não aparece no catálogo do RCA.

**Verificações**:
- `MXSPRODUT.OBS2` com valor 'FL' (Fora de Linha).
- Parâmetro `OCULTAR_PROD_FORA_LINHA` habilitado. Desabilitar para exibir produtos fora de linha.

### Código de Distribuição Divergente

**Cenário**: Produto não aparece devido a código de distribuição diferente.

**Verificações**:
- `MXSPRODUT.CODDISTRIB` deve ser igual a `MXSFORNEC.CODDISTRIB`. Se divergirem, o produto pode ser ocultado.

### Restrição de Venda (Rotina 391)

**Cenário**: Produto não aparece devido a restrições cadastradas na rotina 391.

**Solução**: Cadastrar parâmetro `RESTRINGIR_PRODUTOS_391 = 'N'` para exibir produtos mesmo com restrição.

### Filial Não Aparece para Cliente Específico

**Verificações**:
- Cliente possui tabela de preço para a filial?
- Cliente está na `MXSTABPRCLI` com a filial correta?
- Há restrição de venda (rotina 391) para o cliente/filial?
- Verificar divergências na base.

### Erro de Custo Financeiro

**Descrição**: Erros como "Custo Financeiro inválido" ocorrem quando `CUSTOREAL`, `CUSTOFIN` ou `CUSTOREP` estão zerados na `MXSEST`. Esses valores devem ser maiores que zero.

**Verificação**:

```sql
SELECT CUSTOREAL, CUSTOFIN, CUSTOREP, E.*
FROM MXSEST E
WHERE CODPROD = :codprod;
```

**Possível causa**: Se os valores estiverem corretos, verificar a filial retira padrão do produto (`MXSPRODUT.CODFILIALRETIRA`). Se o RCA não tiver acesso a essa filial, o sistema pode tentar buscar custo dessa filial e falhar.

---

## Atualizar Coordenadas do Cliente

**Parâmetros**:
- `GPS_UPDATE_COORDENADAS_ON_PEDIDO` – Atualiza coordenadas ao fazer pedido.
- `GPS_UPDATE_COORDENADAS_ON_JUSTIFICATIVA_VISITA` – Atualiza ao justificar visita.
- `GPS_UPDATE_COORDENADAS_ON_ALTERACAO_CADASTRO_CLIENTE` – Atualiza ao alterar cadastro.
- `CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE` – Pergunta ao usuário se deseja atualizar as coordenadas após confecção do pedido (em conjunto com `GPS_TRACKING_ENABLED`).
- Permissão: **"Solicitar autorização para alterar coordenadas do cliente"** no painel admin.

---

## Solicitação de Visita Avulsa

**Descrição**: Permite que o RCA adicione um cliente ao roteiro do dia atual, mesmo não estando agendado.

**Procedimento**:
1. No aplicativo, clicar e segurar sobre o cliente na lista.
2. Selecionar a opção **"Gerar Visita Avulsa"**.
3. O cliente será adicionado ao roteiro do dia.

**Parâmetros**: (necessário verificar se há parâmetros que controlam essa funcionalidade).

---

## Pedido TV7 e TV8 (Venda Assistida)

**Descrição**: Tipos de venda TV7 (venda assistida) e TV8 (venda assistida com entrega) no maxPedido.

**Atenção**: Se a integradora do Winthor for versão 30 ou superior, ela barra pedidos TV8.

**Configuração**:
1. Parâmetro: `HABILITA_VENDA_ASSISTIDA = 'S'`.
2. No cadastro do usuário/perfil, conceder permissão para **Tipo de Venda 7 e 8**.
3. Fluxo no aplicativo: ao iniciar pedido, selecionar o tipo de venda desejado.

---

## Crédito Disponível do Cliente Não Atualiza na APK

**Causa**: Parâmetro `CONSIDERAR_CLIENTE_EXCLUIDO_LIMITE` na `PCMXSCONFIGURACOES` está como 'N'. Isso faz com que, se o cliente principal estiver excluído (`DTEXCLUSAO` preenchido ou `CODOPERACAO = 2`), ele não seja considerado no cálculo do limite.

**Solução**: Alterar o parâmetro para 'S' se desejar considerar clientes excluídos no cálculo.

---

## Limitar Quantidade de Venda de Determinado Produto

**Para Winthor**: Funciona por cotas (rotina específica a pesquisar).
**Para OERPs**: Enviar o endpoint **ProdutosUsuarios** (tabela `MXSPRODUSUR`), que define limites por produto por usuário.

---

## Tipo de Venda TV4 - Simples Fatura (Broker)

**Descrição**: TV4 é utilizada para vendas do tipo Broker, onde a venda é feita em nome de um terceiro.

**Pré-requisitos**:
- `CONDVENDA4` na `MXSCLIENT` = 'S'.
- RCA com permissão para TV4 na Central de Configurações.
- Parâmetros:
  - `BROKER_HABILITADO = 'S'` (Máxima)
  - Winthor: parâmetro 1666 `FIL_BROKER = 'S'`, parâmetro 1667 `FIL_TIPOBROKER = 'PAD'`.

**Funcionamento**: Ao iniciar um pedido TV4, o RCA deve informar a filial configurada para Broker. As informações de preço, tributação, etc., seguem as mesmas regras do TV1.

---

## Parâmetro para Habilitar Aba de Relatórios da Central

**Parâmetro**: `HABILITAR_GERADOR_RELATORIOS = 'S'` (Central de Configurações). Essa aba permite personalizar o relatório do espelho do pedido.

---

## Bloquear Pedido com Cliente Pendente no Roteiro Anterior

**Parâmetros** (exemplo do chamado MXPEDDV-69774):
- `DIAS_VERIFICACAO_ROTEIRO_PENDENTE = 1` (considera ontem)
- `BLOQ_RCA_COM_ROTA_PENDENTE = 'S'`
- `JUSTIFICAR_ROTEIRO_ANTERIOR = 'S'`
- `ROTEIRO_PENDENTE_ONTEM = 'S'`

**Comportamento**: Se no dia anterior houver clientes na rota sem justificativa, bloqueia novos pedidos até que sejam justificados.

---

## Como Analisar o Extrator na Máquina Linux (Comandos Úteis)

**Instalação do Docker**:

```bash
sudo apt update
sudo apt-get remove docker docker-engine docker.io containerd runc -y
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

**Instalação do Portainer**:

```bash
docker run -d -p 9000:9000 --name MXS_Portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce --admin-password '$2y$05$Xb5IB53HjCQqfD/7k9F2d.thkVspomm/2udcI6/dg8Q6nKJ9Z0Zda' --logo "https://maxsolucoes-versoes.s3.amazonaws.com/extrator/v1/logo/logo-maxima.png"
```

**Verificar conectividade**:

```bash
telnet intext-hmg.solucoesmaxima.com.br 81
telnet intpdv-hmg.solucoesmaxima.com.br 81
telnet appsy.solucoesmaxima.com.br 8081
```

**Exemplo de stack (docker-compose)**:

```yaml
version: '3'
services:
  MxS-Extrator_None_Cliente:
    privileged: true
    image: dockermaxima/extrator:latest
    environment:
      USUARIO_EXTRATOR_NUVEM: "xxxx"
      SENHA_EXTRATOR_NUVEM: "xxxx"
      USUARIO_SYSTEM_WINTHOR: "xxxx"
      SENHA_SYSTEM_WINTHOR: "xxxx"
      TZ: America/Sao_Paulo
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /app/maxima/MXS_Extrator/imagens_data:/mnt/maxima/produtos_fotos
      - /app/maxima/MXS_Extrator/extrator_prd_data/Conf:/app/maxima_extrator/extrator_prd/Conf
      - /app/maxima/MXS_Extrator/extrator_prd_data/LOGS:/app/maxima_extrator/extrator_prd/LOGS
    ports:
      - 9002:81
```

---

## Mudança de Servidor Winthor

**Procedimento realizado em chamado**:
- Alterado IP do banco Winthor no extrator.
- Alterado usuário/senha da conexão Winthor.
- Após atualização do extrator (versão .361 para .382), foi necessário ativar parâmetro `PRIMEIRA_IMPLANTACAO`.
- Atualizado ambiente local e nuvem (Hangfire e Atualizador).
- Atualizada versão do aplicativo (3.209 para 3.228.1).

---

## Sem Acesso ao Portainer e Hangfire

**Verificações**:
- Testar portas com ferramentas como [testedeportas.com](https://testedeportas.com) ou [yougetsignal.com](https://www.yougetsignal.com/tools/open-ports/).
- Verificar se as portas (9000, 9002, etc.) estão liberadas no firewall.
- Acessar o servidor Linux do cliente e verificar se o serviço do Docker está rodando e escutando as portas.

**Comandos para testar no Linux**:
```bash
telnet intext-hmg.solucoesmaxima.com.br 81
telnet intpdv-hmg.solucoesmaxima.com.br 81
telnet appsv.solucoesmaxima.com.br 8081
```

---

## Pedido Complementar

**Descrição**: Pedido que complementa um pedido principal já existente (com NUMPEDERP gerado), permitindo adicionar itens extras que serão faturados na mesma nota.

**Parâmetro**: `HABILITAR_OPCAO_PEDIDO_COMPLEMENTAR`

**Regras**:
- Não é possível inserir no complementar um produto já existente no pedido principal.
- O pedido principal não pode estar na posição "Faturado" no ERP.

**Fluxo**:
1. Fazer um pedido TV1 normalmente.
2. Ao criar novo pedido, marcar a opção **"É complementar"** no cabeçalho.
3. Selecionar o pedido principal na lista (baseado na `MXSHISTORICOPEDC`).

---

## Cotação de Concorrente

**Descrição**: Funcionalidade que permite ao RCA registrar preços de concorrentes. Para mais detalhes, consultar a Base do Conhecimento (LINK).

---

## Bloquear Pedidos Fora de Rota

**Por usuário (todos)**:
- Marcar a permissão **"Bloquear venda de clientes fora da rota"** na Central de Configurações.

**Por quantidade**:
- Parâmetro `QTD_MAX_PED_FORA_ROTA` (número) – define quantos pedidos fora de rota são permitidos. Se zero, não valida. Se marcada a permissão de bloqueio, não é necessário usar este parâmetro.
- Parâmetro `PERIODO_PED_FORA_ROTA` (número) – define o período (dias) para contar os pedidos fora de rota (0 = só hoje, 1 = hoje + ontem, etc.). Informações são armazenadas na `MXSPEDIDOFORAROTA`.

---

## Bloquear Envio de Pedido para Cliente Acima do Limite

**Prioridade de parâmetros**:

1. **`BLOQ_SALVAR_PEDIDO_ACIMA_LIMITE_CLI_APK`** (Central de Configurações) – Bloqueia o salvamento do pedido quando cliente não tem limite suficiente, independente do Winthor.
2. **`BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE`** (Central) – Controla envio.
3. **`CON_ACEITAVENDABLOQ`** (Winthor) – Se 'N', não envia; se 'S', aceita enviar.

---

## Preço na Listagem vs. Tela de Negociação (Divergência)

**Possíveis causas**:
- Campo `CALCULAST` na `MXSCLIENT`: se 'S', calcula ST e aplica na negociação; se 'N', pode haver divergência.
- Campo `PERACRESCISMOPF` na `MXSTRIBUT` preenchido e parâmetro `VALIDAR_ACRESCIMO_PF_LISTAGEM` não habilitado: faz com que o preço da listagem inclua acréscimo para pessoa física, mas a negociação não.

---

## Mensagem de Endereço Secundário ao Iniciar Pedido

**Erro**: "É necessário escolher um endereço secundário para que o sistema possa buscar a tributação, caso não seja escolhido será usado o padrão do cliente."

**Resolução**: O parâmetro `UTILIZATRIBENDENT` da rotina 132 está habilitado para a filial. Desabilitá-lo.

---

## Nível de Venda

**Descrição**: Controle de acesso a cobranças baseado no nível de venda do cliente. Um cliente com nível de venda 5 (mais restritivo) só pode usar cobranças de nível igual ou superior (ex: nível 5, 4, etc.). Nível 1 é o mais permissivo.

**Exemplo**:
- Cliente vinculado a uma cobrança de nível 5 (campo `NIVELVENDA` na `MXSCOB`).
- Tenta usar cobrança de bonificação de nível 3 → bloqueado.

**Referência**: Biblioteca Máxima – Nível de Venda.

---

## Sugestão de Venda Não Aparece

**Descrição**: Sugestão de venda são produtos com alta probabilidade de compra, baseados no histórico do cliente.

**Requisitos**:
- Cliente precisa ter histórico de compras repetidas nos últimos 3-6 meses.
- Dados são obtidos da `MXSHISTORICOPEDC` e `MXSHISTORICOPEDI`.
- Parâmetro `CATALOGO_PEDIDOS_DIAS_SYNC` deve ser suficientemente grande (recomendado 90 a 180 dias) para que haja dados.
- Após alterar o parâmetro, pode ser necessária uma carga de dados nas tabelas de histórico.

**Funcionamento**:
1. Iniciar um pedido.
2. Na aba "Tabela", uma pop-up pergunta se deseja iniciar uma sugestão de venda.
3. Se aparecer "Não há sugestão de venda para esse cliente", provavelmente falta histórico ou o período é curto.

---

## Comportamento do Campo Valor do Imposto (IPI)

**Exemplo**: Percentual de IPI no banco (5%) divergente do correto (3,25%). Necessário que a integração envie novamente os percentuais.

**Configuração**:
- Tabela `MXSTRIBUT` (endpoint Tributos) – campos `MOSTRARPVENDASEMIPI` e `MOSTRARPVENDASEMST` devem estar 'S' para exibir preços sem impostos.
- Produto pode ter `PERCIPIVENDA` na `MXSPRODUT` para IPI específico.

---

## Importação de Arquivo de Negociação

**Descrição**: Permite importar configurações de negociação (descontos, promoções) via arquivo. Ver Base do Conhecimento para detalhes.

**Possíveis erros na Central de Configurações**: (verificar logs e formato do arquivo).

---

## Comissões

**Para OERPs**:
- Endpoint `ComissoesRegioes` (tabela `MXSCOMISSAOREGIAO`) ou `ComissoesUsuarios` (`MXSCOMISSAOUSUR`).

**Parâmetro**: `EXIBIR_SUGESTAO_PRECO_COMISSAO` – Exibe a diferença em reais da comissão que o RCA receberia se praticasse um desconto diferente.

**Observação**: As comissões mostradas dependem do campo `PERDESCMAX` da `MXSTABPR` (desconto máximo permitido). Comissões com percentual acima do máximo não aparecem.

---

## Desmembramento de Pedido por Filial Retira

**Parâmetro**: `DESMEMBRAR_PED_FILIAL_RETIRA` (configurável por usuário/perfil/geral).

**Funcionamento**:
- Habilitado: ao salvar e enviar o pedido, o aplicativo desmembra o pedido com base na filial retira de cada item. Cada grupo de itens com mesma filial retira vira um pedido separado, com aquela filial no cabeçalho.
- Validações são feitas no pedido original.
- Não é permitido usar autorização em pedidos que serão desmembrados.

**Ticket relacionado**: MXPEDDV-79067.

---

## Data da Última Compra na Lista de Clientes

**Descrição**: A data exibida no canto inferior direito da lista de clientes vem do campo `DTULTCOMP` da `MXSCLIENT`. Não é necessariamente a data do último pedido no maxPedido, pois pode haver pedidos feitos diretamente no ERP (rotina 316).

---

## Cadastro de Grupos de Clientes / Grupos de Produtos

**No Winthor**:
- Rotina 3311 → `PCGRUPOSCAMPANHAC` (cabeçalho) e `PCGRUPOSCAMPANHAI` (itens).
- Tipo: 'GR' para grupo de produtos, 'CL' para grupo de clientes.

**Para OERPs**:
- Endpoint `GruposCampanhas` (cabeçalho) e `GruposCampanhasItens` (itens).

**Como funciona**:
- Define um código de grupo e o tipo.
- No caso de grupo de clientes, `CODITEM` = `CODCLI`.
- No caso de grupo de produtos, `CODITEM` = `CODPROD`.

---

## Limitar Quantidade de Itens em um Pedido

**Parâmetros**:
- `VERIFICAR_QTD_MAX_ITENS_PEDIDO` (S/N) – Habilita a verificação.
- `VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO` (inteiro) – Quantidade máxima de itens permitida.

---

## Compartilhar Nota Fiscal (DANFE) dos Pedidos

**Requisitos**:
- Banco atualizado.
- Dados na `ERP_MXSDOCELETRONICO` (endpoint Doceletronico para OERPs).
- App na versão V4.
- Pedido com posição "Faturado" (caso contrário, opção desabilitada).
- Coluna `NUMTRANSVENDA` na `MXSHISTORICOPEDC` preenchida.
- Para compartilhar boleto: cobrança do pedido deve ser boleto (`MXSCOB.BOLETO = 'S'`) e parâmetro `EXIBE_LINHA_DIGITAVEL` habilitado.

**Erro "Não foi possível gerar o XLS"**:
- Verificar permissão do app "Acesso a todos os arquivos" nas configurações do dispositivo.

---

## Inserir Quantidade Máxima de Produtos por Pedido

**Descrição**: Controlar a quantidade máxima de um mesmo produto em um pedido.

**Implementação**: Pode ser feito via restrições no ERP (rotina 391) ou via campos de limite no cadastro do produto (`QTDMAXPEDIDO` na `MXSPRODUT`? – verificar).

---

## Campanha por Pontuação

**Tabelas envolvidas**:
- `MXSPROMOC` (cabeçalho)
- `MXSPROMOI` (itens)

**Parâmetro**: `EXIBIR_PONTOS_PROD_LISTAGEM` – Exibe pontuação dos produtos na listagem.

---

## MAX VIEWER

**Descrição**: Ferramenta de suporte para acesso remoto à tela do cliente.

**Links de download**:
- Cliente Windows: [maxviewer_clientes.exe](https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer_clientes.exe)
- APK Android: [maxviewer.apk](https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer.apk)
- EXE Windows (stand-alone): [maxviewer.exe](https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer.exe)
- Debian/Ubuntu: [maxviewer-linux-installer-v1-x86_64.deb](https://maxsolucoes-versoes.s3.us-east-1.amazonaws.com/ti/maxviewer/maxviewer-linux-installer-v1-x86_64.deb)
- Acesso web: [http://maxviewer.maximatech.com.br:21114/](http://maxviewer.maximatech.com.br:21114/)

---

## MAX CATÁLOGO

### Liberando Versão do MaxCatálogo

**Requisitos**:
- maxPedido deve estar na versão >= 3.246.0.
- Rotina: 9 (maxCatálogo).
- Link de acesso: `https://maxcatalogoapi.solucoesmaxima.com.br/api/v1/`
- Package name: `br.maximasistemas.catalogo`

**Exemplo de liberação**:
- Cliente: 1846 - MORBENE
- Versão: 2.12.14
- Link de download: `https://nexus.maximasistemas.com.br/repository/public/br/maximasistemas/maxcatalogo/2.12.14/maxcatalogo-2.12.14.apk`

---

## MAX-GESTÃO

### maxGestão PWA

**Links**:
- [https://maxgestao-pwa.solucoesmaxima.com.br](https://maxgestao-pwa.solucoesmaxima.com.br)
- [Base do conhecimento: Como instalar em Android](link)
- [Base do conhecimento: Como instalar em iOS](link)

### Supervisor Não Aparece no maxGestão

**Verificações**:
- Usuário tem permissão para ver supervisores?
- Supervisor está inativo?
- RCA's vinculados ao supervisor na rotina 516 do Winthor?

### Dashboard - Indicadores

**Rotinas de origem**:
- Rotina 146: Emissão
- Rotina 111: Faturamento

**Parâmetros obrigatórios no ERP (PCMXSCONFIGURACOES)**:
- `UTILIZA_GESTAO_LOGISTICA = 'S'`
- `ENVIA_PEDIDOS_TELEMARKETING` (e outros: BROKER, CALL_CENTER, BALCAO, AUTOSERVICO)

**Script para consultar esses parâmetros**:

```sql
SELECT * FROM PCMXSCONFIGURACOES
WHERE NOME IN ('UTILIZA_GESTAO_LOGISTICA','ENVIA_PEDIDOS_TELEMARKETING','ENVIA_PEDIDOS_BROKER','ENVIA_PEDIDOS_CALL_CENTER','ENVIA_PEDIDOS_BALCAO','ENVIA_PEDIDOS_AUTOSERVICO','ENVIAR_PRODUTO_SEM_REVENDA');
```

**Cálculo dos valores do dashboard (exemplo)**:

```sql
-- Total de vendas
SELECT SUM(VLATEND), SUM(VLTABELA), SUM(VLTOTAL)
FROM MXSHISTORICOPEDC
WHERE TRUNC(DATA) BETWEEN TO_DATE('inicio','DD/MM/YYYY') AND TO_DATE('fim','DD/MM/YYYY')
  AND CODOPERACAO != 2
  AND POSICAO NOT IN('C');

-- Total de itens vendidos
SELECT SUM(QT * PVENDA)
FROM MXSHISTORICOPEDI
WHERE NUMPED IN (
    SELECT NUMPED FROM MXSHISTORICOPEDC
    WHERE TRUNC(DATA) BETWEEN ... AND POSICAO NOT IN('C')
)
AND POSICAO NOT IN('C');
```

### RCA Vinculado Não Aparece ao Supervisor

**Verificações**:
- Na `MXSUSUARI`, campo `CODSUPERVISOR` deve estar preenchido com o código do supervisor.
- Na `MXSSUPERV`, o código deve corresponder.

**Script para listar supervisores acessíveis a um usuário**:

```sql
SELECT CODSUPERVISOR, NOMESUPERVISOR, CODFILIAL
FROM (
    -- consulta complexa com permissões
) V
WHERE CODFILIAL IS NOT NULL
GROUP BY CODSUPERVISOR, NOMESUPERVISOR, CODFILIAL
ORDER BY CODSUPERVISOR;
```

**Resolução**: Se o supervisor não aparecer, pode ser falta de vínculo com filial na `MXSUSUARI.CODFILIAL`. Se for de todas as filiais, usar filial 99.

### Localização - maxTrack

**Parâmetros**:
- `GPS_TRACKING_ENABLED = 'S'` – habilita rastreamento.
- `GPS_TRACKING_INTERVAL` – intervalo de captura em segundos (recomendado 30s).
- `GPS_TRACKING_STARTTIME` – horário de início do serviço (ex: 0700).

**Observações**:
- Nem todo RCA pode ser rastreado (apenas CLT ou PJ com contrato).
- No app, é necessário fornecer permissão de localização "o tempo todo".
- Modo avião e economia de energia devem ser desativados.

**Análise de rastros**:
- Exportar base maxTrack e consultar com SQLite.
- Endpoint da API de rastros: `https://maxrastro-prod.solucoesmaxima.com.br/swagger/index.html`

**Exemplo de consulta na API**:
```
https://maxrastroprod.solucoesmaxima.com.br/api/v1.1/eventos/hora-evento?codigoProdutoMaxima=1&codigoClienteMaxima=xxxx&dateStart=2024-10-28T00:00:00&dateEnd=2024-10-28T23:59:59&codigoUsuario=yyyy&tipoEvento=CHECKIN,CHECKOUT,PEDIDO,...
```

**Como obter token**: No inspetor do navegador (Central de Configurações), copiar o token do local storage e usar no Swagger.

---

## Encerramento

Este documento consolida as principais informações de suporte e configuração dos produtos Máxima, especialmente maxPedido, integração com Winthor, banco de dados e procedimentos comuns. Para dúvidas não contempladas, consulte a Base do Conhecimento oficial ou abra um chamado para o time de suporte.