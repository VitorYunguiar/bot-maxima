# Parametros e Configuracao — Base de Conhecimento maxPedido/Winthor

## Metadados

**Palavras-chave**: parametros, configuracao, maxPedido, winthor, central de configuracoes, permissoes, perfil de usuario, sincronizacao

**Sistema**: maxPedido / Winthor / Central de Solucoes

**Area**: Configuracao e Administracao

---

## Tabela de Parametros do Sistema

### Como Usar Este Documento

Este documento consolida todos os parametros do sistema maxPedido/Winthor, procedimentos de configuracao via Central de Solucoes, e informacoes essenciais sobre perfis de usuario, permissoes e integracao.

Os parametros estao organizados por categoria funcional para facilitar a busca. Cada parametro possui descricao, tipo de dado, tipo de parametro (Geral/Usuario/Filial) e tabela de armazenamento.

---

## Parametros de GPS e Rastreamento

### GPS_TRACKING_ENABLED

**Descricao**: Habilitar a utilizacao do GPS e geracao da base maxTracking, permitindo rastreamento dos RCA's.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GPS_TRACKING_INTERVAL

**Descricao**: Intervalo de envio de localizacoes (em segundos). O valor padrao desse parametro e 5, ou seja, de 5 em 5 segundos as coordenadas capturadas no aparelho do RCA serao enviadas para o banco.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE

**Descricao**: Ao termino da confeccao de um pedido, o sistema vai questionar o usuario se ele deseja atualizar as informacoes de GPS do cliente. Atua em conjunto com a permissao SOLICITAR AUTORIZACAO PARA ALTERAR COORDENADAS DO CLIENTE na Central de Configuracoes.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GPS_IS_REQUIRED_CONFEC_PEDIDO

**Descricao**: Quando habilitado, nao permite que o representante inicie o pedido sem que o GPS esteja habilitado.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GPS_UPDATE_COORDENADAS_SOMENTE_SE_NAO_PREENCHIDO

**Descricao**: So altera as coordenadas se estiverem vazias.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Check-in e Check-out

### UTILIZA_CHECKIN_CHECKOUT

**Descricao**: Habilita utilizacao de Check-in e Check-out no maxPedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### PERMITIR_PEDIDO_SEM_CHECKIN

**Descricao**: Permite realizar pedidos sem efetuar check-in para o cliente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### OBRIGA_CHECKIN_CLIENTE_FORA_ROTA

**Descricao**: Obriga check-in caso o cliente esteja fora do roteiro do dia. Se o cliente nao tiver nenhum roteiro no dia, entao o RCA sera obrigado a realizar check-in para qualquer cliente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### LIMITE_RAIO_CHECK_IN_OUT

**Descricao**: Configurar o limite do raio para que se possa efetuar Check-in e Check-out no cliente, ou seja, se estiver '100' o check-in ou check-out so pode ser realizado quando o representante estiver dentro de um raio de 100 metros da localizacao cadastrada do cliente.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### TEMPO_MIN_PERMANENCIA

**Descricao**: Configurar o tempo minimo de atendimento do representante ao cliente, caso este utilize Check-in / Check-out. O valor do parametro deve conter 5 caracteres, incluindo os dois pontos. Ex: 00:10. Ou seja, o tempo minimo entre o check-in e check-out sera de 10 minutos.

**Tipo de Dado**: 1 - LITERAL

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### OBRIGAR_ATENDIMENTO_PARA_CHECKOUT

**Descricao**: Quando habilitado, o maxPedido nao permitira fazer check-out sem que tenha sido feito atendimento no cliente (atendimento pode ser um pedido ou entao uma justificativa de nao venda).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Bloqueio e Limite de Credito

### BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ

**Descricao**: Caso habilitado, nao vai permitir fazer pedido se o cliente estiver bloqueado.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ

**Descricao**: Bloquear confeccao de pedidos quando o cliente principal esta bloqueado.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ALERTAR_TIT_VENCIDO

**Descricao**: Ao iniciar um pedido em um cliente que possua titulos vencidos, o RCA sera alertado atraves de uma pop-up que existe titulos vencidos.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### NUMERO_DIAS_CLIENTE_INADIMPLENTE

**Descricao**: Define a quantidade de dias que o cliente inadimplente tera seu pedido bloqueado, definido como inteiro, colocar o numero de dias.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE

**Descricao**: Caso habilitado, ira bloquear realizacao de pedido em cliente que estiver com titulos em aberto (inadimplente).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ALERTAR_TIT_INADIMPLENTE

**Descricao**: Ao iniciar um pedido de vendas de um cliente que possua titulos inadimplentes o RCA sera alertado atraves do em pop-up.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQUEIA_PEDIDO_CLIENTE_SEMLIMITE

**Descricao**: Caso habilitado, o pedido sera feito, porem ficara bloqueado na APK e nao sera enviado para o banco nuvem. Assim que normalizado, devera editar o pedido ou duplicar o mesmo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ACEITAVENDAAVISTACLIBLOQ

**Descricao**: Com o parametro = 'S' o sistema deixara iniciar o pedido para cliente bloqueado, porem deixara salvar apenas se o plano de pagamento for "A VISTA" e a cobranca for: Dinheiro (D), Dinheiro em transito (DH) ou Cartao (CAR).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: FILIAL

**Tabela**: MXSPARAMFILIAL

### ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO

**Descricao**: Aceita ou bloqueia fazer pedidos quando clientes da rede estiverem bloqueados.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CON_ACEITAVENDABLOQ

**Descricao**: Bloqueia ou nao venda para clientes bloqueados.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMFILIAL

### BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE

**Descricao**: E se parametro CON_ACEITAVENDABLOQ - Aceita venda bloqueado da rotina 132 estiver como N e o parametro BLOQPEDLIMCRED estiver como N nao deixa salvar o pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CON_PEREXCEDELIMCRED

**Descricao**: Parametro do ERP Winthor utilizado para configurar um percentual maximo permitido para exceder o limite de credito do cliente na venda e funciona no maxPedido. A configuracao quando ativada funciona para todos os RCAs, sem possibilidade de excecoes.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMFILIAL

### ATUALIZAR_LIMCRED_CLIENTE_POS_PEDIDO

**Descricao**: Habilita atualizacao do limite de credito do cliente logo apos o envio de pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_ALERTA_CREDITO_CLIENTE

