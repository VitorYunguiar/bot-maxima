# GATE-32 - Preço unitário na tela de negociação

**Contexto**

Cliente quer que seja exibido o preço unitário na tela de negociação. Ja foram criados os parâmetros EXIBIR_VALOR_UNITARIO e EXIBE_PRECO_UNIT_LISTAGEM porem ainda exibe apenas o valor total. Alterado na base da APK o PVENDA para 10 e o MXSEMBALAGEM.QTUNIT para 12 na intenção de verificar se era a falta de informação de valor unitário e quantidade de unidades na embalagem porem o campo segue inalterado

Cliente: 1718
Produto 941

**Passos para reproduzir**

- Logar no maxPedido
- iniciar pedido para cliente 1718
- Abrir produto 941
- Verificar que não é exibido o valor unitário do produto, apenas o valor total

**Diagnostico e orientacao**

Para o cliente trabalhar com a informação "Valor Un:" o primeiro passo é desativar a permissão "Exibir Valor Total" do cadastro do RCA ou do Perfil de usuários

Em seguida, o parâmetro EXIBIR_VALOR_UNITARIO deve ser configurado = S (Sim)

E por fim, o cliente precisa alterar a informação da quantidade Unitário do produto no cadastro da rotina 203. No banco de dados nuvem é a QTUNIT da MXSPRODUT, no banco do Winthor é a QTUNIT da PCPRODUT

**Evidencias tecnicas**

Para validar o cenário, acessar o inspect e setar

UPDATE MXSPRODUT SET QTUNIT = 20 WHERE CODPROD IN(941)

Lembre-se de averiguar o parâmetro e a permissão

# GATE-38 - Margem de lucratividade não altera

**Contexto**

Após parametrizar para exibir os campos de lucratividade foi verificado que os campos estão apresentando uma margem de lucratividade que inicialmente não faz sentido. Ocorre que ao inserir um produto, independente da quantidade de desconto aplicada, a margem de lucratividade permanece em 92.98% ou 92.99%

Gostaria de entender qual cálculo está sendo feito

**Passos para reproduzir**

- Acessar APK
- Iniciar pedido
- Adicionar um item
- Observar como a lucratividade do item se comporta inserindo desconto/acréscimo no produto

**Diagnostico e orientacao**

Cenário utilizado

Cliente: 103786

Produto: 5400100

O cálculo de lucratividade aplicado ao produto é o seguinte: ((61.74 - 4.3318) / 61.74) * 100 resultando nos 92,98% de lucratividade. Esses 4.3318 são referentes ao custo financeiro do produto que é calculado da seguinte forma: MXSTABPR.PVENDA1 * (MXSTRIBUT.CODICMTAB / 100). Atualmente, esse é o cáculo em todos os produtos deles e ele ocorre devido a esse parâmetro estar desativado (DESCONSIDERAR_IMPOSTOS_CALCULO_LUCRATIVIDADE = N), com esse parâmetro desativado, validamos a tributação para calcular o custo finanaceiro que é utilizado no cáculo de lucratividade do item

O que acontece se ativar o parâmetro DESCONSIDERAR_IMPOSTOS_CALCULO_LUCRATIVIDADE?

Então a gente simplifica o cáluclo de lucratividade e passa a buscar o custofinanceiro diretamente da MXSEST.CUSTOFIN, como está 0,01, então o resultado da lucratividade seria 99,98%

Quando é colocado desconto, então, ocorre o seguinte

Por exemplo: 80% de desc

PVENDA = 12.35

Lucratividade: (PVENDA - CUSTOFIN) / PVENDA

(12.35 - (12.35 * 0.07 + 0.01)) / 12.35
Sendo: 0.07 o CODICMTAB e 0.01 o custo real original CUSTOREP da MXSEST

(12.35 - 0.8745) / 12.35

11,4755 / 12.35
Esse cálculo vai resultar no 92.92%

# GATE-44 - Caso em uma REDE DE CLIENTE, um deles for bloqueado, impedir pedidos na rede toda

**Contexto**

O cliente quer que bloqueie realizar pedidos quando o cliente PRINCIPAL ou algum cliente SECUNDARIO de uma rede de clientes, estiver bloqueado

Exemplo: Drogasil e uma rede de clientes, codcli 333,334,335,336,337 e 338
se o 334 ta bloqueado, o cliente quer que NENHUM dos outros clientes possam realizar pedidos

**Passos para reproduzir**

- Ao realizar pedidos para o cliente bloqueado, ele permite continuar e emitir um orçamento

**Diagnostico e orientacao**

A parametrização a seguir vai forçar o sistema a validar cliente bloqueado no código principal e impedir o RCA de confeccionar o pedido

BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ = S
ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO = N

PERMITE_ORCAMENTO_CLIENTE_BLOQ = N
PERMITE_ORCAR_CLIENT_BLOQ = N

ACEITAVENDAAVISTACLIBLOQ = N

Versão analisada 3.248.1 – Porém funciona praticamente em qualquer versão porque a última alteração foi em 2021 nesse fluxo

Foi possível solucionar o caso sem precisar de correção. Abaixo vou passar os detalhes

Parametrizações maxPedido
ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO = N
ACEITAVENDAAVISTACLIBLOQ = N
BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ = S
PERMITE_ORCAMENTO_CLIENTE_BLOQ = S

Parâmetros da 132
CON_ACEITAVENDABLOQ tanto faz se S ou N
CON_VERIFICARCLIENTESREDE = S (já está)

No cenário verificamos 3 clientes da mesma rede sendo o 2258 o principal

SELECT CODREDE, CODCLI, CODCLIPRINC, CLIENTE, FANTASIA, BLOQUEIO, BLOQUEIOSEFAZ, BLOQUEIODEFINITIVO, CODUSUR1, CODUSUR2, CODUSUR3
FROM MXSCLIENT WHERE CODCLI in (2258,8922,114809) ORDER BY CODCLIPRINC DESC

O que ocorre, quando o principal está bloqueado, não é validado o parâmetro ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO de forma a impedir a venda e permitir somente orçamento

Para barrar quando o principal está bloqueado, o parâmetro BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ entra na atuação

Então com isso precisamos dos dois parâmetros trabalhando juntos
BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ e ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO

Quando pelo Winthor o cliente bloqueia um cliente do RCA, além da MXSCLIENT BLOQUEIO = 'S', é gerada uma tabela com o registro do bloqueio que é a MXSCLIENTESBLOQUEADOS. O maxPedido usa a informação nessa tabela para validar clientes da mesma rede bloqueados, por isso você não conseguiu a validação antes, porque como a gente tá fazendo aqui manualmente, então precisei fazer um insert nessa tabela que citei

Então quando você tem qualquer outro cliente da rede, que não seja o principal bloqueado, por exemplo, o 114809, o sistema valida o parâmetro ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO, e então ocorre o comportamento que o cliente quer. Nenhum cliente da mesma rede, ligados pelo codcliprinc, podem transmitir pedido enquanto um estiver bloqueado

# GATE-47 - Preço Fixo não valida para Filial 07

**Contexto**

- O preço fixo para o produto 8153 destinado a filial 07 e 50, não está sendo apresentado no APP

- Foi feita a atualização do ambiente nuvem e local do cliente, no qual estava divergênte e nesse processo o preço fixo para filial 50 tornou a validar, porém para filial 07, mesmo com registro na base do RCA, não é apresentado

**Passos para reproduzir**

- Iniciar Pedido P/ Cliente: 4924
- Filial 07
- Produto: 8153
- +Info / Politicas Comerciais

**Diagnostico e orientacao**

O problema ocorre porque ao trocar a filial de venda de 50 para 7, "por baixo dos panos", a filialNF não é alterada junto

Na prática o que ocorre é o pedido inicia na filial 50 com filialnf 50. Quando o RCA troca para filial 7, a filialnf continua na 50. Com isso, a política de preço fixo não é validada porque a filial de venda é 7, mas a filialnf sendo 50, busca dados da região 50

O responsável por mudar esse comportamento, é o parâmetro IGUALAR_FILIALNF_AO_ALTERAR_FILIAL que não está cadastrado para todos os RCAs nesse cliente. Verifique no bd nuvem
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%IGUALAR_FILIALNF_AO_ALTERAR_FILIAL%'

Então uma das opções que eles tem para resolver essa situação é ativar esse parâmetro, colocando ele IGUALAR_FILIALNF_AO_ALTERAR_FILIAL = S

Uma recomendação minha, nem precisa avisar ao cliente porque não vai ter impactos negativos. Desativar o parâmetro FILIALNF_DEFINE_FILIAL_PEDIDO

Se o cliente quiser também optar por selecionar a filialnf nos pedidos, ele pode habilitar a permissão para os RCAs: "Permitir escolha da filial de emissão da NF

Não vai ter impacto para esse cliente configurar o sistema dessa forma, porque ele não usa filialnf nos cadastros dos clientes dele
Eu validei assim
SELECT * FROM MXSCLIENT WHERE CODFILIALNF IS NOT NULL AND CODOPERACAO <> 2

# GATE-50 - Relatorio de conta corrente puxando pedidos de março

**Contexto**

O relatório de conta corrente para o RCA Pedro (28) com filtro de data 10/09/2024 - 10/09/2024 está puxando pedidos feitos em março

Na segunda houve uma situação onde foi validado que registros da MXSHISTORICOPEDC estava com CODOPERACAO = 2 e tiveram que ser reenviados pelo ERP. Verifiquei que alguns dos pedidos com datas de março estao com DTATUALIZ = 10/09/2024

É possivel que o reenvio desses registros para a MXSHISTORICOPEDC estejam causando o erro no filtro da data do relatório? Cliente OERPs

**Passos para reproduzir**

- Verificar pedidos do relatório
- Verificar MXSHISTORICOPEC numped 216631

**Diagnostico e orientacao**

O que acontece é o seguinte, quando o ERP mandou os registros ativos no dia 10/09/2024 e isso foi no dia 10/09/2024 (na vida real), a nossa JOB nossa de movimentação de conta corrente, que esse cliente usa, movimentou fazendo a leitura do histórico desse 216631 e outros pedidos na mesma condição

Então a JOB fez a leitura da MXSHISTORICOPEDC e MXSHISTORICOPEDI devido ao dtatualiz e também porque o pedido está Faturado e movimentou o conta corrente para esse pedido (e isso pode acontecer com outros pedidos)

Quando a JOB é movimentada, gravamos um log na ERP_MXSLOGRCA, você até consegue consultar nessa tabela: SELECT * FROM ERP_MXSLOGRCA WHERE NUMPED IN(216631)

Como a JOB rodou no dia 10/09/2024, ela grava o histórico de movimentação do conta corrente nessa data. E o maxGestão usa uma consulta que busca dados nessa tabela para construir o relatório, por isso que, filtrando no mês de Setembro, traz dados do pedido de março, porque os registros foram atualizados em Setembro com posição de Faturado e houve uso de Conta Corrente nesses pedidos. O histórico do Conta Corrente é referente a movimentção de Setembro por isso é exibido no relatório

- *Não passar ao cliente*

Obs: Se o cliente não aceitar essa história, a gente pode mandar para N3, porém ele precisa fazer um levantamento com o Integrador deles, para nos passar a lista com os pedidos que eles reenviaram os históricos. E ainda não é garantido que nós façamos ajuste desses registros; A gente teria que verificar se tem como alterar as datas no histórico de conta corrente

# GATE-55 - Travar pedido BNF sem Saldo CC

**Contexto**

- Cliente estava se baseando no Parâmetro: ACEITA_BNF_SEM_SALDO_CC no qual irá barrar o pedido BNF caso o mesmo esteja sem saldo de conta corrente. Aparentemente o parâmetro se trata de MaxFarma, porém o mesmo deseja que todo pedido BNF / Trocas, no qual seja utilizado o saldo do RCA e o mesmo esteja negativo, seja barrado no MaxPedido

**Passos para reproduzir**

- Iniciar Pedido para qualquer cliente
- Alterar para BNF
- Inserir qualquer item e aplicar desconto que ultrapasse o limite do RCA
- Apresenta que o mesmo não possui saldo, é enviado para o gestão, porém é barrado na Integradora. Cliente quer barrar esse cenário já no MaxPedido

**Diagnostico e orientacao**

Versão validada 3.235.1, então acima vai validar tambémVersão validada 3.235.1, então acima vai validar também

Foi realizado teste, quando habilito parâmetros da forma que citei, o sistema apresenta a mensagem "produto excedeu crédito do RCA" nas *Bonificações*. No pedido normal deixa transmitir mesmo se ultrapassar

Eu habilitei os parâmetros no ambiente dele, mas configurei de forma para não barrar, para que o cliente possa optar por definir na regra dele se quer usar a configuração recomendada ou não. Atualmente está configurado por usuário ambos parâmetros e dessa forma

PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = S

IMPEDIR_ABATIMENTO_SEMSALDORCA = N

Primeiramente, esse parâmetro não valida na apk ACEITA_BNF_SEM_SALDO_CC. Ele nem existe para validar no maxPedido

Para barrar no maxPedido, impedindo de salvar o pedido, nós temos os parâmetros

PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N

IMPEDIR_ABATIMENTO_SEMSALDORCA = S

Se configurar com eles o sistema já vai barrar, impedindo o RCA de inserir o item no pedido caso ultrapasse o conta corrente disponível durante a bonificação

Plus: Enviar para a autorização de pedido parâmetros (valida pedido e bonificação)

Se quiser enviar direto para a aprovação de pedidos quando o saldo do RCA estiver insuficiente e ele ultrapassar o limite da política de descontos: parâmetro ENVIAR_PEDIDO_SEMSALDO_AUTORIZACAO = S

Esse é caso o conta corrente seja insuficiente e o RCA digitou desconto no pedido independente de ter política: Validar conta corrente do vendedor quando o desconto for dentro do teto máximo, caso não possua saldo deverá enviar o pedido para autorização.VALIDAR_CC_APROV_PEDIDO = S

# GATE-63 - Bloquear pedido acima do limite

**Contexto**

Cliente deseja impedir o RCA de salvar pedido que tem valor acima do limite de crédito do cliente. Foi criado o parâmetro BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE e feito as alterações informadas na tela de parametros. Tambem foi criado o parâmetro PERMITI_VENDA_AVISTA_SEMLIMITE, porem o pedido segue sendo enviado normalmente. Abaixo os parâmetros utilizados

BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE = S
CON_ACEITAVENDABLOQ = N
BLOQPEDLIMCRED = N
PERMITI_VENDA_AVISTA_SEMLIMITE = N

CODCLI = 26658

**Passos para reproduzir**

- Alterar os parâmetros na base da APK e verificar se o pedido é impedido de ser enviado

**Resultado apresentado**

Pedido é enviado normalmente

**Resultado esperado**

APK impedindo RCA de salvar e enviar o pedido caso o limite do cliente seja menor do que o valor total do pedido

**Diagnostico e orientacao**

Compreendi que o cliente gostaria que não deixasse nem salvar o pedido caso o limite de crédito fosse excedido e a cobrança utilizada fosse DH com plano de pagamento A VISTA

Verificando o comportamento do código atualmente, para cliente Winthor, que é o caso da PCM, sempre vai deixar salvar e bloquear ou salvar e enviar o pedido

Por padrão o parâmetro PEFRMITI_VENDA_AVISTA_SEMLIMITE vem = Não; E ele sempre entra no fluxo de validar o limite do cliente e passar a mensagem: "Cliente sem limite de crédito. Esse pedido será salvo mas poderá não ser processado no ERP

Conclusão, não tem configuração atualmente, para impedir o RCA de salvar o pedido. Pelo menos eu não consegui rastrear e fiz vários testes e leitura das configurações

Tem um caminho para seguir, existe uma configuração no Winthor que fala exatamente sobre esse ponto. Então eu recomendo validar com esse cliente na 316 com essa configuração do parâmetro dessa base de conhecimento

Se o Winthor deles não deixar salvar o pedido então pode subir uma demanda de erro para o maxPedido N3. Por que no caso nós estamos deixando e existe a possibilidade de eles não estarem deixando

# GATE-66 - Alterar cod.fábrica pela MARCA do produto na tela de pedido

**Contexto**

Cliente- Queremos alterar a informação cod.fábrica pela marca do produto na tela de pedido

Foi hablitado paremetro LIST_PROD_FIELD_MARCA (Exibe o campo Marca na Listagem de Produtos)

**Passos para reproduzir**

- Acessar maxPedido >> Iniciar pedido ou pesquisar produto >> Listagem de produto

**Resultado apresentado**

>> Ao habilitar parametro LIST_PROD_FIELD_MARCA, o cod.Fabricante será alterado para MARCA

**Resultado esperado**

>> Ao habilitar parametro LIST_PROD_FIELD_MARCA, o cod.Fabricante será alterado para MARCA

**Diagnostico e orientacao**

Realizando a leitura da demanda, compreendi que o cliente deseja trocar a informação que é apresentada no maxPedido, na listagem de produtos. No caso, ele quer trocar o Código de fábrica dos produtos pela descrição da marca dos produtos

Para obter esse comportamento, ele pode estar desabilitando o parâmetro HABILITAR_VISUALIZACAO_COD_FAB_PROD_TAB = N, isso vai ocultar o código de fábrica dos produtos na listagem

E habilitar o LIST_PROD_FIELD_MARCA, que vai exibir o campo da Marca do produto caso esteja cadastrado

# GATE-70 - Não apresenta opção para atualizar as coordenadas do cliente

**Contexto**

O cliente já tem ativo os parâmetros GPS_TRACKING_ENABLED = S e CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE = S e quando finaliza um pedido, não apresenta a mensagem se deseja ou não atualizar as coordenadas do cliente

Schema: JFRIOS_582_PRODUCAO
Service name: maxsolucoes-xios.cm35ayc6yrqh.us-east-1.rds.amazonaws.com

**Passos para reproduzir**

- Acessar o aplicativo
- Iniciar um pedido em qualquer cliente
- Salvar e enviar o pedido
- E assim irá ver que não aparece a mensagem para atualizar as coordenadas do cliente

**Resultado apresentado**

Não apresenta a mensagem para atualizar as coordenadas do cliente ao salvar e enviar um pedido

**Resultado esperado**

Que apresente a mensagem para atualizar as coordenadas do cliente ao salvar e enviar o pedido

**Diagnostico e orientacao**

Validei na versão 3.249.2, mas na versão do cliente vai funcionar também

A mensagem não estava sendo apresentada devido a falta da permissão "Solicitar autorização para alterar coordenadas do cliente", nesse fluxo de validação do parâmetro CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE, é validada se essa permissão está ativa, assim como o GPS_TRACK_ENABLED que foi citado

Essa permissão não vai literalmente solicitar uma autorização, essa mensagem não está muito coerente com o que a funcionalidade faz junto com o parâmetro "CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE", mas no final ela só é necessário mesmo para mostrar ou não a mensagem nesse fluxo

Essa permissão também é válida para atualizar coordenadas do cliente através do botão "Atualizar Coordenadas" que aparece quando você preciona o dedo no cliente antes de abrir um pedido, por exemplo. Ai nesse caso em específico ele pede autorização

Conclusão, para apresentar a amensagem de "Atualizar" ou "Não atualizar", é necessário ter a permissão e os dois parâmetros habilitados

# GATE-72 - Bloquear RCA de iniciar bonificação caso não tenha saldo de conta corrente

**Contexto**

gostaria de saber qual a parametrização necessária para bloquear que o vendedor inicie/envie um pedido bonificado caso não tenha saldo de conta corrente para tal, ou também se possível, permitir que ele insiria produtos bonificados somente até onde vai seu saldo de conta corrente

**Passos para reproduzir**

- Acessar APK
- Iniciar pedido em algum cliente
- Enviar um pedido normal
- Enviar um pedido bonificado vinculando ao pedido normal

**Resultado apresentado**

Mesmo o RCA tendo 11 mil reais negativos em saldo de conta corrente, o mesmo consegue enviar bonificações normalmente

**Resultado esperado**

Impedir o RCA de gastar o que não possui

**Diagnostico e orientacao**

Validado na versão 3.249.3, mas na do cliente também vai funcionar

Para ter o comportamento desejado deve ser configurado o parâmetro PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = 'N' diretamente na nuvem porque ao sincronizar o aplicativo faz a leitura desse parâmetro e insere em uma tabela chamada MXSCONFIG a informação
Por isso que só alterar o parâmetro na base da apk não resolve o caso, precisa ser alterado em nuvem e sincronizado o parâmetro PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N. Assim o comportamento já vai ser conforme solicitado. Ao colocar A venda Bonificação, se o saldo exceder ou for negativo, quando tentar inserir o item a mensagem será exibida: "Produto excedeu crédito do RCA." dessa forma impedindo de confeccionar o pedido Bonificado

Cenário
CODFILIAL 09
Tipo Venda Bonificação
Plano 26 - BONIFICACAO
Cobrança - BONIFICACAO

Aba TABELA qualquer produto, mas usei o 120812-2
Apertar para inserir, imagem apresentada do que ocorre (a msg)

# GATE-94 - Valor divergente do ERP

**Contexto**

O valor apresentado usando os mesmo filtros está divergente da rotina 146. Verifiquei o acesso a todos os fornecedores, porem quando são aplicados os mesmos filtros o valor sempre apresenta divergencia

**Passos para reproduzir**

- Entrar no maxGestão
- Buscar indicadores de acordo com os filtros mostrados

**Resultado apresentado**

Valor divergente da rotina 146

**Resultado esperado**

Valor igual ao Winthor

**Diagnostico e orientacao**

OBS *Não passar essa parte para o cliente, é só para você estar ciente*

- *O comportamento do maxGestão sempre foi assim, quando o cliente tem uma divergência entre histórico de itens e pedidos, os valores do maxGestão para venda transmitida não batem com a 146. Isso não se aplica a 111, a 111 tem que bater 100% em todos os casos porque lá a apuração é diferente; Se o cliente quiser que mesmo com essas condições que expliquei, os dados sejam compatíveis, então terá de solicitar melhoria para porque o maxGestão não faz o cálculo apurando por histórico de capas de pedidos.*

O que ocorre, referente a essa divergência é que a Rotina 146 realiza a apuração baseada no Histórico de Capas dos Pedidos (PCPEDC) fazendo a soma dos valores atendidos dos pedidos e que não foram cancelados

Não é exatamente como vou colocar abaixo que a 146 faz, mas serve de base para nos ajudar nas análises
{color:#739eca}SELECT{color}

{color:#c1aa6c}COUNT{color}(*),{color:#c1aa6c}SUM{color}({color:#00b8b8}VLTOTAL{color}),{color:#c1aa6c}SUM{color}({color:#00b8b8}VLATEND{color}),{color:#c1aa6c}SUM{color}({color:#00b8b8}VLTABELA{color})

{color:#739eca}FROM{color}

{color:#b788d3}MXSHISTORICOPEDC{color}

{color:#739eca}WHERE{color}

{color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/08/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color}) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'31/08/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} != {color:#cac580}'C'{color}

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color}({color:#c0c0c0}3{color})

{color:#739eca}AND{color} {color:#00b8b8}CONDVENDA{color} {color:#739eca}IN{color}({color:#c0c0c0}1{color},{color:#c0c0c0}5{color},{color:#c0c0c0}14{color},{color:#c0c0c0}9{color}){color:#eecc64};{color}

{color:#669768}--R$16797441.02 (VLATEND) {color}

Já o maxGestão por padrão, sempre fez por histórico de itens dos pedidos, porque a gente entende nesse conceito que traz uma informação mais real referente a apuração de pedidos
{color:#739eca}SELECT{color}

{color:#c1aa6c}COUNT{color}({color:#739eca}DISTINCT{color} {color:#00b8b8}NUMPED{color}),{color:#c1aa6c}SUM{color}({color:#00b8b8}QT{color} * {color:#00b8b8}PVENDA{color})

{color:#739eca}FROM{color}

{color:#b788d3}MXSHISTORICOPEDI{color}

{color:#739eca}WHERE{color}

{color:#00b8b8}NUMPED{color} {color:#739eca}IN{color}({color:#739eca}SELECT{color} {color:#00b8b8}NUMPED{color} {color:#739eca}FROM{color} {color:#b788d3}MXSHISTORICOPEDC{color} {color:#739eca}WHERE{color}

{color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/08/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color}) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'31/08/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} != {color:#cac580}'C'{color}

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color}({color:#c0c0c0}3{color})

{color:#739eca}AND{color} {color:#00b8b8}CONDVENDA{color} {color:#739eca}IN{color}({color:#c0c0c0}1{color},{color:#c0c0c0}14{color},{color:#c0c0c0}9{color},{color:#c0c0c0}5{color}))

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} != {color:#cac580}'C'{color}

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}{color:#eecc64};{color}

{color:#669768}--R$17055721.76 maxGestão {color}

# GATE-102 - Troca de usuário

**Contexto**

>> O cliente possui um RCA Anderson que é Supervisor e RCA, o mesmo realiza troca de CODUSUR pela central de configurações, e quando tenta retornar para a base dele no app, não apresenta nada, fluxo testado na V2 e V3

**Passos para reproduzir**

- Acessar Central de configurações / Acessar o cadastro do usuário do mesmo
- Trocar seu CODUSUR por outro
- Acessar MaxPedido
- Menu "Ferramentas" / Supervisor

**Resultado apresentado**

>> Apresenta em branco

**Resultado esperado**

>> Apresenta o seu usuário representante para trocar de base

**Diagnostico e orientacao**

Nesse caso não se trata de uma falha de sistema, vou explicar abaixo como a funcionalidade trabalha e também o motivo de não exibir nenhum RCA quando a troca é realizada diretamente via Central

A funcionalidade trabalha da seguinte forma: O Supervisor no caso 218, usa o maxPedido, com o código de RCA 218, por dentro do maxPedido, quando ele vai trocar de base para outro RCA, serão exibidos todos os RCAs que estiverem vincualdos ao supervisor 218 pelo CODSUPERVISOR da tabela MXSUSUARI e que estiverem ativos e também com licença liberada do maxPedido. Então quando o Supervisor pelo maxPedido dele troca de base, automaticamente na Central é atualizada a referência de Código de RCA para a base que ele selecionou, porém o código padrão dele se mantém 218, para que, quando ele for retornar para a base dele também seja exibida essa opção. E essa funcionalidade está normal, pelo menos na versão 3.251.4. Na V2 o conceito é o mesmo, apesar que pode estar com algum problema não tratado

Porque não aparece nenhum usuário quando é colocado direto um outro CODUSUR via Central de Configurações? Isso ocorre porque nenhum RCA da equipe 218 está ativo e com licença liberada do maxPedido, então apesar de conseguir acessar a base do RCA fazendo uma modificação direta pela Central, isso fere as validações que o aplicativo faz para que seja possível voltar para a base de origem, sendo necessário caso o usuário queira voltar, faça a alteração manualmente via Central

# GATE-105 - maxGestão com divergência do ERP

**Contexto**

O cliente reclama de divergencia no maxPedido com o ERP, analise do DEV, onde o maxGestão bate com o ERP nas sem devoluções, porém no geral, o maxGestão permanece incorreto

**Passos para reproduzir**

- os dados do ERP do cliente, assim como os cenários
- Validar os valores no maxGestao seguindo as datas dos relatórios

**Resultado apresentado**

>>O valor quando se retira as devoluções, bate com o valor total do cliente
>>Quando se pega os relatórios onde não existe devolução, o valor bate

**Resultado esperado**

>>Os valores do ERP e do maxGestao devem bater

**Diagnostico e orientacao**

eu disponibilizei, um txt com o sql que a Máxima realiza para apurar os dados, com as mesmas condições do maxGestão. Te mandei para você ter uma ideia de como são apurados os dados. OBS *NÃO PASSAR o arquivo 'SQL_FATURADOS'* para o cliente

No arquivo "Faturamento_Total_maxGestao_com_TV1_e_TV5" a gente extraiu os pedidos, os valores atendidos deles por item e quantidade que o ERP nos enviou e também o valor das devoluções por pedido somados

Quando somarem o campo VLATEND do excel , vão chegar no número R$943.740 que siginificam todas as vendas, incluindo bonificações e pedidos normais sem deduzir devolução

Essa apuração a gente faz baseada nos dados que a integração do ERP nos manda para a nuvem via API. Os principais endpoints que nós recebemos os dados são esses: ERP_MXSNFENT, ERP_MXSESTCOM, ERP_MXSNFSAID, ERP_MXSMOV, noMXSHISTORICOPEDC

Acredito que no caso de vocês, se corrigirem os dados no endpoint ERP_MXSMOV verificando nota a nota e os valores apresentados nelas, também cuidando com a data que foi incluída de faturamento delas, provavelmente resolve a informação divergente. Porque nós fazemos a soma do PUNIT * QT desse endpoint para obter o valor dos faturados

# GATE-136 - PCORCAVENDAI

**Contexto**

cliente abriu uma demanda solicitando que mudem a procedure do FV para que registre o CODDESCONTO na PCORCAVENDAI, pelo que o cliente me falou, quando o RCA ao fazer um orçamento, clica na opção "Salvar e Enviar Orçamento", o maxPedido grava nessas duas tabelas o orçamento, porém segundo o cliente, o campo CODDESCONTO não está sendo gravado

Conectei no ambiente do cliente e validei que não existe uma PCORCAVENDACFV ou PCORCAVENDAIFV

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

Se trata de melhoria alinhado com o P.O Cleyton, por gentileza, verificar com o cliente se ele quer seguir com o processo de melhoria e então encaminhar para N3 como épico

Fiz atualização do cliente e testei também na versão ponta maxPedido e banco de dados, atualmente o fluxo de gravar seria na PCPEDIFV e depois PCORCAI, porém a gente não grava a informação no bd do cliente e por isso seria melhoria e não apresenta a informação lá que ele deseja

O cliente gostaria da funcionalidade para

Essa informação é útil pra saber se o representante tá usando uma política circular do mês inteiro por exemplo, ou se é uma política especifica, e eu vou usar pra fazer o conta corrente da empresa esses dados

# GATE-137 - Transferência de flex

**Contexto**

Usuário Fabiano não está tendo acesso ao saldo CC do Edcarlos, para fazer transferência de de conta correte

**Passos para reproduzir**

- Acessar MaxGestão WEB ou APP
- Conta Correte / Gestão de conta corrente
- Procurar usuário Edcarlos

**Resultado apresentado**

>> Não apresenta o Edcarlos

**Resultado esperado**

>> Visto que o representante Edcarlos é vinculado ao seu usuário de supervisor, e o Fabiano tem acesso a sua equipe no seu perfil, logo era para aparecer no MaxGestão

**Diagnostico e orientacao**

Como o RCA EDCARLOS (como RCA) não tem nenhuma licença do maxPedido, então ele é considerado um "Usuário Geral" no maxGestão, e para movimentar o conta corrente dele usando o maxGestão, então o usuário do fabiano no maxGestão, precisa ter a permissão "Permite movimentar Conta Corrente do Usuário Geral para Vendedores" que fica localizada em Usuários >> Editar >> Permissões >> Conta Corrente >> Permite movimentar Conta Corrente do Usuário Geral para Vendedores

Com essa permissão, na aba de Gerenciar Conta corrente ele vai conseguir ver o usuário EDCARLOS como RCA para movimentar o conta corrente dele

# GATE-142 - Dashboard inicial sem valores

**Contexto**

- Após atualizar o ambiente nuvem e local do cliente, os valores na dashboard inicial não apresenta nada

**Passos para reproduzir**

- Acessar MaxPedido
- Atualizar Menu

**Resultado apresentado**

>> Dados atualizados
>> Porém não carrega nenhum valor

>> No resumo de vendas apresenta vendas faturadas

**Resultado esperado**

>> Que carregue os valores visto que todos os acessos externos estão liberados

**Diagnostico e orientacao**

Para atualizar o gráfico do menu de vendas, na Rotina 353 eles precisariam cadastrar a meta do RCA 145 mensal, porque eles não cadastraram ainda, a tabela PCMETARCA está vazia

Uma dica boa também para entender o funcionamento do gráfico do Menu inicial: Ele depende de a meta mensal estar definida, essa meta mensal fica na aba de Objetivos > Venda dentro do maxPedido, se o campo "Meta:" estiver assim R$0,00 então significa que não foi cadastrada a meta mensal

Então por isso que mesmo com acesso na 9002, não atualiza o menu deles com os resultados. Pelo o que analisei, seria somente isso, as PCDIASUTEIS e PCDATAS deles já estão corretas

Após cadastrarem a meta de venda mensal do RCA na 353 é só atualizar o menu e validar a mesma aba dentro de objetivos que os dados serão apresentados

Já sobre as outras informações da tela inicial (Pedidos e Objetivos)

- nada é apresentado porque o parâmetro CRITERIOVENDA está definido como "F" então só vai carregar a venda faturada do mês atual e como nenhum pedido foi faturado ainda desse RCA nesse Mês, nenhuma informação é apresentada

# GATE-144 - Vinculo de grupo de cliente MXSPRECOPROM

**Contexto**

gostaria de saber qual tabela faz o vinculo dos clientes do grupo que é utilizado no MXSPRECOPROM.CODGRUPOCLI

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

A Laredo é um cliente que usava essa função com a MXSDESCONTO, então em versões recentes isso precisa funcionar, na dúvida atualiza para a ponta. A ideia é que as política de preço fixo sejam validadas com grupos de clientes cadastrados

A gente integra esses grupos e relação com as campanhas nas tabelas MXSGRUPOSCAMPANHAC e MXSGRUPOSCAMPANHAI. Abaixo eu coloquei a relação que elas têm com a MXSPRECOPROM para validação dos preços fixos por grupo de clientes

MXSGRUPOSCAMPANHAC.codgrupo = mxsprecoprom.codgrupocli
MXSGRUPOSCAMPANHAI.codgrupo = mxsprecoprom.codgrupocli
MXSGRUPOSCAMPANHAI.coditem = codcli

- Se não estiver integrando corretamente do bd local para a nuvem ou não estiver funcionando conforme o esperado, por gentileza, me informar que eu posso estar revisando a funcionalidade

# GATE-145 - Oscilação na margem de lucratividade

**Contexto**

O Cliente enviou um problema relacionado a transformar orçamento em pedidos

Toda vez que essa transição acontece a margem de lucratividade muda drasticamente

Um video enviado foi enviado

Testes realizados + resultados nas versões
- *3.251.9*: Crash de apk ao transformar orçamento bloqueado em pedido
- *3.251.8*: Crash de apk ao transformar orçamento bloqueado em pedido
- *3.251.6*: Problema não encontrado em BASE DO ZERO
- *3.251.6*: Problema foi simulado exatamente como descrito BASE RCA

**Passos para reproduzir**

- BASE DO ZERO
- realizar um orçamento
- plano de pagamento e cobrança ( A VISTA e PIX )
- Adicionar um valor acima de 300 (Valor minimo da integradora)
- Checar a aba de totais do ORÇAMENTO
- Ir na timeline de pedidos e transformar o orçamento em pedido
- Checar a aba de totais do PEDIDO

**Resultado apresentado**

BASE DO ZERO NA VERSÃO 3.251.9
Crash de apk ao transformar o orçamento em pedido

BASE DO ZERO NA VERSÃO 3.251.8
Crash de apk ao transformar o orçamento em pedido

BASE DO ZERO NA VERSÃO 3.251.6
o problema não acontece

BASE DO CLIENTE NA VERSÃO 3.251.6
Diferença drastica na margem de lucratividade, onde no meu caso saiu de 30 pra 615

O video enviado enviado pelo cliente tambem mostra a situação

**Resultado esperado**

Identificar o motivo da margem de lucratividade oscilar tanto ao transformar o orçamento em pedido

Identificar o motivo do crash nas versões mais atualizadas

**Diagnostico e orientacao**

A lucratividade muda porque a gente tem uma funcionalidade no maxPedido que recalcula os preços dos produtos conforme a informação mais atual na base do RCA

Significa que no dia 03/10/2024 o orçamento tinha um custo e preço nos produtos. E no dia 04/10/2024, depois de sincronizar, já é outro preço e custo. Por isso ocorre um recálculo e muda drasticamente

Não cheguei a validar se a informação está correta a nível de cálculo, somente que ocorre um recálculo. E isso é devido ao parâmetro QTDE_DIAS_VALIDAR_ORC_IMPORTACAO por default ser 0, então ao importar de orçamento para pedido sempre recalcula. Ao editar não, somente ao importar. E isso pode ser mudado, por exemplo se você colocar QTDE_DIAS_VALIDAR_ORC_IMPORTACAO = 7, então até 7 dias de validade no orçamento ele não recalcula os preços e o custo

Um paliativo por enquanto, seria cadastrar o parâmetro QTDE_DIAS_VALIDAR_ORC_IMPORTACAO = 7, dai não ocorre aquele recálculo de comissão

Sobre o crash eu mandei para N3 para correção e pedi para no teste eles verificarem também se o valor de comissão está correto no recálculo

# GATE-147 - Pedido de brinde sendo enviado junto com o TV1

**Contexto**

Ao gerar um pedido com brinde é criado um pedido TV5 automaticamente, porem ele so é enviado para a nuvem depois que o pedido TV1 é liberado pelo ERP. Cliente deseja que os dois pedidos sejam enviados ao mesmo tempo, sem que o TV5 precise aguardar a liberação do TV1

Cenário utilizado

Cliente 10119
Produto 3911 - 15 unidades a R$155
Pedido TV1: 1022
Pedido TV5: 1023
Base

**Passos para reproduzir**

- Cliente 10119
- Produto 3911 - 15 unidades a R$155
- Pedido TV1: 1022
- Pedido TV5: 1023

**Resultado apresentado**

O pedido TV5 so subiu para a nuvem depois que o pedido TV1 passou para LIBERADO na apk

**Resultado esperado**

TV5 enviado para integração juntamente com o TV1, sem a necessidade de aguardar a liberação do pedido original

**Diagnostico e orientacao**

Sobre o comportamento do maxPedido: o pedido de bonificação é gerado e somente enviado para a nuvem da Máxima após o retorno do numpederp na crítica do pedido pai (TV1) no endpoint StatusPedidos

Mesmo que o erp dê o retorno instantaneamente pela api, para que essa informação seja carregada na aplicação é necessário que o RCA realize o swipe. Então existe atualmente uma dependência com o RCA realizar o swipe para essas bonificações serem enviadas para a nuvem da Máxima

O ERP pode rapidamente retornar a crítica do pedido com o NUMPEDERP no pedido principal, porém, somente depois que o RCA faz o swipe no maxPedido é que ele recebe essa informação no pedido principal e posteriormente realiza novamente o swipe, assim possibilitando o envio da bonificação para a nuvem

No momento, infelizmente, não temos configurações disponíveis para alterar esse comportamento, se o cliente quiser bater o pé, teria de ser analisado como Melhoria, dai você mesmo pode abrir a melhoria para N3

Um paliativo muito útil: temos trabalhado em uma novidade e tínhamos a intenção e previsão de liberar a sincronização automática dos pedidos e de outras informações do sistema já nesse mês. Com isso, ajuda nesses cenários onde a bonificação não sobe por dependência com o usuário do maxPedido, ela subindo de forma automática o sistema fica mais fluido. --Você pode também conversar com o cliente para ver se isso já ajuaria eles e se o cliente quiser depois alinhar diretamente com o Cleyton

# GATE-148 - Roteiro não gera na MXSCOMPROMISSOS

**Contexto**

Cliente é OERPs, o registro foi enviado para a ERP_MXSROTACLI e parece estar enviado corretamente, porém o roteiro não é gerado na MXSCOMPROMISSOS, tentei atualizar o banco nuvem porém não adiantou

**Passos para reproduzir**

- Acessar APK
- BANCO NUVEM
- SELECT * FROM MXSCOMPROMISSOS WHERE CODUSUARIO = 101402
- SELECT * FROM ERP_MXSROTACLI WHERE CODUSUR = 3844 ORDER BY DTPROXVISITA DESC

**Resultado apresentado**

Roteiro não é gerado na MXSCOMPROMISSOS

**Resultado esperado**

Gerar os roteiros

**Diagnostico e orientacao**

Estava com problema para gerar os compromissos no banco nuvem, foi corrigido com a atualização, assim que você atualizou e a job de compromissos rodou, foi gerada a agenda normalmente, para verificar você pode conferir sincronizando o maxPedido

Ou também consultando no {color:#cccccc}{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCOMPROMISSOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} = {color:#c0c0c0}101402{color}{color:#eecc64};{color}{color}

atualizado --3.1.3.353

- 2024-10-04 15:52:43.000

# GATE-151 - Pedido não atualiza status com a sync automatica

**Contexto**

Pedidos ja foram integrados e estão com status 4 porem na timeline de pedidos os status não são atualizados. Cliente usa sync automática e não pode fazer swipe

Tratado no ticket MXPEDDV-81866

Base

**Passos para reproduzir**

- Logar no maxPedido
- Verificar timeline de pedidos

**Resultado apresentado**

Status não são atualizados

**Resultado esperado**

Status atualizando normalmente

**Diagnostico e orientacao**

Os pedidos não estavam tendo o status atualizado automaticamente porque o usuário em específico, não estava configurado para trabalhar com a sincronização automática

- *Não passar essa info abaixo em negrito para o cliente:*

- *O campo USAMSGMAXSYNC não estava = S na MXSUSUARIOS do banco nuvem (Oracle) no CODUSUARIO 100967*

Então para resolver, a gente ativou essa configuração e reenviou os pedidos de forma a recriar a informação assíncrona para o usuário receber

Então agora esse RCA já pode estar validando os pedidos 800012, 800011, 800010 se os status foi atualizado automaticamente e também validar os próximos pedidos realizados

Lembrando como ele trabalha com sincronização automática, ele não pode usar otimização de bateria no maxPedido

Recomendo cadastrar o parâmetro BLOQUEAR_UTILIZACAO_BATERIA_OTIMIZADA = S

Precisa ser o RCA diretamente para validar, não baixa a base dele porque senão você rouba a sincronização automática

# GATE-154 - Histórico de compras não está batendo resultados

**Contexto**

Foi feita uma análise no banco de dados nuvem primeiro, fizemos um Select para saber o valor(SUM (Pvenda*qt)) que daria junto dos filtros que foram dados pelo cliente (codcli 216/codusur 62/posicao F/codfilial 1), levando ao valor "87.129,99775", olhando a tabela do zero (Segunda foto), o valor mesmo com uma divergência mínima(87.130,00), bate com o valor que apresenta no aplicativo, diferente do valor na base do cliente que deu 23.495,72, tendo uma divergência enorme, junto também do relátorio que ele mandou do mesmo cliente e mesmo RCA que deu 107.326,10

A gente foi analisar no banco de dados local do cliente assim procurando saber se havia uma divergência de bancos, porém, os valores do banco nuvem e banco local também bate seus valores, excluindo essa possibilidade

**Passos para reproduzir**

- RCA 62: login: exporfrios.62 | Cliente 216

**Resultado apresentado**

Há uma divergência nos valores dos bancos de dados (local e nuvem), em que os valores estão iguais, porém, em relação aos dados que o cliente apresentou s estão diferentes

**Resultado esperado**

Um resultado sem divergências naquilo que o cliente apresentou

**Diagnostico e orientacao**

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSPARAMETRO{color} {color:#739eca}WHERE{color} {color:#00b8b8}NOME{color} {color:#739eca}LIKE{color} {color:#cac580}'%SYNC%'{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSUSUARIOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}LOGIN{color} = {color:#cac580}'exporfrios.62'{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color}

{color:#c1aa6c}SUM{color}({color:#00b8b8}PVENDA{color} * {color:#00b8b8}QT{color})

{color:#739eca}FROM{color}

{color:#b788d3}MXSHISTORICOPEDI{color}

{color:#739eca}WHERE{color}

{color:#00b8b8}NUMPED{color} {color:#739eca}IN{color}(

{color:#739eca}SELECT{color}

{color:#00b8b8}NUMPED{color}

{color:#739eca}FROM{color}

{color:#b788d3}MXSHISTORICOPEDC{color}

{color:#739eca}WHERE{color}

{color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TRUNC{color}({color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/09/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'30/09/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})

{color:#739eca}AND{color} {color:#00b8b8}CODUSUR{color} {color:#739eca}IN{color}({color:#c0c0c0}62{color})

{color:#739eca}AND{color} {color:#00b8b8}CODCLI{color} {color:#739eca}IN{color}({color:#c0c0c0}216{color})

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color}({color:#c0c0c0}1{color})

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} = {color:#cac580}'F'{color}

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}

{color:#739eca}AND{color} {color:#00b8b8}CONDVENDA{color} = {color:#c0c0c0}1{color})

{color:#739eca}AND{color} {color:#00b8b8}CODOPERACAO{color} != {color:#c0c0c0}2{color}

{color:#739eca}AND{color} {color:#00b8b8}POSICAO{color} = {color:#cac580}'F'{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSPARAMETRO{color} {color:#739eca}WHERE{color} {color:#00b8b8}NOME{color} {color:#739eca}LIKE{color} {color:#cac580}'%CRITERIOVENDA%'{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCLIENTCHARTHISTVENDA{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODCLI{color} {color:#739eca}IN{color}({color:#c0c0c0}216{color}) {color:#739eca}AND{color} {color:#00b8b8}CODUSUR{color} {color:#739eca}IN{color}({color:#c0c0c0}62{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TRUNC{color}({color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/09/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'30/09/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}sync_d_mxsclient{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODCLI{color} {color:#739eca}IN{color}({color:#c0c0c0}216{color}) {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}53739{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSAPARELHOSCONNLOG{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}53739{color}) {color:#739eca}ORDER{color} {color:#739eca}BY{color} {color:#00b8b8}DTATUALIZ{color} {color:#739eca}DESC{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCONEXOESLOG{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}53739{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#00b8b8}DATA_INICIO{color}) {color:#739eca}BETWEEN{color} {color:#c1aa6c}TRUNC{color}({color:#c1aa6c}TO_DATE{color}({color:#cac580}'01/07/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color})) {color:#739eca}AND{color} {color:#c1aa6c}TO_DATE{color}({color:#cac580}'30/07/2024'{color}, {color:#cac580}'DD/MM/YYYY'{color}){color:#eecc64};{color}

- *Não passar essas informações em negrito para o cliente*

- *A nossa funcionalidade é alimentada por uma job nossa da Máxima que possui regras próprias para apurar e apresentar essa informação no maxPedido.*

- *A tabela que alimenta a informação no maxPedido é a MXSCLIENTCHARTHISTVENDA*

- *Não foi possível identificar a causa da informação não ter descido sozinha via sincronização para a base da RCA porque é um dado de Setembro que deveria ter descido com sicnronização realizada na época, mas a gente não guarda logs dessa data para analisar então não tem evidência para analisar nos restando realizar a carga.*

A informação na base do maxPedido do RCA de fato estava incorreta, para resolver esse cenário a gente realizou uma carga da tabela MXSCLIENTCHARTHISTVENDA desde Setembro até o dia atual. Para ela e outros RCAs com possíveis divergências receberem a informação, eles precisam estar sincronizando o maxPedido, somente

O valor que vai constar na base do RCA referente ao mês de Setembro é R$87129.99775 ~= 87130

O valor que o Winthor dela apura é referente a Data de Faturamento de pedidos, por isso a informação diverge bastante, porque você pode ter pedidos faturados que não correspondem a data de emissão do pedido

Em outras palavras o Winthor, na rotina que ela apurou, faz de um jeito, e a nossa funcionalidade faz de outro, os dados nunca vão ser compatíveis da forma que ela apurou

O valor que a nossa aplicação está apresentando pode ser considerado correto, é o esperado pela nossa funcionalidade. Se a cliente quiser mudar esse conceito (o valor que é exibido) seria uma melhoria, dai você pode entender com a cliente a necessidade que ela tem e subir diretamente um ticket de N3 épico

# GATE-162 - Resumo de venda não atualiza

**Contexto**

>>Ao clicar em Atualizar menu o sistema exibe um erro

Não foi possível atualizar o resumo de vendas
Tente novamente mais tarde

**Passos para reproduzir**

- Abrir a base do zero do RCA 158 ou outro
- Clicar em atualizar menu

**Resultado apresentado**

>>O sistema exibe o erro
Não foi possível atualizar o resumo de vendas
Tente novamente mais tarde

**Resultado esperado**

>>Que o menu seja apresentado sem erros

**Diagnostico e orientacao**

Eu verifiquei juntamente com um desenvolvedor e acreditamos que para o menu de vendas atualizar com sucesso só está faltando o cadastro das datas no Winthor na Rotina 309, essa rotina alimenta a tabela PCDATAS que validamos ao fazer a requisição para atualizar esse menu da tela inicial. Dai teria de ser cadastado desse e dos outros meses para evitar que ocorra nos meses seguintes também

No caso precisa orientar o cliente sobre esse cadastro da rotina 309 para o mês vigente, essa validação é importante para outras funcionalidades do força de vendas, além dessa atualização do Menu inicial. E feito isso no Winthor, pode estar validando a atualização do Menu inicial. Se por acaso continuar dando errado, por gentileza, nos acionar novamente

Para validar, depois de cadastrar no Winthor as datas, acredito também que será necessário relogar no usuário no maxSoluções. Deslogar no usuário e depois logar novamente e então mandar atualizar

- *Não passar ao cliente: O link do cliente t-cloud no cadastro na nuvem do extrator dele estava com http e não https; http não é para ser. E como estava esse link errado então infelizmente precisa relogar no maxsoluções como expliquei acima*

# GATE-174 - Replicador MXSUSUARIOS

**Contexto**

Cliente informou que o registros dos RCAS 2543(cadastrado 07/10/2024) e 2544 (cadastrado 09/10/2024) não foram encontrados na tabela MAXSOLUCOES.MXSUSUARIOS, o que indica que a replicação não está funcionando

Alinhado com o Filipe Padilha

**Passos para reproduzir**

- Validar informações na descrição

**Resultado apresentado**

Dados não estão sendo replicados

**Resultado esperado**

Dados replicados

**Diagnostico e orientacao**

Foi reativado o replicado do cliente que estava parado desde o dia 21/09/2024 por uma causa que ainda não identificamos; No caso o problema dos dados não aparecerem foi resolvido com a reativação do replicados mas a causa raíz para ter parado de funcionar ainda não, por isso vou enviar N3

O cliente já pode estar verificando no banco dele que os dados desses RCAs que eles vão estar lá
{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSUSUARIOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUR{color} {color:#739eca}IN{color}({color:#c0c0c0}2543{color},{color:#c0c0c0}2544{color}){color:#eecc64};{color}

# GATE-177 - Obrigar sequenciamento de visitas

**Contexto**

O cliente gostaria de obrigar um sequenciamento das visitas no MaxPedido

Exemplo o RCA tem no seu roteiro do dia 11/10 os clientes
Cliente 1
Cliente 2
Cliente 3
RCA realizou o atendimento no cliente 1, e já seguiu para o cliente 3, nesse momento o cliente quer que o aplicativo barre o atendimento ao cliente 3, obrigando o RCA a fazer o atendimento do cliente 1 primeiro. Com essa ideia o cliente obriga o RCA a seguir todo o seu roteiro naquele dia, entendo que temos parametrizações para bloquear a rota pendente, mas o bloqueio ocorre somente no outro dia

O que o cliente precisa é que o RCA siga com todas as suas visitas na sequencia, sem pular de fazer check-in/out, justificativa de não venda ou pedido nos clientes do roteiro do dia

Testamos isso habilitando a permissão: Obrigar sequenciamento de visitas e habilitando o parâmetro OBRIGAR_ATENDIMENTO_PARA_CHECKOUT, mais o RCA conseguiu não seguir o sequenciamento das visitas

**Passos para reproduzir**

- Acessar o aplicativo
- Ir na tela de clientes
- Iniciar um pedido no primeiro cliente do roteiro
- Fazer check-in, justificativa de não venda e gravar o check-out
- Seguir para o terceiro cliente do roteiro
- E assim o aplicativo não barra nada, ou seja não obriga o RCA seguir o sequenciamento das visitas

**Resultado apresentado**

Aplicativo não obriga o RCA a seguir o sequenciamento de visitas

**Resultado esperado**

O que o cliente precisa é que o RCA siga com todas as suas visitas na sequencia, sem pular de fazer check-in/out, justificativa de não venda ou pedido nos clientes do roteiro do dia

**Diagnostico e orientacao**

- Foi feita análise na versão ponta 3.253.3

Para obrigar o sequenciamento nos clientes do Roteiro

Permissões na Central
Bloquear venda de clientes fora da rota = V
Obrigar sequenciamento de visitas = V

Parâmetro: UTILIZA_CHECKIN_CHECKOUT = S

Com essas permissões para fazer um atendimento fora de rota o RCA sempre vai precisar gerar uma visita avulsa, pressionando em cima do cliente que não é do roteiro atual. Dai ao gerar a visita avulsa ele vai conseguir atender fora de rota e sem seguir sequência. Porém os clientes da Rota, ele vai ser forçado a seguir a sequência

Se você quiser testar antes de entregar ao cliente, eu deixei o usuário jfrios.TI pronto com essas configurações

- *Obs: Não passar ao cliente, analisando eu não encontrei outra forma de configurar, para obrigar a sequência no roteiro precisa ter as duas permissões que citei acima*

!image-2024-10-14-09-42-44-204.png!

Se quiser atender fora de rota (só para clientes fora do roteiro atual)

!image-2024-10-14-09-43-21-078.png!

!image-2024-10-14-09-43-38-077.png!

!image-2024-10-14-09-44-01-263.png!

!image-2024-10-14-09-44-55-864.png!

!image-2024-10-14-09-45-34-608.png!

# GATE-182 - Informações de venda não aparecem na filial 5

**Contexto**

Estou com uma situação no maxGestão onde ao pesquisar as informações no Painel Geral, não retorna nada ao selecionar a filial 5

Foi verificado na ERP_MXSNFSAID, MXSHISTORICOPEDC, MXSHISTORICOPEDI e os supervisores e cobranças utilizados nos pedidos, tudo parece estar correto, não encontrei o que está causando o problema de não gerar os dados

**Passos para reproduzir**

- Acessar maxGestão
- Painel Geral
- Filtrar data inicial 01/10 até dia atual
- Filtrar filial 5
- SELECTS UTILIZADOS
- SELECT CODCOB, CODSUPERVISOR, CODOPERACAO, MXSHISTORICOPEDC.* FROM MXSHISTORICOPEDC WHERE CODFILIAL = 5 ORDER BY DATA DESC
- SELECT CODOPERACAO, MXSHISTORICOPEDI.* FROM MXSHISTORICOPEDI WHERE NUMPED IN(SELECT NUMPED FROM MXSHISTORICOPEDC WHERE CODFILIAL = 5) ORDER BY DATA DESC
- SELECT * FROM MXSSUPERV WHERE CODSUPERVISOR IN(44, 45, 42, 43, 27, 33, 39, 33)
- SELECT * FROM MXSCOB WHERE CODCOB = 'BK'
- SELECT * FROM ERP_MXSNFSAID WHERE CODFILIAL = 5 ORDER BY DTSAIDA DESC

**Resultado apresentado**

Ao pesquisar a filial 5 não retorna dados nos indicadores, permanecendo 0. O problema não ocorre nas outras filiais

**Resultado esperado**

Entender o que está impedindo os dados de serem exibidos no maxGestão

**Diagnostico e orientacao**

Para resolver a situação eu realizei uma atualização do ambiente nuvem do cliente e verifiquei se ele possuía todos os acessos a fornecedores na aba abaixo

!image-2024-10-15-13-31-48-850.png!

Então após fazer esse procedimento, eu validei novamente os indicadores do mês atual usando o usuário sysmax e os dados foram apresentados normalmente, tanto na venda transmitida quanto na faturada para a Filial 5

Outro detalhe, eu removi a licença do sysmax e coloquei novamente na aba de versões porque como ele tem dois ambientes, às vezes pode ocorrer algum problema ao fazer a troca de licenças para usar nos ambientes

Se algum outro usuário do cliente ainda não estiver apresentnado dados, pode ser alguma questão de permissão de acesso no perfil do usuário específico

# GATE-183 - Replicador causando lock de banco

**Contexto**

Cliente informou que após alterar o horario de execução do replicador de 18h para 16h ocorreram locks no banco local devido ao replicador

**Resultado apresentado**

Ocorrendo locks no banco devido ao replicador

**Resultado esperado**

Não ocorrer locks no banco

**Diagnostico e orientacao**

Voltamos a hora para disparo do Replicador para as 18h, porém não sei se só isso iria resolver o lock que está ocorrendo, porque o lock pode ser devido a outro motivo

O lock para a gente saber o motivo precisa estar ocorrendo na hora, então eu recomendo que o cliente deixe o lock e nos acionar caso ocorra novamente. Se ele identificar o motivo, também é válido para a gente entender o que causa, porque o DBA também pode investigar locks no banco de dados local

Já sobre os logs que ele mandou a gente fez a correção no banco de dados na coluna CODUSUARIO das tabelas MXSUSUARIOS e MXSCOMPROMISSOS porque teve um aumento desse campo em uma alteração recente na nuvem

Também foi feita a carga dos dados que não haviam gravado corretamente dos compromissos devido ao erro

O Replicador não usa o processador.dll que está acusando no lock por isso acredito que as coisas não tenham relação

# GATE-189 - Mesmo cumprindo o roteiro do dia anterior, está pedindo desbloqueio no outro dia

**Contexto**

Conforme alinhado via Discord com o Filipe, esse é um assunto recorrente com o cliente. Eles utilizam um parâmetro que bloqueia a rota do dia seguinte caso o roteiro do dia anterior não tenha sido concluído. No entanto, o cliente continua abrindo diversos tickets informando que, mesmo o RCA cumprindo todo o roteiro do dia, a rota do dia seguinte ainda é bloqueada

Essa questão já foi encaminhada para o desenvolvimento e tratada no ticket MXPEDDV-80135, no qual foi habilitado o parâmetro PERMITIR_DELETE_HISTORICOCOMP, mas a situação ainda persiste

Na análise realizada, foi verificado que o RCA cumpriu todo o roteiro no dia 15/10. No entanto, hoje (16/10), foi solicitada a liberação da rota, pois o sistema bloqueou o acesso, alegando que o roteiro do dia anterior não foi cumprido

O roteiro de visitas criado pelo roteirizador de vendedores incluía 17 clientes. No sistema ERP_MXSVISITAFV, constam 16 visitas realizadas e 3 pedidos integrados em clientes dentro do roteiro. Além disso, o relatório extraído do painel de auditoria do sistema de gestão também confirma que o RCA completou todas as visitas planejadas para o dia 15/10

**Passos para reproduzir**

- Acessar o aplicativo
- Importar a base anexada
- Tentar iniciar um pedido em qualquer cliente do roteiro de hoje dia 16/10
- E assim retorna a mensagem informando que não cumpriu todo o roteiro do dia anterior

**Resultado apresentado**

Mesmo que o RCA tenha concluído todo o roteiro do dia anterior, ao iniciar o roteiro no dia atual, é solicitado o desbloqueio, informando que o roteiro do dia anterior não foi cumprido

**Resultado esperado**

Que quando o RCA tenha cumprido todo o roteiro do dia anterior, não fique bloqueando de iniciar o pedido no roteiro atual

**Diagnostico e orientacao**

Para o cliente você pode dizer que foi feita somente uma normalização dos registros, de forma que ajustamos os compromissos para validar corretamente de agora em diante quando o RCA cumprir todo o roteiro não ficar apresentando no aplicativo como se não tivesse cumprido

- *Não passar ao cliente detalhes abaixo, vou explicar só para você entender o que houve e ficar registrado:*

Basicamente o registro no banco nuvem da MXSHISTORICOCOMPROMISSOS foi deletado com codoperacao = 2, porém essa deleção não chegou via sincronismo para o RCA. E então na base do RCA haviam registros não deletados de forma incorreta

Alguns dos registros que eu analisei eram por exemplo, dos dias 15,16 e 17 de Outubro de 2024, e eles foram apagados no dia 27/09/2024. Então no dia 30/09/2024 quando o RCA fez o primeiro sincronismo eles deveriam ter descido, mas não desceram deletando e o motivo não temos mais como saber porque essa evidência se perdeu a nível de desenvolvimento

A gente guarda até 10 dias desse registro de sincronizações de informações que descem, então como era para ter descido no dia 30/09, já não temos mais a evidências do problema em si para analisar

Para resolver então eu fiz uma carga reenviando os registros de compromissos deletados para todos os RCAs do cliente, então conforme eles sincronizarem vai normalizar as bases. Amanhã, por exemplo, não vai ocorrer o problema e daqui em diante não é para ocorrer mais teoricamente. Porém se tiver algum caso, o procedimento é o mesmo, analisar se cumpriu a rota anterir e pegar a base do maxPedido para analisarmos

- Eu testei essa solução sicronizando e vai resolver o caso deles, hoje mesmo se ele quiser testar já vai dar certo depois de sincronizar

# GATE-197 - RCA não cumpriu todo o roteiro e mesmo assim não solicitou desbloqueio

**Contexto**

O RCA 9231 não cumpriu todo o roteiro do dia anterior 16/10, e o aplicativo não bloqueou solicitando o desbloqueio para o mesmo iniciar as visitas de hoje dia 17/10

O cliente tem ativo o parâmetro BLOQ_RCA_COM_ROTA_PENDENTE, e com isso quando um vendedor não conclui o roteiro do dia anterior, deve bloquear no outro dia solicitando o desbloqueio

Mas ocorre que em alguns casos não está ocorrendo isso

Pelo que analisei de fato o vendedor não cumpriu todo seu roteiro do dia 16/10, faltando os clientes 114144 e 115059, que foi colocado no roteiro do dia 16/10 criado no roteirizador de vendedores

Também notei que no MaxPedido não constou o roteiro do dia 16/10, e gostaria de entender o que ocorreu para não ter o roteiro no MaxPedido, uma vez que o mesmo foi gerado na MXSCOMPROMISSOS, e também o cliente atendeu diversos clientes do roteiro faltando somente os clientes com código 114144 e 115059

Analisei a tabela MXSAPARELHOSDESBLOQLOG e de fato para esse RCA não teve nenhum desbloqueio

**Passos para reproduzir**

- Acessar o aplicativo
- Importar a base anexada
- Acessar a tela de clientes
- Clicar nos 3 pontinhos
- Ir em roteiro
- Ir para o roteiro do dia 16/10 e assim irá ver que não consta clientes nesse roteiro do dia 16/10
- Então queria entender o que está havendo, se foi por isso que não bloqueou do RCA iniciar a rota no dia seguinte, sem cumprir todo o roteiro, e também ver se não há algo que está faltando configurar

**Resultado apresentado**

O RCA não conclui todo o roteiro planejado para o dia anterior, e o aplicativo não impede o início do roteiro do dia atual

**Resultado esperado**

Quando o RCA não concluir todo o roteiro do dia anterior, o aplicativo deve bloqueá-lo de iniciar o roteiro do dia atual

**Diagnostico e orientacao**

Em outro chamado o dev MXPEDDV-80135, recomendou usar o parâmetro PERMITIR_DELETE_HISTORICOCOMP = S para deletar os históricos junto com os compromissos, porém esse parâmetro não pode ser usado junto com a questão do roteiro pentende porque o aplicativo usa essa informação para validar o roteiro do dia anterior

Como esse parâmetro está ativo o roteiro do dia 16/10 foi totalmente apagado junto com o histórico dele e por isso mesmo que o RCA não tenha cumprido a rota, nada foi validado no sistema. No caso o dia 16/10 é um dia que se perdeu e não tem como restaurar mais para validar o roteiro, mas agora que eu voltei o parâmetro na nuvem para PERMITIR_DELETE_HISTORICOCOMP = N, o do dia 17, será validado amanhã no dia 18/10, normalmente

# GATE-200 - Painel de Auditoria não exibe filial 1 e 5

**Contexto**

estou com uma situação no maxGestão onde no painel de auditoria não aparece as filiais 1 e 5, fiz uma validação na MXSUSUARI e MXSSUPERV e os vinculos com a filial 5 estão feitos normalmente, não consgui identificar o motivo de não exibir as outras filiais

**Passos para reproduzir**

- Acessar maxGestão da GP DONIZETE WINTHOR
- Painel de Auditoria
- Tentar filtrar filial 5 ou 1

**Resultado apresentado**

Mesmo o usuário sysMax tendo permissão de acesso para todas as filiais, elas não são apresentadas nos filtros

na MXSUSUARI existem RCAs vinculados a filial 5 e com supervisores também vinculados e ativos

**Resultado esperado**

Entender o motivo de não apresentar as outras filiais

**Diagnostico e orientacao**

- *Não passar as querys para o cliente são dados sensíveis nossos*

A Query definitiva é essa
{color:#739eca}SELECT{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}AS{color} {color:#00b8b8}CODIGO{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}RAZAOSOCIAL{color} {color:#00b8b8}DESCRICAO{color}

{color:#739eca}FROM{color} {color:#b788d3}MXSUSUARI{color}

{color:#739eca}INNER{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSSUPERV{color} {color:#b788d3}S{color}

{color:#739eca}ON{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODSUPERVISOR{color} = {color:#b788d3}S{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#739eca}LEFT{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSFILIAL{color}

{color:#739eca}ON{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} = {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODFILIAL{color}

{color:#739eca}WHERE{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color} ({color:#739eca}SELECT{color} {color:#00b8b8}KEYDADOS{color} {color:#739eca}FROM{color} {color:#b788d3}MXACESSODADOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDADOS{color} = {color:#cac580}'6'{color} {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} = {color:#7ebad3}:CODUSUARIO{color})

{color:#739eca}AND{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODSUPERVISOR{color} {color:#739eca}IN{color} ({color:#739eca}SELECT{color} {color:#00b8b8}KEYDADOS{color} {color:#739eca}FROM{color} {color:#b788d3}MXACESSODADOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDADOS{color} = {color:#cac580}'5'{color} {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} = {color:#7ebad3}:CODUSUARIO{color} )

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} <> {color:#cac580}'0'{color}

{color:#739eca}AND{color} {color:#9e9e9e}FUNCAO_INDICE{color} ({color:#00b8b8}CODFILIAL{color}) {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#9e9e9e}FUNCAO_INDICE{color} ({color:#00b8b8}DTTERMINO{color}) {color:#739eca}IS{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}BLOQUEIO{color} = {color:#cac580}'N'{color}

{color:#739eca}AND{color} {color:#b788d3}S{color}.{color:#00b8b8}COD_CADRCA{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}GROUP{color} {color:#739eca}BY{color} {color:#00b8b8}CODIGO{color}, {color:#00b8b8}RAZAOSOCIAL{color}{color:#eecc64};{color}

O código de usuário do sysmax é
{color:#669768}--82572{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSUSUARIOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}NOME{color} {color:#739eca}LIKE{color} {color:#cac580}'%Sys%'{color}{color:#eecc64};{color}

Caso você queria rodar a Query no bd deles

O que a Query faz?
R: Ela busca os RCAs vinculados aos supervisores pelo codsupervisor e verifica se a filial cadastrada existe na MXSFILIAL para ser apresentada. A base da consulta é essa
{color:#739eca}SELECT{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}AS{color} {color:#00b8b8}CODIGO{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}RAZAOSOCIAL{color} {color:#00b8b8}DESCRICAO{color}

{color:#739eca}FROM{color} {color:#b788d3}MXSUSUARI{color}

{color:#739eca}INNER{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSSUPERV{color} {color:#b788d3}S{color}

{color:#739eca}ON{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODSUPERVISOR{color} = {color:#b788d3}S{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#739eca}LEFT{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSFILIAL{color}

{color:#739eca}ON{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} = {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODFILIAL{color}

Abaixo então eu peguei a mesma base e só editei colocando mais informações e também adicionando apenas uma clásula WHERE para você visualizar que não tem nenhum RCA vinculado em outras filiais a não ser a 4 e a 5
{color:#739eca}SELECT{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}AS{color} {color:#00b8b8}CODIGO{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}RAZAOSOCIAL{color} {color:#00b8b8}DESCRICAO{color}

{color:#b788d3}S{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#b788d3}S{color}.{color:#00b8b8}COD_CADRCA{color}

{color:#b788d3}S{color}.{color:#00b8b8}NOME{color}

{color:#b788d3}U{color}.{color:#00b8b8}CODUSUR{color}

{color:#b788d3}U{color}.{color:#00b8b8}NOME{color}

{color:#b788d3}U{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#739eca}FROM{color} {color:#b788d3}MXSUSUARI{color} {color:#b788d3}U{color}

{color:#739eca}INNER{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSSUPERV{color} {color:#b788d3}S{color}

{color:#739eca}ON{color} {color:#b788d3}U{color}.{color:#00b8b8}CODSUPERVISOR{color} = {color:#b788d3}S{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#739eca}LEFT{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSFILIAL{color}

{color:#739eca}ON{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} = {color:#b788d3}U{color}.{color:#00b8b8}CODFILIAL{color}

{color:#739eca}WHERE{color} {color:#b788d3}U{color}.{color:#00b8b8}CODFILIAL{color} {color:#739eca}NOT{color} {color:#739eca}IN{color}({color:#c0c0c0}4{color},{color:#c0c0c0}5{color}){color:#eecc64};{color}

Mas e porque se tem a 5 não mostra ela?

Por causa das outras clásulas que estão no WHERE da consulta principal e original
{color:#739eca}WHERE{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color} ({color:#739eca}SELECT{color} {color:#00b8b8}KEYDADOS{color} {color:#739eca}FROM{color} {color:#b788d3}MXACESSODADOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDADOS{color} = {color:#cac580}'6'{color} {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} = {color:#7ebad3}:CODUSUARIO{color})

{color:#739eca}AND{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODSUPERVISOR{color} {color:#739eca}IN{color} ({color:#739eca}SELECT{color} {color:#00b8b8}KEYDADOS{color} {color:#739eca}FROM{color} {color:#b788d3}MXACESSODADOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDADOS{color} = {color:#cac580}'5'{color} {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} = {color:#7ebad3}:CODUSUARIO{color} )

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} <> {color:#cac580}'0'{color}

{color:#739eca}AND{color} {color:#9e9e9e}FUNCAO_INDICE{color} ({color:#00b8b8}CODFILIAL{color}) {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#9e9e9e}FUNCAO_INDICE{color} ({color:#00b8b8}DTTERMINO{color}) {color:#739eca}IS{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}BLOQUEIO{color} = {color:#cac580}'N'{color}

{color:#739eca}AND{color} {color:#b788d3}S{color}.{color:#00b8b8}COD_CADRCA{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}GROUP{color} {color:#739eca}BY{color} {color:#00b8b8}CODIGO{color}, {color:#00b8b8}RAZAOSOCIAL{color}{color:#eecc64};{color}

Especificamente a regra {color:#cccccc} AND{color} {color:#b788d3}S{color}.{color:#00b8b8}COD_CADRCA{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color} que significa que todos os supervisores que estão vinculados a RCAs que estão na filial 5, não possuem essa informação COD_CADRCA na tabela MXSSUPERV deles. Então como é is not null, ele remove as filiais desses supervisores nessas condições, no caso a 5

Então como o cliente pode fazer para resolver?

Eles podem estar resolvendo, vinculando os RCAs nas filiais que eles desejam que sejam apresentadas na MXSUSUARI Rotina 517 e elas precisam exisitir na MXSFILIAL 535 e estarem sendo integradas à Máxima. E eles precisam vincular esses RCAs na Rotina também 517 aos supervisores que existam na Rotina 516. E por fim, na Rotina 516 eles precisam vincular o Supervisor a um RCA, pode ser qualquer RCA, mas quem define essa regra de qual vai ser são eles (Geralmente os clientes colocam o próprio código de supervisor exemplo: Supervisor 10 código de RCA 10 – Eu acho mais correto porque fica organizado)

- *Outra opção que eles tem:* Eles podem na rotina 517, colocar todos os RCAs sem exceção vinculados ao conceito de filial 99 (que pertencem a todas as filiais); – Não sei que impactos isso pode ter no Winthor. Mas aqui no Painel de Auditoria o que vai acontecer é que nenhuma filial mais será apresentada no filtro de filiais. Porém todos os supervisores estarão vinculados a filial 99 e serão exibidas todas as equipes ao apertar no filtro de supervisor. Assim meio que você intuiliza o filtro de filial já que os supervisores estão vinculadas à 99 (todas). E continua considerando a regra do COD_CADRCA, os supervisores precisam estar vinculados a alguma RCA próprio deles na 516

# GATE-204 - MXSPRODUTPOS não gera registro

**Contexto**

Foi verificado que vários produtos foram positivados para um cliente nesse mesmo mês mas não gerou registro na MXSPRODUTPOS, alguns dos produtos já foram faturados porém também não gera na MXSPRODUTPOS

**Passos para reproduzir**

- Acessar APK
- Iniciar pedido no cliente 135838
- Aba tabela
- Olhar os produtos 134857, 134752, 111169, '099003', '009891', 104691
- Verificar que consta como se os produtos não estivessem positivados no mês de Outubro
- ##SELECTS UTILIZADOS##
- SELECT * FROM MXSHISTORICOPEDI WHERE CODPROD IN(134857, 134752, 111169, '099003', '009891', 104691) AND NUMPED IN(SELECT NUMPED FROM MXSHISTORICOPEDC WHERE CODCLI = 135838)
- SELECT * FROM MXSPRODUTPOS m WHERE CODPROD IN(134857, 134752, 111169, '099003', '009891', 104691) AND CODCLI = 135838
- SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%GERAR_DADOS_POS_PRODUTOS%'
- SELECT * FROM MXSVERSAOBD ORDER BY DTATUALIZACAO DESC

**Resultado apresentado**

Os produtos foram vendidos no mês de Outubro para esse cliente porém não gerou registros na MXSPRODUTPOS, tendo somente 4 com status de deletado

**Resultado esperado**

Gerar os registros

**Diagnostico e orientacao**

Basicamente o problema deles é que eles tem uma configuração no parâmetro da MXSPARAMETRO, (VALIDAR_APURACAO_NF = S) e com isso, o nosso sistema valida informações dos endpoints ERP_MXSMOV e ERP_MXSNFSAID. E eles não estão enviando os dados dos pedidos corretamente para gerar a positivação dos pedidos do RCA 3315 no cliente 135838 que seria o do cenário

- Então para resolver o cliente teria duas opções

- Ou o cliente vai precisar ou desligar o parâmetro VALIDAR_APURACAO_NF, colocando ele = N, assim não vai validar mais a questão de nota fiscal e movimentações que eles estão deixando de enviar corretamente para a gente

- Dai amanhã quando a JOB rodar novamente vai apurar os dados somente validando se o pedido tá com posicao = 'F' na MXSHISTORICOPEDC (que eles já estão enviando certo)

- Ou 2° opção, o cliente envia corretamente via integração os dados dos pedidos relacionando eles na MXSHISTORICOPEDC, ERP_MXSMOV e ERP_MXSNFSAID considerando as propriedades NUMPED e NUMTRANSVENDA

- Se o cliente perguntar por que não funcionou quando faturou o pedido e antes funcionava, é porque antes a integração fazia certo e agora parou de fazer e então ele teria que mostrar todas essas evidências e verificar com o integrador dele

- Eu recomendo eles só desligarem o parâmetro VALIDAR_APURACAO_NF

- *Abaixo vou colocar os detalhes da análise caso você queira entender também tudo que foi feito e verificado*

- O cliente usa o parâmetro CRITERIOVENDA = 'F'

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%CRITERIOVENDA%'; -- = F

- Então a gente valida a MXSHISTORICOPEDC se a POSICAO = 'F' e a positivação ela é referente somente ao mês 10

SELECT * FROM MXSHISTORICOPEDC WHERE CODUSUR IN(3315) AND CODCLI IN(135838) AND POSICAO IN('F') AND CODOPERACAO <> 2 AND TRUNC(DATA) BETWEEN TO_DATE('01/10/2024', 'DD/MM/YYYY') AND TO_DATE('18/10/2024', 'DD/MM/YYYY')

- Retorna os 3 pedidos certo? 8817136, 8817105, 8828379

- Então agora a gente valida o parâmetro VALIDAR_APURACAO_NF que está ativo desde 2023 na Donizete então não é novidade para eles

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%VALIDAR_APURACAO_NF%'; -- = S

- Então agora a gente valida o NUMTRANSVENDA dos pedidos

SELECT NUMTRANSVENDA FROM MXSHISTORICOPEDC WHERE CODUSUR IN(3315) AND CODCLI IN(135838) AND POSICAO IN('F') AND CODOPERACAO <> 2 AND TRUNC(DATA) BETWEEN TO_DATE('01/10/2024', 'DD/MM/YYYY') AND TO_DATE('18/10/2024', 'DD/MM/YYYY')

- Estão nulos, eles teriam de estar preenchidos pelo menos no NUMTRANSVENDA da ERP_MXSMOV que se relaciona com a ERP_MXSNFSAID

- O que a consulta faz é o que está abaixo, no caso olha se tem o numtransvenda para o rca

SELECT US.CODUSUARIO

PI.CODPROD

NVL(PI.CODAUXILIAR, 0) AS CODAUXILIAR

'P' AS TIPOPOSITIVACAO

MIN(PC.DTSAIDA) DTPOSITIVACAO

NULL QTDEPOSITIVACAO

NULL HASH

FROM MXSUSUARIOS US, ERP_MXSNFSAID PC, ERP_MXSMOV PI

WHERE PI.NUMTRANSVENDA = PC.NUMTRANSVENDA

AND PC.CODUSUR = US.CODUSUR

AND PC.DTCANCEL IS NULL

AND PC.CODFILIAL IN (SELECT CHAVEDADOS FROM MXSACESSODADOS WHERE CODDADOS = 6 AND CODUSUARIO = US.CODUSUARIO)

AND PC.DTSAIDA BETWEEN TO_DATE('01/10/2024', 'DD/MM/YYYY') AND TO_DATE('18/10/2024', 'DD/MM/YYYY')

AND PC.CODOPERACAO != 2

AND PI.CODOPERACAO != 2

AND US.CODOPERACAO != 2

AND US.CODUSUR = '3315'

GROUP BY US.CODUSUARIO, PI.CODPROD, NVL(PI.CODAUXILIAR, 0)

- Não retorna nada, significa que os pedidos foram faturados 8817136, 8817105, 8828379, mas não recebemos da integração as notas fiscais e nem as movimentações referentes a esses pedidos

- Se quiser conferir direto nos endpoints também

SELECT * FROM ERP_MXSMOV WHERE CODUSUR IN(3315);--Dos pedidos 8817136, 8817105 e 8828379 não consta a movimentação

SELECT * FROM ERP_MXSNFSAID WHERE NUMPED IN(8817136, 8817105, 8828379); --do 8828379 não recebemos a nota

SELECT * FROM ERP_MXSMOV WHERE NUMTRANSVENDA IN(4884757, 4884758); -- Não tem esses numtransvenda

# GATE-207 - Gerar visitas de RCAs (replicador)

**Contexto**

Devido ter parado a integração de dados do relatório de efetividade 8092, do dia 01/10 até 10/10/2024. Precisamos que seja gerado as visitas de todos os RCA no mesmo layout da tabela MXSCOMPROMISSOS do 01/10/2024 até 18/10/2024 para que os RCAs não sejam prejudicados

Cliente que utiliza o replicador e relatório de efetividade

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

Foi gerado o excel com os compromissos dentro das datas solicitadas pelo cliente 01/10/2024 - 18/10/2024 e disponibilizado
Peço por gentileza, para conferir com o cliente se seria isso mesmo que ele precisa

# GATE-214 - Duvida - Campo ausente do maxGestão no PWA

**Contexto**

O cliente gostaria de saber o MOTIVO do pedido que foi a autorização

No maxGestão WEB o campo é exibido, porem no PWA não encontrei o campo

**Passos para reproduzir**

- enviados com as mesmas seçoes web no PWA porem com o campo faltando

**Resultado apresentado**

O Campo MOTIVO

Dos pedidos que chegam para autorização no PWA não está sendo exibido no PWA

**Diagnostico e orientacao**

No maxGestão PWA existe a opção de ver o motivo da autorização, ela fica localizada em uma aba que abre ao apertar o botão "Ver Mais

coloquei uma imagem para ilustrar

No caso seria orientar ele a usar o recurso existente e que tem uma dependência com o usuário apertar em Ver Mais, se ele quiser sugerir uma forma diferente de ver a informação seria uma melhoria

# GATE-220 - RCAs não aparecem nos filtros de Visitas Previstas x Realizadas

**Contexto**

Estou subindo o ticket agora devido o cliente só ter criado agora, o problema é o que comentamos anteriormente, por algum motivo os RCAs sumiram dos filtros de visitas prevista x realizada, estava funcionando até semana passada mas agora só aparece 1 representante

Tentei verificar as questões mais básicas como codsupervisor, codfilial, se estão ativos, etc... mas não consegui identificar o motivo do problema

**Passos para reproduzir**

- Acessar maxGestão da TROIA
- Visitas Previstas x Realizadas
- Filtrar mês atual
- Todos supervisores
- Verificar que só aparece um representante

**Resultado apresentado**

Os outros RCAs deixaram de aparecer nos filtros

**Resultado esperado**

Voltar a aparecer todos os RCAs

**Diagnostico e orientacao**

- Na apuração de dados do Visitas Previstas Versus Realizadas
- São executadas várias consultas para trazer os dados
- Primeiro por filial, sendo o CODUSUARIO do Sysmax 18304 (para usar na consulta)
SELECT
CODFILIAL AS CODIGO
CASE
WHEN CODFILIAL = '99' THEN 'FILIAL 99'
ELSE RAZAOSOCIAL
END AS RAZAOSOCIAL
FANTASIA
COUNT (DISTINCT (MXSUSUARI.CODSUPERVISOR)) QTSUPERV
0 VLVENDA
0 AS VLVENDAPREV
0 INATIVOS
('0') EQUIPES
FROM
MXSUSUARI
INNER JOIN MXSSUPERV S ON
MXSUSUARI.CODSUPERVISOR = S.CODSUPERVISOR
LEFT JOIN MXSFILIAL ON
MXSFILIAL.CODIGO = MXSUSUARI.CODFILIAL
WHERE
CODFILIAL IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = '6'
AND CODUSUARIO = :codusuario)
AND MXSUSUARI.CODSUPERVISOR IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = '5'
AND CODUSUARIO = :codusuario )
AND CODFILIAL <> '0'
AND Funcao_indice (codfilial) IS NOT NULL
AND Funcao_indice (dttermino) IS NULL
AND MXSUSUARI.BLOQUEIO = 'N'
AND S.COD_CADRCA IS NOT NULL
AND S.POSICAO <> 'I'
GROUP BY
CODFILIAL
RAZAOSOCIAL
FANTASIA
- Retorna só a filial 1
- Depois você busca pelos supervisores

SELECT
CODSUPERVISOR
NOME
EQUIPES
ATIVOS
AUSENTES
INATIVOS
AGENDADOS
VISITADOS
POSITIVADOS
VLVENDA
VLPREVENDA
PERCVISITADOS
PERCPOSITIVADOS
PERCEFICIENCIA
VISITADOSA
POSITIVADOSA
EFICIENCIAA
CODIGOGRUPOFILIAL
CODIGOGRUPOGERENTE
CODIGOGRUPOCOORDENADOR
FROM
(
SELECT
MX.CODSUPERVISOR
MX.NOME
0 EQUIPES
0 ATIVOS
0 AUSENTES
0 INATIVOS
0 AGENDADOS
0 VISITADOS
0 POSITIVADOS
0 VLVENDA
0 AS VLPREVENDA
0 PERCVISITADOS
0 PERCPOSITIVADOS
0 PERCEFICIENCIA
('') VISITADOSA
('') POSITIVADOSA
('') EFICIENCIAA
NVL(F.CODIGO, MXU.CODFILIAL) CODIGOGRUPOFILIAL
NVL(G.CODGERENTE, '0') CODIGOGRUPOGERENTE
NVL(C.CODIGO, '0') CODIGOGRUPOCOORDENADOR
FROM
MXSSUPERV MX
LEFT JOIN ERP_MXSCOORDENADORVENDA C
ON
C.CODIGO = MX.CODCOORDENADOR
LEFT JOIN ERP_MXSGERENTE G
ON
G.CODGERENTE = NVL (C.CODGERENTE
MX.CODGERENTE)
INNER JOIN MXSUSUARI USU
ON
USU.CODUSUR = MX.COD_CADRCA
LEFT JOIN MXSFILIAL F
ON
USU.CODFILIAL = F.CODIGO
LEFT JOIN MXUSUARIOS MXU
ON
MX.CODSUPERVISOR = MXU.CODSUPERV
WHERE
MX.CODSUPERVISOR IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = 5
AND CODUSUARIO = :CODUSUARIO)
AND MX.POSICAO <> 'I'
UNION
SELECT
MX.CODSUPERVISOR
MX.NOME
0 EQUIPES
0 ATIVOS
0 AUSENTES
0 INATIVOS
0 AGENDADOS
0 VISITADOS
0 POSITIVADOS
0 VLVENDA
0 AS VLPREVENDA
0 PERCVISITADOS
0 PERCPOSITIVADOS
0 PERCEFICIENCIA
('') VISITADOSA
('') POSITIVADOSA
('') EFICIENCIAA
F.CODIGO CODIGOGRUPOFILIAL
NVL(G.CODGERENTE, '0') CODIGOGRUPOGERENTE
NVL(C.CODIGO, '0') CODIGOGRUPOCOORDENADOR
FROM
MXSSUPERV MX
INNER JOIN MXUSUARIOS MXU
ON
MX.CODSUPERVISOR = MXU.CODSUPERV
AND MXU.CODUSUARIO = :CODUSUARIO
LEFT JOIN ERP_MXSCOORDENADORVENDA C
ON
C.CODIGO = MX.CODCOORDENADOR
LEFT JOIN ERP_MXSGERENTE G
ON
G.CODGERENTE = NVL (C.CODGERENTE
MX.CODGERENTE)
LEFT JOIN MXSFILIAL F
ON
F.CODIGO = MXU.CODFILIAL
WHERE
MX.CODSUPERVISOR IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = 5
AND CODUSUARIO = :CODUSUARIO )
AND MXU.CODFILIAL IN (
SELECT
KEYDADOS
FROM
MXACESSODADOS
WHERE
CODDADOS = 6
AND CODUSUARIO = :CODUSUARIO )
AND MX.POSICAO <> 'I'

) V
GROUP BY
CODSUPERVISOR
NOME
EQUIPES
ATIVOS
AUSENTES
INATIVOS
AGENDADOS
VISITADOS
POSITIVADOS
VLVENDA
VLPREVENDA
PERCVISITADOS
PERCPOSITIVADOS
PERCEFICIENCIA
VISITADOSA
POSITIVADOSA
EFICIENCIAA
CODIGOGRUPOFILIAL
CODIGOGRUPOGERENTE
CODIGOGRUPOCOORDENADOR
ORDER BY
CODSUPERVISOR

- Vai retornar os 3 supervisores

- Por fim vai carregar os RCAs (Esse sql eu não ajustei para rodar pq é muitro trabalhoso mas é ele que o maxGestão faz)
WITH USUARIO AS
(SELECT * FROM
(SELECT MXSUSUARI.codusur,(:PDATAINICIAL) as data,nvl(MXSUSUARI.codfilial,0) codfilial
- usa este sql para não trazer duplicidade quando esta amarrado em mais de 1 usuario
nvl((SELECT MIN(codusuario) FROM mxsusuarios WHERE codusur = MXSUSUARI.codusur and status <> 'I'),0) codusuario
FROM MXSUSUARI
INNER JOIN MXSSUPERV ON MXSSUPERV.codsupervisor = MXSUSUARI.codsupervisor and MXSSUPERV.posicao = 'A' and MXSUSUARI.bloqueio = 'N'
{PARAMFILTRARPORSUPERV}
INNER JOIN mxacessodados z ON MXSSUPERV.codsupervisor = z.keydados
and z.coddados = 5
and z.codusuario = :codusuario
WHERE codfilial <> '0' and codfilial is not null and (trunc(MXSUSUARI.dttermino) > trunc(:PDATAINICIAL) OR dttermino is null)
GROUP BY MXSUSUARI.codusur, codfilial)
WHERE codusuario >0), --filtra apenas os que tiverem ligação com a mxsusuarios

LOCALIZACAO AS
(SELECT "CODUSUARIO
CODUSUR
DATA
CODFILIAL
RNK
FROM (SELECT mxs.codusuario
US.codusur
US.codfilial
mxs.data
RANK () OVER (PARTITION BY mxs.codusuario ORDER BY mxs.data DESC) AS rnk
FROM USUARIO US
LEFT JOIN mxslocation mxs ON mxs.codusuario = US.codusuario AND mxs.DATA <= SYSDATE and trunc(mxs.data) = trunc(US.data))
WHERE rnk = 1)

SELECT mxs.codusuario,mxs.nome,(mxs.nome) nomerca
ativos, agendados,visitados,positivados,vlvenda,vlprevenda
round(get_percentual(visitados, agendados) * 100,2) percvisitados
round(get_percentual(positivados , agendados) * 100,2) percpositivados
round(get_percentual(positivados , visitados) * 100,2) perceficiencia
('') visitadosA,('') positivadosA,('') eficienciaA,('')indexmapa
ultposicao,primeirocliente,ultcliente,versao
US.codusur
ROUND((select sum(distancia) from mxslocation where codusuario = US.codusuario
AND DATA <= SYSDATE
and trunc(data) = trunc(US.data)) / 1000,2) kmrodado --encontrada em metro e convertido para km
FROM mxsusuarios mxs,usuario US, (
SELECT pcu.codusur,pcu.nome
sum(nvl(tbequipes.ativos,0)) ativos
sum(nvl(tbdadoscli.agendados,0)) agendados
sum(nvl(tbdadoscli.visitado,0) + nvl(tbdadoscli.visitado1,0) + nvl(tbdadoscli.visitado2,0)) visitados
sum(nvl(tbpositivados.qtpositivados,0) + nvl(0,0)) positivados
sum(nvl(tbpositivados.vlatend,0)) vlvenda
sum(nvl(0,0)) vlprevenda
max(DECODE(nvl(ultposicao,0),'0','00:00',ultposicao)) ultposicao
min(DECODE(nvl(primeirocliente,0),'0','00:00',primeirocliente)) primeirocliente
max(DECODE(nvl(ultcliente,0),'0','00:00',ultcliente)) ultcliente
min(primeirocliente) primeiro,max(ultcliente) ultimo
max(versao) versao
FROM MXSUSUARI pcu
(SELECT codusur, ativos, ultposicao, versao
FROM
(SELECT codusur
(CASE WHEN NVL(codusuario,0) = 0 THEN 2 --0 - ativo 1 - inativo 2 - ausente
WHEN (SYSDATE - data) * 1440 < 30 THEN 0 ELSE 1 END) ativos
to_char(data, 'HH24:MI') as ultposicao
data
(select appversion FROM ((SELECT appversion,codusuario from mxsaparelhosconnlog WHERE trunc(dtinicioconexao) BETWEEN trunc(:PDATAINICIAL) AND trunc(:PDATAFINAL) order by numconexao desc))
where rownum = 1 and codusuario = US.codusuario) as versao
FROM LOCALIZACAO US
WHERE 1=1)
group by codusur, ativos, ultposicao, versao) tbequipes
(SELECT codusur
sum((SELECT count(codcli) FROM mxscompromissosmov mxs WHERE mxs.CODUSUARIO = US.CODUSUARIO AND trunc(mxs.data) = trunc(US.data))) Agendados
sum((SELECT count(DISTINCT codcli)
FROM MXSHISTORICOPEDC
WHERE MXSHISTORICOPEDC.codusur = US.codusur AND TRUNC (MXSHISTORICOPEDC.dtaberturapedpalm)= trunc(US.data)
{PARAMEMITIDORCA}
AND MXSHISTORICOPEDC.CODOPERACAO <> 2
and MXSHISTORICOPEDC.codcli NOT IN
(SELECT distinct pfv.codcli
FROM ERP_MXSVISITAFV pfv, MXSCLIENT
WHERE MXSCLIENT.codcli = pfv.codcli and pfv.CODUSUR = US.codusur
and trunc(pfv.DATA) = trunc(US.data)))) as visitado
sum((SELECT count(pfv.codcli)
FROM ERP_MXSVISITAFV pfv, MXSCLIENT
WHERE MXSCLIENT.codcli = pfv.codcli and pfv.CODUSUR = US.codusur
and trunc(pfv.DATA) = trunc(US.data) GROUP BY pfv.codusur)) as visitado1

SUM ((SELECT count(MXSINTEGRACAOPEDIDO.codcli) FROM MXSINTEGRACAOPEDIDO, MXSCLIENT
WHERE MXSINTEGRACAOPEDIDO.status = 6
AND MXSCLIENT.CODCLI = MXSINTEGRACAOPEDIDO.CODCLI
AND MXSINTEGRACAOPEDIDO.CODUSUR = US.cod_usur
AND TRUNC(MXSINTEGRACAOPEDIDO.DATA) = trunc(US.data)
GROUP BY MXSINTEGRACAOPEDIDO.codusur))
/*
sum((SELECT count(mxsgeo.codcli)
FROM mxsgeopedido mxsgeo, MXSCLIENT
WHERE MXSCLIENT.codcli = mxsgeo.codcli and mxsgeo.CODUSUR = US.codusur
and trunc(mxsgeo.DATA) = trunc(US.data) GROUP BY mxsgeo.codusur))
- */
as visitado2
MIN((SELECT min(primeirocliente) FROM
(SELECT TO_CHAR(TO_DATE('01/01/1900 ' || pfv.horainicial || ':' || pfv.minutoinicial,'DD/MM/YYYY HH24:MI:SS'),'HH24:MI') PrimeiroCliente,codusur
FROM ERP_MXSVISITAFV pfv, MXSCLIENT WHERE MXSCLIENT.codcli = pfv.codcli and (CODUSUR,trunc(DATA)) in (select codusur,trunc(data) from usuario)
UNION
SELECT TO_CHAR(data,'HH24:MI'), codusur
FROM mxslocation WHERE tipo = 'Checkin' AND DATA <= SYSDATE and (CODUSUR,trunc(DATA)) in (select codusur,trunc(data) from usuario)) where codusur = US.codusur GROUP BY codusur )) PrimeiroCliente
MAX((SELECT max(ultimocliente) FROM
(SELECT TO_CHAR(TO_DATE('01/01/1900 ' || pfv.horafinal || ':' || pfv.minutofinal,'DD/MM/YYYY HH24:MI:SS'),'HH24:MI') ultimocliente,codusur
FROM ERP_MXSVISITAFV pfv,MXSCLIENT WHERE MXSCLIENT.codcli = pfv.codcli and (CODUSUR,trunc(DATA)) in (select codusur,trunc(data) from usuario)
UNION
SELECT TO_CHAR(data,'HH24:MI'), codusur
FROM mxslocation WHERE tipo = 'Checkout' AND DATA <= SYSDATE and (CODUSUR,trunc(DATA)) in (select codusur,trunc(data) from usuario)) where codusur = US.codusur GROUP BY codusur )) ultcliente
FROM USUARIO US
WHERE 1 = 1
GROUP BY codusur) tbdadoscli
(SELECT MXSHISTORICOPEDC.codusur, SUM (Decode (MXSHISTORICOPEDC.condvenda, 5, 0
6, 0
11, 0
12, 0
MXSHISTORICOPEDC.vlatend)) AS vlatend
count(DISTINCT MXSHISTORICOPEDC.codcli) qtpositivados
FROM MXSHISTORICOPEDC, USUARIO US
WHERE MXSHISTORICOPEDC.CONDVENDA NOT IN (4,5,6,8,10,11,12,13,20,98,99)
AND MXSHISTORICOPEDC.DTCANCEL IS NULL
AND TRUNC (MXSHISTORICOPEDC.dtaberturapedpalm)= trunc(US.data)
AND MXSHISTORICOPEDC.codusur = US.codusur
AND MXSHISTORICOPEDC.CODOPERACAO <> 2
{PARAMEMITIDORCA}
GROUP BY MXSHISTORICOPEDC.codusur) tbpositivados
WHERE tbequipes.codusur (+) = pcu.codusur
and tbdadoscli.codusur (+) = pcu.codusur
and tbpositivados.codusur(+) = pcu.codusur
group by pcu.codusur, pcu.nome) DADOS
WHERE US.codusur = DADOS.codusur
AND mxs.codusuario = US.codusuario
{PARAMFILTRARPORRCA}
ORDER BY codusuario ASC

- Então por isso que ao executar ela retorna somente 1 RCA

- Abaixo eu dividi as regras por tabela para melhor entendimento

- Então por exemplo, primeiro a gente desconsidera os Supervisores inativos e também que não possuem COD_CADRCA no cadastro

SELECT * FROM MXSSUPERV WHERE CODOPERACAO != 2 AND POSICAO IN('A') AND COD_CADRCA IS NOT NULL
- Ficamos somente com os supervisores 1,6,8

- Depois a gente vai trazer os vendedores que estão ativos, ou seja DTTERMINO IS NULL e que estão vinculados nesses 3 supervisores
SELECT * FROM MXSUSUARI WHERE CODSUPERVISOR IN(1,6,8) AND DTTERMINO IS NULL AND CODOPERACAO != 2
- Obtemos 4 RCAs
- Por fim vamos buscar na MXSUSUARIOS usuários com licença do maxPedido ativa
SELECT * FROM MXSUSUARIOS WHERE CODUSUR IN(29, 1, 95, 120) AND STATUS IN('A')
- Obtemos somente a RCA MANUELA R DA SILVA no código de usuário 18373

- Então o que ele precisa fazer para resolver e ver mais RCAs lá?
- 1° Ele precisa colocar todos os supervisores vinculados a algum COD_CADRCA na Rotina 516
- 2° Ele precisa verificar se os RCAs que ele associou aos supervisores, se eles possuem CODFILIAL vinculado 99 ou alguma outra filial específica
- 3° Os RCAs que ele deseja visualizar precisam ter uma licença do maxPedido e estarem ativos

# GATE-226 - diveregencia de quantidades de clientes entre banco e aplicaçao

**Contexto**

ao analisar o cenário citado estamos observando divergência em quantidade de clientes que não identifiquei qual a regra que está afetando o sistema e gerando essa situação. No roteirizador exibe a quantidade abaixo

!image-2024-10-24-09-12-35-485.png!

enquanto que na view que trás essa informação, a contagem trás o seguinte valor

!image-2024-10-24-09-15-55-681.png!

Não identifiquei de onde está sendo observado esse valor de 196 clientes que o sistema trás

**Passos para reproduzir**

- acessar o ambiente do roteirizador do cliente e buscar pelo vendedor MARCONES MENDES DOS SANTOS - CODUSUR 522
- Comparar com os registros que são contados na view de vinculos dos clientes com RCA

**Resultado apresentado**

divergência na quantidade de clientes entre banco e sistema

**Resultado esperado**

a principio, é esperado que a quantidade seja equivalente entre a consulta realizada e o que o sistema exibe, porém não tenho certeza se há outra regra que restringe as quantidades retornadas por algum motivo

**Diagnostico e orientacao**

O que ocorre é que no Roteirizador tem uma opção na engrenagem em cima na direita de "excluir clientes inativos", então com isso faz uma validação onde remove alguns clientes com DTEXCLUSAO preenchida e bloqueiodefinitivo != 'S' e também sem coordenadas definidas

Coloquei na imagem Screenshot_1.png

Então para os dados ficarem compatíveis com o número de clientes da carteira e que também é gerado na view (211) ele deve desmarcar essa configuração

A view é a SELECT COUNT(*) FROM MXSVCLIENTESRCA WHERE CODUSUR IN(522)

Os dados exibidos serão conforme ela

O SQL que ela faz é

SELECT "CODUSUR
CODCLI
DTCADASTRO
DTULTCOMP
FROM (SELECT DISTINCT codusur
codcli
dtcadastro
dtultcomp
FROM (SELECT c.codusur1 codusur
c.codcli
c.dtcadastro
c.dtultcomp
FROM mxsclient c
WHERE NVL(c.codusur1,'0') > '0' AND c.codoperacao != 2
UNION
SELECT c.codusur2 codusur
c.codcli
c.dtcadastro
c.dtultcomp
FROM mxsclient c
WHERE NVL(c.codusur2,'0') > '0' AND c.codoperacao != 2
UNION
SELECT c.codusur3 codusur
c.codcli
c.dtcadastro
c.dtultcomp
FROM mxsclient c
WHERE NVL(c.codusur3,'0') > '0' AND c.codoperacao != 2
UNION
/* CONSULTA PARA ENVIAR OS CONSUMIDORES FINAIS PARA TODOS OS CODUSUR - FILTRAR_CONSUMIDOR_FINAL_GERACAO = N */
SELECT DISTINCT CODUSUR
C.CODCLI
C.DTCADASTRO
C.DTULTCOMP
FROM MXSUSUARIOS M, MXSCLIENT C
WHERE M.STATUS = 'A'
AND M.CODUSUR IS NOT NULL
AND M.CODOPERACAO != 2
AND OBTER_PARAMETRO ('FILTRAR_CONSUMIDOR_FINAL_GERACAO', NULL, 'N') = 'N'
AND C.CODCLI IN ('1', '2', '3')
AND C.CONSUMIDORFINAL = 'S'
UNION
/* CONSULTA PARA ENVIAR OS CONSUMIDORES FINAIS APENAS PARA OS CODUSUR VINCULADOS NA ERP_MXSUSURCLI - FILTRAR_CONSUMIDOR_FINAL_GERACAO = S */
SELECT DISTINCT
E.CODUSUR
C.CODCLI
C.DTCADASTRO
C.DTULTCOMP
FROM MXSCLIENT C
INNER JOIN ERP_MXSUSURCLI E ON E.CODCLI = C.CODCLI AND E.CODOPERACAO != 2
WHERE C.CODOPERACAO != 2
OR (OBTER_PARAMETRO ('FILTRAR_CONSUMIDOR_FINAL_GERACAO', NULL, 'N') = 'S'
AND C.CODCLI IN ('1', '2', '3')
AND C.CONSUMIDORFINAL = 'S'
AND C.CODOPERACAO != 2)))
WHERE codusur = 522

# GATE-229 - Mesmo cumprindo o roteiro do dia anterior, está pedindo desbloqueio no outro dia

**Contexto**

O cliente voltou com a situação do RCA ter cumprido todo o roteiro do dia anterior e mesmo assim ter bloqueado no outro dia

Pelo que analisei dentro do roteirizador de vendedores tinha 12 clientes no roteiro do dia 23/10, mas na MXSCOMPROMISSOS constam 15 clientes no roteiro, e gostaria de entender o porque dessa divergência

**Passos para reproduzir**

- Acessar o aplicativo
- Ir na tela de clientes
- Tentar iniciar um pedido em qualquer cliente do roteiro de hoje dia 24/10
- E assim retorna que não cumpriu todo o roteiro do dia anterior, solicitando o desbloqueio

**Resultado apresentado**

Mesmo RCA cumprindo todo o roteiro no dia anterior solicita desbloqueio informando não ter cumprido todo o roteiro do dia anterior

**Resultado esperado**

Que não bloqueie a rota no dia seguinte, o RCA tendo cumprido todo o roteiro do dia anterior

**Diagnostico e orientacao**

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXMI_AGENDA_RCA{color} {color:#739eca}WHERE{color} {color:#00b8b8}ID_RCA{color} {color:#739eca}IN{color}({color:#c0c0c0}9108{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#00b8b8}INICIO_VISITA{color}) = {color:#c1aa6c}TRUNC{color}({color:#b19b9b}SYSDATE{color},{color:#cac580}'DD'{color}) - {color:#c0c0c0}1{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}ERP_MXSROTACLI{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUR{color} {color:#739eca}IN{color}({color:#c0c0c0}9108{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSHISTORICOCOMPROMISSOS{color} {color:#b788d3}m{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}40740{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#b788d3}m{color}.{color:#00b8b8}DTINICIO{color}) = {color:#c1aa6c}TRUNC{color}({color:#b19b9b}SYSDATE{color},{color:#cac580}'DD'{color}) - {color:#c0c0c0}1{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCOMPROMISSOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}40740{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#00b8b8}DTINICIO{color}) = {color:#c1aa6c}TRUNC{color}({color:#b19b9b}SYSDATE{color},{color:#cac580}'DD'{color}) - {color:#c0c0c0}1{color}{color:#eecc64};{color}

{color:#eecc65}--SELECTS NA BASE DA APK ABAIXO{color}
{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCOMPROMISSOS{color} {color:#739eca}WHERE{color} {color:#739eca}date{color}({color:#00b8b8}dtinicio{color}) = {color:#739eca}date{color}({color:#cac580}'2024-10-23'{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSHISTORICOCOMPROMISSOS{color} {color:#739eca}WHERE{color} {color:#739eca}date{color}({color:#00b8b8}dtinicio{color}) = {color:#739eca}date{color}({color:#cac580}'2024-10-23'{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSUSUARIOS{color}{color:#eecc64};{color}

- Não finalizei a análise ainda, preciso entender porque o cliente apagou a rota no dia 23/10 às 15h e como isso pode impactar na geração da tabela MXSHISTORICOCOMPROMISSOS no dia seguinte

Provavelmente será tratado como erro ou melhoria. Será encaminhado para desenvolvimento como Erro para eles avaliarem. O que aconteceu é que há registro de alteração da rota do RCA no dia 23/10 enquanto ela ainda estava vigente, e aparentemente o nosso sistema não tem nenhum mecanismo que reconheça que a rota foi editada no dia vigente e apague o histórico dos compromissos de forma compatível com as remoções realizadas

# GATE-230 - Produto não aparece

**Contexto**

O produto 92656 não aparece ao RCA 956, o mesmo não aparece somente a esse vendedor e pelo que analisei as tabela principais estão ok

**Passos para reproduzir**

- Acessar o aplicativo
- Iniciar um pedido em qualquer cliente ou ir no card de produtos na tela inicial
- Procurar pelo item 92656
- E o mesmo não aparece

**Resultado apresentado**

Produto 92656 não aparece ao RCA

**Resultado esperado**

Que o produto 92656 apareça ao RCA

**Diagnostico e orientacao**

O produto não aparece em alguns casos devido a região selecionada de precificação, conforme vou explicar abaixo

SELECT PVENDA1,PTABELA,CODOPERACAO,CODPROD,NUMREGIAO FROM MXSTABPR WHERE CODPROD IN(92656) AND NUMREGIAO IN(2, 3, 1, 10, 11, 6, 8, 12, 15)

- O RCA tem acesso às regiões

- 2, 3, 1, 10, 11, 6, 8, 12, 15

- Ele só vai conseguir vender para clientes das regiões

- 2, 12, 6, 8, 10, 11, 1

- Porque só nelas o produto está precificado

Então por exemplo, ele aparece para o cliente 833952 e buscando no card de produtos pelo código dele na região 1. Se o cliente quiser que ele apareça para outros clientes de outras regiões, bem como no card de produtos de outras regiões, ele vai precisar precificar esse produto nessas regiões específicas

# GATE-233 - divergencia de painel de indicadores e rotina do winthor.

**Contexto**

estamos observando uma divergência de valores entre o painel de indicadores e rotina 146 que não é esperada. A principio, o painel abaixo deveria apresentar o mesmo valor que é retornado na rotina
!image-2024-10-28-09-57-39-495.png!

!image-2024-10-28-09-57-59-949.png!

Uma vez que o filtro utilizado no painel geral, é o filtro equivalente ao que está sendo usado na rotina, porém os valores tem essa divergência

!image-2024-10-28-09-59-18-654.png!

**Passos para reproduzir**

- Acessar o ambiente do cliente e realizar os filtros conforme os prints, em seguida realizar a consulta equivalente na rotina do winthor

**Resultado apresentado**

divergencia de valores de venda sendo retornados

**Resultado esperado**

é esperado queos

**Diagnostico e orientacao**

A rotina 146 do Winthor considera o valor de venda dos históricos das capas dos pedidos (VLATEND) da PCPEDC e o maxGestão considera o valor dos históricos de vendas dos itens

Por esse motivo ocorre essa diferença na apresentação da informação

SELECT SUM(VLATEND) FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('22/10/2024', 'dd/MM/yyyy') AND TO_DATE('22/10/2024', 'dd/MM/yyyy') AND POSICAO <> 'C' AND CODSUPERVISOR = 16
Resulta em R$120389.53

SELECT SUM(QT*PVENDA) FROM PCPEDI WHERE NUMPED IN(SELECT NUMPED FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('22/10/2024', 'dd/MM/yyyy') AND TO_DATE('22/10/2024', 'dd/MM/yyyy') AND POSICAO <> 'C' AND CODSUPERVISOR = 16 AND CODFILIAL = 'T3') AND POSICAO <> 'C'
Resulta em R$120597.3185851 ~= 120597.33

Como o cliente tem uma divergência nos históricos do próprio banco local referente a essa informação da venda dos itens, então os valores não batem

Importante pontuar também que a maioria dos clientes essa informação não bate mesmo. O maxGestão tem essa apuração a parte das informações, mas que também garante mais precisão na informação. No caso específico da venda transmitida, é considerado normal e está no escopo do produto que não é compatível com a 146, porque o ERP faz de um jeito e a nossa aplicação de outro, simplesmente

Já referente a Rotina 111 sim (Venda Faturada), os dados devem bater, essa explicação acima é uma especificidade da venda transmitida no maxGestão em relação à 146

Por fim, se o cliente quiser um comportamento divergente do atual, seria considerado uma sugestão de melhoria do sistema

# GATE-235 - Relatorio Venda por Equipe e Análise de Vendas x Rotina 146

**Contexto**

Valores apresentados no relatório "Venda por Equipe e Análise de Vendas" do portal administrativo estão divergentes dos valores apresentados na rotina 146

**Passos para reproduzir**

- Replicar busca com os mesmos filtros das imagens

**Resultado apresentado**

Valores divergentes

**Resultado esperado**

Valores iguais

**Diagnostico e orientacao**

Por padrão a Rotina 146 desconsidera o valor das bonificações e na hora de filtrar no relatório de Venda por Equipe e Análise de Venda eu reparei que não foi habilitado esse filtro

Ele fica localizado na opção de "Deduzir" Selecionar tipo dedução antes de gerar os dados

Com essa dedução (Bonificações) habilitada, os valores da 146 com o do relatório devem estar batendo

!image-2024-10-29-11-51-00-172.png!

Obs: Tentei solicitar conexão para o cliente para eu verificar na 146 deles e garantir a taça, porém o cliente não me respondeu

# GATE-242 - supervisor auto serviço não aparece e diverência de valores

**Contexto**

>> O campo "Auto serviço" não aparece no maxGestao, nem nos selects via banco

TeamViewer ID: 140 169 544

**Passos para reproduzir**

- Verificar no maxGestao onde o supervisor "auto serviço" não aparece
- Verificar no banco os seguintes selects, onde não retornam nada
- (SELECT * FROM MXSHISTORICOPEDC WHERE ORIGEMPED IN('A') AND TRUNC(DATA) BETWEEN TO_DATE('01/10/2024','DD/MM/YYYY') AND TO_DATE('28/10/2024','DD/MM/YYYY') AND POSICAO <> 'C'
- SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%ENVIA_PEDIDOS_AUTOSERVICO%'
- O supervisor "Auto Serviço" não aparece
- O supervisor deve aparecer no maxgestao e o valor entre o Winthor e o maxGesta deve bater

**Diagnostico e orientacao**

O motivo de os valores estarem divergentes inicialmente era devido aos pedidos de origem 'A' não estarem sendo integrados ao banco de dados nuvem para a Filial 4

Então considerando esse cenário, foi realizada conexão no ambiente do cliente, feita configuração para importar pedidos de origem 'A' Auto_servico e também feita a carga de todas as tabelas necessárias para gerar o histórico e apuração no maxGestão

No momento dia 30/10/2024 essa carga ainda não foi finalizada, provavelmente vai finalizar entre hoje no final do dia 18h e amanhã. Provavelmente de manhã já vai ter finalizado

Então sob esse contexto, eu acredito que amanhã o cliente possa validar no maxGestão se os dados estão próximos do que ele tem na Rotina 146 do Winthor seguindo os filtros que ele colocou

Ocorre também que não necessariamente vai bater os dados com a Rotina 146 porque no Winthor os dados são apurados conforme o histórico de capas dos pedidos e no maxGestão nós trazemos uma informação dos históricos dos itens dos pedidos vendidos. Então se o cliente tiver uma divergência entre o valor vendido que fica guardado nas capas dos pedidos em relação aos itens, terá uma pequena diferença de valores e isso é considerado normal

# GATE-246 - valores divergentes ao filtrar com deduções

**Contexto**

ao analisar o cenário da demanda, estamos observando divergencias entre valores, de forma inesperada. Quando o filtro aplicado, não possui deduções sendo aplicadas, os valores ficam equivalentes e adequados para venda faturada
!image-2024-10-29-17-30-36-254.png!

!image-2024-10-29-17-30-55-919.png!

quando se aplicam deduções aos filtros para se obter valores líquidos na apresentação, as divergências começam a serem observadas

!image-2024-10-29-17-32-19-360.png!

!image-2024-10-29-17-32-40-469.png!

não foi observado problemas relacionados a tipos de venda nas filtragens efetuadas

**Passos para reproduzir**

- realizar os filtros conforme a descrição apresentada, no maxgestão e na rotina de resumo de faturaento e comparar os resultados

**Resultado apresentado**

o gestão traz dados divergentes das deduções a serem aplicadas no filtro

**Resultado esperado**

é esperado que os dados entre os dois locais estejam equivalentes, uma vez que os parametros de consulta e a base de dados dos dois locais são os mesmos

**Diagnostico e orientacao**

Foi enviado para N3

Foi feita carga dos dados no banco local do cliente e mesmo assim os dados não batem acredito que seja algum problema com as devoluções calculadas na Rotina 111 e em relação ao que temos para calcular na nuvem

# GATE-250 - [MXGESN] Filtro - Relatório de Acessos

**Contexto**

Estou com uma dúvida, um cliente abriu uma demanda sobre a tela "Relatórios de Acessos", que pra mim é uma novidade, não me lembro de ter visto essa funcionalidade antes

Nisso, ao filtrar nessa tela do relatório não exibe nenhum gerente, eu não entendi muito bem esse filtro, pois ele filtra gerentes e também supervisores, e os gerentes são necessários para poder visualizar os supervisores

Gostaria de entender qual amarra é feito entre gerente e supervisor

**Passos para reproduzir**

- Acessar maxGestão
- Relatórios de Acesso
- Tentar filtrar algum gerente

**Resultado apresentado**

Ao filtrar nessa tela do relatório não exibe nenhum gerente, mesmo o usuário sysMax tendo acesso total

**Resultado esperado**

Entender qual é o vinculo entre gerente e supervisor

**Diagnostico e orientacao**

Para apresentar os gerentes no filtro, será necessário o cliente informar um código de RCA para o Gerente porque o filtro considera as filiais disponíveis conforme a MXSUSUARI (CODFILIAL) e para exisitir essa relação com o Gerente, precisa ter o ERP_MXSGERENTE.CODUSUR = MXSUSUARI.CODUSUR

No caso deles eles não possuem RCA vinculado ao gerente, por isso não carrega a informação na ERP_MXSGERENTE e consequentemente não exibe no filtro

# GATE-262 - Mensagem de Acesso Negado no maxGestão PWA

**Contexto**

>> Realizados testes e verificado que quando se tira uma permissão na central de configurações, a opção some do maxGestão PWA, evitando que o RCA encontre uma tela que ele não tenha acesso
>> Verificado com o Gatekeeper Filipe Padilha que, provavelmente, por estar o app aberto por muito tempo em segundo plano, o app fica sem atualizar, e com isso acaba perdendo o token de acesso, fazendo com que as telas fiquem indispoíveis, sendo necessário fechar o app e abrir novamente

**Passos para reproduzir**

- USUÁRIO DE TESTE 1
- USUÁRIO DE TESTE 2
- USUÁRIO DE TESTE 3

**Resultado apresentado**

>> Aparece tela para o usuário informando "Acesso Negado", e que o mesmo não tem permissão para acessar a página, sendo que só aparece as telas que ele possui permissão para acessar

**Resultado esperado**

>> Tela de "Acesso Negado" não aparecer para o usuário

**Diagnostico e orientacao**

Foi revisado o fluxo na aplicação e foi constatado que ao logar na aplicação é gerado um token, este token tem validade de 24 horas. Após as 24 horas, o token é expirado fazendo com que a validação da versão pro/plus fique falha. E então o usuário perde acesso as funcionalidades do maxGestão, apresentando assim a mensagem "Acesso Negado

Nesse caso, é preciso que seja tratado com uma melhoria pra implementar uma função de revalidação/refresh no token, assim, não será preciso matar a aplicação

Como solução paliativa, é preciso matar a aplicação e fazer o login novamente

- Tentei rastrear se havia alguma melhoria aberta sobre isso e não encontrei então o melhor é se o cliente quiser, abrir uma nova melhoria sobre o assunto. E cada ticket pai deve ser vinculado a uma melhoria individual. Não pode vincular vários N1 em apenas um N3 de Melhoria mesmo que sejam do mesmo assunto

# GATE-264 - falha momentanea de reconhecimento de licença  do sistema

**Contexto**

estamos identificando que a aplicação do maxgestão PWA, tem alguns momentos que deixa de reconhecer a licença do produto que o usuário se encontra logado e começa a exibir os alertas que são observados abaixo

!image-2024-11-01-12-15-43-299.png|width=276,height=592!!image-2024-11-01-12-24-06-760.png|width=272,height=591!

Mesmo estando conectado a internet, demanda que seja refeito o login manualmente para reconhecer a versão do produto adequadamente, ainda que não tenham sido realizadas alterações no usuário que possam indicar essa necessidade, o que gera um falso negativo na visão do cliente que, há um problema com as versões do produto

Credencial do cliente

**Passos para reproduzir**

- efetuar o login na aplicação e realizar o uso por um periodo de tempo

**Resultado apresentado**

a aplicação apresenta os alertas como nas imagens, mesmo que o usuário logado, tenha a versão do produto liberada e conexão ativa e regular em seu aparelho

**Resultado esperado**

é esperado que não se apresentem essas mensagens no cenário do usuário, uma vez que o mesmo está regularmente operando, com a versão do produto liberada e adequada

**Diagnostico e orientacao**

Foi revisado o fluxo na aplicação e foi constatado que ao logar na aplicação é gerado um token, este token tem validade de 24 horas. Após as 24 horas, o token é expirado fazendo com que a validação da versão pro/plus fique falha. E então o usuário perde acesso as funcionalidades do maxGestão, apresentando assim a mensagem "Acesso Negado

Nesse caso, é preciso que seja tratado com uma melhoria pra implementar uma função de revalidação/refresh no token, assim, não será preciso matar a aplicação

Como solução paliativa, é preciso matar a aplicação e fazer o login novamente

- Tentei rastrear se havia alguma melhoria aberta sobre isso e não encontrei então o melhor é se o cliente quiser, abrir uma nova melhoria sobre o assunto. E cada ticket pai deve ser vinculado a uma melhoria individual. Não pode vincular vários N1 em apenas um N3 de Melhoria mesmo que sejam do mesmo assunto

# GATE-267 - resumo de vendas não atualiza (T-Cloud)

**Contexto**

>> Verificado que o IP de acesso do cliente, no cadastro do extrator, estava como " porém ao rodar a Pipeline de ler variáveis do Jenkins, verifiquei que o DNS correto seria o
>> Após atualizar para o DNS correto, verificado que o resumo de vendas continuou sem atualizar
>> Creio que não seja bloqueio GEOLOCATION aos IPs dos EUA, pois o cliente agora é T-Cloud
>> Verificado que o hangfire está acessível normalmente (

**Passos para reproduzir**

- Tentar atualizar o resumo de vendas

**Resultado apresentado**

>> Resumo de vendas não atualiza

**Resultado esperado**

>> Atualizar resumo de vendas

**Diagnostico e orientacao**

Salvando dados
USER_HANGFIRE=admin
PASS_HANGFIRE=Ozy1L4JM011HzDv+ImCPc6qp6xA=
USUARIO_EXTRATOR_NUVEM=jotabe.armazemcruzeiroproducao
SENHA_EXTRATOR_NUVEM=XC9D2SWJnGArIQ/iLhUE/UwtprTApXfQWDyNkTCyJRU=
USUARIO_SYSTEM_WINTHOR=MAXSOLUCOES
SENHA_SYSTEM_WINTHOR=y+TzuIH5WEzQTZ72nNZYopPDIuhY8vTLJFCpVgMfkgA=
SENHA_MAXSOLUCOES=y+TzuIH5WEzQTZ72nNZYopPDIuhY8vTLJFCpVgMfkgA=
LINK_API_WINTHOR_CANCELAMENTO=
USUARIO_API_WINTHOR_CANCELAMENTO=
SENHA_API_WINTHOR_CANCELAMENTO=
TZ=America/Sao_Paulo
VERSAO:dockermaxima/extrator:3.1.2.442

O link correto de fato é o

As informações para atualização do menu no banco do cliente também estão corretas

Eu fiz um teste com o usuário jotabe.maxima e assim que baixou a base eu testei a atualização e foi com sucesso

!image-2024-11-04-14-28-26-030.png!

No caso só não vai atualizar o gráfico de vendas porque o usuário vinculado é o RCA 1 e ele não possui meta cadastrada (verifiquei tabelas PCMETA e PCMETARCA)

Isso aconteceu contigo porque após trocar o link de atualização no cadastro do extrator de " para " para essa mudança surtir na apk, é necessário relogar no maxSoluções

No caso, para resolver basta relogar no maxSoluções visto que você já resolveu ao alterar o link de atualização do menu para

# GATE-286 - Falha acesso Max Gestão PWA via web

**Contexto**

estão acontecendo as seguintes falhas de acesso ao PWA via web em alguns momentos

!image-2024-11-06-10-52-12-168.png!

onde mesmo que o usuário esteja ativo e acessando o appsv e com versão liberada

!image-2024-11-06-10-53-02-594.png!

ocorre falha no login

!image-2024-11-06-10-53-40-431.png!

**Passos para reproduzir**

- acessar e tentar o login com a seguinte credencial
- observar os resultados

**Resultado apresentado**

falha de acesso via PWA através da web

**Resultado esperado**

que o acesso ocorra normalmente sem falhas

**Diagnostico e orientacao**

Foi alinhado com o P.O Thiago Castro que esses problemas de 401 e também de falha de autenticação ao tentar usar o PWA no comuputador como se fosse WEB é considerado normal. No caso o PWA mobile está acessando normalmente
Nessa segunda será lançada uma versão do PWA para WEB e então vai normalizar esses acessos web, até isso ocorrer nós recomedamos usar o maxGestão WEB acessando pelo portal appsv mesmo para computador e para celular usar o PWA que seria o correto

# GATE-289 - Locks no banco local

**Contexto**

>> Cliente informa que está com lock no banco por conta de JOBs da Máxima, porém conforme verificado na rotina 551 aparentemente no momento não existem locks. Orientado pelo Filipe Padilha a subir chamado pra GATE

**Passos para reproduzir**

- Verificar print apresentado

**Resultado apresentado**

>> Locks no banco do cliente

**Resultado esperado**

>> MAXSOLUCOES não causar locks no banco do cliente

**Diagnostico e orientacao**

Foi feito contato com o cliente hoje de manhã 07/11/2024 e eu busquei entender com o cliente se no momento estão ocorrendo problemas com o banco de dados, no que diz respeito a LOCKs e também a muitas Sessions ativas com JOBS em execução e ele me informou que no momento não tem nada impactando no ambiente dele

Ofereci fazer uma análise, mas ele disse que prefere entrar em contato na hora sinalizando caso tenha problemas. Então eu combinei com ele que se ele tiver problemas com o banco, referente ao assunto desse ticket, ele vai me acionar diretamente via Whatasapp para que eu possa investigar

Obs: De fato estar ocorrendo o problema na hora é necessário porque eu preciso analisar as jobs em execução em tempo real, e também, principalmente se for LOCK. Claro que ele pode também gerar um AWR do banco que guarda esses dados, mas como não temos, ficamos acordados dessa forma

Obs2: Já alinhei com o cliente sobre o MaxViewer e pedi para ele baixar, para deixar pronto caso precisemos conectar na hora para verificar

- Equanto agurdamos alguma ocorrência desse cliente relacionada a esse assunto, vou encerrar esse do GATE e você pode pausar o N1 como aguardando dados

# GATE-295 - Erro no Mix Ideal dando erro

**Contexto**

Cliente relatou sobre um erro em que quando cadastra políticas de desconto e tenta salvar, acaba aparecendo um erro que impede dele de salvar qualquer coisa. O ambiente já foi atualizado (extrator e banco de dados), porém, não houve mudanças

**Passos para reproduzir**

- 1- Tentar cadastrar politica de desconto
- 2- Tentar Salvar

**Resultado apresentado**

Erro descrito na imagem anexada

**Resultado esperado**

Conseguir salvar normalmente sem apresentar erros

**Diagnostico e orientacao**

Se trata de uma falha de sistema porque a gente não está exibindo uma mensagem intuitiva para o usuário; Vamos encaminhar essa questão da mensagem para N3, eu vou assumir o ticket temporariamente e devolver depois

No entanto, é bem importante informar o cliente que, o problema é o cadastro de código auxiliar do produto 1572 na rotina 203 de cadastro de produto. Essa informação está faltando nesse produto, que seria o código auxiliar do produto que é compatível ao cadastro da embalagem. No caso para resolver a situação e ele conseguir cadastrar o produto no mix ideal, ele precisará cadastrar o código auxiliar desse produto

# GATE-304 - maxGestão - com preço em euro

**Contexto**

Verifiquei que o relatorio citado, em

MENU LATERAL > RELATORIOS > Pesquisa "Analise de Ven" > primeiro item
de fato esta em euro

Apos orientação do gatekeeper Filipe, e a atualização do ambiente, o problema permaneceu

Elevado a GATE N2

**Passos para reproduzir**

- MENU LATERAL > RELATORIOS > Pesquisa "Analise de Ven" > primeiro item

**Resultado apresentado**

Relatório exibe os valores monetarios como Euro

**Resultado esperado**

correção

**Diagnostico e orientacao**

Problema já foi corrigido pelo pessoal do MaxGestão quando eu fui analisar já estava normalizado

- Como não está mais ocorrendo e já foi corrigido, então basta entregar para o cliente

# GATE-324 - Divergencia de base, encaminhar a n3

**Contexto**

Ja realizei carga de DTATUALIZ e alteração no CODOPERACAO
sincronizei na base da RCA e não aparecem os produtos

Passei muito tempo tentando conectar no celular dela, não deu certo, maxViewer não instala la

Tratamos por fotos, ela foi me mandando foto a foto das telas que ela se mexia, de fato mudar o DTATUALIZ e o CODOPERACAO não foi suficiente para fazer os produtos da filial2 e filialnf2 funcionarem

- *BASE DO ZERO FUNCIONA NORMAL.*

**Passos para reproduzir**

- Qualquer cliente
- Trocar para filial 2 e filial nf 2
- BASE DO ZERO = PRODUTOS
- BASE CLIENTE = SEM PRODUTOS

**Resultado apresentado**

Divergencia de base

**Resultado esperado**

Carga

**Diagnostico e orientacao**

Os produtos não estavam aparecendo por dois motivos

Haviam itens da MXSPRODFILIAL que não desceram para a base da RCA referente a Filial 2

E também tem uma restrição de venda código 10, que impede a visualização dos produtos na filial 2, por ser uma restrição geral para a filial 2

Se ela voltar reclamando que os itens não estão sendo exbidos, pode ser que seja um cliente pessoa jurídica e ela esteja vendendo na filial, e então a restrição de código 10 vai restringir o acesso

Para ela mudar a restrição de venda pode estar fazendo na Rotina 391 do Winthor

Como ela limpou a base, então os dados da MXSPRODFILIAL foram novamente sincronizados e por isso os itens podem ter voltado a aparecer para clietes PF

Foi feito debug e visto no SQL o motivo dos itens não serem exibidos

Também foram feitos vários testes e hoje, ao baixar a base do zero, independente da versão, os itens não estavam sendo exibidos devido validação da restrição de venda

O João me informou que a cliente limpou a base, então se ela tentar vender para cliente pessoa Jurídica, os itens não serão exibidos, porém se for Pessoa Física, vai aparecer na Filial 2

# GATE-329 - Produto não aparece

**Contexto**

Alguns produtos não aparecem, cliente deu como exemplo o produto 3324

**Passos para reproduzir**

- Acessar aba de produtos, ou em qualquer cliente
- Pesquisar o produto 3324

**Resultado apresentado**

Foi realizado a verificação no banco de dados nuvem e local e identificado que possui divergência entre as tabelas MXSTABPR, na qual no banco local possui dados para e no banco nuvem não
O produto aparece na rotina 316 normalmente
Na APK não

**Resultado esperado**

Produto aparecer na APK

**Diagnostico e orientacao**

O problema do cliente são os registros da tabela MXSTABPR que estão com divergência da PCTABPR conforme foi inforamdo

Isso é causado porque a nossa PGK_CARGA_NUVEM está inválida no ambiente do cliente. Então a nossa TRIGGER tenta executar os comandos para integração, porém como a PKG está inválida, não consegue exeuctar o comando para intergar os registros

Para a PKG deixar de estar inválida, é necessário o cliente executar os grants do arquivo "SCRIPT_TCLOUD_MAXIMA" com um usuário com privilégios, como o SYSTEM, por exemplo no banco de dados do Winthor dele. Dentro desse arquivo tem a GRANT para o MAXSOLUCOES ta tabela PCTRIBUTEXCECAO onde está sendo reportado o problema. --Essa parte de executar os GRANTs eu já pedi para ele, porém é bom reforçar no retorno do ticket no Jira

Depois que ele executar os GRANTs solicitados, pode ser necessário ainda a gente conectar e recompilar a nossa PKG

Porém para evitar que a gente reconecte ele pode também executar a parte, depois de rodar os grants esse comando

ALTER PACKAGE PKG_CARGA_NUVEM COMPILE BODY; COMMIT

Feito isso, pode ser validado comparando ambas tabelas

SELECT * FROM MXSTABPR WHERE CODPROD IN(3324)

SELECT * FROM PCTABPR WHERE CODPROD IN(3324)

Depois de integrado o cliente sincroniza o maxPedido e os produtos devem ser apresentados

# GATE-334 - mix cliente 180 dias

**Contexto**

Com a atualização do prazo máximo do mix do cliente (90 dias), alguns vendedores sentiram dificuldade para realizar consulta de itens. Afinal, esse é uma das funções mais utilizadas do MaxPedido

Tendo em vista o retorno que o PO passou no ticket anterior MXPED-61460, gostaria que fosse avaliado pelo time de desenvolvimento a possibilidade de ampliar para o prazo de 180 dias

**Passos para reproduzir**

- Configurar o parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS para 180 dias

**Resultado apresentado**

Atualmente o parâmetro é de no máximo 90 dias

Cliente solicitou um aumento para 360 dias, porem o o P.O sugeriu analise pela equipe de desenvolvimento para liberar 180 dias

**Resultado esperado**

Configurar o parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS para 180 dias

**Diagnostico e orientacao**

Eu decidi escalar a demanda para N3 como dúvida para pegar a opinião e envolver mais pessoas

O caso é que se fosse tecnicamente falando, o nosso DBA informou que não seria viável os 180 dias porque geraria muito processamento de dados para o banco e pode gerar instabilidade para o cliente

Atualmente eles usam o parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS = 90, o que gera 35 mil registros

Com o parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS = 180, os dados gerados seriam de 95 mil registros

- Se você tiver alguma ponderação do CS ou alguma outra percepção que recebeu do cliente, por gentileza, nos informar

A gente precisa medir os dois lados, o que seria vital para o cliente de informações, a negativa que já veio da melhoria e agora uma segunda negativa para os 180 dias. E o que seria viável para a Máxima no quesito de alteração do parâmetro

# GATE-336 - espelho de rota com campos fixos

**Contexto**

ao analisarmos o cenário da demanda citada, é possível identificar que o menu de impressão de espelho de rota no painel de auditoria, tem apresentado um comportamento que a principio, não é esperado. Quando acessamos o painel de auditoria, existe a possibilidade de configurar quais os campos que serão exibidos no ato da consulta. Porém ao realizar a impressão do espelho de rotas, isso não é levado em consideração e o espelho trás sempre um fomato padrão, com as mesmas colunas. A duvida é: ele deve ter esse comportamento de sempre trazer as colunas "padrão", ou deve trazer as colunas com base no que há no grid? Caso seja o cenário da segunda opção, ocorreram alterações no padrão desse espelho, uma vez que o cliente tem um exemplo de espelho de rotas "antigo" que possui mais colunas que o espelho atual (vide )?

**Passos para reproduzir**

- conforme descrição

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

Enviado para N3 para checarem se o comportamento mudou ou se seria uma falha

Uma sugestão, o cliente ainda consegue extrair todos os dados do Grid, apertando no botão 'exportar dados do grid' que aparece ao aperta na flecha. (Não é o botão Imprimir), dai o grid é exportado conforme os campos configurados para exibição

# GATE-355 - Carregamento infinito ao importar planilha de clientes

**Contexto**

Tô com uma demanda da DESTRO onde o problema só acontece com o cliente, mas o mesmo evidenciou e eu conectei pra validar

Acontece o seguinte
Quando o cliente acessa a tela de pré-pedido na central de configurações e importa os clientes da planilha, no cliente a maioria das vezes fica carregando por muito tempo e não importa. Quando tentei simular, em todos testes que eu fiz deu certo, importou sem problemas

Conectei no computador do cliente e tentei limpar o cache e trocar de navegador, mesmo assim o problema persistiu. Quando troquei de navegador, a primeira importação deu certo, mas ao fazer outro teste o problema voltou a ocorrer

Vou deixar os logs que consegui tirar print, caso sirva de ajuda

Obs: Esse problema acontece só no ambiente de homologação, no ambiente de produção, segundo o cliente, funciona normal

**Passos para reproduzir**

- [AMBIENTE DE HOMOLOGAÇÃO]
- Inteligência de Negócios
- Recomendação de produtos
- Criar um novo pré-pedido
- Importar clientes das planilhas

**Resultado apresentado**

Quando o cliente acessa a tela de pré-pedido na central de configurações e importa os clientes da planilha, no cliente a maioria das vezes fica carregando por muito tempo e não importa. Quando tentei simular, em todos testes que eu fiz deu certo, importou sem problemas

**Resultado esperado**

Importar normalmente a planilha de clientes

**Diagnostico e orientacao**

Foi feita validação e consegui validar o problema na minha máquina, criei um pré-pedido de teste onde ocorre o problema pré-pedido "TESTE MAXIMA", por gentileza, não apagar porque vou enviar para o nosso desenvolvimento validar o erro e ver as possíveis soluções

# GATE-365 - Vendedor está conseguindo passar mais pedidos fora de rota do que está definido no parâmetro QTD_MAX_PED_FORA_ROTA

**Contexto**

O vendedor com codusur 229 conseguiu passar 8 pedidos fora de rota, mesmo estando definido no parâmetro QTD_MAX_PED_FORA_ROTA que é possível passar somente 6 pedidos fora de rota

Os pedidos foram nos clientes 28322,27627,27646,27203,8086,28138,28610,20434, e nenhum desses clientes constam no roteiro do dia 20/11 na ERP_MXSROTACLI, e na MXSCOMPROMISSOS

Mais vemos que na MXSINTEGRACAOPEDIDO tem os pedidos com ID_PEDIDO 28322,27627,27646,27203,8086,28138,28610,20434 que foram realizados nesses clientes fora de rota no dia 20/11

Para a tabela MXSPEDIDOFORAROTA subiu somente 5 pedidos constando como fora de rota, mais na realidade esse vendedor realizou 8 pedidos para clientes fora de rota
Pedidos que constam na MXSPEDIDOFORAROTA são os pedidos com ID_PEDIDO: 345685, 345688, 345804, 345806 e 345910

Identifiquei que só retorna a mensagem que pode realizar 6 pedidos fora de rota nos clientes que não fazem parte do roteiro do dia se arrastar para o lado iniciando um pedido, se gerar uma visita avulsa parece não fazer a contagem como fora de rota

**Passos para reproduzir**

- Acessar o aplicativo
- Iniciar um pedido em qualquer cliente fora de rota gerando uma visita avulsa
- E assim não retorna a mensagem que só pode realizar 6 pedidos fora de rota
- Então acredito que como ele gera visita avulsa para os cliente fora de rota não está contabilizando como pedido fora de rota, e o cliente quer que bloqueio somente 6 pedidos fora de rota mesmo gerando uma visita avulsa no cliente fora de rota

**Resultado apresentado**

Vendedor conseguindo realizar mais pedidos fora de rota do que está definido no parâmetro QTD_MAX_PED_FORA_ROTA

**Resultado esperado**

Que o vendedor consiga realizar somente os 6 pedidos fora de rota definidos no parâmetro QTD_MAX_PED_FORA_ROTA, mesmo que seja gerando uma visita avulsa

**Diagnostico e orientacao**

Referente ao fluxo que você mesma identificou

Então acredito que como ele gera visita avulsa para os cliente fora de rota não está contabilizando como pedido fora de rota, e o cliente quer que bloqueio somente 6 pedidos fora de rota mesmo gerando uma visita avulsa no cliente fora de rota

É exatamente assim que funciona atualmente, quando o RCA faz uma manda gerar uma visita avulsa, ele inclui esse cliente no roteiro, e como ele inclui no roteiro, não conta como pedido fora de rota, e por isso não cai no contador do parâmetro 'QTD_MAX_PED_FORA_ROTA'

Esse é o comportamento atual da aplicação mesmo, para trabalhar de uma forma diferente, eles teriam duas opções que eu pensei

1° Seria uma melhoria para contar a "visita avulsa" que entra para o roteiro como fora de rota; Não sei se faz muito sentido, mas teria que criar uma regra difernte ai específica

2° eles poderiam tirar a permissão de gerar visita avulsa e trabalhar só com o roteiro e com os atendimentos fora de rota pela listagem geral, assim sempre entraria para o contador do parâmetro QTD_MAX_PED_FORA_ROTA. Assim para mim faz mais sentido deles trabalharem, mas dai teria que fazer o repasse para entender com eles se seria viável

# GATE-367 - Divergencia de comportamento entre base do zero e base do app da RCA

**Contexto**

ao realizar a analise sobre a demanda citada, enquanto em base do zero a negociação ocorre de forma regular
!image-2024-11-22-08-18-40-579.png!

Na base do RCA mesmo sincronizando acontece essa situação mesmo sincronizando o app

!image-2024-11-22-08-19-14-083.png!

**Passos para reproduzir**

- efetuar o login na aplicação com o login gtdist.509
- iniciar a negociação para o cliente 29
- tentar negociar os produtos conforme o print na descrição e no video
- comparar os resultados

**Resultado apresentado**

é apresentado divergencia de comportamento entre as bases do zero e base de rca

**Resultado esperado**

que assim que o cliente sincronize o seu aparelho, ele consiga negociar sem falhas o produto

**Diagnostico e orientacao**

Como ele renovou a política hoje no diaComo ele renovou a política hoje no dia

- 2024-11-22 09:05:30.000

- 2024-11-22 09:05:30.000

Quando o RCA sincronizar vai descer normalmente, eu testei na base dele sincronizando e desceu
Dai para garantir que ele sincronize e desça também, eu fiz a carga mesmo assim, o que atualizou para

- 2024-11-22 12:23:01.000

- 2024-11-22 12:23:01.000

Então para resolver o RCA só precisa sincronizar e atualizar a versão do aplicativo, vou explicar abaixo como eu analisei

Analisei as bases que rastreei conforme a dica que você deu de atualização ontem 21/11 às 18:55

E rastreei as políticas anteriores que foram cadastradas pelo cliente nos códigos

72025: 2024-11-22 09:02:26.000

72024: 2024-11-21 18:55:08.000

72019: 2024-11-21 18:55:28.000

A última data de atualização delas foi essa acima ao lado dos códigos e foi um comando de deleção dessas políticas, de forma que inativasse ou não enviasse ao força de vendas

E nesse aspecto o aplicativo se comportou corretamente, baixando as informações conforme o RCA sincronizava

O que pode ter ocorrido é o seguinte, antes o RCA estava na versão 3.220.8, ontem mesmo 21/11/2024 às 18:50

Nesse horário a política 72025 estava na base dele, que é a política que validaria a questão dos descontos. Porém nessa versão, não tem a correção que valida políticas cadastradas dessa forma dtini e dtfim estarem 2024-11-21 00:00:00; (Horário totalmente 00:00:00)

Por isso que ao trocar de versão na ponta deu certo e na do RCA não

Então não é um problema de sincronização de dados e sim da versão, que ao atualizar já resolve o problema de validar a política

# GATE-388 - problemas na leitura de codigo de barras de boleto

**Contexto**

ao analisarmos o cenário relatado estou observando o mesmo comportamento relatado pela cliente: ao gerarmos um boleto, o código de barras está com problemas de leitura, fiz um teste lendo o boleto em aplicativos de banco diferentes e a leitura não aconteceu em nenhum app

**Passos para reproduzir**

- cliente 10177
- compartilhar o titulo 769699-3
- abrir o PDF gerado e tentar fazer a leitura do codigo em algum app de banco
- observar os resultados

**Resultado apresentado**

o codigo de barras do arquivo gerado, não está sendo lido pelo app

**Resultado esperado**

é esperado que o codigo de barras presente no arquivo, seja lido sem problemas

**Diagnostico e orientacao**

Foi feito teste com o documento anexado no ticket do gate e a leitura do código de barras ocorreu com sucesso. Testei no aplicativo do Flash e Banco Itaú

Também fiz o teste com o boleto gerado do banco Safra pelo cliente, que está anexado no ticket principal e capturou o boleto com sucesso

Além disso, baixei a base do RCA que está anexada no ticket de GATE e fiz todos os testes que eu sabia sobre compartilhamento de boleto referente ao número único e ao código de barras começando por

1° teste: Acessar a aba de Consultas >> Títulos Abertos e apertar em "copiar" cima da linha digitável: Depois acessar o aplicativo de pagamento e colar; Boleto gerado com sucesso

2° teste: Acessar a aba de Consultas >> Títulos Abertos e apertar em "Compatilhar" Será gerado um arquivo com o código de barras em um boleto gerado pela Máxima: Depois acessar o aplicativo de pagamento e colar; Boleto gerado com sucesso
Houve um teste que eu fiz em base zerada com o título duplicata número 682733 cuja linha digitável é : 42297.17808 00020.041463 00372.861724 1 93540000078349 e nesse teste deu um erro de CIP. A msg que o banco me retornou foi: "Por favor, entre em contato com a emissora do boleto para solucionar o problema de cadastro na CIP

Eu fiz outro teste com um boleto 7609430-3 e ele está vencido a 36 dias e também gerou com sucesso

Então dito isso eu identifiquei um padrão: Os boletos vencidos a muitos dias estão apresentando esse erro no CIP

Por exemplo: boleto 688057 vencido a 535 dias, deu o mesmo erro da mensagem que citei acima

Com isso eu pensei o seguinte: De fato os números das linhas digitáveis em boletos antigos está com defeito e seria um problema de geração dessa informação no ERP, porque a gente só integra para a nuvem esse campo de linha digitável.Fica no banco local na PCPREST no campo LINHADIG

SELECT * FROM ERP_MXSPREST WHERE DUPLIC IN('682733');--42297.17808 00020.041463 00372.861724 1 93540000078349

Na nossa nuvem LINHADIG da ERP_MXSPREST que é a mesma que é utilizada no maxPedido. Nesse sentido não seria um problema do força de vendas e sim da informação do título que é gerado no ERP e apensas integra com a Máxima

É um problema da informação em si e nesse caso eu não sei nem como poderia orientar o cliente para ele resolver a questão, isso é algo que ele vai precisar verificar no ERP

# GATE-390 - Solicitação de Querys

**Contexto**

A GSA abriu uma demanda solicitando as Querys para montar relatórios personalizados, sendo solicitado

RESUMO DE VENDAS POR VENDEDOR

RESUMO DE VENDAS POR SUPERVISOR X META

RELATORIO DE POSITIVAÇÃO POR MARCA

RELATORIO DE POSITIVAÇÃO POR VENDEDOR

RELATORIO DE POSITIVAÇÃO POR SUPERVISOR

CLIENTES SEM COMPRAS

CLIENTES INADIMPLENTES X DIAS

Desde já agradeço

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

No Suporte, na nossa operação é totalmente inviável a gente oferecer esse tipo de serviço. Por uma série de questões como por exemplo, tempo para confecção das querys, regra de negócios envolvidas, testes, pode correr o risco de a gente tentar fazer e não dar certo ou o cliente não ficar satisfeito

O Thiago Melo também apontou que seja o Produto ou o Suporte a Máxima não oferece esse tipo de serviço, que se enquadraria como Consultoria

Ne sentido, pode ser feita a negativa para a GSA quanto esse assunto porque a Máxima não oferece esse serviço de consultoria na confecção de querys para relatórios personalizados

Como alternativas, eu pensei em 2 possibilidades: 1°o Suporte ou o CS podem procurar o Thiago Castro para entender se o DW (maxInsighits) atenderia nesses cenários que a GSA pediu para gerar os dados e outra possibilidade é de a própria GSA, através do Layout de integração pensar em formas de construir esses SQLs por conta própria que seria o processo correto. Afinal o próprio layout de integração disponibiliza detalhes sobre as tabelas do nosso banco com os atributos e também as relações que elas possuem. Também está descrito a finalidade da tabela no layout de integração

# GATE-391 - Produtos não aparecem na base do RCA (carga)

**Contexto**

Produtos sendo exibidos normalmente em base do zero, porem na base do RCA mesmo com sincronização parcial os produtos não são exibidos

Base do RCA

**Passos para reproduzir**

- Logar no maxPedido
- Iniciar pedido para cliente 376618
- Validar que os produtos são exibidos normalmente
- Importar base do RCA
- Iniciar pedido para o mesmo cliente

**Resultado apresentado**

Na base do RCA nenhum produto é exibido para nenhum cliente

**Resultado esperado**

Produtos sendo exibidos na base do RCA

**Diagnostico e orientacao**

Foi realizada a carga dos dados para o RCA sincronizar e validar se agora os produtos são exibidos corretamente

Foram reenvidas todas as dependências relacionadas aos produtos para garantir quetodos os produtos serão exibidos corretamente. Ou seja, em base zerada eram 169 disponíveis para venda no cliente e com a sincronização eu validei e isso vai descer para o RCA assim que ele realizar o processo

# GATE-393 - Verificar motivo do extrator Tcloud ter caído

**Contexto**

>>O cliente reclamou de demora na integração de pedidos

>>Verificado juntamente ao gate Filipe nos LOGS do grafana que o extrator ficou Ofline durante as 14:17 e 14:57 de hoje 26/11

>>Subindo gate para que seja verificado o motivo do extrator ter ficado ofline

**Passos para reproduzir**

- Verificar no banco nuvem os LOGS do pedido ID_PEDIDO 5706
- Verificar nos Logs do grafana durante este período

**Resultado apresentado**

>>O pedido demorou 38 min para ser integrado
>>Nos Logs do grafana o extrator apresentou erros durante este tempo

**Resultado esperado**

>>O extrator não deveria cair novamente

**Diagnostico e orientacao**

Foram verificados os logs do Extrator e foi constatado que de fato houve uma instabilidade que ocasionou a paralisação da integração com o força de vendas do cliente entre 14:19 e 14:56 do dia 26/11/2024

Segundo o pessoal mais experiente do desenvolvimento backend essa é uma verificação que precisa ser feita em parceria com a TECH, porque até então não há indícios de problemas no código do Extrator ou das aplicações backend do maxPedido, que poderiam ocasionar o problema

Então eu conversei com o Pedro Bernardes, que é da TECH e ele informou que o "Healthcheck estava habilitado e funcionando, ele disse que teve vários logs e que precisaria entender melhor o log, porém era muito conteúdo para analisar

Então dito isso, não tem o que o pessoal do maxpedido backend analisar, teria de ser com a TECH, mas ele me fez um pedido, que se acontecer novamente a mesma situação, a gente analisar na hora do problema, para que assim possa seguir o fluxo >> Gate e depois acionar a TECH

Para o cliente: Você pode dizer basicamente que houve uma instabilidade, que nossos mecanismos automaticamente corrigiram esse problema e por isso voltou a funcionar depois de um tempo sozinho. Porém que vamos continuar acompanhando e caso ocorra novamente algum caso de demora assim na integração ele pode por favor nos informar via ticket que a gente gostaria de tentar analisar o problema acontecendo em tempo real. No momento ele não precisa se preocupar porque está em funcionamento e estável

# GATE-396 - Alto processamento no banco do cliente

**Contexto**

>> Segundo o cliente, o banco do cliente "Reposit" está com processamento alto, por conta de vários processos do MAXSOLUCOES
>> Relatório AWR do chamado

**Passos para reproduzir**

- Verificado relatório AWR

**Resultado apresentado**

>> Alto processamento no banco do cliente, conforme print apresentado

**Resultado esperado**

>> Tabelas do MAXSOLUCOES não causar alto processamento no banco do cliente

**Diagnostico e orientacao**

Enviado para N3 para resguardar uma análise de um desenvolvedor experiente, porém eu vou deixar a minha análise aqui e já uma possível solução visto que o cliente está bastante exaltado com os problemas que vem enfrentando

Baseado na análise do AWR deles e também de casos semelhantes em outros clientes, eu sugiro a criação dos INDEX

Quem precisa criar é o DBA ou alguém com permissão do usuário SYSTEM diretamente no banco do cliente

CREATE INDEX SOLMAR.PCPEDC_MXS01 ON SOLMAR.PCPEDC(DTCANCEL,CONDVENDA,POSICAO, CODCOB) TABLESPACE TS_DADOS

CREATE INDEX SOLMAR.PCPREST_MX01 ON SOLMAR.PCPREST (NUMPED) TABLESPACE TS_DADOS

CREATE INDEX SOLMAR.PCPREST_MX02 ON SOLMAR.PCPREST (CODCOB, DTPAG, NVL (CHEQUETERCEIRO, 'N')) TABLESPACE TS_DADOS

Coletar estatísticas

BEGIN
DBMS_STATS.GATHER_TABLE_STATS(ownname => 'SOLMAR'
tabname => 'PCPREST', cascade => true
estimate_percent => dbms_stats.auto_sample_size)
END

BEGIN
DBMS_STATS.GATHER_TABLE_STATS(ownname => 'SOLMAR'
tabname => 'PCPEDC', cascade => true
estimate_percent => dbms_stats.auto_sample_size)
END

Feito isso ele pode já conferir se os problemas cessaram e aguardar o retorno mais completo do N3

# GATE-405 - Status dos pedidos não atualizam

**Contexto**

Novamente os status dos pedidos não atualizam para os RCAs e ficam divergentes do banco nuvem

Pedido ja consta na MXSHISTORICOPEDC com posição L, mas não é atualizado na base do RCA

Cliente usa Sync automática

**Passos para reproduzir**

- Verificar pedido 223000698 na MXSHISTORICOPEDC

**Resultado apresentado**

Posição L no banco nuvem nas não atualiza na base do RCA

**Resultado esperado**

Status de pedidos atualizando automaticamente

**Diagnostico e orientacao**

O problema já foi corrigido e acreditamos que seja um problema da questão da assinatura, porém o Desenvolvimento ainda não publicou porque é final de mês

No caso nós vamos fazer o seguinte, eu vou reenviar os dados do pedido para o RCA receber novamente a assinatura e o aplicativo baixar automaticamente o status. Isso deve estar resolvendo o problema no momento

A correção definitiva ainda será lançada para evitar que isso ocorra novamente e não precisaremos ficar intervindo

Para valiadar o RCA deve estar verificando por conta própria se na timeline, esse pedido 223000698 foi atualizado para a posição "L

Quando a janela de publicação dessa demanda, se você ou a CS precisarem saber dessa informação, teria que conversar com a Lorrayne. E o Brunão que fez o ajuste

# GATE-407 - KMs incorretos no painel de auditoria

**Contexto**

Alguns RCAs estão contabilizando valores absurdos de KM total e KM trabalhado

Dados referentes ao dia 27/11 no painel de auditoria

**Passos para reproduzir**

- Logar no maxGestão
- Acessar painel de auditoria
- Buscar dados do dia 27/11/2024 para o vendedor 25851

**Resultado apresentado**

Informado que o KM total no dia foi de 13015 km

**Resultado esperado**

Dados corretos

**Diagnostico e orientacao**

Eu fiz uma pré-análise, os dados na API de rastros estão constando com esse km total de 34mil
Nesse caso, eu vou precisar da base maxTracking e também do maxPedido das opções em Ferrametas
>> Exportar Banco
>> Exportar Banco MaxTracking

Porque eu preciso verificar se saiu inconsistente da base do RCA esses rastros

Pode ser só as bases do RCA
25851 - ELTON VENICIO DE OLIVEIRA

Feito isso por gentileza, abrir um novo gate, que dai eu vou dar continuidade

# GATE-408 - Painel de auditoria sem dados

**Contexto**

>> Ao validar informações do rastro do RCA no painel de auditoria, só consta informações a partir das 16:43 à 16:45, o restante do dia sem rastro nenhum

**Passos para reproduzir**

- Acessar MaxGestão (SysMax)
- Geolocalização / Painel de auditoria
- Filtro: Filial 01 / Supervisor: Todos / RCA: Marcos Eli / Data: 27/11
- Acessar dados do RCA

**Resultado apresentado**

>> Durante toda a rota do RCA ao longo do dia, só captou rastro do mesmo a partir das 16:43 e finalizou as 16:45, apresentando quase os mesmos valores em 4 vendas diferentes

**Resultado esperado**

>> Visto que o RCA realizou uma rota de mais de 10 clientes, no qual teve vendas sendo transmitidas e deslocamento, os dados referente à quilometragem era para estar sendo validado

**Diagnostico e orientacao**

Enviar para N3 e vincular na demanda MXGESNDV-15096
As evidências revelaram que o problema já foi identificado e está em processo de correção
Será importante acompanhar se depois que voltar do N3 se o problema foi resolvido de fato

# GATE-414 - Extrator T-Cloud offline

**Contexto**

Extrator Tcloud offline e banco winthor não acessa

**Passos para reproduzir**

- Verificar status do extrator tcloud no grafana

**Resultado apresentado**

Extrator offline

**Resultado esperado**

Extrator online

**Diagnostico e orientacao**

Foi verificado com o Carlos Prates que estava em contato com o pessoal da TOTVs e segundo os dados que obtivemos, houve uma instabilidade na nuvem da TOTVs que os analistas deles atuaram e normalizou

Eu acompanhei os logs da Nutrypower e já está integrando normalmente

Se voltar a acontecer eu acho mais correto o cliente procurar a TOTVs nesse caso já que sem intervenção da Máxima a situação foi normalizada e foi informado pela própria TOTVs problemas no ambiente deles

# GATE-416 - Problema no Processamento de Fotos no Ponto de Montagem

**Contexto**

Filipe/Carlos

Estou enfrentando um problema no ponto de montagem da NORDIL (DILNOR), onde algumas fotos de produtos não estão sendo processadas durante a execução da job de fotos. Esses produtos possuem caminhos válidos no Winthor, mas, ao rodar a job, as fotos de alguns produtos não são processadas, sem que sejam apresentadas mensagens de falha

Verifiquei que as fotos estão no caminho correto no Linux e que os arquivos de fato existem. Não consegui confirmar se as fotos estão corrompidas ou apresentam outro problema. Solicitei ao cliente que realizasse o upload das imagens novamente no Winthor, mas essa ação não trouxe resultados

Obrigado desde já

**Passos para reproduzir**

- Servidor Linux
- Banco nuvem
- SELECT * FROM MXSPRODUTOSFOTOS WHERE CODPROD IN(108827, 108789)
- obs: o produto 108789 tem foto e está ok, o produto 108827 tem foto no Linux mas não gera registro na MXSPRODUTOSFOTOS ao rodar a job no hangfire
- Cliente relatou que o problema acontece em diversos produtos, não só nesses
- Se consultar na SELECT * FROM MXSPRODUTOSFOTOS WHERE LINK LIKE '%found%'
- pode verificar todos os produtos com o problema nas fotos

**Resultado apresentado**

Algumas fotos de alguns produtos não estão sendo processadas ao rodar a job de fotos. Esses produtos tem um caminho válido no Winthor porém ao rodar a job as fotos de alguns produtos não é processada, sem apresentar falhas

**Resultado esperado**

Ao rodar a job, processar as fotos e criar o registro na MXSPRODUTOSFOTOS

**Diagnostico e orientacao**

Existia um problema com as imagens de fato, que era um bug onde elas não atualizavam sozinhas daquela condição de "notfound" ao rodar a job de fotos

Eu não consegui corrigir esse bug (até pq não sou dev ainda né), mas eu resolvi o cenário fazendo o seguinte
Eu alterei o diretório da stack do portainer para uma que não era funcional, colocando P:\FOTOS\, salvei a stack assim e rodei a job

Com isso, todas as fotos foram apagadas, até as que estavam com problemas de "notfound" só que a job apagou elas no S3 e também no banco nuvem

Depois disso eu só troquei novamente na stack para o original \\192.168.8.103\p\PRODUTOS_DILNOR\ e disparei a job. Todas as fotos voltaram a subir e inclusive as dos produtos que estavam com problemas atualizaram e passaram a ser exibidas com link válido no S3
SELECT * FROM MXSPRODUTOSFOTOS m WHERE CODPROD IN(108771, 108776, 108875, 108777, 108876, 108773, 108774, 108829, 108830, 108831, 108832, 108926)

Nesse caso eu descobri também que o "p" ou "P" e o "jpg" ou "JPG" não mudam nada no cenário

As fotos que continuam com codoperacao 2 ou inválidas, ou não existe um diretório como no caso do produto 108827; Tem um motivo específico. Ou o cadastro da DIRFOTOPROD está errado, ou a imagem não existe na pasta de fotos

No caso do produto 108827 em específico, como eles mudaram a imagem na pasta de fotos para "108827.jpeg" e na DIRFOTOPROD da PCPRODUTO está "108827.JPG", dai nossa job não encontrou a imagem para atualizar. Ai para resolver basta eles ou mudarem a imagem novamente para jpg ou trocar no cadastro do produto para jpeg

# GATE-420 - maxPag - Pedido ja pago, reenviado por engano, não chega ao winthor

**Contexto**

O numped 19471392 é um pedido de 16.000 que foi pago, porem não chegou no ERP
O motivo original era que a data que a previsão de faturamento que havia sido selecionada era inconpativel com o parametrizado no ambiente do cliente

Tentei alterar a data para permitir que o pedido chegasse ao erp mas ao seguir o curso de reenviar o pedido, acabou que o pedido entrou novamente no fluxo do maxPag e gerou um novo link e ficou preso no limbo de aguardando pagamento
SQL's realizados

SELECT * FROM MXSINTEGRACAOPEDIDO ORDER BY DATA DESC
SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPED =19471392 AND CODUSUR = 1947
SELECT * FROM MXSINTEGRACAOPEDIDO_LOGST WHERE ID_PEDIDO = 597520
SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED =

SELECT * FROM MXSHISTORICOCRITICA WHERE ID_PEDIDO = 597520

SELECT * FROM MXSMAXPAYMENTMOV WHERE ID_PEDIDO = 597520

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%PRAZO_VALIDADE_PEDIDO%'
SELECT * FROM MXSPARAMETRO ORDER BY CODPARAMETRO DESC

**Passos para reproduzir**

- BASE DE DADOS ANEXADA
- TIMELINE DE PEDIDOS, NUMPED 19471392 não envia ao ERP

**Resultado apresentado**

O pedido está preso em um loop do maxPag de geração de um novo link de pagamento, e apesar de já ter sido pago via PIX o pedido não chega ao ERP para ser montado

**Resultado esperado**

Conseguir passar o pedido de modo que chegue ao Winthor

**Diagnostico e orientacao**

Funciona assim: Quando o pagamento é aprovado, tem uma função no nosso backend que valida esses dados do pagamento e seta o pedido para status 0 para ele ser enviado ao ERP e processado

Então o que eu fiz foi isso setei para 0 e já acompanhei que foi integrado normalmente no Winthor e gerou a crítica

Descricao": ">>PEDIDO : 19471392\n594910 - MOUSTACHE BEAMS LTDA\nTotal : 16441.42\n--------------------------------------------\nPedido Winthor Normal : 1947002945\nVlr. Total : 16441.42\nVlr. Atendido : 16371.91\nQt Tot.Itens(Ped.Principal): 58\nQt Itens Atend: 57\n\n\nProduto: 16570 - ALGODAO 1X25G COTTONBABY CAIXA-Qt. Pedida: 27 Qt. Atendida: 0\n\nAtenção! A quantidade solicitada de um dos produtos foi menor que a quantidade faturada. Verifique se houve falta em um dos produtos do seu pedido. \n\nAtenção! A integradora informou que houve corte em um ou mais produtos do seu pedido. \n

E posição Liberado. O corte a gente vai estornar o PIX automaticamente quando o pedido for faturado. Já sobre o parâmetro PRAZO_VALIDADE_PEDIDO, ele fez diferença porque ao colocar 30 dias ele permitiu que o pedido fosse integrado

Porém é melhor colocar ele para 7 dias depois que acabar essa novela desse pedido

# GATE-422 - Dados na tabela MXSQTDEPRODVENDA não estão sendo gerados

**Contexto**

Cliente abriu uma demanda em julho para verificar a possibilidade da aplicação exibir a quantidade de venda dos produtos nos últimos 3 meses. Na ocasião em questão, foi informado que o cliente deveria enviar as tabelas ERP_MXSMOV e ERP_MXSNFSAID, e que o parâmetro GERAR_DADOS_QTDEPRODVENDA deveria estar = 'S', para que fossem gerados os dados na tabela MXSQTDEPRODVENDA e as quantidades fossem exibidas
Foi verificado então que uma das condições para que o registro fosse gerado, era que o campo ERP_MXSMOV.CODUSUR deveria estar igual ao campo ERP_MXSNFSAID.CODUSUR, entretanto o cliente já está realizando o envio desses dados conforme prints apresentados e mesmo assim os dados na MXSQTDEPRODVENDA não são gerados

**Passos para reproduzir**

- Entrar no banco do cliente, selecionar uma nota fiscal na tabela ERP_MXSNFSAID qualquer e comparar os campos da ERP_MXSMOV

**Resultado apresentado**

É verificado que embora o cliente esteja realizando o envio dos dados de corretamente em ambas as tabelas, os registros de venda na MXSQTDEPRODVENDA não estão sendo gerados

**Resultado esperado**

É esperado que a tabela em questão seja gerada pela job e exiba as quantidades de venda dos meses anteriores

**Diagnostico e orientacao**

O Script completo que gera a MXSQTDEPRODVENDA é esse
SELECT CODCLI
CODPROD
TRUNC(DATA,'mm') DATA
SUM (CASE WHEN TIPOOPER = 'D' THEN 0 ELSE QTDEVENDA END) AS QTDEVENDA
FROM ( SELECT ERP_MXSNFSAID.CODCLI
MXSPRODUT.CODPROD
TRUNC(ERP_MXSNFSAID.DTSAIDA,'mm') DATA
'P' AS TIPOVENDA
'V' AS TIPOOPER
NVL (ERP_MXSMOV.QT,0) QTDEVENDA
FROM ERP_MXSNFSAID
MXSPRODUT
ERP_MXSMOV
MXSCLIENT
MXSUSUARI
MXSPLPAG
MXSFORNEC
WHERE ERP_MXSMOV.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA
AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD
AND ERP_MXSNFSAID.CODCLI = MXSCLIENT.CODCLI
AND MXSFORNEC.CODFORNEC = MXSPRODUT.CODFORNEC
AND ERP_MXSNFSAID.CODUSUR = MXSUSUARI.CODUSUR
AND ERP_MXSNFSAID.CODFILIAL IN (SELECT DISTINCT CHAVEDADOS FROM MXSACESSODADOS WHERE CODDADOS = 6)
AND ERP_MXSNFSAID.CODPLPAG = MXSPLPAG.CODPLPAG
AND NVL(ERP_MXSNFSAID.CODFISCAL,0) NOT IN (522,622,722,532,632,732)
AND NVL(ERP_MXSNFSAID.CONDVENDA,0) NOT IN (4,8,10,13,20,98,99)
AND (ERP_MXSNFSAID.DTCANCEL IS NULL)
AND MXSCLIENT.DTEXCLUSAO IS NULL
AND ERP_MXSMOV.CODFILIAL = ERP_MXSNFSAID.CODFILIAL
AND ERP_MXSNFSAID.DTSAIDA BETWEEN ADD_MONTHS(TRUNC(SYSDATE,'MM'),-3) AND LAST_DAY(SYSDATE)
AND ERP_MXSNFSAID.CODOPERACAO != 2
AND MXSPRODUT.CODOPERACAO != 2
AND ERP_MXSMOV.CODOPERACAO != 2
AND MXSCLIENT.CODOPERACAO != 2
AND MXSUSUARI.CODOPERACAO != 2
AND MXSPLPAG.CODOPERACAO != 2
AND MXSFORNEC.CODOPERACAO != 2
UNION ALL
SELECT ERP_MXSNFSAID.CODCLI
MXSPRODUT.CODPROD
TRUNC(ERP_MXSNFENT.DTENT,'mm') DATA
'P' AS TIPOVENDA
'D' AS TIPOOPER
NVL (ERP_MXSMOV.QT * -1, 0) QTDEVENDA
FROM ERP_MXSNFENT
ERP_MXSESTCOM
ERP_MXSNFSAID
ERP_MXSMOV
MXSPRODUT
MXSCLIENT
MXSFORNEC
MXSPRACA
WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT
AND MXSCLIENT.CODPRACA = MXSPRACA.CODPRACA
AND ERP_MXSESTCOM.NUMTRANSENT = ERP_MXSMOV.NUMTRANSENT
AND MXSFORNEC.CODFORNEC = MXSPRODUT.CODFORNEC
AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+)
AND (ERP_MXSESTCOM.NUMTRANSVENDA <> 0 OR (ERP_MXSESTCOM.NUMTRANSVENDA = 0)) --AVULSAS
AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD
AND ERP_MXSNFENT.CODFORNEC = MXSCLIENT.CODCLI
AND ERP_MXSNFSAID.CODFILIAL IN (SELECT DISTINCT CHAVEDADOS FROM MXSACESSODADOS WHERE CODDADOS = 6)
AND NVL (ERP_MXSNFENT.CODFISCAL, 0) IN (131,132,231,232,199,299)
AND ERP_MXSMOV.DTCANCEL IS NULL
AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA'
AND NVL (ERP_MXSNFSAID.CONDVENDA, 0) NOT IN (4,8,10,13,20,98,99)
AND ERP_MXSNFENT.DTENT BETWEEN ADD_MONTHS(TRUNC(SYSDATE,'MM'),-3) AND LAST_DAY(SYSDATE)
AND ERP_MXSNFENT.CODOPERACAO != 2
AND ERP_MXSESTCOM.CODOPERACAO != 2
AND ERP_MXSNFSAID.CODOPERACAO != 2
AND ERP_MXSMOV.CODOPERACAO != 2
AND MXSPRODUT.CODOPERACAO != 2
AND MXSCLIENT.CODOPERACAO != 2
AND MXSFORNEC.CODOPERACAO != 2
AND MXSPRACA.CODOPERACAO != 2
)
GROUP BY CODCLI, CODPROD, TRUNC(DATA,'mm')
ORDER BY CODCLI, TRUNC(DATA,'mm'), CODPROD

Nele tem uma primeira parte do SQL que verifica no WHERE o seguinte: ERP_MXSMOV.CODFILIAL = ERP_MXSNFSAID.CODFILIAL

E é justamente essa parte que a gente valida para consolidar a quantidade vendida por mês e que esse cliente não está enviando corretamente. Então abaixo eu vou explicar olhando para um cenário

Vamos pegar o pedido de forma aleatória: NUMPED 1000194898, por exemplo

SELECT * FROM MXSHISTORICOPEDC WHERE CODCLI IN(10029) AND NUMPED IN(1000194898) ORDER BY DATA DESC

Nele nós vamos olhar se ele existe lá na ERP_MXSMOV
SELECT * FROM ERP_MXSMOV WHERE NUMPED IN(1000194898)

- E existe (e está certo vários registros porque ele grava por item), então vamos olhar o CODFILIAL dele

SELECT NUMPED, CODPROD, CODOPERACAO,NUMTRANSVENDA,CODFILIAL FROM ERP_MXSMOV WHERE NUMPED IN(1000194898)

- NUMTRANSVENDA: 1070199869
- CODFILIAL: NULL

- Agora vamos olhar na ERP_MXSNFSAID

SELECT NUMPED, CODOPERACAO,NUMTRANSVENDA,CODFILIAL FROM ERP_MXSNFSAID WHERE NUMPED IN(1000194898)

- NUMTRANSVENDA: 1070199869
- CODFILIAL: 1

Então isso fere a validação que a gente faz para consolidar os dados que é o ERP_MXSMOV.CODFILIAL = ERP_MXSNFSAID.CODFILIAL
e por isso, os dados não são gerados na MXSQTDEPRODVENDA

Para resolver a integração do cliente deve nos mandar o CODFILIAL compatível nesses endpoints ERP_MXSMOV e ERP_MXSNFSAID

E porque dessa alteração (caso a integração questione): A nossa resposta pode ser que simplesmente o cliente quer usar uma funcionalidade nova do força de vendas que depende dessa informação e então eles precisariam mandar esse dado para dar certo

# GATE-427 - Parâmetros cadastro de cliente

**Contexto**

O cliente LDF abriu uma demanda questionando sobre alguns parâmetros da central de configurações que ele não sabe o funcionamento, e nem eu

Gostaria de ajuda pra entender o que fazem esses parâmetros de "cadastro de cliente

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

Todas essas informações vão do maxPedido via integração para o Winthor e chegam na PCCLIENTFV que é a tabela intermediária da integração. A tabela que finaliza o cadastro é a PCCLIENT que a TOTVs grava, a gente vai somente até a PCCLIENTFV

Todos esses parâmetros são validados somente por usuário ou perfil de usuários. Não tem para geral e nem por filial

Cadastro de cliente: Valor do credito do cliente": Serve para definir um limite de crédito disponível para todo novo cliente cadastrado pelo RCA através do maxPedido. (O RCA não pode alterar essa informação, vai padrão da integração do maxPedido para o Winthor)

Cadastro de cliente: Valor padrão para Calcular ST": Serve para definir se é calculado ST no cliente (O RCA não pode alterar essa informação, vai padrão da integração do maxPedido para o Winthor)

Cadastro de cliente: Valor padrão para Cliente contribuinte": Serve para vir marcado por padrão se o cliente é contribuinte ou não, essa informação é exibida na tela de cadastro de clientes do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das permissões do usuário

Cadastro de cliente: Valor padrão para Plano de Pagamento": Serve para vir padrão um plano de pagamento cadastrado para o cliente, essa informação é exibida na tela de cadastro de clientes dentro do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das configurações do formulário de cadastros da Central (Configurações > Configurações > Formulários)

Cadastro de cliente: Valor padrão para Praca de Atendimento": Serve para vir padrão uma praça cadastrado para o cliente, essa informação é exibida na tela de cadastro de clientes dentro do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das configurações do formulário de cadastros da Central (Configurações > Configurações > Formulários)

Cadastro de cliente: Valor padrão para Simples Nacional": Serve para vir marcado por padrão se o cliente é simples nacional ou não, essa informação é exibida na tela de cadastro de clientes do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das permissões do usuário

Cadastro de cliente: Valor padrão para Tipo de Cobranca": Serve para vir padrão uma cobrança cadastrada para o cliente, essa informação é exibida na tela de cadastro de clientes dentro do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das configurações do formulário de cadastros da Central (Configurações > Configurações > Formulários)

Cadastro de cliente: Valor padrão para Tipo de Empresa": Por padrão vem "P", eu não achei essa informação para ser alterada pelo aplicativo, mas eu acredito que ela vai assim padrão para que não ocorra problemas com a integração com o Winthor. E então chega no campo TIPOEMPRESA na PCCLIENTFV

# GATE-433 - Carga atualizid para historico de pedidos dos clientes

**Contexto**

>>O RCA 18 entrou de férias e o cliente passou os clientes para o RCA 19, por isso ele quer que façamos carga no RCA 19 para que o histórico de pedidos dos cliente apareçam para ele

**Passos para reproduzir**

- Baixar a base do RCA 19
- Abrir os clientes por exemplo o cliente 198870170

**Resultado apresentado**

>>No momento não aparece o histórico de pedidos dos clientes recém transferidos do antigo RCA

**Resultado esperado**

>>O Histórico de pedidos dos clientes deve aparecer para o RCA

**Diagnostico e orientacao**

Foi realizada a carga de dados das tabelas MXSHISTORICOPEDC e MXSHISTORICOPEDI para as vendas realizadas dos RCAS 18 e 19 dos últimos 100 dias, porém o parâmetro de histórico deles está para 30 dias, então vai exibir histórico dos últimos 30 dias de compras
CATALOGO_PEDIDOS_DIAS_SYNC = 30

Se eles quiserem mais dias, ai teria que mudar o parâmetro e fazer a carga de novo

# GATE-434 - Resumo de venda não atualiza

**Contexto**

Resumo de venda não atualiza. Foi verificado as portas 9000/9002 e ambas entao liberadas

Foi visto no banco nuvem na tabela MXSDIASUTEIS e não tem dias uteis cadastradas para o ano de 2024

Foi verificado no banco local do cliente e na tabela PCDATAS aparecem os dias cadastradas no ano de 2024

**Passos para reproduzir**

- Acessar maxPedido, ir em objetivos e pesquisar, depois ir em atualizar menu

**Resultado apresentado**

>> Resumo de venda não atualiza

**Resultado esperado**

>> Resumo de venda atualiza

**Diagnostico e orientacao**

Pelo o que eu analisei usando o IP deles externo: nas portas 9000 e 9002 eles estão inacessíveis

Para testar o teste de portas, você pode fazer assim

IP deles público: 201.86.30.77

Portas 9000 e 9002

Não deu para acessar via VPN e nem Workspace quer dizer que eles estão totalmente bloqueados para acesso externo, por isso o resumo de vendas não atualiza

Para fazer o suporte ao extrator a gente usa a porta 9000 e para atualizar o menu e outras funcionalidades que envolvem API, a gente usa a porta 9002

Para resolver então eu sugiro que eles façam liberação de TCP externo para qualquer IP externo que tentar conexão nessas portas 9000 e 9002

Conforme consta no nosso site
- * *Acesso externo para servidor Máxima:* Portas TCP 9000, 9001, 9002, 9003 (Liberar no firewall (NAT) para acesso externo)

Outra opção que eles tem, caso não queiram liberar acesso total, seria liberar somente para os IPS e portas citados na listagem

- *Acesso externo Liberados no Firewall nos seguintes IP’s e Portas**:* (incluir uma tabela)

os ips constam no site

Depois que eles liberarem os acessos externos, dai pode baixar uma base e fazer o teste de atualização de menu no maxPedido

# GATE-435 - desativar PWA

**Contexto**

Segue abaixo relato da cliente, a qual deseja desativar o PWA, pois tem gerado dificuldades em sua operação

Existe uma forma de desabilitar o novo painel?

Motivo: Quando efetua o login no gestão, pede novamente para efetuar o login e o pessoal estão reclamando

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

Atualmente para desativar a opção do maxGestão web redirecionar para o PWA web com as opções dos dashboards novos, teria que fazer manualmente via banco a configuração da seguinte forma

- Confere os usuários que precisam ter a opção desligada
SELECT MOSTRARNOVIDADES, MXSUSUARIOS.* FROM MXSUSUARIOS WHERE CODUSUARIO IN()

- Marca para não mostrar as novidades
UPDATE MXSUSUARIOS SET MOSTRARNOVIDADES = 'N' WHERE CODUSUARIO IN(); COMMIT

# GATE-437 - Incluir itens nas familias já criadas no Desconto Progressivo

**Contexto**

O cliente precisa adicionar novos produtos nessas famílias que foram cadastradas sem filial

**Resultado apresentado**

Anteriormente, era possível usar o botão "Importar Produtos via XLS" sem a necessidade de selecionar uma filial. No entanto, com a alteração no comportamento do sistema, agora é obrigatório marcar uma filial para realizar essa importação

Por conta dessa mudança, as famílias de produtos criadas antes dessa atualização não estão permitindo a adição de novos produtos

**Resultado esperado**

Inserir os novos produtos

**Diagnostico e orientacao**

Inclusão dos itens nas famílias conforme do ticket realizado com sucesso

Para validar conferir no banco ou através da central no cadastro das famílias

# GATE-444 - Carga de dados - itens em promoção

**Contexto**

Cliente relata que na base do RCA em questão, ao acessar a aba 'Tabela' e selecionar o filtro de produtos em promoção, a aplicação retorna alguns itens incluindo o 22156, entretanto esse item não consta em promoção. Foi realizado teste em base zero e verificado que o produto não é apresentado como 'Em promoção', entretanto ao realizar o mesmo teste na base do RCA o produto é apresentado como 'Em promoção'
Favor realizar a carga no usuário em questão

Login para teste
5estrelas.145

**Passos para reproduzir**

- Entrar na base do vendedor, iniciar um pedido no cliente 37258, filial 1, plano de pagamento 8 , cobrança BOLETO. Na aba 'tabela', selecionar o filtro 'Em promoção'

**Resultado apresentado**

É verificado que o item 22156 consta em promoção na base do rca, mas em base zero o item é apresentado normalmente

**Resultado esperado**

É esperado que o item em questão não seja apresentado em promoção

**Diagnostico e orientacao**

Foi feita a carga de dados da tabela MXSPRODUTMSK para normalizar a base do maxPedido

Para validar os RCAs só precisam estar sincronziando o sistema. Eu mandei uma normalização geral para já evitar qualquer outro caso em outros RCAs

- Não passar ao cliente

Só para você ficar ciente e ficar também documentado

- Como o registro não existe mais no banco de dados nuvem na tabela MXSPRODUTMSK , então não tem como investigar o motivo de não ter descido naturalmente via sincronismo parcial do maxPedido

# GATE-447 - PCTABPRCLI e MXSTABPRCLI divergentes

**Contexto**

>>Cliente diz que ao cadastrar na rotina 3314 o maxPedido ainda não está validando a região cadastrada

>>Verifiquei que o cliente 2619 de exemplo possui registro na PCTABPRCLI, mas não na MXSTABPRCLI

>>Segundo o cliente são vários casos

**Passos para reproduzir**

- Baixar a base do RCA
- Iniciar pesido para o cliente 2619 e incluir um produto (2641 de exemplo)

**Resultado apresentado**

>>O valor que aparece pertence a região 1 e não a 2 que está cadastrada na PCTABPRCLI

**Resultado esperado**

>>A PCTABPRCLI e a MXSTABPRCLI devem estar iguais
>>O valor que aparece para o cliente deve ser correspondente a região cadastrada na 3314 (PCTABPRCLI )

**Diagnostico e orientacao**

A nossa trigger da PCTABPRCLI só sobe dados se a filial de importação configurada do registro estiver configurada na tabela PCMXSCONFIGURACOES

Como o registro é da filial 3, e na PCMXSCONFIGURACOES o CODFILIAL_IMPORTACAO = 3 não estava configurado, o registro não subiu

Então para resolver eu configurei a filial 3 na CODFILIAL_IMPORTACAO da PCMXSCONFIGURACOES no banco local do cliente

Depois fiz a carga de filial nova, no caso filial 3

Enviei o ticket para a TECH só porque me solicitaram para formalizar

# GATE-451 - divergencia de precificação entre app e 316

**Contexto**

ao analisar o cenário da demanda citada, estamos observando que o aplicativo está apresentando uma precificação divergente da apresentada na rotina 316 do cliente. Ao negociar um pedido para o seguinte cliente

!image-2024-12-04-12-26-25-805.png!

Vejam o comparativo de comportamento entre os dois cenários abaixo

!image-2024-12-04-12-09-29-821.png!

!image-2024-12-04-12-11-03-447.png!

essa situação gera o bloqueio para inserção aqui observado

!image-2024-12-04-12-12-11-318.png!

porém essa situação não deveria ocorrer, pois não há politicas comerciais para o produto

!image-2024-12-04-12-29-23-341.png!

e baseado no preço de venda do item, o valor negociado não deve ter desconto

!image-2024-12-04-12-13-50-180.png!

em validações de comparativo da origem de preço, observei que a 316 traz uma origem de preço com alguns valores de codigo de tributação diferentes do que há no app

!image-2024-12-04-12-18-19-695.png!

!image-2024-12-04-12-18-44-102.png!

consultando os valores que constam na mxstribut para o codst 43, há alguns registros que divergem do que há para a origem de preço da 316

!image-2024-12-04-12-23-07-105.png!

Nesse cenário e com base nessas evidencias, o que pode estar gerando essa divergência de precificação? Ao que tudo indica há uma situação de divergência de aplicação de tributação sendo apresentada, isso é gerado por qual motivo? O que deve ser feito para que o aplicado se comporte de forma a trazer os preços da mesma forma que há na 316?

**Passos para reproduzir**

- cliente: 26309
- filial 2
- produto 101002
- tentar negociar o item com o preço de venda da MXSTABPR para a região do cliente e observar os resultados

**Resultado apresentado**

o app, aparentemente, está acrescendo um valor de forma inesperada diretamente no preço de tabela do item

**Resultado esperado**

é esperado que a negociação ocorra de forma adequada da mesma forma que ocorre na 316

**Diagnostico e orientacao**

Foi feita carga de algumas tabelas que envolvem cenário de tributação e preço (MXSTABPR, MXSTABPRCLI, MXSTRIBUT, MXSTRIBUTEXCECAO, MXSTRIBUTEXCECAOREGRA e MXSTABTRIB) porém, mesmo assim o maxPedido continua apresentando o preço de venda com divergência da 316

Será enviado para N3 para verificarem se é problema de cálculo ou se ainda tem alguma divergência

# GATE-454 - Conta Corrente está com o saldo negativo.

**Contexto**

O cliente relata que está com o saldo da conta corrente negativo, mesmo depois de atualizar a versão do aplicativo

**Passos para reproduzir**

- 1 - Abrir o maxPedido
- 2 - Ver a CC negativa

**Resultado apresentado**

CC ao invés de estar zerada, está com saldo negativo

**Resultado esperado**

CC com o valor padrão correto

**Diagnostico e orientacao**

Se você importar a base do RCA, como ele tem pedidos na base, que transmitiu e que consumiram conta corrente, então o parâmetro DESCONTA_SALDOCCRCA_OFFLINE da MXSPARAMETRO faz o cálculo somente a nível de maxPedido para exibir para o RCA já uma prévia da conta corrente que ele movimentou

Esse parâmetro causa propositalmente divergência das informações do ERP e dos endpoints MXSSALDOCCRCA e MXSUSUARI

Então para resolver, será necessário entender com o cliente se ele quer trabalhar com conta corrente nesse RCA. Se ele quiser trabalhar então esteja ciente que esse parâmetro DESCONTA_SALDOCCRCA_OFFLINE realmente gera esse comportamento, para reter o saldo de conta corrente conforme o RCA já for negociando usando o maxPedido

Ele pode usar conta corrente, mas não trabalhar com o DESCONTA_SALDOCCRCA_OFFLINE, o caso, é que se ele estiver ativo, como expliquei o cálculo já ocorre conforme o RCA negocia os pedidos no maxPedido. Então se ele usar conta corrente, porém o parâmetro DESCONTA_SALDOCCRCA_OFFLINE = N; O maxPedido vai fazer a leitura do MXSSALDOCCRCA

Se ele não quiser trabalhar com o Conta Corrente e quiser que fique totalmente zerado, então teria que desativar esse parâmetro DESCONTA_SALDOCCRCA_OFFLINE

Na base do zero, como não tem nenhum pedido ainda transmitido, que alimente a tabela mxspedido (salvou ou bloqueado, ou salvo e enviado) então o conta corrente fica R$0,0

# GATE-460 - Compromissos não descem para a base do RCA

**Contexto**

Cliente relata que os roteiros do usuário codusur 3481 não estão sendo apresentados no aplicativo. Foi realizada a atualização de todo o ambiente do cliente e simulação em base zero, onde ao consultar a tabela MXSCOMPROMISSOS via inspect foi verificado que não constava nenhum registro, indicando que os dados não foram baixados do banco nuvem ao subir a base
Foi realizada comparação dos registros da ERP_MXSROTACLI com a MXSCOMPROMISSOS no banco nuvem e observado que os registros do dia 05/12 em diante na MXSCOMPROMISSOS constavam com o CODOPERACAO = 2. Foi realizado o update nos registros acima do dia 05/12 e tentativa de subir a base novamente, onde os registros continuaram a não serem enviados para a base

Login para teste
refil.juliano

O cliente é Winthor e a situação ocorre também com o usuário refil.bento

**Passos para reproduzir**

- Entrar na base zerada do vendedor, ir na aba 'Clientes' e selecionar a opção 'Roteiro' ou 'Roteiro hoje'

**Resultado apresentado**

É verificado que o roteiro não é apresentado

**Resultado esperado**

É esperado que o roteiro seja apresentado para o vendedor

**Diagnostico e orientacao**

O RCA que utilizamos como cenário foi o REFIL.juliano cujo CODUSUR é o 3481

Ele possui rota cadastrar na ERP_MXSROTACLI para os clientes: (106917, 79299, 109903, 113916, 127567, 128772, 129278, 134842, 131826, 71451)

Nenhum desses clientes está na carteira do RCA 3481, por isso, a job roda e não gera os compromissos como ativos para o RCA na MXSCOMRPOMISSOS

Para conferir que os clientes não estão na carteira
SELECT CODCLI, CODUSUR1, CODUSUR2, CODUSUR3 FROM MXSCLIENT WHERE CODCLI IN(106917, 79299, 109903, 113916, 127567, 128772, 129278, 134842, 131826, 71451)
SELECT * FROM ERP_MXSUSURCLI WHERE CODCLI IN(106917, 79299, 109903, 113916, 127567, 128772, 129278, 134842, 131826, 71451) AND CODUSUR IN(3481)

Então para resolver e gerar os compromissos é obrigatório que os clientes sejam da carteira do RCA

# GATE-465 - Pedido estornado após faturamento

**Contexto**

Foi identificado que o pedido *2160003614* teve corte de itens no *WinThor*, resultando em uma divergência de valores em relação ao valor original enviado pelo *maxPedido*. Nesse cenário, o comportamento esperado seria o estorno apenas do valor referente ao corte, e não do valor total do pedido

Conversei com o Divino, que mencionou o seguinte
{quote}_"O problema deve estar nesse valor (imagem apresentada). Tem uma regra que, quando passa 0, o maxPag estorna o valor total. Tem que verificar isso aí com o pessoal do maxPedido. Se bloquear isso, pode afetar no fluxo deles lá."_
{quote}

**Passos para reproduzir**

- Acessar maxPag, verificar pedido estornado no valor R$ 2.088,50, NSU 415022. 28/11/2024 16:49

**Resultado apresentado**

>> pedido 2160003614 foi estornado após faturamento

**Resultado esperado**

>> Caso tenha corte de itens no pedido, estorna somente o valor do corte e não o valor total

**Diagnostico e orientacao**

Analisei os dados do chamado anterior MXPED-62118 que foi citado pelo cliente e aparentemente o problema é o mesmo

O pedido foi na verdade estornado totalmente quando houve corte de apenas um item no pedido no dia 2024-12-02 20:36:47. E depois de estornado ele foi Faturado

Nesse pedido 21601735, não vai ter mais o que a gente fazer, no sentido que, como o PIX já foi estornado, então agora eles teriam que conferir com esse cliente se foi mesmo estornado e solicitar o pagamento novamente

Referente o problema ter ocorrido, a correção foi feita no último ticket e foi lançada a versão de extrator 3.1.2.446. Porém o cliente não foi atualizado e estava na versão 3.1.2.440. Então hoje eu atualizei eles para a 3.1.2.449 e também atualizei o banco nuvem e local. Isso deve estar resolvendo o problema, evitando que ocorra novamente. Então a correção é válida para os novos pedidos transmitidos a partir de hoje

# GATE-468 - Trajeto incorreto do RCA aos clientes

**Contexto**

>>O trajeto do RCA 70 (Codusuario: 104860) mostra uma rota incorreta do RCA onde ele de tempos em tempos retorna a um ponto específico do mapa

>>Os parâmetros "GPS_TRACKING_ENABLED" e "HABILITA_EVENTOS" ativos simultâneamente

>>Base maxTracking

**Passos para reproduzir**

- Entrar em geolocalização
- Clicar no RCA
- Colocar qualquer data (Aparecem acima do dia 18)

**Resultado apresentado**

>>No trajeto do RCA mostrado, a localização do RCA "pula" para um ponto específico no mapa de tempos em tempos, gerando assim um transtorno
>>Os parâmetros "GPS_TRACKING_ENABLED" e "HABILITA_EVENTOS" estão ativos simultâneamente

**Resultado esperado**

>>A localização apresentada deve ser a mesma feita pelo RCA

**Diagnostico e orientacao**

Vamos fazer o seguinte, na tentativa de resolver para que não ocorram casos futuramente do mesmo problema

Desativa o parâmetro HABILITA_EVENTOS = N para todos os RCAs
Deixa ativado somente o GPS_TRACKING_ENABLED = S; (do jeito que já está)

E solicita para todos os RCAs atualizarem para a última versão, Libera no portal deles a última versão

Feito isso, pede para acompanhar se, depois de atualizado, parou de ocorrer o problema. Caso ocorra o problema, mesmo atualizado, dai pode mandar outro GATE; Se ocorrer em versão desatualizada, cobra fazer a atualização do RCA

Referente ao cenário já apresentando (dos rastros picotados) eu não sei se tem como converter, então eu vou mandar para N3 do maxgestão para eles darem uma olhada

# GATE-469 - Sequenciamento de visitas

**Contexto**

Cliente relata que a aplicação não está obrigando o RCA a realizar a sequência de visitas, mesmo com a permissão 'Obrigar sequenciamento de visitas' ativa para o RCA e o parâmetro UTILIZA_CHECKIN_CHECKOUT ativo para o RCA

Foi verificado que o rca em questão possui roteiro cadastrado no dia

Além disso, os testes foram realizados em base zero na versão de ponta

**Passos para reproduzir**

- Entrar na base do rca, iniciar um pedido e realizar checkin no primeiro cliente do dia, realizar o pedido e checkout. Em seguida, realizar o checkin no último cliente do dia

**Resultado apresentado**

É verificado que o fluxo citado na reprodução é possível, mesmo com a permissão obrigando o sequenciamento de visitas ativa

**Resultado esperado**

É esperado que a aplicação respeite o sequenciamento de visitas

**Diagnostico e orientacao**

Seria uma melhoria por causa do seguinte, para usar sequenciamento de visitas, é obrigatório habilitar a permissão "Bloquear venda de clientes fora da rota

E eu observei que eles trabalham com visita fora de rota, então eles não poderiam ligar essa configuração

Eles teriam a seguinte opção no momento

>> Eles teriam que trabalhar com sequenciamento de visitas e visita avulsa bloqueando venda fora de rota, dai só conseguiria vender fora de rota gerando visita avulsa. Porém na visita avulsa não é validada sequência de visitas

O que eles estão querendo é trabalhar com visita fora de rota e com sequenciamento de visitas e essa opção atualmente não existe no maxPedido

# GATE-472 - Política de desconto não se aplica ao cliente

**Contexto**

>>No maxPedido as políticas de desconto 7799 e 13723 da rotina 561 não aparecem para os clientes, ex. 1425 mesmo na base do zero

>>Produto 66060

>>RCA 103(uai.103)

>>Na 316 a política de desconto é aplicada ao cliente

>>Sem restrições de venda (Testei deletando via inspect)

**Passos para reproduzir**

- Baixar a base do zero do RCA 103 ou base
- Iniciar pedido para o cliente 1425
- Clicar no produto 66060
- Mais info> Políticas comerciais

**Resultado apresentado**

>>É exibida mensagem que não existe política vigente para este produto
>>Na 316 como segue prints, a política é incluída automaticamente

**Resultado esperado**

>>As políticas de desconto devem ser validadas para o cliente

**Diagnostico e orientacao**

O problema ocorreu devido a falta de informações que não integraram para a nossa nuvem da tabela MXSGRUPOSCAMPANHAI

Provavelmente era uma falha da versão antiga do banco de dados, porque esse cliente estava na versão 3.1.3.243, sendo que, foi atualizado a última vez em 2023

Então para resolver eu atualizei o banco de dados deles e fiz carga das tabelas MXSGRUPOSCAMPANHAC e MXSGRUPOSCAMPANHAI

Para validar no maxPedido basta realizar a sincronização

# GATE-484 - Relatorio 8012 não é gerado

**Contexto**

O relatório não é gerado no maxGestão, e o unico log que aparece na pasta GERADOR00 > LOGS informa apenas "O relatório não foi gerado

No Winthor o relatório é gerado normalmente

Relatório 8012

**Passos para reproduzir**

- Acessar maxGestão
- Buscar relatório 8012 e gerar com os mesmos filtros

**Resultado apresentado**

Exibido apenas uma faixa vermelha de erro e o log na pasta do gerador informa somente "O relatório não foi gerado." sem mais informações

**Resultado esperado**

Relatório sendo gerado

**Diagnostico e orientacao**

Se tratava de atualização dos relatórios na pasta interna, na máquina onde foi instalado o IIS. Conforme conversamos também, no caso do rel 8012, está tendo um erro de SQL e se quiser mostrar o log desse erro na tela do maxGestão, teria de ser uma melhoria

# GATE-487 - Erro desconto progressivo

**Contexto**

Vendedor relata que ao enviar pedidos que possuam itens que fazem parte de uma campanha de desconto progressivo, os valores de descontos dos itens ficam irreais quando o pedido é enviado do APK
Foi analisado o pedido 22022728, onde foram inseridos itens como o codprod 1914319, que ao ser enviado é verificado que consta um desconto de 66,67%, mas o desconto não existe no valor do item, uma vez que o item possui o preço unitário de tabela de 12,46 com embalagem múltiplo 3, totalizando os 37,38 que são exibidos no aplicativo
A situação ocasiona num pedido que o valor de tabela é de quase 3x o valor original do pedido
A situação ocorre apenas em pedidos que possuem desconto progressivo

Login para teste
destro.22004365

**Passos para reproduzir**

- Entrar na base do vendedor, duplicar o pedido 22022728 inserindo os itens que atendem à campanha progressiva e enviar o pedido

**Resultado apresentado**

Ao enviar, é verificado no JSON do pedido que os descontos estão desordenados e irreais quando comparados com os valores dos itens do pedido, além de que o valor geral do pedido é alterado

**Resultado esperado**

É esperado que os valores de desconto retornados no aplicativo estejam de acordo com os valores dos itens

**Diagnostico e orientacao**

Abaixo vou estar esclarecendo o que de fato está ocorrendo com o pedido NUMPEDERP IN(3408381204)

Primeiramente, o % de 66,67% de desconto está sendo exibido no histórico de itens do pedido devido ao cálculo do preço de tabela e do preço de venda da tabela MXSHISTORICOPEDI

O maxPedido basicamente acessa a MXSHISTORICOPEDI do pedido 3408381204 e pega por exemplo, o preço de tabela do item (1914319) R$37.38 campo PTABELA e a partir dele calcula o desconto que foi dado, comparando com o PVENDA do produto (1914319) R$12.46. Então porque mostra os 66,67%? Porque 66,67% de 37.38 é igual a 12.46. E esses dados o ERP está nos enviando no histórico do endpoint MXSHISTORICOPEDI

Então para resolver essa questão da exibição do desconto no histórico de itens dos pedidos, o integrador do SAP precisa verificar de onde eles estão tirando o preço de tabela e enviando para a gente no campo PTABELA da MXSHISTORICOPEDI. O correto nesse caso seria eles terem enviado por exemplo, o valor de "12.46" porque não teve desconto no pedido digitado manualmente pelo RCA

Existe um segundo cenário que eu acredito que seja um erro pré-existente (ou seja, que não tem relação com o relato acima) que seria o seguinte

Se você pegar o aplicativo antes de enviar o pedido para o ERP e simular
- CODCLI 53436
- CODFILIAL DE04
- PLPAG P018
- CODPROD 1914319
- CODPROD 1953546

E aplicar o desconto progressivo, não vai ser aplicado o desconto progressivo no item e segundo o log do maxPedido diz que tem desconto flex aplicado no item (O que não é verdade)

Então esse cenário que eu levantei de erro pré-existente eu vou mandar para N3, para eles verificarem o que está ocorrendo. Já o relato acima, é o caso de eles verificarem com a integração porque como vimos, nem desconto aplicado teve e a integração deles tá mandando o PTABELA diferente do PVENDA, assim o aplicativo na hora de calcular o desconto fica com a informação errada

Será enviado para N3 ticket

# GATE-489 - Checkin do cliente não subiu para a API

**Contexto**

>>O checkin do RCA 104 não apareceu no maxGestão nem na API de rastro mesmo estando na base Maxtrack do RCA

**Passos para reproduzir**

- Abrir o mapa do maxGestão
- Geolocalização> Painel de auditoria
- Verificar o RCA 104 codusuario 91281

**Resultado apresentado**

>>O cliente 245601 consta como 'apenas CHECKOUT'
>>Não consta na API o checkin
>>Na base MAXTRACK consta tanto o checkin quanto o checkout

**Resultado esperado**

>>Deve aparecer no maxSolucoes tanto o checkin como o checkout do RCA neste cliente

**Diagnostico e orientacao**

Devido a versão que o RCA estava utilizando, ocorreu um problema com a subida do rastro para a API e por este motivo, não estava sendo apresentado no maxGestão. Para resolver eu fiz a normalização dos dados, reenviando somente as informações que estavam presentes na base maxTracking, mas não na API de rastros

Recomenda-se atualizar a versão do maxPedido para a mais recente (observei que já está 3.262.0) e monitorar se resolve definitivamente

Para validar basta ir no maxGestão e filtrar os dados do dia 11/12/2024

# GATE-492 - Produtos Frios sendo cortado no força de vendas

**Contexto**

Produto frios estão sendo cortado no força de vendas. Mesmo depois de ter mudado na rotina PA (padrão) para FR (frios)

**Passos para reproduzir**

- 1 - entrar no maxPedido e tentar fazer um pedido com produtos frios

**Resultado apresentado**

Estão sendo cortado no força de vendas e retornando uma crítica

**Resultado esperado**

Pedido fluir normalmente sem cortes

**Diagnostico e orientacao**

Realizei atualização do ambiente nuvem, extrator
Para simular a situação, seria necessário enviar um pedido utilizando a última versão do maxPedido
Além disso, a gente precisa olhar na 316 deles a simulação do pedido, para ver se os valores batem, valor total e líquido do item no pedido

Nesse sentido, recomendo fazer um teste na versão ponta do maxPedido e também testar um pedido via 316 para ver o valor total do pedido com o cenário
RCA: 91
CODIFILIAL 1
CODPLPAG 9
CODCLI 11156
CODPROD 3604 2 unidades
Pegar a origem de preço do produto na 316 também

Caso o problema continue persistindo nas versões atualizadas do sistema, então reabrir o chamado do Gate com as evidências solicitadas

# GATE-496 - reprocessamento de registros de rastro

**Contexto**

ao analisarmos o cenário da demanda citada, observei que a RCA estava usando a versão 3.248.2, versão essa que é anterior a versão 3.258.3 que contém correções implementadas em calculo de KM total, onde é possível constatar que as inconsistências que o cliente relata abaixo, possam ser geradas devido a essa versão

Possui um erro no registro de KM do setor 54, em que a mesma realizou toda a rota planejada e possui apenas 1,72 no registro de KM total segue prints e base de dados

Nesse cenário, a atualização da versão corrige essas inconsistências de valores anteriores de KM que o cliente relata, ou para se obter os dados retroativos demanda de um reprocessamento no back-end para ser regularizados os registros de KM? segue base maxtracking


**Diagnostico e orientacao**

Realizei a análise do dia 19/11/2024 referente ao trajeto rastreado através do maxPedido da RCA 30784

A análise revelou que os dados apresentados do Km total e Trabalhado estão bastante consistentes

eu disponibilizei um vídeo explicando a análise realizada e também imagens chave com as informações

O fato é que a RCA não se deslocou nesse dia mais que duas ruas, ela ficou andando apenas no entorno do mesmo lugar. Todas as evidências comprovam que a RCA teve um rastreamento consistente no maxPedido e que ela não foi aos clientes que constam como roteirizados

Nesse sentido, o cliente precisa entender que o km total calculado está consistente e que a RCA não deslocou para gerar uma kilometragem maior do que a apresentada no sistema. Sendo assim, não será necessário reprocessamento de dados, e nem seria possível, porque o próprio rastreamento foi consistente e mostra que foram rastreados os 1,72km total

# GATE-498 - Ocultar aba títulos pendentes

**Contexto**

O cliente gostaria de ocultar no cadastro do cliente a aba de títulos pendentes. Gostaria de saber se é possível ocultar

**Passos para reproduzir**

- Acessar o aplicativo
- Ir na tela de clientes
- Clicar em qualquer cliente
- Ir na aba de títulos pendentes
- Logo o cliente quer ocultar essa aba de títulos pendentes
- usuário: pwclub.geovanna

**Resultado apresentado**

Aba de títulos pendentes está aparecendo no aplicativo

**Resultado esperado**

Que oculto a aba de títulos pendentes

**Diagnostico e orientacao**

CLIENTE_EXIBIR_TITULOS - existe o parâmetro e ele oculta a aba de Títulos ao apertar para ver informações do cliente (antes de iniciar o pedido)

Parâmetro deve ser configurado CLIENTE_EXIBIR_TITULOS = Não para ocultar

Depois de alterar lembre de sincronziar para validar no maxPedido

# GATE-500 - Indenização não aparece no Winthor

**Contexto**

Cliente relata que as indenizações não estão sendo exibidas no Winthor. Foi verificado o cenário da indenização NUMINDENIZACAO 80254 (codusur 17 e codcli 219), onde foi retornada a crítica de sucesso no processamento mas ao pesquisar a indenização nas tabelas PCINDC, PCINDCFV e PCINDIFV, a indenização não existe
Foi possível visualizar a indenização em questão apenas na MXSINTEGRACAOINDENIZACAO, onde consta também a crítica de sucesso de processamento do registro

**Passos para reproduzir**

- Entrar no banco local do cliente, verificar as tabelas PCINDC, PCINDCFV, PCINDI o registro NUMINDENIZACAO 80254

**Resultado apresentado**

É verificado que o registro não consta nas tabelas de integração do WINTHOR

**Resultado esperado**

É esperado que o registro seja apresentado corretamente no Winthor

**Diagnostico e orientacao**

Eu analisei o fluxo desde a apk usando o login deles 'sulfrios.mateus' e o processo para gerar a indenização é o seguinte

O maxPedido utilizar o campo PROXNUMPEDFORCA para gerar o numindenizacao que é chave primária da indenização

Então quando o usuário inicia uma indenização no maxPedido, o sistema faz o seguinte

PROXNUMPEDFORCA + 1 = numdenizacao. Exemplo PROXNUMPEDFORCA = 803260, então numdenizacao = 803261

Feito isso o maxPedido salva a indenização e manda para o backend processar

O nosso backend pega o numdenizacao e converte para codindeniz que será gravado lá na PCINDCFV

Campo que será gravado é o PCINDCFV.CODINDENIZ

Te expliquei o fluxo para entendermos o que ocorreu com a indenização (803254). No caso, o numindenizacao é 803254 que foi gerado a partir do pedido 803253

Como expliquei o numindenizacao é convertido para codindeniz. Então o nosso backend tentou gravar lá na tabela

PCINDCFV.CODINDENIZ = 803254

Porém já existia uma indenização com esse código e não dá para reescrever os dados de uma indenização em cima da outra. No caso não é uma falha nossa (Máxima)

Isso seria uma questão de cadastro, onde, na Rotina 517 o PROXNUMPEDFORCA nunca pode ser igual ao de outro RCA e também não pode existir no banco de dados do Winthor, seja na PCINDC, PCINDCFV, PCPEDCFV ou PCPEDC

Se ele já existir em alguma tabela de histórico, então vai ocorrer isso da indenização não ser apresentada corretamente, porque não tem como sobrescrever histórico de um codindeniz que já existia no banco do Winthor

# GATE-505 - Status dos pedidos não atualizam

**Contexto**

Status dos pedidos não atualizam na sync automática mesmo após a correção que foi liberada no dia 02/12

Múltiplos usuários com o mesmo problema

ttslz.cristiellen1377
Base

Como é sync automática, não abri a base no maxPedido para não roubar a sincronização que deveria ir para o RCA

**Passos para reproduzir**

- Verificar por que o status do pedido não atualiza com a sync automática

**Resultado apresentado**

Status parado no envio para o banco nuvem mesmo com pedido ja faturado

**Resultado esperado**

Status atualizando corretamente

**Diagnostico e orientacao**

Foi feito o reenvio dos dados para o RCA referente aos pedidos 267201484 e 267201483 que foram evidenciados na imagem anexada. Esse reenvio foi feito de forma paliativa só para o RCA obter as informações dos pedidos corretamente enquanto investigamos a causa raíz

Não foi possível identificar no Gate a cauza raíz do problema, por este motivo, estou enviando a solicitação para N3 para que seja feita uma investigação ou solução mais aprofundada

# GATE-519 - Vendas clientes vs nivel produto

**Contexto**

Estou com dúvida sobre como analisar o relatório "Acompanhamento Vendas Cliente vs Nível de Produto

Inicialmente, essa demanda foi direcionada ao N3, pois o PO Thiago solicitou que o relatório fosse testado no maxGestão. O relatório já estava ativo no maxPedido, mas não retornava nenhum dado. No entanto, o relatório não aparecia no maxGestão, o que levou à abertura de um ticket no N3 para o atualizador (AT-1728), a fim de habilitar o relatório na GSA

Após a execução do atualizador, o relatório passou a ser exibido no maxGestão, porém, assim como no maxPedido, ele continua sem retornar dados

Gostaria de entender

O que deve ser analisado para identificar a causa do problema?
O que pode estar impedindo os dados de serem exibidos no relatório?

Agradeço a ajuda

**Passos para reproduzir**

- Acessar maxGestão
- Acompanhamento Vendas Cliente vs Nível de Produto
- Filtrar mês inteiro
- Filtrar todos RCAs e equipes
- Filtrar todos departamentos

**Resultado apresentado**

O relatório ao ser consultado apresenta uma mensagem informando que não há informações a serem exibidas

**Resultado esperado**

Entender o relatório

**Diagnostico e orientacao**

Foi analisado o SQL que gera o relatório de Acompanhamento Vendas Cliente Vs Nivel de Produto. Abaixo eu vou colocar o SQL para que você possa entender o ponto que eu identifiquei de divergência

- *Não compartilhe esse SQL com nenhum cliente*

WITH VENDASDETALHADAS AS (
SELECT
CLIENT.CODCLI AS CODIGOCLIENTE
CLIENT.CLIENTE AS RAZAOSOCIAL
CLIENT.ENDERCOB AS ENDERECO
CIDADE.NOMECIDADE AS CIDADE
PEDI.NUMPED AS NUMEROVENDA
PEDI.QT AS QUANTIDADEITEMS
COALESCE(
(SELECT NOME FROM MXSUSUARI WHERE MXSUSUARI.CODUSUR = PEDC.CODUSUR AND ROWNUM = 1)
(SELECT NOME FROM MXSUSUARIOS WHERE MXSUSUARIOS.CODUSUR = PEDC.CODUSUR AND ROWNUM = 1)
) AS NOMEVENDEDOR
PROD.CODPROD AS CODIGOPRODUTO
PROD.CODSEC AS CODIGOSECAO
PROD.CODCATEGORIA AS CODIGOCATEGORIA
PROD.CODMARCA AS CODIGOMARCA
COALESCE(PROD.CODFORNEC, FORNEC.CODFORNEC) AS CODIGOFORNECEDOR
'COD-' || DEP.CODEPTO || ': ' || DEP.DESCRICAO AS DESCRICAO_DEPARTAMENTO
'COD-' || PROD.CODPROD || ': ' || PROD.DESCRICAO AS DESCRICAO_PRODUTO
'COD-' || SEC.CODSEC || ': ' || SEC.DESCRICAO AS DESCRICAO_SECAO
'COD-' || CAT.CODCATEGORIA || ': ' || CAT.CATEGORIA AS DESCRICAO_CATEGORIA
'COD-' || MAR.CODMARCA || ': ' || MAR.MARCA AS DESCRICAO_MARCA
'COD-' || FORN.CODFORNEC || ': ' || FORN.FORNECEDOR AS DESCRICAO_FORNECEDOR
'COD-' || SUBCAT.CODSUBCATEGORIA || ': ' || SUBCAT.SUBCATEGORIA AS DESCRICAO_SUBCATEGORIA
CASE
WHEN (
SELECT
COUNT(*)
FROM
MXSCOMPROMISSOS C
WHERE
C.CODCLI = CLIENT.CODCLI
AND C.CODUSUARIO = USUARIOS.CODUSUARIO
AND TRUNC(SYSDATE) BETWEEN TRUNC(C.DTINICIO) AND TRUNC(C.DTTERMINO)
) > 0
OR (
SELECT
COUNT(*)
FROM
MXSCOMPROMISSOSALT CA
WHERE
CA.CODCLI = CLIENT.CODCLI
AND CA.CODUSUARIO = USUARIOS.CODUSUARIO
AND TRUNC(SYSDATE) BETWEEN TRUNC(CA.DTINICIO) AND TRUNC(CA.DTTERMINO)
) > 0
OR (
SELECT
COUNT(*)
FROM
MXSCOMPROMISSOSMOV CM
WHERE
CM.CODCLI = CLIENT.CODCLI
AND CM.CODUSUARIO = USUARIOS.CODUSUARIO
AND TRUNC(SYSDATE) BETWEEN TRUNC(CM.DTINICIO) AND TRUNC(CM.DTTERMINO)
) > 0 THEN 1
ELSE 0
END AS CLIENTE_ROTEIRO_DO_DIA
FROM
MXSHISTORICOPEDI PEDI
JOIN MXSINTEGRACAOPEDIDO PEDIDO ON
PEDIDO.NUMPEDERP = PEDI.NUMPED
JOIN MXSHISTORICOPEDC PEDC ON
PEDC.NUMPED = PEDI.NUMPED
AND PEDC.NUMPEDRCA = PEDIDO.NUMPED
JOIN MXSUSUARI USU ON
PEDC.CODUSUR = USU.CODUSUR
JOIN MXSUSUARIOS USUARIOS ON
USUARIOS.CODUSUR = USU.CODUSUR
JOIN MXSCLIENT CLIENT ON
CLIENT.CODCLI = PEDC.CODCLI
JOIN MXSCIDADE CIDADE ON
CLIENT.CODCIDADE = CIDADE.CODCIDADE
JOIN MXSPRODUT PROD ON
PEDI.CODPROD = PROD.CODPROD
LEFT JOIN MXSFORNEC FORNEC ON
PROD.CODFORNEC = FORNEC.CODFORNEC
LEFT JOIN MXSSUPERV SUP ON
COALESCE(PEDC.CODSUPERVISOR, USU.CODSUPERVISOR) = SUP.CODSUPERVISOR
LEFT JOIN MXSFILIAL FILIAL ON
PEDC.CODFILIAL = FILIAL.CODIGO
LEFT JOIN MXSMARCA MAR ON
PROD.CODMARCA = MAR.CODMARCA
LEFT JOIN MXSFORNEC FORN ON
PROD.CODFORNEC = FORN.CODFORNEC
LEFT JOIN MXSDEPTO DEP ON
DEP.CODEPTO = PROD.CODEPTO
LEFT JOIN MXSSECAO SEC ON
PROD.CODSEC = SEC.CODSEC
AND SEC.CODEPTO = DEP.CODEPTO
LEFT JOIN MXSCATEGORIA CAT ON
PROD.CODCATEGORIA = CAT.CODCATEGORIA
AND CAT.CODSEC = SEC.CODSEC
LEFT JOIN MXSSUBCATEGORIA SUBCAT ON
SUBCAT.CODSUBCATEGORIA = PROD.CODSUBCATEGORIA
AND SUBCAT.CODCATEGORIA = CAT.CODCATEGORIA
AND SUBCAT.CODSEC = SEC.CODSEC
WHERE
PEDC.CONDVENDA NOT IN (3, 4, 8, 10, 13, 20, 98, 99)
AND PEDC.CODOPERACAO != 2
AND PEDI.CODOPERACAO != 2
AND NVL(PEDC.POSICAO, 'X') != 'C'
AND NVL(PEDI.POSICAO, 'X') != 'C'
AND TRUNC(PEDC.DTABERTURAPEDPALM) BETWEEN TRUNC(TO_DATE('17/12/2024', 'DD/MM/YYYY')) AND TRUNC(TO_DATE('17/12/2024', 'DD/MM/YYYY'))
- \{PARAMETRO_SUPERVISOR}
- \{PARAMETRO_MODO_ANALISE}
- \{PARAMETRO_CLIENTE}
- \{PARAMETRO_FORNECEDOR}
- \{PARAMETRO_DEPARTAMENTO}
- \{PARAMETRO_SECAO}
- \{PARAMETRO_CATEGORIA}
- \{PARAMETRO_SUBCATEGORIA}
- \{PARAMETRO_MARCA}
- \{PARAMETRO_REPRESENTANTES}
- \{PARAMETRO_CODIGOUSUARIORCA}
)
SELECT
CODIGOCLIENTE
RAZAOSOCIAL
ENDERECO
CIDADE
COUNT(DISTINCT NUMEROVENDA) AS QTDE_VENDAS
SUM(QUANTIDADEITEMS) AS QUANTIDADEITEMS
MAX(CLIENTE_ROTEIRO_DO_DIA) AS CLIENTE_ROTEIRO_DO_DIA
LISTAGG(DESCRICAO_PRODUTO || ':' || QUANTIDADEITEMS, ', ') WITHIN GROUP (
ORDER BY
DESCRICAO_PRODUTO) AS DESCRICOESPRODUTOS
LISTAGG(DESCRICAO_SECAO || ':' || QUANTIDADEITEMS, ', ') WITHIN GROUP (
ORDER BY
DESCRICAO_PRODUTO) AS DESCRICOESSECOES
LISTAGG(DESCRICAO_CATEGORIA || ':' || QUANTIDADEITEMS, ', ') WITHIN GROUP (
ORDER BY
DESCRICAO_PRODUTO) AS DESCRICOESCATEGORIAS
LISTAGG(DESCRICAO_MARCA || ':' || QUANTIDADEITEMS, ', ') WITHIN GROUP (
ORDER BY
DESCRICAO_PRODUTO) AS DESCRICOESMARCAS
LISTAGG(DESCRICAO_FORNECEDOR || ':' || QUANTIDADEITEMS, ', ') WITHIN GROUP (
ORDER BY
DESCRICAO_PRODUTO) AS DESCRICOESFORNECEDORES
LISTAGG(DESCRICAO_DEPARTAMENTO || ':' || QUANTIDADEITEMS, ', ') WITHIN GROUP (
ORDER BY
DESCRICAO_PRODUTO) AS DESCRICOESDEPARTAMENTOS
LISTAGG(DESCRICAO_SUBCATEGORIA || ':' || QUANTIDADEITEMS, ', ') WITHIN GROUP (
ORDER BY
DESCRICAO_SUBCATEGORIA) AS DESCRICOESSUBCATEGORIAS
FROM
(
SELECT
DISTINCT
CODIGOCLIENTE
RAZAOSOCIAL
ENDERECO
CIDADE
NUMEROVENDA
QUANTIDADEITEMS
NOMEVENDEDOR
CLIENTE_ROTEIRO_DO_DIA
DESCRICAO_PRODUTO
DESCRICAO_SECAO
DESCRICAO_CATEGORIA
DESCRICAO_MARCA
DESCRICAO_FORNECEDOR
DESCRICAO_DEPARTAMENTO
DESCRICAO_SUBCATEGORIA
FROM
VENDASDETALHADAS
)
GROUP BY
CODIGOCLIENTE
RAZAOSOCIAL
ENDERECO
CIDADE
ORDER BY
CODIGOCLIENTE

Se você abrir o ambiente da GSA e executar esse SQL, nenhum dado será retornado. Isso ocorre porque a integração da GSA nunca nos enviou o campo DTABERTURAPEDPALM no endpoint MXSHISTORICOPEDC. E nesse relatório o filtro essencial que busca por data, faz a busca nesse campo em específico

Se você quiser verificar que eles nunca enviam esse dado temos esse SQL
SELECT * FROM MXSHISTORICOPEDC WHERE DTABERTURAPEDPALM IS NOT NULL

Eu fiz um teste alterando a data de abertura desse pedido
SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED = 1963132
SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP = 1963132

E depois consultei no relatório direto pelo maxGestão e já trouxe a informação

Nesse sentido, para usar esse relatório eles precisarão adequar a integração deles para nos trazer a informação do DTABERTURAPEDPALM solicitada. Qualquer alteração nesse fluxo seria considerada melhoria para a Máxima

Para eles resolverem na Integração, acredito que será algo simples. Essa informação do DTABERTURAPEDPALM é algo que a gente já fornece para o ERP no endpoint StatusPedidos (MXSINTEGRACAOPEDIDO) quando o pedido faz o GET e nos devolve que foi processado no mesmo endpoint

Como lá nós já enviamos esse dado, basta eles extraírem a informação para reenviar no endpoint MXSHISTORICOPEDC juntamente com a última numeração do pedido NUMPED. No caso o que eles chamam de "última crítica" e finalização dos dados no histórico de pedidos

# GATE-521 - Divergencia entre a PCPLPAGCLI e a MXSPLPAGCLI

**Contexto**

>>Poucos planos de pagamento esão aparecendo para os cliente, exemplo 10201

>>Na PCPLPAGCLI existem 4 registros para esse cliente

>>Na MXSPLPAGCLI existem apenas dois registros

>>Esta divergência está fazendo com que os planos de pagamento não apareçam para os RCA's

**Passos para reproduzir**

- Baixar a base do RCA 55 DONACOTA.SAULO, base ou base do zero
- Iniciar pedido no cliente 10201
- Cobrança Bk (COBRANCA BANCARIA)

**Resultado apresentado**

>>Aparecem apenas dois planos de pagamento, 1 e 3
>>Verificando na MXSPLPAGCLI realmente aparecem apenas os registros 1 e 3
>>Porém na PCPLPAGCLI aparecem 4 registros

**Resultado esperado**

>>Tanto na MXSPLPAGCLI quanto no aplicativo deve aparecer os planos de pagamento para o cliente

**Diagnostico e orientacao**

Não passar esses dados para o cliente
Sobre a MXSPLPAGCLI, provavelmente quando a implantação fez a
carga de filial, não habilitou a opção 'Clientes', com isso os dados de vínculo do cliente (PCPLPAGCLI) não desceram para a nuvem

Outra possibilidade é que esse registro nunca foi alterado porque a trigger muda ele. Pode ser q na carga não subiu, por algum motivo: Por exemplo: cliente não fazia parte da regra; plano não fazia parte da regra

Para resolver então eu fiz a carga de dados, como eles são T-Cloud está demorando para descer os registros, mas eu vou fechar o ticket e é só esperar os registros caírem na
SELECT * FROM MXSPLPAGCLI WHERE CODCLI IN(10201)

Se quiser acompanhar via postman o comando é

SELECT TABELA, COUNT(*) FROM PCMXSINTEGRACAO WHERE STATUS = -1 GROUP BY TABELA

A partir daqui pode passar para o cliente se quiser

Para resolver o problema de divergência da PLPAGCLI foi feita normalização de dados. Depois que os registros finalizarem a integração, basta sincronizar o maxPedido

Além desse ponto, tem alguns objetos inválidos lá no banco do cliente no nosso schema porque fizemos uma melhoria recentemente que não teve as tabelas criadas

Então eles precisam rodar esse arquivo
SCRIPT_TCLOUD_MAXIMA.txt

# GATE-526 - Atendimentos não aparecem no painel de auditoria.

**Contexto**

Cliente informou que alguns atendimentos não estão sendo apresentados no painel de auditoria. Como exemplo ela enviou um video feito na segunda feira de justificativa para o 01563801 porem não consta no painel de auditoria

Base de dados e tracking

Video da justificativa feita no dia 16/12/2024

**Passos para reproduzir**

- Verificar painel de auditoria de acordo com o print apresentado

**Resultado apresentado**

Alguns atendimentos não aparecem na listagem

**Resultado esperado**

Todos os atendimentos aparecendo na listagem

**Diagnostico e orientacao**

Será enviado para N3 para verificarem casos semelhantes ao do cliente "01563801" que possui evento e rastro na API porém não está sendo exibindo no painel

A curto prazo, recomendo atualizar a versão do maxPedido porque fomos informados pelo time de apk do maxPedido que houveram correções no fluxo

Ticket em N3

# GATE-530 - Relatório em excel gerando corrompido

**Contexto**

Ao gerar o relatório 8065 em excel, as duas opções de formato geram um arquivo corrompido. Em PDF está sendo gerado normalmente

Arquivos gerados em .xls e .xlsx

**Passos para reproduzir**

- Gerar relatório com os filtros do print apresentado

**Resultado apresentado**

Arquivos sendo gerados corrompidos

**Resultado esperado**

Arquivo sendo gerado corretamente

**Diagnostico e orientacao**

Foi feito mudança no gerador do relatório para corrigir o problema de arquivo corrompido ao gerar o Excel e Excel XLSX

Foi realizado o teste e agora os dados estão sendo gerados corretemente

Diferente do PDF, quando é gerado com cabeçalho e demais informações. No caso o Excel gera só os dados brutos tabelados e está correta a geração

# GATE-534 - Status de pedidos não atualiza

**Contexto**

O cliente está questionando a demora na atualização do status de pedidos bonificados

Durante a análise, foram observados os pedidos 72362596 e 72362597

- O pedido 72362596 já foi atualizado para o status "Faturado
- Entretanto, o pedido 72362597 ainda consta com o status B no banco nuvem
- Ao verificar no banco local, foi identificado que o pedido 72362597 já está registrado como "Faturado

**Passos para reproduzir**

- Acessar maxPedido, importar base de dados, ir na timeline de pedidos, procurar pedido 1947016199 (72362597)

**Resultado apresentado**

>> Pedido 1947016199 ainda consta com status B, porém o mesmo já foi faturado no banco local

**Resultado esperado**

>> Status dos pedidos atualizem conforme for enviado pelo ERP

**Diagnostico e orientacao**

O problema ocorreu porque o pedido foi alterado para origemped "T" na PCPEDC e na PCMXSCONFIGURACOES do banco deles, que é uma configuração para descida de informações para a nossa nuvem via extrator o parâmetro ENVIA_PEDIDOS_TELEMARKETING estava configurado como "N" (desligado)

Então nesse caso não é falha do sistema é uma falta de configuração para descer pedidos da origem "T" que foi uma alteração que ocorreu no Winthor nesse pedido

Para resolver e atualizar corretamente na nuvem, então eu alterei o parâmetro ENVIA_PEDIDOS_TELEMARKETING = 'S' e fiz a normalização dos dados somente desse mês de Dezembro, enviando eles para a nuvem

Dados reenviados da PCPEDC e PCPEDI, depois que a carga acabar, basta os RCAs realizarem o swipe que vai atualizar os status corretamente

# GATE-535 - Lucratividade divergente da 146

**Contexto**

Porcentagem da lucratividade do relatório do maxGestão está divergente da 146

Validado no banco local do cliente que os valores da PCHISTORICPEDC e PEDI estão exatamente iguais ao banco nuvem

Executados os selects no banco local e no banco nuvem e os dois retornaram exatamente os mesmos valores

Busca no maxGestão feita com e sem debitar bonificação, porem o valor segue divergente

**Passos para reproduzir**

- Acessar o maxGestão
- Relatório Venda por Equipe e Análise de Vendas
- Inserir filtros do print apresentado
- Comprar com os valores anexados da rotina 146 do Winthor

**Resultado apresentado**

Valor da %Luc divergente entre o maxGestão e a 146

**Resultado esperado**

Valores iguais

**Diagnostico e orientacao**

O script que a gente executa no portal executivo, para o relatório "Venda por Equipe e Análise de Vendas" por padrão faz a dedução das despesas em cima do valor de venda

Para ficar compatível com a 146, atualmente é necessário sempre marcar a opção "Desconsiderar valor despesas" diretamente na Rotina dentro do Winthor

Outra ponderação: No maxGestão é necessário deduzir as Bonificações porque a 146 faz isso por padrão

Com isso você verá que a lucratividade passa a bater entre maxGestão e Rotina 146 e o valor de venda também

Porém, mesmo fazendo esse procedimento, eu reparei que fica errado a lucratividade de uma das equipes de supervisores. E devido a isso, eu vou encaminhar a demanda para N3

Eu também vou questioná-los sobre essa questão do "Desconsiderar valor despesas", que atualmente, na 146 é parametrizável a dedução, porém no nosso relatório sempre deduz e não tem como alternar isso no maxGestão

# GATE-537 - funcionalidade para gerar destaques em clientes especificos

**Contexto**

ao analisar a demanda citada onde o cliente diz o seguinte
preciso que alguns clientes aparecem com algum destaque de ou cores diferentes... pois são clientes schatech e precisar ter uma atenção maior para venda". Não consegui identificar um formato de configuração que hoje atenda o cliente. O mesmo testou a viabilidade de utilizar cores por classe de venda(com base no campo VIP da MXSCLIENT), porém o cliente já utiliza essas classes internamente no winthor para a sua regra de negócios para indicar diferenças de faturamento

Existe algum outro formato em que o cliente consiga gerar esse destaque de forma que ele possa escolher os clientes com base em seu próprio critério? segue audio curto do cliente explicando sua necessidade

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

Qualquer outra forma que ele quiser diferente disso que cito abaixo, poderia ser considerado para avaliação como Melhoria do sistema

Sobre sinalização que eu encontrei no maxPedido, atualmente teríamos

Por Classe de Venda e coloração: Seria possível mudar a coloração do cliente por classe de venda que é a informação que a gente integra na CLASSEVENDA da MXSCLIENT, algo que o cliente preenche na 302. Informação sai na listagem de clientes

Por definição de cliente "VIP": Tem um campo que integramos também dos clientes que é o campo "VIP" da MXSCLIENT, porém diferente dos outros, esse campo para o RCA visualizar no app, teria que apertar para "Ver informações cadastrais" antes ou depois que já tivesse iniciado o pedido

Por 'Cliente Sinalizado': É um parâmetro por DEFAULT é false SINALIZA_CLIENTES e trabalha em conjunto com QT_DIAS_SINALIZAR_CLIENTE = 60 que é uma informação validada através da MXSCLIENT no campo DTULCOMP. Quando ultrapassa o número de dias do QT_DIAS_SINALIZAR_CLIENTE, gera uma legenda que é um ícone amarelinho na listagem de clientes chamada "cliente sinalizado", você consegue conferir apertando nos "três pontinhos" na listagem. A informação sai na listagem de clientes

Por Faixa de Sortimento: Não são todos os cliente Winthor, que tem a opção de cadastrar o cliente por Faixa de Sortimento. No Winthor em específico eu não sei como ele faria para configurar a integração e cadastro desse campo, porém eu sei que a Nordil tem isso na Rotina 302 deles. O cliente teria que ver dois pontos com a TOTVs, sendo 1° se existe a possibilidade de habilitar e 2° se habilitado, se ele pode cadastrar quantos números quiser ou é restrito à seis faixas (1,2,3,4,5,6). A informação sai na listagem de clientes com cor roxa

Outra possibilidade, se ele curtir a ideia da faixa de sortimento, poderia também entrar em contato com a CS ou através de melhoria solicitar acesso a API da Máxima para integrar diretamente via API no endpoint de clientes no campo faixasortimento. Afinal, por exemplo, Laredo é cliente Winthor mas tem acesso para integrar na API o pré-pedido

# GATE-543 - Ocultar produtos com restrição de venda

**Contexto**

Cliente relata que ao cadastrar restrições na rotina 391, os produtos ainda são apresentados no maxPedido. A restrição cadastrada foi para o departamento 33 e supervisor 2, onde foi verificado que ao filtrar pelo departamento na aba 'Tabela' do maxPedido, os produtos continuam a ser apresentados normalmente

Login para teste
columbia.1322

**Passos para reproduzir**

- Entrar na base do rca, iniciar um pedido em um cliente qualquer e filtrar pelos produtos do departamento 33, conforme restrição 3488

**Resultado apresentado**

É verificado que os produtos são apresentados mesmo havendo a restrição

**Resultado esperado**

É esperado que os produtos sejam ocultados devido a restrição

**Diagnostico e orientacao**

No maxPedido existe o parâmetro 'RESTRINGIR_PRODUTOS_391', que quando setado com valor = 'N' apresenta o produto e informa qual a restrição cadastrada e quando o parâmetro estiver = 'S', não exibe o produto por causa da restrição de venda

# GATE-547 - produtos não aparecem - carga

**Contexto**

Os produtos da filial 1 não estão aparecendo, a base do zero estão aparecendo os 50 produtos normalmente, porém, na base do RCA estão aparecendo apenas 13 (depois de ter feito uma carga interna)

**Passos para reproduzir**

- Produto: 9075, 9076, 7, 9063, 9529, 9067, 5991
- 1 - Ir em produtos, selecionar filial 1 e pesquisar

**Resultado apresentado**

Apenas aparece 13 produtos, não são todos

**Resultado esperado**

Todos os 50 produtos que a base zerada nos mostra

**Diagnostico e orientacao**

Realizei uma normalização de dados para liberar a RCA e permitir que ela consiga sincronizar e receber as informações dos produtos na base dela

Então para resolver pode orientar a RCA a sincronizar

- Não passar ao cliente esse detalhe abaixo
Mesmo assim, vou enviar o ticket para N3 porque nos dados que verifiquei identifiquei um log de erro na sincronização

# GATE-550 - Carga de dados - PCTABTRIB

**Contexto**

Cliente relata que ao inserir o produto 34119, é apresentado um erro de tributação
Ao verificar na MXSTABTRIB, a tributação para o produto não existe, mas ao verificar na PCTABTRIB, a tributação consta para o produto, sendo necessário realizar a carga da tabela em questão

Login para teste

piarara.227

**Passos para reproduzir**

- Entrar na base do vendedor, iniciar um pedido em um cliente qualquer, adicionar o produto 34119

**Resultado apresentado**

Ao inserir, é apresentado erro de tributação

**Resultado esperado**

É esperado que o produto seja carregado normalmente, conforme rotina 316 do Winthor

**Diagnostico e orientacao**

Registro não havia integrado na nuvem provavelmente porque o produto estava inativo, com DTEXCLUSAO preenchido, marcado para ENVIARFORCAVENDAS = N, com REVENDA = N ou com OBS marcado = 'PV'; Dai o cliente mexeu na tributação primeiro e depois ativou o produto, com isso a tributação não sobe

O ideal nesse cenário era o próprio cliente só alterar a tributação novamente, para ela integrar naturalmente. Mas para facilitar a gente fez a carga da PCTABTRIB completa, todas as filiais seguindo os critérios que citei acima, somente produtos ativos e que podem ser vendidos tiveram a tributação integrada

Produto integrado com sucesso
{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSTABTRIB{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODPROD{color} {color:#739eca}IN{color}({color:#c0c0c0}34119{color}){color:#eecc64};{color}

# GATE-552 - Mix do Cliente não aparecec

**Contexto**

Mesmo com as informações no banco, o mix do cliente e a tabela (produtos) estão vazios. Está ocorrendo com apenas um cliente

**Passos para reproduzir**

- Cliente: 2563
- (BASE NOS COMENTÁRIOS)
- 1 - Iniciar um pedido no cliente 2563
- 2 - Ver as informações presentes e tabelas e mix do cliente

**Resultado apresentado**

Mesmo com as informações estarem presentes, tanto no inspect quanto no banco nuvem, os produtos e nem o mix aparecem

**Resultado esperado**

Aparecer todas as devidas informações

**Diagnostico e orientacao**

O cliente 2563 possui um vínculo na PCTABPRCLI, que integrou para a nossa nuvem na MXSTABPRCLI que é o registro da filialnf 3 vinculado na região 363

Na região 363, não tem nenhum produto precificado (MXSTABPR) se você consultar vai retornar nulo
SELECT * FROM MXSTABPR WHERE NUMREGIAO IN(363)

Inclusive eu verifiquei e essa região no banco local (PCREGIAO e PCTABPR) estão nulos também, essa região de preço nem existe

O nosso aplicativo sempre prioriza esse vínculo que é realizado na Rotina 3314 do cliente à filial e à região de venda

Como os dados estão nulos, nenhum produto é exibido nem na tabela e nem no mix do cliente

Para resolver ele deve configurar corretamente a precificação do cliente, dessa forma os itens serão exibidos tanto na tabela quanto no mix do cliente

# GATE-553 - Problema na autorização de pedidos

**Contexto**

O pedido está com um dos itens indo com o valor de "Gerar autorização no gestão: FALSE

e isso causa com que o produto não reflita as edições no campo de comissão, quando o produto vai para o winthor

**Passos para reproduzir**

- BASE DE DADOS ANEXADA
- ACESSO: fcd.teste_ti
- SELECT * FROM MXSUSUARIOS WHERE CODUSUR = 1
- fcd.teste_ti || CODUSUR 1
- Usuario que fez o pedido
- SELECT * FROM mxsautori WHERE NRAUTORIZACAO IN (7621,7622,7623,7620,7619)
- Teste na versão 2.260.4 > Produtos aprovados na data do teste, O PRODUTO 1041 não consta
- Teste na versão 3.251.3 > (7613,7614,7612,7611,7610)
- SELECT * FROM MXSPRODUT WHERE CODPROD IN (1041)
- Produto com erro
- SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP =100509
- Teste na versão 3.251.3 numpederp = 100508

**Resultado apresentado**

Na aprovação do maxGestão PWA é alterada a comissão dos produtos de 4% para 2%

A maioria dos produtos funciona no entanto o produto 1041 não aplica as modificaçoes

Verificado no JSON do pedido que "SolicitandoAutorizacaoPreco": false para o produto 1041, e TRUE para os demais

**Resultado esperado**

Identificar o problema

**Diagnostico e orientacao**

Eu vou encaminhar para N3 para validar se os desenvolvedores podem fazer algo a respeito, mas a princípio, não se trata de um erro. A funcionalidade do maxGestão apenas não explica todos os fatos que podem ocorrer durante a autorização de pedidos com alteração da comissão dos produtos. Abaixo vou explicar como funciona e o caso do cliente

No maxPedido quando você está inserindo itens no pedido, você tem a opção de negociar um preço acima do permitido. Quando isso ocorre aparece a msg no maxPedido, informando ao usuário que o ITEM em específico, será enviado para a aprovação de pedidos do maxGestão. Apesar do pedido todo ir para o maxGestão apenas alguns itens vão configurados com SolicitandoAutorizacaoPreco = true e isso é normal já que está sinalizando para o backend do maxPedido, que apenas alguns itens dentro do pedido sofreram de desconto acima do permitido

Então quando o supervisor ou usuário vai autorizar no maxGestão, o sistema está permitindo ele alterar a comissão de todos os itens, o que define o campo ComissaoAlteradaPorAutorizacao = true para todos os itens. Porém a autorização só será gerada de fato para os itens com SolicitandoAutorizacaoPreco = true

É isso que ocorre no caso do Ruddy, nos pedidos que ele testou, em todos ele sempre adicionou o item 1041 sem negociar um preço acima do permitido. Por esse motivo, mesmo alterando a comissão do item, a autorização não é gerada e por isso a comissão chega no Winthor dele com o valor default de 4%. E é isso que o maxGestão não informa que pode ocorrer com o produto, nem no PWA e nem na versão Web

Isso é regra de negócios do sistema. Só para você imaginar, pense que no maxPedido nunca existiu a opção "enviar para a alteração de comissão", o RCA não consegue simplesmente mandar o pedido para que seja alterada a comissão, essa é uma condição que só pode ser alterada se o produto estiver sob solicitação de alteração de preço, porque é assim que ele sobe para a autorização de pedidos e por isso só gera autorização também dos itens que estão flagados com SolicitandoAutorizacaoPreco = true

Então eu vou enviar para N3 do maxGestão como eu disse, mas pode ocorrer de eles dizerem que se trata de melhoria e não erro

# GATE-557 - Filtro de comissão diferenciada

**Contexto**

Cliente deseja usar o filtro de comissão diferenciada no maxPedido, porem a única informação que temos é um artigo da base de conhecimento do pedido de venda

Esse filtro funciona no maxPedido?

Como é feito o cadastro da comissão diferenciada?

Login de exemplo: mba.2099

**Passos para reproduzir**

- Iniciar pedido para qualquer cliente
- Na aba tabela, marcar o filtro "Comissão diferenciada

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

No maxPedido, basicamente quando os parâmetros OPERADOR_COMISSAO_DIFERENCIADA e PERCENTUAL_COMISSAO_DIFERENCIADA não estão cadastrados, ele tenta buscar os dados da tabela MXSCOMISSAODIFERENCIADA

Essa tabela MXSCOMISSAODIFERENCIADA no maxPedido não é alimentada em nenhum momento porque provavelmente é uma funcionalidade que veio herdada do pedido de vendas. Embora tenhamos esse detalhe, a comissão diferenciada funciona no maxPedido e abaixo vou explicar como atualmente

Você pode preencher o parâmetro OPERADOR_COMISSAO_DIFERENCIADA (Ele é do tipo String "1") utilizando os seguintes operadores e condições

> (maior que): Verifica se o valor é maior que o percentual definido
< (menor que): Verifica se o valor é menor que o percentual definido
>= (maior ou igual a): Verifica se o valor é maior ou igual ao percentual definido
<= (menor ou igual a): Verifica se o valor é menor ou igual ao percentual definido
== (igual a): Verifica se o valor é exatamente igual ao percentual definido
= (igual a): Também verifica se o valor é exatamente igual ao percentual definido (mesma lógica do operador ==)

Exemplos
Operador > e Percentual 10

O sistema verificará se o valor é maior que 10

Operador < e Percentual 5

O sistema verificará se o valor é menor que 5

Operador >= e Percentual 8

O sistema verificará se o valor é maior ou igual a 8

Operador = e Percentual 12

O sistema verificará se o valor é exatamente igual a 12

Essas condições serão aplicadas automaticamente no sistema com base nos parâmetros que você informar

O parâmetro PERCENTUAL_COMISSAO_DIFERENCIADA é do tipo string (1) também e deverá ser preenchido com o valor da comissão que você deseja definir como critério de comparação (por exemplo, "10" ou "15.5")

O percentual definido é comparado com os campos de comissão cadastrados no produto (MXSPRODUT) Rotina 203. São os campos (comissão cadastrada para o produto) SELECT PCOMREP1, PCOMINT1, PCOMEXT1, CODPROD FROM MXSPRODUT WHERE CODPROD IN()

O filtro de comissão diferenciada basicamente faz a leitura dos parâmetros, assim ele entende o critério de comparação e apresenta somente os produtos que se encaixarem no critério de avaliação. Por exemplo, se você configurar o parâmetro OPERADOR_COMISSAO_DIFERENCIADA = ">" e PERCENTUAL_COMISSAO_DIFERENCIADA = 2, então o filtro ao ser ativado, irá mostrar somente produtos com a comissão cadastrada > que 2 cadastro esse que vem da MXSPRODUT

# GATE-563 - Inconsistência de Dados

**Contexto**

Bom da Carlos / Filipe

Preciso de ajuda para identificar um problema que está ocorrendo na SILBAS ao tentar iniciar um pedido para o cliente 2922. Durante o processo, é exibida uma mensagem informando que não foi possível iniciar o pedido devido a uma inconsistência nos dados, e que nenhum plano de pagamento pôde ser carregado para o pedido

Realizei verificações preliminares nas tabelas MXSCLIENT e MXSPLPAGCLI e, em seguida, analisei os vínculos e as tabelas relacionadas aos planos e cobranças (MXSPLPAG e MXSCOB). Contudo, não consegui identificar a causa do problema

**Passos para reproduzir**

- Iniciar APK
- Tentar iniciar pedido no cliente 2922

**Resultado apresentado**

Ao iniciar pedido é exibida uma mensagem informando que não foi possível iniciar o pedido devido a uma inconsistência nos dados, e que nenhum plano de pagamento pôde ser carregado para o pedido

**Resultado esperado**

Iniciar o pedido

**Diagnostico e orientacao**

O plano de pagamento não carrega devido ao vínculo restritivo de plano e cobrança da tabela MXSCOBPLPAG

No caso, o cliente 2922 inicia o pedido com o plano 15 e com a cobrança 2 (MXSCLIENT) e na tabela MXSCOBPLPAG a cobrança 2 só pode ser usada com o plano 11

Para resolver nesse caso eu recomendo que o cliente altere no cadastro do cliente (MXSCLIENT), o plano para o 11. Vou explicar o motivo

Ocorre que, não faz sentido vincular o plano 15 à cobrança 2, porque a cobrança é Dinheiro, que é utilizada para vendas A VISTA. Como no caso do plano 11 TIPOVENDA (VV)

O plano 15 é do tipo venda a prazo, isso quem dita é o campo TIPOVENDA e também a descrição né, que é BOLETO 15 DIAS, ou seja, geralmente venda a prazo se utiliza com cobrança BOLETO mesmo

Outra observação, a cobrança 15 já está vinculada na cobrança 4, se o RCA selecionar uma cobrança do tipo boleto (4), o plano 15 será exibido

Consultas utilizadas

SELECT CODCOB, CODCLI, CODPLPAG FROM MXSCLIENT WHERE CODCLI IN(2922)
SELECT * FROM MXSPLPAGCLI WHERE CODCLI IN(2922)
SELECT * FROM MXSCOBCLI WHERE CODCLI IN(2922)
SELECT * FROM MXSCOBPLPAG WHERE CODCOB IN('2')

SELECT * FROM MXSPLPAG WHERE CODPLPAG IN(15,11);--TIPOVENDA VP VENDA A PRAZO
SELECT * FROM MXSCOB WHERE CODCOB IN('2')

# GATE-565 - Layout de impressão, drivers não funcionam

**Contexto**

Impressora Portátil Térmica Leopardo XR

ESPECIFICAÇÕES IMPRESSÃO
Método de impressão: Térmica Direta
Tipo de Mídia: Papel térmico, Papel térmico personalizado com Blackma
Largura do papel: 80 mm
Largura de impressão: 72 mm
Resolução: 8 pontos/mm (203 dpi)
Pontos/Linha: 576 pontos
Velocidade de impressão: Até 90 mm/seg
Linguagem de Programação: ESC/POS
Códigos de Barras: UPC-A, EAN13, EAN8, CODE 39, ITF, CODABAR, CODE39, CODE128 E QRCODE
Vida Ú_l Cabeça de Impressão: 50 KM

ESPECIFICAÇÕES FÍSICAS
Grau de Proteção: IP42 sem capa
Resistência: Queda 1,20 metros / Opcional: Capa com resistência até 1,50 metros
Dimensão Externa: 125 X 100 X 50 mm
Peso: 360 gramas (com bateria)
Diâmetro da Bobina: Até 50 mm
Interface: USB / Bluetooth
Bateria: Bateria de Lí_o 1.800 mAh 7.4 V (*)
Sistemas: Android, Windows
Tempo de carga completa: 3-4 horas
ESPECIFICAÇÕES DO AMBIENTE
Temperatura de operação: -10°C 50°C
Umidade de operação: 20% 85% RH
Temperatura de armazenam/o: -20°C 70°C
Umidade de armazenamento: 5% 95% RH

OUTRAS ESPECIFICAÇÕES
Garantia: 18 (dezoito) Meses
Acessórios
Fonte de Alimentação 110/220 V
Cabo USB
Carregador Veicular 12V
Bobina de Papel e Manual

**Passos para reproduzir**

- não está trazendo informações de pedidos
- Ao solicitar para trocar o driver o cliente informou que testou em todos e nenhum imprimiu corretamente
- O cliente utilizava a impressora " A7 ", e mudou para a "Leopardo XR" que tem suas especificaçoes citadas na sessão de DESCRIÇÃO, deste chamado

**Resultado apresentado**

Alguns dados não são exibidos em tickets impressos recentemente, como a sessão de DADOS DOS PRODUTOS ()

**Resultado esperado**

Identificar o problema

**Diagnostico e orientacao**

Verifiquei os dados que foram anexados e precisamos te devolver o ticket, para que o cliente nos ajude com mais algumas informações importantes para a análise

>> Precisamos saber o método de impressão que foi utilizado, por exemplo, se foi impressão de nota fiscal, se foi nota de contigência, se foi boleto, etc

>> Precisamos do login do RCA, para que a gente possa simular também o problema no desenvolvimento usando uma impressora com o mesmo modelo

>> Precisamos da base do RCA, que constam os dados dos pedidos na timeline onde foi feita a tentativa de geração do arquivo via mini impressora

>> Precisamos saber dados sobre o(s) pedido(s) (NUMPED e NUMPEDRCA) que foram feitas as tentativas de impressão dos dados, para que possamos conferir se os dados estão sendo enviados via integração corretamente

# GATE-567 - Campo de endereço de entrega não puxa no relatório

**Contexto**

Ao gerar o espelho do pedido as informações de endereço de entrega não são apresentadas, mesmo com o endereço constando na base do RCA e no JSON do pedido

**Passos para reproduzir**

- Importar base do RCA no maxPedido
- Gerar espelho do pedido

**Resultado apresentado**

No espelho do pedido não são apresentadas as informações de endereço de entrega

**Resultado esperado**

Espelho do pedido apresentando informações de endereço de entrega

**Diagnostico e orientacao**

Vou encaminhar para N3 porque não foi possível identificar o motivo do campo não estar gerando no relatório customizado para pedidos que possuem histórico já definido

Em pedidos novos, seja na versão antiga ou na nova, as informações são apresentadas normalmente

Na verdade o cliente está usando um relatório customizado 341 Padrão - Villa Camarão

No caso, atualmente está configurado como \{EnderecoEntrega.endereco}, que traz só a informação da rua quando selecionado no pedido na aba TOTAIS

Sobre a data de entrega, na aba TOTAIS do maxPedido se o RCA digitar uma "data prevista de faturamento", então essa informação sai no relatório que ele configurou customizado como se fosse "A data de entrega do pedido

# GATE-570 - Pedido não aparece na autorização

**Contexto**

Cliente relata que o pedido ID_PEDIDO 185559 (NUMPED 4817) não é apresentado no maxGestão para autorização. Foi verificado na MXSINTEGRACAOPEDIDO o pedido consta com status 8, e ao verificar na MXSINTEGRACAOPEDIDO_LOGST, é verificado que o pedido não teve outros status (0, 2, 6, etc)
Foi verificado também os vinculos do usuário que realizou o pedido com a equipe do supervisor 68

**Passos para reproduzir**

- Entrar no maxGestão do cliente, usuáro SYSMAX, consultar o pedido 4817

**Resultado apresentado**

Ao consultar, é verificado que o mesmo não é apresentado para a autorização, mesmo que conste com status 8 na integração

**Resultado esperado**

É esperado que o pedido conste corretamente para a autorização

**Diagnostico e orientacao**

Leia com atenção, coloquei dados internos nossos sobre a Máxima

Nunca vi isso antes, não sei como pode ter ocorrido, mas basicamente o pedido está com status 8, sendo que não passou por 0 e nem 2, e nele CODUSUARIO está = 277 (e não existe nenhum)

CODPLPAG também está nulo no pedido

CODSUPERVISOR está nulo também

CODIFILIAL nulo

E por isso o pedido não é exibido para aprovação. Nesse caso, eu penso em duas possibilidades, ou a integração do ERP deles falhou muito e gravou um registro na nuvem direto com status 8 ou o nossos aplicativo (acho bem difícil) gerou um registro todo errado com codusuario errado e demais informações inconsistentes. Bem difícil o app ter feito isso porque o codusuario nem abre o maxPedido se não estiver correto

Enfim, algum sistema falhou de forma bem grave que gerou esse pedido com informações inconsistentes

Se esse pedido tiver sido feito no maxPedido, então vai estar no sistema do RCA "000277" que seria o RCA GUARAVES.Jose.Rinaldo Nome JOSE RINALDO DA SILVA ALVES

Nesse caso eu recomendo orientar o RCA a duplicar o pedido e enviar novamente, conferindo os itens e reinserindo se necessário, eu coloquei um resumo do que era o pedido de acordo com o JSON

Eu oriento a fazermos isso porque estou achando que foi a integração deles que simplesmente colocou uma informação na nossa nuvem. E para contestar isso, caso o RCA tenha o pedido no aparelho ele vai conseguir nos mandar evidenciando com a base e vai conseguir refazer o pedido. Se ele não achar o pedido, então quer dizer que pode ter sido inconsistência da integração

- *Pedir a base do RCA para que possamos entender se foi uma falha nossa do maxPedido na hora de gerar o pedido para autorização e podermos realizar demais testes usando versão ponta

Obs: Provavelmente eles não vão ter a base e então vamos jogar a responsabilidade para a integração deles de ter gravado um pedido diretamente na nossa API com status 8 e dados inconsistentes

# GATE-573 - Ajuste de conta corrente incorreto.

**Contexto**

>>Na MXSHISTORICOPEDI do pedido 517261 de exemplo (Existem outros) os valores do PTABELA e PVENDA são iguais, porém mesmo assim na ERP_MXSLOGRCA e no sistema foi adicionado o valor de 220, sendo 2,20 para cada unidade do produto 176

Selects utilizados

SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED = 517261

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPED = 517261 ORDER BY DATA DESC

**Passos para reproduzir**

- Verificar a MXSHISTORICOPEDI e a ERP_MXSLOGRCA com os selects enviados
- Verificar relatório da central de configurações enviado ou retirar um novo

**Resultado apresentado**

>>Mesmo não havendo nenhum desconto ou acrescimo nos pedidos, o sistema está fazendo alterações no conta corrente do RCA

**Resultado esperado**

>>Como não existe acrescimo ou desconto, o conta corrente deve permanecer com o mesmo valor

**Diagnostico e orientacao**

O sistema utiliza o parâmetro USAR_CCRCA_MAXIMA = S na tabela MXSPARAMETRO, de modo que a movimentação é realizada na nossa PKG, baseada nas informações do sistema

Contexto do Pedido
Pedido
NUMPEDRCA: 137
NUMPED: 517261
Item: 176
Preço Base: 13,80
Informações no JSON e Histórico
No JSON enviado, o campo "PrecoVendaInformado" tinha o valor de 13,80
No JSON enviado, o preço base do campo "PrecoBase": 13.8" também confirmava esse preço de base
Nesse dia, também havia uma política de descontos que creditava sob a política e era aplicada ao preço de tabela do produto 176. A política com aplicação automática "DESCONTOROMA176" incidia 13.75% de desconto no preço de 16 reais, resultando nos 13.80. Por esse motivo houve movimentação de conta corrente

Entretanto, segundo o ERP deles e o preço de tabela, o preço de venda registrado no histórico do pedido (tabela MXSHISTORICOPEDC) foi de 16,00

Datas relevantes
Pedido aberto: 2024-12-30 15:49:29.000
Última atualização do histórico: 2024-12-31 03:04:18.000

Conclusão
Se confirmado que o preço correto do item na época era R$13,80, o problema provavelmente se originou na integração, que registrou erroneamente o preço de venda como R$16,00 no histórico. Isso requer análise do cliente com a integração do ERP dele para alinhar os sistemas e evitar futuros problemas com movimentação de conta corrente. Se não era para ter movimentado, então o ERP deles deveria ter enviado o preço de venda no endpoint MXSHISTORICOPEDC = 13.80. Se era para ter movimentado então a justificativa já está citada acima e o ERP mandou o preço corretamente

# GATE-575 - Permissão não sobe via sincronização

**Contexto**

Permissão ja foi marcada e o pedido está iniciando normalmente na base do zero, porem na base do RCA não atualizam mesmo sincronizando e não é possivel iniciar o pedido

**Passos para reproduzir**

- Logar no maxPedido
- Importar base do RCA
- Iniciar pedido para cliente 2401

**Resultado apresentado**

Pedido não inicia devido a falta de permissão de acesso a cobrança

**Resultado esperado**

Permissão recebida via sincronização

**Diagnostico e orientacao**

Foram verificados os registros da base da RCA, que geram o problema de iniciar o pedido no cliente 2401

- *Não passar ao cliente:*
Durante a análise eu constatei o seguinte

Na verdade a RCA tem acesso a permissão da cobrança BK. O acesso se dá na tabela da apk
SELECT * FROM mxsacessodados

O que causa o problema é que a RCA não conseguiu sincronizar com sucesso a cobrança 'BK' na tabela MXSCOB

Eu validei os registros de logs que tínhamos disponíveis, porém o dado é de 2024-11-19 12:18:03.000
SELECT * FROM MXSCOB WHERE CODCOB IN('BK')

Então não tem mais informações que levariam a descobrir se ocorreu algum erro de base do maxPEdido, pode ter sido erro de coluna no maxPedido, pode ter sido falha de sincronização, etc

Pode passar para a cliente
Pra resolver eu fiz uma normalização de dados, então quando a RCA sincronizar ela vai receber essa informação da cobrança e vai resolver a situação

Recomendo você atualizar a versão dela e ambiente porque saiu uma correção que, quando ocorre erro de sincronismo, o nosso backend reenvia a informação que falhou no processo de download

# GATE-579 - Ajuda com Crítica da Integradora ao Enviar Pedido TV8

**Contexto**

Carlos/Filipe

Preciso de auxílio para identificar a causa da crítica apresentada pela integradora ao enviarmos um pedido TV8 (Venda Assistida)

Realizei a atualização completa do ambiente antes de testar, mas obtive o mesmo resultado observado pelo cliente. A integradora retorna uma mensagem referente ao "buffer de string de caracteres", indicando que ele é "pequeno demais, numérico ou de valor

**Passos para reproduzir**

- Iniciar pedido no cliente 1 - CONSUMIDOR FINAL
- Tipo de venda entrega futura
- Filial 51
- Marcar a bolinha de "venda assistida
- Plan. Pg 20
- Cobrança Visa Débito
- Adicionar qualquer produto no pedido
- Quando aparecer o pop up da venda assistida, selecionar RI - Entrega Imediata
- Salvar e enviar o pedido
- Observar a crítica

**Resultado apresentado**

Quando o pedido é processado a integradora retorna a crítica

Pedido TV8 gerado : 286472 na posicao : L
- 6502-ORA-06502: PL/SQL: erro: buffer de string
de caracteres pequeno demais numerico ou de
valor-ORA-06512: em "LDF.INTEGRADORA_COMPLE
line 2890
ORA-06512: em "LDF.INTEGRADORA", line 27821

**Resultado esperado**

Entender o que está causando isso e se podemos resolver daqui sem acionar a TOTVS

**Diagnostico e orientacao**

Realizei a conexão com o banco do cliente para realizar a verificação do problema e abaixou vou estar colocando os detalhes

Inicialmente, gostaria de esclarecer que o problema não é causado pela Máxima e a resolução também não será feita por nossas equipes

O problema ocorre na package "INTEGRADORA_COMPLE" que é do SCHEMA principal da "LDF" do banco do ERP (WINTHOR). Segundo os dados que rastreamos, na hora de processar o pedido na PCPEDCFV, essa pkg utiliza a variável VSCODFILIAL que está definida como VARCHAR2(1); onde justamente está sendo acusado o erro que foi retornado na própria crítica da Integradora do Winthor. linha 2890

Isso ocorre porque o pedido foi enviado na Filial (51), ou seja, se a variável só aceita VARCHAR2(1), vai estourar o campo e dar problema na hora de processar a informação

eu disponibilizei prints seguindo a orientação do próprio banco do Winthor para localizar o problema na PKG do banco

Então conforme evidências e expliquei inicialmente, nós não prestamos consultoria e nem manutenção em recursos do Banco do Winthor que não são nossos. No caso a "LDF.INTEGRADORA_COMPLE" não é uma funcionalidade desenvolvida pela Máxima e portanto não prestamos a manutenção nela

O cliente deve validar o criador dessa PKG, não sabemos se é da TOTVS ou se é algo interno e solicitar a manutenção ao criador

# GATE-585 - Mesmo com todas as informações corretas a API de cancelamento não funciona

**Contexto**

>>Mesmo com todas as informações corretas a API de cancelamento do cliente Tcloud não funciona

>>IP enviado pelo cliente (Testei com e sem a porta)

>Usuário: JOAO

>Senha: 0497 Criptografada: (8RLCic66YyfVSKrrN66faQ==)

Usuário maxPedido: BRITOTARGI.rca

**Passos para reproduzir**

- Acessar o maxPedido em base do zero ou na base
- Iniciar um pedido para um cliente qualquer ex.1124
- Incluir algum produto ex. 57
- Salvar e enviar
- Ir na timeline de pedidos
- Segurar sobre o pedido e solicitar cancelamento

**Resultado apresentado**

>>No maxPedido o pedido aparece como cancelado, porém ao verificar na MXSHISTORICOPEDC o pedido ainda consta com posição = L
>>Na MXSINTEGRACAOPEDIDO o pedido aparece como CANCELADO = S

**Resultado esperado**

>>Tanto na MXSHISTORICOPEDC quanto no aparelho do RCA, os pedidos devem ser cancelados pela API

**Diagnostico e orientacao**

O problema era causado pela configuração do IP no extrator (Jenkins) do cliente. Foi necessário colocar o IP " dessa forma, sem a porta, porque no Workspace ele só acessa o WTA do cliente se não tiver a porta. É comum isso em alguns casos (quando o cliente não tem acesso externo liberado para a porta do WTA)

Feito isso eu reiniciei o extrator e atualizei a versão de banco. Também executei o teste no maxPedido e cancelou com sucesso via API de cancelamento

O parâmetro UTLIZA_API_CANCEL_WINTHOR para testar eu habilitei ele para todos os RCAs = S

Já o parâmetro PERMITE_CANCELAR_PEDIDO_ERP eu deixei para Geral NULL, nesse fluxo que ele vai trabalhar não precisa desse parâmetro

Para validar o cliente só precisa sincronizar os RCAs e liberar as permisões de edição ou cancelamento de pedidos na central. Com isso já vão conseguir cancelar pedidos com posição diferente de "M" "C" e "F

# GATE-588 - Pedidos com origem telemarketing não estão sendo enviados para o banco nuvem

**Contexto**

Os pedidos de origem telemarketing não estão sendo enviados para a MXSHISTORICOPEDC e MXSHISTORICOPEDI, foi habilitado na PCMXSCONFIGURACOES o parâmetro ENVIA_PEDIDOS_TELEMARKETING e atualizado todo o ambiente do cliente e mesmo assim os pedidos com ORIGEMPED = T não vieram para o banco nuvem

**Passos para reproduzir**

- Acessar o banco do cliente
- Realizar uma consulta na tabela MXSHISTORICOPEDC e procurar pelo pedido 513037598
- E assim ele não consta no banco nuvem
- O mesmo tem ORIGEMPED = T e consta no banco local

**Resultado apresentado**

Pedidos do tipo telemarketing não estão sendo enviados para o banco nuvem

**Resultado esperado**

Que os pedidos do tipo telemarketing sejam enviados para nosso banco nuvem

**Diagnostico e orientacao**

As informações dos pedidos retroativos não sobem somente ao alterar o parâmetro ENVIA_PEDIDOS_TELEMARKETING para = S na PCMXSCONFIGURACOES

Ao ativar ele, somente pedidos feitos após a ativação vão subir via Extrator

Então para resovler esse caso é somente fazendo carga dos retroativos

Então foi feita carga da PCPEDC e PCPEDI referentes às filiais 1 e 3 e do mês passado inteiro e mês atual

# GATE-595 - clientes em especifico utilizarem apenas uma determinada filial

**Contexto**

ao analisar a demanda citada, observei a seguinte situação: o cliente vem enfrentando um cenário em que pedidos de determinados clientes estão sendo gerados de forma inadequada para uma de suas filiais. No cenário de exemplo, o cliente reporta que o cliente 5523 não deveria ter pedidos negociados através da filial 1

!image-2025-01-07-17-59-38-257.png!

porém existem pedidos que estão saindo pela filial citada

!image-2025-01-07-18-01-29-640.png!

Ao analisar o cenário no aplicativo, observei que o app disponibiliza as duas filiais para o RCA selecionar, o que permite com que o pedido possa ser negociado em ambas as filiais

!image-2025-01-07-18-02-42-010.png!

Nesse cenário, qual a configuração que o cliente pode estar realizando para que restrinja no ato da negociação a nível de cliente e filial, para impedir que esses clientes consigam negociar pedidos na filial 1, mas sem remoção de permissões ou cadastrando as restrições para a venda via 521? quais as tabelas que seriam utilizadas para efetuar a configuração desejada pelo cliente?

cliente: 5223

**Passos para reproduzir**

- efetuar o login e analise conforme a descrição

**Resultado apresentado**

pedidos sendo gerados em filiais que o cliente não espera que sejam realizadas

**Resultado esperado**

é esperado que o aplicativo não permita a negociação do pedido de determinados clientes para determinadas regiões

**Diagnostico e orientacao**

Como o cliente é usuário do ERP Winthor, então teríamos duas opções que eu me recordo referente a restringir o acesso de filial durante a negociação no cliente. Seriam essas

Rotina 3314: Grava na PCTABPRCLI que integramos na MXSTABPRCLI e a regra é que o cliente só vai ter acesso a filial que está vinculada ao código dele e também a região de preço determinada nessa rotina

Rotina 391: É possível cadastrar também uma restrição por cliente, onde o cliente não pode acessar determinada filial. A que não possuir restrição, ele conseguirá acessar normalmente. Grava na PCRESTRICAOVENDA e sobe para a MXSRESTRICAOVENDA

Ambas regras devem funcionar no maxPedido

# GATE-597 - Falha na geocodificação de clientes no Roteirizador

**Contexto**

ao realizar o fluxo de configuração da geolocalização, está ocorrendo o seguinte falha conforme abaixo

**Passos para reproduzir**

- acessar o roteirizador do cliente e buscar pela RCA NATALIA ALVES PEREIRA
- clicar em gerenciar coordenadas
- buscar pelo cliente 323943
- clicar em ações e observar o resultado

**Resultado apresentado**

está ocorrendo falha conforme o erro apresentado

**Resultado esperado**

é esperado que não ocorra a exception e que possa gravar a geolocalização do cliente normalmente

**Diagnostico e orientacao**

Existiam dois registros ID 21052 e 21053 na tabela MXMP_LOCALIZACAO_CLIENTE_VENDA, com isso, na hora de realizar a busca das coordenadas do cliente, ocorria uma exceção no código

O Roteirizador já conta na versão mais atualizada, com mecanismos para impedir que a localização do cliente seja gravada duas vezes na mesma tabela. Então provavelmente esse registro estava duplicado devido a uma versão antiga do Roteirizador que foi utilizada pela cliente e ainda possuía a falha

Também foi verificado que o único registro duplicado era desse cliente 323943, nenhum outro registro estava duplicado que poderia causar o mesmo problema

Para resolver foi feita normalização dos registros, deletando a duplicidade da tabela no banco de dados ORACLE

Foi feito o teste no Roteirizador de vendedores no cenário informado e o erro não ocorreu novamente

# GATE-598 - RCA não retorna na busca da jornada de trabalho.

**Contexto**

Ao tentar buscar um RCA para vincular a jornada de trabalho o RCA não é listado na busca do maxGestão

Porem na busca do maxPedido ele é retornado e é possivel vincular o RCA a jornada

Se o vinculo for realizado pelo maxPedido o RCA é apresentado na listagem de usuários vinculados do maxGestão normalmente e é possivel até remover ele da jornada pelo maxGestão, porem nunca é exibido na listagem de disponiveis para vinculo

Testado no usuários sysmax e usuário do cliente, ambos com todas as permissões marcadas

68361 - DOUGLAS RODIGUES GARCIA - 947

**Passos para reproduzir**

- Acessar maxGestão
- Jornada de trabalho, Cadastro de Jornada
- Editar jornada "JORNADA PADRÂO
- Buscar RCA na listagem de usuários disponiveis para vinculo

**Resultado apresentado**

RCA não aparece na listagem de usuários do maxGestão, porem aparece no maxPedido

**Resultado esperado**

RCA sendo apresentado na listagem de usuários disponiveis para vinculo do maxGestão

**Diagnostico e orientacao**

Será encaminhado para N3

Eu identifiquei o seguinte comportamento errado
Se o usuário esperar a lista toda carregar e diretamente pesquisar o número correto desejado, seja 947 ou 68361, então a busca retorna o RCA. Porém se ele digitar errado ou o código de outro RCA primeiro: 570 (por exemplo) e depois tentar digitar 947, a busca não reinicia, por isso não retorna o usuário desejado
Sobre o campo (Nome), ele busca pelo nome do login do usuário não pelo nome do usuário, se você colocar "DOUGLAS" nada retorna mesmo e isso está correto, no caso ele busca correto só se você esperar a lista carregar e depois escrever "HIMALAIA.947

# GATE-601 - Valores do resumo de venda não batem com o ERP

**Contexto**

Cliente - VENDA DO VENDEDOR CLAUDIO NÃO ESTÁ BATENDO O VALOR TOTAL DO MÊS DE DEZEMBRO COM O VALOR TOTAL NO MEU ERP, VERIFICA POR FAVOR
Verifiquei nas tabelas historicopedc e pedi e os valores não batem

**Passos para reproduzir**

- Login - meta.rca
- Acessa resumo de venda, ir pesquisar vendas do mes de dezembro

**Resultado apresentado**

Valor não esta batendo com o valor do ERP

**Resultado esperado**

Que os valores batem com o ERP

**Diagnostico e orientacao**

Primeiramente é importante citar que o cálculo realizado no resumo de vendas da Máxima utiliza informações que nós recebemos nos endpoints, ou seja, informações provenientes da integração com o ERP

No caso deles, a venda faturada está sendo calculada por meio do uso das informações nos endpoints: MXSHISTORICOPEDC(HistoricosPedidosCapas), MXSHISTORICOPEDI(HistoricosPedidosItens), MXSUSUARI(Usuaris) e MXSPRODUT(Produtos)

Então para resolver o problema deles, eles precisam focar em "concertar" as informações que eles nos enviam em alguns desses endpoints que citei acima

- Resumo dos parametros
- CODUSUR = 7348
- DATAINICIO = '01/01/2025'
- DATAINICIO = '31/01/2025'
- FILIAIS = '1','5','7'
- DEDUZDEVOL_VENDA_TRANSMITIDA = N
- DEDUZOUTRASDESP_VENDA_TRANSMITIDA = N
- IGNORARTV5TV11APURACAOMETAS = N
- CRITERIOVENDAFDEDUZIRDEV = N
- CRITERIOVENDALUCROLIQ = N
- REDUZIRST_DADOS_RELATORIO = N
- REDUZIRIPI_DADOS_RELATORIO = N
- CRITERIOVENDAFCONSIDERADEVAVULSA = N
- PERC_COMISSAO_RATEADA = 0
- VALIDAR_APURACAO_NF = N
- CRITERIOVENDA = F
- APURACAO_RESUMO_DTFAT = N

- Consulta

SELECT
MXSHISTORICOPEDC.CODUSUR
SUM((MXSHISTORICOPEDI.QT * MXSHISTORICOPEDI.PVENDA)
- (DECODE (OBTER_PARAMETRO('REDUZIRST_DADOS_RELATORIO', NULL, 'N'),'S', MXSHISTORICOPEDI.QT * NVL(MXSHISTORICOPEDI.ST,0),0))
- (DECODE (OBTER_PARAMETRO('REDUZIRIPI_DADOS_RELATORIO', NULL, 'N'), 'S', NVL (MXSHISTORICOPEDI.QT * NVL(MXSHISTORICOPEDI.VLIPI,0), 0), 0))) VLVENDAFATURADA
FROM
MXSHISTORICOPEDC
MXSHISTORICOPEDI
MXSUSUARI
MXSPRODUT
WHERE
MXSHISTORICOPEDI.NUMPED = MXSHISTORICOPEDC.NUMPED
AND MXSHISTORICOPEDC.CODUSUR = MXSUSUARI.CODUSUR
AND MXSHISTORICOPEDI.CODPROD = MXSPRODUT.CODPROD
AND MXSHISTORICOPEDC.DTCANCEL IS NULL
AND DECODE(OBTER_PARAMETRO('APURACAO_RESUMO_DTFAT', NULL, 'N'), 'S', TRUNC(NVL(MXSHISTORICOPEDC.DTFAT, MXSHISTORICOPEDC.DATA)), MXSHISTORICOPEDC.DATA) BETWEEN TRUNC(TO_DATE('01/12/2024', 'DD/MM/YYYY')) AND TRUNC(TO_DATE('31/12/2024', 'DD/MM/YYYY'))
AND MXSHISTORICOPEDC.CODFILIAL IN ('1', '5', '7')
AND MXSHISTORICOPEDC.CODUSUR = 7348
AND MXSHISTORICOPEDC.POSICAO = 'F'
AND NVL(MXSHISTORICOPEDI.POSICAO, MXSHISTORICOPEDC.POSICAO) = 'F'
AND MXSHISTORICOPEDC.CODOPERACAO != 2
AND MXSHISTORICOPEDI.CODOPERACAO != 2
AND MXSUSUARI.CODOPERACAO != 2
AND (OBTER_PARAMETRO('IGNORARTV5TV11APURACAOMETAS'
NULL
'N') = 'N'
OR OBTER_PARAMETRO('IGNORARTV5TV11APURACAOMETAS'
NULL
'N') = 'S'
AND MXSHISTORICOPEDC.CONDVENDA NOT IN (5, 11))
AND OBTER_PARAMETRO('VALIDAR_APURACAO_NF'
NULL
'N') = 'N'
GROUP BY
MXSHISTORICOPEDC.CODUSUR

- A partir daqui pode passar se quiser, cuidado com as palavras que vai usar com o cliente

eu também coloquei o agrupamento por pedido, dos itens e das quantidades vendidas dentro do período estipulado do RCA 7348. Se você realizar a soma da venda faturada agrupada no Excel vai resultar também no valor total faturado do script

Então analisando essas informações a gente conclui que não há falhas no cálculo que realizamos. Ele simplesmente é um cálculo que apura venda faturada e é utilizado por vários clientes nossos, ele é bastante consistente, possui uma regra de negócios própria e não precisa de correções

Então, por que o número fica errado ao comparar com o ERP?
Essa é uma pergunta difícil de responder porque depende de vários fatores a serem analisados
- É importante saber se o ERP está deduzindo devoluções e bonificações
- É importante saber se o valor de venda faturada é com ou sem impostos
- É importante saber se, eles fazem a apuração por DATA de lançamento do pedido ou por DTFAT (Data de Faturamento do pedido)
- Eles precisam revisar a planilha no quesito dos preços que foram enviados dos itens e quantidades por pedido, para que em comparação com o ERP, saibam se estão nos enviando os mesmos dados que eles tem lá no ERP via API nos nossos endpoints

Quem deve realizar essa análise?
No momento a Máxima esgotou as possibilidades de análise das informações em nosso ambiente, nós não temos o dever e nem temos acesso a informações confidenciais do ERP para comparar com os nossos endpoints

Nesse caso, o correto é que o Integrador ou algum responsável capacitado, extraia informações do ERP para comparar com os dados que disponibilizamos dos nossos endpoints em formato Excel. Dessa forma, será possível indentificar a causa da divergência, para que então a Integração do ERP possa realizar a correção no envio das informações

No final, quando os dados forem corretamente enviados para a Máxima, a apuração do Resumo de Vendas baterá com a do ERP, porém entenda, que isso não depende da Máxima, isso depende da integração do seu ERP nos enviar os dados corretos referentes às vendas realizadas por item, pedido, RCA e data

# GATE-602 - Divergência entre a ERP_MXSPREST e a PCPREST

**Contexto**

>>No Winthor a duplicata 669805 foi baixada, porém no banco nuvem essa duplicata ainda permanece sem DTPAG e VPAGO como segue prints apresentados

**Passos para reproduzir**

- Acessar base do zero ou base
- Abrir o cadastro do cliente 507353 na aba títulos

**Resultado apresentado**

>>O título 669805 consta como pendente
>>Na ERP_MXSPREST também consta como pendente
>Na PCPREST o título está pago

**Resultado esperado**

>>O título deve aparecer como pago no banco nuvem, da forma que já está no banco local

**Diagnostico e orientacao**

Foi realizada a normalização dos registros, sanando a divergência entre os bancos local e nuvem

A duplicata no processo foi definida para codoperacao = 2, isso garante que ela será dada como baixa (apagado) do maxPedido

O problema ocorreu porque no passado, no dia 06/12/2024 houve a seguinte falha "-6508 -ORA-06508: PL/SQL: could not find program unit being called", que não encontrava o programa para realizar a subida das informações da nuvem. O problema posteriormente foi corrigido, porém os dados retroativos só sobem realizando a normalização

A job vai rodar para atualizar o registro na MXSTITULOSABERTOS às 12:05:00 hoje, ela dispara a cada 1h, então depois desse horário: Para validar o RCA pode estar sincronizando o maxPedido, o título vai sumir do maxPedido

# GATE-609 - falhas com gerador de relatorios 800

**Contexto**

ao analisar o cenário relatado pelo cliente, não estou identificando qual a razão de estar apresentando falha nas gerações

o parametro do endereços dos relatorios está configurado adequadamente

!image-2025-01-09-12-51-44-094.png!

o acesso externo está sendo realizado normalmente

!image-2025-01-09-12-52-12-115.png!

os teste de autenticação e autorização estão corretamente aplicados

!image-2025-01-09-12-53-12-024.png!

assim como o acesso a pasta dos relatorios estão operando normalmente

!image-2025-01-09-12-54-08-763.png!

porém não é carregado nem os parametros do relatorio ou a geração dele é executada

!image-2025-01-09-12-54-46-942.png!

o que está acontecendo que está gerando essas situação, uma vez que todas das configurações esperadas de serem realizadas, estão corretas? existe algum outro ponto de configuração que demanda de ser realizado?

**Passos para reproduzir**

- Acessar o maxgestão do cliente, ir em relatorios winthor, buscar pelo relatorio 8044 e tentar gerar o mesmo

**Resultado apresentado**

está ocorrendo falha na geração dos relatorios

**Resultado esperado**

é esperado que o relatorio seja gerado sem falhas

**Diagnostico e orientacao**

Verifiquei a instalação dos relatórios 800, procurei também por LOGs e não identifiquei nenhum problema com essas informações

Eu realizei atualização do arquivo gerador da 800, removi a porta 8090 que estava sem uso para evitar qualquer tipo de conflito, deixando somente a 9090

Realizei uma normalização de dados, onde identifiquei que parâmetros da nossa nuvem estavam divergentes da PCPARAMETROS

Embora tenha validado tudo isso, não resolveu a situação. Então eu validei a questão de acessos

Com a VPN e com uma máquina usando a rede na região brasileira, está acessando normalmente o IP

Porém no Workspace não está acessando, provavelmente é algum bloqueio de região que o cliente possui na rede dele

O maxGestão precisa acessar pelo AWS, geralmente o pessoal libera porque a request do gestão utiliza essa conexão

Comparei também com outros clientes (MEGGA e HOTBEL) que estão funcionando atualmente e acessam pelo Workspace

Então sugiro duas coisas

1° Solicitar ao cliente verificar possíveis bloqueios por região, de forma que permita o acesso externo através de uma máquina que está fora do País (Vírginia - USA)

# GATE-612 - Divergencia entre valores exibidos entre maxgestão e rotina 146

**Contexto**

ao analisar o cenário relatado pelo cliente, não consegui identificar o que tem gerado a situação de divergência relatada, uma vez que observei a seguinte situação

Portal MaxGestão apresenta o seguinte valor

!image-2025-01-09-15-55-30-337.png!

Para a 146 está exibindo o seguinte valor

!image-2025-01-09-15-56-36-487.png!

MXSHISTORICOPEDC

!image-2025-01-09-15-57-33-910.png!

MXSHISTORICOPEDI

!image-2025-01-09-15-58-19-303.png!

Nesse cenário, o que está incorreto para que esteja sendo apresentado tal divergencia? existem alguns outros parametros na consulta que devem ser considerados para se chegar ao valor esperado?

**Passos para reproduzir**

- efetuar o acesso ao portal do maxgestão do cliente e realizar a consulta conforme os filtros nos prints apresentados

**Resultado apresentado**

divergencias de valores entre rotina 146 e o que é exibido no gestão

**Resultado esperado**

o cliente espera que sejam exibidos valores equivalentes

**Diagnostico e orientacao**

A rotina 146 do Winthor considera o valor de venda dos históricos das capas dos pedidos (VLATEND) da PCPEDC e o maxGestão considera o valor dos históricos de vendas dos itens

Por esse motivo ocorre essa diferença na apresentação da informação

SELECT SUM(VLATEND) FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('07/01/2025', 'dd/MM/yyyy') AND TO_DATE('07/01/2025', 'dd/MM/yyyy') AND POSICAO <> 'C' AND CODSUPERVISOR = 14
Resulta em R$198689.3

SELECT SUM(QT*PVENDA) FROM PCPEDI WHERE NUMPED IN(SELECT NUMPED FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('07/01/2025', 'dd/MM/yyyy') AND TO_DATE('07/01/2025', 'dd/MM/yyyy') AND POSICAO <> 'C' AND CODSUPERVISOR = 14) AND POSICAO <> 'C'
Resulta em R$201231.48

Como o cliente tem uma divergência nos históricos do próprio banco local referente a essa informação da venda dos itens, então os valores não batem

Importante pontuar também que a maioria dos clientes essa informação não bate mesmo. O maxGestão tem essa apuração a parte das informações, mas que também garante mais precisão na informação. No caso específico da venda transmitida, é considerado normal e está no escopo do produto que não é compatível com a 146, porque o ERP faz de um jeito e a nossa aplicação de outro, simplesmente

Já referente a Rotina 111 sim (Venda Faturada), os dados devem bater, essa explicação acima é uma especificidade da venda transmitida no maxGestão em relação à 146

Por fim, se o cliente quiser um comportamento divergente do atual, seria considerado uma sugestão de melhoria do sistema

# GATE-614 - Integradora rejeitando pedido pois estamos gravando um CODAUXILIAR errado

**Contexto**

Ao tentar realizar pedidos pelo MaxPedido com o item 29825 a integradora está rejeitando os pedidos pois estamos gravando na PCPEDIFV o CODAUXILIAR 10061 que não existe na PCEMBALAGEM, esse CODAUXILIAR existe somente na nossa tabela do banco nuvem MXSEMBALAGEM

Logo vê-se que está tendo divergência entre as tabelas PCEMABALAGEM e MXSEMBALAGEM

Foi realizado de teste o pedido 62255039

Constatei somente o CODAUXILIAR que estamos mandando errado sobre o preço não constatei nada

Dados para conectar no banco T-CLOUD do cliente
Schema: MAXSOLUCOES
Service name: CR0V85_124364_W_high.paas.oracle.com
Host: 181.41.189.71

**Passos para reproduzir**

- Acessar o aplicativo
- Iniciar um pedido no cliente 34503
- Ir na aba tabela e procurar pelo item 29825
- Adicionar o mesmo ao pedido
- Salvar e enviar o pedido
- E assim a integradora irá rejeitar o pedido informando que o preço de tabela está zerado e o CODAUXILIAR não existe no winthor
- OBS: CONSTATEI SOMENTE ISSO QUE ESTAMOS MANDANDO ERRADO

**Resultado apresentado**

Integradora rejeitando pedido devido estarmos enviando o CODAUXILIAR da embalagem que não existe no winthor

**Resultado esperado**

Que a gente envia o CODAUXILIAR correto e a integradora aceite o pedido

**Diagnostico e orientacao**

Foi feita normalização do produto 29825 e dos demais registros da filial 2, onde foi detectado o problema

Não foi possível identificar a causa exata da divergência, por esse motivo foram adicionados logs no cliente na trigger das embalagens para que caso ocorra algum problema semelhante novamente, possamos ter mais informações para análise

Os logs na trigger não foram colocados no atualizador do banco nuvem. Então caso o cliente seja atualizado, vai perder os logs que foram colocados diretamente no ambiente do cliente (no caso, vai parar de gerar log)

Para validar os RCAs podem estar sincronizando o maxPedido. A embalagem errada foi excluída, para transmitir o pedido corretamente o RCA deve sincronizar, remover o item do pedido caso esteja a embalagem ainda errada, e inserir novamente antes de transmitir o pedido

No caso eu vou todos os dias excluir os logs para que novos sejam gerados sem comprometer o espaço do banco, essa trigger gera muitos logs então não dá para deixar virar mais de um dia gerando logs

Quando o cliente ou suporte identificarem o problema novamente, se tivermos sorte, vamos conseguir analisar os logs criados

# GATE-617 - Restrições não sendo validadas

**Contexto**

Carlos e Filipe

Preciso de ajuda para entender uma situação que está ocorrendo na GSA e verificar se pode se tratar de um erro

O time de TI da empresa me informou que alguns RCAs estão conseguindo enviar pedidos com valores abaixo do limite definido na restrição de R$300. No entanto, ao tentar reproduzir o cenário em uma base do zero, não consegui replicar o comportamento. No meu teste, o sistema bloqueou o envio do pedido no final, apresentando a mensagem correspondente à restrição que impedia o processamento

Gostaria de entender como alguns RCAs estão conseguindo superar essa limitação e, se possível, identificar a causa do problema

**Passos para reproduzir**

- Acessar APK
- Importar base
- Observar o pedido 64220005
- Observar valor do pedido
- Consultar restrição 3648 da MXSRESTRICAOVENDA
- Tentar fazer o mesmo pedido em uma base do zero

**Resultado apresentado**

Alguns RCAs estão conseguindo enviar pedidos com valores abaixo do limite definido na restrição de R$300

Não consegui simular esse problema na base do RCA devido o limite de credito vencido do cliente do problema

**Resultado esperado**

Entender como isso aconteceu

**Diagnostico e orientacao**

No momento, é conforme foi descrito no ticket, não é possível simular o problema, porém através de logs dos jsons dos pedidos foi possível identificar a causa

Nos pedidos 64220005 e 64220007 o número da região no objeto está = 0, então provavelmente quando o RCA fez o pedido ocorreu algum problema com a região do cliente, porque se estivesse na mesma região da restrição cadastrada, teria barrado no valor de R$300

Em pedidos mais recentes que verifiquei, todos estão vindo com o número da região. Se voltar a ocorrer, eu oriento a pegar a base já na mesma hora, identificou que o pedido saiu errado, já pedir para o RCA mandar a base do maxPedido, porque nesses casos, teria de ter um cenário com o problema ocorrendo para debugar e identificar o motivo da região não gravar no JSON do pedido

Caso ocorra também com muita frequência e esteja impactando, mesmo sem cenário podemos tentar enviar para o nosso desenvolvimento pensar numa forma de rastrear o problema

# GATE-623 - PCPEDC divergente da MXSHISTORICOPEDC

**Contexto**

>>Os pedidos estão sendo gravados na PCPEDC porém não estão aparecendo na MXSHISTORICOPEDC, exemplo o pedido '119219089'

**Passos para reproduzir**

- Baixar base do RCA
- Verificar a timeline de pedidos
- Verificar as tabelas MXSINTEGRACAOPEDIDO, MXSHISTORICOPEDC e PCPEDC

**Resultado apresentado**

>>Os pedidos não foram enviados para a MXSHISTORICOPEDC e ao tentar pesquisar pelo post ocorrem erros(possívelmente ligado ao motivo do erro)
>>Os pedidos constam como L na timeline, porém já foram faturados na PCPEDC

**Resultado esperado**

>>Os registros da PCPEDC devem ser passados para a MXSHISTORICOPEDC e atualizarem na timeline do cliente

**Diagnostico e orientacao**

Ao verificar o pedido na MXSHISTORICOPEDC, constatei que já foi integrado automaticamente com POSICAO = 'F'

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED = 119014790
MXSHISTORICOPEDC e MXSHISTORICOPEDI normalizadas

Provavelmente, como eles estavam na versão 3.1.3.295 do banco anteriormente, então não estavam atualizados com a nossa alteração na TRIGGER para descer os registros para a MXSHISTORICOPEDC

Então depois que o banco aplicou a atualização no banco local, os registros integraram normalmente

Também fiz uma avaliação do banco local do cliente e constatei que não existem LOCKs e também não há problemas com objetos inválidos; O ambiente está funcional

Se o cliente observar uma lentidão no processamento ou o problema novamente com outros pedidos, por gentileza, reabrir o ticket informando as novas evidências

# GATE-626 - Comissões

**Contexto**

Ticket sendo aberto para análise do fluxo de comissão

Login para teste

destak.rca

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

Hoje eles usam 3.264.0 do maxPedido
Alguns na 3.256.2 e 3.242.1 do maxPedido

Trabalhar com comissão no maxPedido versão 3.268.3
Usuário que utilizamos: DESTAK.rca

Permissões do usuário ou perfil de usuários
- Visualizar valor de comissão de venda: marcado [V]
- Orçamentos > Orçamentos efetuados > Ocultar Informações de Comissão: desmarcado []
- Pedidos > Pedidos efetuados > Ocultar Informações de Comissão: desmarcado []

Documentos que temos na base

MXSFAIXACOMISSAOUSUR Calcular a comissão que é enviada aqui, na tela de negociação do maxPedido seria melhoria. Ele trabalha com o parâmetro HABILITA_FAIXA_COMISSAO = S

Exemplo de POST
/api/v

{version}/FaixaComissaoVendedor
- version = v1
[
\{ "codusur": "string", "numregiao": "string", "codprod": "string", "dtinicio": "2025-01-13T18:26:43.061Z", "dtfim": "2025-01-13T18:26:43.061Z", "faixa_ini_comissao": 0, "faixa_fim_comissao": 0, "comissao_padrao": 0, "hash": "string" }
]

Para cadastrar comissão percentual no produto e mostrar no campo customizado da tela 'Informações'

MXSPRODFILIAL.PCOMERP1, MXSPRODFILIAL.PCOMINT1 e MXSPRODFILIAL.PCOMEXT1

/api/v\{version}

/ProdutosFiliais
[

{ "codfilial": "string", "codprod": "string", "multiplo": 0, "qtminimaatacado": 0, "pcomrep1": 0, "pcomint1": 0,--Caso o vendedor seja do tipo "I" na MXSUSUARI "pcomext1": 0,--Caso o vendedor seja do tipo "E" na MXSUSUARI "qtmaxpedvenda": 0, "percmargemmin": 0, "qtminautoserv": 0, "calculaipi": "string", "hash": "string", "utilizaqtdesupmultipla": "string", "enviarforcavendas": "string", "checarmultiplovendabnf": "string", "proibidavenda": "string", "aceitavendafracao": "string", "permitirbrokertv5": "string" }

]

Comissão por RCA do botão "Comissões" da tela de negociação do maxPedido
Endpoint MXSCOMISSAOUSUR parâmetro EXIBIR_SUGESTAO_PRECO_COMISSAO = S

Exemplo: 91 3.1 5 5 FAIXA3-394.0 RP NULL NULL 394.0 P

/api/v

{version}

/ComissoesUsuarios
[

{ "codfaixa": "string", --FAIXA1-394.0 "percdescini": 0, --1 "percdescfim": 0, --5 "percom": 0, --5 "codusur": "string", --91 "codepto": "string", --NULL "codsec": "string", --NULL "codprod": "string", --394.0 "hash": "string", --NULL "tipo": "string", --P "tipocomissao": "string" --NULL }

]

Obs importante sobre o resumo de vendas

A comissão prevista na tela inicial carrega conforme comissão retornada nos endpoints de histórico

MXSHISTORICOPEDC.COMISSAO --na venda sem apuração por nota fiscal do resumo de vendas

Se for com apuração por nota fiscal dai seria na ERP_MXSNFSAID.COMISSAO

—

Outra informação importante
Se usar a tabela MXSCOMISSAOUSUR e MXSPRODFILIAL, funciona o cálculo previsto de comissão no final do pedido e inclusive, os dois também mexem na comissão apresentada do produto nos campos customizados

# GATE-630 - Não gera arquivo ao exportar pedidos

**Contexto**

Ao exportar os pedidos pelo menu de ferramentas aparentemente não estão sendo gerados os arquivos do pedido, e ao tentar importar os pedidos depois de limpar a base do aplicativo ele retorna que não existem arquivos de pedidos para importação

**Passos para reproduzir**

- Logar no maxPedido
- Importar a base anexada
- Exportar os pedidos
- Limpar a base do aplicativo
- Baixar base do zero
- Tentar importar os pedidos

**Resultado apresentado**

Mensagem informando que "Esse dispositivo não possui pedidos/orçamentos para importar

**Resultado esperado**

Importando os pedidos que foram exportados anteriormente

**Diagnostico e orientacao**

Se trata de erro foi realizado teste na versão 3.256.0 antes da alteração da SDK e funcionalidade estava com comportamento correto
1° Exportar pedidos
2° Limpar dados no armazenamento externo do maxPedido dentro das configurações do Android
3° Baixar base do zero
4° Importar pedidos
Resultado = pedidos importados com sucesso

Será encaminhado para N3

# GATE-631 - Plano de pagamento vinculado ao cliente

**Contexto**

Foi explicando para cliente que

o plano de pagamento cadastro desse cliente foi excluído, então ele não tem nem um plano de pagamento vinculado a ele, mas o plano de cobrança dele que e o O748 (COBRANCA OPTIMI ) ainda esta ativo, esse plano de cobrança é vinculado a outros planos de cobranças. Em resumo, por padrão vai buscar o que tiver vinculado ao plano de cobrança

Recomendo você trocar o plano de cobrança e de pagamento desse cliente, assim ele vai buscar o que tiver vinculado a ele

O comportamento padrão do aplicativo é buscar o plano de pagamento e o plano de cobrança configurados diretamente no cadastro do cliente

No caso específico do cliente X, ele está vinculado a um plano de pagamento inativo (plano Y). Por isso, o aplicativo busca automaticamente o primeiro plano de pagamento e cobrança ativo que o RCA possui acesso para utilizar com este cliente

Recomendamos que você compare este cliente X com outro cliente que esteja funcionando da forma desejada. Isso ajudará a identificar as diferenças de configuração no ERP

A regra de qual plano será carregado por padrão é definida diretamente no ERP, na Rotina 302. É lá que você configura o plano de cobrança e pagamento para cada cliente

- *_Só que cliente está questionado o por que esta aparecendo para todos os clientes o no cabeçalho do pedido plano de 7 dias._*

**Passos para reproduzir**

- Login - OPTIMI.977
- Acessar cliente 4071, ou qualquer cliente

**Resultado apresentado**

Cliente esta questionando que todos os cliente no cabeçalho do pedido esta aparecendo plano de pagamento de 7 dias

**Resultado esperado**

Que apareça o plano vinculado ao cliente

**Diagnostico e orientacao**

Quando o cliente não trabalha com MXSCOBPLPAG e MXSPLPAGCLI, então a aplicação carrega o plano de pagamento inicial cadastrado no cliente (MXSCLIENT campos CODPLPAG e CODCOB)

Se o plano não estiver ativo, existir alguma restrição de uso do plano no cliente ou o RCA não possuir acesso, então não deixa nem iniciar o pedido

Caso o cliente use o vínculo da MXSCOBPLPAG, então o sistema carrega seguindo a ordenação do menor plano de pagamento e cobranças que o cliente e RCA possuem acessos para utilizar

Como no caso do cliente 4076, ele possui no cadastro da MXSCLIENT o plano 133 e codcob O748. Se você colocar algum plano ou cobrança que o RCA possui acesso, então ele valida a regra da MXSCLIENT e a da MXSCOBPLPAG em conjunto
O que carrega é a ordenação dos planos e cobranças que o RCA possui acesso. No caso, as cobranças que ele possui acesso são

SELECT * FROM MXSACESSODADOS WHERE CODDADOS = 2
- ANT DEPOSITO ANTECIPADO
- BNF BONIFICACAO
- O748 COBRANCA OPTIMI PROM
- COBRANÇA PROMOVET OPTIMI
- SENT ENTREGA FUTURA

O plano 133 ele não existe na base do RCA SELECT * FROM MXSPLPAG WHERE CODPLPAG IN('133')

Então o sistema nesse caso carrega a cobrança direto ao abrir o pedido "O748 COBRANCA OPTIMI PROM" e já carrega os planos que o RCA e cliente possuem acesso ordenando por CODPLPAG

Se o RCA não tivesse acesso a nenhuma cobrança ou plano então carregaria simplesmente a ordenação do CODCOB e CODPLPAG menor conforme os acessos e a tabela MXSCOBPLPAG (Lembre que nesse caso está usando a MXSCOBPLPAG, se não estivesse usando ele validaria a MXSCLIENT primeiro e daria erro para abrir o pedido)

# GATE-633 - Valor UN do produto está incorreto

**Contexto**

Produto 701 na aba de negociação esta com o Valor UN dividido. Ex
Valor : 84,99 , valor UN 44,50

**Passos para reproduzir**

- Acessar maxPedido, iniciar pedido para cliente 29555, ou qualquer outro
- Pesquise pelo produto 701

**Resultado apresentado**

>> Produto 701, na parte de valor Un esta incorreto, trazendo valor dividido

**Resultado esperado**

>> Não dividir o valor UN. Valor correto

**Diagnostico e orientacao**

Para exibir o valor cheio do produto conforme a QTUNIT cadastrada no item que é de QTUNIT.MXSPRODUT = 2, basta habilitar a permissão "Exibir valor total" na Central de Configurações do usuário

Outra opção que eles possuem, é ficar com a permissão desativada "Exibir valor total" e configurar o produto na rotina 201 (integra na MXSPRODUT) para QTUNIT = 1, assim o valor unitário não será dividido por 2 resultando em 42,50

# GATE-638 - ordenação de criticas sendo exibidas de forma adequada

**Contexto**

ao analisar o cenário relatado pelo cliente no ticket citado, estou identificando que está ocorrendo uma ordenação inadequada de criticas no pedido, onde o ID critica foi gerado fora da sequencia esperada para a ocorrência dos eventos que foram aplicados pedido. No cenário que analisei, observa-se que a critica com o maior ID é uma critica anterior a critica mais atual presente para o pedido

!image-2025-01-14-16-17-40-724.png!

Essa situação gera um comportamento inadequado no app, exibindo legendas que não condizem com a realidade do pedido levando a uma interpretação inadequada da real posição e status do pedido

É possivel constatar isso via integração do pedido, que demonstra uma critica de erro

!image-2025-01-14-16-20-32-735.png!

mas o app exibe uma legenda de falha parcial

!image-2025-01-14-16-21-03-683.png!

**Passos para reproduzir**

- efetuar o login no aplicatico com o login wbcomp.ti
- acessar a tela de pedidos e observar as legendas do pedido, bem como as criticas do pedido presente e a ordem com que são apresentadas

**Resultado apresentado**

a aplicação está apresentando criticas sem seguir a ordem temporal dos eventos que o pedido passou e com isso gerando legendas que não condizem com a condição atual do pedido

**Resultado esperado**

é esperado que a ordem de criticas presentes siga os registros de data e hora com que foram realizados, tranzendo o real status dos pedidos

**Diagnostico e orientacao**

Foi inserido o parâmetro USAR_STATUS_ULTIMACRITICA para garantir que o sequenciamento está sendo feito conforme a última crítica

Realizada a normalização e redefinição do sequenciador MXSPROXNUMCRITICA no banco local e nuvem do cliente

Para normalizar para os RCAs eles precisam sincronizar o maxPedido

Podem realizar o swipe também que a timeline deverá atualizar corretamente os pedidos retroativos, pois o número da crítica foi aumentado e reprocessado

Também encaminhei para N3 porque a solução definitiva depende da correção que está sendo feita no ticket MXPEDDV-72797

# GATE-641 - RCAs não conseguem visualizar produtos (nenhum)

**Contexto**

Produtos não estão aparecendo para todos os RCAs, ambiente atualizado e testado na última versão, cliente não utiliza filial retira

**Passos para reproduzir**

- 1 - ir em produtos, selecionar filtros
- FILIAL 2 e REGIÃO 3

**Resultado apresentado**

Produtos não aparecem
Acontecendo com todos os RCA

**Resultado esperado**

Aparecer os produtos normalmente

**Diagnostico e orientacao**

Na base da RCA 128 grande parte dos produtos que não apareciam cerca de 400 produtos, era devido a restrições de venda

Então provavelmente o cliente observou isso e removeu as restrições do sistema para os produtos serem vendidos

Fiz teste em base zerada da RCA 145 que foi comentado no discord e constatei que está funcional também trazendo os produtos de exemplo "Cid" - CIDENTAL

Se a base da RCA estiver com divergências, dai eu precisaria da base dela e que um novo ticket de gate fosse aberto, mas acredito que eles resolvendo a questão das restrições deve ter normalizado para todos os RCAs

Igual é importante dialogar com o cliente para entender isso

# GATE-647 - Falha ao gerar roteiro de visitas

**Contexto**

ao analisar o cenário do ticket referido eu não identifiquei o que gera esse alerta abaixo

!image-2025-01-15-14-41-56-578.png!

onde mesmo que a configuração da semana tenha clientes definidos nos dias, não permite a geração da agenda por não encontrar uma sequencia

!image-2025-01-15-14-44-34-722.png!

Nesse cenário, o que falta de ser configurado no sistema pelo cliente para que a agenda possa ser gerada? ou se trata de algum erro no comportamento da aplicação?

**Passos para reproduzir**

- efetuar o login no portal do roteirizador do cliente
- buscar pelo RCA LEANDRO DIAS FERREIRA
- efetuar a roteirização do RCA
- clicar em agenda e selecionar agenda dinamica
- definir as regras conforme o print apresentado e no planejamento semanal escoler a rota SEMANA 2
- Clicar em "add sequencia
- observar o alerta retornado
- voltar as rotas do RCA e editar a SEMANA 2
- observar as listas de clientes definidos nessa respectiva rota

**Resultado apresentado**

está ocorrando um alerta de que a rota selecionada não possui uma sequencia de clientes para agendamento, mesmo que os dias da semana tenham clientes selecionados

**Resultado esperado**

é esperado que a sequencia ocorra sem falhas ao ser selecionada essa rota

**Diagnostico e orientacao**

A mensagem de não permitido adicionar "Rota SEMANA 1 não possui sequência de clientes para agendar visitas

Ocorre porque o cliente não finalizou o cadastro do Roteiro, que seria o percurso em Km Total que é gerado pela posição dos clientes no mapa

Esse cliente trabalha com "Regiões cadastradas" no Roteirizador e esse conceito fica habilitado para ser selecionado na hora de cadastrar a rota

Então para gerar a Roteirização ele precisa selecionar uma região em pelo menos um dia da semana na Rota cadastrada e depois apertar para Roteirizar

Feito isso o Km Total será gerado e ele conseguirá adicionar a Rota na Semana para geração de Agenda Dinâmica

Se eles não quiserem trabalhar com esse conceito, teriam que excluir as regiões cadastras no Roteirizador

Se ele contestar por qualquer outro motivo, por gentileza, me contatar para a gente conversar

# GATE-648 - Status dos pedidos não atualizam

**Contexto**

Status do pedido não atualiza na sync automática mesmo com os pedidos ja integrados

**Passos para reproduzir**

- Verificar pedido NUMPED = 5956

**Resultado apresentado**

Status dos pedidos não atualizam

**Resultado esperado**

Status dos pedidos atualizando na sync automática

**Diagnostico e orientacao**

Primeiro gostaria de esclarescer um ponto: Somente o pedido 5696 foi integrado a nuvem por enquanto, porque o pedido 5697 possui uma dependência de receber os dados primeiro do 5696 para depois ser enviado ao ERP

Sobre o pedido 5696, ele foi para a nuvem e ficou disponível para o ERP realizar a integração dele
>> O ERP integrou e nos gerou a informação da numeração do pedido ERP como "010122119700". Conforme reunião já realizadas com o responsável da integração do cliente
>> Acordamos que, para usar sincronização automática, eles precisariam enviar essa informação do pedido sem o "0" na frente
>> Também foi passado, mas vamos reforçar que o tamanho máximo é NUMBER (10) para o campo do pedido

>> Eles devem enviar o numPedidoERP sem o "0" na frente como expliquei, e essa informação se repete no mesmo endpoint (MXSINTEGRACAOPEDIDO)
1° A gente usa e registra ela vindo do ERP no campo numPedidoERP.CRITICA.NUMPEDERP como uma string JSON
2° A gente armazena ela também exclusivamente no campo NUMPEDERP.MXSINTEGRACAOPEDIDO

Eles também não retornaram ainda o histórico do pedido 5696. Que seria o nosso endpoint MXSHISTORICOPEDC(HistoricosPedidosCapas) com as inforamções do pedido

Aqui bem importante também, regras devem ser respeitadas na hora de eles nos enviarem o endpoint MXSHISTORICOPEDC

Eles devem copiar o DTABERTURAPEDPALM da MXSINTEGRACAOPEDIDO e mandar igual na MXSHISTORICOPEDC

Devem mandar o NUMPEDRCA e NUMPED corretamente na MXSHISTORICOPEDC, sendo a regra

MXSINTEGRACAOPEDIDO.NUMPED = MXSHISTORICOPEDC.NUMPEDRCA
e
MXSINTEGRACAOPEDIDO.NUMPEDERP = MXSHISTORICOPEDC.NUMPED

Devem mandar o mesmo CODUSUR, CODCLI, CODFILIAL, CONDVENDA que foi digitado (MXSINTEGRACAOPEDIDO). O endpoint deve ter exclusivamente esses dados batendo na (MXSHISTORICOPEDC e MXSINTEGRACAOPEDIDO)

- Mais um detalhe, o fluxo do maxSync está desligado na Safari porque da última vez a gente acordou que para testar, teria que solicitar ao Integrador verificar o fluxo no ERP e a gente na Máxima habilitar o fluxo internamente. Por esses motivos esse teste não foi 100% efetivo, seria necessário habilitar os fluxos e realizar um pedido novo do zero

# GATE-653 - Análise do comportamento do Flex e acréscimos na conta corrente

**Contexto**

O cliente relatou que, no período de 11/01 a 13/01, a conta corrente do vendedor Arthur apresenta valores como se houvesse acréscimos aplicados ao Flex. Contudo, segundo informado, os pedidos realizados no ERP do cliente não utilizam a funcionalidade Flex

Verifiquei na tabela ERP_MXSLOGRCA e só achei um pedido desse usuário no dia 11/01

**Passos para reproduzir**

- Usuário: meta.arthur1627
- Verificar pedidos feito na data 11/01 a 13/01

**Resultado apresentado**

N/A

**Resultado esperado**

N;A

**Diagnostico e orientacao**

Verifiquei o pedido que o cliente informou e foi comprovado que de fato veio do ERP porque possui ORIGEMPED = 'B' e não existe nenhuma relação com pedido na nuvem

Numéro 517706 não existe na MXSINTEGRACAOPEDIDO
e na MXSHSITORICOPEDC o numped = 517706

Nesse caso a nossa PKG por padrão sempre movimenta conta corrente de pedidos que vem do histórico, ou seja se vem direto do ERP a gente movimenta

Então para resolver, considerando o relato do cliente, foi feito o cadastrado e desativado o parâmetro USAR_PEDIDOS_ERP_CALCULO_CC. (USAR_PEDIDOS_ERP_CALCULO_CC = 'N')

Com isso, se o pedido vir direto com histórico do ERP, nós não faremos em hipótese alguma, movimentação do conta corrente dele. Será feita movimentação somente em pedidos confeccionados no Força de Vendas e que vierem histórico de pedidos que já existem processados no banco nuvem

# GATE-659 - maxGestao divergente  da 146

**Contexto**

Verificada divergência entre a 146 e o maxGestao no mês de dezembro

Na 111 o valor bate corretamente

**Passos para reproduzir**

- Abrir o maxGestao
- Colocar a data de 01/12 até 31/12 no filtro do painel geral

**Resultado apresentado**

>>Na 146 aparece um valor de R$2.033.342,77
>>No painel geral o valor é de R$332.719,32

**Resultado esperado**

>>O valor normalmente não bate entre a 146 e o Gestao, mas a diferença deve ser muito menor

**Diagnostico e orientacao**

Provavelmente cliente foi implantando no Winthor T-Cloud e não realizaram a carga dos pedidos do mês passado para o banco nuvem

SELECT SUM(VLATEND) FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('01/12/2024','DD/MM/YYYY') AND TO_DATE('31/12/2024','DD/MM/YYYY') AND CODFILIAL IN(1) AND POSICAO NOT IN('C')
Deu o mesmo resultado da 146, porque é de forma sintética o que a 146 faz. Resultando em R$2033342.77

SELECT SUM(QT*PVENDA) FROM PCPEDI WHERE NUMPED IN(SELECT NUMPED FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('01/12/2024','DD/MM/YYYY') AND TO_DATE('31/12/2024','DD/MM/YYYY') AND CODFILIAL IN(1) AND POSICAO NOT IN('C')) AND POSICAO NOT IN('C')

Já por histórico de itens, (como o maxGestão faz), não bate igual a 146, porque o valor dá divergente: R$2056551.45. Então o maxGestão e a 146 irão ficar divergentes justamente porque existe uma divergência dos valores dos históricos no banco do Winthor entre PCPEDC e PCPEDI

- Para comparar com a 146 realizar dedução de bonfiicações

No momento, (que estou te integrando o ticket) os valores estão batendo entre 146 e maxGestão deduzindo bnf. Porém ainda temos 20 mil registros descendo via integração do banco local para a nuvem então esse valor pode variar, até considerando o que expliquei sobre divergência de valores entre PCPEDC e PCPEDI

# GATE-663 - Cliente não aparece para ser roteirizado

**Contexto**

Cliente não aparece no sistema para ser roteirizado, mesmo estando vinculado ao RCA no campo MXSCLIENT.CODUSUR1

CODCLI: 65273

**Passos para reproduzir**

- Abrir roteirizador de vendedores
- Roteirizar RCA MAICON RODRIGUES LISKOSKI
- Buscar cliente 65273

**Resultado apresentado**

Cliente não aparece no sistema para ser roteirizado, mesmo estando vinculado ao RCA no campo MXSCLIENT.CODUSUR1

**Resultado esperado**

Cliente aparecendo na listagem para roteiziação

**Diagnostico e orientacao**

RCA
MAICON RODRIGUES LISKOSKI

O cliente 65273 não aparece para ser roteirizado porque não possui coordenadas cadastradas

Para resolver, antes de Roteirizador o RCA, deve ser verificado os "clientes sem coord." e validar que o cliente em questão 65273 não possui coordenadas. Elas devem ser cadastradas conforme o endereço do cliente ou se souber também a localização exata. Somente assim será possível adicionar no Roteiro de visitas do RCA

# GATE-668 - Valores gravados incorretos no JSON do pedido

**Contexto**

Carlos / Filipe

Identifiquei um problema na DESTRO que possivelmente ocorreu antes da correção do MXPEDDV-86344

No JSON, foi gravado o campo PrecoVenda como 35,52, que corresponde ao preço cheio (2,96 * 12 [fator] = 35,52). Contudo, o valor correto que deveria ter sido gravado é 2,96

No contexto do MXPEDDV-86344, foi confirmado que se tratava de um erro já corrigido. Entretanto, outros pedidos criados antes dessa versão ainda não foram identificados pelo cliente, o que pode impactar relatórios futuros. Esse caso específico já gerou confusões nos relatórios do MaxGestão

Detalhes do Pedido

PEDIDO: 3408409997
CODPROD: 1935856002, 1935855003, 361003
CODUSUARIO: 20645

**Passos para reproduzir**

- Acessar banco nuvem
- Consultar (SELECT * FROM MXSINTEGRACAOPEDIDO m WHERE NUMPEDERP = '3408409997'
- Observar os campos PrecoVenda e PrecoBase no JSON do pedido referente aos produtos 1935856002, 1935855003, 361003
- Consultar (SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED = 3408409997 AND CODPROD IN(1935856002, 1935855003, 361003)
- Observar os campos PVENDA e PBASERCA

**Resultado apresentado**

No JSON foi gravado o PrecoVenda = 35.52 que é o preço cheio, ou seja, 2,96 * 12 (fator) = 35,52. Enquanto o preço que deveria ter sido gravado é de 2,96

**Resultado esperado**

Saber como podemos corrigir isso nos pedidos que já foram processados

**Diagnostico e orientacao**

Foram verificados dados específicos de dois RCAs da Destro
Rcas desses pedidos
SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(3408409997, 3408434351)

Durante a análise observei que estão usando versão 3.257.0 e nessa versão, ainda não existe a correção para a aplicação do desconto PRG feita no ticket (MXPEDDV-86344)

E acredito que as coisas estejam interligadas. Porque os itens entram no Json do pedido com descontoprogressivo = true, porém não sofrem a alteração do desconto. Isso já é suficiente para os itens gravarem no relatório. Porém como não tem o desconto progressivo, os itens ficam com o totalizar de desconto zerado

Como no cenário do ticket informado os valores estavam negativos, eu fiz o ajuste do dado diretamente na MXSHISTORICOPEDI
SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED IN(3408409997) AND CODPROD IN(1935856002, 1935855003, 361003)

Antes o valor estava conforme o precoVenda do JSON e foi alterado para o pvenda e ptabela serem iguais

Nesse caso, com os dados retroativos, não tem o que possa ser feito, o relatório vai apresentar inconsistências, itens sem desconto progressivo aplicado devido ao uso da versão antiga

O ideal é que eles mudem de versão seja para a última antes da V4 ou para a própria V4. Digo isso só pela questão do Layout que muda. Eles precisam da migração em massa dos RCAs para o desconto progressivo funcionar corretamente tanto a nível de venda quanto de relatórios

Feitas as mudanças de versão, é só acompanhar o relatório para ver se ainda terão casos de preço de venda = preço de tabela e desconto nulo

# GATE-669 - maxPag não realizou estorno

**Contexto**

Não coloquei produto gatekeeper maxPag pois não tinha, porém tinha alinhado com o Filipe para subir GateKeeper

Acontece que no dia 10/01 foi realizado um pedido e feito o pagamento via PIX no maxPag, esse mesmo pedido foi para o ERP e teve cortes pela integradora, porém esse valor do corte não foi estornado no pedido conforme podemos observar nas movimentações do pedido pelo maxPag

ID TRANSAÇÃO MAXPAG: TMOsfx2IW8Lo6WhipoDaLuA7Nb
NUMPEDRCA: 3320007645
NUMPED: 332050052
VALOR TOTAL NO MAXPAG: 536,73
PCPEDC.VLATEND: 353.25

Verifiquei que não gerou registro de corte dos produtos na PCCORTE, mas não sei se é algo essencial para que o maxPag realize o estorno

**Passos para reproduzir**

- Acessar maxPag do cliente LDF
- No filtro 'Campos extras' consultar 3320007645
- Clicar para ver as movimentações do pedido
- Observar que não tem histórico de estorno por parte do maxPag
- Observar que o valor do pedido difere do valor atendido pelo ERP
- OBS: Link da base está no comentário do ticket em um link WeTransfer
- ##SELECTS UTILIZADOS
- SELECT NUMPEDERP, CODCLI, VLATEND, VALORTOTAL, em.* FROM MXSINTEGRACAOPEDIDO em WHERE NUMPED = 3320007652
- SELECT * FROM ERP_MXSCORTE WHERE NUMPED = 332050052 OR NUMPED = 3320007645

**Resultado apresentado**

Esse pedido foi para o ERP e teve cortes da integradora, porém esse valor do corte não foi estornado no pedido no maxPag

**Resultado esperado**

Que o valor da diferente de produtos não atendidos no corte seja estornado para o cliente

**Diagnostico e orientacao**

Foi feita correção no ticket de Gate mesmo a natureza correta é Erro

- Foi feita correção direto no Gate e lançado em produção

Existia um problema onde, o estorno do maxPag acumulava uma lista de pedidos e ele sempre processava seguindo a ordem do primeiro lançado > para o último lançado

Ou seja no caso o pedido ID_PEDIDO = 921199, ficou no final da fila e o processamento do estorno nunca chegava nele, e haviam outros pedidos nessa condição também

Para resolver, então foi alterada a lógica das buscas dos pedidos para estorno diretamente no Extrator. Assim que a alteração foi feita, lançamos a versão de extrator 3.1.2.458 e agora nós buscamos de forma dinâmica os pedidos para processar o estorno, garantindo que todos sejam processados corretamente conforme as pendências de estorno

- Para conferir é só consultar no pedido. Foi gravado o log na tabela e o cliente pode conferir também no maxPag e diretamente com o cliente se o Estorno foi efetuado com sucesso. A chamada do estorno nós fizemos automaticamente via Extrator da Máxima
SELECT * FROM MXSMAXPAYMENTMOV WHERE ID_PEDIDO IN(921199)

# GATE-672 - Divergencia de preço entre clientes

**Contexto**

Está ocorrendo uma divergencia de preço entre dois clientes operando sob a mesma tabela de preço, região, plano de pagamento, cobrança, filial, tributação, sem politicas de desconto

Ambos os clientes são PJ, do mesmo estado e mesma praça

Verifiquei as tabelas de preço, tributação, politicas, e os cadastros dos dois clientes, porem está ambos sob o mesmo cenário exato e não consegui encontrar motivo para a diferença nos preços

Clientes: 02934601, 02596801
CODPROD: 62120001
Filial 03
PLPAG: 0012
COB: BOLETO BANCARIO

**Passos para reproduzir**

- Logar no maxPedido
- Reproduzir os dois cenários nos dois clientes

**Resultado apresentado**

Mesmo com os cenários iguais existe uma divergencia de preço no produto 62120001 entre os dois clientes

**Resultado esperado**

Preços iguais

**Diagnostico e orientacao**

CODCLI 02934601 DE PB
62120001 PVENDA 1.69 CX R$243.12

CODCLI 02596801 DE PB
62120001 PVENDA 1.60 CX R$231.00

Cliente 02934601 possui um acréscimo na tabela MXSACRESCIMOSCLIENTES de 5.263158 e é isso que causa a diferença no valor de venda dos itens entre um e o outro cliente

Cliente 02596801 não possui acréscimo nessa tabela MXSACRESCIMOSCLIENTES

Para resolver a questão da diferença basta o cliente entender esse acréscimo que estamos recebendo via integração e alterar corretamente nos clientes

# GATE-679 - Após a carga das filiais 4, 5, 34 e 35 produtos carregam preço infinito

**Contexto**

As filiais 4 e 5 carregam os produtos normal, mas as filiais 34 e 35 carregam os produtos infinitamente

**Passos para reproduzir**

- 108459 || grupogeb.elilson-mendonca || 222
- SELECT * FROM mxstabprcli WHERE CODFILIALNF IN (4,5,34,35)

**Resultado apresentado**

Foi feita uma carga das filiais 4, 5, 34 e 35, no entanto mesmo tendo produto nas filiais 34 e 35 o preço não carrega

**Resultado esperado**

CARGA

**Diagnostico e orientacao**

Foi realizada carga das filiais novas 4, 5, 34 e 35 e já foi finalizada, o cliente pode estar validando testando realizar pedidos nessas filiais via maxPedido e comparando preços e estoques dos produtos em relação ao Winthor

# GATE-683 - Carga na MXSHISTORICOPEDC E MXSHISTORICOPEDI

**Contexto**

Cliente deseja que seja apresentado os dados referentes a 2024

Atualmente constam registros na MXSHISTORICOPEDC somente a partir de 01/12/2024 00:00:00

Alinhado com o DBA Lucas Silva e o Gatekeeper Filipe Padilha

**Passos para reproduzir**

- Carga nas tabelas PCPEDC E PCPEDI para as tabelas MXSHISTORICOPEDC e MXSHISTORICOPEDI para o período de todo o ano de 2024

**Resultado apresentado**

Atualmente constam registros na MXSHISTORICOPEDC somente a partir de 01/12/2024 00:00:00

**Resultado esperado**

Apresentado os dados referentes a todo 2024

**Diagnostico e orientacao**

Realizada a carga dos históricos de pedidos PEDC e PEDI referente ao ano passado inteiro 01/01/2024 a 31/12/2024

O histórico dos itens ainda está descendo via integração, para acompanhar você pode acessar

A carga foi feita somente na filial que eles já estão configurados para importar: Filial 1

Somente quando finalizar a baixa de todos os registros é que pode ser dado como finalizado. Lembre se que no maxGestão rotina 146 para comparar venda transmitida não bate em todos os casos e a Rotina 111 deve bater

# GATE-686 - Erro Estoque Maxpedido

**Contexto**

- *Cliente* - Estamos tentando implantar os pedido, mas o aplicativo está acusando que não tem saldo de estoque, sendo que o estoque dos produtos estão normais

acusando a mensagem de erro, permitindo implantar o pedido, o pedido chega no WT como bloqueado, não permitindo desbloquear e cancelando o pedido
Fiz teste na versão de ponta do maxPedido v4, e ao realizar teste foi visto que o sistema não busca a filial com estoque que no caso seria a filila 2, produto 101016 . Cliente disse que na versão v3.218 busca o estoque normalmente (produto 101016)

Fiz teste na versão v3.218 e realmente quando coloca a filial 2 no cabeçalho do pedido já busca a filial com estoque no caso a filial 2

**Passos para reproduzir**

- Iniciar pedido para qualquer cliente, colocar filial 2 no cabeçalho do pedido, busca pelo produto 101016

**Resultado apresentado**

>> Nas versões atuais, quando pesquisa pela produto 101016 incialmente mostra estoque, mas quando clica no produto mostra que o estoque esta zerado

>> Na versão v3.218, quando coloca filial 2 no cabeçalho do pedido, ao clicar no produto já e informado o estoque do produto

**Resultado esperado**

>> Mostre o estoque da filial 2

**Diagnostico e orientacao**

A versão que o cliente utiliza para comparação é muito antiga 3.218. E pode apresnetar erros já corrigidos em outras versões

A versão 3.269.2 que é a última antes da V4 já não possui mais o comportamento da 3.218

Nesse sentido vamos avaliar o cenário direto com base na V4 do maxPedido

Na V4, como ele possui registro na tabela MXSFILIALRETIRA, a apk realiza a seguinte consulta para buscar o estoque
SELECT mxsfilial.codigo, mxsfilial.razaosocial, MAX(IFNULL(mxsest.qtestger, 0) - IFNULL(mxsest.qtreserv, 0) - IFNULL(mxsest.qtbloqueada, 0) , 0) AS estoquedisp
FROM mxsfilial,mxsest,mxsacessodados,mxsfilialretira
WHERE
mxsfilialretira.codfilialvenda = '2'
AND mxsacessodados.coddados = 6
AND mxsacessodados.codusuario = 19120
AND mxsest.codfilial = mxsfilial.codigo
AND mxsfilial.codigo = mxsfilialretira.codfilialretira
AND mxsfilialretira.codfilialretira = mxsacessodados.chavedados
AND mxsest.codprod = '101016'

Atualmente a MXSFILIALRETIRA deles está divergente da PCFILIALRETIRA, esse é o motivo de estar tendo problema no carregamento do estoque, porque quando vende na filial 2, sempre retira na 2, segundo a regra da PCFILIALRETIRA deles

Hoje a MXSFILIALRETIRA está assim

3 1
1 3
1 2
1 1
3 2
2 2

E a PCFILIALRETIRA deles está assim

2 2
1 1
3 1

Nesse sentido, da forma que está hoje a nossa tabela, o SQL que citei acima sempre retorna primeiro o estoque da filial retira 1 que é estoque zero = (0)

Para resolver o cenário deles eu estarei realizando a normalização da divergência dos registros. Com isso, eu testei e o maxPedido pega o estoque da filial retira 2, mostrando corretamente e inserindo também a quantidade certa no pedido

Dito isso, agora é necessário que o cliente utilizando a última versão sincronize e realize o teste até o faturamento se fica tudo ok com o pedido

# GATE-688 - [BACKEND] Documentos de apoio deletados na central de configurações não são excluidos na nuvem

**Passos para reproduzir**

- Gostaria que fosse verificado se há um erro no fluxo dos cadastros de documento de apoio, visto que foi cadastrado o documento de apoio 101 anteriormente, que foi deletado porém continua com CODOPERACAO = 1 na MXSALERTARESTRICOES, impedindo que um determinado cliente seja cadastrado em outro documento de apoio
- Acessar Central de Configurações da GSA
- Extras: Documento de Apoio
- Criar novo documento de apoio
- Selecionar todos os ramos de atividade
- Selecionar região "SEM TABELA VINCULADA
- Selecionar o cliente 17484 - RB AGUIAR
- SELECT CODOPERACAO, MXSALERTACLIENTE.* FROM MXSALERTACLIENTE WHERE CODIGO = 101
- SELECT * FROM MXSALERTARESTRICOES WHERE CODIGO = 101 AND ID_REGISTRO = '17484'

**Resultado apresentado**

Ao salvar é exibido um pop-up informando que o cadastro não pode ser salvo por que o cliente está vinculado ao documento de apoio 101, porém esse documento já foi deletado

Na MXSALERTARESTRICOES foi alterado apenas a coluna ENVIAFV para N, o CODOPERACAO continua sendo 1

**Resultado esperado**

Que ao deletar o cadastro na central de configurações ele também seja deletado no banco nuvem

**Diagnostico e orientacao**

Foi verificado que o problema de exclusão já foi solucionado, ou seja, quando o cabeçalho do documento é excluído as restrições também devem ser excluídas

Porém haviam registros retroativos com problemas. Porque na versão antiga, não ocorria exclusão conforme regra citada

Para resolver o cenário foi feita normalização dos registros, agora todos os cabeçalhos excluídos possuem restrições excluídas e foi feito teste e de fato está excluindo

# GATE-689 - PREÇO DE TABELA PRODUTO 801695 DIFERENTE DO WINTHOR

**Contexto**

ao analisar o cenário abaixo

O pedido RCA 1862212947, teve o produto 801695 RUFFLES SAL C/PRECO 1X32G com um preço de tabela inferior da tabela no winthor, o preço de tabela do produto no prazo de 14 dias é de R$3,03 e no maxpedido ficou R$2,82 e com 7% de desconto de um combo chegou a R$2,62 onde o correto seria o valor mínimo de R$2,82, ficou como se o sistema deixou colocar o desconto duas vezes de 7%. Por favor verificar

Eu não consegui identificar o que aconteceu com esse pedido que gerou esse cenário que o cliente relata. O produto citado, teve um preço de tabela informado no JSON de 2,82: !image-2025-01-24-10-17-42-060.png!

Porém o preço original do item é de 2,99

!image-2025-01-24-10-19-22-759.png!

que condiz com o preço presente na mxstapr para a região do cliente do pedido

!image-2025-01-24-10-20-19-170.png!

o produto possui 2 politicas comerciais aplicadas(uma de desconto e outra acréscimo), mas que não alteram o preço de tabela

!image-2025-01-24-10-21-52-395.png!

Mas há um cenário anormal registrado, nas campanhas de desconto, onde o JSON foi gerado com um registro duplicado da mesma campanha

!image-2025-01-24-10-23-01-893.png!

com isso, essa situação é o que gerou o cenário em questão? ou é esperado que ocorra a negociação do item da forma que foi apresentada?

o seguinte script de consultas abaixo efetuei para fazer a validação que citei
{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsintegracaopedido{color} {color:#739eca}WHERE{color} {color:#00b8b8}numped{color} = {color:#c0c0c0}1862212947{color}{color:#eecc64};{color} {color:#669768}--politicas 1011960 1011904{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsdesconto{color} {color:#739eca}WHERE{color} {color:#00b8b8}coddesconto{color} {color:#739eca}IN{color} ({color:#c0c0c0}1011960{color},{color:#c0c0c0}1011904{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsusuarios{color} {color:#739eca}WHERE{color} {color:#00b8b8}codusuario{color} = {color:#c0c0c0}81812{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsaparelhosconnlog{color} {color:#739eca}WHERE{color} {color:#00b8b8}codusuario{color} = {color:#c0c0c0}81812{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} {color:#00b8b8}ptabela{color}, {color:#b788d3}c{color}. * {color:#739eca}FROM{color} {color:#b788d3}mxstabpr{color} {color:#b788d3}c{color} {color:#739eca}WHERE{color} {color:#00b8b8}codprod{color} = {color:#c0c0c0}801695{color} {color:#739eca}AND{color} {color:#00b8b8}numregiao{color} = {color:#c0c0c0}15{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsplpag{color} {color:#739eca}WHERE{color} {color:#00b8b8}codplpag{color} = {color:#c0c0c0}3{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} {color:#b788d3}C{color}.{color:#00b8b8}CLIENTE{color},{color:#b788d3}C{color}.{color:#00b8b8}CODCLI{color},{color:#b788d3}C{color}.{color:#00b8b8}CODPRACA{color},{color:#b788d3}N{color}.{color:#00b8b8}NUMREGIAO{color},{color:#b788d3}R{color}.{color:#00b8b8}REGIAO{color} {color:#739eca}FROM{color} {color:#b788d3}MXSCLIENT{color} {color:#b788d3}C{color}

{color:#739eca}JOIN{color} {color:#b788d3}MXSPRACA{color} {color:#b788d3}N{color} {color:#739eca}ON{color} {color:#b788d3}C{color}.{color:#00b8b8}CODPRACA{color} = {color:#b788d3}N{color}.{color:#00b8b8}CODPRACA{color}

{color:#739eca}JOIN{color} {color:#b788d3}MXSREGIAO{color} {color:#b788d3}R{color} {color:#739eca}ON{color} {color:#b788d3}R{color}.{color:#00b8b8}NUMREGIAO{color} = {color:#b788d3}N{color}.{color:#00b8b8}NUMREGIAO{color}

{color:#739eca}WHERE{color} {color:#00b8b8}CODCLI{color} = {color:#c0c0c0}206472{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsfilial{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsdescontoc{color} {color:#739eca}WHERE{color} {color:#00b8b8}codigo{color} = {color:#c0c0c0}11079{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}mxsdescontoi{color} {color:#739eca}WHERE{color} {color:#00b8b8}codigo{color} = {color:#c0c0c0}11079{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} {color:#b788d3}PED_TAB{color}.{color:#00b8b8}ID_PEDIDO{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}NUMPED{color} {color:#00b8b8}NUMPEDRCA{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}CODCLI{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}CODUSUR{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}CODFILIAL{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}CONDVENDA{color}, {color:#b788d3}PED_TAB{color}.{color:#00b8b8}TIPOPEDIDO{color}, {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}CODPROD{color}, {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}QUANTIDADE{color},{color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}APLICOUDESCONTOESCALONADO{color}

{color:#c1aa6c}ROUND{color}({color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}PRECOVENDA{color},{color:#c0c0c0}2{color}) {color:#00b8b8}PRECOVENDA{color}, {color:#c1aa6c}ROUND{color}({color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}PRECOBASE{color},{color:#c0c0c0}2{color}) {color:#00b8b8}PRECOBASE{color}, {color:#739eca}CASE{color} {color:#739eca}WHEN{color} {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}PRECOVENDA{color} > {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}PRECOBASE{color} {color:#739eca}THEN{color} {color:#cac580}'C'{color} {color:#739eca}ELSE{color} {color:#cac580}'D'{color} {color:#739eca}END{color} {color:#00b8b8}TIPOOPER{color}, {color:#b19b9b}PJSONPROD{color}.{color:#9e9e9e}SEQUENCIA{color} {color:#739eca}FROM{color} {color:#b788d3}MXSINTEGRACAOPEDIDO{color} {color:#b788d3}PED_TAB{color}, {color:#b19b9b}JSON_TABLE{color}({color:#9e9e9e}OBJETO_JSON{color}, {color:#cac580}'$.Produtos[*]'{color} {color:#9e9e9e}COLUMNS{color} ({color:#739eca}ROW_NUMBER{color} {color:#739eca}FOR{color} {color:#739eca}ORDINALITY{color}, {color:#9e9e9e}CODPROD{color} {color:#c1aa6c}VARCHAR2{color}({color:#c0c0c0}4000{color}) {color:#739eca}PATH{color} {color:#cac580}'$.Codigo'{color}, {color:#9e9e9e}PRECOBASE{color} {color:#c1aa6c}NUMBER{color} {color:#739eca}PATH{color} {color:#cac580}'$.PrecoBase'{color}, {color:#9e9e9e}PRECOVENDA{color} {color:#c1aa6c}NUMBER{color} {color:#739eca}PATH{color} {color:#cac580}'$.PrecoVenda'{color}, {color:#9e9e9e}QUANTIDADE{color} {color:#c1aa6c}NUMBER{color} {color:#739eca}PATH{color} {color:#cac580}'$.Quantidade'{color},{color:#9e9e9e}APLICOUDESCONTOESCALONADO{color} {color:#c1aa6c}VARCHAR2{color}({color:#c0c0c0}4000{color}) {color:#739eca}PATH{color} {color:#cac580}'$.AplicouDescontoEscalonado'{color}, {color:#9e9e9e}SEQUENCIA{color} {color:#c1aa6c}VARCHAR2{color}({color:#c0c0c0}4000{color}) {color:#739eca}PATH{color} {color:#cac580}'$.Sequencia'{color} )) {color:#9e9e9e}PJSONPROD{color} {color:#739eca}WHERE{color} {color:#9e9e9e}PED_TAB{color}.{color:#9e9e9e}ID_PEDIDO{color} = {color:#c0c0c0}350702{color} {color:#739eca}ORDER{color} {color:#739eca}BY{color} {color:#9e9e9e}SEQUENCIA{color}

**Passos para reproduzir**

- efetuar as consultas e validações conforme o cenário citado

**Resultado apresentado**

a principio, está sendo identificada que foi efetuada uma aplicação dupla de desconto no item com o mesmo percentual, de forma inesperada

**Resultado esperado**

é esperado que apenas a uma validação e inserção do desconto de 7% tenha sido aplicada

**Diagnostico e orientacao**

FILIAL 3
CODPLPAG 3
CODCLI 206472
CODPROD: 801695

Crítica do pedido

Descricao": ">>PEDIDO : 1862212947\n206472 - MARIA ANGELICA RODRIGUES DA SILVA\nTotal : 181.03\n--------------------------------------------\nPedido Winthor Normal : 1862006104\nVlr. Total : 181.03\nVlr. Atendido : 181.03\nQt Tot.Itens(Ped.Principal): 8\nQt Itens Atend: 8\n\n

Informações que temos no log do JSON do pedido
PrecoVenda": 2.62226
PercDescontoInformadoTela": 0.07
Tributacao": {
CodIcmPF": 0.2
CodIcmRural": 0.2
CodIcmPJ": 0.2
CodIcmTAB": 0.0925
SitTributaria": "90
CodFiscal": "5403
CodFiscalInterestadual": "6102
PrecoBase": 2.62226
PrecoOriginal": 2.99

repetido 2x

ListaCampanhasDesconto": [
Codigo": "11079
Descricao": "COMBO PARTE 01 - ITENS PRIORITARIOS ELMA
TipoPatrocinio": "E
TipoCampanha": "MIQ
DataInicio": "2025-01-03T00:00:00
DataTermino": "2025-01-31T23:59:59
CodigoProduto": "801695
QtMinima": 2.0
QtMaxima": 560.0
PercDesconto": 0.07
QtPedido": 0.0
UtilizaCodProdPrincipal": false
DescricaoProduto": null
Sequencia": 87
Chave": null
ComboContinuo": true
]
PoliticaCampanhaDesconto": {
Codigo": "11079
Descricao": "COMBO PARTE 01 - ITENS PRIORITARIOS ELMA
TipoPatrocinio": "E
TipoCampanha": "MIQ
DataInicio": "2025-01-03T00:00:00
DataTermino": "2025-01-31T23:59:59
CodigoProduto": "801695
QtMinima": 2.0
QtMaxima": 560.0
PercDesconto": 0.07
QtPedido": 0.0
UtilizaCodProdPrincipal": false
DescricaoProduto": null
Sequencia": 87
Chave": null
ComboContinuo": true

PrecoVendaInformado": 2.62226
PrecoTabelaInformado": 2.81963

Produto já não faz mais parte da campanha, para validar inserir
INSERT INTO MXSDESCONTOI (CODIGO, SEQUENCIA, CODPROD, QTMINIMA, PERDESC, TIPOPRODUTO, QTMAXIMA, SYNCFV, TIPODESCONTO, CODAUXILIAR) VALUES (11079, 87, 801695, 2.0, 7.0, NULL, 560.0, 'S', 'A', '7892840822996')

Em base do zero na mesma versão que o cliente está usando, não houve problemas nem com pedido normal, nem duplicado

Cenário do pedido dele passou por status 6 salvo e bloq e depois reenviado
6 2025-01-16 15:02:49.000
0 2025-01-16 15:10:46.000
2 2025-01-16 15:10:50.000
11 2025-01-16 15:10:53.000
4 2025-01-16 15:11:01.000

Comentários sobre a análise, não é possível replicar o problema. Aparentemente houve sim duas apliações de 7% de desconto no item do pedido. Pode ter sido fruto de algum bug de duplicação de pedidos ou então de importação de base que o RCA pode ter feito

Na própria base do RCA não é póssível simular. Se você tentar iniciar um pedido novo nem na base do zero, não é possível reproduzir nem na versão ponta do maxPedido e nem na versão do cliente

Nesse caso recomendo habilitar o parâmetro de log

GRAVA_LOG_ENVIO_PEDIDO

E utilizar a versão de ponta do maxPedido que já passou por correções no fluxo de duplicação e mudanças no uso de campanhas de Desconto

O pedido que foi passado com preço divergente apesar do problema, a Integradora da TOTVs não recusou a entrada do item

O desenvolvimento não tem como realizar uma correção retroativa do item que foi enviado com preço errado e como não é possível reproduzir o problema, e também não está utilizando versão de ponta, então não temos como realizar uma correção, é necessário o cliente utilizar as versões atualizadas do sistema para quando o problema ocorrer novamente (se ocorrer) a gente conseguir enviar para desenvolvimento N3

# GATE-690 - Preenchimento automático de informações no pedido para consumidor final

**Contexto**

>>Ao realizar pedido para consumidor final aparece o campo 'consumidor final' onde se preenche com os dados do cliente, porém o cliente deseja que os campos como endereço, numero, bairro, cep, telefone , etc sejam completos automaticamente, porém pelo que vi apenas os campos 'Cliente', 'CPF/CNPJ', 'Cidade/UF' e 'Email' são preenchidos

Estou abrindo este ticket para que seja verificado se existe algum modo de fazer com que na aba de consumidor final todos os campos podem ser preenchidos e o RCA apague e substitua apenas o necessário a eles

**Passos para reproduzir**

- Logar no maxPedido em base do zero ou base
- Iniciar pedido para consumidor final
- Incluir um item
- Salvar e bloquear o pedido

**Resultado apresentado**

Será aberta uma nova tela onde deve se colocar a informações do cliente
Apenas 'Cliente', 'CPF/CNPJ', 'Cidade/UF' e 'Email' são preenchidos

**Resultado esperado**

O cliente deseja que todas sejam preenchidas com as informações padrão cadastradas para o cliente 'consumidor final' e que o RCA consiga alterar apenas o que seja necessário a eles

**Diagnostico e orientacao**

A gente faz preenchimento das informações citadas
endereço, numero, bairro, cep, telefone

porém a gente busca de outros campos do cadastro do cliente, no caso se for Winthor, o cliente teria de cadastrar as informações na Rotina 302, referente a endereço comercial dos clientes consumidores finais

Se for cliente OERPs, seria no endpoint MXSCLIENT os campos

BAIRROCOM
ENDERCOM
NUMEROCOM
CEPCOM
TELCOM

# GATE-692 - Pedido Historico

**Contexto**

Pedido 17211982 não foi feito pelo RCA não aparece na aba de historico de pedidos, mas foi processado no whithor

**Passos para reproduzir**

- Foi analisado o banco do cliente na MXSINTEGRACAOPEDIDO
- os dois pedidos 17211982,17211984 consta em status 4
- Analisado o pedido na base do vendedor e não consta nenhum pedido 17211982, mesmo tirando todos os filtros do aplicativo
- Cliente relatou que pedidos não são feitos no maxPedido e sobem para o whinthor e que já ocorreu esse cenario mais de uma vez
- De acordo com o cliente o rca fez apenas o pedido 17211984
- base do rca muito grande para adicionar nos , encaminharei via WhatsApp ou discord

**Resultado apresentado**

>> Pedido 17211982 não apareceu no maxPedido

**Resultado esperado**

>> Pedido 17211982 aparecer no maxPedido

**Diagnostico e orientacao**

Foi verificado no detalhe a confecção dos pedidos. Após verificação dos dados eu pude concluir que o RCA 172 fez de fato esses pedidos, nós temos os logs do celular e das datas que ele sincronizou o maxPedido, e essas informações estão compatíveis com a data de abertura dos pedidos

Também gostaria de pontuar que o sistema não faz envio de pedidos de forma automática, isso depende de uma ação manual do RCA de digitar o pedido e então mandar salvar e enviar

Pelos logs dos pedidos, não foi um pedido salvo e bloqueado, foi um pedido normal que foi salvo e enviado diretamente para integração com o Winthor

Obs: não havia a base do RCA no ticket para análise, porém, se os pedidos não aparecem no maxPedido, na timeline por exemplo, pode ser porque o RCA excluiu os pedidos diretamente pelo maxPedido

Mesmo tendo excluído eles vão constar na aba Consultas > histórico de Pedidos
E se quiser restaurar eles na timeline de pedidos, basta habilitar o parâmetro
PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO = S e sincronizar o maxPedido

Abaixo coloquei as consultas realizadas na análise para entender o fluxo e ter dados mais concretos provando que o RCA 172 fez sim os pedidos

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPED IN(17211982,17211984)

SELECT * FROM MXSUSUARIOS WHERE CODUSUARIO IN(75880)
SELECT * FROM MXSUSUARIOS WHERE CODUSUR IN(172)
- Registro da data de abertura dos pedidos no maxPedido do RCA
- DTABERTURAPEDPALM
- 2025-01-14 08:29:25.000
- 2025-01-14 08:31:49.000

SELECT * FROM MXSAPARELHOSCONNLOG WHERE CODUSUARIO IN(75880) ORDER BY DTATUALIZ DESC
- O usuário estava usando esse aparelho e sincronizando normalmente para fazer pedidos durante o horário de confecção dos pedidos
- samsung SM-A207M 20250114094910 2025-01-14 09:49:10.000
- samsung SM-A207M 20250114084652 2025-01-14 08:46:52.000

SELECT * FROM MXSINTEGRACAOPEDIDO_LOGST WHERE ID_PEDIDO = 785452 ORDER BY DTATUALIZACAO ASC
SELECT * FROM MXSINTEGRACAOPEDIDO_LOGST WHERE ID_PEDIDO = 785456 ORDER BY DTATUALIZACAO ASC

SELECT * FROM MXSHISTORICOCRITICA m WHERE ID_PEDIDO = 785452 ORDER BY DATA ASC

SELECT * FROM MXSHISTORICOCRITICA m WHERE ID_PEDIDO = 785456 ORDER BY DATA ASC

SELECT ORIGEMPED,NUMPED,CODUSUR,CODCLI,DATA,DTFAT,DTABERTURAPEDPALM FROM MXSHISTORICOPEDC WHERE NUMPED IN(172006755, 172006631)
- Bate a data de abertura do pedido com o do maxPedido
- DTABERTURAPEDPALM
- 2025-01-14 08:29:25.000
- 2025-01-14 08:31:49.000

# GATE-694 - Erro de processamento de pedidos

**Contexto**

Conforme informado via Discord, será realizada a tentativa de reprocessamento dos pedidos mediante análise do erro ORA600 por parte do dba responsável pelo banco do cliente

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

O problema ocorreu devido a uma informação corrompida dentro do banco Oracle, na tabela PCPEDCFV provavelmente no campo DADOSPED CLOB

A causa raíz para isso nós não temos como identificar porque ocorreu dentro do banco Oracle localmente, e para identificar essa causa teria de ter analisado junto ao DBA o alert log do Oracle

Porém para resolver o problema a gente fez o drop da coluna DADOSPED e em seguida, recriou ela no schema da LDF

Recompilou o objeto e reenviou os pedidos com status 5, para status 0 para que eles fossem reintegrados

No momento os pedidos estão integrando normalmente

# GATE-697 - Movimentação na Flex.

**Contexto**

Cliente - esse exemplo aqui do flex do vendedor Arthur, ele não usou flex nesse pedido hoje e mesmo assim movimentou, parece que esse pequeno acréscimo veio do ERP

**Passos para reproduzir**

- Pedido numped 518094
- Verificar o por que teve desconto na FLEX

**Resultado apresentado**

Cliente informou que o RCA não utilizou a FLEX e mesmo assim teve desconto

**Resultado esperado**

Que não tenha desconto quando nao utilizar a flex

**Diagnostico e orientacao**

Para a Máxima, conforme já conversamos, é irrelevante configurações se debita/credita conta corrente. A gente não faz esse tipo de validação. Se ocorreu divergência entre o preço de venda e o preço base do item, ocorrerá débito ou crédito de conta corrente

Analisei dois itens desse pedido, o código 30 e 5299 ambos nós recebemos um valor divergente na MXSHISTORICOPEDI, que é alimentada pelo ERP, onde o preço de venda foi maior que o preço base dos produtos, por isso houve movimentação de conta corrente

Eu contatei o Renan integrador do ERP deles e repassei o mesmo cenário e pedi para ele verificar, agora precisamos aguardar retorno do Integrador

A nossa parte você já pode passar para o cliente

Consultas utilizadas

Cenário 1

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518094)
SELECT NUMPEDERP,NUMPED FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518094)

- "PrecoVenda": 5.45
- "PrecoBase": 5.45

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518094)
SELECT SUM(ROUND(PVENDA,2) * QT - ROUND(PBASERCA,2) * QT) AS CC ,PVENDA,PBASERCA FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 30 GROUP BY PVENDA, PBASERCA
SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 30

- PVENDA--5.472
- PBASERCA--5.45
SELECT SUM(VLCORRENTE - VLCORRENTEANT) FROM ERP_MXSLOGRCA WHERE NUMPEDRCA = 3322 AND CODPROD = 30
SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA = 3322 AND CODPROD = 30

SELECT * FROM MXSUSUARI WHERE CODUSUR IN(1627)

ListaPoliticasDescontoPorQuantidade": [
CodigoPolitica": "3051
QuantidadeInicial": 6
QuantidadeFinal": 9999
PercentualDesconto": 0.05505
PercentualDescontoMaximo": 0.0
AplicacaoAutomatica": true
Prioritaria": false
CreditaSobrePrecoTabela": true
BaseDebCredRCA": true
DataInicio": "2000-01-01T00:00:00
DataTermino": "5000-01-01T00:00:00
AlteraPrecoTabela": false
]

Cenário 2

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%CON_NUMCASASDECVENDA%'

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518094)
SELECT NUMPEDERP,NUMPED FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518094)

- "PrecoVenda": 1.45
- "PrecoBase": 1.45
- "PrecoOriginal": 1.65
- "Quantidade": 192.0

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518094)
SELECT SUM(ROUND(PVENDA,2) * QT - ROUND(PBASERCA,2) * QT) AS ,ROUND(PVENDA,2),PBASERCA FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 5299 GROUP BY PVENDA, PBASERCA
SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 5299

- PVENDA--1.455
- PBASERCA--1.45
SELECT SUM(VLCORRENTE - VLCORRENTEANT) FROM ERP_MXSLOGRCA WHERE NUMPEDRCA = 3322 AND CODPROD = 5299
SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA = 3322 AND CODPROD = 5299

SELECT * FROM MXSUSUARI WHERE CODUSUR IN(1627)

- política 529952

- "PoliticaDescontoPorQuantidade": {
- "CodigoPolitica": "529952
- "QuantidadeInicial": 16
- "QuantidadeFinal": 9999
- "PercentualDesconto": 0.12121
- "PercentualDescontoMaximo": 0.0
- "AplicacaoAutomatica": true
- "Prioritaria": false
- "CreditaSobrePrecoTabela": true
- "BaseDebCredRCA": true
- "DataInicio": "2000-01-01T00:00:00
- "DataTermino": "5000-01-01T00:00:00
- "AlteraPrecoTabela": true

Pedido: 518094
CODCLI: 4195
CODUSUR: 1627 (RCA)
CODFILIAL: 5
Cenário 1
Produto 30
Preço enviado no JSON da Máxima
- "PrecoVenda": 5.45
- "PrecoBase": 5.45
Preço enviado pelo ERP no nosso endpoint MXSHISTORICOPEDIO
- PVENDA--5.472
- PBASERCA--5.45
Movimentação de conta corrente: 0.08
SELECT SUM(ROUND(PVENDA,2) * QT - ROUND(PBASERCA,2) * QT) AS ,ROUND(PVENDA,2),PBASERCA FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 30 GROUP BY PVENDA, PBASERCA

Pedido: 518094
CODCLI: 4195
CODUSUR: 1627 (RCA)
CODFILIAL: 5
Cenário 2
Produto 5299
Preço enviado no JSON da Máxima
- "PrecoVenda": 1.45
- "PrecoBase": 1.45
Preço enviado pelo ERP no nosso endpoint MXSHISTORICOPEDIO
- PVENDA--1.455
- PBASERCA--1.45
Movimentação de conta corrente: 1.92
SELECT SUM(ROUND(PVENDA,2) * QT - ROUND(PBASERCA,2) * QT) AS ,ROUND(PVENDA,2),PBASERCA FROM MXSHISTORICOPEDI WHERE NUMPED IN(518094) AND CODPROD = 30 GROUP BY PVENDA, PBASERCA
O preço sofre um arredondamento 2 casas decimais sempre, de 1.455 passa a ser 1.46

# GATE-699 - API de cancelamento

**Contexto**

Cliente relata que no rca masterfrios.felipe, ao solicitar o cancelamento de um pedido qualquer, a aplicação retorna uma falha de autenticação da api do winthor. Foi verificado que o problema só ocorre com o RCA em questão, e ao consultar os dados de autenticação do usuário do WTA e comparar com os dados na stack do portainer, não foram verificadas irregularidades

Dados usuário WTA
SUPORTE
MASTERFRIOS

**Passos para reproduzir**

- Entrar na base zero do RCA, digitar um pedido qualquer e solicitar o cancelamento

**Resultado apresentado**

Ao solicitar e retornar a crítica, é verificado que é retornado uma falha de autenticação na API do Winthor

**Resultado esperado**

É esperado que o rca consiga cancelar o pedido normalmente

**Diagnostico e orientacao**

Fiz o teste com o usuário: masterfrios.FELIPE

Pedido enviado: SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP = 41055078

Pedido cancelado com sucesso na crítica e na PEDC: SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED = 41055078

Forma correta de cadastrar a stack

LINK_API_WINTHOR_CANCELAMENTO
USUARIO_API_WINTHOR_CANCELAMENTO: SUPORTE
SENHA_API_WINTHOR_CANCELAMENTO: FD03cHDMTmGBco1Dkv57Tw==

Como ele é cliente com extrator on-primise então eu peguei o IP direto da MXSPARAMFILIAL
SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%MOBILE%'

Ele clientes com extrator on-primise, ou seja, que não são t-cloud, deve ser utilizado o IP interno do WTA para utilizar a API de cancelamento de pedidos

# GATE-704 - Pedidos não estão sendo enviados para a nuvem da Máxima (V3 e V4)

**Contexto**

>> Cliente informa que vários RCAs estão passando pedidos, e alguns pedidos simplesmente não são enviados para a nuvem, mesmo com o ato do "Swipe
>> Foi passado uma base como exemplo, e mesmo importando a base no meu aparelho e fazendo swipe, os pedidos não foram enviados
>> Realizado teste na versão ponta da V3 e também na ponta da V4, e mesmo assim os pedidos não foram enviados

**Passos para reproduzir**

- Acessar a timeline de pedidos
- Observar os pedidos 1658 e 1659
- Realizar Swipe

**Resultado apresentado**

>> Os pedidos não estão sendo enviados para o banco nuvem

**Resultado esperado**

>> Pedidos serem enviados para a nuvem

**Diagnostico e orientacao**

- O cliente Fricó utiliza o maxSync

E estava na versão antiga que ainda não havia passado pelas correções da sinc automática. Inclusive, usar a base do cliente com a versão antiga do maxPedido causa problemas de sincronismo dos dados

SELECT * FROM MXSUSUARIOS WHERE CODUSUR IN(127)
- Está com a opção marcada USAMSGMAXSYNC = S

Nesse caso, por estar usando versão antiga com o maxSync, o que houve foi um problema com os registros dos pedidos, que já foram enviados para a nuvem e processados, porém não ocorreu o retorno correto via sinc automática para a base do RCA

Para resolver eu atualizei a versão do bd nuvem e do maxPedido e reprocessei somente os pedidos em específico 1658 e 1659

Foi também habilitado o parâmetro HABILITA_SYNC_AUTOMATICA = S por usuário somente nesse RCA

O problema foi causado por utilizar o fluxo de sync automática ativo no usuário, sem o parâmetro estar ativo

E a correção se deu reenviando os dados do pedido e utilizando sync automática

Se por acaso não quiserem mais usar sync automática nesse RCA, deve ser desfeito, o parâmetro HABILITA_SYNC_AUTOMATICA = N e o USAMSGMAXSYNC = N na MXSUSUARI (Suporte deve fazer)

O RCA deve migrar para a versão mais recente do maxPedido e sincronizar assim terá os status atualizados automaticamente, o sincronismo será somente para pegar os parâmetros e configurações alteradas

Outra opção como expliquei, fica na versão antiga, desfaz as configurações do maxSync e sincroniza

# GATE-705 - API de cancelamento

**Contexto**

Cliente relata que ao solicitar o cancelamento de um pedido qualquer, a aplicação retorna uma falha de autenticação da api do winthor. Foi verificado que o problema só ocorre com todos os RCAS, e ao consultar os dados de autenticação do usuário do WTA e comparar com os dados na stack do portainer, não foram verificadas irregularidades

Dados usuário WTA
MAXPEDIDO
@@MAX2332

Login para teste
bhatac.189

**Passos para reproduzir**

- Entrar na base zero do RCA, digitar um pedido qualquer e solicitar o cancelamento

**Resultado apresentado**

Ao solicitar e retornar a crítica, é verificado que é retornado uma falha de autenticação na API do Winthor

**Resultado esperado**

É esperado que o rca consiga cancelar o pedido normalmente

**Diagnostico e orientacao**

O IP estava errado no cadastro da stack para utilizar a API de cancelamentos

IP correto
LINK_API_WINTHOR_CANCELAMENTO
USUARIO_API_WINTHOR_CANCELAMENTO: MAXPEDIDO
SENHA_API_WINTHOR_CANCELAMENTO: xiqkk9xEEGxh3vkqhYwYlQ==

Como ele é cliente on-primise ele usa o IP que vai configurado na rotina 132 do Winthor. E a gente importa esse IP na coluna IPMOBILE

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%MOBILE%'

# GATE-708 - Painel de auditoria-Tempo de atendimento incorreto.

**Contexto**

Ao pesquisa no painel de auditoria RCA GLESON no dia 27/01, é informado que em quase todos os clientes o atendimento foi de 10 minutos

**Passos para reproduzir**

- Usuário: meggadist.510
- Ir no maxGestão, painel de auditoria, realizar pesquisa, filial 2, supervisor Douglas, RCA Gledson., dia 27/01 a 27/01
- Verificar tempo de atendimento

**Resultado apresentado**

>> Tempo de atendimento de quase todos clientes esta de 10 minutos

**Resultado esperado**

>> Que seja mostrado o tempo correto de atendimento

**Diagnostico e orientacao**

Foi analisado a base maxTracking do RCA e constatado que foram gravados os eventos com diferença de 10 minutos

Eu enviei para desenvolvimento para verificarem se estou correto na minha análise

A princípio o problema é gerado por uma versão antiga do maxPedido. Para resolver essa questão do tempo registrado nos eventos, recomendo atualizar a versão do maxPedido e habilitar o parâmetro BLOQUEAR_UTILIZACAO_BATERIA_OTIMIZADA que garante uma apuração mais precisa das informações de rastro

Mesmo atualizando a versõa, os dados retroativos não serão resolvidos, após atualizar esperamos que os novos registros não fiquem assim inconsistentes

Os dados retroativos não tem mais como serem corrigidos

# GATE-709 - RCA Gledson consta separado do supervisor 17 no relatório de auditoria

**Contexto**

Ao analisar o RCA Gledson, identificamos um problema na hierarquia do usuário. Quando selecionamos a opção de imprimir, o sistema mostra que o usuário não está vinculado ao supervisor 17. Em vez disso, ele aparece separado, como se não fizesse parte da equipe desse supervisor

**Passos para reproduzir**

- Acessar maxGestão
- Ir no painel de auditoria
- Realizar pesquisa para todos os usuários e supervisores, dias 27/01
- Ir na opçao de imprimir, verificar relatorio
- Verificar RCA Gledson, se esta abaixo do supervisor 17

**Resultado apresentado**

>> No relatorio mostra RCA Gledson seperado, como se não fosse vinculado ao supervisor 17

**Resultado esperado**

>> Que no relatorio mostre que o RCA Gledson esta vinculado ao supervisor 17

**Diagnostico e orientacao**

A funcionalidade que gera o relatório agrupado por supervisor, também agrupa por filial, porque o Supervisor é voinculado a filial 2

O RCA 510 que não aparece agrupado na equipe do Supervisor 17, é exibido dessa forma porque no cadastro do RCA na Rotina 517, ele não está vinculado à mesma filial do Supervisor dele, que é a filial 2

Para resolver, caso eles desejem que o RCA seja agrupado no relatório, eles precisam configurar o RCA vinculando ele à filial 2. Caso contrário ele será exibido desagrupado da equipe

Se quiserem alterar esse comportamento do maxGestão, eu sugiro abrir uma demanda de melhoria

SELECT * FROM MXSUSUARI WHERE CODUSUR IN(487, 510, 543,545)

SELECT * FROM MXSUSUARIOS WHERE CODUSUARIO IN(107360, 74412, 85595)

SELECT * FROM MXSSUPERV WHERE CODSUPERVISOR = 17

# GATE-711 - Pedido não atualiza na timeline

**Contexto**

>>O pedido 39003011 de exemplo (possuem outros), não aparece como enviado para o ERP, mesmo já tendo sido faturado

**Passos para reproduzir**

- Baixar a base do RCA
- Ir na timeline de pedidos
- Fazer swipe

**Resultado apresentado**

>>Mesmo após realizar swipe o pedido ainda não aparece como enviado para o ERP, mesmo o pedido estando como faturado na MXSHISTORICOPEDC
>>A útima crítica enviada é que o pedido foi de 'Sucesso'

**Resultado esperado**

>>Os pedidos devem aparecer assim como o status da MXSHISTORICOPEDC

**Diagnostico e orientacao**

39003011, 39003020, 39003005, 39002955, 39002957, 39002969, 39002999

Todos os pedidos que não tem a timeline atualizada são do tipo ORIGEMPED = R

E o parâmetro ENVIA_PEDIDOS_BALCAORESERVA do backend estava igual = N desde 2024-10-29 17:29:43.000

Para resolver foi feita ativação do parâmetro e carga dos pedidos dessa origem referente ao mês atual

Essa situação independe de versão era questão do parâmetro

O RCA deve sincronizar o maxPedido e depois verificar na timeline que tudo estará nos conformes

# GATE-715 - Graficos Desatualizados

**Contexto**

Não aparece informações nos gráficos o numero de vendas, os itens vendidos e clientes atendidos

**Passos para reproduzir**

- Verificado que existem registros na ERP_MXSDATAS
- Visto que existem registros no resumo de vendas
- dois vendedores relataram o erro

**Resultado apresentado**

>> Graficos não atualizam

**Resultado esperado**

>> Graficos mostrando informações

**Diagnostico e orientacao**

Dados corretos de conexão no cliente são

RAFATIGA_3095_PRODUCAO
maxsolucoes-card.cm35ayc6yrqh.us-east-1.rds.amazonaws.com

identifiquei isso pelo ticket pai e também pelo login que existe na base citada e também é o mesmo do usuário logado, quando confere via inspect

SELECT * FROM MXSUSUARIOS

Dados do bd T-CLOUD

189.126.154.116
CUG0DS_162882_W_high.paas.oracle.com
gdent17243ZRSPH@?

O gráfico do objetivo não atualiza porque o cliente não possui meta cadastrada para esse RCA
Que seria a rotina 353 no Winthor

SELECT * FROM PCMETARCA WHERE CODUSUR IN(2) ORDER BY DATA DESC

Além disso, os demais gráficos não atualizam porque eles não possuem o cadastro na

SELECT * FROM PCDIASUTEIS ORDER BY DATA DESC
e
SELECT * FROM PCDATAS ORDER BY DATA DESC

Amanhã vou concluir a análise

Os dados que constam sobre o cliente no ticket estão parcialmente corretos

Dados corretos de conexão no cliente são

RAFATIGA_3095_PRODUCAO
maxsolucoes-card.cm35ayc6yrqh.us-east-1.rds.amazonaws.com

identifiquei isso pelo ticket pai e também pelo login que existe na base citada e também é o mesmo do usuário logado, quando confere via inspect

SELECT * FROM MXSUSUARIOS

Dados do bd T-CLOUD

189.126.154.116
CUG0DS_162882_W_high.paas.oracle.com
gdent17243ZRSPH@?

O gráfico do objetivo não atualiza porque o cliente não possui meta cadastrada para esse RCA
Que seria a rotina 353 no Winthor

SELECT * FROM PCMETARCA WHERE CODUSUR IN(2) ORDER BY DATA DESC

Além disso, os demais gráficos não atualizam porque eles não possuem o cadastro na PCDATAS para o ano e mês atual. (2025/01)

SELECT * FROM PCDATAS ORDER BY DATA DESC

Depois de cadastrar a PCDATAS utilizando o Winthor, creio que a Rotina 309, poderá estar mandando atualizar o menu no maxPedido para conferir se os gráficos atualizam

# GATE-716 - Embalagem divergente

**Contexto**

Cliente relata que ao enviar um pedido com o produto 733480, a integradora realiza o corte do produto e retorna a crítica de que a embalagem não é válida. Foi verificado que a situação ocorre pois a embalagem que está sendo enviada associada ao produto não está mais ativa no sistema, sendo necessário realizar uma carga de dados para normalizar o cenário e corrigir o codauxiliar dos produtos em questão

**Passos para reproduzir**

- Acessar o banco nuvem do cliente, verificar o codauxiliar do produto na filial 3 e procurar pela embalagem 7899874103930, que está sendo enviada nos pedidos

**Resultado apresentado**

É verificado que a embalagem não consta na filial em questão, e que no Winthor a embalagem está inativa

**Resultado esperado**

É esperado que seja enviada a embalagem correta dos produtos nos pedidos

**Diagnostico e orientacao**

Foi realizada normalização das embalagens do cliente, todas as inativas foram setadas no banco nuvem corretamente para ficar espelhado com o banco local

Embalagem
CODFILIAL 1 AUXULIAR 7899874103930 CODPROD 733480
setada para codoperacao = 2

SELECT * FROM MXSEMBALAGEM WHERE CODPROD IN(733480)

Para os RCAs validarem basta sincronizar o maxPedido

- Foram validados os logs e não foi identificada nenhuma causa em potencial para o ocorrido, por isso, coloquei los na TRIGGER que faz a replicação dos dados para a nossa nuvem para caso ocorra novamente, termos informações para analisar

# GATE-718 - divergencia valores de grafico comissão v4 e v3

**Contexto**

estamos identificando divergências de comportamento nos valores que estão sendo retornados nos gráficos da V4. Enquanto a versão 3.269.2 retorna valores adequados para o que está presente na 1249

!image-2025-01-29-13-19-27-179.png!

A versão 4.000.4 trás valores completamente diferentes

!image-2025-01-29-13-20-09-404.png!

Observei que além da comissão, essa situação é apresentada em outros cenários, onde o valor de venda transmitida tbm tem essa divergência. Ocorreu alguma alteração no formato de calculo que a V4 tem para retornar esses valores ou há algum erro na aplicação que gera essa situação?

**Passos para reproduzir**

- efetuar o login na aplicação e atualizar os graficos da tela inicial e atualização de menu
- Comparar os resultados entre V3 e V4

**Resultado apresentado**

a versão ponta tras dados divergentes dos valores retornados no winthor e ná V3

**Resultado esperado**

é esperado que o valor retornado na V4 seja equivalente o que é exibido na V3

**Diagnostico e orientacao**

A comissão atualiza na tela conforme o botão que você pode alterar no gráfico 1 de

últimos 7 dias
última semana
Semana atual
Mês atual

E na tela inicial, considerando principalmente a questão da versão, o parâmetro "CRITERIO_VENDA_CARD_PEDIDO" atua. Por padrão ele mostra no gráfico 1 a apuração por venda Transmitida

Então eles poderiam mudar o parâmetro para CRITERIO_VENDA_CARD_PEDIDO = F

InformacoesRepresentanteResumo: REQ_MXSRESUMOVENDAS

InformacoesRepresentanteResumoDetalhado: REQ_MXSRESUMOVENDASDETALHE

obterInformacoesRepresentanteMix: REQ_MXSVENDA_MIX

Eu fiz uma análise prévia, porém, não consegui resolver a divergência entre v3 e v4 é evidente, vou encaminhar para dev porque exige um tempo de análise muito maior, de analisar scripts do backend que carregams os dados para depois carregarem no maxPedido e serem exibidos

# GATE-720 - Erro ao gerar visita avulsa

**Contexto**

Cliente relata que o RCA 137 não consegue gerar a visita avulsa em nenhum cliente no aplicativo. Foi realizada a simulação do cenário em base zero, onde o problema não foi replicado, entretanto ao simular na base do RCA, o problema relatado foi apresentado

Login para teste
mbm.suelemvieira

**Passos para reproduzir**

- Entrar na base zero do rca e gerar a visita avulsa no painel de clientes. Importar a base do rca e realizar o mesmo processo

**Resultado apresentado**

Ao simular na base do rca, ao gerar a visita avulsa a aplicação não inicia o pedido no cliente

**Resultado esperado**

É esperado que o RCA consiga gerar a visita avulsa corretamente

**Diagnostico e orientacao**

O maxPedido aparentemente está com um problema para gerar novas visitas avulsas, por não conseguir validar visitas e compromissos já criados

Como na base do RCA já existem compromissos criados, então o app entra em conflito com eles e não consegue gerar novos atualizados

Para resolver o problema, eu enviei um comando de deleção dos compromissos e das visitas avulsas criadas para o aparelho do RCA. Então quando ele sincronizar já estará livre para continuar usando o sistema

Eu encaminhei para N3 para o pessoal avaliar a necessidade de correção dado o cenário encontrado na MXSVISITAS e MXSCOMPROMISSOS

# GATE-722 - Quantidade de vendidos no mês não aparece na APK.

**Contexto**

A informação de quantidade de vendidos nos meses não está sendo exibida na APK. Atualmente nem os meses zerados são exibidos, apenas a informação "Sem venda registrada nos últimos 3 meses

Vou verificar nos tickets anteriores que foi passado para o cliente corrigir as informações das tabelas ERP_MXSMOV e ERP_MXSNFSAID, e os campos citados constam no banco nuvem, porem não reflete correção na APK

Verifiquei em clientes que fizeram pedidos nos últimos meses, com retorno correto para o banco nuvem

Listados produtos que foram positivados no período

Parâmetro NUNCA_EXIBIR_QUANTIDADE_VENDA_MES = N

Ocorrendo em base do zero

**Passos para reproduzir**

- Logar no maxPedido
- Iniciar pedido para cliente '05585470 0001' e filial '0101010'
- Listar produtos

**Resultado apresentado**

Nenhum produto apresenta a informação de vendidos nos meses anteriores

**Resultado esperado**

Listagem de produtos exibindo as informações de vendidos nos meses anteriores

**Diagnostico e orientacao**

Cenário do cliente '05585470 0001'
CODFILIAL '0101010'

Produtos vendidos nos últimos 3 meses

ALFFDV003, ALFFDV009, ALFFDV005

Produtos abaixo não foram vendidos nesse cliente nos últimos 3 meses, segundo dados que temos na nuvem, então por isso não tem informação de qtd vendida

BIOFVT015, MATTJK021, MATTJK022

- Regra que está impedindo a geração dos dados
- ERP_MXSMOV.CODFILIAL = ERP_MXSNFSAID.CODFILIAL

Eles continuam enviando a informação do ERP_MXSMOV.CODFILIAL = NULL

Para conferir

SELECT CODFILIAL FROM ERP_MXSMOV WHERE NUMTRANSVENDA = 3962734
SELECT CODFILIAL FROM ERP_MXSNFSAID WHERE NUMTRANSVENDA = 3962734
SELECT CODFILIAL FROM ERP_MXSMOV WHERE NUMTRANSVENDA = 3972784
SELECT CODFILIAL FROM ERP_MXSNFSAID WHERE NUMTRANSVENDA = 3972784
SELECT CODFILIAL FROM ERP_MXSMOV WHERE NUMTRANSVENDA = 3980984
SELECT CODFILIAL FROM ERP_MXSNFSAID WHERE NUMTRANSVENDA = 3980984

Para resolver eles precisam enviar o código da filial corretamente seguindo a regra conforme expliquei

# GATE-730 - Relatório geolocalização

**Contexto**

Na MXSVISITAFV consta apenas um atendimento para cada cliente, porem no maxGestão constam multiplos atendimentos para o mesmo cliente

**Passos para reproduzir**

- Na MXSVISITAFV consta apenas um atendimento para cada cliente, porem no maxGestão constam multiplos atendimentos para o mesmo cliente

**Resultado apresentado**

Mostram múltiplos atendimentos para o mesmo cliente sendo que teve apenas 1

**Resultado esperado**

Mostrar apenas 1 atendimento

**Diagnostico e orientacao**

Será encaminhado para N3, porém abaixo é importante realizar o entendimento sobre o que foi analisado

Cenário
CODUSUARIO: 93229 LOGIN: larbos.rodolfo

Segundo a base de dados maxTracking, ocorreu o evento de justificativa de não venda no cliente 5446 duas vezes (2x)

Foram registradas essas duas de forma correta
{"codigoVinculacao":-1,"dataAbertura":"Jan 22, 2025 10:23:23","dataFechamento":"Jan 22, 2025 10:23:28","motivoJustificativa":"Cliente Abastecido"}

{"codigoVinculacao":-1,"dataAbertura":"Jan 22, 2025 10:05:48","dataFechamento":"Jan 22, 2025 10:06:02","motivoJustificativa":"Cliente Abastecido"}

A princípio, isso foi uma ação manual do vendedor, de registrar duas vezes a justificativa

Referente às quatro informações de justificativa do cliente 5446 que constam no relatório do dia 22/01/2025, será encaminhado para N3 do maxPedido, porque foi o maxPedido que gerou a informação em duplicidade. Será solicitado que realizem a normalização e investiguem possíveis problemas com a geração dos dados

######################################################################

Sobre o questionamento do pedido do cliente 557841 no dia 22/01/2025

Ele na verdade é um pedido complementar, e de fato o RCA digitou fora do raio do cliente

Limite do raio do cliente para checkin e checkout: 100 (só valida se o RCA realizar o Checkin)

Tolerancia da cerca eletrônica(GPS_EDGE_METERS_SIZE): NULL

GPS_EDGE_BLOCK = N, não está fazendo validação sempre da localização ao realizar Checkin, pedidos ou justificativas

O sistema deles não está configurado para sempre solicitar Checkin, por isso ele conseguiu enviar um pedido mesmo sem estar na localização. Ele não precisou fazer Checkin para digitar o pedido

O parâmetro PERMITIR_PEDIDO_SEM_CHECKIN está configurado = Sim no RCA 543

Para sempre solicitar Checkin configurar os parâmetros
PERMITIR_PEDIDO_SEM_CHECKIN = N
OBRIGA_CHECKIN_CLIENTE_FORA_ROTA = S

# GATE-736 - Posição dos pedidos não atualizam na timeline

**Contexto**

Posição dos pedidos não atualizam na timeline

Base , ocorrendo com multiplos RCAs

**Passos para reproduzir**

- Verificar pedidos na MXSHISTORICOPEDC

**Resultado apresentado**

Status dos pedidos não atualizam

**Resultado esperado**

Status atualizando na sync automática corretamente

**Diagnostico e orientacao**

Foi realizada a carga dos dados retroativos que não haviam descido naturalmente para atualização da timeline através de sincronização automática

Foi realizada carga somente nesse caso porque já foi alinhado com o desenvolvimento sobre a última correção necessária que saiu na versão 4

Então os RCAs que estiverem usando o maxSync automática devem estar atualizados para a versão de ponta da V4 e então já podem conferir se os status foram atualizados automaticamente

# GATE-737 - divergencia em base do zero e base anexada

**Contexto**

ao analisar o cenário relatado pelo cliente, está sendo observado divergência de comportamento entre base do zero e a base anexada, onde mesmo o RCA sincronizando o app não normaliza a exibição dos produtos. Esse cenário acontece com vários vendedores do cliente

**Passos para reproduzir**

- efetuar o login na aplicação
- iniciar a negociação para o cliente 309799
- buscar os produtos na tabela
- comparar o mesmo fluxo na base anexada

**Resultado apresentado**

mesmo sincronizando, o RCA não consegue ver os produtos

**Resultado esperado**

é esperado que o app tenha o mesmo comportamento que ocorra na base do zero

**Diagnostico e orientacao**

Foi realizada a carga para as filiais 235, 251, 261, 271 que foram encontradas na base do RCA anexado. Dito isso, todos os RCAs que trabalham também com essas filiais terão como realizar a sincronização dos dados

Eu optei por fazer diretamente a carga porque eu entendi que esse cliente precisava de uma ação imediata para liberar os RCAs para venda

Eu vou continuar investigando para tentar encontrar a cauza raiz. A resolução definitiva, não é com a gente suporte/N2 isso é com o N3. Por isso eu vou encaminhar para desenvolvimento

- Sugestões de perguntas para esse cliente

>> Questionar que horas eles realizam a integração dos dados, e se eles fazem modificações em massa, porque a Máxima realiza manutenção no nosso bd nuvem de madrugada e se isso for concorrer com a integração do cliente, a integração simplesmente é parada

>> Questionar que horas os RCAs se dão conta que os itens sumiram

>> Questionar para o cliente se ele costuma trocar as filiais de venda dos RCAs com frequência através da Central
(No vídeo que chegou para mim no GATE o RCA Luciano possui acesso a 4 filiais e no momento, olhando pela central do RCA, ele possui acesso somente a 1 então isso comprova a teoria que o cliente fica alterando as filiais dos RCAs já em produção)

# GATE-743 - Acréscimo Flex.

**Contexto**

- *_Cliente _*- Ainda está sendo mandando um acréscimo do sintec para o max, sem o vendedor ter movimentado a conta corrente

Esses 2 ai já foi depois que eu havia zerado a conta e ia fazer o teste

**Passos para reproduzir**

- Analisar os pedido (518354,518362)

**Resultado apresentado**

>>está sendo mandando um acréscimo do sintec para o max, sem o vendedor ter movimentado a conta corrente

**Resultado esperado**

>> Não mandar o acréscimo para ERP

**Diagnostico e orientacao**

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518354,518362)

SELECT ROUND(PBASERCA,2), ROUND(PVENDA,2),CODPROD FROM MXSHISTORICOPEDI WHERE NUMPED = 518354

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA IN(3371)

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518354,518362)

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%CON_TIPOMOVCCRCA%'

SELECT C.NUMPED
NVL(C.NUMPEDRCA,'0') NUMPEDRCA
C.CODCLI
C.CODUSUR
C.CODFILIAL
C.POSICAO
C.CONDVENDA
FROM MXSHISTORICOPEDC C
INNER JOIN MXSUSUARI U
ON U.CODUSUR = C.CODUSUR AND U.CODOPERACAO != 2
WHERE C.DTATUALIZ >= TRUNC(SYSDATE) - 1
AND NVL(C.NUMPED,0) != 0
/* FLAG PROCESSARCC CRIADA PARA N¿O FICAR REPROCESSANDO QUANDO O PEDIDO FOR FATURADO OU CANCELADO */
AND NVL(C.PROCESSARCC,'S') = 'S'
AND NUMPED = 518354
ORDER BY C.NUMPED

SELECT
I.CODPROD
NVL(I.QT, 0) QUANTIDADE
ROUND(NVL(I.PBASERCA, I.PTABELA), 2) PRECOBASE
ROUND(I.PVENDA, 2) PRECOVENDA
CASE
WHEN I.PVENDA > I.PTABELA THEN 'C'
ELSE 'D'
END TIPOOPER
NVL(I.NUMSEQ, 1) SEQUENCIA
FROM
MXSHISTORICOPEDI I
WHERE
NUMPED = 518354
ORDER BY
I.NUMSEQ

Foi analisado o cenário do cliente referente aos pedidos citados e constatado que atualmente a Máxima não atende ao cenário de movimentação de Conta Corrente através da PKG

Porque o Preço de base deles é utilizado e salvo para comparação do preço de venda ao faturar o pedido. Porém nesse preço base, não ocorre o cálculo do acréscimo de boleto que eles fazem posteriormente dentro do ERP

Atualmente eu pensei em duas alternativas, mas não sei sobre a viabilidade, são apenas ideias

1° Eles teriam que integrar com a gente esse acréscimo especificamente para boletos de forma que isso vá calculado no PrecoBase do maxPedido e também no PrecoVenda. Assim na hora da PKG movimentar já estaria considerando o acréscimo. Porém isso mexe também na regra de negócios deles, porque os RCAs estariam já informando diratamente o preço final para os clientes durante a venda

2° A gente teria que fazer uma melhoria na PKG, parametrizável, para quando o houver recálculo no ERP, eles nos mandam isso já na MXSHISTORICOPEDI, o PBASERCA e PVENDA corretos, a gente pegaria da MXSHISTORICOPEDI as informaçõs do ERP para realizar a comparação e mover conta corrente. Atualmente a gente pega da ERP_MXSLOGRCA que ficou gravado já na transmissão do pedido (maxPedido), por isso dá divergência entre pvenda e pbase e movimenta conta corrente
======================
OBS IMPORTANTE: Por enquanto pausa o ticket dele e informa que está sendo analisado pelo desenvolvimento o assunto. (Na verdade está rolando o e-mail interno que eu escalei o assunto)

Não informa nem o Integrador deles e nem o cliente por enquanto, que a nossa PKG não atende o cenário deles

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED IN(518354,518362)

SELECT ROUND(PBASERCA,2), ROUND(PVENDA,2),CODPROD FROM MXSHISTORICOPEDI WHERE NUMPED = 518354

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA IN(3371)

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(518354,518362)

SELECT ROUND(PBASERCA,2), ROUND(PVENDA,2),CODPROD, DTATUALIZ FROM MXSHISTORICOPEDI WHERE NUMPED = 518362

SELECT * FROM ERP_MXSLOGRCA WHERE NUMPEDRCA IN(3373)

SELECT * FROM MXSPARAMFILIAL WHERE NOME LIKE '%CON_TIPOMOVCCRCA%'
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%NAO_MOVIMENTAR_CC_PED_BLOQUEADO%'

# GATE-744 - Dropar schema Pedido de Vendas

**Contexto**

>> Cliente solicita para limpar os os objetos que não são utilizados mais no banco Local dele (dropar schema do Pedido de Vendas)
>> Alinhado com o gateKeeper Filipe Padilha para dropar o schema do Pedido de Vendas do cliente

**Resultado apresentado**

N/A

**Resultado esperado**

N/A

**Diagnostico e orientacao**

Realizado o drop dos schemas do pedido de vendas não mais utilizados pelo cliente

Verificado também que o TS não se encontra no ambiente

# GATE-750 - Produto não aparece na base do RCA, porém aparece na base do zero

**Contexto**

>>Ao baixar a base do RCA vários produtos não aparecem para o RCA ex:5320

>>Não existe filtro aplicado

>>Realizei carga de atualizid nas seguintes tabelas porém mesmo sincronizando o problema não deixou de ocorrer

(MXSPRODUT, MXSPRODFILIAL, MXSEMBALAGEM, MXSFORNEC, MXSDEPTO, MXSSECAO, MXSTABPR, MXSTABPRCLI e MXSRESTRICAOVENDA0)

**Passos para reproduzir**

- Gerar base do zero e base do RCA
- Iniciar pedido para o cliente 10722 de exemplo
- procurar o produto 5320

**Resultado apresentado**

>>Na base do zero o produto aparece
>>na base do RCA o produto não aparece mesmo realizando carga

**Resultado esperado**

>>Os produtos devem aparecer na base do RCA

**Diagnostico e orientacao**

Realizada normalização dos dados que não eram apresentados para o RCA (produtos que não apareciam). Realizei o teste e após sincronizar o RCA conseguirá ver os produtos que não apareciam normalmente

O problema foi causado por um erro de sincronização e uso de múltiplos aparelhos. Nos logs da MXSAPARELHOSCONNLOG, constam 2 aparelhos utilizados no mesmo usuário do RCA, e na sincronização que desceria os dados da região de preço do produto, ocorreu um erro

Esses erros de sincronismo são tratados no nosso backend, foi feita uma correção para esse fluxo, onde, caso ocorra erro na sincronização, a próxima sincronização recebe novamente os dados para resolver o problema

Porém, para receber essa correção, o banco de dados nuvem deve ser atualizado

# GATE-751 - Clientes positivados zerados mesmo com pdidos na base do RCA

**Contexto**

>>Mesmo com registro na MXSDIASUTEIS e na ERP_MXSDATAS e com pedidos na base do RCA o maxPedido ainda mostra o gráfico 'Clientes positivados' em branco

**Passos para reproduzir**

- Baixar a base do RCA
- Ir até o gráfico 'Clientes positivados'
- Ir nos pedidos enviados

**Resultado apresentado**

>>Mesmo com pedidos na base do RCA o gráfico ainda permanece como '0'
>>A parte de meta também permanece zerada, mas pelo que vi a meta é de 1 milhão e os pdidos somaram R$1.485,26 o que não chega perto de 1 % da meta que seria de R$10.000,00

**Resultado esperado**

>>Os clientes devem aparecer no gráfico de clientes positivados

**Diagnostico e orientacao**

Foi verificado que o maxPedido v4 busca as informações no backend por padrão do script REQ_MXSVENDA_MIX

E na consulta do script, se tratando de positivação de clientes, ela sempre ocorrerá somente se o pedido for faturado, porque nós buscamos e validamos dados da PCNFSAID

Como os pedidos do RCA CODUSUR 2, que é atualmente o RCA vinculado ao usuário não estão FATURADOS e não possuem nota, então o gráfico permanece zerado na positivação de clientes

(O comportamento é diferente na positivação de produtos, tem parâmetro para considerar só por positivação no faturamento ou na transmissão de pedidos)

Referente ao gráfico de vendas, realmente, como a meta é 1 milhão e o valor vendido não ultrapassou os R$10000 que seria correspondente à 1%, então o valor atual seria 0.53% (Nem 1% ainda) então o gráfico não mostra a porcentagem abaixo de 1%

Esses gráficos são novos então se o cliente quiser alterar a regra de negócios eu recomendo enviar como melhoria

# GATE-758 - Itens do carregamento pronta entrega não aparecem no aplicativo

**Contexto**

>>Verificado que ao entrar no carregamento do pronta entrega os itens do carregamento 152743 não aparecem para o RCA

Tabelas que verifiquei

ERP_MXSMOV e PCMOV> Ambas possuem registros do carregamento 152743

ERP_MXSCARREG e PCCARREG > Na PCCARREG aparecem registros para o carregamento, porém na ERP_MXSMOV não aparece nenhum registro o que pode ser a causa da divergência

MXSESTMANIF> Não possui registros para esse usuario

**Passos para reproduzir**

- baixar base do zero ou base
- Abrir a aba'Consultas' e depois 'Venda pronta entrega'

**Resultado apresentado**

>>Aparece na tela o carregamento 152743 porém não aparece nenhum item para ser incluído

**Resultado esperado**

>>Os itens devem aparecer para serem vendidos

**Diagnostico e orientacao**

O processo de Prontra Entrega com o maxPedido considera vendas do tipo CONDVENDA = 13 na MXSHISTORICOPEDC e ERP_MXSNFSAID

Além disso, a gente utiliza da informação da tabela ERP_MXSCARREG para gerar o estoque no maxPedido

No caso do cliente, exisitia uma divergência de banco de dados, onde a PCCARREG possuia o número do carregamento, porém ele não desceu para o nosso banco nuvem

Para resolver eu fiz uma carga de vários registros dessa tabela PCCARREG para elas descerem para o nosso banco nuvem

Durante a análise não identifiquei problemas com os objetos do banco de dados e nem logs de erros

Pode ter ocorrido algum problema com os registros, para a nossa trigger não ter pego de forma automática os dados, porém não conseguimos identificar. Como expliquei, foi feita então essa descida manual dos registros

Nesse sentido, eu recomendo acompanhar para caso ocorra outra situação dessas, a gente encaminhar para outra equipe da Máxima que pode aprofundar a análise

Para o RCA receber o carregamento no aparelho, basta realizar uma sincronização parcial (apertar para sincronizar o maxPedido, que os produtos serão exibidos)

# GATE-759 - Erro ao inserir item

**Contexto**

+texto sublinhado+Ao tentar inserir o item 3614 está tendo um erro, porém, na 316 está passando normalmente. Está ocorrendo com todos os usuários

**Passos para reproduzir**

- Produto: 3614
- Tentar inserir o produto em algum pedido, gerando a mensagem de "erro

**Resultado apresentado**

Mensagem presente nos

**Resultado esperado**

Conseguir inserir normalmente

**Diagnostico e orientacao**

Ao realizar o teste na versão 3.230.0 que o cliente está utilizando, de fato o problema ocorre, mas não deveria

Então eu testei na versão 4.000.8 e funcionou normalmente, então isso quer dizer que houve correção para que o item fosse carregado com sucesso em versões posteriores à 3.230.0

Nesse sentido, recomendo atualizar a versão do maxPedido para a 4, porém se o cliente quiser se manter na 3, ele pode atualizar para a 3.269.2 (última da v3) ou até anteriores como a 3.258.0, por exemplo

# GATE-761 - API DE CANCELAMENTO COM ERRO

**Contexto**

Foi feita a troca de IP na stack do extrator: o IP antigo (192.168.0.9:8180) foi alterado para o novo IP (192.168.9.25:8180)

Mesmo após a mudança, o cliente ainda não consegue cancelar os pedidos no MaxPedido

Foi realizado um teste utilizando o IP local para acessar o Winthor Anywhere, e o acesso foi realizado com sucesso

**Passos para reproduzir**

- Acessar maxPedido com qualquer usuário, enviar pedidos e logo depois cancelar

**Resultado apresentado**

>> Não esta cancelando os pedidos, dando critica de API CANCELADA INVALIDA

**Resultado esperado**

>> Que os RCA consegui cancelar os pedidos enviados

**Diagnostico e orientacao**

A autenticação não estava funcionando devido à identação da variável na Stack (compose) do cliente

Para resolver eu fiz o seguinte

Acessei o

entrei na stack e substituí a variável
LINK_API_WINTHOR_CANCELAMENTO

Substituí por
LINK_API_WINTHOR_CANCELAMENTO

Depois fiz o deploy, baixei o maxPedido na versão 4.000.8 e simulei o uso da API

Pedido cancelado com sucesso via API

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPEDRCA IN(282710440)

# GATE-767 - Importação do Mix ideal barra produtos

**Contexto**

Ao tentar inserir produtos na edição do mix ideal pela função de importação de excel, é exibido um erro informando que "itens não foram importados pois não existem na base ou não satisfazem as parametrizações de venda por embalagem", porem é possível inserir esses itens manualmente sem nenhum impeditivo

Tabela

**Passos para reproduzir**

- Abrir mix ideal
- Tentar importar produtos
- Em seguida inserir manualmente produtos que foram barrados na importação

**Resultado apresentado**

erro informando que "itens não foram importados pois não existem na base ou não satisfazem as parametrizações de venda por embalagem

**Resultado esperado**

Importação ocorrendo com sucesso

**Diagnostico e orientacao**

Na planilha tem vários CODAUXILIAR associados a produtos que não existem no nosso banco nuvem

Por exemplo, o produto 1930243014 possui as três embalagens cujos CODAXILIAR são da FILIAL DE06

17509546695386
2050001915573
2050001915535

Quando é inserido via Central selecionado específico o codprod, então a gente carrega as embalagens conforme a filial selecionada, por isso dá certo. A gente carrega no caso as três embalagens que existem ativas na nuvem

17509546695386
2050001915573
2050001915535

Pra validar
- O retorno será somente os produtos com CODAUXILIAR cadastrado na DE06
SELECT * FROM MXSEMBALAGEM WHERE CODAUXILIAR IN(7891024134702
7891024033715
7509546656861
7793100111143
7509546684789
7891024025017
7891024132371
7509546669953
7891528038001
7891528028132
7891024026434
7891024184509
7501033205293
7891024029886
7891024136409
7891024174715
7891024174210
7891024110300
7891024182475
7891024035139
7891024027325
7891024194102
7891024194607
7891024120705
7891024128305
7793100111143
7509546684789
7891024025017
7509546684048
7891024135020
7891024135310
7509546686042
7509546688091
7509546695389
7891024110409) AND CODFILIAL IN('DE06') AND CODOPERACAO <> 2

- Select só para vc ver que é o mesmo número que a central retorna, ou seja de 35, somente 14 são encontrados, ficando 21 que não passam na validação
SELECT 35 - 14 FROM DUAL

# GATE-770 - Parâmetro não é vinculado a filial

**Contexto**

Parâmetro CON_PERMAXINDENIZPEDIDO está vinculado a filial 3, porem o pedido da filial 3 não puxa o valor de indenização que consta no parâmetro mesmo estando correto dentro da base da APK

Na base consta o parâmetro CON_PERMAXINDENIZPEDIDO para a filial 99 e filial 3. Mesmo deletando o registro da filial 99 a APK apresenta o valor da indenização = 0 mas não puxa o valor vinculado a filial 3

vídeo do processo e a base utilizada

Ocorrendo também em base do zero

**Passos para reproduzir**

- Reproduzir passos do vídeo

**Resultado apresentado**

Mesmo deletando o registro da filial 99 a APK apresenta o valor da indenização = 0 mas não puxa o valor vinculado a filial 3

**Resultado esperado**

APK puxando o valor do parâmetro CON_PERMAXINDENIZPEDIDO para a filial 3

**Diagnostico e orientacao**

O parâmetro CON_PERMAXINDENIZPEDIDO e original do Winthor, por isso existe esse conceito no força de vendas da Máxima
Porém no próprio Winthor, ele é um parâmetro geral e não pode ser configurado por Filial, por este motivo, nós atualmente apenas replicamos esse comportamento

Nesse sentido: O maxPedido realmente não valida essa configuração de indenização por filial, para alteração desse comportamento teríamos de avaliar como possibilidade de Melhoria para o sistema

Cenário
CODCLI: 73718
Região 70000
CODPLPAG 6
CODPROD
973727 QT 4

Ps: faltou o login só 🙂 na próxima lembra de colocar

# GATE-773 - divergencia de comportamentos entre V3 e V4 - check - in/out fora do raio

**Contexto**

ao analisar e replicar o comportamento citado pela cliente na demanda aqui linkada, estou observando um comportamento onde a V4 não está validando de forma esperada as permissões de "Solicitar autorização para checkin fora do raio" e "Requer autorização para checkout fora do raio do cliente" que estão marcadas no usuário

!image-2025-02-11-10-25-17-702.png!

há 2 videos que gravei simulando o mesmo fluxo nas duas versões de tentar iniciar um pedido para um cliente fora de rota e fora do raio de check-in/check-out, onde exibem essa diferenças de comportamento. Enquanto a V3 gera 3 requisições de desbloqueio para: visita avulsa, check-in fora do raio e check-out fora do raio, a V4 solicita apenas um desbloqueio

Esse comportamento é um erro ou o fluxo teve alguma alteração nessas validações devido as alterações de estrutura e de regras de negocio do aplicativo?

**Passos para reproduzir**

- efetuar o login na aplicação, acessar a tela de clientes, buscar pelo primeiro cliente fora de rota que for exibido e tentar iniciar um pedido

**Resultado apresentado**

a V4 gera uma unica solicitação de desbloqueio quando o cliente se encaixa no cenario de ser fora de rota e fora de raio

**Resultado esperado**

o cliente espera que a V4 gere as mesmas requisições de desbloqueio que ele observa acontecer na V3

**Diagnostico e orientacao**

O comportamento na versão nova realmente foi alterado, a alteração é do ticket
Resolve: MXPEDDV-81774

Falha: Ao realizar uma visita avulsa, sequenciamento de visitas e cerca eletronica estão sendo validados, dificultando experiência do rca

Defeito: Pela regra, entende-se que o rca ao realizar uma visita avulsa, não há intenção de validação de raio e sequenciamento de visitas, haja visto que ele deverá realizar conseguir realizar o pedido avulso de onde estiver, e não necessariamente dentro do cliente avulso da rota

Solução: inserida validação, onde caso haja criação de visita avulsa, este rca não terá necessidade de validar cerca e sequenciamento dentro do processo de checkin, ao terminar o atendimento, deverá continuar com as validações inerentes aos clientes dentro do roteiro

Nesse caso, a configuração atual deles, que funcionava na versão antiga, não vai mais atender ao cenário

O que eles poderiam fazer, seria adotar um novo fluxo de trabalho com os parâmetros

PERIODO_PED_FORA_ROTA = 0 (para validar o dia atual)
QTD_MAX_PED_FORA_ROTA = 1 (A quantidade que o RCA for ter de permissão para pedido fora de rota); --Não pode ser 0, quando é zero não valida esse bloqueio de pedidos para clientes fora de Rota

Ambos parâmetros funcionam por RCA

Bloquear venda de clientes fora da rota [] desmarcar (assim poderá fazer pedido fora de rota)

A autorização de atender fora de rota nesse caso, pode desmarcar também, porque ela sempre valida junto com a de Bloquear venda de clientes fora de rota, não valida em nenhum outro fluxo de forma avulsa

Com a configuração que sugeri, a "permissão" de fazer pedido fora de rota será controlada pelo parâmetro QTD_MAX_PED_FORA_ROTA, e nesse fluxo, sempre valida Checkin/Checkout e o Raio do Checkin/Checkout

Qualquer fluxo diferente desse nas versões novas, pode ser considerado melhoria

# GATE-776 - Acréscimo máximo

**Contexto**

Cliente deseja trabalhar com acréscimo máximo por produto no maxPedido
Foi verificado inicialmente por parte do cliente o cadastro de um percentual máximo de acréscimo pela Central de Configurações, em Inteligência de Negócios > Detalhes de produtos. Entretanto, em conversa interna com o gatekeeper, foi verificado que a opção desejada pelo cliente não se aplica em cenários de cliente Winthor
Dessa forma, foi realizado teste no suporte, onde foi realizada a alteração do campo MXSTABPR.PERACRESCMAX para o produto 40455 via inspect em uma base zero, mas ao simular a inserção do produto com um acréscimo maior que o definido na tabela, a aplicação não recusou a inserção do produto devido ao acréscimo indevido
Foram verificadas as tabelas MXSUSUARI.PERCACRESFV, MXSCLIENT.PERDESC, MXSATIVI.PERCDESC, o parâmetro ACEITADESCTMKFV na MXSPARAMFILIAL e as políticas de desconto, onde não foram verificados registros que impactassem na simulação realizada

login para teste
cetap.3103

**Passos para reproduzir**

- Entrar na base do rca, iniciar o pedido em qualquer cliente, inserir o produto 40455 com um acréscimo maior que 1%, conforme definido na MXSTABPR

**Resultado apresentado**

Ao inserir um acréscimo maior, é verificado que a aplicação não barra o produto de ser inserido

**Resultado esperado**

É esperado que a aplicação valide o acréscimo máximo dos produtos

**Diagnostico e orientacao**

O maxPedido atualmente está pegando o acréscimo da configuração desse parâmetro CON_PERMAXVENDA que na CETAP está configurado como 9999

A regra é a seguinte

a) mxsprodut.peracrescmax (cenário atual está preenchido)
b) mxsusuari.PERCACRESFV (não está preenchido)
c) CON_PERMAXVENDA

Se mxsprodut.peracrescmax e mxsusuari.PERCACRESFV não estiverem zerados, usa o maior percentual, senão usa o CON_PERMAXVENDA

Como o mxsusuari.PERCACRESFV está nulo então ele pega do parâmetro configurado

A alteração que faz isso no código é desse ticket: MXPEDDV-38957

Então para resolver, eles teriam que, ou configurar o mxsusuari.PERCACRESFV do RCA, ou, zerar o parâmetro CON_PERMAXVENDA na Rotina 132

Se o cliente questionar, não quiser realizar alterações, então ele teria que validar na 316 e nos mostrar o comportamento atual deles na 316, considerando os parâmetros e a forma que está configurado atualmente

Se existir divergência entre 316 e maxPedido, pode encaminhar para desenvolvimento N3. Mas aqui o caso eu acredito que seja falta de conhecimento sobre essas configurações citadas

# GATE-780 - Não está gerando a nota em pedidos do pronta entrega

**Contexto**

Ao realizar alguns pedidos pelo MaxPedido com o tipo de venda pronta entrega, não está emitindo as notas, quando realiza o pedido internamente pelo winthor as notas são emitidas normalmente

Gostaria de apoio para entender porque os pedidos pelo força de vendas utilizando o pronta entrega está retornando essa crítica e não permitindo emitir as notas

**Passos para reproduzir**

- Acessar o aplicativo
- Importar a base anexada
- Ir na tela de pedidos
- Duplicar o pedido 2582580831
- Salvar e enviar o pedido
- Irá ver que o pedido é enviado mais logo após um tempo retorna um x no pedido e a crítica anexada

**Resultado apresentado**

Pedidos realizados utilizando o pronta entrega não está emitindo as notas

**Resultado esperado**

Que os pedidos realizados pelo pronta entrega emita as notas

**Diagnostico e orientacao**

Geralmente quando dá esse erro de geração de nota é alguma questão de cadastro que faltou no Winthor. Isso não é parte da Máxima o cliente precisa verificar no Winthor com a TOTVs se necessário

Da nossa parte, sempre orientar o cliente a verificar na rotina de faturamento se está emitindo a nota de fato. Se NÃO der erro na geração da nota na rotina de faturamento, então pode ser alguma questão nossa. Mas como no caso a gente não fez nenhuma intervenção e o pedido foi processado com sucesso então foi uma questão de demora ou problema na primeira tentativa de geração da nota no ERP

Se o Sefaz demorar para gerar a nota dá esse erro também de timeout, ou também quando não gera a nota com sucesso

Quando dá erro assim no pedido o RCA pode reenviar o pedido, porque assim, caso a nota esteja gerada a gente vai buscar de novo. Ou então ele pode duplicar ou editar e enviar de novo o pedido

# GATE-781 - divergencia de comportamento de exibição de preço min/max entre tipos de venda

**Contexto**

Ao validarmos o relato do cliente abaixo

parâmetro?

Ocorre a seguinte situação ao emularmos esse cenário

Tipo normal

!image-2025-02-12-16-09-51-519.png|width=296,height=527!

Tipo balcão reserva

!image-2025-02-12-16-13-39-786.png!

Se perceberem ao comparar as 4 imagens, apenas na V2 pedido normal que é exibido os valores de 11.50, porém o cliente retorna que esse é o valor correto que deve ser ai apresentado. A unica politica presente para o item é essa

!image-2025-02-12-15-53-33-086.png!

!image-2025-02-12-15-53-49-577.png!

Nesse cenário, o que pode estar gerando aquele valor diferente de 11,50 que o cliente informa ser o valor correto a ser exibido, uma vez que não identifiquei registros de configuração ou parâmetro que criem aquele valor? mesmo a V2 não traz outra politica presente, mas apenas a politica do print acima

**Passos para reproduzir**

- cliente: 1328
- cobrança: dinheiro
- plano de pagamento: 75
- produto 50
- iniciar um pedido normal, buscar pelo item e observar o valor presente no campo Preço Min/Max
- iniciar um pedido balcão reserva e fazer o mesmo fluxo( há dois videos desse fluxo)

**Resultado apresentado**

divergencia de preço min/max entre versões e entre tipo de venda normal e balcão reserva

**Resultado esperado**

segundo o cliente, o valor correto que deve ser exibido são os 11,50 que constam no pedido normal da V2

**Diagnostico e orientacao**

Preco Min/%

O preço mínimo que está sendo apresentado na forma de Pedido Normal está vindo de uma permissão de desconto que o RCA possui na tabela MXSTABPR no campo PERDESCMAX no valor de desconto de 3.17

No caso do balcão reserva o sistema valida o campo PERDESCMAXBALCAO. Isso o sistema sempre fez desde 2016 tem isso no fonte. Então como esse campo na MXSTABPR está vazio, ele pega o percentual de desconto da política 0.78% para aplicar e considerar como preço mínimo

Para resolver eles teriam que mandar esse campo preenchido via integração para a gente (PERDESCMAXBALCAO)

# GATE-783 - Não permite transferir o saldo de conta corrente

**Contexto**

Não está permitindo transferir o saldo de conta corrente tanto no PWA quanto no web

**Passos para reproduzir**

- Acessar o MaxGestão
- Ir na parte de transferir o saldo de conta corrente
- Tentar transferir o saldo de qualquer vendedor
- E assim irá ver que não deixa transferir e retorna erro

**Resultado apresentado**

Não permite transferir saldo de conta corrente

**Resultado esperado**

Que permita transferir o saldo de conta corrente

**Diagnostico e orientacao**

Identificado que o extrator do cliente estava apontando para a API antiga, por esse motivo não ocorria a movimentação de conta corrente

Então foi feita alteração no Extrator do cliente para a API intpdv-unificado e após isso, realizados os testes e a tranferência voltou a funcionar com sucesso

# GATE-793 - Pedidos salvo e bloqueado entrando no fluxo da API de cancelamento no momento de editar

**Contexto**

Pedidos que estão salvos e bloqueados ao editar está entrando no fluxo da API de cancelamento. Se o pedido está salvo e bloqueado e ele for editado não deveria entrar no fluxo da API de cancelamento

**Passos para reproduzir**

- Acessar o aplicativo
- Iniciar um pedido em qualquer cliente
- Salvar e bloquear pedido
- Ir na tela de pedidos
- Editar o pedido que está salvo e bloqueado
- Salvar e enviar o pedido
- E assim irá ver que ao enviar o pedido retorna uma crítica informando que não foi possível autenticar na API de cancelamento do winthor

**Resultado apresentado**

Pedido salvo e bloqueado ao ser editado está entrando no fluxo da API de cancelamento do winthor

**Resultado esperado**

Que o pedido salvo e bloqueado ao ser editado não entre no fluxo da API de cancelamento

**Diagnostico e orientacao**

Será encaminhado para N3 porque está induzindo o usuário ao erro. O comportamento correto seria ao editar um pedido salvo e bloqueado, se o usuário salvar e enviar o pedido, ele entra em fluxo normal de envio, sem passar pelo WTA

Só deve entrar em fluxo de WTA caso o pedido já esteja salvo e enviado e respeitando demais regras (não pode editar/cancelar pedido faturado ou montado)

# GATE-794 - Coordenadas clientes

**Contexto**

Cliente quer usar as coordenadas cadastradas no Roteirizador no maxPedido

**Passos para reproduzir**

- Cliente utiliza o roteirizador e gostaria de importar as coordenadas ja utilizadas para o maxPedido

**Resultado apresentado**

Cliente utiliza o roteirizador e gostaria de importar as coordenadas ja utilizadas para o maxPedido

**Resultado esperado**

Cliente utiliza o roteirizador e gostaria de importar as coordenadas ja utilizadas para o maxPedido

**Diagnostico e orientacao**

Conforme citei no GATE-795, isso se trata de uma melhoria se o cliente quiser fazer isso de forma independente dentro dos sistemas da Máxima

Outra opção que eles tem é contruir integração para enviar os dados do ERP: Máxima

# GATE-795 - Coordenadas clientes

**Contexto**

Cliente utiliza roteirizador e gostaria de importar as coordenadas dos clientes para o maxPedido

**Passos para reproduzir**

- Cliente utiliza roteirizador e gostaria de importar as coordenadas dos clientes para o maxPedido

**Resultado apresentado**

- Cliente utiliza roteirizador e gostaria de importar as coordenadas dos clientes para o maxPedido

**Resultado esperado**

- Cliente utiliza roteirizador e gostaria de importar as coordenadas dos clientes para o maxPedido

**Diagnostico e orientacao**

Não se trata de um erro, o cliente não cadastrou as coordenadas no nosso endpoint MXSCLIENT e atualmente eles teriam de fazer isso manualmente via Central de Configurações do maxPedido, ou através de integração com o ERP, sendo do ERP: Máxima

Com as coordenadas cadastradas, os RCAs precisam sincronizar o maxPedido, e então vão receber os dados que o sistema usa para validar localização do RCA e comparar na hora de realizar o Check-in/Check-out com Raio

Para resolver definitivamente, é necessário o cliente construir uma integração que envie esses dados para Máxima. Eles podem por exemplo, pegar as coordenadas que vamos transferir para a tabela MXSCLIENT e guardar no ERP e depois enviar no mesmo endpoint

Outra opção que eles teriam é solicitar uma melhoria, porque essa movimentação de dados que vou fazer no banco de dados nuvem será manual e não existe uma automação nos sistemas da Máxima para isso

Paliativamente então foi feita transferência dos dados das coordenadas do Roteirizador para o endpoint MXSCLIENT através do banco de dados nuvem, dessa forma os RCAs podem sincronizar os dados no maxPedido. Observação importante: Se o ERP sobrescrever a informação do endpoint MXSCLIENT nos campos LATITUDE e LONGITUDE, os dados das coordenadas serão novamente perdidos

# GATE-799 - Comissão divergente do resumo de vendas e Winthor

**Contexto**

A comissão apresentada acima do gráfico na tela inicial apresenta um valor divergente do que é apresentado no resumo de vendas/Winthor. O valor diverge entre informações do próprio maxPedido

prints dos valores apresentados ontem e prints dos valores apresentados hoje

Na tela inicial: R$1060,00
No Resumo de vendas/Winthor: 1614,54

**Passos para reproduzir**

- Logar no maxPedido
- Buscar resumo de vendas
- Verificar campo "Prev. Comissão de venda
- Atualizar menu na tela inicial
- Verificar campo "Comissão

**Resultado apresentado**

O valor diverge entre informações do próprio maxPedido

**Resultado esperado**

Valores iguais

**Diagnostico e orientacao**

Na tela a informação de comissão bate com o resumo de vendas, porém o filtro selecionado deve ser "Mês atual", ocorre tanto na tela inicial e no resumo agora o RCA pode escolher o filtro referente aos dados apresentados

O script que gera a informação tela inicial da Comissão no nosso backend vem do
SELECT * FROM MXSSCRIPTS m WHERE OBJETO LIKE '%REQ_MXSRESUMOVENDASDETALHE%'
MXSRESUMOVENDASDETALHE | REQ_MXSRESUMOVENDASDETALHE | REQUEST

É a soma do campo VLCOMISSAOVENDA

Já sobre a do Resumo de vendas, vem do script SELECT * FROM MXSSCRIPTS m WHERE OBJETO LIKE '%REQ_MXSRESUMOVENDAS%'

MXSRESUMOVENDAS | REQ_MXSRESUMOVENDASE | REQUEST

E todos rodam diretamente no banco local e podem ser comparados somente à Rotina 1249

- Há casos que as notas podem estar divergentes e pode ser necessário recálculo das notas

A comparação da comissão do aplicativo com a comissão da rotina 1248 não é válida porque a aplicação não valida comissão por liquidez, somente a comissão 'pura', enquanto nessa rotina do Winthor são validadas devoluções e outros fatores de deduções do Winthor

O que geralmente os clientes fazem é criar um relatório na rotina 800 que traz a informação pro rca, aí ele consegue emitir diretamente pelo apk e não vai haver divergência dos valores

# GATE-804 - Diminuir o tamanho da tabela AD_MAXIMALOG

**Contexto**

O cliente precisa reduzir o tamanho da tabela AD_MAXIMALOG

**Passos para reproduzir**

- Nenhum passo foi feito

**Resultado apresentado**

Nenhum passo foi feito

**Resultado esperado**

Nenhum passo foi feito

**Diagnostico e orientacao**

Nesse caso, como a situação é com a Sankhya, então nós temos um processo diferente de abertura do chamado
1° Você deve Ficar com o ticket em N1 aberto e trocar a Natureza dele para Integração

2° Depois deve ir no link e abrir um ticket em nome do cliente Silbas

>> Login: maxima.integracao@maximatech.com.br
>> Senha: InteMax@Tech2610

Observações
Quando for mandar ticket para a integração, é necessário colocar a natureza do ticket pai como integração (não conta SLA)
Não falar para o cliente que o problema está na integração (falar que o ticket está indo para DEV)
Colocar o telefone do cliente no ticket para a SANKHYA, e também o seu telefone corporativo mesmo
>> No ticket você coloca as evidências que o cliente te passou do Sankhya e explica a situação em detalhes referente o que o cliente precisa

3° Depois de aberto o chamado SANKHYA, ir no chamado original N1 > Mais > Link > Link da WEB > Colocar link do chamado da SANKHYA

No Gatekeeper a gente não intervém nesse cenário, você fica com o ticket principal MXPED-66603 em N1 mesmo, (não manda para N3), e deixa ele em aberto e vincula ele conforme o processo de abertura para a devStudio

Assim você consegue se comunicar com o Felipe da Sankhya que é responsável pelas análises na parte da Sankhya

Contatar o Felipe Integração +55 27 98843-1292 E mencionar para ele no whats-app o chamado

# GATE-812 - Relatório Clientes sem vendas não gera dados

**Contexto**

Subindo gate depois de alinhado com o gatekeeper Filipe Padilha

Ao tentar gerar o relatório de Clientes sem vendas no portal executivo do maxGestão, independente dos filtros escolhidos não é gerado nenhum dado no relatório

**Passos para reproduzir**

- Acessar portal executivo
- Buscar relatório de clientes sem vendas
- tentar gerar relatório

**Resultado apresentado**

Não é gerado nenhum dado para nenhum filtro inserido

**Resultado esperado**

Relatório gerando dados

**Diagnostico e orientacao**

O relatório 'Relatório Clientes sem vendas' inicialmente utiliza essa consulta para carregar o grid de informações

SELECT DISTINCT mxsclient.codcli,P.codusur,P.codsupervisor, mxsclient.cliente, mxsclient.fantasia,mxsclient.telent
mxsclient.dtultcomp, mxsclient.bloqueio,mxsclient.obs, mxspraca.praca
FROM mxsclient
mxspraca
mxsusuari P
mxsvclientesrca
mxshistoricopedc
WHERE mxspraca.codpraca = mxsclient.codpraca
AND mxsclient.codcli = mxsvclientesrca.codcli
AND P.codusur = mxsvclientesrca.codusur
AND P.codsupervisor IN (SELECT keydados
FROM mxacessodados
WHERE coddados = 5
AND codusuario = :codusuario)
AND TRUNC(MXSHISTORICOPEDC.data) BETWEEN TO_DATE('01/02/2025','DD/MM/YYYY') AND TO_DATE('14/02/2025','DD/MM/YYYY')
AND ((trunc(sysdate) - MXSHISTORICOPEDC.data) <= :VNUMDIAS)
ORDER BY mxsclient.cliente

Nessa consulta, se você preencher e executar ela, verá que o codusuario 107133 não retorna dados. Isso ocorre porque ele só possui acesso à equipe 2700

Nessa equipe 2700, só tem 1 RCA vinculado, e esse RCA não possui vendas registradas em históricos

Se você pegar por exemplo o nosso usuário sysmax e utilizar o mesmo relatório, verá que carregam dados, porque o Sysmax possui acesso à todas as equipes que possuem RCAs com vendas

Possível solução

O usuário precisa ter acesso a equipes onde existam RCAs vinculados a clientes e esses RCAs tenham vendido para os clientes, porque o que o relatório basicamente faz, é analisar os históricos de vendas dos RCAs, considerando, Supervisor e clientes

Outra coisa que eu observei, o usuário em questão é o HIMALAIA.2500 PAULO CEZAR REIS DO AMARAL e nas permissões dele, ele só possui acesso à equipe 2700, sendo que a equipe dele próprio, seria a 2500, talvez se só mudar essa permissão, ele já consiga tirar o relatório que precisa

# GATE-814 - alteração de data final de campanhas de desconto escalonado

**Contexto**

Segue solicitação do cliente

Preciso que todos os DESCONTOS ESCALONADOS, com vigência ou data final que estão até 31/12/2025, fiquem com a data final igual a 17/02/2025
Hoje iniciamos novas escalonadas que estão com vigência de hoje, 18/03/2025 até 03/03/2025 e estas devem ser mantidas
O motivo desta solicitação é para não gerar conflitos nos descontos escalonados

!image-2025-02-18-08-53-23-104.png!

!image-2025-02-18-08-53-51-887.png!

Com base nisso, o cliente solicita que seja realizada alteração manual em banco, alterando as campanhas de desconto escalonada que tem uma data final de 31/12/2025 para a data de 17/02/2025. O mesmo precisa manter essas campanhas na base, mas que tenham uma data final menor que a data atual e essa operação a central não permite a execução

**Passos para reproduzir**

- Conforme descrição

**Resultado apresentado**

o cliente tentou alterar a data final das campanhas de desconto escalonado para uma data menor da data atual, mas a central não permite essa ação

**Resultado esperado**

ele espera que seja efetuada a alteração dessa data via banco

**Diagnostico e orientacao**

Foi feita a inativação por data de vigência das campanhas seguindo esse critério para o UPDATE

SELECT * FROM MXSDESCESCALONADOC WHERE TRUNC(DTFIM) = TO_DATE('17/02/2025','DD/MM/YYYY')

Assim as campanhas deixam de ser enviadas para o maxPedido pois uma job nossa lê as vigências e atualiza o campo enviafv para = 'N'

Para validar os RCAs devem estar sincronizando o maxPedido

Se o cliente quiser alguma alteração da regra de negócios do sistema, se encaixa em cenário de melhoria

# GATE-816 - observação padrão em pedido

**Contexto**

fiz algumas consultas no ambiente do cliente, bases de conhecimento e tickets o JIRA, mas não identifiquei algo que se aproxime da necessidade do cliente

Existe alguma funcionalidade no aplicativo que permita cadastrar observações padrões por clientes de modo que cada vez que um vendedor digitar um pedido essa observação entre no pedido ?

**Passos para reproduzir**

- conforme descrição

**Resultado apresentado**

conforme descrição

**Resultado esperado**

conforme descrição

**Diagnostico e orientacao**

Dado o contexto do ticket, eu analisei e encontrei essas seguintes opções

- Essa parte só funcionou na v4 durante os meus testes

Teria como mostrar o campo
OBS2 que vai cadastrado na MXSCLIENT
Porém ele depende dos parâmetros HABILITAR_OBSERVACOES_CLIENTE e CON_GRAVAROBSCLIENTENOPEDIDO estarem ambos ativos; sendo o HABILITAR_OBSERVACOES_CLIENTE da MXSPARAMETRO e o CON_GRAVAROBSCLIENTENOPEDIDO da MXSPARAMFILIAL

- Essa parte funcionou na v3.264.0 e na v4

No pedido, para ter observações fixas por cliente sempre que inicia o pedido, é só cadastrar os campos
OBSENTREGA1 = ex 'ENTREGAR RUA XXXXX N 25434'
OBSENTREGA2 = ex '1542132'
OBSENTREGA3 = ex 'CELULAR 9999999999'

Preenchendo os dados de OBS1,2,3,4 e 5 do cliente, vai aparecer na aba Inf. Cliente (Informações do cliente) no card "Outros

# GATE-822 - Venda transmitida

**Contexto**

O valor exibido na *tela inicial* da venda transmitida está *divergente* do valor apresentado no *resumo de vendas*

**Passos para reproduzir**

- Valor na venda transmitida presente na tela inicial está divergente do valor no resumo de vendas
- Na base do zero foi apresentado o valor exibido corretamente na tela inicial e no resumo de vendas
- A divergência ocorre apenas na base do RCA

**Resultado apresentado**

> Valor na venda transmitida presente na tela inicial está divergente do valor no resumo de vendas

**Resultado esperado**

> Valor que apresenta no resumo de vendas ser o mesmo que apresenta na tela inicial

**Diagnostico e orientacao**

Será encaminhado para desenvolvimento N3, porque pelo o que eu observei, tem dados duplicados na base do RCA, por isso as informações são apresentadas inconsistentes nos gráficos

Paliativamente eu já mandei apagar as duplicidades, então para resolver o problema do usuário, basta ele mandar atualizar o menu que todos os gráficos serão atualizados com os valores corretamente

# GATE-823 - DANF-E não está integrando os dados presente na PCDOCELETRONICO

**Contexto**

vimos no banco local do cliente que mesmo com a tabela PCDOCELETRONICO preenchida, quando buscamos na ERP_MXSDOCELETRONICO não aparece nenhum dado

**Passos para reproduzir**

- NUMPED = 800017210
- NUMTRANSVENDA = 2030479

**Resultado apresentado**

Não é possível gerar com DANF-E
Ambiente já atualizado. Além disso, ao que parece não esta integrado em nosso banco

**Resultado esperado**

Conseguir gerar normalmente o DANF-E e ter as devidas informações na ERP_MXSDOCELETRONICO

**Diagnostico e orientacao**

Foi realizada normalização dos dados para descer a tabela PCDOCELETRONICO corretamente para o banco de dados nuvem. Conferi e agora os dados estão na ERP_MXSDOCELETRONICO corretamente. Na normalização eu também acatei outras notas que poderiam estar com problemas

Após a descida na ERP_MXSDOCELETRONICO, a nossa job rodou e gerou a tabela MXSDOCELETRONICO que o maxPedido utiliza para fazer a geração da nota

Para validar baixar uma base do zero e testar se gera corretamente o arquivo. No caso do RCA, é só ele sincronizar o maxPedido e realizar o teste

# GATE-831 - Supervisor não aparece no painel de auditoria

**Contexto**

O supervisor 2500-PAULO CEZAR REIS DO AMARAL não aparece no painel de auditoria para visualizar

Foi visto as permissões e os usuários tem acesso ao supervisor, mesmo assim não aparece

**Passos para reproduzir**

- Entra no MAXGESTÃO---GEOLOCALIZAÇÃO---PAINEL DE AUDITORIA
- Seleciona a filial 1
- Supervisor: era para aparecer o 2500-PAULO CEZAR REIS DO AMARAL

**Resultado apresentado**

Não aparece o supervisor

**Resultado esperado**

Que fosse possivel selecionar o supervisor

**Diagnostico e orientacao**

No maxGestão (Painel de Auditoria) existe uma regra onde, os usuários são apresentados conforme a filial vinculada no RCA do Supervisor
Abaixo vou explicar com exemplo para ficar mais claro

Na tabela MXSSUPERV existe o campo COD_CADRCA que é o usuário de vendas vinculado ao supervisor

No Painel de Auditoria todo Supevisor precisa ter seu usuário de vendas vinculado senão não carrega ele para ser selecionado no Painel

Esse campo COD_CADRCA referencia o CODUSUR da outra tabela MXSUSUARI

Além do vínculo que comentei, precisa ter outra configuração na tabela MXSUSUARI

O campo CODFILIAL da MXSUSUARI deve ser preenchido com o código da filial específica, ou se não tiver uma filial específica do usuário, pode ser o código 99 que indica todas as filiais

Compara como exemplo, dessa forma

SELECT * FROM MXSSUPERV WHERE CODSUPERVISOR IN(2500,1000)
SELECT * FROM MXSUSUARI WHERE CODUSUR IN(1000, 2500)

O supervisor 1000 é um que aparece normalmente porque segue esses critérios, então o 2500 precisa desses ajustes no cadastro

# GATE-833 - Roteiro anterior gerado incorretamente.

**Contexto**

Cliente relata que os compromissos de roteiros dos RCAs estão sendo apresentados incorretamente no apk
Foi verificado no codusur 120, ao consultar o roteiro de visita do dia anterior na base do rca, que os compromissos constavam de forma incoerente e desorganizados quando comparados com o roteiro gerado pelo roteirizador na tabela MXMI_AGENDA_RCA. No dia analisado ('19/02/2025') foram verificados mais de 100 compromissos para o RCA, sendo que o mesmo possuía apenas 10 clientes roteirizados no dia
Foi verificado também que não existem rotas geradas na ERP_MXSROTACLI
Foi verificado que para o dia atual, os compromissos são gerados corretamente conforme registros na MXSCOMPROMISSOS, entretanto ao observar os dias anteriores é verificado que são gerados compromissos duplicados na MXSHISTORICOCOMPROMISSOS
Com esse fluxo em mente, o cliente utiliza os parâmetros de justificativa de roteiro anterior, e devido ao problema que está sendo apresentado os rcas ficam impedidos de realizar vendas pois os compromissos gerados de forma incorreta do dia anterior ficam pendentes e o RCA não consegue acessar os clientes para justificar ou digitar um novo pedido

Login para teste
mix.120

**Passos para reproduzir**

- Entrar na base do RCA, verificar o roteiro de visitas do dia 19/02/2025
- Em seguida, realizar os seguintes selects no banco nuvem do cliente
- SELECT * FROM ERP_MXSROTACLI WHERE CODUSUR = 120 AND DTPROXVISITA >= '19/02/2025'
- SELECT * FROM MXMI_AGENDA_RCA WHERE ID_RCA = 120 AND INICIO_VISITA BETWEEN TO_DATE('19/02/2025', 'DD/MM/YYYY') AND TO_DATE('20/02/2025', 'DD/MM/YYYY') ORDER BY INICIO_VISITA ASC
- SELECT * FROM MXSCOMPROMISSOS WHERE CODUSUARIO = 64596 AND CODOPERACAO != 2 AND DTINICIO BETWEEN TO_DATE('19/02/2025', 'DD/MM/YYYY') AND TO_DATE('20/02/2025', 'DD/MM/YYYY') ORDER BY DTINICIO ASC
- SELECT * FROM MXSUSUARIOS WHERE CODUSUR = 120
- SELECT * FROM MXSVERSAOBD ORDER BY DTATUALIZACAO DESC
- SELECT * FROM MXSHISTORICOCOMPROMISSOS WHERE CODUSUARIO = 64596 AND CODOPERACAO != 2 AND DTINICIO BETWEEN TO_DATE('19/02/2025', 'DD/MM/YYYY') AND TO_DATE('20/02/2025', 'DD/MM/YYYY') ORDER BY DTINICIO ASC

**Resultado apresentado**

É verificado que nos dias anteriores ao dia atual (20/02/2025), são geradas visitas de forma inconsistente e aleatórias, impactando no fluxo de justificativa de roteiro

**Resultado esperado**

É esperado que os roteiros anteriores sejam gerados corretamente na MXSHISTORICOSCOMPROMISSOS e que o vendedor consiga iniciar novos pedidos corretamente

**Diagnostico e orientacao**

Os dados do cliente estava errados na tabela MXSHISTORICOCOMPROMISSOS, gerando vários compromissos de clientes não atendidos no roteiro anterior de forma inconsistente

Isso ocorria segundo o nosso dev backend devido a problemas de versões antigas do banco de dados

Então para resolver a situação foi feito o seguinte

Foi gerada uma normalização de todos os registros de históricos de compromissos baseando os dados nos compromissos ativos do dia 20/01/2025 até o dia 03/01/2025

Por que foi feito isso? Porque eles trabalham com o roteiro pendente somente do dia anterior, então se hoje é dia 21/02/2025, então eu só preciso do histórico normalizado do dia 20/02/2025 em diante

Até o dia 03/01/2025, provavelmente não ocorrerá mais nenhum problema, porque foi feita normalização de todos esses dados que era o máximo da data que havia compromisso gerado pela nossa job

Agora para resolver nos RCAs, eles apenas precisam estar sincronizando o maxPedido, ao fazer isso é esperado que eles recebam somente os compromissos pendentes do dia 20/02/2025 corretamente

É necessário monitorar se ocorrer algum problema, enviar outro gate, mas como expliquei, provavelmente, problema com os roteiros anteriores pode ocorrer só depois do dia 03/01/2025, (não é esperado que ocorra) porque houveram correções no backend, então a gente espera que os históricos sejam gerados corretamente daqui em diante, mas é necessário acompanhar

# GATE-841 - Mesmo com o novo cadastro, o cadastro temporário dos clientes não somem

**Contexto**

>>Mesmo com o campo CODFUNCULTALTER da MXSCLIENT preenchido e com os parâmetros HABILITA_PED_CLI_NAO_SINC e HABILITA_PED_CLI_RECEM_CADASTRADO ativos, os cadastros temporários de clientes não somem fazendo com que os clientes fiquem duplicados

**Passos para reproduzir**

- Baixar a base do RCA 355
- Ir até a aba clientes
- Usuário: tozzi.euler

**Resultado apresentado**

>>Mesmo ao sincronizar, ou fazer swipe na tela de pedidos e no gerenciar clientes os clientes ficam duplicados

**Resultado esperado**

>>Os clientes temporários deveriam sumir assim que o cadastro permanente fosse aceito pelo ERP

**Diagnostico e orientacao**

Foi feito um paliativo somente para o RCA do ticket codusuario (106237), quando ele sincronizar, os clientes temporários serão deletados da base do aplicativo dele assim ocultando os clientes recém cadastrados

Eu vou encaminhar o chamado para N3 de qualquer forma, para ser verificado o motivo para mostrar duplicado e esses clientes não estarem sumindo da base após receber o cadastro efetivo na MXSCLIENT

# GATE-854 - app travar a negociação na embalagem master

**Contexto**

ao analisar o cenário citado, o cliente necessita que alguns de seus RCAS negociem os seus produtos apenas com a embalagem master do mesmo. Realizamos a parametrização no usuário habilitando o parâmetro FORCAR_UNIDADE_MASTER_PRODUTO mas ainda assim a aplicação exibiu ambas as embalagens

!image-2025-02-25-08-29-00-801.png!

No cenário do cliente, qual a configuração que precisa ser realizada para que a aplicação se comporte com essa forma que o cliente deseja, para além do parâmetro citado?

**Passos para reproduzir**

- efetuar a negociação sobre o seguinte cenário
- filial 1
- e observar o campo da embalagem

**Resultado apresentado**

mesmo com o parametro habilitado a aplicação não está sendo forçada a utilizar a embalagem master do produto

**Resultado esperado**

é esperado que ao iniciar a negociação, o campo de embalagem esteja travado com a embalagem master do produto

**Diagnostico e orientacao**

Foi considerado o cenário que o cliente gostaria de trabalhar e também a forma que o aplicativo permite trabalhar atualmente

Então o que atenderia o cenário do cliente, ou seja, ele queria trabalhar de forma que o RCA pudesse vender somente uma embalagem específica do produto

Então eles teriam que configurar restrições de venda usando o conceito do CODAUXILIAR da embalagem que não poderá ser vendido, eles podem fazer via central ou Winthor

E também precisam que o parâmetro do maxPedido esteja marcado RESTRINGIR_PRODUTOS_391 = 'N' por default ele oculta os produtos com restrição de venda, e vem = 'S'

Outra possibilidade, seria trabalhar com a permissão Acesso ao controle de caixa fechada (Produto) = [X], ela força o RCA a vender o múltiplo cadastrado no campo QTUNITCX da MXSPRODUT

Qualquer cenário diferente desse seria uma melhoria

# GATE-856 - Relatório de entrada de produtos não apresenta dados

**Contexto**

Relatório de entrada de produtos não apresenta dados mesmo com registros na MXSESTPEND

Tambem foi verificados os registros locais na PCMOV e PCNFENT, que constam para a data selecionada, porem no relatório do portal executivo não retorna nenhum dado

Cliente TCLOUD
Senha maxsolucoes: sgzvc58629MWANS?@

HOST: 177.136.11.103
SERVICE: CTDQ2Z_186152_W_high.paas.oracle.com

**Passos para reproduzir**

- Verificar tabelas do banco nuvem e banco local

**Resultado apresentado**

Relatório não retorna dados

**Resultado esperado**

Relatório retornando dados

**Diagnostico e orientacao**

Foi verificado que o relatório utiliza dados da ERP_PCNFENT (PCNFENT) e ERP_MXSMOV (PCMOV) para gerar os dados, porém o parâmetro UTILIZA_GESTAO_LOGISTICA = N foi alterado no cliente em 15-FEB-25. Com o parâmetro = N os dados dessas tabelas não são integrados à Nuvem da Máxima

Nesse caso eu ativei o parâmetro diretamente no banco local dele via Winthor Nuvem na nossa tabela PCMXSCONFIGURACOES

E fiz a carga só desse Mês de fevereiro em todas as filiais que integram com a Máxima nas tabelas PCMOV e PCNFENT

Para validar é só esperar agora os registros terminarem de ser integrados

# GATE-858 - Clientes duplicados no banco nuvem

**Passos para reproduzir**

- Estou com uma situação que, alguns clientes da 969 - SUPERELIZEU estão com registros "duplicados" na MXSCLIENT, exemplo os clientes 77892, 77893, 78002, 78003
- Verifiquei no banco do Winthor que esses registros duplicados na nuvem não existem no banco local, no caso no banco local existem somente os clientes 77892 e 78002 dos 4 citados
- Ao conversar com o cliente o mesmo informou que recentemente foi realizada uma migração vindo do Pedido de Vendas para o maxPedido, o que pode ter sido o causador da duplicidade desses registros
- Segundo o cliente, o problema afeta outros RCAs
- Acessar APK (base do zero)
- Observar os clientes que possuem registros duplicados (ex: 77892, 77893, 78002, 78003)

**Resultado apresentado**

Alguns clientes estão com registros "duplicados" na MXSCLIENT, exemplo os clientes 77892, 77893, 78002, 78003

**Resultado esperado**

Normalizar os registros

**Diagnostico e orientacao**

Foi feita normalização dos dados da tabela MXSCLIENT, durante o processo eu normalizei 190 de cadastros duplicados de clientes

A normalização consiste em igualar as informações com o banco do Winthor PCCLIENT = MXSCLIENT. E a integração está funcionando normalmente

Para os RCAs receberem a correção nos dispositivos, basta realizar a sincronização do maxPedido

# GATE-876 - Pedido bloqueado não pode ser editado

**Contexto**

Cliente relata que o vendedor 253, ao editar o pedido NUMPEDRCA 253003848 a apk retorna a mensagem de que não é possível editar pedido já enviado. Entretanto, ao olhar o pedido na integração, é verificado que o pedido consta com o status 6 (bloqueado)
Foi realizado teste na base do rca, onde foi verificado que ao liberar a permissão 'Permite editar pedidos já enviados' na Central de Configurações, a aplicação permitiu editar o pedido normalmente
À priori, trata-se de uma falha da apk, pois o pedido em questão ainda não foi enviado para o ERP, e pelo fato do cliente trabalhar com a API de cancelamento pode causar problemas nos fluxos e regras internas do cliente

Verificado com o P.O Cleyton que trata-se de um erro, encaminhado ao gate para análise

Login para teste
amorix.253

**Passos para reproduzir**

- Entrar na base do rca, procurar o pedido NUMPEDRCA 253003848 e tentar editá-lo

**Resultado apresentado**

Ao realizar a ação, a apk retorna a mensagem de que não é possível editar um pedido já enviado, entretanto o pedido consta como bloqueado no apk
Ao habilitar a permissão 'Permite editar pedido já enviado' na Central de Configurações

**Resultado esperado**

É esperado que o vendedor consiga realizar a edição do pedido bloqueado sem a permissão em questão

**Diagnostico e orientacao**

- Ao atualizar a versão do aplicativo identifiquei que o funcionamento está normalizado, ao editar pedidos, não ocorre a mensagem impedindo

# GATE-882 - problemas de configuração para funcionamento API De estoque online SANKHYA

**Contexto**

ao analisarmos o cenário relatado pelo cliente, estamos verificando que a sua atualização estoque não está ocorrendo regularmente, conforme aqui indicado

!image-2025-02-27-10-12-32-061.png!

essa situação vem ocorrendo devido ao TOKEN que o cliente possui cadastrado em seu ambiente de homologação: !image-2025-02-27-10-13-27-153.png!

o qual é reportado estar invalido

!image-2025-02-27-10-14-05-734.png!

Em contato junto ao cliente, o mesmo reportou que essa situação ocorre devido ao ambiente de homologação do sankhya apontar para outra URL e outro tipo de ambiente e as configurações do APPKEY e URL da maxima apontam para o cenário de produção. Vide áudios onde o cliente descreve essa questão

Como proceder com essa configuração? Na biblioteca da maxima em que nos baseamos para analise desse cenário, não estou identificando informações necessárias para proceder com a analise dessa questão, uma vez que não é citado qual a configuração que precisamos alterar para apontar ao ambiente de sanbox ou teste do cliente

Obs.: o ambiente de produção opera regularmente onde apenas o ambiente de homologação que apresenta a falha aqui relatada

!image-2025-02-27-10-22-43-932.png!

**Passos para reproduzir**

- fazer a validação conforme a descrição

**Resultado apresentado**

o token gerado pelo cliente não é valido para a atualização de estoque
Segundo o cliente, isso acontece por questões de URL e appkey que a maxima usa apenas do ambiente de produção

**Resultado esperado**

é esperado que o token citado seja validado normalmente e sem falhas

**Diagnostico e orientacao**

Dentro do maxPedido só existe integração direta com o link de produção da Sankhya

A URL é fixa no código do maxPedido, não é parametrizável. Então atualmente não teria como o cliente operar em ambiente de teste usando o maxPedido e o ambiente de HMG

Precisaria ser tratado como melhoria para mapear a questão de mudança do APPKEY e também da URL que é diferente na homologação da Sankhya
Link do HMG

Uma alternativa seria ele usar o ambiente de produção mesmo para realizar os testes com 1/dois usuários de teste ou até de produção

# GATE-893 - duplicidade de pedidos

**Contexto**

o cliente 746 - MEGA DISTRIBUIDORA está com a mesma situação de duplicidade que foi apresentada na demandas GATE-892, GATE-869, GATE-843 e GATE-777 onde realizamos a atualização do ambiente do cliente mas há a necessidade do envio da carga de dados com o script que corrige a tabela MXSHISTORICOPEDC

!image-2025-02-28-12-18-04-910.png!

**Passos para reproduzir**

- efetuar a carga para aplicação normalizar os registros duplicados

**Resultado apresentado**

pedidos em duplicidade no historico

**Resultado esperado**

que não sejam apresentados registros duplicados

**Diagnostico e orientacao**

Foi feita a normalização das bases dos RCAs, para validar o cliente e RCAs só precisam sincronizar o maxPedido

Visto que estamos tendo vários casos como esse, eu solicitei ao dev que adicione a tratativa no atualizador do maxPedido, não é garantido que vão colocar ainda, depois eu trago a notícia, mas essa parte de identificar a necessidade e solicitar foi feita

# GATE-896 - Ativar sincronização automática

**Contexto**

>>O cliente deseja ativar a sincronização automática para o RCA 366 e segundo o gate Filipe agora devemos enviar a demanda para gatekeeper pois não podemos mais ativar o parâmetro na central de configurações

**Passos para reproduzir**

- Tentar ativar a sincronização automática para o cliente(Setar OCULTO = N no banco nuvem)

**Resultado apresentado**

>>Não é mais possível alterar o parâmetro assim como prints apresentados

**Resultado esperado**

>>Ativar a sincronização automática para o RCA 366 para testes

**Diagnostico e orientacao**

Feita ativação da sincronização automática diretamente via banco no usuário 104944

# GATE-898 - Pedidos do dia 28/02/2025 não aparece no palm

**Contexto**

Analisado com o vendedor no dia 28/02/2025 e verificando todos os filtros, os pedidos do dia 28 não aparece no palm do mesmo, porém ao importar a base do vendedor em meu aparelho, aparece todos os pedidos feito nesse dia. Fiz o teste na ponta e tambem na versão do vendedor ou outro teste em outra versão, na V3 ainda e com ele continua sem aparecer os pedidos e no meu equipamento aparece

**Passos para reproduzir**

- 1-Entrar com o usuario gigavale.guilherme
- 2-Importar a base que
- 3-Consultar os pedido feitos do dia 28/02/2025

**Resultado apresentado**

Na importação da base no meu aparelho mostrar todos os pedidos, porém no aparelho dele não mostra

**Resultado esperado**

Mostra-se os pedido do dia 28 no aparelho do vendedor

**Diagnostico e orientacao**

Ao acessar a base do RCA, conforme descrito, realmente não há problemas na exibição dos pedidos, eles constam na base do RCA e portanto ao filtrar corretamente na timeline são exibidos sem problemas

Nesse contexto, para ser um problema, ele precisa ser simulável. No vídeo que o cliente colocou no ticket principal, dá para observar que o RCA estava usando de filtros na timeline de pedidos aba (Pedidos), onde ele estava filtrando para mostrar somente Orçamentos, então pode estar ocorrendo uma dificuldade de uso do aplicativo, mas não há evidências de aparentes problemas

Nesse caso eu recomendo os seguintes procedimentos
1° Limpar os filtros da Timeline de Pedidos. Apesar de a limpeza resolver 95% dos casos, pode ter um caso de o filtro não ter sido limpo completamente por causa de algum problema de versão, então recomendo revisar todos os filtros referentes a datas e os tipos de pedidos que estão sendo apresentados. A maiora dos casos de problema de pedido que não aparece simplesmente é o usuário realizando filtros que depois não altera mais (Data Prevista Faturamento) são os casos mais comuns

2° Reestruturar o banco do aplicativo em Ferramentas: Reestruturar Banco

3° Se o usuário apagou os pedidos (o que é uma possibilidade em alguns casos) ele pode restaurar a timeline usando o parâmetro PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO = S
Depois de ativo ao sincronizar busca e restaura o histórico de pedidos na timeline

4° Atualizar a versão do maxPedido e limpar os filtros

5° Se o problema persistir será necessário o cliente fornecer um cenário consolidado, com vídeo e a base problemática do RCA. Em último caso dá para fazer uma conexão remota no aparelho do RCA para identificar a real causa dos pedidos não estarem sendo exibidos

# GATE-899 - Validar cálculo do painel geral

**Contexto**

Gostaria de ajuda para que fosse validado se o cálculo feito pelo maxGestão para exibir o Painel Geral está correto, uma vez que o cliente mostrou não estar batendo com o ERP

Tentei rodar o SQL do painel geral porém mesmo trocando o CODUSUARIO e as datas o SQL retorna 0 pra mim

Com o cálculo estando correto e batendo com o maxGestão podemos evidenciar ao cliente que estamos apenas exibindo o que chegou do ERP via API de integração

**Passos para reproduzir**

- Acessar maxGestão
- Painel Geral
- Filtrar 01/02/2025 até 28/02/2025
- Todos tipos de venda, pedidos e clientes
- Deduzir devoluções
- Observar o valor apresentado no painel geral
- Observar no o valor apresentado no ERP
- OBS: Segundo o cliente, o valor que mais se aproxima é quando o filtro é feito por data de faturamento do pedido

**Resultado apresentado**

O valor do painel geral do Gestão está maior do que no ERP

Validei o valor das devoluções e a diferença entre o ERP e o painel geral é de apenas R$ 560

Já a diferença no valor das vendas é em torno de R$ 72 mil

**Resultado esperado**

Gostaria de ajuda para que fosse validado se o cálculo feito pelo maxGestão para exibir o Painel Geral está correto, uma vez que o cliente mostrou não estar batendo com o ERP

**Diagnostico e orientacao**

- Nos eu coloquei as planilhas com os cálculos por pedido dentro do período selecionado, esperamos que com esses dados o ERP faça uma apuração dos dados internos do banco do ERP e também consiga comparar com os dados enviados para o nosso banco via API, para que assim possam identifiar as divergências e realizar o entendimento de como calculamos

- OBS: não passar as consultas inteiras da Máxima, só alguns detalhes, as consultas são propriedades intelectuais da Máxima

- VALOR SEM DEDUZIR = 2006552.19
- VALOR DAS DEVOLUCOES = 6.984.31
Você pode fazer assim SELECT (2006552.19 - 6984.31) FROM DUAL; (terá o resultado do painel de auditoria)

- Como apuramos para chegar nessa informação consulta somente da parte de venda transmitida

SELECT
- Soma do QT * PVENDA, excluindo certas condições de venda e arredondando para 2 casas decimais
SUM(NVL(DECODE(VENDAS.CONDVENDA, 6, 0, 11, 0, 12, 0, ROUND((ITEMPED.QT * ITEMPED.PVENDA), 2) - 0 - 0), 0)) - 0 AS VALORTOTAL
FROM
MXSHISTORICOPEDC VENDAS
- Faz a junção com a tabela de itens do pedido, garantindo que o pedido exista na MXSHISTORICOPEDC
INNER JOIN MXSHISTORICOPEDI ITEMPED ON VENDAS.NUMPED = ITEMPED.NUMPED
- Faz a junção com a tabela de usuários para validar a existência do RCA
INNER JOIN MXSUSUARI US ON VENDAS.CODUSUR = US.CODUSUR
- Faz um LEFT JOIN para trazer dados da MXSINTEGRACAOPEDIDO se houver correspondência
LEFT JOIN (
- Seleciona pedidos distintos da MXSINTEGRACAOPEDIDO com supervisores válidos dentro do período
SELECT DISTINCT NUMPEDERP, CODSUPERVISOR, CODUSUR
FROM MXSINTEGRACAOPEDIDO
WHERE CODSUPERVISOR IS NOT NULL
- Filtra por datas dentro do mês de fevereiro de 2025
AND TRUNC(DATA) BETWEEN TO_DATE('01/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
AND TO_DATE('28/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
- Garante que o usuário tenha permissão de acesso aos dados do supervisor e filial
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '80445' AND CODDADOS = '5' AND MXSINTEGRACAOPEDIDO.CODSUPERVISOR = KEYDADOS)
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '80445' AND CODDADOS = '6' AND MXSINTEGRACAOPEDIDO.CODFILIAL = KEYDADOS)
AND CODSUPERVISOR IS NOT NULL
) MXSI ON MXSI.NUMPEDERP = VENDAS.NUMPED AND MXSI.CODUSUR = VENDAS.CODUSUR
WHERE
- Exclui certos tipos de condição de venda
VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)
- Considera apenas pedidos que não foram cancelados
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
- Filtra pedidos criados dentro do período de fevereiro de 2025
AND TRUNC(VENDAS.DATA) BETWEEN TO_DATE('01/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
AND TO_DATE('28/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
- Garante que o usuário tenha acesso à filial do pedido
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '80445' AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)
- Valida acesso ao supervisor do pedido
AND EXISTS(
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445' AND KEYDADOS = VENDAS.CODSUPERVISOR
UNION ALL
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445' AND KEYDADOS = MXSI.CODSUPERVISOR AND VENDAS.CODSUPERVISOR IS NULL
)
- Exclui operações canceladas
AND VENDAS.CODOPERACAO <> 2
AND ITEMPED.CODOPERACAO <> 2
- Exclui pedidos e itens com posição cancelada
AND VENDAS.POSICAO <> 'C'
AND NVL(ITEMPED.POSICAO, 'L') <> 'C'
- Filtra apenas pedidos com condição de venda igual a 1
AND VENDAS.CONDVENDA IN (1)

- Basicamente pegamos a soma dos itens dos pedidos da MXSHISTORICOPEDI e fazendo validações com a MXSHISTORICOPEDC sendo
- MXSHISTORICOPEDI a soma do QT * PVENDA com arredondamento de 2 casas decimais
- Validando se o pedido existe na MXSHISTORICOPEDC
- Apura só os dados que foram filtrados e que o usuário possui acesso quanto à equipes e Filiais

- Reduzi ela para ficar mais fácil de entender

SELECT VENDAS.NUMPED
SUM(NVL(DECODE(VENDAS.CONDVENDA, 6, 0, 11, 0, 12, 0, ROUND((ITEMPED.QT * ITEMPED.PVENDA), 2) - 0 - 0), 0)) - 0 AS VALORTOTAL
FROM
MXSHISTORICOPEDC VENDAS
INNER JOIN MXSHISTORICOPEDI ITEMPED ON VENDAS.NUMPED = ITEMPED.NUMPED
INNER JOIN MXSUSUARI US ON VENDAS.CODUSUR = US.CODUSUR
WHERE
VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND TRUNC(VENDAS.DATA) BETWEEN TO_DATE('01/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
AND TO_DATE('28/02/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '80445' AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)
AND EXISTS(
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445' AND KEYDADOS = VENDAS.CODSUPERVISOR
)
AND VENDAS.CODOPERACAO <> 2
AND ITEMPED.CODOPERACAO <> 2
AND VENDAS.POSICAO <> 'C'
AND NVL(ITEMPED.POSICAO, 'L') <> 'C'
AND VENDAS.CONDVENDA IN (1)
GROUP BY VENDAS.NUMPED

- Eles teriam que pegar esses pedidos e fazer um cálculo interno NO ERP agrupando por pedido assim para comparar com o que eles enviam para a gente via integração e assim identificar os pontos de divergência para mandar a correção dos envios dos dados para a nossa nuvem

- Para o cálculo das devoluções considera as datas da DTENT da ERP_MXSNFENT

Considera pedidos com CONDVENDA que não sejam de 6 e 11 da tabela

Considera a QT * PUNIT do endpoint ERP_MXSMOV

Também só apura dados de devolução através do conceito

AND ERP_MXSMOV.CODOPER = 'ED'

Se precisar de mais detalhes de como é apurada a devolução tem no script explicando ponto a ponto, mas basicamente eles já fazem o envio desses dados da integração deles, eles só precisam verificar se tem alguma informação que não está sendo enviada para a nossa nuvem em conformidade

Se eles precisarem de como a informação está gravada em algum endpoint específico você pode consultar e mandar para eles, às vezes a divergência pode estar sendo causada porque uma devolução está sem, por exemplo, o conceito de AND ERP_MXSMOV.CODOPER = 'ED' definido no registro

Se precisar ainda tirar mais dúvidas comigo sobre esse assunto e analisar mais algum detalhe pode me chamar diretamente que eu analiso

WITH AA AS (
- Seleciona os dias úteis dentro do período especificado
SELECT A.DATA
FROM MXDIASUTEIS A
WHERE DATA BETWEEN TO_DATE('01/02/2025', 'dd/mm/yyyy') AND TO_DATE('28/02/2025', 'dd/mm/yyyy')
GROUP BY A.DATA
)

B AS (
- Relaciona cada dia útil ao seu respectivo mês/ano
SELECT DIAUTIL, TO_CHAR(A.DATA,'MM/YYYY') AS DATA
FROM MXDIASUTEIS A
JOIN AA ON A.DATA = AA.DATA
)

A AS (
- Calcula o valor total das devoluções dentro do período
SELECT
DEVOL.DATA AS DATA
DECODE('S','N',0,SUM(DEVOL.VLDEVOLUCAO - 0 - 0 - DEVOL.VLREPASSE)) VLTOTAL
FROM (
- Obtém valores das notas fiscais de entrada (devoluções)
SELECT TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY') AS DATA
NVL(
SUM(
CASE
- Exclui certas condições de venda
WHEN ERP_MXSNFSAID.CONDVENDA IN (6,11) THEN 0
ELSE
( NVL (ERP_MXSMOV.QT, 0) * ( NVL (ERP_MXSMOV.PUNIT, 0) +
NVL (ERP_MXSMOV.VLFRETE, 0) +
NVL (ERP_MXSMOV.VLOUTRASDESP, 0) +
NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) +
NVL (ERP_MXSMOV.VLOUTROS, 0)
NVL (ERP_MXSMOV.VLREPASSE, 0) ))
END
)
0
) AS VLDEVOLUCAO
- Calcula valores de ST, IPI e repasse
NVL(SUM(NVL (ERP_MXSMOV.QT, 0) * NVL (ERP_MXSMOV.ST, 0)),0) VLST
NVL(SUM(NVL(ERP_MXSMOV.VLIPI, 0) * NVL (ERP_MXSMOV.QT, 0)),0) VLIPI
NVL(ROUND(SUM(ERP_MXSMOV.QT * ERP_MXSMOV.VLREPASSE), 2), 0) VLREPASSE
FROM ERP_MXSNFENT
ERP_MXSESTCOM
ERP_MXSTABDEV
MXSCLIENT
MXSEMPR
MXSUSUARI
MXSSUPERV
MXSFORNEC F
ERP_MXSNFSAID
ERP_MXSMOV
MXSPRODUT
ERP_MXSDEVCONSUM
MXSHISTORICOPEDC VENDAS
WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT(+)
- Relaciona a devolução com a tabela de devoluções cadastradas
AND ERP_MXSNFENT.CODDEVOL = ERP_MXSTABDEV.CODDEVOL(+)
AND MXSCLIENT.CODCLI = ERP_MXSNFENT.CODFORNEC
AND ERP_MXSNFENT.NUMTRANSENT = ERP_MXSDEVCONSUM.NUMTRANSENT(+)
- Relaciona com motorista, usuários e supervisores
AND ERP_MXSNFENT.CODMOTORISTADEVOL = MXSEMPR.MATRICULA(+)
AND ERP_MXSNFENT.CODUSURDEVOL = MXSUSUARI.CODUSUR
AND MXSUSUARI.CODSUPERVISOR = MXSSUPERV.CODSUPERVISOR(+)
- Relaciona movimentações de estoque com os produtos
AND TO_NUMBER(ERP_MXSESTCOM.NUMTRANSENT) = ERP_MXSMOV.NUMTRANSENT
AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD(+)
- Exclui registros cancelados
AND NVL(TO_CHAR(ERP_MXSMOV.DTCANCEL,'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND NVL (ERP_MXSMOV.CODOPER, 'ED') = 'ED'
- Filtra apenas registros dentro do período de fevereiro de 2025
AND TRUNC(ERP_MXSNFENT.DTENT) BETWEEN TO_DATE('01/02/2025', 'dd/mm/yyyy') AND TO_DATE('28/02/2025', 'dd/mm/yyyy')
- Considera apenas determinados tipos de descarga e notas fiscais
AND ERP_MXSNFENT.TIPODESCARGA IN ('6','7','T')
AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA'
AND ERP_MXSNFENT.CODFISCAL IN ('131','132','231','232','199','299')
- Relaciona vendas e condições de venda
AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+)
AND NVL(ERP_MXSNFSAID.CONDVENDA,0) NOT IN (4, 8, 10, 13, 20, 98, 99)
- Filtra acesso do usuário a supervisores e filiais
AND MXSUSUARI.CODSUPERVISOR IN (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445')
AND ERP_MXSESTCOM.NUMTRANSVENDA = VENDAS.NUMTRANSVENDA(+)
AND ERP_MXSNFENT.CODFILIAL IN (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '6' AND CODUSUARIO = '80445')
- Relaciona fornecedor
AND F.CODFORNEC(+) = ERP_MXSNFENT.CODFORNEC
- Considera apenas pedidos com condição de venda igual a 1
AND ERP_MXSNFSAID.CONDVENDA IN (1)
GROUP BY TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY')
) DEVOL
GROUP BY DEVOL.DATA
)

- Seleciona os dados finais
SELECT
'DEVOL' SERIE
NVL(B.DATA, A.DATA) DATA
B.DIAUTIL DIAUTIL
NVL(A.VLTOTAL,0) VLTOTAL
FROM A
LEFT JOIN B ON A.DATA = B.DATA
GROUP BY NVL(B.DATA, A.DATA), B.DIAUTIL, VLTOTAL, 'DEVOL'

A baixo agrupado por pedido e a consulta reduzida para melhor entendimento

SELECT
DEVOL.DATA AS DATA
DEVOL.NUMPED
DECODE('S','N',0,SUM(DEVOL.VLDEVOLUCAO - 0 - 0 - DEVOL.VLREPASSE)) VLTOTAL
FROM (
- Obtém valores das notas fiscais de entrada (devoluções)
SELECT TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY') AS DATA
VENDAS.NUMPED
NVL(
SUM(
CASE
- Exclui certas condições de venda
WHEN ERP_MXSNFSAID.CONDVENDA IN (6,11) THEN 0
ELSE
( NVL (ERP_MXSMOV.QT, 0) * ( NVL (ERP_MXSMOV.PUNIT, 0) +
NVL (ERP_MXSMOV.VLFRETE, 0) +
NVL (ERP_MXSMOV.VLOUTRASDESP, 0) +
NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) +
NVL (ERP_MXSMOV.VLOUTROS, 0)
NVL (ERP_MXSMOV.VLREPASSE, 0) ))
END
)
0
) AS VLDEVOLUCAO
- Calcula valores de ST, IPI e repasse
NVL(SUM(NVL (ERP_MXSMOV.QT, 0) * NVL (ERP_MXSMOV.ST, 0)),0) VLST
NVL(SUM(NVL(ERP_MXSMOV.VLIPI, 0) * NVL (ERP_MXSMOV.QT, 0)),0) VLIPI
NVL(ROUND(SUM(ERP_MXSMOV.QT * ERP_MXSMOV.VLREPASSE), 2), 0) VLREPASSE
FROM ERP_MXSNFENT
ERP_MXSESTCOM
ERP_MXSTABDEV
MXSCLIENT
MXSEMPR
MXSUSUARI
MXSSUPERV
MXSFORNEC F
ERP_MXSNFSAID
ERP_MXSMOV
MXSPRODUT
ERP_MXSDEVCONSUM
MXSHISTORICOPEDC VENDAS
WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT(+)
- Relaciona a devolução com a tabela de devoluções cadastradas
AND ERP_MXSNFENT.CODDEVOL = ERP_MXSTABDEV.CODDEVOL(+)
AND MXSCLIENT.CODCLI = ERP_MXSNFENT.CODFORNEC
AND ERP_MXSNFENT.NUMTRANSENT = ERP_MXSDEVCONSUM.NUMTRANSENT(+)
- Relaciona com motorista, usuários e supervisores
AND ERP_MXSNFENT.CODMOTORISTADEVOL = MXSEMPR.MATRICULA(+)
AND ERP_MXSNFENT.CODUSURDEVOL = MXSUSUARI.CODUSUR
AND MXSUSUARI.CODSUPERVISOR = MXSSUPERV.CODSUPERVISOR(+)
- Relaciona movimentações de estoque com os produtos
AND TO_NUMBER(ERP_MXSESTCOM.NUMTRANSENT) = ERP_MXSMOV.NUMTRANSENT
AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD(+)
- Exclui registros cancelados
AND NVL(TO_CHAR(ERP_MXSMOV.DTCANCEL,'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND NVL (ERP_MXSMOV.CODOPER, 'ED') = 'ED'
- Filtra apenas registros dentro do período de fevereiro de 2025
AND TRUNC(ERP_MXSNFENT.DTENT) BETWEEN TO_DATE('01/02/2025', 'dd/mm/yyyy') AND TO_DATE('28/02/2025', 'dd/mm/yyyy')
- Considera apenas determinados tipos de descarga e notas fiscais
AND ERP_MXSNFENT.TIPODESCARGA IN ('6','7','T')
AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA'
AND ERP_MXSNFENT.CODFISCAL IN ('131','132','231','232','199','299')
- Relaciona vendas e condições de venda
AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+)
AND NVL(ERP_MXSNFSAID.CONDVENDA,0) NOT IN (4, 8, 10, 13, 20, 98, 99)
- Filtra acesso do usuário a supervisores e filiais
AND MXSUSUARI.CODSUPERVISOR IN (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '80445')
AND ERP_MXSESTCOM.NUMTRANSVENDA = VENDAS.NUMTRANSVENDA(+)
AND ERP_MXSNFENT.CODFILIAL IN (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '6' AND CODUSUARIO = '80445')
- Relaciona fornecedor
AND F.CODFORNEC(+) = ERP_MXSNFENT.CODFORNEC
- Considera apenas pedidos com condição de venda igual a 1
AND ERP_MXSNFSAID.CONDVENDA IN (1)
GROUP BY TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY'), VENDAS.NUMPED
) DEVOL
GROUP BY DEVOL.DATA, DEVOL.NUMPED

# GATE-900 - Praça de atendimento não oculta do cadastro

**Contexto**

Cliente deseja impedir o RCA de cadastrar a praça de atendimento no cadastro do cliente via APK, porem mesmo desmarcando a obrigatoriedade e marcando a flag de ocultar o campo na central de configurações ela continua apresentando obrigatoriedade na APK

**Resultado apresentado**

APK continua a apresenta obrigatoriedade para preenchimento de praça

**Resultado esperado**

Se foi desmarcado na central, na APK não deveria obrigar o preenchimento do campo

**Diagnostico e orientacao**

O cadastro da praça é obrigatório, no próprio Layout da TOTVs consta como obrigatório envio do CODPRACA na tabela PCCLIENTFV da integração com o Winthor

No maxPedido também é obrigatório a praça para carregamento de demais informaçõe sobre os preços dos produtos, mesmo sendo de Outros ERPs

Na central o campo tem a utilidade de ser permitido edição em novos cadastros e/ou edição; A opção de ocultar é apresentada devido ao padrão genérico de exibição da Central

Nesse caso acredito que nem sugerir melhoria cabe nesse contexto, porque a integração com o ERP força que um cadastro de praça seja definido

Uma opção que eles têm é tornar o código da praça padrão e inalterável pelo RCA no maxPedido. Com os Parâmetros COD_PRACA_PADRAO e BLOQUEIA_PRACA_PADRAO somado a configuração da Central no campo de "praça de atendimento

Assim o RCA não pode alterar e uma praça padrão sempre é enviada via integração do maxPedido para o Winthor

# GATE-901 - Venda broker não carrega em nova filial

**Contexto**

Cliente realizou a alteração da filial de venda principal de um perfil de vendedor da filial 2 para a filial 18
Cliente relata que ao iniciar um pedido na filial 18 como venda broker, a aplicação retorna a mensagem de inconsistência de dados devido à permissão de coleção de filiais do vendedor. O teste foi realizado no cliente 226972 e em base zero
Ao iniciar um pedido em um perfil que vende na filial 2 como venda broker, a aplicação inicia o pedido normalmente
Foi realizada a conferência dos parâmetros
FIL_BROKER
FIL_PERCOMFILIALBROKER
FIL_PERCOMMOTBROKER
FIL_PERCOMRCABROKER
FIL_PERFRETEBROKER
FIL_TIPOBROKER

E também as permissões de filiais dos vendedores, e os campos CONDVENDA4.MXSCLIENT, BROKER.MXSFILIAL e TIPOBROKER.MXSFILIAL

Login para teste
copinisan.emanoel

**Passos para reproduzir**

- Entrar na base do rca, iniciar um pedido no cliente 226972 como venda broker

**Resultado apresentado**

Ao iniciar, a aplicação retorna a mensagem de inconsistência de dados

**Resultado esperado**

É esperado que os vendedores possam iniciar pedidos de venda broker na filial 18

**Diagnostico e orientacao**

Para trabalhar com o processo de filial Broker a configuração do campo TIPOBROKER da MXSFILIAL, deve ser enviada com a informação 'MAB'

Na hora de listar as filiais o código do maxPedido valida se essa informação está sendo enviada

Então para resolver o cenário do ticket, ele só precisa enviar essa informação 'MAB', na filial 18, assim como na filial 1 por exemplo, nesse campo da MXSFILIAL. Se o cliente não tiver essa intrergação programada a gente pode fazer via banco nuvem

Feito isso os RCAs precisam sincronizar para validar
