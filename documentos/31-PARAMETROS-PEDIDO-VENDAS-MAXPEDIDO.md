# Parametros Pedido de Vendas e MaxPedido

## Metadados

**Palavras-chave**: parametros, pedido de vendas, maxPedido, MXSCONFIGDATA, MXSPARAMETRO, rotina 132, Winthor, configuracao

**Sistema**: maxPedido / Pedido de Vendas / Winthor

**Area**: Configuracao e Parametros

---

## Escopo

Este documento consolida os parametros extraidos para a categoria Pedido de Vendas e MaxPedido, incluindo parametros da rotina 132 do Winthor e parametros das tabelas MXSCONFIGDATA / MXSPARAMETRO.

Campos principais: nome do parametro, tipo e descricao.

---

## Parametros da Rotina 132

| Codigo / titulo | Parametro | Tipo | Descricao |
|---|---|---|---|
| 1020 - Prazo de validade do Orçamento | `CON_PRAZOVALIDADEORCAMENTO` | NUMBER | Este campo define por quantos dias o orçamento poderá ser usado após a sua criação na rotina 316. |
| 1094 - % máximo para exceder o limite de crédito | `CON_PEREXCEDELIMCRED` | NUMBER | % máximo permitido para exceder o limite de credito do cliente na venda. |
| 1074 - Validar preço na bonificação | `CON_VALIDAPVENDABONIFIC` | S/N | Validar o preço de venda na digitação de pedido de venda de bonificação ou troca. |
| 1078 - Plano de pagamento inicial | `CON_CODPLPAGINICIAL` | NUMBER | Define o plano de pagamento padrão ao cadastrar clientes pelo força de vendas. |
| 1116 - Aceita venda balcão com estoque negativo | `CON_ACEITAVENDABALCAOESTNEG` | S/N | Desabilita na rotina 316 a validação de estoque disponível caso a filial do pedido seja Autosserviço. Isto é, o parâmetro 1619 deve ser Sim. |
| 1182 - Preço de venda para mercadorias a retirar nos tipos de venda 11 e 12 | `CON_USATROCACOMPRECOVENDA` | S/N | O padrão do Winthor nas trocas dos tipos de venda 11 e 12 é gravar as mercadorias a retirar com custo financeiro. Este parâmetro permite usar o custo financeiro ao invés de usar o próprio preço de venda da mercadoria. No força de vendas é utilizado para c |
| 1224 - Separar pedidos que possuam produtos com restrição de transporte | `CON_SEPARARPRODCOMRESTRICAOTRANSP` | S/N | Este parâmetro indica que na inclusão de um pedido de venda todos os produtos que possuam restrição de transporte serão separados em um novo pedido, porém com os mesmos dados do pedido original (Cliente, Vencimento, Plano de Pagamento). Trabalha em conjun |
| 1337 - Valor máximo para pessoa física (/Mês) (reais) | `CON_VLMAXVENDAPF` | S/N | Valor máximo que pode ser realizado para pessoa física noa Mês |
| 1429 - Aceitar pedido de venda Bloqueado | `CON_ACEITAVENDABLOQ` | S/N | Indica se aceita pedidos de venda bloqueados. Se Sim, irá fazer com que pedidos com alguma ressalva entrem Bloqueados no Winthor. Se Não, fará com que o pedido seja rejeitado pelo Winthor, não será gravado. |
| 1455 - Usar crédito de RCA | `CON_USACREDRCA` | S/N | Usar crédito de conta corrente de RCA. |
| 1494 - Opção de arredondamento para o cálculo de SUFRAMA | `CON_TIPOCALCSULFRAMA` | TEXT | Tipo de cálculo do desconto SUFRAMA. Este parâmetro permite definir com quantas casas decimais será gravado do Desconto SUFRAMA. |
| 1105 - somar quantidade na venda | `CON_SOMAQTPEDVENDA` | S/N | inexistente |
| 1526 - Permitir digitar o mesmo item no pedido | `CON_USACHAVETRIPLAPCPEDI` | S/N |  |
| 1550 - Usar déb./créd. RCA nas trocas (TV11 e TV12) | `CON_TROCAALTDEBCREDRCA` | S/N | As vendas bonificadas devem alterar o saldo de débito/crédito do RCA. |
| 1881 - Cálculo de IPI | `CON_TIPOCALCIPI` | TEXT | Tipo de cálculo do IPI. Este parâmetro permite definir com quantas casas decimais será gravado o IPI. |
| 1891 - Aceitar desconto no preço fixo | `CON_ACEITADESCPRECOFIXO` | S/N | Aceita desconto no preço fixo. |
| 1073 - Permitir alterar pl. pagto na venda | `CON_PERMITEALTPLPAGVENDA` | S/N | Indica se permite alterar o plano de pagamento na digitação do pedido de venda. "Impacta na alteração do pedido para Bonificação" |
| 1942 - Aceitar desconto maior que o flexível no telemarketing | `CON_ACEITADESCTMK` | S/N | O pedido com desconto maior que o flexível ficará na posição bloqueado. Esse maxsuporte é geral, existe o por filial 2551 - ACEITADESCTMKFV |
| 2172 - Permitir acréscimo na venda com preço fixo | `CON_ACEITAACRESCIMOPRECOFIXO` | S/N | Permitir acréscimo na venda com preço fixo. |
| 2207 - Bloquear pedido de venda abaixo do valor mínimo | `FIL_BLOQUEARPEDIDOSABAIXOVLMINIMO` | S/N |  |
| 2236 - Permitir informar profissional na venda | `FIL_INFORMARPROFISSIONALVENDA` | S/N | Exibe / Oculta as informações da Comissão Por Profissional do cabeçalho da confecção do pedido de venda (Chamado: 853354) |
| 2512 - Separar pedidos que possuam | `SEPARARPRODCOMRESTRICAOTRANSP` | S/N | Este parâmetro indica que na inclusão de um pedido de venda todos |
| 2697 - Bloquear pedidos com valor acima do limite de crédido do cliente no FV | `BLOQPEDLIMCRED` | S/N | Caso o valor do pedido vindo do Força de Vendas, seja superior ao valor de limite de crédito. Este parâmetro é independente do 1429, e trata de forma separada os assuntos relacionados a clientes bloqueados dos sem limite de crédito ou com limite insuficie |
| 2805 - Utilizar venda por grade | `VENDAPORGRADE` | S/N | Habilita/Desabilita a venda de produtos por grade. Com esta opção marcada o sistema fará baixa de estoque apenas de produtos principais. |
| Permitir digitar pedido de cliente com bloqueio SEFAZ | `VERIFICABLOQUEIOSEFAZ` | S/N | Parâmetro permite ou não que usuário digite pedido de venda de cliente com restrição no SEFAZ. |
| Ao iniciar pedido escolhe o tipo de documento: Cupom ou Nota Fiscal | `DEFINIRTIPODOCVENDA` | S/N | Ao iniciar pedido escolhe o tipo de documento: Cupom ou Nota Fiscal |
| 1131 - Utilizar restrição de fornecedores por RCA | `CON_UTILIZAPCUSURFORNEC` | S/N | inexistente |

---

## Parametros MXSCONFIGDATA / MXSPARAMETRO