**Descricao**: Habilitado como 'S', ira exibir uma mensagem com o valor de credito do cliente ao iniciar o pedido. Padrao = 'N'.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Conta Corrente (CC / Flex)

### CON_USACREDRCA

**Descricao**: Define se utiliza ou nao o processo de conta corrente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: FILIAL

**Tabela**: MXSPARAMFILIAL

### EXIBIR_SALDOCC_DISPONIVEL

**Descricao**: Exibir o valor do saldo de Conta Corrente disponivel nos campos referentes a CC. Se estiver desabilitado, sera apresentado dois tracos no lugar de Saldo de Conta Corrente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### APRESENTAR_CARD_CC

**Descricao**: Caso o campo USADEBCREDRCA do RCA seja = 'S', e o parametro APRESENTAR_CARD_CC estiver habilitado, entao sera apresentado o card de conta corrente na tela inicial do maxPedido. Caso o parametro esteja desabilitado, o card nao sera apresentado, mesmo se o RCA utiliza o processo de Conta Corrente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GERAR_DADOS_CC_RCA

**Descricao**: Sincroniza as movimentacoes de conta corrente, inicialmente apenas os ultimos 7 dias.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DESCONTA_SALDOCCRCA_OFFLINE

**Descricao**: Define se pedidos salvos como bloqueados ou pedidos pendentes (Offline) irao influenciar no saldo de Conta Corrente. Atencao, pode causar divergencia entre o saldo de conta corrente no aparelho e o que e apresentado no ERP.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### IMPEDIR_ABATIMENTO_SEMSALDORCA

**Descricao**: Se for = 'N', vai permitir que seja debitado saldo de Conta Corrente do RCA mesmo que esteja negativo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQUEAR_SALVAR_PEDIDO_SEMSALDORCA

**Descricao**: Parametro que bloqueia a gravacao de pedidos por RCA sem saldo de conta corrente (flexivel).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DESABILITA_INSERCAO_ITEM_ACIMALIMITECREDITORCA

**Descricao**: Nao vai permitir a inclusao de produtos no pedido com desconto caso o C.C. do RCA esteja igual ou menor que zero ou seja inferior ao desconto informado.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_TODA_MOVIMENTACAO_CC

**Descricao**: Parametro para definir se na aba de totais a exibicao do saldo previsto CC vai exibir toda movimentacao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

**Nota sobre Conta Corrente**: Verificar sempre se MXSUSUARI.USADEBCREDRCA = S e o tipo de movimentacao CON_TIPOMOVCCRCA (valores possiveis: VA - Debito na venda credito no acerto, VF - Debito na venda credito no faturamento, VV - Debito/Credito na venda, FF - Debito/Credito no faturamento).

---

## Parametros de Roteiro e Visitas

### QTD_MAX_PED_FORA_ROTA

**Descricao**: Quantidade maxima de pedidos fora de rota que o maxPedido aceita. Ex.: Se for configurado com o valor 3, entao o maxPedido aceitara no maximo 3 pedidos fora de rota. Se for configurado com o valor 0 o parametro nao sera validado.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### PERIODO_PED_FORA_ROTA

**Descricao**: Quantidade de dias para zerar a validacao da quantidade maxima de pedidos fora de rota. Se o valor for 0, valida no dia atual a quantidade maxima permitida em pedidos fora de rota.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_RCA_COM_ROTA_PENDENTE

**Descricao**: Bloqueia iniciar o pedido no dia se tiver com rotas pendentes no dia anterior.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_RETRO_DIAS_ROTEIRO

**Descricao**: Representa a quantidade maxima de dias de atraso que possa ser visualizado o roteiro.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLK_SYNC_ROTEIRO_PENDENTE

**Descricao**: Se estiver ativo e existirem clientes do Roteiro de Visitas ainda nao atendidos ou justificados, ao tentar sincronizar, o sistema emitira o alerta: "existem clientes ainda nao atendidos ou justificados".

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

### DIAS_ATENDI_ROTEIRO_SEMANAL

**Descricao**: Quantidade de dias que o RCA tem para atender a rota dele. Caso este parametro seja preenchido, o sistema ira considerar que o RCA tem a quantidade de dias informado para visitar o cliente.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DIAS_ADIAMENTO_VISITA

**Descricao**: Limite de dias para adiamento de visita.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### PERMITIR_DELETE_HISTORICOCOMP

**Descricao**: Parametro do backend. Caso habilitado, ira deletar o historico de compromissos (compromissos do dia anterior).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Horario de Atendimento

### BLOQ_VENDA_FORA_HORARIO_COM

**Descricao**: Controlar os horarios que o RCA podera confeccionar pedidos.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_VENDA_FORA_HORARIO_COM_IM

**Descricao**: Controlar os horarios que o RCA podera confeccionar pedidos atraves do Forca de Vendas (Android) - IM => Inicio Manha - DEVE OBEDECER O FORMATO: HHMM. Exemplo: 1430 para 14:30.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_VENDA_FORA_HORARIO_COM_IT

**Descricao**: Controlar os horarios que o RCA podera confeccionar pedidos atraves do Forca de Vendas (Android) - IT => Inicio Tarde - DEVE OBEDECER O FORMATO: HHMM. Exemplo: 1430 para 14:30.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_VENDA_FORA_HORARIO_COM_TM

**Descricao**: Controlar os horarios que o RCA podera confeccionar pedidos atraves do Forca de Vendas (Android) - TM => Termino Manha - DEVE OBEDECER O FORMATO: HHMM. Exemplo: 1430 para 14:30.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_VENDA_FORA_HORARIO_COM_TT

**Descricao**: Controlar os horarios que o RCA podera confeccionar pedidos atraves do Forca de Vendas (Android) - TT => Termino Tarde - DEVE OBEDECER O FORMATO: HHMM. Exemplo: 1430 para 14:30.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Estoque

### BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE

**Descricao**: Quando o produto nao tem estoque, bloqueia a insercao do item sem estoque.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQUEAR_VENDA_ACIMA_DO_ESTOQUE

**Descricao**: Quando o parametro for 'S', o sistema nao vai deixar o RCA vender uma quantidade de itens acima do estoque disponivel para o mesmo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DESABILITA_ALERTA_ESTOQUE

**Descricao**: Desabilita o alerta de "Produto sem estoque suficiente" ao inserir esse produto no pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBE_ESTOQUE_FILIAL

