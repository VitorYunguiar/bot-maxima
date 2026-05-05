# Mapa de Funcionalidades e Tabelas da Logística

Referência que conecta funcionalidades de maxRoteirizador e maxMotorista ?s tabelas usadas em diagnóstico.

## INTRODUÇÃO

Este capítulo tem como objetivo servir como um índice rápido para o analista de suporte e para a IA.
Aqui, cada funcionalidade/tela dos módulos maxRoteirizador e maxMotorista é mapeada diretamente para:
o módulo em que ela se encontra (portal, app, roteirização, consultas, etc.);
as tabelas principais de banco de dados que alimentam aquela tela (tanto ERP quanto MXMP/MXS);
as tabelas auxiliares que influenciam filtros, cadastros, parametrizações e regras de negócio.
A ideia é que, ao receber um chamado sobre uma tela específica (“não aparece entrega”, “pedido não entrou na roteirização”, “dashboard divergente”), o analista consiga:
### localizar rapidamente a funcionalidade neste capítulo;
identificar quais tabelas consultar no banco para diagnóstico;
entender quais parametrizações ou cadastros podem estar impactando o comportamento daquela tela.
Este capítulo não entra em detalhes de regra de negócio de cada funcionalidade, mas funciona como um mapa técnico de referência, conectando telas ↔ módulos ↔ tabelas ↔ pontos de atenção de suporte.

### 4.1 MAXROTEIRIZADOR – MAPA FUNCIONALIDADE X TABELAS
#### 4.1.1 Funcionalidade: Roteirização – Mapa de Montagem de Carga

Módulo:
### maxRoteirizador – Roteirização
### Tabelas principais (ERP – origem do pedido):
### • MXSHISTORICOPEDC (cabeçalho do pedido)
### • MXSHISTORICOPEDI (itens do pedido)
### • ERP_MXSMOV (movimentos/pedidos em aberto)
• MXSNFSAID (notas fiscais emitidas, quando já faturado)
• MXSCLIENT (clientes)
### • MXSCLIENTENDENT (endereços de entrega do cliente)
Tabelas auxiliares (MXMP – parametrização e apoio):
### • MXMP_AREAS_ATENDIMENTO
### • MXMP_AREAS_ATENDIMENTO_FILIAL
### • MXMP_REGIOES_ATENDIMENTO
### • MXMP_TABELA_FRETE
### • MXMP_ROTA_COMPLEMENTO
### • MXMP_COMPLEMENTO_ROTA
### • MXMP_CONFIGURACAO_ROTEIRIZACAO
### • MXMP_PERFIL_ROTEIRIZACAO
### • MXMP_SERVICO_ROTEIRIZACAO
### • MXMP_PARAMETROS
### • MXMP_PARAMETROS_FILIAL
### • MXMP_LOCALIZACAO_CLIENTE
Tabelas auxiliares (ERP – cadastros de apoio):
### • MXSROTAEXP
### • MXSCIDADE
### • MXSPRACA
### • MXSREGIAO
### • MXSFILIAL
### • MXSPRODUT

Observações de suporte:
• A seleção de pedidos para montagem de carga parte de MXSHISTORICOPEDC / MXSHISTORICOPEDI, combinadas com o status em ERP_MXSMOV / MXSNFSAID.
• Filtros por cidade, praça, rota, região, etc. dependem do preenchimento correto desses campos no ERP e da vinculação nas tabelas MXMP_* de área/região.
### • Se o pedido “não aparece” no mapa:
o validar se existe em MXSHISTORICOPEDC / MXSHISTORICOPEDI;
### o conferir se está com status liberado/faturado;
o Checar se já não possui um numcar vinculado a ele na MXSHISTORICOPEDC
### ________________________________________
#### 4.1.2 Funcionalidade: Consultas – Carregamentos

Módulo:
### maxRoteirizador – Consultas
Tabelas principais (ERP):
• MXSCARREG (carregamentos no ERP)
### • MXSHISTORICOPEDC (pedidos vinculados ao carregamento)
### • MXSHISTORICOPEDI (itens dos pedidos do carregamento)
### • ERP_MXSMOV (movimentos/pedidos em aberto)
• MXSNFSAID (notas fiscais emitidas, quando já faturado)
• MXSCLIENT (clientes)
### • MXSCLIENTENDENT (endereços de entrega do cliente)

Tabelas principais (MXMP):
### • MXMP_ROMANEIO
### • MXMP_ROTA_ROMANEIO
### • MXMP_CUSTO_CARREGAMENTO
Tabelas auxiliares (MXMP):
### • MXMP_INFO_CROSSDOCKING
### • MXMP_INFO_TRANSBORDO
### • MXMP_FILIAIS_VEICULOS
Tabelas auxiliares (ERP):
### • ERP_MXSVEICUL
### • MXSEMPR
Observações de suporte:
• Quando um carregamento não aparece:
o confirmar se existe em MXSCARREG e em MXMP_ROMANEIO;
o conferir se os pedidos dele estão presentes em MXSHISTORICOPEDC / MXSHISTORICOPEDI;
o validar a filial e o status (carregamento fechado/aberto).
### ________________________________________
#### 4.1.3 Funcionalidade: Consultas – Romaneios

Módulo:
### maxRoteirizador – Consultas
Tabelas principais (ERP):
• MXSCARREG (carregamentos no ERP)
### • MXSHISTORICOPEDC (pedidos vinculados ao carregamento)
### • MXSHISTORICOPEDI (itens dos pedidos do carregamento)
### • ERP_MXSMOV (movimentos/pedidos em aberto)
• MXSNFSAID (notas fiscais emitidas, quando já faturado)
• MXSCLIENT (clientes)
### • MXSCLIENTENDENT (endereços de entrega do cliente)
Tabelas principais (MXMP):
### • MXMP_ROMANEIO
### • MXMP_ROTA_ROMANEIO
Tabelas auxiliares (MXMP):
### • MXMP_CUSTO_ROMANEIO
Tabelas auxiliares (ERP):
### • MXSCLIENT
### • MXSFILIAL
Observações de suporte:
• MXSHISTORICOPEDC/MXSHISTORICOPEDI são base para saber quais pedidos/itens compõem o romaneio.
• Se o romaneio não aparece ou parece incompleto:
### o checar se todos os pedidos/itens estão em MXSHISTORICOPEDC/MXSHISTORICOPEDI;
o conferir vínculos com MXSNFSAID e MXMP_ROMANEIO;
o validar filtros de período e filial.
### ________________________________________
#### 4.1.4 Funcionalidade: Consultas – Falha Geocode