| Parametro | Tipo | Descricao |
|---|---|---|
| `CATALOGO_APAGA_ARQUIVOS_TEMP` | S/N | Apaga arquivos temporarios do Catálogo no aparelho. |
| `CATALOG_APRESENTA_IMAGEM_ESTOQUE` | S/N | Catálogo apresenta somente fotos de produtos que tenham estoque (caso esteja como S e o RCA não tenha clientes no FV ou não tenha o aplicativo do FV instalado, o Catálogo não exibe foto de nenhum produto). |
| `CATALOG_CAN_INPUT_QUANTITY` | S/N | Ao iniciar pedido no FV e abrir o catálogo, com esse parâmetro S irá exibir a quantidade e os botões + e - para regular quantidade na interface de inserção do Catálogo. |
| `CATALOG_CAN_SHOW_DETAILEDINFO` | S/N | Ao iniciar pedido no FV e abrir o catálogo, com esse parâmetro S irá exibir alguns detalhes dos dados do produto na interface de inserção do Catálogo. |
| `CATALOG_CAN_SHOW_ESTOQUE` | S/N | Ao iniciar pedido no FV e abrir o catálogo, com esse parâmetro S irá exibir a quantidade disponível em estoque na interface de inserção do Catálogo. |
| `CATALOG_CAN_SHOW_PRICES` | S/N | Ao iniciar pedido no FV e abrir o catálogo, com esse parâmetro S irá exibir o preço do produto na interface de inserção do Catálogo. |
| `CATALOG_CAN_SHOW_PRICESCOMIMP` | S/N | Ao iniciar pedido no FV e abrir o catálogo, com esse parâmetro S irá exibir o preço do produto COM impostos na interface de inserção do Catálogo. |
| `CATALOG_CAN_SHOW_PRICESSEMIMP` | S/N | Ao iniciar pedido no FV e abrir o catálogo, com esse parâmetro S irá exibir o preço do produto SEM impostos na interface de inserção do Catálogo. |
| `CATALOG_CAN_USE_MOBILE_NETWORK` | S/N | Quando inserido como N não permiti baixar o catalogo pela rede mobile, somente pelo wifi. |
| `CATALOG_CONTROLE_POR_RCA` | S/N | Habilita a opção de controle do catalogo por rca no portal administrador do catalogo. |
| `CATALOG_APAGA_ARQUIVOS_TEMP` | S/N | Com o parâmetro com valor S o aplicativo apaga os arquivos temporários no aparelho. |
| `HABILITA_CADASTRO_ROTA_CLIENTE` | S/N | Habilitar o cadastro de rotas durante o cadastro ou edição do cliente no aplicativo do Pedido de Vendas. Cadastro de clientes - Roteiro de visitas |
| `JUSTIFICAR_ROTEIRO_ANTERIOR` | S/N | Default vem desativado. Se estiver ativo, obriga o RCA a justificar a visita do roteiro pendente, caso o RCA não tenha justificado ainda é apresentada a msg "Existem clientes da última rota que não foram justificados!" |
| `ORDENA_COR_PREPEDIDO` | S/N | Afim de não trazer o Pop-up e trazer os itens do pré-pedido na aba tabela em primeiro na listagem #prepedido pre-pedido PREPEDIDO PRÉ-PEDIDO #COR cor |
| `NOME_FOTO_FACHADA` | TEXT | Define qual foto será atualizada no cadastro do cliente, deve ser inseriro no valor do parametro o nome da foto, sem a extensão, que será atualizada. Valor padrão "FOTO_FACHADA", o valor do parâmetro não é case sensitive. |
| `TOTALIZA_ESTOQUE_FIL_RETIRA_LISTAGEM_PRODUTO` | S/N | Durante um pedido na listagem de produtos, será exibido o total do estoque de produtos das filiais retira (Das quais o usuário possui permissão - "Filial Estoque") |
| `VALIDA_RESTRICAO_PRODUTO_POR_TIPO_VENDA` | S/N | Parâmetro configurado por filial, para a filial de venda validar restrição por tipo de venda. O parâmetro deve ser configurado na MXSPARAMFILIAL e não na MXSPARAMETRO |
| `USAR_CAMPANHA_DESCONTO_PROGRESSIVO` | S/N | Parâmetro necessário para ativar a Campanha de Desconto Progressivo. |
| `NOVO_FLUXO_GERAR_SENHA` | S/N | Parâmetro para informar se vai utilizar ou não o novo fluxo de gerar autorização de senha. |
| `VALIDA_RESTRICAO_ESTOQUE` | S/N | Impede a visualização de produtos sem estoque. |
| `CON_CGCCLIEXCLUSIVO` | S/N | Não Informado |
| `TEMPO_MIN_ALTERTA_JORNADA` | TEXT | Parâmetro responsável por configurar a periodicidade dos alertas de jornada. (Serve somente para o cliente Nordil). |
| `CON_USADESCPORQUANT` | S/N | Esse parâmetro serve para poder aceitar os descontos de quantidade cadastrados na rotina 561. Tem que estar como 'S' no Winthor para aceitar os descontos por quantidade nas negociações dos produtos. |
| `CON_UTILIZACONTROLEMEDICAMENTOS` | S/N | Habilitar parâmetro na rotina 132 do winthor |
| `TIPO_AMBIENTE` | TEXT | Valor = P (produção) Valor = T (Teste) Esse parâmetro serve para a integração de outros ERP verificar através de um POST na API se o ambiente do cliente é Produção ou Teste. |
| `RESTRINGIR_EMBALAGEM_FILHO_CAMPANHA` | S/N | Restringir embalagens de produto filho na campanha de desconto, caso marcado como N, nenhuma restrição é feita na seleção de embalagens do produto filho. |
| `Parâmetros MXSCONFIGDATA / MXSPARAMETRO` | S/N | . |
| `CAMINHO_FISICO_PASTA_RELATORIO` | TEXT | Diretório dos relatórios da 800. |
| `USAR_QTUNITCX_EXIBICAO` | S/N | - Não funciona - Caso o parâmetro 'USAR_QTUNITCX_EXIBICAO' estiver ativo, ele mostra na Quantidade da caixa o valor do campo qtunitcx da mxsprodut. Caso este esteja inativo ou não exista. O valor mostrado na tela será o da unidade da embalagem. |
| `ACRESCICMSPARTILHAPRECO` | TEXT | Agrega o valor do icms partilha no cálculo do preço base do produto. OBSERVAÇÃO: NÃO UTILIZAR ESSE PARÂMETRO QUANDO O CLIENTE UTILIZA INTEGRADORA DA PC |
| `LAYOUT_TABELA_SIMPLICICADO` | S/N | Força o Layout da aba TABELA do força de venda ficar resumido. |
| `VALIDAR_PRECO_MINIMO_201` | S/N | Se marcado como "S" não permite inserir produto com preço inferior ao preço mínimo da rotina 201 do Winthor. Valor Default = "N". MAXPEDIDO: A partir da 3.10.0, irá ignorar o parâmetro (CON_VALIDAPRECOMINIMO) que vem da 132 do Winthor e fica na MXSPARAMFILIAL. |
| `EXIBE_MSG_REC_ENV_TV11` | S/N | Exibir ou não a mensagem para TV11. Caso esteja como 'S' irá exibir, caso esteja como 'N' será utilizado "Enviar" como padrão. |
| `RECUPERAR_APENAS_PRIMEIRA_CONEXAO` | S/N | Parâmetro utilizado na MXSCONFIGDATA para recuperar a conexão após percar de sincronização. |
| `IMAGEBUILDLASTTIME` | NUMBER | Parâmetro utilizado para baixar a fotos no pedido de venda. Deixar o mesmo sempre zerado. |
| `MOSTRAR_COLUNA_PVENDASEMIMPOSTO_NA_LISTAGEM` | S/N | Apresenta coluna preço venda sem imposto na listagem dos produtos na aba TABELA. (MAXPEDIDO trabalha em conjunto com o parâmetro MOSTRAR_COLUNA_PVENDA_NA_LISTAGEM que apresenta o preço com imposto na listagem) |
| `VALIDA_RETRICAO_PLPAG_ORCAMENTO` | S/N | Valida restrição no plano de pagamento para orçamento. |
| `SERIALSERVIDOR` | NUMBER | É a chave que identifica de forma única o servidor do cliente. Ela é composta pela criptografia da trinca: nome do computador, código do cliente e código do produto. |
| `GRAVA_INFO_FECP` | S/N | Grava informações do FECP (NÃO É MAIS UTILIZADO DEVIDO AO MOTOR DE FÓRMULAS)Caso o valor do ST e FECP esteja sendo somado ao valor do produto, mesmo com o parâmetro UTILIZA_PRECOVENDA_SEM_IMPOSTO como S, esse parâmetro GRAVA_INFO_FECP deve ser inserido com o Valor = S |
| `NAO_CALCULAR_FECP_UF` | TEXT | Estados que não calculamos FECP (NÃO É MAIS UTILIZADO DEVIDO AO MOTOR DE FÓRMULAS) |
| `HABILITAR_OPCAO_PEDIDO_COMPLEMENTAR` | S/N | Com a opção 'É Pedido Complementar' no cabeçalho visível, ao marcar o parâmetro com 'S', é habilitada a opção para ficar editável. |
| `NAO_REVALIDAR_EST_EDICAO` | S/N | Tem a finalidade de desabilitar a validação de estoque de produtos já enviados na edição de pedidos. Com o parâmetro definido igual a 'S', os produtos enviados anteriormente não passarão por uma nova validação de estoque. |
| `BUSCA_DADOS_REGISTROPONTO` | S/N | Permite que os dados registrados no Firebase (jornada) sejam gravados na tabela MXSLOCATION. |
| `HABILITAR_OPCAO_GERAR_PEDIDO_BONIFICADO` | S/N | Com a opção 'Gerar Pedido Bonificado' no cabeçalho visível, ao marcar o parâmetro com 'S', é habilitada a opção para ficar editável. |
| `UTILIZA_DESMEMBRAMENTO_PARA_MULTIFILIAIS` | S/N | Se o cliente utiliza multifiliais, será obtido as diferentes filiais vinculadas ao pedido. Parâmetro da BOCCHI |
| `PORTACOMUNICACAONUVEM` | NUMBER | Parâmetro responsável por configurar a porta de comunicação com a nuvem. |
| `POSICAOPEDIDO` | NUMBER | Parâmetro responsável por mostrar a posição do Pedido. P = Pendente B = Bloqueado |
| `MOSTRAR_PERCDESC_SEMIMPOSTO` | S/N | Permite mostrar o percentual de desconto na aba produtos , com a dedução dos impostos. |
| `TIPO_DESC_PROGRESSIVO` | TEXT | Para utilizar o desconto progressivo como Campanha Progressiva, deve estar como 'PRG' na MXSPARAMETRO Para utilizar o desconto progressivo como Campanha P&G, deve estar como 'PEG' na MXSPARAMETRO |
| `FORCA_APLC_TX_FINAN` | S/N | Caso o parametro FORCA_APLC_TX_FINAN esteja habilitado vai aplicar as taxas financeiras apenas após definição do preço sem imposto |
| `EXIBIR_QTUNIT_ABRIR_PRODUTO` | NUMBER | EXIBIR_QTUNIT_ABRIR_PRODUTO com o valor igual S e o produto é frios (tipoestoque = 'FR') e a embalagem é KG ou KILOGRAMA, o aplicativo tenta utilizar o qtunit da embalagem cadastrada para o produto (Caso não tenha qtunit ele utiliza o valor do campo pesopeca cadastrado para o produto). Com o valor do parâmetro igual 'N', o aplicativo pega o pesopesa cadastrado para o produto. |
| `EXIBIR_CONTATO_REPRESENTANTE_LAYOUT_COMPARTILHADO` | S/N | Exibe telefone de contato do representante no layout do arquivo gerado para compartilhar o pedido. |
| `OCULTAR_IMPOSTOS_PEDIDO_EMAIL` | S/N | Ocultar impostos do pedido no layout do arquivo gerado para compartilhar o pedido. |
| `EXIBIR_PRECO_UNIT_EMB` | S/N | Exibe o preço unitário do pedido no layout do arquivo gerado para compartilhar o espelho do pedido. |
| `ACEITA_BNF_SEM_SALDO_CC` | S/N | Parâmetro Criado no MaxFarma conforme solicitação do Ticket MXFARDV-263 Parametro configurado como S ira aceitar pedidos BNF sem saldo de CC. |
| `ACEITAVENDAAVISTACLIBLOQ` | S/N | Na rotina 132 do Winthor (select * FROM PCPARAMFILIAL where nome like '%ACEITAVENDAAVISTACLIBLOQ%') Com o parâmetro = 'S' o sistema deixará iniciar o pedido para cliente bloqueado , porém deixará salvar apenas se o plano de pagamento for "A VISTA" e a cobrança for : Dinheiro (D), Dinheiro em trânsito (DH) ou Cartão (CAR). |
| `USAPRECOTABELA_CALC_PERDESC` | NUMBER | Usa preço de tabela para validação de desconto informado na inclusão do produto |
| `OBRIGAR_ATENDIMENTO_PARA_CHECKOUT` | S/N | Obriga realizar um pedido ou justificativa de não venda, em um atendimento ao fazer o checkout. |
| `STARTCLEANUPTIMER` | S/N | Inicia o Timer que faz a limpeza de DataFiles e arquivos de Log. Ele será responsável por iniciar a limpeza quando utilizado o parâmetro DAYSTOKEEPTEMPDATA. |
| `OCULTAR_PROD_FL_SEM_ESTOQUE` | S/N | Oculta produtos sem estoque no menu Produtos |
| `VALIDAR_ACRESCIMO_PF_LISTAGEM` | S/N | Caso o cliente seja PF (pessoa física) e possua acréscimo para PF o sistema calcula essa % no preço do produto e fica visível na aba Tabela |
| `META_GERAL_VLVENDA` | S/N | Ativa a meta por venda no menu de representantes. |
| `VALIDA_CPF_CNPJ_CONS_FINAL` | S/N | VALIDA_CPF_CNPJ_CONS_FINAL" do tipo booleano a nível geral com default TRUE. Quando este estiver desabilitado "VALIDA_CPF_CNPJ_CONS_FINAL" o maxPedido não obrigará a informar o campo CPF/CNPJ nos dados do consumidor final. Caso seja informado valor para o campo, este continuará a ser validado, independente do novo parâmetro "VALIDA_CPF_CNPJ_CONS_FINAL" |
| `TEMPO_MIN_PERMANENCIA` | TEXT | Configura o tempo mínimo de atendimento ao cliente, caso este utilize checkin/checkout. O valor do parâmetro deve conter 5 caracteres, incluindo o dois pontos. Ex: 00:10. Ou seja, o tempo mínimo de atendimento seria 10 minutos. |
| `CONSULTA_PRODUTO_POSITIVADO_PRODUTPOS` | S/N | No card "Produtos" do menu no maxPedido, caso esteja como 'S', é igualada a quantidade de produtos positivados na tela principal a rotina 1464 do Winthor. |
| `EMBALAGEM_PADRAO_CAIXA` | S/N | Quando habilitado, carrega a embalagem caixa primeiro. |
| `OBRIGA_LIMPEZA_ARQUIVOS` | S/N | Realiza a limpeza dos arquivos de pedidos antigos. |
| `OBRIGA_RECUPERACAO_PEDIDOS` | S/N | Serve para recuperar o pedido quando a aplicação e finalizada. |
| `ORDEM_TABELA_PEDIDO` | TEXT | Será reordenado produtos na listagem de tabela do pedido por tipo: Valores: "0,1,2" '0' = Ordenação Padrão de produtos '1' = Histórico de Compras '2' = Mix Ideal ',' = separador de ordenação obs.: Pode ser cadastrado em qualquer ordem, desde que seja separado por virgula |
| `APLICAR_DESCONTO_AUTOMATICO_MULTI_SELECAO` | S/N | Aplica o desconto automático de políticas da 561 e 3306, que estejam configuradas com aplicação automática, quando não é informado desconto para o produto na tela de múltipla seleção. |
| `MANTER_DESCONTO_TROCA_EMBALAGEM` | S/N | Mantem desconto informado na tela de negociação ao realizar a troca de embalagem. |
| `NAOVALIDA_MARGEMIN_WINTHOR` | S/N | Para não bloquear salvar pedido com Margem mínima de lucratividade abaixo do permitido pela presidência. (NÃO EXISTE NA APK OU NO SERVER) |
| `CATALOGO3_Produtos_ReprocNovo_IntervaloDias` | TEXT | CatalagoDigital - Armazena a quantidade, em dias, que o processamento dos produtos irá utilizar. Data atual menos a quantidade |
| `NOTIFICACAO_BRINDE` | S/N | Habilitar notificação brinde e também habilita notificação de produtos dentro de campanha de desconto da 3306. |
| `INICIAR_NEGOCIACAO_QTDE_MULTIPLO_APENAS_UNIDADE` | TEXT | Quando Habilitado (S), na tela de negociação do produto é exibido a quantidade inicial do produto de acordo com seu múltiplo na embalagem unidade, ou seja (mxsembalagem.qtunit), somente para embalagens com mxsembalagem.unidade = UN. |
| `HORA_INICIO_ENVIO_PEDIDO` | NUMBER | Horário inicial de envio de pedidos. |
| `HORA_FIM_ENVIO_PEDIDO` | NUMBER | Horário final de envio de pedidos |
| `GERARLOGSEMAIL` | S/N | Permite escolher se o server deve ou não gerar logs no processamento de envio de e-mails. |
| `EMAIL_AUTOMATICO_ASSUNTO` | TEXT | Para o envio de emails (pedido/orçamento) automatico é necessário preencher esse parâmetro. Que pode ser configurado através de configurações do Portal Admin |
| `HABILITAR_RELATORIOS_CUSTOMIZADOS` | S/N | NÃO UTILIZAR ESSE PARAMETRO - ALTERADO PARA HABILITAR_GERADOR_RELATORIOS |
| `VERSAO_ATUAL_DIFERENTE_NOVA` | S/N | Parâmetro que força verificação de nova versão _antes_ da sincronização |
| `USA_EMB_PROD_FILHO` | S/N | Trabalha junto com o parâmetro UTILIZA_EMBALAGEM_CAMPANHA_3306 e FIL_UTILIZAVENDAPOREMBALAGEM. Quando estes parâmetros estão habilitados, no momento do calculo do carregamento do produto, a embalagem carregada é a do produto filho. |
| `VERIFICA_FALTA_PED_RESTTRANSP` | S/N | Como a package que faz a restriçao de transporte não retorna um tipo de crítica, é verificado se existe alguma falta e aí sim alterar o tipo da crítica. |
| `UTILIZA_VLTOTGER_VENDAS_RCA` | S/N | Parâmetro validado pela job JOB_VENDAS_RCA (Requer implementação na job. verificar se o parâmetro é validado abrindo o corpo da package e buscando o nome do parâmetro). Utiliza o campo VLTOTGER em vez do VLTOTAL da tabela PCNFSAID quando CRITERIOVENDA = 'F' (Faturado) para o cálculo do valor alcançado pelo RCA |
| `USA_EMBALAGEM_MINIMA` | S/N | Ao definir o parametro USA_EMBALAGEM_MINIMA como N, a aplicação passa a exibir a embalagem da MXSPRODUT |
| `EXIBE_LINHA_DIGITAVEL` | S/N | Serve para exibir a linha digitável do titulo no menu de títulos. |
| `META_GERAL_QTPROD` | S/N | Habilitar visualização da aba pedido no menu Objetivos |
| `ALTERAR_PEDIDO_TV11_PARA_TV5` | S/N | Esse parâmetro como N o pedido de troca será gravado na pcpedcfv o campo condvenda como '11'. Como S e o pedido de troca será gravado na pcpedcfv o campo condvenda como '5'. Por default o parâmetro já vem como S então caso não exista é importante coloca-lo. |
| `UTILIZA_DE_PARA_MOTOR_CALCULO` | S/N | Define se será utilizado o motor de fórmulas, ou não. obs.: Após alterar na APK deve forçar a parada do maxpedido no android |
| `INTERVALO_ATUALIZ_FOTO_CLIENTE` | NUMBER | Configura a frequencia em MINUTOS com que será verficada as fotos de fachada dos clientes na Amazon. |
| `TEMP_ARREDONDAR_PRECO_UNITARIO_EMBALAGEM_TEMP` | S/N | Arredondamento de embalagem |
| `RV_FATURAMENTO_PESSOA_FISICA` | S/N | Exibir o campo Venda Faturada Pessoa Fisica no resumo de vendas, o valor padrão é S |
| `VLSUFRAMACALCULADO` | S/N | Parâmetro para tratar o valor de SUFRAMA, caso ele já venha calculado no preço de venda enviado pela APK. Colocar o parâmetro como N caso o valor de SUFRAMA não esteja embutido no preço de venda enviado pela APK. Colocar o parâmetro como S caso o valor |
| `VALIDAR_APURACAO_NF` | S/N | Considerada a validação da nota na positivação dos pedidos e nos valores de metas (No Resumo de vendas e Metas) os valores e itens são definidos pelos registros da nota. Por que a Sankhya não altera o histórico do pedido itens quando há um corte parcial ou total. (Resumo de venda e Metas) |
| `NUMDIAS_BUSCAR_STATUS_PEDIDO` | NUMBER | Valor limite de dias para buscar o status (críticas) dos pedidos. |
| `NAO_UTILIZAR_MASK_EST` | S/N | Quando esse parâmetro é ativado, o aplicativo deixa de limitar a quantidade de estoque de um produto na aba tabela a 99999, mostrando a quantidade exata acima desse valor. |
| `MXSESTNOTIFICACAO_STATUS` | S/N | Habilitar visualização de Notificação de estoque |
| `UTILIZAPLPAGMEDICAMENTO` | S/N | Habilitar permissão de plano de pagamento ético/genérico na mxsclient, ou seja, rotina 302 do winthor |
| `ULTIMA_VENDA_SEM_IMPOSTO` | S/N | Exibe o ultimo preço de venda no APK sem imposto |
| `QTDE_DIAS_HIST_VENDA_CLIENTE` | NUMBER | Define a quantidade em dias para gerar o historico de venda do cliente (default 90 dias) |
| `Portal Executivo - MXCONFIGDATA` | NUMBER | . |
| `USA_TARIFA_BOLETO` | S/N | caso o parametro CON_VLTARIFA da 132 esteja com valor definido, para aplicar a taxa cadastrada o pametro USA_TARIFA_BOLETO deve estar habilitado. |
| `MOSTRAR_EMBALAGEM_NOTAFISCAL` | S/N | Permite a inclusão da embalagem da MXSPRODUT na descrição do produto na impressão da nota fiscal do pedido |
| `DIAS_VERIFICACAO_ROTEIRO_PENDENTE` | NUMBER | Quantidade em dias que será verificado a existência ou não de pendencias no roteiro. OBS.: Para pegar o dia de "ontem", é necessário que o valor do parâmetro seja 1. Se for 2, vai pegar "anteontem", e se for 0 não será validado |
| `APRESENTAR_DESCONTOS_PEDIDO_EMAIL` | S/N | Marcado como sim irá exibir oscampos de desconto no template do orçamento/pedido PDF. Campos: VL DESC % DESC |
| `CONSIDERA_POS_CLIENTE` | S/N | Define se a positivação de itens será ou não considerada por clientes. |
| `RELATORIO800_INVERTER_DATA` | S/N | Conversão de datas para relatório da 800, por padrão é "N" |
| `QTD_PEDIDOS_LISTAR` | NUMBER | Serve para colocar a quantidade de pedidos que quer ser mostrado quando for na APK e clicar em pedidos, quando é feita a pesquisa ele ir e trazer no resultado apenas a quantidade informada neste parâmetro |
| `EXIBIR_EMBALAGEM_PEDIDO` | S/N | Exibir embalagem do pedido ao enviar o pdf no e-mail. |
| `COPIAR_RCA_ENVIO_EMAIL_AUTOMATICO` | S/N | Parâmetro que informa se deve ou não copiar o RCA no envio de e-mail automático |
| `CARREGAR_PLANOBNF_ANTES_COBRACA` | S/N | Ativa para carregar o plano de pagamento antes de carregar a cobrança, evitando erro de não validar a cobrança com o plano de pagamento. (MAXPEDIDO e Pedido de Venda) versão minima - 20.91.03 |
| `DEFINE_CC_MENU` | NUMBER | Determina qual o valor de conta corrente que sera apresentado na tela inicial. 0 - Apresenta o valor do saldo disponivel 1 - Apresenta o valor do saldo disponivel + limite de credito 2 - Apresentar o valor do limite de credito |
| `ENVIAR_EMAIL_AUTOMATICO` | S/N | Envia para os clientes e-mail automático de pedidos gerados pelo pedido de venda. |
| `ENVIAR_EMAIL_PEDIDO_AUTOMATICO_SUPERVISOR` | S/N | Envia cópia dos pedidos para o e-mail do supervisor. Os RCAs precisar estar vinculados ao supervisores no WinThor. Os supervisores precisam ter seu e-mail cadastrado |
| `IMPEDIR_ALTER_COMERCIAL_PRODUTO` | S/N | IMPEDIR_ALTER_COMERCIAL_PRODUTO parâmetro responsável por bloquear as alterações comerciais do produto. Esse parâmetro é configurado por filial no portal admin da maxima, as informações gravada está na tabela MXSFILIALCONFIG. (maxPedido aparece o campo ULT.PRECO 'último preço' na tela de negociação. Desativando esse parâmetro faz com que oculte esse campo também na negociação do produto.) |
| `FILA_ENVIO_INTEGRADORA` | S/N | Habilita o processamento de pedidos através de fila para a chamada a Integradora. (Server >= 20.7.62.82) |
| `FILA_ENVIO_INTEGRADORA_TEMPO` | S/N | Tempo para chamada dos pedidos para processamento na Integradora. (Server >= 20.7.62.82) |
| `FILTRAR_TITULOS_RCA` | S/N | parametros que devem estar como N para exibir os titulos pendentes e tambem o popup de titulos em aberto. FILTRAR_DADOS_TITULOS_RCA e FILTRAR_TITULOS_RCA |
| `INFORMAR_TODOS_PARAMETROS_BRINDES` | S/N | Obrigatório informar todos os parâmetro para geração de brinde. |
| `LIST_PROD_FIELD_INFTECNICAS` | S/N | #TECNICAS #tecnicas Exibe a opção Informações técnicas em Dados Adicionais do Produto. |
| `OCULTAR_PEDIDO_COMPLEMENTAR` | S/N | MAXPEDIDO - parametro para ocultar das opções do pedido a checkbox (é pedido complementar) |
| `OCULTAR_GERAR_PEDIDO_BONIFICADO` | S/N | MAXPEDIDO - parametro para ocultar das opções do pedido a checkbox (gerar pedido bonificado) |
| `PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO` | S/N | Mostra o histórico de pedidos feitos pelo ERP e não somente o que foi feito na APK (MAXPEDIDO) e habilita exibição na apk na aba de pedidos (TIMELINE). |
| `USAR_TODAS_EMB_3306` | S/N | . |
| `VALIDAR_LIMITE_CREDITO_WINTHOR` | S/N | Utilizar apenas o parâmetro BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE. ***Não utilizar o parâmetro VALIDAR_LIMITE_CREDITO_WINTHOR, por favor remover. |
| `MOSTRAR_LEGENDAS_3320` | S/N | Mostra legenda de produto da 3320 na aba TABELA. |
| `INTERVALO_ENVIO_EMAIL` | S/N | Parâmetro que determina em minutos o intervalo de envio de e-mail. |
| `OCULTAR_PRECO_MINIMO_201` | S/N | Quando habilitado como 'S', o mesmo irá ocultar o campo preço mim precificado '201' |
| `BLOQUEIO_COMERCIAL_ERP` | S/N | Define se o usuario pode utilizar bloqueio comercial ERP. Parâmetro não validado no fonte da V3 maxPedido. |
| `VALIDAR_ATENDIMENTO_DIAS_SEMANA` | S/N | Específico DFS: Valida os dias de atendimento do cliente tendo como base as informações preenchidas no cadastro na rotina 302. Parâmetro não validado no fonte da V3 maxPedido. |
| `EXIBIR_AGRUPAMENTO_FORNECEDOR` | S/N | MELHORIA EBD: Agrupamento de produtos por fornecedor. |
| `BLOQUEAR_PEDIDO_ABAIXO_MIN_PLANO_PAGAMENTO` | S/N | Se marcado como "SIM", não permitirá salvar pedido abaixo do mínimo permitido para o plano de pagamento. Se marcado como "NÃO", validará de acordo com os parâmetros do ERP. ******OBS.******: Também deve respeitar o parâmetro "CON_ACEITAVENDABLOQ" ou "ACEITAVENDABLOQ", onde altera o comportamento do parâmetro, pois caso ambos estejam como 'S', não irá bloquear o salvamento do pedido, apenas irá gerar um alerta na aba "ALERTAS DO PEDIDO". Caso esteja como 'S' e mesmo assim deseja bloquear o salvamento do pedido, selecionar no portal admin o acesso "Bloquear Pedidos Abaixo da Margem Mínima" |
| `APLICAR_PERCBASERED` | S/N | Ao marcar como "N", não irá aplicar o |
| `OBRIGATORIOVINCULARTV5COMTV1` | S/N | Obrigar o vinculo de pedido TV1 no pedido de bonificação. Obs: o mesmo parâmetro existe na rotina 132 por filial. |
| `ARREDONDAR_PRECOSEMIMPOSTO` | S/N | ARREDONDAR_PRECOSEMIMPOSTO parâmetro para arredondar o preço sem imposto, é necessário habilitar esse parâmetro quando o cliente trabalha apenas com duas casas decimais e está calculando o valor do ST errado. OBSERVAÇÃO: ATIVAR ESSE PARÂMETRO APENAS COM ORIENTAÇÃO DO DESENVOLVIMENTO. |
| `CON_BONIFICALTDEBCREDRCA` | S/N | Debita valor de produtos bonificados da conta corrente do RCA |
| `EXIBIR_AVALIACAO_REPRESENTANTE` | NUMBER | Parâmetro responsável por controlar a exibição da guia Avaliação Representante no menu Representante. Por padrão (default) é lido como S na apk. |
| `RV_PREVISAO_COMISSAO_VENDA` | S/N | Caso esteja marcado como S vai exibir o campo "Previsão Comissão de Venda" no resumo de venda. Como padrão fica como S. |
| `FUSO_HORARIO_JORNADA` | TEXT | Com esse parâmetro você configura o fuso horário que a jornada vai utilizar para validar o bloqueio do aparelho. Valor de exemplo do parâmetro: America/Sao_Paulo |
| `CATALOG_ENCAMINHA_PEDIDO_VENDAS` | S/N | Parâmetro do CATALOGO, para redirecionar para o pedido de vendas |
| `HABILITA_LEMBRETE_ANIVERSARIANTES` | S/N | Habilita lembrete de aniversariantes |
| `CPF_CNPJ_EXCLUSIVO` | NUMBER | CNPJ Exclusivo do cliente, para clientes cadastrados via APK da MaximaTech |
| `GRAVAR_FILIAL_NF_NULO` | S/N | Quando o parâmetro GRAVAR_FILIAL_NF_NULO está com o valor igual 'S' e o cliente não tem uma filial NF definida e o pedido também não tem filial NF definida. O aplicativo vai utilizar o preço da região do cliente (Ou seja o preço de acordo com a praça do cliente) |
| `PERMITE_ALTERAR_FILTRO_MARCA` | S/N | Permite alterar o filtro de marca ao editar o pedido |
| `SEARCH_PEDIDO_FORCAR_MARCA` | NUMBER | Forçar utilizar marca única no pedido |
| `SEARCH_PEDIDO_MARCA` | S/N | Exibir filtro por marca, utilizar com o parâmetro REST_PESQ_MARCA = S |
| `GERARCHAVENOLINK` | S/N | Habilitar a opção de utilizar Link para Acesso, no cadastro do RCA/Vendedor na tela de cadastro de usuário, aba Dispositivos |
| `NUMDIAS_ALERTA_VALIDADE` | NUMBER | Deverá informar a quantidade de dias para começar a informar que o produto esta próximo ao vencimento. |
| `POLITICA_USA_MAIOR_NUMERAL_ACRESCIMO` | S/N | Parâmetro responsável por definir se a politica de acréscimo vigente será a de maior valor monetário ou maior valor escalar. Ex: PercentualAcrescimo[-3%, -1%] Caso definido como 'S' o PercentualAcrescimo vigente será o de 1%. Caso definifo como 'N' o PercentualAcrescimo vigente será o de 3%. |
| `GPS_ENVIA_COORDENADAS` | S/N | Quando ativado faz o registros da localização do vendedor na GPS_RASTREAMENTO, para utilizar juntamente com a geolocalização e rastreamento. |
| `PERMITIR_VENDA_CARTAO_TV7` | S/N | Permitir fazer venda cartão com TV7 |
| `UTILIZA_RESUMO_METAS_REQUISICAO` | S/N | Parâmetro para ativar a solicitação de resumo de vendas e metas por requisição, dispensando o uso de Jobs para alimentar as informações. |
| `TELA_3306_ANTERIOR` | S/N | Habilita a visualização da antiga tela de campanhas da 3306, onde não há a repetição de produtos por faixa de desconto no momento da inserção. OBS: Vai funcionar a partir da 20.127.00 |
| `REL800_WINTHOR29` | S/N | Geração de relatórios da rotina 800 para |
| `OCULTAR_VALIDADE_PROPOSTA` | S/N | Parâmetro para ocultar o campo validade da proposta no pedido/orçamento enviado por email |
| `ENVIA_PEDIDOS_BALCAO_RESERVA` | S/N | Enviar Historico de pedidos do Balcão Reserva O nome do parametro correto é ENVIA_PEDIDOS_BALCAORESERVA |
| `ENVIA_PEDIDOS_WEB` | S/N | Enviar Histórico de pedidos WEB |
| `ENVIA_PEDIDOS_AUTOSERVICO` | S/N | Enviar Histórico de pedidos Auto Serviço |
| `DEFINE_META_GRAFICO` | NUMBER | Define meta da 399 para o gráfico da tela inicial do maxPedido: 0 -> Venda 1 -> MIX 2 - > Clientes 3 -> Pedidos |
| `OCULTAR_OPCAO_INFORMACOES_EXTRAS` | S/N | Ocultar a opção de informações extras. Obs : Se o parâmetro EXIBIR_VENDA_MES estiver como S também ira ocultar. |
| `UTILIZAR_META_TRANSMITIDA_EM_TIPO_ZERO` | S/N | Onde o parâmetro DEFINE_META_GRAFICO for definido como 0, devemos definir qual o tipo de meta para a venda habilitando mais um parâmetro (tipo lógico) conforme o tipo: UTILIZAR_META_TRANSMITIDA_EM_TIPO_ZERO = S ( Para venda transmitida ) UTILIZAR_META_TRANSMITIDA_EM_TIPO_ZERO = N ( Para venda faturada ) |
| `OCULTAR_COMISSAO_MENU` | S/N | Visualiza ou não a comissão prevista na aba objetivos do menu inicial do aplicativo. Para não trazer deve estar setado com S. |
| `INICIAR_NEGOCIACAO_QTDE_MULTIPLO` | S/N | Inicia a negociação de produto com o campo Qtde preenchido com valor do campo mxsprodfilial.multiplo se não mxsprodut.multiplo |
| `VALIDA_COBRANCA_INICIO_PEDIDO` | S/N | Define se irá validar restrições de cobrança ao iniciar o pedido. |
| `FORCEREADMSGS` | S/N | Caso esteja como "S", força a leitura das mensagens para iniciar um pedido, |
| `TIPO_VENDA_PRIORITARIO` | NUMBER | Define o tipo de venda prioritário no inicio da confecção do pedido. Apk outros ERPs. |
| `DEFINE_CODAUXILIAR2_PADRAO_VENDA` | S/N | Quando setado como 'S' a embalagem que irá aparecer por padrão, é a que contem o mesmo código codauxiliar na mxsembalalagem igual ao código codauxiliar2 na mxsprodut. |
| `REST_PESQ_MARCA` | S/N | Habilita pesquisa por marca na aba tabela , utilizar com o parâmetro SEARCH_PEDIDO_MARCA = S |
| `EXIBIR_FOTO_DO_PRODUTO_PERSONALIZADO_PDF` | S/N | Exibir as fotos em tamanho grande no final do PDF quando compartilhar o pedido. |
| `EXIBIR_FOTO_DO_PRODUTO_PDF` | S/N | Exibir as fotos ao lado dos produtos no PDF quando compartilhar o pedido. |
| `PRECO_EXIBICAO_COM_IMPOSTOS` | S/N | Quando marcado como S, exibe o preço unitário com imposto (só vale para clientes que negociam sem imposto) |
| `MOSTRAR_LOTE_SOMENTE_COM_ESTOQUE` | S/N | Quando marcado como S exibe apenas os lotes que ainda possui estoque, caso marcado como N, exibe os lotes com estoque e sem estoque. |
| `MOSTRAR_CLIENTE_SEM_LOCALIZACAO_CADASTRADA` | S/N | Quando habilitado, vai exibir a legenda de cliente sem localização na listagem de clientes quando os campos longitude e latitude da MXSCLIENT tiver vazio. |
| `PERMITE_INICIAR_PEDIDO_COMO_ORCAMENTO_NAO_MOV_CC` | S/N | Com esse parametro cadastrado e definido como S, ao inciar um pedido a aplicação vai questionar se você deseja iniciar um pedido de orçamento, caso marque sim, o pedido vai ser apenas em orçamento, caso marque não, vai iniciar um pedido normal. Com este parametro cadastrado com valor S o saldo conta corrente não é movimentado em pedido orçamento. Caso este parametro esteja cadastrado, porém sem nenhum valor, a aplicação vai iniciar o pedido e dentro da negociação você define se quer salvar o pedido normal ou orçamento. |
| `BLOQ_SALVAR_PEDIDO_ACIMA_LIMITE_CLI_APK` | S/N | Bloquea o salvamento do pedido quando o cliente não tiver limite de credito suficiente. |
| `USAR_VALIDACAO_REFINADA_RESTRICAO` | S/N | Quando marcado como N, desabilita a busca refinada de restrições de venda. É orientado para clientes que tem poucos produtos e poucas restrições, para que a listagem e busca de produtos fique mais rapida. |
| `HABILITA_EVENTOS` | S/N | HABILITA_EVENTOS = 'S' para enviar os rastros para o maxGestão e ter as informações em auditoria |
| `FILTRAR_HISTCOMPRAS_RCA` | S/N | Parametro por default é setado = N. O mesmo realiza ou não o filtro onde sera apresentado o historico de compras somente do rca quem vendeu ou de todos os representantes. |
| `DESATIVA_VALIDACAO_CNPJ_CADASTRADO` | S/N | Quando habilitado não fará a validação, no Winthor, se o cliente já existe pelo CNPJ/CPF. Permitindo assim o representante salvar e enviar o cadastro do cliente realizado no aplicativo. |
| `EXIBIR_DIALOG_DE_BRINDE` | S/N | Para apresentar a mensagem de possibilidade de brinde ao negociar o produto. |
| `EMPRESA` | TEXT | Define o nome da empresa que será apresentado na aplicação. |
| `PERC_ACRESC_PREAUTORI_CARTAO_CRED` | NUMBER | Irá acrescentar esse valor percentual a mais no valor que será reservado na pré-autorização no cartão de credito do cliente. Funciona com novo processo de cartões via maxPayment do maxPedido. |
| `META_GRUPO` | S/N | Parâmetro para habilitar a aba de meta por grupo de produtos. |
| `DESABILITAR_ESCOLHA_TIPO_DOCUMENTO` | S/N | Se o parâmetro estiver setado com 'S' não irá trazer a opção para escolher o tipo de documento no início do pedido. Se o parâmetro estiver setado com 'N' irá respeitar o parâmetro do Winthor 'DEFINIRTIPODOCVENDA' (parâmetro 2384 - Definir o tipo de documento na venda). |
| `ENVIAR_APENAS_TITULOS_VENCIDOS` | S/N | Parâmetro para enviar somente os dados de títulos que estão vencidos, os outros títulos não serão importados para o banco da nuvem. Parâmetro do Extrator. |
| `QTDE_PERMITIDA_IMPORTAR_ORCAMENTO` | NUMBER | Quando informado um valor irá limitar a quantidade de vezes que orçamento pode ser importado para pedido. Se nulo ou não existente não terá o limitador. |
| `VALIDA_DTVENC_LIMCRED_INICIO` | S/N | Quando estiver como 'S' ao iniciar o pedido e o cliente estiver com limite de crédito vencido não permite iniciar um pedido. |
| `META_DEVOLUCAO` | S/N | Habilita a aba Devoluções no card Objetivos. Obs.: o parâmetro por default é True no código. |
| `BLOQUEAR_ENVIO_PED_FORA_INTERVALO` | S/N | Habilita a opção para bloquear envio de pedidos fora do horário na central de configurações (deve ser do tipo "por usuário"). |
| `BLOQUEAR_SINC_FORA_INTERVALO` | S/N | Habilita a opção para bloquear o envio e recebimento de dados fora do horário na central de configurações, (deve ser do tipo "por usuário"). |
| `JORNADA_APOS_CHECKIN` | S/N | Quando o parâmetro estiver habilitado o botão para registro de jornada deverá ficar habilitado para o primeiro registro de ponto somente após registrar o checkin no cliente. |
| `ALERTA_TEMPO_MAXIMO_ALMOCO` | S/N | Se o parâmetro estiver habilitado, o aplicativo deverá verificar o registro da entrada para o almoço e caso o vendedor não registre a saída do antes do tempo máximo configurado deverá exibir um alerta no aplicativo. |
| `BLOQUEIA_ PED_FORA_JORNADA` | S/N | Quando estiver habilitado irá permitir o representante apenas fazer consultas na aplicação. Não será possível iniciar um novo pedido, nem duplicar os pedidos. A exceção será quando depois da jornada ocorrer a liberação através da senha gerado pelo central de configurações. |
| `TRAVA_MES_ATUAL_OBJETIVOS` | S/N | Quando este for habilitado, o sistema vai travar a consulta de objetivos no mês atual. |
| `ENVIA_PEDIDOS_BROKER` | S/N | Enviar os pedidos broker para a apk. |
| `BLOQ_PERIODO_MENU_RCA` | S/N | Bloquear a lupa da aba objetivos. -filtro objetivos -consulta |
| `RV_VOLUME_VENDA` | DATA | Marcado como N oculta da tela de resumo de vendas o campo Volume de venda. |
| `CALCULAR_IMPOSTOS_ITEM_CESTA` | S/N | CALCULAR_IMPOSTOS_ITEM_CESTA = 'N' quando está dando erro de imposto no produto que é KIT (cesta) na hora da negociação, não deixando entrar para negociar. Mensagem: Produto sem precificação definida (PRECO NULO OU ZERO). Nao é possivel inclui-lo no pedido. |
| `MARCAR_FILTRO_MIXIDEAL` | S/N | Por padrão vem false, caso esteja como true irá apresentar somente os itens que estão cadastrados no mix ideal na inteligência de negocio. Atenção: Caso esteja true e o cliente nao tenha mix cadastrado irá ocultar todos os outros produtos. |
| `VALIDAR_TIPOVENDA_BONIFICACAO` | S/N | Caso esteja como 'N' na venda tipo 5 (bonificação) ira desconsiderar o plano de pagamento com tipoprazo = 'B' e a cobrança 'BNF'. |
| `MULTIPLICA_PERCDESCONTOINFORMADOTELA` | S/N | Multiplica por 100 o valor da propriedade "PercDescontoInformadoTela" no JSON. |
| `OCULTAR_LIMITE_CLIENTE` | S/N | Oculta as informações de limite de credito do cliente. |
| `PERMITIR_SELECIONAR_BRINDES` | S/N | Gera automaticamente um pedido bonificado com os itens de brinde do pedido normal. |
| `VALIDAPESO` | S/N | Valida se a campanha de desconto FPU (MXSDESCONTOC) vai ser por peso do produto. |
| `PESQUISA_ESTOQUE_ONLINE` | S/N | Habilita opção de sincronizar estoque do produto a partir do Endpoint criado pelo ERP |
| `USUARIO_INTEGRACAO` | TEXT | Utilizado em conjunto com o parâmetro 'PESQUISA_ESTOQUE_ONLINE' |
| `SENHA_INTEGRACAO` | TEXT | Define a senha do usuário da integração durante a integração, em conjunto com o parâmetro 'PESQUISA_ESTOQUE_ONLINE' |
| `IP_SERVER_INTEGRACAO` | TEXT | IP do endpoint de integração, utilizado em conjunto com 'PESQUISA_ESTOQUE_ONLINE' |
| `CON_ACEITAVENDABLOQ` | S/N | 1 - E se parametro CON_ACEITAVENDABLOQ - Aceita venda bloqueado da rotina 132 estiver como S o pedido é salvo no aparelho; |
| `INVERTER_BASECREDDEBRCA_AUTORIZACAO` | S/N | Permite inverter o valor definido no campo "Debitar do RCA" do portal executivo, o valor invertido será gravado no campo BASECREDDEBRCA da tabela PCAUTORI. |
| `EDITA_QUANTIDADE_PRE_PEDIDO` | S/N | Permite alterar a quantidade dos itens que estão sendo inseridos através do pré pedido quando o parâmetro está como S, não é possivel editar a quantidade dos itens quando o parâmetro está como N. Valor padrão: N |
| `EDITA_PRODUTOS_PRE_PEDIDO` | S/N | Quando o parâmetro está como S é permitido inserir os itens de pré pedido que o vendedor desejar, quando está com N é obrigatório inserir todos os itens do pré pedido. |
| `FORCA_EXIBIR_VALOR_TITULO` | S/N | 'S' vai exibir o valor dos títulos conforme o Winthor |
| `GERAR_MIXCLIENTE_HISTORICO` | S/N | Habilita o histórico do mix de clientes para visualização na apk. |
| `BLOQUEAR_UTLIZACAO_ECONOMIA_BATERIA` | S/N | Exibirá uma mensagem se a economia de bateria estiver ativada e bloqueia o uso do aplicativo. |
| `IGNORAR_ESTOQUE_FILIAIS` | S/N | Parametro de banco, para gerar os dados da tabela MXSESTFILIAL, quando "S" permite gerar dados de produtos sem estoque, valor padrão: "S" |
| `FORCAR_RESTRICAO_COBRANCA_PLANO_PAGAMENTO` | S/N |  |
| `VALIDAR_PRAZOMEDIO_COBRANCA_DH` | S/N | Permite a cobrança DH trabalhar a prazo. Deve ser colocado como N para permitir a cobrana DH ser a prazo caso contrario sera tratada como DINHIERO |
| `BLOQ_SOLIC_AUTO_PRECO_FIXO` | S/N | Permite bloquear solicitar autorização de preço quando utilizado preço fixo. |
| `ALERTAR_SYNC_ROTEIRO_PENDENTE` | S/N | Se estiver ativo e existirem clientes do Roteiro de Visitas ainda não atendidos ou justificados, ao tentar sincronizar, o sistema emitirá o alerta: “existem clientes ainda não atendidos ou justificados” . |
| `ALERTA_TIT_VENCIDO` | S/N | Apresenta uma tela informando que o cliente possui títulos em aberto. Informa uma lista com os títulos inadimplentes do cliente. O nome do correto é ALERTAR_TIT_VENCIDO |
| `EXIBIRTITULOSPAGOS` | S/N | Parametro que permite exibir titulos pagos na consulta de titulos, caso esteja como S os titulos pagos que estão na base da APK seram exibidos na tela de titulos pagos. |
| `NOVA_3306` | S/N | Quanto esse parâmetro está como S faz a mesma validação do winthor considerando as embalagens cadastradas na campanhas. |
| `TEMPO_LIMITE_SINCRONIZACAO` | NUMBER | Parametro que define o tempo limite de sincronização em minutos, o server irá fechar a conexão retornando mensagem pra APK quando o tempo de sincronização ultrapassar o definido no parametro |
| `ARREDONDAR_VALOR_TOTAL` | S/N | Exibe nos campos "Valor Total e Valor Tabela" na aba "TOTAIS", o valor com duas (2) casas decimais, mesmo que no Winthor o cliente trabalhe com seis (6) casas decimais, parâmetro Winthor: CON_NUMCASASDECVENDA. |
| `VALIDA_MULT_DISDAL` | S/N | Marcado como 'S', irá validar o múltiplo do produto no FV, mesmo que o campo VALIDARMULTIPLOVENDA da rotina 302, no cadastro do cliente esteja marcado como 'N'. |
| `MXS_UTILIZAVENDAPOREMBALAGEM` | S/N | Força a utilização de venda por embalagem pela aplicação, criado para atender uma demanda da STO MXS_UTILIZAVENDAPOREMBALAGEM substitui o FIL_UTILIZAVENDAPOREMBALAGEM da 132. |
| `PERMITE_EDITAR_CAMPANHAS` | S/N | Habilitado com S, vai permitir editar produtos de campanha da 3306, direto na aba PRODUTOS. Sem a necessidade de ficar removendo o ítem e inserindo novamente a partir da aba Campanha de Desconto. |
| `VENDA_PRODUTO_SU` | S/N | Permitir que Produtos Suspensos no Winthor (rotina 203 - OBS = 'SU') sejam apresentados e vendidos no MaxPedido. |
| `DESCONTO_ACIMA_PERMITIDO_2551` | S/N | Faz a validação do parâmetro 2551 da 132, permitindo que o rca inclua desconto acima do permitido no produto. |
| `CLIENTE_EXIBIR_TITULOS` | S/N | Por default = 'S', responsável por mostrar os títulos dos clientes ao abrir o cadastro no fv. |
| `IGNORA_PARAMETRO_2618` | S/N | Permite aplicar desconto no fv para clientes bloqueados, desconsiderando o parâmetro 2618 da rotina 132 . |
| `DIAS_PERMITIDOS_ROTEIRO_ANTERIOR` | NUMBER | - Se JUSTIFICAR_ROTEIRO_ANTERIOR = S e houver rota anterior permitida (verificar parametro DIAS_PERMITIDOS_ROTEIRO_ANTERIOR) restringir abertura de pedidos aparecendo a dialog: "Existem clientes da última rota que não foram justificados!" |
| `PERMITE_PROD_SEM_DISTRIBUICAO` | S/N | Parâmetro que será validado junto com o campo mxsusuari.permiteprodsemdistribuicao, |
| `FILTRAR_CONSUMIDOR_FINAL_GERACAO` | S/N | Definido com o valor = 'S', faz com que os clientes consumidores finais padrão do winthor cod 1, 2 e 3, não sejam enviados para o força de vendas. O valor padrão fica como 'N'. |
| `QUALIDADE_IMAGENS_ESPELHO_PEDIDO` | TEXT | Quando habilitado a API vai realizar o redimensionamento das imagens a fim de que otimize o download do arquivo na aplicação. Valor do parametro sera B (baixo), M (médio), A (alto). |
| `HABILITA_RECOMENDACAO_PRODUTOS` | S/N | Parâmetro responsável por habilitar a recomendação de produto pela apk através da inteligência artificial (IA). Gera dados depois de 24h após a ativação. Gera dados na tabela MXSRECOMENDACAO |
| `PARAMETROS_CODUSUR_REL_800` | TEXT | Ao imprimir o relatório pelo app, faz com o relatório saia somente referente ao usuário logado no aplicativo. \| precisa-se colocar a variável do codusur que fora utilizado no sql do relatório no valor do parâmetro. |
| `GERAR_POSITIVACAO_CLIENTE_DTFAT` | S/N | Considerar data de faturamento na positivação dos clientes (MXSHISTORICOPEDC.DTFAT). Para habilitar a opção, habilitar o parâmetro: GERAR_POSITIVACAO_CLIENTE_DTFAT = 'S' e esperar a job executar. A job é executada em intervalos de tempo de uma hora. |
| `PADRAO_FRETE_DESPACHO` | TEXT | Será definido qual o tipo padrão do frete Despacho |
| `PADRAO_FRETE_REDESPACHO` | TEXT | Será definido qual o tipo padrão do frete Redespacho |
| `OCULTAR_VALOR_ACRESCIMO_PEDIDO_COMPARTILHADO` | S/N | Irá ocultar o valor de acréscimo(caso o item tenha acréscimo adiconado) ao compartilhar o pdf do pedido. Parâmetro será validade no apk a partir da versão 20.183.14 ou superior do aplicativo do pedido de vendas e a partir da versão SRV20.263.0.83 ou superior do server. |
| `CONSIDERAR_DATA_ATUAL_PREV_FAT` | S/N | Alterar |
| `VERIFICAR_STATUS_RCA_SYNC` | S/N | verifica status do RCA na sincronização |
| `EXIBIR_UNIDADE_POR_EMBALAGEM_EMAIL` | S/N | Com valor = 'S' irá exibir o campo EMB ao compartilhar o pdf do pedido/orçamento com o valor da qtunit da embalagem do produto. |
| `NOTIFICAR_CLIENTES_PROXIMOS` | S/N | Gerar notificação de Check-In/Check-Out no celular. |
| `TEMPO_VERIFICACAO_CLIENTES_PROXIMOS` | NUMBER | Tempo que a apk leva para gerar notificação de Check-In/Check-Out na notificação do celular. |
| `HABILITA_ANOTACOES_CLIENTE` | S/N | Habilita a opção de anotações para os clientes do RCA no maxPedido; Serve para o RCA realizar qualquer anotação em determinado cliente |
| `EXIBIR_ACRESC_CRED_FAT` | S/N | Exibe a positivação de conta corrente na aba de Totatis (TOTAIS) do pedido, por default vem = N. Se etiver habilitado mostra a positivação da conta corrente prevista no pedido baseado em acréscimos dados nos itens incluídos no pedido. |
| `ENVIAR_FILIAL_RETIRA_ESTOQUE` | S/N | Ao deixar o paramentro S e enviado o estoque da filial venda e filial de estoque para a MXSEST, quando trabalha com Filial retira diferente da filial de venda |
| `TIPO_COBRANCA_PADRAO_CADASTRO_CLIENTE` | NUMBER | Define uma cobrança padrão para o cadastro de cliente |
| `GRAVA_LOG_ERRO_ENVIO_PEDIDO` | S/N | [Funcional a partir da v4.032.5] Registra a log dos pedidos na APK na tabela LOGJSON. Ideal para registrar log de pedidos presos na nuvem, atrasos no envio etc. OBS: desativar os parâmetros após 15 dias ou 1 mês, se o problema não vier a ocorrer novamente. Para que a base não fique com muitos registros. ATIVAR TAMBÉM: GRAVA_LOG_ERRO_ENVIO_PEDIDO GRAVA_LOG_ENVIO_PEDIDO_NUVEM GRAVA_LOG_ENVIO_PEDIDO GRAVA_LOG_PEDIDOS_PENDENTES |
| `GRAVA_LOG_ENVIO_PEDIDO` | S/N | [Funcional a partir da v4.032.5] Registra a log dos pedidos na APK na tabela LOGJSON. Ideal para registrar log de pedidos presos na nuvem, atrasos no envio etc. OBS: desativar os parâmetros após 15 dias ou 1 mês, se o problema não vier a ocorrer novamente. Para que a base não fique com muitos registros. ATIVAR TAMBÉM: GRAVA_LOG_ERRO_ENVIO_PEDIDO GRAVA_LOG_ENVIO_PEDIDO_NUVEM GRAVA_LOG_ENVIO_PEDIDO GRAVA_LOG_PEDIDOS_PENDENTES |
| `GRAVA_LOG_PEDIDOS_PENDENTES` | S/N | [Funcional a partir da v4.032.5] Registra a log dos pedidos na APK na tabela LOGJSON. Ideal para registrar log de pedidos presos na nuvem, atrasos no envio etc. OBS: desativar os parâmetros após 15 dias ou 1 mês, se o problema não vier a ocorrer novamente. Para que a base não fique com muitos registros. ATIVAR TAMBÉM: GRAVA_LOG_ERRO_ENVIO_PEDIDO GRAVA_LOG_ENVIO_PEDIDO_NUVEM GRAVA_LOG_ENVIO_PEDIDO GRAVA_LOG_PEDIDOS_PENDENTES |
| `OCULTAR_OPCAO_SALVAR_ENVIAR_ORC` | S/N | Foi criado o parâmetro 'OCULTAR_OPCAO_SALVAR_ENVIAR_ORC ' que quando habilitado, irá ocultar a opção de salvar e enviar orçamento. Esta solicitação está disponível na versão 1.15.95 superior do aplicativo do maxPedido. |
| `LISTAR_PROD_EST_RETIRA` | S/N | Exibe o estoque da filial retira definido na tabela mxsfilialretira. |
| `CONSULTA_PRODUTO_POSITIVADO_PRODUTOS` | S/N | Para o extrator gerar as informações corretamente. |
| `OCULTAR_OPCAO_SALVAR_BLOQUEAR_ORC` | S/N | oculta a opção de salvar bloqueando orçamento |
| `USAR_AUTORI_LIMITE_CLENTE` | S/N | Usa solicitaÃ§Ã£o de limite de crÃ©dito via mensageria |
| `QTDE_DIAS_FINAL_TITULOS` | NUMBER | Parâmetro em questão foi substituído pelo CON_NUMDIASMAXVENDACLIINADIMPLENTE, no adiciona a quantidade de dias que se pode realizar após o vencimento do título de cliente inadimplentes. |
| `EMITIR_COMPROVANTE_JORNADA` | S/N | Caso valor = Sim, ativa a caixa de seleção para salvar comprovante de jornada. |
| `HABILITA_PROC_PROD_AGREGADO` | S/N | Habilita visualização de produtos agregados. Parâmetro não validado no fonte da V3 maxPedido. |
| `PRIMEIRA_IMPLANTACAO` | S/N | Caso = S, Informa para o extrator que é a primeira implantação para rodar todos os scripts. |
| `ACEITA_VENDA_CLIENTE_BLOQ` | S/N | Permite enviar pedido para cliente bloqueado |
| `HABILITA_PED_CLI_RECEM_CADASTRADO` | S/N | Permite iniciar pedido para clientes recém cadastrados. |
| `PEDIR_AUTORIZACAO_TV5_VINCULADO_TV1` | S/N | quando habilitado junto com a permissão de solicitar autorização de pedido bonificado, ao vincular um tv1 em um tv5 irá solicitar a aprovação do tv5 ou tv5 depois do tv1 na aba de cabeçalho. |
| `GRAVAR_LOG_TROCA_COBRANCA_PLPAG` | S/N | Grava log de troca de cobrança com plano de pagamento caso seja identificado que foram salvos pedidos com e cobranças que não são possíveis setar manualmente sistema através de pedido, ou seja, plano bonificação cobrança cartão de crédito, onde ex: plpag.bnf só ser salvo com cob.bnf |
| `MODO_HOLOGACAO_API_CARTAO` | S/N | Parametrização para habilitar a funcionalidade de pagamento com cobrança "cartão de crédito" via pagamento através do maxPayment. ATENÇÃO: Será descontinuado após a retirada do fluxo antigo de que preenche via apk os dados do cartão, ou seja, necessário verificar se precisa cadastrar ou não. |
| `GRAVA_LOG_EDICAO_EXCLUSAO_PEDIDO` | S/N | grava log de edição e exclusão de pedidos na apk |
| `EXIBIR_INFORMACOES_TECNICAS` | S/N | Exibir info técnicas do produto da mxsprodut - mxsprodut.INFORMACOESTECNICAS |
| `LABEL_OBS_1` | TEXT | Parametro utilizado para alterar o nome do label (Observações do pedido / Cadastro:) ex: se no valor parametro colocarmos: teste, então o primeiro label observações vai ser exibido o nome teste no lugar padrão (Observações do pedido / Cadastro:) |
| `LABEL_OBS_2` | TEXT | Parametro utilizado para alterar o nome do label (Observações de entrega) ex: se no valor do parametro colocarmos: teste, então o segundo label referente entrega da aba observações vai ser exibido o nome no lugar do nome padrão (Observações de entrega) |
| `TAMANHO_OBS1` | NUMBER | Determina a quantidade de caracteres que o primeiro campo de digitação da observação pedido / cadastro comportar. Sendo que a limitação do campo é até caracteres. Parametro criado para ERP (OUTROS ERPs) |
| `TAMANHO_OBS2` | NUMBER | Determina a quantidade de caracteres que o segundo campo de digitação da observação pedido / cadastro comportar. Sendo que a limitação do campo é até caracteres. Parametro criado para ERP (OUTROS ERPs) |
| `TAMANHO_OBS_ENT1` | NUMBER | Determina a quantidade de caracteres que o primeiro campo de digitação da observação de entrega vai comportar. Sendo que a limitação do campo é até caracteres. Parametro criado para ERP (OUTROS ERPs) |
| `TAMANHO_OBS_ENT2` | NUMBER | Determina a quantidade de caracteres que o segundo campo de digitação da observação de entrega vai comportar. Sendo que a limitação do campo é até caracteres. Parâmetro criado para ERP (OUTROS ERPs) |
| `TAMANHO_OBS_ENT3` | NUMBER | Determina a quantidade de caracteres que o terceiro campo de digitação da observação de entrega vai comportar. Sendo que a limitação do campo é até caracteres. Parâmetro criado para ERP (OUTROS ERPs) |
| `CARREGAR_CAMPANHAS_INICIALIZACAO_PEDIDO` | S/N | Quando habilitado, as campanhas não irão carregar automaticamente na inicialização do pedido, somente quando for na aba de Campanhas e clicar na Lupa carregar. |
| `HABILITAR_CAPTURA_HORARIO_MAXTRACKING` | S/N | Habilitar captura do maxTrancking por dia e horário configurados na Central de Configurações. |
| `IGNORA_VENDA_FRACIONADA_NO_BRINDE` | S/N | IGNORAR FRAÇÃO DO ITEM DO BRINDE |
| `CODCOB_MARVIN` | NUMBER | Código da cobrança que sera usada para o pagamento Marvin |
| `CONSULTA_MAXPAG_SERVICO_ADQUIRENTE_MARVIN` | NUMBER | Valor que sera informado na propriedade servicoAdquirente da API do maxPag para buscar recebíveis Marvin (Consultar Agenda Recebíveis = |
| `PERMITE_FILIAL_NF_NULA` | S/N | Aceita salvar pedidos sem filialNF quando habilitada permissão para selecionar via spinner na apk. FilialNF idêntica à filial do cabeçalho conforme parâmetro COMPORTAMENTO_WHINTOR_FILIAL = TRUE. |
| `HABILTAR_RELATORIO_DIARIO` | S/N | O relatório será buscado do endpoint api/v1/geolocalizacao/gerar-relatorio-diario-Rca MXPEDDV-55343 |
| `EXIBIR_PAUTA_TRIBUT` | S/N | Quando Ativo, será exibido o campo mxstribut.pauta |
| `PERMITE_EDITAR_PEDIDO_COM_BRINDE` | S/N | Quando parâmetro 1552 - CON_GERARBRINDEPEDBONIFIC estiver cadastrado como 'N' (false) no Winthor (rotina pedidos que gerarem itens de brinde vinculados (pcpedi.brinde = 'S') poderão ser editados caso este parâmetro estiver como 'S' (true). |
| `LIBERAR_BONIFIC_AUTORI_VINC_TV1` | S/N | Ao habilitar este parametro e ao realizar um pedido bonificado, onde o mesmo for vinculado a um pedido normal, não enviar para a autorização de limite de ou autorização de cliente bloqueado. Demais autorizações em pedidos bonificados vai subir para o maxGestão normalmente Trabalha em conjunto com o parametro VINCULAR_TV5_COM_TV1_FINAL_PEDIDO |
| `GRAVAR_LOG_GERAR_INDENIZACAO` | S/N | gravar informação ao realizar indenização |
| `INFORMAR_QUANTIDADES_BRINDES` | S/N | Informar quantidade no fluxo de brinde |
| `ENVIA_NUMPED_PED_COMPLEMENTAR` | S/N | Grava o NUMPED no lugar do NUMPEDRCA na propriedade "CodigoPaiPedidoComplementar" quando parâmetro ENVIA_NUMPED_PED_COMPLEMENTAR OUTROS_ERP estiver habilitado. |
| `VALIDA_RESTRICAO_VENDA_MENU_PRODUTOS` | S/N | quando habilitado validará as restrições de venda (CODPROD, NUMREGIAO, CODFORNEC, CODUSUR, CODEPTO, CODSEC, CODSUPERVISOR, CODFILIAL, CODPLPAG, CODMARCA, ORIGEMPED) no menu |
| `HABILITA_CANCEL_PED_DESMEMBRADO` | S/N | Se este parâmetro estiver habilitado, irá cancelar simultaneamente o pedido original e seu pedido desmembrado quando o pedido for editado ou cancelado via maxPedido. Válido para pedidos que foram desmembrado dentro do ERP WINTHOR via rotina etc. Parametro para extrator |
| `DESMEMBRAR_PED_FILIAL_RETIRA` | S/N | Se trabalhar com filiais retira diferentes nas negociações dos produtos (aba tabela), ao salvar o pedido, ele desmembrado em vários outros conforme as filiais dos produtos. O pedido desmembrado assumirá cabeçalho do pedido conforme a filial retira desmembrada. Parâmetro para desmembramento de pedido por pagamento (HABILITA_PLPAG_PRODUT - cliente deve OERPS) é prioritário, ou seja, o pedido será desmembrado por plano e não por filial retira. |
| `PROCESSAR_NOTA_AUTO_PRONTA_ENTREGA` | S/N | Se vai aceitar o manifesto do pronta entrega automaticamente caso for TRUE. Se parametrizado FALSE, o vendedor tem que aceitar o carregamento Consultas > Carregamento Pronta Entrega (fluxo somente na V2, na V3 tem que deixar por default |
| `SEARCH_PEDIDO_FORCAR_CAMPANHA_BRINDE` | S/N | Quando mesmo está habilitado, será possível selecionar apenas 1 campanha de brinde para inserir os itens pedido. ou seja, o pedido como um todo, só terá vinculados na campanha de brinde selecionada. Trabalha em conjunto com o parâmetro DESABILITA_GERACAO_BRINDE_AUTOMATICO para somente um pedido OERPs seguindo o mesmo fluxo Winthor, ou seja, a integração irá gerar o brinde automático através da propriedade no json: CampanhaBrindeSelecionada |
| `PERMITE_CANCELAR_PED_MONTADO_BALCAO` | S/N | Permitir cancelar pedido balcão reserva montado |
| `PERMITE_EDITAR_PED_MONTADO_BALCAO` | S/N | Permitir editar pedido balcão reserva montado |
| `DESABILITA_GERACAO_BRINDE_AUTOMATICO` | S/N | Se habilitado, irá gerar somente um pedido OERPs seguindo o mesmo fluxo do Winthor, ou seja, a integração irá gerar o brinde automático através da propriedade json: CampanhaBrindeSelecionada. Se tiver desabilitado não existir, irá criar dois pedidos (TV1 + TV5) seguindo fluxo padrão para OERPS. Trabalha em conjunto com parâmetro SEARCH_PEDIDO_FORCAR_CAMPANHA_BRINDE |
| `CALCULAR_ST_SAIDA` | S/N | O parâmetro visa identificar a alíquota de ST Saída cadastrada nos campos MXSTRIBUT.ALIQSTSAIDA MXSTRIBUT.ALIQSTSAIDAPF. |
| `ESCALA_COR_DESC_TABELA_PRECO` | S/N | Quando o parâmetro ‘ESCALA_COR_DESC_TABELA_PRECO’ estiver habilitado, e com os campos de preço mínimo preço de venda médio preenchido irá trazer na lucratividade a cor de acordo com a faixa de preço. |
| `HABILITA_MAPA_OPORTUNIDADE` | S/N | Habilita o mapa de oportunidades no maxPedido |
| `ATIVAR_DELAY_RECALCULO_NEGOCIACAO` | S/N | Criado para ser ativado em aparelhos com baixo desempenho. O padrão do sistema é fazer o recálculo preço a cada digitação, em aparelhos com baixo desempenho isso pode causar certa lentidão na digitação. Assim, ao ativar o parâmetro o recálculo só será feito 1 segundo que parar de digitar, melhorando a usabilidade para esses aparelhos. |
| `HABILITA_CNPJ_CPF_LISTAGEM_CLIENTES` | S/N | Quando ativo, o campo de CNPJ/CPF vai ser apresentado na listagem de clientes. Obs: Só funciona no novo |
| `GERAR_DADOS_CESTABASICA` | S/N | Parâmetro deve ser cadastrado na PCMXSCONFIGURACOES. Se false ou não existir, gerar o preço fixo para cesta básica, ou seja, não preço fixo cadastrado nas MXSPRECOCESTAC e |
| `PERMITE_TV13_SEM_CARREGAMENTO` | S/N | =S o app permite salvar um pedido 'TV13 - reabastecimento' mesmo quando não existe carregamento vinculado ao usuário |
| `EXIBIR_OBSERVACAO_HISTORICO` | S/N | Possui valor default como verdadeiro. Quando configurado como false, vai exibir a observação da MXSPEDIDO da MXSHISTORICOPEDC. |
| `HABILITA_FILIAL_RETIRA_FILIAL_PRODUTO` | S/N | Com o parametro habilitado, ao abrir a tela de negociação devera apresentar como padrão a filial da mxsprodfilial.codfilialretira referente a filial do cabeçalho pedido; Com o parametro desabilitado, deve seguir comportamento normal do aplicativo para validação filial retira; |
| `CANCELA_PEDIDO_AUTORIZACAO` | S/N | Com o parâmetro ativado, fará com que o APK identifique esse parâmetro e inclua no DTO do pedido (em pedidos.configurações) uma tag de identificação. indicará que o pedido integrado deve ser cancelado de seguir para o fluxo de edição e posteriormente aprovação. (Default = N) |
| `GPS_TRACKING_REAL_TIME` | S/N | Gps em tempo real. |
| `GRAVA_LOG_ERRO_RELATORIO_800` | S/N | Se ativar o parâmetro GRAVA_LOG_ERRO_RELATORIO_800, irá mostrar toast do fluxo de download até abrir o e gravar na tabela LOGJSON um registro dos fluxos poder analisar o usuário e identificar o que possa ocorrendo no aparelho dele. |
| `NAO_ATUALIZAR_HISTORICO_ITENS` | S/N | Quando o parâmetro estiver habilitado, não se deve atualizar o histórico de nenhum pedido da timeline aplicativo. |
| `TURNOS_ENTREGA` | TEXT | Inserir conforme regra do cliente (T,M,TN,MN) |
| `HABILITA_SISTEMA_GERA` | S/N | Quando habilitado, validar o fluxo GERA |
| `GUID_DISTRIBUIDOR_GERA` | S/N | Código fornecido pelo cliente/gera |
| `FUNCTION_KEY_GERA` | TEXT | Código fornecido pelo cliente/gera |
| `DISTRIBUIDORES_GERA` | TEXT | CODFORNEC da gera separados por vírgula (,) sem espaço. [Pegar com cliente/gera] |