**Descricao**: Para visualizar o estoque de outras filiais, na opcao '+ Inf.' na tela de insercao do produto.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ENVIA_ESTOQUE_TODAS_FILIAIS

**Descricao**: Quando habilitado permite visualizar o estoque dos produtos mesmo nas filiais que o rca nao tem acesso.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ENVIA_NOTIFICACAO_ESTOQUE_TODAS_FILIAIS

**Descricao**: Parametro para enviar previsao de estoque mesmo das filiais que o rca nao tem acesso.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_ESTOQUE_BLOQUEADO

**Descricao**: Exibir estoque bloqueado, caso esteja como 'S' sera exibido o estoque bloqueado na listagem e no dialog de inserir produto.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_ESTOQUE_CONTABIL

**Descricao**: Parametro responsavel por exibir na tela de insercao produto o estoque contabil dele.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBE_VALIDADE_PRODUTO_WMS

**Descricao**: Habilita a visualizacao da validade dos produtos que estao no WMS na opcao '+.Info' na tela de insercao do item.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Pedidos e Orcamentos

### PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO

**Descricao**: Mostra os pedidos do historico de pedidos na timeline de pedidos.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITAR_DADOS_ENTREGA

**Descricao**: Habilitar Acompanhamento de Entrega dentro da Timeline de Pedidos (somente se tiver maxMotorista).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DIAS_EDICAO_PEDIDO

**Descricao**: Quantidade de dias permitido para que o rca possa editar o pedido.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITA_PED_CLI_NAO_SINC

**Descricao**: Permite ao RCA digitar pedido de cliente recem cadastrado, sem precisar atualizar o cadastro do cliente no ERP. (Isso pode gerar duplicidade de clientes na listagem de clientes, caso tenha duplicidade, e necessario realizar swipe na timeline de pedidos).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITA_PED_CLI_RECEM_CADASTRADO

**Descricao**: Permite iniciar pedido para clientes recem cadastrados (pre-cadastro), que ainda nao tiveram aprovacao do cadastro no ERP.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### TRUNCAR_ITEM_PCPEDI

**Descricao**: Deixa colocar o mesmo item varias vezes no pedido se marcado como S.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### PERMITE_INICIAR_PEDIDO_COMO_ORCAMENTO_NAO_MOV_CC

**Descricao**: Com esse parametro cadastrado e definido como S, ao inciar um pedido a aplicacao vai questionar se voce deseja iniciar um pedido de orcamento, caso marque sim, o pedido vai ser apenas em orcamento, caso marque nao, vai iniciar um pedido normal. Com este parametro cadastrado com valor S o saldo conta corrente nao e movimentado em pedido orcamento. Caso este parametro esteja cadastrado, porem sem nenhum valor, a aplicacao vai iniciar o pedido e dentro da negociacao voce define se quer salvar o pedido normal ou orcamento.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQUEIA_ENVIO_ORCAMENTO_ERP

**Descricao**: Bloqueia envio de orcamento para o winthor.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### INTERVALO_ENVIO_PEDIDOS_APK

**Descricao**: Tempo definido em minutos para definir o envio automatico de pedidos, validado somente na APK.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ENVIA_PEDIDOS_BALCAO

**Descricao**: Enviar Historico de pedidos Balcao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ENVIA_PEDIDOS_CALL_CENTER

**Descricao**: Enviar Historico de pedidos do Call Center.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ENVIA_PEDIDOS_TELEMARKETING

**Descricao**: Enviar Historico de pedidos do Telemarketing.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Pedidos Bloqueados e Pendentes

### BLK_CONN_CONSIDERAORCBLOQCOMOPEND

**Descricao**: Considera orcamento bloqueado para envio como pendente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

### BLK_CONN_CONSIDERAPEDBLOQCOMOPEND

**Descricao**: Considera pedido bloqueado para envio como pendente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

### BLK_CONN_INTERVALOCONEXAO

**Descricao**: Bloqueio de pedidos - Intervalo entre conexoes para bloquear novo pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

### BLK_CONN_PRIMEIRACONEXAO

**Descricao**: Bloqueio de pedidos - Hora limite para efetuar a primeira sincronizacao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

### BLK_CONN_QTDEORCPENDENTE

**Descricao**: Bloqueio de orcamentos - Quantidade de orcamentos pendentes para bloqueio de novo orcamento.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

### BLK_CONN_QTDEPEDPENDENTE

**Descricao**: Bloqueio de pedido - Quantidade de pedidos pendentes para bloqueio de novo pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

---

## Parametros de Bonificacao (TV5)

### OBRIGATORIOVINCULARTV5COMTV1

**Descricao**: Obrigar o vinculo de pedido TV1 no pedido de bonificacao. Obs: o mesmo parametro existe na rotina 132 por filial.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: FILIAL

**Tabela**: MXSPARAMFILIAL

### PEDIR_AUTORIZACAO_TV5_VINCULADO_TV1

**Descricao**: quando habilitado junto com a permissao de "solicitar autorizacao de pedido bonificado", ao vincular um pedido tv1 em um tv5 ira solicitar a aprovacao do tv5. ou ao gerar tv5 depois do tv1 na aba de cabecalho. Essa autorizacao vai para o maxGestao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_ALTERACAO_PED_BONIFIC

**Descricao**: Bloqueia a alteracao de pedidos de bonificacao (TV5) qunado ja salvos no pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

**Nota sobre Bonificacao**: Para bloquear RCA de fazer bonificacao sem saldo de C/C, verificar: CON_USACREDRCA = S, CON_BONIFICALTDEBCREDRCA = S, IMPEDIR_ABATIMENTO_SEMSALDORCA = S, PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N.

---

## Parametros de Descontos e Precos

### CON_ACEITADESCPRECOFIXO

**Descricao**: Aceita aplicar desconto em Politica de Preco Fixo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: FILIAL

**Tabela**: MXSPARAMFILIAL

### USAR_CAMPANHA_DESCONTO_PROGRESSIVO

**Descricao**: Esse parametro ativa a campanha de desconto progressivo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### TIPO_DESC_PROGRESSIVO

**Descricao**: Para utilizar o desconto progressivo como Campanha Progressiva, deve estar com o valor 'PRG'. Para utilizar o desconto progressivo como Campanha P&G, deve estar com o valor 'PEG'.

**Tipo de Dado**: 1 - LITERAL

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### APLICAR_CAMPANHA_DESCONTO_PRIORITARIA