Módulo:
### maxRoteirizador – Consultas
Tabelas principais (MXMP):
### • MXMP_FALHA_GEOCODE
### • MXMP_FILA_GEOCODE
Tabelas auxiliares (MXMP):
### • MXMP_LOCALIZACAO_CLIENTE
### • MXMP_LOCALIZACAO_END_ENTREGA
### • MXMP_SERVICO_GEOCODIFICACAO
### • MXMP_LOG_ERROS
Tabelas auxiliares (ERP):
### • MXSCLIENT
### • MXSCLIENTENDENT
### • MXSCIDADE
Observações de suporte:
### • Se cliente/pedido aparece em “falha geocode”, verificar:
o endereço em MXSCLIENT / MXSCLIENTENDENT;
### o se há pedidos relacionados em MXSHISTORICOPEDC;
o se houve erro de serviço em MXMP_FALHA_GEOCODE / MXMP_LOG_ERROS.
### ________________________________________
#### 4.1.5 Funcionalidade: Dashboard – Indicadores de uso

Módulo:
### maxRoteirizador – Dashboards
Tabelas principais (MXMP):
### • MXMP_POSICAO_TATICO_OPERACIONAL
Observações de suporte:
• Neste é neste campo que é preenchido as informações para acompanhamento do extrator do cliente se ele está online ou não banco de dados e servidor nesta tela é possível reiniciar o extrator e fazer validações de indicadores de uso.
### ________________________________________
#### 4.1.6 Funcionalidade: Dashboard – Pedidos prontos para montagem

Módulo:
### maxRoteirizador – Dashboards
Tabelas principais (ERP):
### • MXSROTAEXP
### • MXSPRACA
### • MXSFILIAL
### • MXSHISTORICOPEDC
### • MXSHISTORICOPEDI
Observações de suporte:
• “Pedidos prontos para montagem” vêm diretamente de MXSHISTORICOPEDC/MXSHISTORICOPEDI filtrados por status/condição.
### • Se um pedido não entra no indicador:
o conferir sua situação em MXSHISTORICOPEDC;
o validar se não está já vinculado em MXMP_BASE_CARREGAMENTO;
o checar parametrizações em MXMP_CONFIG_MAXENTREGAS.
### ________________________________________
#### 4.1.7 Funcionalidade: Cadastros – Clientes

Módulo:
### maxRoteirizador – Cadastros
Tabelas principais (ERP):
### • MXSCLIENT
### • MXSCLIENTENDENT
Tabelas principais (MXMP):
### • MXMP_CLIENTE_COMPLEMENTO
### • MXMP_CLIENTE_CENTRO_DISTRIBUICAO
Tabelas auxiliares (MXMP):
### • MXMP_LOCALIZACAO_CLIENTE
### • MXMP_LOCALIZACAO_END_ENTREGA
### • MXMP_REGIAO_CLIENTE
### • MXMP_REGIOES_ENTREGA
### • MXMP_REGIOES_ENTREGA_ROTAS
Tabelas auxiliares (ERP):
### • MXSCIDADE
### • MXSPRACA
### • MXSREGIAO
Observações de suporte:
• Problemas na roteirização/visualização de clientes muitas vezes envolvem:
• endereço incompleto em MXSCLIENTENDEN ou MXSCLIENT;
o ausência de localização em MXMP_LOCALIZACAO_CLIENTE;
o Falta de filial vinculada ao cliente
o Falta de vinculo do codcidade da MXSCIDADE
o Campos obrigatórios não preenchidos
### ________________________________________
#### 4.1.8 Funcionalidade: Cadastros – Veículos / Tipo / Característica

Módulo:
### maxRoteirizador – Cadastros
Tabelas principais (ERP):
### • ERP_MXSVEICUL
Tabelas principais (MXMP):
### • MXMP_TIPO_VEICULO
### • MXMP_VEICULO_COMPLEMENTO
### • MXMP_FILIAIS_VEICULOS
Tabelas auxiliares (MXMP):
### • MXMP_VEICULO_INDISPONIBILIDADE
### • MXMP_VEICULO_RASTREADOR
### • MXMP_TANQUE_COMBUSTIVEL
Observações de suporte:

• Se o veiculo não aparece, revisar vinculo de filial
• Se o veiculo não aparece, revisar campos obrigatórios
• Se o sistema recusa uma carga por capacidade, revisar:
o ERP_MXSVEICUL + MXMP_VEICULO_COMPLEMENTO;
o parâmetros de frete/capacidade.

### ________________________________________
#### 4.1.9 Funcionalidade: Cadastros – Rotas / Áreas / Regiões de Atendimento

Módulo:
### maxRoteirizador – Cadastros
Tabelas principais (ERP):
### • MXSROTAEXP
### • MXSPRACA
### • MXSREGIAO
### • MXSCIDADE
Tabelas principais (MXMP):
### • MXMP_ROTA_COMPLEMENTO
### • MXMP_COMPLEMENTO_ROTA
### • MXMP_AREAS_ATENDIMENTO
### • MXMP_REGIOES_ATENDIMENTO
### • MXMP_REGIOES_ENTREGA
Tabelas auxiliares (MXMP):
### • MXMP_AREAS_ATENDIMENTO_POLYLINE
### • MXMP_REGIOES_ATENDIMENTO_CIDADE
### • MXMP_REGIOES_ATENDIMENTO_PRACA
### • MXMP_REGIOES_ATENDIMENTO_ROTA
### • MXMP_REGIOES_CIDADES
### • MXMP_REGIAO_CLIENTE
Observações de suporte:
• Agrupamentos e filtros de roteirização usam essas tabelas combinadas com os pedidos em MXSHISTORICOPEDC/MXSHISTORICOPEDI.
• Se o agrupamento por rota/área/região não funciona:
o conferir vínculos em MXMP_REGIAO_CLIENTE;
o validar se os pedidos (MXSHISTORICOPEDC) têm rota/área/região preenchidos.
### ________________________________________
#### 4.1.10 Funcionalidade: XML / Excel – Importar XML de NF

Módulo:
### maxRoteirizador – XML / Excel
Tabelas principais (ERP):
### • MXSHISTORICOPEDC
### • MXSHISTORICOPEDI
### • MXSNFSAID
Tabelas auxiliares (MXMP):
### • MXMP_LOG_ERROS
Observações de suporte:
• Após a importação, pedidos/entregas relacionados alimentam MXSHISTORICOPEDC/MXSHISTORICOPEDI via fluxo do ERP.
### • Se nota/pedido não aparece para roteirização:
o validar se o XML foi importado (MXSNFSAID);
o checar se a integração posterior preencheu MXSHISTORICOPEDC/MXSHISTORICOPEDI corretamente.
### ________________________________________
#### 4.1.11 Funcionalidade: Mapas – Visualizar Clientes