**Descricao**: Questiona quanto a aplicacao da campanha de desconto da rotina 561.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### NOTIFICAR_PRODUTO_CAMPANHA_3306

**Descricao**: Quando o rca inserir um produto na aba tabela que esta cadastrado em uma campanha da rotina 3306, ira notificar informando que o produto faz parte de uma campanha de desconto.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_SUGESTAO_PRECO_COMISSAO

**Descricao**: Apresenta a diferenca em reais da comissao que o RCA recebera caso pratique uma porcentagem determinada de desconto. Esta funcionalidade foi criada para apresentar ao RCA melhores oportunidades de ganhos em sua comissao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

**Nota sobre Desconto Maximo**: Verificar MXSTABPR.PERDESCMAX, MXSCLIENTREGIAO.PERDESCMAX e as Politicas de desconto do item.

---

## Parametros de Plano de Pagamento e Cobranca

### LISTAR_TODOS_PLANOS_PAGAMENTO

**Descricao**: Listar planos de pagamento ao cadastrar um novo cliente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ORDENACAO_PLANO_PAGAMENTO

**Descricao**: Ordernar a lista do plano de pagamento.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### VALIDAR_PRAZOMEDIO_COBRANCA_DH

**Descricao**: Permite a cobranca DH trabalhar a prazo. Deve ser colocado como N para permitir a cobrana DH ser a prazo caso contrario sera tratada como DINHEIRO.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CON_CODPLPAGINICIAL

**Descricao**: Parametro do ERP Winthor que define o plano de pagamento padrao ao cadastrar clientes pelo forca de vendas.

**Tipo de Dado**: 1 - LITERAL

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMFILIAL

### CONFIRMAR_ALTERACAO_PLANO_PAGTO

**Descricao**: E utilizado pra saber se o RCA vai poder escolher uma das 3 opcoes de recalculo ou se o recalculo sera automatico, trabalha em conjunto com o paramtro PADRAORECALCPLPAG.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Titulos e Financeiro

### SOMAR_JUROS_TITULOS

**Descricao**: Vai somar o valor do Juros no valor do Titulo. O RCA nao ira ter necessidade de fazer contas.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ENVIAR_APENAS_TITULOS_VENCIDOS

**Descricao**: Somente os dados de titulos que estao vencidos sobem para a nuvem, os demais titulos nao serao importados.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIRTITULOSPAGOS

**Descricao**: Parametro que permite exibir titulos pagos na consulta de titulos, caso esteja habilitado, os titulos pagos que estao na base da APK serao exibidos na tela de titulos pagos.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBE_PREV_COMISSAO

**Descricao**: Visualiza ou nao a Previsao de comissao listada na pesquisa de titulos. Para nao trazer deve estar setado com N.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_TAXABOLETO

**Descricao**: Informa se a taxa de boleto deve ser apresentada ou nao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITAR_SOMA_MULTA_TITULO

**Descricao**: Habilita soma da multa no saldo de titulos na aba de titulos pendentes.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### APENAS_TITULOS_FILIAIS_PERM

**Descricao**: Exibe os titulos em aberto apenas das filiais permitidas.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### FILTRAR_DADOS_TITULOS_RCA

**Descricao**: Utiliza o valor do parametro FILTRAR_DADOS_RCA / S - So mostra os titulos do RCA que esta logado / N - Mostra os titulos de todos os RCAs.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

**Nota sobre Imprimir Boleto**: EXIBE_LINHA_DIGITAVEL = S - Ira aparecer a linha de boleto na tela de titulo e ao clicar, gera o arquivo PDF do boleto.

---

## Parametros de Filial e Tributacao

### PERMITE_FILIAL_NF_NULA

**Descricao**: Aceita salvar pedidos sem filialNF quando habilitada permissao para selecionar via spinner na apk. FilialNF sera identica a filial do cabecalho conforme parametro COMPORTAMENTO_WHINTOR_FILIAL = S.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GRAVAR_FILIAL_NF_NULO

**Descricao**: Quando o parametro GRAVAR_FILIAL_NF_NULO esta com o valor igual 'S' e o cliente nao tem uma filial NF definida e o pedido tambem nao tem filial NF definida. O aplicativo vai utilizar o preco da regiao do cliente (Ou seja o preco de acordo com a praca do cliente).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### USA_FILIALNF_CLIENTE_PARA_DEFINIR_TRIBUTACAO

**Descricao**: Usa filial de Nota Fiscal para definir tributacao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO/FILIAL

**Tabela**: MXSPARAMETRO

### COMPORTAMENTO_WHINTOR_FILIAL

**Descricao**: Valida as filiais de venda conforma comportamento do winthor.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DEFINE_FILIAL_RETIRA_PADRAO

**Descricao**: Define qual sera a filial retira padrao de todos os produtos, independente do cadastro do winthor.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### FILIALNF_DEFINE_FILIAL_PEDIDO

**Descricao**: A filial de nota fiscal define a filial de venda (Carrega filial definida ou especificada para o cliente).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CALCULAR_ST_SAIDA

**Descricao**: O parametro visa identificar a aliquota de ST Saida cadastrada nos campos MXSTRIBUT.ALIQSTSAIDA e MXSTRIBUT.ALIQSTSAIDAPF.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

---

## Parametros de Cadastro de Clientes

### DESATIVA_VALIDACAO_CNPJ_CADASTRADO

**Descricao**: Quando habilitado nao fara a validacao, no Winthor, se o cliente ja existe pelo CNPJ/CPF. Permitindo assim o representante salvar e enviar o cadastro do cliente realizado no aplicativo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CLIENTESIMPLESNACIONAL_SIM

**Descricao**: Define se a opcao Cliente Simples Nacional vira sim por padrao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CLIENTECONTRIBUINTE_SIM

**Descricao**: No cadastro do cliente, a opcao Cliente Contribuinte vira por padrao Sim.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DESABILITA_CADASTRO_PESSOA_FISICA

**Descricao**: Ira desabilitar o cadastro de Cliente quando esse for pessoa Fisica.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ENVIAR_CLIENTES_RCA_9999

**Descricao**: Parametro que controla o envio de clientes vinculados ao rca 9999.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### LIST_CLI_CPFCNPJ

**Descricao**: Habilita mostrar o CNPJ do cliente na listagem de clientes.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### FILTRAR_CLIENTES_CONSUMIDOR_FINAL