Módulo:
### maxRoteirizador – Mapas
Tabelas principais (ERP):
### • MXSCLIENT
### • MXSCLIENTENDENT
Tabelas principais (MXMP):
### • MXMP_LOCALIZACAO_CLIENTE
### • MXMP_LOCALIZACAO_END_ENTREGA
Tabelas auxiliares (ERP):
### • MXSCIDADE
### • MXSPRACA
Observações de suporte:
• Se o cliente não aparece analisar na MXSCLIENT se tem vinculo com MXSCIDADE ________________________________________
#### 4.1.12 Funcionalidade: Relatórios – Resumo de Montagem

Módulo:
### maxRoteirizador – Relatórios
Tabelas principais (MXMP):
### • MXMP_ROMANEIO
### • MXMP_ROTA_ROMANEIO
### • MXMP_CUSTO_CARREGAMENTO
Tabelas principais (ERP):
### • MXSCARREG
### • MXSHISTORICOPEDC
### • MXSHISTORICOPEDI
Tabelas auxiliares (MXMP):
### • MXMP_CUSTO_ROMANEIO
Observações de suporte:
• Os resumos cruzam dados de romaneio/carga (MXMP_ROMANEIO/MXSCARREG) com pedidos/itens (MXSHISTORICOPEDC/MXSHISTORICOPEDI).
• Diferenças entre resumo e consultas geralmente estão ligadas a:
o filtros de período;
### o status de romaneio/carga;
o pedidos não vinculados corretamente.
### ________________________________________
#### 4.1.13 Funcionalidade: Relatórios – Lucratividade / Custo por Romaneio

Módulo:
### maxRoteirizador – Relatórios
Tabelas principais (MXMP):
### • MXMP_CUSTO_ROMANEIO
### • MXMP_CUSTO_ROMANEIO_FRETE
### • MXMP_CUSTO_ROMANEIO_TERCEIRIZADO
Tabelas principais (ERP):
### • MXSHISTORICOPEDC
### • MXSHISTORICOPEDI
### • MXSNFSAID
Tabelas auxiliares (MXMP):
### • MXMP_TABELA_FRETE
### • MXMP_CUSTO_CIDADE_FRETE
### • MXMP_CUSTO_FAIXA_FRETE
### • MXMP_FAIXA_TABELA_FRETE
### • MXMP_FAIXA_TRANSPORTADORA
Tabelas auxiliares (ERP):
### • MXSCOB
### • MXSREGIAO
Observações de suporte:
• A receita e o volume vêm de MXSHISTORICOPEDC/MXSHISTORICOPEDI/MXSNFSAID;
• Os custos vêm das tabelas MXMP_CUSTO_* e da Tabela de Frete.
• Se a lucratividade parecer incorreta:
o validar dados do pedido/nota nas tabelas MXSHISTORICOPEDC/MXSHISTORICOPEDI/MXSNFSAID;
o conferir regras de frete e custos configurados.
### ________________________________________
#### 4.1.14 Funcionalidade: Configurações – Usuários e Perfil de Acesso

Módulo:
### maxRoteirizador – Configurações
Tabelas principais (MXMP):
### • MXMP_USUARIOS
### • MXMP_PERFIL_ACESSO
### • MXMP_USUARIO_PERFIL_ACESSO
### • MXMP_PERMISSOES
### • MXMP_PERMISSOES_PERFIL
### • MXMP_PERMISSOES_USUARIO
Tabelas auxiliares (MXMP):
### • MXMP_USUARIOS_FILIAIS
### • MXMP_USUARIOS_ROTAS
### • MXMP_DADOS_USUARIO
### • MXMP_CD_USUARIO
Tabelas auxiliares (ERP):
### • MXSEMPR
Observações de suporte:
• Não usa diretamente MXSHISTORICOPEDC/MXSHISTORICOPEDI, mas o acesso às telas que consomem esses dados depende daqui.
### • Se usuário não enxerga funcionalidades relacionadas a pedidos/roteirização:
o revisar perfil de acesso e filial vinculada.
o Se o usuário não tem acesso a alguma tela deve ser vinculado aqui
### ________________________________________
#### 4.1.15 Funcionalidade: Configurações – Geração de Coordenadas / Geocode
Módulo:
### maxRoteirizador – Configurações
Tabelas principais (MXMP):
### • MXMP_SERVICO_GEOCODIFICACAO
### • MXMP_FILA_GEOCODE
### • MXMP_FALHA_GEOCODE
Tabelas auxiliares (MXMP):
### • MXMP_LOCALIZACAO_CLIENTE
### • MXMP_LOCALIZACAO_END_ENTREGA
### • MXMP_LOG_ERROS
Tabelas auxiliares (ERP):
### • MXSCLIENTENDENT
### • MXSCIDADE
Observações de suporte:
• Não lê diretamente MXSHISTORICOPEDC/MXSHISTORICOPEDI, mas impacta pedidos que dependem de localização para roteirização.
### • Se pedidos não entram em roteirização por problemas de endereço:
o conferir se geocode está ativo e sem falhas;
o verificar se clientes estão corretamente localizados.

### 4.2 MAXMOTORISTA – MAPA FUNCIONALIDADE X TABELAS

#### 4.2.1 Funcionalidade: Dashboard – Visão Tático Operacional / Nível de Serviço / Painel de Monitoramento

Módulo:
### maxMotorista – Portal Web (dashboards)
### Tabelas principais (ERP – origem dos pedidos/entregas):
### • MXSHISTORICOPEDC (pedidos)
### • ERP_MXSCARREG
### • MXSHISTORICOPEDI (itens do pedido)
• MXSNFSAID (notas fiscais de saída)
### Tabelas principais (MXMP – consolidação de entregas e posição):
### • MXMP_ENTREGAS
### • MXMP_ROMANEIO
### • MXMP_DADOS_ENTREGA_NOTA
### • MXMP_POSICAO_TATICO_OPERACIONAL
### • MXMP_TEMPO_CLIENTE
### • MXMP_NOTAS_FISCAIS
### • MXMP_APARELHOS
### • MXMP_ENDERECO_ENTREGA
Tabelas auxiliares (MXMP – visão gerencial / parâmetros):
### • MXMP_VISAO_GERENCIAL
### • MXMP_FILIAL_VISAO_GERENCIAL
### • MXMP_PRACA_VISAO_GERENCIAL
### • MXMP_ROTA_VISAO_GERENCIAL
### • MXMP_SLA_CLIENTE
### • MXMP_SLA_REDE
### • MXMP_SLA_REGIAO
### • MXMP_PARAMETROS
### • MXMP_PARAMETROS_FILIAL
Tabelas auxiliares (ERP):
### • MXSCLIENT
### • MXSCLIENTENDENT
### • MXSFILIAL
### • MXSPRACA
### • MXSROTAEXP
Observações de suporte:
• Os indicadores de OTIF, nível de serviço, atrasos e desempenho vêm da combinação:
### MXSHISTORICOPEDC/MXSHISTORICOPEDI/MXSNFSAID → MXMP_ENTREGAS → MXSROTAEXP.DIASENTREGA
• Se o dashboard não bate com consultas/relatórios:
### o conferir se a entrega existe em MXMP_ENTREGAS;
### o verificar se o histórico foi consolidado em MXMP_HISTORICO_ENTREGAS;
o validar filtros de data/filial.
### • Se o motorista não aparece no painel de monitoramento:
- Verificar se o carregamento na PCCARREG esta vinculado a ele
- Verificar se ele já realizou alguma sincronização pela mxmp_aparelhos.
### ________________________________________
#### 4.2.2 Funcionalidade: Consultas – Entregas