**Descricao**: Filtra se o rca ou todos vao poder clientes consumidor ou nao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITA_CLIENTES_BLOQUEIO_DEFINITIVO

**Descricao**: Parametro ira listar os clientes com bloqueio definitivo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQUEIA_PRACA_PADRAO

**Descricao**: Bloqueia alteracao de praca no cadastro de cliente. Trabalha em conjunto com o maxsuporte COD_PRACA_PADRAO.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### COD_PRACA_PADRAO

**Descricao**: Praca padrao que sera utilizada no cadastro de novos clientes.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITA_ENVIAR_TODAS_AS_PRACAS_PARA_RCA

**Descricao**: Habilitar envio de todas as pracas.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DIAS_ATUALIZACAO_CADASTRO_CLIENTE

**Descricao**: Valida o campo DTULTALTER da MXSCLIENT e ao iniciar pedido questiona ou forca a edicao do cadastro do cliente (se valor = 0 nao abre dialogo, ou seja, tem que ser > 0) - Vinculo com Parametro: FORCAR_ATUALIZACAO_CADASTRO_CLIENTE.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### FORCAR_ATUALIZACAO_CADASTRO_CLIENTE

**Descricao**: vinculo com paramtro: DIAS_ATUALIZACAO_CADASTRO_CLIENTE.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITA_ALERTA_CLIENTE_OBS

**Descricao**: Gerar pop-up, essas observacoes sao as do campo "Pos. Financeira" do Forca de Vendas, que sao correspondentes ao Campo "Observacao" da Rotina 1203. Cada linha corresponde a observacao. A linha 1 corresponde ao parametro 'HABILITA_ALERTA_CLIENTE_OBS'.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CON_VLMAXVENDAPF

**Descricao**: Parametro do ERP Winthor para configurar um valor maximo que pode ser realizado atraves de pedidos para cliente pessoa fisica no Mes.

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMFILIAL

---

## Parametros de Embalagem e Quantidade

### USA_EMBALAGEM_UNIDADE_PADRAO

**Descricao**: Quando habilitado so ira influenciar no processo de Frios, das tres embalagens padrao de Frios a embalagem do meio 'KG' sera ocultada.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### USAR_MULTIPLO_QTDE

**Descricao**: Realiza um calculo com a quantidade informada x multiplo do produto, pode ser usando em conjunto com o parametro INICIA_QTDE_UM.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### INICIA_QTDE_UM

**Descricao**: Define se sinaliza ou nao clientes sem comprar a X dias. Trabalha em conjunto com o parametro QT_DIAS_SINALIZAR_CLIENTE.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITAR_ARREDONDAMENTO_MULTIPLO

**Descricao**: Habilitar ou desabilitar opcao de arredondamento para multiplo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_QUANTIDADE_SEM_FATOR_EMBALAGEM

**Descricao**: faz a divisao da quantidade unitaria pela quantidade da caixa.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### ATIVAR_NOTIFICACAO_EMBALAGEM_MASTER

**Descricao**: Quando ativado ira gerar um lerta mostrando que o produto tem embalagem master.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Espelho do Pedido (PDF/Email)

### EXIBIR_PRECO_UNIT_EMB

**Descricao**: Exibir preco unitario do pedido no layout padrao do espelho do pedido (arquivo gerado para compartilhar o pedido).

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### APRESENTAR_DESCONTOS_PEDIDO_EMAIL

**Descricao**: Quando habilitado, ira exibir os campos de desconto no layout padrao do espelho do pedido. Campos: VL DESC % DESC.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### OCULTAR_IMPOSTOS_PEDIDO_EMAIL

**Descricao**: Quando habilitado, ira ocultar os impostos do pedido no layout padrao do espelho do pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### OCULTAR_VALIDADE_PROPOSTA

**Descricao**: Quando habilitado, ira ocultar o campo de validade proposta no layout padrao do espelho do pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_FOTO_DO_PRODUTO_PDF

**Descricao**: Quando habilitado, ira exibir as fotos dos produtos no layout padrao do espelho do pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBIR_FOTO_DO_PRODUTO_PERSONALIZADO_PDF

**Descricao**: Quando habilitado, ira exibir as fotos dos produtos no layout personalizado do espelho do pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### DESABILITAR_ESPELHO_PED_PADRAO

**Descricao**: Quando o parametro estiver habilitado e tiver um ou mais layout de espelho do pedido customizado, entao nao sera aparesentado o espelho do pedido padrao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

**Nota sobre Espelho do Pedido**: EXIBIR_CAMPOS_ESPELHO_POR_EMBALAGEM = S em conjunto com EXIBIR_PRECO_UNIT_EMB cria um campo chamado VL. UNIT EMB. que mostra o valor total da embalagem, nao o valor unitario dos produtos da embalagem.

---

## Parametros de Mix, Positivacao e Recomendacao

### GERAR_DADOS_MIX_CLIENTES

**Descricao**: Habilita o mix do cliente.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GERAR_DADOS_MIX_CLIENTES_DIAS

**Descricao**: Quantidade de dias para gerar o mix de clientes.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### FILTRAR_DADOS_RCA_MIXVENDIDO

**Descricao**: Quando este parametro estiver setado como 'S', no mix do cliente ira filtrar o mix do cliente por RCA.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### FILTRAR_FILIAL_MIX

**Descricao**: Se S so aparece produtos da filial que esta sendo digitado o pedido. Caso esteja como N, ira apresentar idependente da filial de venda. DEFAULT maxPedido = 'S' caso nao existir cadastrado.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GERAR_DADOS_POS_CLIENTES

**Descricao**: Habilita gerar e exibir os clientes positivados no sistema.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GERAR_DADOS_POS_PRODUTOS

**Descricao**: Habilita gerar e exibir os produtos positivados no sistema.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### AGRUPAR_RELPOSITIVCLIENTE_FORNEC

**Descricao**: Caso esteja ativado, agrupa a apresentacao dos clientes positivados por fornecedores na guia de Consultas.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITA_RECOMENDACAO_PRODUTOS

**Descricao**: Parametro responsavel por habilitar a recomendacao de produto no maxPedido atraves da inteligencia artificial (IA). Gera dados depois de 24h apos a ativacao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXIBE_SUGESTAO_VENDA

**Descricao**: Exibir Sugestao de Venda.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Sincronizacao e Comunicacao