Módulo:
### maxMotorista – Portal Web (Consultas)
Tabelas principais (ERP):
### • MXSHISTORICOPEDC
### • MXSHISTORICOPEDI
### • MXSNFSAID
### • ERP_MXSCARREG
Tabelas principais (MXMP):
### • MXMP_ENTREGAS
### • MXMP_ROMANEIO
### • MXMP_NOTAS_FISCAIS
### • MXMP_DADOS_ENTREGA_NOTA
Tabelas auxiliares (MXMP):
### • MXMP_LOG_SITUACAO_ENTREGA_NOTA
### • MXMP_ENDERECO_ENTREGAS
Tabelas auxiliares (ERP):
### • MXSCLIENT
### • MXSCLIENTENDENT
### • MXSCIDADE
### • MXSFILIAL
Observações de suporte:
• Quase toda análise de “entrega não aparece” começa por MXMP_ENTREGAS + MXSHISTORICOPEDC/MXSNFSAID.
• Passos típicos:
### o validar se existe nota em MXSNFSAID e pedido em MXSHISTORICOPEDC;
### o checar se a procedure/job de entregas alimentou MXMP_ENTREGAS;
o se a tela mostra “entrega pendente”, analisar detalhes em MXMP_HISTORICO_ENTREGAS / MXMP_LOG_SITUACAO_ENTREGA_NOTA.
### ________________________________________
#### 4.2.3 Funcionalidade: Consultas – Listagem de Romaneios

Módulo:
### maxMotorista – Portal Web (Consultas)
Tabelas principais (ERP):
### • MXSHISTORICOPEDC
### • ERP_MXSCARREG
### • MXSHISTORICOPEDI
### • MXSNFSAID
Tabelas principais (MXMP):
### • MXMP_ROMANEIO
### • MXMP_ROTA_ROMANEIO
### • MXMP_ENTREGAS (entregas vinculadas ao romaneio)
Tabelas auxiliares (MXMP):
### • MXMP_HISTORICO_CARREGAMENTO
### • MXMP_CUSTO_ROMANEIO
### • MXMP_CUSTO_ROMANEIO_FRETE
Observações de suporte:
• Romaneio “some” da listagem quando:
o filtros de período/filial não incluem o dado;
o status do romaneio foi alterado (ex.: cancelado) e a tela filtra.
### o Job de entregas não rodou
### o Romaneio sem pedidos
• Para verificar se o romaneio está consistente:
o conferir MXMP_ROMANEIO;
### o listar pedidos/itens do romaneio via MXSHISTORICOPEDC/MXSHISTORICOPEDI;
o cruzar com entregas em MXMP_ENTREGAS.
### ________________________________________
#### 4.2.4 Funcionalidade: Consultas – Despesas (inclui Despesas do aplicativo)

Módulo:
### maxMotorista – Portal Web (Consultas)
Tabelas principais (MXMP):
### • MXMP_DESPESAS
### • MXMP_DESPESA_ABASTECIMENTO
### • MXMP_DESPESA_INFRACAO
Tabelas auxiliares (MXMP):
### • MXMP_TIPO_DESPESA
Observações de suporte:
• Se a despesa lançada no app não aparece no portal:
### o checar se existe registro em MXMP_DESPESAS com vínculo ao motorista/romaneio;
o validar se a sincronização do motorista foi concluída (MXMP_CONTROLE_SINC_MOTORISTA);
o conferir filtros de data/motorista na tela.
### ________________________________________
#### 4.2.5 Funcionalidade: Consultas – Hodômetros

Módulo:
### maxMotorista – Portal Web (Consultas)
Tabelas principais (MXMP):
### • MXMP_HODOMETROS
Tabelas principais (ERP):
### • ERP_MXSVEICUL
Tabelas auxiliares (MXMP):
### • MXMP_LANCAMENTOS_JORNADA
### • MXMP_HODOMETRO
### • MXMP_JORNADAS
### • MXMP_VEICULO_COMPLEMENTO
Observações de suporte:
• Se o hodômetro não aparece:
o conferir lançamentos em MXMP_HODOMETROS;
o verificar se o registro foi feito em jornada correta (MXMP_LANCAMENTOS_JORNADA + motorista);
o validar se a sincronização do motorista foi concluída (MXMP_CONTROLE_SINC_MOTORISTA);
o Pegar a base do motorista, usuário e senha e importar para tentar sincronizar e analisar ela.
o checar se o veículo está ativo e corretamente vinculado.
### ________________________________________
#### 4.2.6 Funcionalidade: Consultas – Recebíveis

Módulo:
### maxMotorista – Portal Web (Consultas)
Tabelas principais (MXMP):
### • MXMP_RECEBIVEIS
Tabelas principais (ERP):
• MXSPREST (quando existe vínculo com prestação/título)
Observações de suporte:
• Se o recebível não aparece ou não baixa:
### • Validar se de fato o motorista sincronizou

### ________________________________________
#### 4.2.7 Funcionalidade: Consultas – Log de Sincronização do Motorista
Módulo:
### maxMotorista – Portal Web (Consultas)
Tabelas principais (MXMP):
### • MXMP_CONTROLE_SINC_MOTORISTA
### • MXMP_FALHA_SINCRONIZACAO
Tabelas auxiliares (MXMP):
### • MXMP_USUARIOS
Observações de suporte:
• Quando o motorista diz que “não apareceu entrega nova / não subiu ocorrência / despesa”:
### o sempre consultar MXMP_CONTROLE_SINC_MOTORISTA;
o se houver falha, analisar detalhes em MXMP_FALHA_SINCRONIZACAO / MXMP_LOG_ERROS;
o CONFERIR NA MXMP_ENTREGAS se possui data de sincronização.
### o Conferir se gerou as entregas corretamente
o Conferir se tem registro de nota na mxmp_NOTAS_FISCAIS E NA MXSMOV
### o Conferir se o carregamento esta de fato para o motorista
### o Pegar a base do motorista para conectar no banco e analisar
o confirmar horário da última sincronização com o horário das integrações.
### ________________________________________
#### 4.2.8 Funcionalidade: Mapas – Monitoramento de Entregas / Monitoramento do Motorista