### CONFIRMAR_PROCESSO_SYNC

**Descricao**: Quando este parametro estiver ativado, ao clicar em Comunicar para realizar a sincronizacao do aparelho, sera questionado se deseja realmente sincronizar com as opcoes de Sim ou Nao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITAR_CONEXAO_SINC

**Descricao**: Ao iniciar o processo de sincronizacao, caso o aparelho nao esteja com nenhuma rede Wi Fi ou 3G ativa, o sistema ira habilitar uma das redes para iniciar a sincronizacao e a encerrara ao termino do processo de sincronizacao.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BAIXAR_FOTOSPROD_APENAS_WIFI

**Descricao**: Configura se as fotos de produto na APK devem ser baixadas apenas se houver conexao com WIFI - Padrao: N.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMETRO

**Nota**: Para permitir o download das imagens utilizando a rede de dados moveis, no menu Configuracoes clicar em ver parametros e marcar "Enviar fotos usando redes moveis (3G/4G)".

---

## Parametros de Mensagens e Notificacoes

### APRESENTAR_MSG_POS_ENVIO

**Descricao**: Quando o RCA enviar um recado, caso esse parametro esteja como S, o recado ficara visivel em Mensagens / Caixa de Saida.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_MARCAR_MSG_COMO_LIDA

**Descricao**: Opcao dentro de 'Mensagens', 'Marcar todas como lidas', sera bloqueada caso o parametro esteja como Sim.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### EXCLUIR_SOMENTE_LIDAS

**Descricao**: Caso a parametro esteja ativo, verifica se o RCA selecionou mensagens nao lidas e impede caso haja tentativa de exclusao, orientando a leitura.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Relatorios e Menus

### HABILITAR_GERADOR_RELATORIOS

**Descricao**: Quando "S" habilita a opcao de relatorios customizados no Central de Configuracoes do maxPedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### OCULTAR_COMISSAO_MENU

**Descricao**: Ao ser habilitado, oculta o menu de comissao da tela inical do aplicativo.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### BLOQ_PERIODO_MENU_RCA

**Descricao**: Bloquear lupa de pesquisa (Botao de Filtros) na tela de Resumo de Vendas, aba RESUMO.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Metas e Estatisticas

### CRITERIOVENDAFDEDUZIRDEV

**Descricao**: Faz com que o sistema deduza as devolucoes na apuracao dos resultados de metas. Deduz devolucao na venda liquida.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### CRITERIOVENDAFCONSIDERADEVAVULSA

**Descricao**: Faz com que o sistema deduza as devolucoes avulsas na apuracao dos resultados de metas.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

**Nota sobre Meta Grafico**: Rotinas relacionadas: 399 / 3305. Tabelas relacionadas: ERP_MXSMETARCA, PCMETARCA, PCMETA. Nao necessariamente as informacoes precisam descer para nuvem, se tratando da rotina 3305, basta apenas que a meta esteja na tabela PCMETA. Possivelmente existe chance de nao informar a meta caso a flag de dias uteis nao esteja marcada.

---

## Parametros de Integracao e Outros Produtos

### HABILITA_MAXPESQUISA

**Descricao**: Habilita para trabalhar com maxPesquisa integrado ao maxPedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITA_VENDA_ASSISTIDA

**Descricao**: habilita a opcao de venda assistida nas informacoes do pedido.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### VALIDAR_FILTRO_BRINDEX

**Descricao**: Valida restricoes de brinde na tela de Politicas de brinde da negociacao do produto.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: USUARIO

**Tabela**: MXSPARAMETROVALOR

**Nota sobre Brindes**: Tabelas relacionadas: MXSBRINDEEXRESTRICOES, MXSBRINDEEX, MXSBRINDEEXVALIDACOES, MXSBRINDEEXPREMIO.

---

## Parametros de Troca e Devolucao

### CON_USATROCACOMPRECOVENDA

**Descricao**: Parametro do ERP Winthor, quando ativado grava as mercadorias a retirar com custo financeiro, trocas dos tipos de venda 11 e 12. Este parametro quando (S) usa o custo financeiro ao inves de usar o proprio preco de venda da mercadoria. Quando (N), usa o preco de venda do item na troca.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL

**Tabela**: MXSPARAMFILIAL

---

## Parametros de Frete

### EDITAR_VALOR_FRETE

**Descricao**: Opcao de editar o valor de frete no pedido de venda.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Personalizacao e Visualizacao

### HABILITA_CHKBOX_AGRUPAMENTO

**Descricao**: Se "S" ao iniciar um pedido de vendas a opcao "Permitir Agrupamento" estara selecionada the full, caso o parametro esteja como "N" a opcao ira iniciar o pedido sem estar selecionada, mas o RCA podera seleciona-la se necessario.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### HABILITAR_VISUALIZACAO_COD_FAB_PROD_TAB

**Descricao**: Exibir codigo do fabrica na listagem dos produtos.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Parametros de Cerca Eletronica (GPS Edge)

### GPS_EDGE_BLOCK

**Descricao**: Cerca Eletronica - Validar cerca eletronica.

**Tipo de Dado**: 3 - LOGICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GPS_EDGE_METERS_SIZE

**Descricao**: Cerca Eletronica - Tolerancia da cerca eletronica (pode ser colocada a metragem desejada).

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GPS_TRACKING_STARTTIME

**Descricao**: Cerca Eletronica - Horario inicial do acompanhamento (pode ser alterado).

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

### GPS_TRACKING_STOPTIME

**Descricao**: Cerca Eletronica - Horario final do acompanhamento (pode ser alterado).

**Tipo de Dado**: 2 - NUMERICO

**Tipo Parametro**: GERAL/USUARIO

**Tabela**: MXSPARAMETRO

---

## Como Inserir Parametros na Central de Solucoes

### Passo 1: Acessando a Central de Solucoes

Acesse o portal maxSolucoes atraves do link: https://appsv.solucoesmaxima.com.br

Digite o usuario e senha de acesso para fazer login no sistema.

### Passo 2: Selecionando o Ambiente

Em casos em que ha dois ambientes "Homologacao" e "Producao", deve-se escolher o ambiente desejado antes de prosseguir.

**Importante**: Na maioria dos casos o correto e escolher o ambiente de "Producao". O ambiente de "Homologacao" e escolhido apenas em casos em que este ambiente esta validado para testes.