Módulo:
### maxMotorista – Portal Web (Mapas)
Tabelas principais (MXMP):
### • MXMP_LOCALIZACAO_MOTORISTA
### • MXMP_ROMANEIO
### • MXMP_ENTREGAS
### • MXMP_LOCALIZACAO_CLIENTE
### • MXMP_LOCALIZACAO_END_ENTREGA
### • MXMP_ENTREGAS
Tabelas principais (ERP):
### • MXSCLIENT
### • MXSCLIENTENDENT
Tabelas auxiliares (MXMP):
### • MXMP_TEMPO_CLIENTE
Observações de suporte:
### • Se o motorista não aparece no mapa:
### o checar MXMP_ENTREGAS (últimos pontos);
### o Verificar se o usuário é responsável pelo motorista
o validar se está sincronizando normalmente (ver também log de sincronização).
### ________________________________________
#### 4.2.9 Funcionalidade: Ocorrências (gerenciamento de ocorrências – devolução, reagendamento, furo de sequência, canhoto)

Módulo:
### maxMotorista – Portal Web (Ocorrências)
Tabelas principais (MXMP):
### • MXMP_OCORRENCIAS
### • MXMP_ENTREGAS
### • MXMP_HISTORICO_OCORRENCIA
### • MXMP_DEVOLUCOES
### • MXMP_DESCARGA_CANCELADA
### • MXMP_DESCARGA_REAGENDADA
### Tabelas principais (ERP – base da entrega/pedido):
### • MXSHISTORICOPEDC
### • MXSHISTORICOPEDI
### • MXSNFSAID
### • MXSMOV
Tabelas auxiliares (MXMP – motivos / classificações):
### • MXMP_MOTIVO_OCORRENCIA
### • MXMP_MOTIVO_REAGENDAMENTO
### • MXMP_MOTIVO_DE_CANHOTO
### • MXMP_MOTIVO_CANCELAMENTO
### • MXMP_TIPOS_DEVOLUCAO
### • MXMP_MOTIVO_FURO_SEQUENCIA
Observações de suporte:
• Se uma ocorrência foi registrada no app e não aparece no portal:
o validar registro em MXMP_OCORRENCIAS / MXMP_HISTORICO_OCORRENCIA;
### o conferir se a sincronização do motorista foi concluída;
o checar se a nota/pedido vinculado existe nas MXSHISTORICOPEDC/PEDI e MXSNFSAID.
### ________________________________________
#### 4.2.10 Funcionalidade: Autorizações – Entrega fora do raio

Módulo:
### maxMotorista – Portal Web (Autorizações)
Tabelas principais (MXMP):
### • MXMP_PARAMETROS
### • MXMP_ENDERECO_ENTREGA
### • MXMP_ENTREGAS

Observações de suporte:
### • Quando o motorista não consegue realizar entrega por “fora do raio”:
o validar parâmetros de raio/restrição em MXMP_PARAMETROS;
o checar se o cliente está corretamente geolocalizado;
### ________________________________________
#### 4.2.11 Funcionalidade: Cadastros – Jornadas, Horários de Trabalho, Ausências

Módulo:
### maxMotorista – Portal Web (Cadastros)
Tabelas principais (MXMP):
### • MXMP_JORNADAS
### • MXMP_HORARIOS_TRABALHO
### • MXMP_TIPO_AUSENCIA
### • MXMP_AUSENCIA
Tabelas auxiliares (MXMP):
### • MXMP_LANCAMENTOS_JORNADA
### • MXMP_DESCANSO_JORNADA
### • MXMP_LOG_REGISTRO_JORNADA
### • MXMP_DADOS_USUARIO
### • MXMP_USUARIOS
Tabelas auxiliares (ERP):
### • MXSEMPR (motoristas/usuários base)
Observações de suporte:
### • Se o motorista não consegue iniciar/finalizar jornada:
o conferir se existe jornada ativa em MXMP_JORNADAS;
o verificar se os horários de trabalho estão configurados;
### o Conferir se a jornada esta vinculada ao motorista na MXMP_USUARIOS
o checar eventuais bloqueios por ausência/descanso.
### ________________________________________
#### 4.2.12 Funcionalidade: Relatórios – Registros de Jornadas / Tempo / Desempenho Motorista

Módulo:
### maxMotorista – Portal Web (Relatórios)
Tabelas principais (MXMP):
### • MXMP_LANCAMENTOS_JORNADA
### • MXMP_JORNADAS
### • MXMP_TEMPO_MEDIO_ATIVIDADE
### • MXMP_TEMPO_CLIENTE
### • MXMP_RAKING_MOTORISTA
### • MXMP_ROMANEIO
Tabelas auxiliares (MXMP):
### • MXMP_DESCANSO_JORNADA
### • MXMP_LOG_REGISTRO_JORNADA
### • MXMP_ENTREGAS
Tabelas auxiliares (ERP):
### • MXSEMPR
### • ERP_MXSVEICUL
Observações de suporte:
• Divergências de tempo/jornada geralmente vêm de:
o registros em duplicidade ou ausentes em MXMP_LANCAMENTOS_JORNADA;
### o motorista esquecendo de iniciar/encerrar jornada;
o ajustes manuais de jornada.
### ________________________________________

#### 4.2.13 Funcionalidade: Cadastros – Motivos (Devolução, Cancelamento, Reagendamento, Furo de sequência, Canhoto)

Módulo:
### maxMotorista – Portal Web (Cadastros)
Tabelas principais (MXMP):
### • MXMP_MOTIVO_CANCELAMENTO
### • MXMP_MOTIVO_DE_CANHOTO
### • MXMP_MOTIVO_FURO_SEQUENCIA
### • MXMP_MOTIVO_OCORRENCIA
### • MXMP_MOTIVO_REAGENDAMENTO
### • MXMP_TIPOS_DEVOLUCAO
Observações de suporte:
• Motivos definidos aqui influenciam diretamente:
### o o que o motorista consegue selecionar no app;
o como as ocorrências são classificadas nos relatórios.
o Tipos de devoluções
### • Se o motorista não encontra o motivo correto:
o checar se o motivo está ativo;
o validar se está vinculado à funcionalidade correta (devolução, reagendamento, etc.).
### ________________________________________
#### 4.2.14 Funcionalidade: Configurações – Usuários, Perfis de Acesso, Portal, Aplicativo

Módulo:
### maxMotorista – Portal Web (Configurações)
Tabelas principais (MXMP):
### • MXMP_USUARIOS
### • MXMP_PERFIL_ACESSO
### • MXMP_USUARIO_PERFIL_ACESSO
### • MXMP_PERMISSOES
### • MXMP_PERMISSOES_PERFIL
### • MXMP_PERMISSOES_USUARIO
Tabelas auxiliares (MXMP):
### • MXMP_USUARIOS_FILIAIS
### • MXMP_DADOS_USUARIO
### • MXMP_PARAMETROS
Tabelas auxiliares (ERP):
### • MXSEMPR
Observações de suporte:
### • Se o usuário não enxerga telas de maxMotorista:
o revisar permissões em MXMP_PERFIL_ACESSO e MXMP_PERMISSOES_*;
o checar filial vinculada em MXMP_USUARIOS_FILIAIS;
o validar se o usuário está ativo e corretamente associado a motorista (quando aplicável).
• É nesta tela de aplicativo e portal que fica armazenado todas as parametrizações
### ________________________________________
#### 4.2.15 Funcionalidade: Configurações – E-mail, Rastreador, Logo da Empresa

Módulo:
### maxMotorista – Portal Web (Configurações)
Tabelas principais (MXMP):
### • MXMP_CONFIGURACAO_EMAIL
### • MXMP_RASTREADOR
### • MXMP_LOGO_EMPRESA
Observações de suporte:
• Afeta:
o envio de e-mails de canhoto/comprovante;
o integração com rastreador de veículo;
o exibição de branding no portal/app.
• Se e-mail/canhoto não é enviado:
checar MXMP_CONFIGURACAO_EMAIL;

### TABELAS APLICATIVO

### MXMD_AGENDAMENTO
### MXMD_AJUDANTES
### MXMD_AUSENCIA
### MXMD_CARREGAMENTOS
### MXMD_CLIENTES
### MXMD_COB_PREVISTAS
### MXMD_CONTROLE_SINC
### MXMD_DESCANSO_JORNADA
### MXMD_DESCARGA_CANCELADA
### MXMD_DESCARGA_REAGENDADA
### MXMD_DESPESAS
### MXMD_ENTREGAS
### MXMD_EVENTOS
### MXMD_EVENTO_ENTREGA
### MXMD_FILIAIS
### MXMD_FOTOS
### MXMD_HISTORICO_OCORRENCIA
### MXMD_HIST_ACEITE_FRETE
### MXMD_HODOMETROS
### MXMD_INFO_TRANSBORDO
### MXMD_INTRAJORNADA
### MXMD_ITEM_COMODATO
### MXMD_ITEM_OCORRENCIA
### MXMD_ITENS_NOTA_FISCAL
### MXMD_JANELA_ENTREGA
### MXMD_LANCAMENTOS_JORNADA
### MXMD_LANC_COMODATO
### MXMD_LOCALIZACAO
### MXMD_LOG_CONEXAO
### MXMD_MARKER_ROMANEIO
### MXMD_MOTIVO_CANCELAMENTO
### MXMD_MOTIVO_DE_CANHOTO
### MXMD_MOTIVO_FURO_SEQUENCIA
### MXMD_MOTIVO_OCORRENCIA
### MXMD_MOTIVO_REAGENDAMENTO
### MXMD_MOTORISTAS_PREPOSTOS
### MXMD_NOTAS_FISCAIS
### MXMD_NOTA_REENTREGA
### MXMD_OCORRENCIAS
### MXMD_PARCELAMENTO
### MXMD_POLYLINE
### MXMD_PONTO_PARADA
### MXMD_PRODUTOS
### MXMD_PRODUTOS_VOLUMES_ENTREGAS
### MXMD_RASTRO
### MXMD_RCA
### MXMD_ROMANEIO
### MXMD_SUPERVISORES
### MXMD_TEMPO_SEMANA
### MXMD_TIPO_DESPESA
### MXMD_TIPO_EVENTO
### MXMD_TITULOS
### MXMD_TOUR
### MXMD_VOLUMES
### MXMD_VOLUMES_CONF_ENT
### MXMD_VOLUMES_ENTREGAS
### MXMD_VOLUMES_ENT_CONF_TEMP
### MXMI_COBRANCAS
### MXMI_CONTATOS
### MXMI_MOTIVOS_DEVOLUCAO
### MXMP_CONTATOS
### MXMP_ENDERECO_ENTREGAS
### MXMP_ITEM_SOLICITACAO
### MXMP_NOTIFICACAO_PORTAL
### MXMP_PARAMETROS
### MXMP_RECEBIVEIS
### MXMP_SOLICITACOES
### MXMP_USUARIOS
android_metadata

### TABELAS INTEGRAÇÃO

MXSATIVI
MXSCIDADE
MXSCLIENT
MXSCLIENTENDENT
MXSULTCOMPCLIENTE
MXSCOB
MXSCONTATO
MXSEMPR
MXSFILIAL
MXSHISTORICOPEDC
MXSHISTORICOPEDI
MXSHISTORICOPEDCORTE
MXSHISTORICOPEDFALTA
MXSDOCELETRONICO
MXSNFSAID
ERP_MXSMOV
MXSPLPAG
MXSPRACA
ERP_MXSPREST
MXSPRODUT
MXSREGIAO
MXSROTAEXP
MXSSUPERV
MXSCARREG
MXSUSUARI
ERP_MXSVEICUL

### TABELAS WEB MOTORISTA/ROTEIRIZADOR