### Passo 3: Acessando o Menu Parametros

Na tela inicial da Central de Configuracoes, acesse o menu:

**Configuracoes > Parametros**

Em seguida, clique na opcao que esta localizada no menu inferior direito: **Criar parametro**

### Passo 4: Preenchendo os Dados do Parametro

Ira surgir uma janela onde iremos alimentar com algumas informacoes referente ao parametro que estamos inserindo:

**Titulo do parametro**: Preencher com o titulo do parametro, esse titulo serve apenas para identificacao.

**Nome do parametro**: Esse campo deve ser preenchido com bastante cuidado pois e onde iremos informar o parametro de fato, respeitando letras minusculas e maiusculas e sem espacos.

**Descricao**: Informar nesse campo um breve resumo descrevendo a funcionalidade do parametro e qual a funcao ira exercer.

**Categoria**: Escolher entre as categorias existentes que podem ser:
- Venda
- Configuracao
- Sincronismo
- Aplicativo
- Catalogo Eletronico
- Estatisticas
- Servidor de comunicacao
- Estoque
- Cadastros
- Email
- Geolocalizacao
- Clientes
- Personalizacao
- Integracao
- Pronta entrega
- Jornada

**Tipo do parametro**: Escolher entre:
- Geral
- Por usuario
- Por filial

**Tipo de dado**: Escolher entre:
- Literal (1)
- Inteiro/Numerico (2)
- Logico (3)

### Passo 5: Salvando o Parametro

Logo apos configurado o parametro, clicar em **Salvar** para finalizar.

---

## Como Configurar Data Limite para Atualizacao do maxPedido

### Resumo

A data limite para atualizacao trata-se do prazo maximo em que o RCA podera usar a versao liberada. Logo apos, o mesmo sera obrigado a atualizar a versao para a proxima disponivel.

### Passo 1: Acessando o Portal

Acesse o portal atraves do seguinte link: https://appsv.solucoesmaxima.com.br

Informe o usuario e senha de acesso.

**Importante**: E necessario ter o Login e Senha do maxSolucoes em maos para fazer as configuracoes.

### Passo 2: Selecionando o Ambiente

Em casos em que ha dois ambientes "Homologacao" e "Producao", deve-se escolher o ambiente desejado antes de prosseguir. Na maioria dos casos o correto e escolher o ambiente de "Producao".

### Passo 3: Definindo a Data Limite para Atualizacao

Navegar ate a tela **Liberar Versao**, onde iremos definir o prazo limite para atualizacao de cada versao liberada.

Acessar o menu lateral e clicar nas opcoes:

**Cadastro > 304 - Liberar Versao**

Na tela que segue, clicar na opcao **Novo**.

Apos clicar nessa opcao:

1. Selecionar o **Cliente**
2. Selecionar a **Rotina/Versao** (essa e a versao que desejamos liberar/definir data limite)
3. Selecionar os **RCA's** que estarao dentro da regra (e possivel selecionar todos os usuarios, bem como filtrar o(s) usuario(s) desejado(s) ou tambem selecionar apenas um clicando no nome dele)
4. Clicar em **Adicionar Selecionados**
5. Preencher o campo **Data Limite Atualizacao**
6. Clicar em **Salvar** para efetivar as configuracoes realizadas

---

## Como Realizar o Processamento de Imagens no maxPedido

### Pre-requisitos

**Diretorio das imagens compartilhada na mesma rede do extrator**:
O diretorio das imagens deve estar compartilhado no mesmo ambiente de rede em que a maquina Extrator/Linux e com permissao de acesso.

**Ponto de montagem configurado no Extrator/Linux**:
O ponto de montagem deve esta previamente configurado na maquina Linux do extrator. Caso o seu servidor Linux nao esteja com essa configuracao pronta, entre em contato com o seu analista de suporte para que ele possa realizar essa configuracao.

### Passo 1: Processando as Fotos

Para processar as imagens, acessar o menu superior direito no aplicativo e logo em seguida clicar em **Ferramentas**.

Depois clicar em **Baixar fotos**, sera forcado o processamento das imagens e elas serao baixadas no aplicativo.

Logo abaixo ira aparecer uma caixa de dialogo pedindo para que nos certifiquemos que o celular esta conectado no wifi. A configuracao padrao so permite o download das fotos quando conectado a esse tipo de rede.

**Nota**: Para acompanhar o progresso do download, observar a barra de notificacoes do Android.

### Passo 2: Permitir Download Via Rede Movel (Opcional)

Para permitir o download das imagens utilizando a rede de dados moveis, no menu **Configuracoes** clicar em **ver parametros** e marcar **Enviar fotos usando redes moveis (3G/4G)**.

---

## Como Cadastrar Perfil de Usuarios no maxPedido

### Passo 1: Acessar Menu de Perfil de Usuarios

Na Central de Configuracoes do maxPedido, clicar no **Menu lateral > Cadastros > Perfil de Usuarios**.

### Passo 2: Criar Novo Perfil

Clicar no icone de **+** no canto direito inferior da tela.

### Passo 3: Configurar Tipo de Perfil

**Caso for um Perfil Administrador**: Quando marcado, as demais opcoes nao serao visualizadas pois, entende-se que devido ser de Administrador ele tera acesso total Referente aos Dados.

**Caso nao seja usuario Administrador**: Clicar na aba **Acesso** para configurar acesso do perfil referente a:
- Fornecedores
- Departamentos
- Secoes
- Regioes
- Transportadoras

Clicar em cada uma delas para configurar.

### Passo 4: Configurar Parametros do Perfil

Na aba **Parametros**, configurar:
- Horario de sincronizacao
- Opcao de bloquear envio de Pedidos e recebimento de dados fora do horario
- Cadastro do horario permitido para a coleta de dados do maxTracking
- Parametros
- Inteligencia Geografica

**Referencias**:
- Como configurar dias e horarios de captura do maxTracking (Rastro)
- Como trabalhar com Inteligencia Geografica no maxGestao

---

## Como Vincular Novo Usuario Cadastrado

### Passo 1: Acessar Menu de Usuarios

Acessar a Central de Configuracoes do maxPedido, clicar no **menu lateral > Cadastros > Usuarios**.

**Importante**: Antes de realizar o vinculo, verificar se o usuario foi devidamente Cadastrado no Portal maxSolucoes.

### Passo 2: Editar Usuario