### MXMP_AGENDA_DINAMICA
### MXMP_AGENDAMENTO
### MXMP_AJUDANTE_COMPLEMENTO
### MXMP_AJUDANTE_CUSTO_FRETE
### MXMP_APARELHOS
### MXMP_APK
### MXMP_AREAS_ATENDIMENTO
### MXMP_AREAS_ATENDIMENTO_DIA
### MXMP_AREAS_ATENDIMENTO_FILIAL
### MXMP_AREAS_ATENDIMENTO_POLYLINE
### MXMP_AREAS_ATENDIMENTO_VEICULO
### MXMP_ARQUIVOS
### MXMP_AUSENCIA
### MXMP_BAIXA_CARREGAMENTO
### MXMP_BANCO_LOGISTICA
### MXMP_BASE_CALC_INFRACAO
### MXMP_BASE_CARREGAMENTO
### MXMP_BASE_OCORRENCIAS
### MXMP_CAD_SEFAZ
### MXMP_CANCELAMENTO_CHECKIN
### MXMP_CARACTERISTICAS_COMPLEMENTO
### MXMP_CARACTERISTICAS_FILIAIS
### MXMP_CARACTERISTICAS_VEICULO
### MXMP_CARACTERISTICAS_VEICULO_FILIAL
### MXMP_CARREGAMENTO_CROSSDOCKING
### MXMP_CARREGAMENTO_LOG
### MXMP_CARREGAMENTO_TEMPORARIO
### MXMP_CARREGAMENTO_TRANSBORDO
### MXMP_CARREG_ENTREGA_INATIVO
### MXMP_CARTEIRIZACAO
### MXMP_CATEGORIA_PECAS_INSUMOS
### MXMP_CATEGORIA_SERVICO
### MXMP_CD_USUARIO
### MXMP_CENTROS_DISTRIBUICAO
### MXMP_CERT_DIGITAL
### MXMP_CIDADE_TABELA_FRETE
### MXMP_CLIENTE_CENTRO_DISTRIBUICAO
### MXMP_CLIENTE_COMPLEMENTO
### MXMP_COD_END_FRETE_TRANSP_PED
### MXMP_CODIGO_INFRACAO
### MXMP_CODIGO_RASTREIO_PEDIDO
### MXMP_COMBUSTIVEL
### MXMP_COMPLEMENTO_ROTA
### MXMP_CONEXOES
### MXMP_CONFIG_EXIBICAO_CAMPOS
### MXMP_CONFIG_EXIBICAO_CAMPOS_ITEM
### MXMP_CONFIG_FILTRO_CORES
### MXMP_CONFIG_MAXENTREGAS
### MXMP_CONFIGURACAO_EMAIL
### MXMP_CONFIGURACAO_ROTEIRIZACAO
### MXMP_CONFIGURACAO_VISITAS_RCA
### MXMP_CONFIG_VISAO_USUARIO
### MXMP_CONTATOS
### MXMP_CONTROLE_EMAIL_ENTREGA
### MXMP_CONTROLE_NOTA
### MXMP_CONTROLE_SINC_MOTORISTA
### MXMP_CORES
### MXMP_COTACAO_FORNECEDORES
### MXMP_CUSTO_CARREGAMENTO
### MXMP_CUSTO_CIDADE_FRETE
### MXMP_CUSTO_ENTREGA
### MXMP_CUSTO_FAIXA_FRETE
### MXMP_CUSTO_MONTAGEM
### MXMP_CUSTO_ROMANEIO
### MXMP_CUSTO_ROMANEIO_FRETE
### MXMP_CUSTO_ROMANEIO_TERCEIRIZADO
### MXMP_DADOS_ENTREGA_NOTA
### MXMP_DADOS_PERFIL
### MXMP_DADOS_USUARIO
### MXMP_DESCANSO_JORNADA
### MXMP_DESCARGA_CANCELADA
### MXMP_DESCARGA_REAGENDADA
### MXMP_DESPESA_ABASTECIMENTO
### MXMP_DESPESA_INFRACAO
### MXMP_DESPESAS
### MXMP_DEVOLUCOES
### MXMP_DIA_MONTAGEM
### MXMP_DIA_MONTAGEM_CARGA_CLIENTE
### MXMP_DIAS_ENT_CIDADE_EMITENTE
### MXMP_DISPOSICAO_GRID_PEDIDOS
### MXMP_ENDERECO_ENTREGAS
### MXMP_ENDERECO_HIERARQUIA
### MXMP_ENTREGAS
### MXMP_EVENTOS
### MXMP_FAIXA_TABELA_FRETE
### MXMP_FAIXA_TRANSPORTADORA
### MXMP_FALHA_GEOCODE
### MXMP_FALHA_SINCRONIZACAO
### MXMP_FILA_GEOCODE
### MXMP_FILA_MENSAGEM
### MXMP_FILA_ROTEIRIZACAO
### MXMP_FILA_VERI_SEFAZ
### MXMP_FILIAIS_VEICULOS
### MXMP_FILIAL_COTACAO_FORNECEDORES
### MXMP_FILIAL_PLANO_MANUTENCAO
### MXMP_FILIAL_ROTA_COMP
### MXMP_FILIAL_TABELA_FRETE
### MXMP_FILIAL_VISAO_GERENCIAL
### MXMP_FOTOS
### MXMP_GRUPO_RAMO_ATIVIDADE
### MXMP_HIERARQUIA_ENTREGA
### MXMP_HIST_ACEITE_FRETE
### MXMP_HISTORICO_CARREGAMENTO
### MXMP_HISTORICO_ENTREGAS
### MXMP_HISTORICO_OCORRENCIA
### MXMP_HISTORICO_TANQUE_COMBUSTIVEL
### MXMP_HIST_REENTREGA_CARREGAMENTO
### MXMP_HODOMETROS
### MXMP_HORARIOS_TRABALHO
### MXMP_HORARIOS_TRABALHO_ITENS
### MXMP_IDENTIFICACAO_PERSONALIZADA_ENTREGA
### MXMP_INFO_CROSSDOCKING
### MXMP_INFO_TRANSBORDO
### MXMP_ITEM_COTACAO_FORNECEDORES
### MXMP_ITEM_MANUTENCAO
### MXMP_ITEM_OCORRENCIA
### MXMP_ITEM_PLANO_MANUTENCAO
### MXMP_ITEM_SOLICITACAO
### MXMP_ITENS_COMODATOS
### MXMP_JANELA_ENTREGA
### MXMP_JORNADAS
### MXMP_LANCAMENTOS_JORNADA
### MXMP_LANC_COMODATO
### MXMP_LINK
### MXMP_LOCALIZACAO_CLIENTE
### MXMP_LOCALIZACAO_CLIENTE_VENDA
### MXMP_LOCALIZACAO_END_ENTREGA
### MXMP_LOCALIZACAO_MOTORISTA
### MXMP_LOCALIZACAO_RCA
### MXMP_LOG_ALTER_ARQUIVO
### MXMP_LOG_BAIXA_TITULO_SINC
### MXMP_LOG_DIST_AUTO
### MXMP_LOG_ERP_MXSCARREG
### MXMP_LOG_ERROS
### MXMP_LOG_MONTAGEM_AUTOMATICA
### MXMP_LOG_MOTORISTA_PREPOSTO
### MXMP_LOG_NUMSEQ_NFSAID
### MXMP_LOGO_EMPRESA
### MXMP_LOG_OPERACOES_ROMANEIO_ERP
### MXMP_LOG_OP_LOGISTICA
### MXMP_LOG_REGISTRO_JORNADA
### MXMP_LOG_SITUACAO_ENTREGA_NOTA
### MXMP_LOG_TRANSF
### MXMP_MANUTENCAO
### MXMP_MARCA_PECAS_INSUMOS
### MXMP_MAXPAG_COB
### MXMP_MAXPAG_LINK
### MXMP_MAXPAG_MOV
### MXMP_MAXPAG_TOKEN
### MXMP_MOTIVO_CANCELAMENTO
### MXMP_MOTIVO_DE_CANHOTO
### MXMP_MOTIVO_FURO_SEQUENCIA
### MXMP_MOTIVO_OCORRENCIA
### MXMP_MOTIVO_REAGENDAMENTO
### MXMP_MOTIVO_TRANSF
### MXMP_MOTORISTA_COMPLEMENTO
### MXMP_MOTORISTA_OMNILINK
### MXMP_MOTORISTAS_PREF_ROTA
### MXMP_MOTORISTAS_PREPOSTOS
### MXMP_NOTA_REENTREGA
### MXMP_NOTAS_FISCAIS
### MXMP_NOTIFICACAO
### MXMP_NOTIFICACAO_CARREGAMENTO
### MXMP_NOTIFICACAO_PORTAL
### MXMP_NOTIFICACAO_ROTEIRIZADOR
### MXMP_OCOREN
### MXMP_OCOREN_ARQUIVO
### MXMP_OCOREN_CODIGO_OCORRENCIA
### MXMP_OCOREN_ENTREGA
### MXMP_OCOREN_OCORRENCIA
### MXMP_OCOREN_TRANSPORTADORA
### MXMP_OCORRENCIAS
### MXMP_OPERADORA_VALE_PEDAGIO
### MXMP_PALAVRA_CHAVE
### MXMP_PARAMETROS
### MXMP_PARAMETROS_CALCULO
### MXMP_PARAMETROS_FILIAL
### MXMP_PARAMETROS_OMNILINK
### MXMP_PARAMETROS_RESTRICAO
### MXMP_PARAMETROS_USUARIO
### MXMP_PECAS_INSUMOS
### MXMP_PEDIDO_CROSSDOCKING
### MXMP_PERFIL
### MXMP_PERFIL_ACESSO
### MXMP_PERFIL_ACESSO_PERMISSAO
### MXMP_PERFIL_ROTEIRIZACAO
### MXMP_PERMISSAO
### MXMP_PERMISSOES
### MXMP_PERMISSOES_PERFIL
### MXMP_PERMISSOES_USUARIO
### MXMP_PLANEJAMENTO_VISITAS_RCA
### MXMP_PLANO_CONTA
### MXMP_PLANO_GRUPO
### MXMP_PLANO_MANUTENCAO
### MXMP_PONTO_PARADA
### MXMP_PONTO_PARADA_ROMANEIO
### MXMP_PONTOS_REFERENCIA
### MXMP_POSICAO_TATICO_OPERACIONAL
### MXMP_PRACA_TABELA_FRETE
### MXMP_PRACA_VISAO_GERENCIAL
### MXMP_PRE_ACERTO_MOTORISTA
### MXMP_PROBLEM_JSON
### MXMP_RAKING_MOTORISTA
### MXMP_RAMO_ATIVIDADE
### MXMP_RAMO_ATIVIDADE_COMPLEMENTO
### MXMP_RASTREADOR
### MXMP_RECEBIVEIS
### MXMP_REGIAO
### MXMP_REGIAO_CLIENTE
### MXMP_REGIOES
### MXMP_REGIOES_ATENDIMENTO
### MXMP_REGIOES_ATENDIMENTO_CIDADE
### MXMP_REGIOES_ATENDIMENTO_PRACA
### MXMP_REGIOES_ATENDIMENTO_ROTA
### MXMP_REGIOES_CIDADES
### MXMP_REGIOES_ENTREGA
### MXMP_REGIOES_ENTREGA_ROTAS
### MXMP_REGISTRO_PONTO_PARADA
### MXMP_REJEICAO_ROTA_AUTO
### MXMP_REPROCESSAR_ROMANEIO_CD
### MXMP_RESPONSAVEL_MOTORISTA
### MXMP_RODIZIO_DIA_SEMANA
### MXMP_RODIZIO_FINAL_PLACA
### MXMP_RODIZIO_ROTA
### MXMP_ROMANEIO
### MXMP_ROTA_COMPLEMENTO
### MXMP_ROTA_MONTAGEM_COMPLEMENTO
### MXMP_ROTA_ROMANEIO
### MXMP_ROTA_SEQUENCIA
### MXMP_ROTA_SEQUENCIA_BKP
### MXMP_ROTAS_TRANSPORTADORA
### MXMP_ROTA_TABELA_FRETE
### MXMP_ROTA_VISAO_GERENCIAL
### MXMP_ROTEIRIZACAO
### MXMP_ROTEIRIZACAO_DIA_SEMANA
### MXMP_ROTEIRIZACAO_LOG_RCA
### MXMP_ROTEIRIZACAO_PEDIDO
### MXMP_ROTEIRIZACAO_RCA
### MXMP_ROTEIRIZACAO_RCA_SEQ
### MXMP_ROTEIRIZADOR_CONFIG
### MXMP_SEGMENTO
### MXMP_SEGMENTO_CLIENTE
### MXMP_SEM_PARAR_PRACA_PEDAGIO
### MXMP_SEQUENCIA_DINAMICA
### MXMP_SERVICO_GEOCODIFICACAO
### MXMP_SERVICO_ROTEIRIZACAO
### MXMP_SLA_CLIENTE
### MXMP_SLA_REDE
### MXMP_SLA_REGIAO
### MXMP_SOLICITACOES
### MXMP_SOLUCAO
### MXMP_SOLUCAO_ROTEIRIZACAO
### MXMP_SUB_PERMISSOES
### MXMP_SUB_PERMISSOES_PERFIL
### MXMP_TABELA_FRETE
### MXMP_TAEMROTA_RESTRICAO_CODCOB
### MXMP_TAEMROTA_RESTRICAO_ORIGEM_PEDIDO
### MXMP_TANQUE_COMBUSTIVEL
### MXMP_TEMP_CARREG_KMINICIAL
### MXMP_TEMPLATE_WHATSAPP
### MXMP_TEMP_LOG_PEDC_NUMSEQENTREGA
### MXMP_TEMPO_CLIENTE
### MXMP_TEMPO_MEDIO_ATIVIDADE
### MXMP_TESTE
### MXMP_TIME_LINE
### MXMP_TIPO_AUSENCIA
### MXMP_TIPO_CARGA
### MXMP_TIPO_DESPESA
### MXMP_TIPO_EVENTO
### MXMP_TIPO_JUSTIFICATIVA
### MXMP_TIPO_NOTIFICACAO_CARREGAMENTO
### MXMP_TIPOS_DEVOLUCAO
### MXMP_TIPO_SERVICO
### MXMP_TIPO_TEMPLATE_WHATSAPP
### MXMP_TIPO_VEICULO
### MXMP_TIPO_VENDA_TABELA_FRETE
### MXMP_TOKEN_VALIDACAO
### MXMP_TOUR
### MXMP_TOUR_USUARIO
### MXMP_TRANSPORTADORA
### MXMP_USUARIO_PERFIL_ACESSO
### MXMP_USUARIOS
### MXMP_USUARIOS_ACESSO
### MXMP_USUARIOS_FILIAIS
### MXMP_USUARIOS_ROTAS
### MXMP_USUARIO_VISAO_GERENCIAL
### MXMP_VEICULO_COMPLEMENTO
### MXMP_VEICULO_COTACAO_FORNECEDORES
### MXMP_VEICULO_INDISPONIBILIDADE
### MXMP_VEICULO_RASTREADOR
### MXMP_VEICULOS_PREF_ROTA
### MXMP_VERSAO_LOGISTICA
### MXMP_VISAO_GERENCIAL
### MXMP_VOLUMES_CONF_ENT