Localizar o usuario cadastrado e clicar no icone de **editar** da coluna **Acoes**.

### Passo 3: Aplicar Perfil de Acesso

Na tela de edicao clicar na aba **Permissoes**, selecionar um perfil de acesso e clicar em **Aplicar**.

Sera exibido na tela um Pop-up para que seja confirmado ou nao o vinculo para o perfil. Clicar na opcao **Sim** para confirmar o vinculo.

### Passo 4: Vincular Representante

Apos a confirmacao sera direcionado para a aba **Dados do Usuario**.

Selecionar o **Representante do ERP** e logo em seguida clicar em **Salvar**.

### Passo 5: Finalizar

Apos realizar estes passos, o vendedor estara apto a utilizar o maxPedido, baixando o aplicativo **maxSolucoes** pela loja Play Store com o Login e as credencias cadastradas.

---

## Parametros de Historico de Pedidos - Filtros

### FILTRAR_HISTCOMPRAS_RCA

**Descricao**: O mesmo realiza ou nao o filtro onde sera apresentado o historico de compras somente do rca quem vendeu ou de todos os representantes.

**Valor**: N (para mostrar todos) / S (apenas do RCA atual)

### FILTRAR_DADOS_RCA

**Descricao**: Mostrar apenas pedidos que foram realizados pelo RCA atual (Se configurado como N traz de todos os RCAs que fizeram pedido no cliente).

**Valor**: N (para mostrar todos) / S (apenas do RCA atual)

### FILTRAR_DADOS_CONSULTA_POSITIVACAO_RCA

**Descricao**: Quando este parametro estiver verdadeiro (S), ira trazer a positivacao dos clientes somente dos pedidos que o RCA fez no modulo Consultas > Positivacao de clientes.

**Valor**: N (para mostrar todos) / S (apenas do RCA atual)

### CATALOGO_PEDIDOS_DIAS_SYNC

**Descricao**: Mostra o historico de vendas dos ultimos X dias.

**Tipo de Dado**: NUMERICO

**Valor Padrao**: 90

---

## Parametros de Previsao de Faturamento

### OBRIGAR_PREVISAO_FATURAMENTO

**Descricao**: Obriga o preenchimento da previsao de faturamento.

**Tipo de Dado**: 3 - LOGICO

**Valor**: N (nao obriga) / S (obriga)

### PRAZO_VALIDADE_PREVISAOFATURAMENTO

**Descricao**: Define o prazo de validade da previsao de faturamento em dias.

**Tipo de Dado**: 2 - NUMERICO

**Valor Padrao**: 30

### PREVISAO_FATURAMENTO_DIA_MAIS_UM

**Descricao**: Define se a previsao de faturamento deve considerar D+1.

**Tipo de Dado**: 3 - LOGICO

**Valor**: S (considera D+1) / N (nao considera)

### CONSIDERAR_DATA_ATUAL_PREV_FAT

**Descricao**: Define se deve considerar a data atual na previsao de faturamento.

**Tipo de Dado**: 3 - LOGICO

**Valor**: N (nao considera) / S (considera)

---

## Tabelas de Permissoes e Acessos

### MXSACESSODADOS

**Descricao**: Acesso as permissoes da central de configuracoes: cobrancas, planos de pagamento, filial de venda, etc.

**Uso**: Controla permissoes gerais do sistema disponibilizadas na Central de Configuracoes.

### MXSACESSOENTIDADES

**Descricao**: Acesso da aba "acessos" das permissoes da central de configuracoes.

**Uso**: Controla acesso a entidades especificas como fornecedores, departamentos, secoes, regioes e transportadoras configurados no perfil de usuario.

---

## Verificacao de Servico Oracle - Agendamento

Consulta SQL mantida no documento canonico `05-SQL-BANCO-E-INTEGRACAO.md`, secao **CONSULTAS SQL DE SUPORTE GERAL**.

---

## Notas Importantes sobre Configuracao

### Sobre Conta Corrente (CC/Flex)

Para trabalhar corretamente com Conta Corrente, verificar:
- CON_USACREDRCA = S
- EXIBIR_SALDOCC_DISPONIVEL = S
- MXSUSUARI.USADEBCREDRCA = S

Tipos de movimentacao (CON_TIPOMOVCCRCA):
- VA: Debito na venda, credito no acerto
- VF: Debito na venda, credito no faturamento
- VV: Debito/Credito na venda
- FF: Debito/Credito no faturamento

### Sobre Venda Broker

Tabela relacionada: MXPED57813

### Sobre Combos de Desconto

Tipos de campanhas disponiveis:
- MIQ: Campanha de desconto por Mix Quantidade
- SQP: Campanha de desconto por Superacao Quantidade Produto
- MQT: Campanha de desconto por Meta Quantidade Total
- FPU: Campanha de desconto Flex Por Unidade
- FPV: Campanha de desconto Flex Por Valor

Consultar a Base de Conhecimento Maxima Tech para detalhes de configuracao de cada tipo de campanha.

---

## Glossario de Termos

**RCA**: Representante Comercial Autonomo - Usuario do sistema maxPedido que realiza vendas em campo

**APK**: Android Package - Aplicativo maxPedido instalado no dispositivo Android

**Central de Configuracoes**: Portal web para gerenciar parametros, usuarios e configuracoes do maxPedido

**maxSolucoes**: Portal de acesso web para configuracoes (https://appsv.solucoesmaxima.com.br)

**Winthor**: Sistema ERP integrado ao maxPedido

**TV1**: Tipo de venda normal/padrao

**TV5**: Tipo de venda de bonificacao

**CC / Flex**: Conta Corrente Flexivel - Sistema de credito para RCA

**Check-in / Check-out**: Registro de entrada/saida em visita ao cliente

**Roteiro**: Planejamento de visitas do RCA aos clientes

**Filial NF**: Filial emissora da Nota Fiscal

**Mix**: Conjunto de produtos vendidos/comprados historicamente

**Positivacao**: Registro de produtos ou clientes com regras especiais

---

## Documento Atualizado em

Data de consolidacao: 2026-02-11

Fontes: BASE DE PARAMETROS MAXIMA TECH.pdf, BMX-26050686 (inserir parametros), BMX-23561224 (data limite atualizacao), BMX-26673755 (processamento imagens), BMX-116262480 (cadastro perfis), BMX-18153545 (vincular usuarios), Lembretes.pdf
