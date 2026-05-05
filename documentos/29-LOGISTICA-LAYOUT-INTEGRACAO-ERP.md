# Layout de Integração Logística ERP x maxMotorista/maxRoteirizador

Dicionário de dados e orientações de integração entre ERP e soluções de logística maxMotorista/maxRoteirizador.

## Apresentação e objetivo

APRESENTAÇÃO Este documento fornece as informações necessárias da s

API ’s de Integração da Máxima , com foco na integração de nossas soluções aos diversos ERP’s do mercado atacadista distribuidor. As Web API’s da Máxima, foram construídas sob a plataforma da Microsoft .NET Core , padrão de com unicação Rest, trafegando objetos JSON conforme padronizado no La

S out de Integração Físico

(PDF), ou online na própria API (Swagger). Possui controle de logs para cada registro enviado ou recebido, possibilitando a parte ativa da integração (extrator de da dos do ERP), um melhor controle dos dados integrados. Utiliza

JWT Bearer Token (RFC 7519) como forma padrão de autenticação (Multi Tenant), aceita métodos de compactação do canal de dados pelos a lgoritimos GZIP ou Brotli. O c liente não precisa se preocupar com a infraestrutura para utilizar as soluções adquiridas, esta ficará 100% na n uvem da Máxima na AWS (Exceto clientes com ERP Winthor)

OBJETIVO DO DOCUMENTO O objetivo desse documento é fornecer o s endpoints que são util izados na integração de ERP’s com a plataforma da Máxima Sistemas.

O documento contém uma visão geral das informações que são integradas a nível de tabelas de banco de dados (via endpoint’s) e negócio. As tabelas do banco de dados do max Soluções citadas ne sse documento podem não ser integradas em sua totalidade , sendo dependente de uma entrevista de negócio para definição do layout ideal de integração

## Página 5

CLIENTES WINTHOR A integração da Máxima Sistemas com o WinThor é composta por Web API’s. Toda a c omunicação entre as API’s é compactada, utiliza se JWT Bearer Token para autenticação de cada canal de comunicação, através de um login exclusivo de acesso de cada cliente Máxima. Cada Token gerado, tem a assinatura única do cliente, cada cliente será dire cionado para seu Banco de Dados exclusivo (Multi Tenant). A responsabilidade da integração é 100% da Máxima. 2.1.1

### Api

EXTRATOR DE DADOS MÁXIMA A função da API Extrator , é gerenciar o trafego de dados entre o WinThor e a nuvem da Máxima, monitorando as inclusões/alterações/deleções de registros deste ERP, consolidando/trafegando somente dados que requer atualização na nuvem, evitando o envio de dados já existentes ou des necessários, garantindo que todas as soluções recebam os dados atualizados para funcionamento de seus recursos, além de gerir os dados enviados destas soluções pela nuvem da Máxima (Pedidos, Clientes entre outros) ao ERP. É recomendado que seja publicado na mesma infraestrutura de rede do Winthor, minimizando a latência no trafego de dados entre a API e o Banco de Dados Oracle do WinThor, o servidor desta

API deve ser Linux (Ver documento de requisitos de sistema s http://go.maximasist.com.br/arquivos/requisitos instalacao/cloud erp winthor.html e http://go.maximasist.com .br/arquivos/requisitos instalacao/hardwares.html

## Página 6

2.1.2

### Api De Integração

### Máxima

ENTRADA A função da API Integração da Máxima, única para todos os clientes é receber dados oriundas da API Extrator de Dados da Máxima respondendo 100% aos seus comandos de forma passiva. Persiste os dados no b anco de dados exclusivos para cada cliente . Esta API é a porta de entrada dos dados a serem integrados com o Winthor 2.1.3

### Api De Integração

### Máxima

(RETORNO/SAÍDA) A função da API Integração da Máxima, única para todos os clientes, é retornar dados à API Extrator de Dados da Máxima , respondendo 100% aos seus comandos de forma passiva. Esta API é a porta de saída dos dados a serem integrados com o Winthor

CLIENTES NÃO WINTHOR (OUTROS ERP’ s A integração da Máxima Sistemas com o ERP’s, exceto Winthor, é composta por Web API’s. Toda a comunicação com as API’s deverá ser compactada, utiliza se JWT Bearer Token para autenticação de cada canal de comunicação, através de um login exclusivo de ace sso de cada cliente Máxima. Cada Token gerado, tem a assinatura única do cliente, e cada cliente será direcionado para seu Banco de Dados exclusivo (Multi Tenant). A responsabilidade da integração é 100% d o parceiro/cliente, referente a criação de uma ferr amenta de extração de dados do ERP Ver documento de requisitos de sistema s http://go.maximasist.com.br/arquivos/requisitos instalacao/cloud outros erps.ht ml e http://go.maximasist.com.br/arquivos/requisitos instalacao/hardwares.html

## Página 7

2.2.1

### Api

EXTRATOR DE DADOS O cliente deve construir, manter, e dar garantia na consistênci a dos dados integrados com a n uvem da Máxima (necessário envio do La

S out de Integração Máxima aos Clientes), conforme API Extrator de dados Máxima conforme quando integrado com o Winthor. 2.2.2

### Api De Integração

### Máxima

ENTRADA A função da API Integração da Máxima, única para todos os clientes é receber dados oriundas da API Extrator de Dados do Cliente, respondendo 100% aos seus comandos de forma passiva. Persiste os dados no b anco de dados exclusivos para cada cliente . Esta API é a porta de e ntrada dos dados a serem integrados com o ERP do cliente. 2.2.3

### Api De Integração

### Máxima

(RETORNO/SAÍDA) A função da API Integração da Máxima, única para todos os clientes, é retornar dados à API Extrator de Dados do Cliente, respondendo 100% aos seus comandos de forma passiva. Esta API é a porta de saída dos dados a serem integrados com o ERP do cliente.

## Página 8

### Visão Geral Dos Conceitos Integrados

## Página 9

As informações enviadas aos E ndpoint s abaixo são consultadas pelas soluções da Máxima Sistemas . Esses dados são provenientes do ERP e são armazenados na base de dados do cliente na nuvem da Máxima. A entrada desses dados é dependente do extrator de dados. Os itens detalhados em amarelo são, a nível de dados, os requisitos mínimos de Endpoint’s/campos A responsabilidade das ações

GET (obter),

PUT (atualizar),

POST (adicionar) e

DELETE (excluir) são do extrator de dados. A s

API ’s de Integração da Máxima são passiva s , isto é, os dados são recebidos/ret ornados sob demanda de requisições d a API

E xtrator de Dados para o ERP, a API é um simples ouvinte, portanto é necessário que a API Extrator de Dados faça requisições em nossa s

API sincronizar os dados com o

ERP. A responsabilidade da API é manter os dad os atualizados em nosso banco de dados. O serviço de extração e gravação de dados do ERP é de responsabilidade do Cliente , exceto para o ERP Winthor. Neste documento é fornecido todas as informações e orientações necessárias para a troca de informações entre os bancos da Máxima e os ERP’s. Contudo, este é um documento vivo que está em constante atualização a versão mais atualizada estará disponível no Portal da Máxima Observa se a necessidade do preenchimento de todos os campos que indicam a obrigator iedade, em caso de o ERP não conter um ou mais campos, estes devem ser preenchidos com valor default/”mockados” consulte a Máxima para mais detalhes

## Página 10

### Orientações Técnicas

API HTTP Rest e objetos no padrão JSON. Operações GET, PUT, POST e

DELETE. Painel/Documentação Online API via Browser/Swagger (Entrada Carga de Dados): http://URLEntrada:Porta/swagger (Substituir ‘ URLEntrada ’ e ‘ Porta’ pelo endereço e porta da API correspondente fornecidos pela Máxima) Painel/Documentação Online API via Browser/Swagger Saída Retorno de Pedidos Clientes e outros http://URLSaida:Porta/swagger (Substituir ‘

URL Saida’ e ‘ Porta’ pelo endereço e porta da API correspondente fornecidos pela Máxima) Login de Acesso Backend: http://URLEntrada:Porta/api/v {version}/Login e/ou http://URLSaida:Porta/api/v {version}/Login Header JSON Login (Exemplo): {"login": " cole_seu_login_aqui ", "password": " cole_sua_senha_aqui

## Página 13

Endpoint sugestão para teste de Integração Backend (Categorias): http://URLEntrada:Porta/api/v {version}/Categorias

## Página 15

Imports System.Net Imports System.IO.Compression Imports System.IO Imports System.Text Imports Newtonsoft.Json Module Module1 Public Class Login Shared _retornoLogin As RetornoLogin Public Class RetornoLogin Public Sucess As Boolean Public Data_Criacao As DateTime Public Data_Expiracao As DateTime Public Token_De_Acesso As String Public Resposta As String End Class Private Sub EfetuaLoginAWSApi() Try If IsNothing(_retornoLogin) Or Not IsNothing(_retornoLogin) AndAlso Now.AddMinutes( 60) >= _retornoLogin.Data_Expiracao) Then Dim token As New KeyValuePair( Of Http StatusCode, String Dim jsonLogin = " {""login"": ""xxxxxxxxxxxxxxx"", ""password"": ""xxxxxxxxxxxxxxxxxxxx""} " Dim httpWebRequest As HttpWebRequest = CType (WebRequest.Create( http://

URL_API:PORTA/Login" ), HttpWebRequest) httpWebRequest.Headers.Add(HttpRequestHeader.AcceptEncoding, "gzip" httpWebRequest.Headers.Add(HttpRequestHeader.ContentEncoding, "gzip" httpWebRequest.ContentType = "application/json" httpWebRequest.Method =

"POST" httpWebRequest.ContentLength = jsonLogin.Length Using streamWriter As New StreamWriter(httpWebRequest.GetRequestStream()) streamWriter.Write( jsonLogin) streamWriter.Close() End Using Using response As HttpWebResponse = CType (httpWebRequest.GetResponse(), HttpWebResponse) Dim receiveStream = response.GetResp onseStream() If response.ContentEncoding.ToLower.Contains( "gzip" Then receiveStream = New GZipStream(receiveStream, CompressionMode.Decompress) End If Dim readStream = New StreamReader(receiveStream, Encoding.UTF8) token = New KeyValuePair( Of HttpStatusCode, String )(response.StatusCode, readStream.ReadToEnd) response.Close() readStream.Close() End Using If token.Key = HttpStatusCode.OK Then _retornoLogin = JsonConvert.DeserializeObject( Of RetornoLogin)(token.Value) Else Throw New Exception( "Erro ao autenticar na AWS API Máxima." End If End If Catch ex As Exception 'Tratamento de erro End Try End Sub

## Página 16

Private Sub ExecutaRequisicao() Try Dim dt As New DataTable 'Tabela com os registros extraidos de uma tabela no ERP Dim retorno As New KeyValuePair( Of HttpStatusCode, String Dim json As String = JsonConvert.SerializeObject(dt, Formatting.None) EfetuaLoginAWSApi() ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls Dim httpWebRequest As HttpWebRequest CType (WebRequest.Create( http://

URL_API:PORTA/Categorias" ), HttpWebRequest) httpWebRequest.Headers.Add(HttpRequestHeader.AcceptEncoding, "gzip" httpWebRequest.Headers.Add(HttpRequestHeader.ContentEncoding, "gzip" httpWebRequest.ContentType = "application/json" httpWebRequest.Method =

"POST" httpWebRequest.Timeout = 12000000 httpWebRe quest.Headers.Add( "Authorization" "Bearer " & _retornoLogin.Token_De_Acesso) Using streamWriter As New StreamWriter(httpWebRequest.GetRequestStream()) streamWriter.Write(json) streamWriter.Close() End Using Using response As HttpWebResponse = CType (httpWebRequest.GetResponse(), HttpWebResponse) Dim receiveStream = response.GetResponseStream() If response.Co ntentEncoding.ToLower.Contains( "gzip" Then receiveStream = New GZipStream(receiveStream, CompressionMode.Decompress) End If Dim readStream = New StreamReader(receiveStream, Encoding.UTF8) retorno = New KeyValuePair( Of HttpStatusCode, String )(response.StatusCode, readStream.ReadToEnd) response.Close() readStream.Close() End Using If retorno.Key = HttpStatusCode.OK Then 'tratar sucesso Else 'tratar erro End If Catch ex As Exception 'Implementar log

E nd Try End Sub End Class End Module

## Página 17

INTRODUÇÃO A UTILIZAÇÃO DO DICIONÁRIO DE DADOS Abaixo segue o dicionário de dados utilizado para integração com outros ERP’s, cada Endpoint/tabela faz parte de um contexto de negóc io, algumas podem ser alimentadas via integração e outras podem ser alimentadas através de nossos portais (BackOffice). O título “Exemplo: .1 Atividade s ” refere se ao nome do endpoint utilizado na API de integração (Atividades) , campo “Coluna” descreve o nome técnico utilizado pela API , já o campo “Tipo” descreve o tipo de valor a ser tratado/enviado, o campo “Tamanho” específica a quantidade máxima de carac teres suportado pelo campo, a coluna “Obrigatório” (S=Sim ou N=Não), descreve se o campo é obrigató rio para o funcionamento da aplicação/funcionalidade, a coluna “PK” determina que o campo é obrigatório e consequentemente chave, a coluna “Observação” descreve de forma breve o contexto de negócio. As tabelas/endpoints que estão definidas na cor amarel são obrigatórias para o funcionamento básico da s aplicaç ões Caso não h aja informação respectiva do ERP, estas deverão ser tratadas na integração para que sejam enviadas, via ”mock” de dados, para mantermos a integridade dos relacional entre tabelas quem compõe o negócio

## Página 18

### Visão Geral De Endpoints Do

### Maxmotorista E Maxroteirizador

(ENTRADA) Para fazer a carga de dados é necessário fazer chamadas PUT/POST/DELETE nos Endpoint correspondentes: http://URL_API_ENTRADA:PORTA/api/v2/

NOME_ENDPOINT Atividades Tabela

MXSATIVI Coluna Tipo Tamanho Obrigatório

PK Observação

### Codativ

### Varchar2

### S

S Código

### Ramo

### Varchar2

S Descrição do Ramo de Atividades

### Percdesc

### Number

S % Acréscimo/Desconto no preço de tabela

### Calculast

### Varchar2

S Flag para definir se irá calcular ST (S ou N) Negócio Responsável por armazenar o ramo de atividade do cliente, é utilizado no maxRoteirizador para que seja possível realizar a filtragem de pedidos no mapa somente de cliente que tem a atividade “X”. Também é utilizado para que seja possível caso seja parametrizável utilizar a funcionalidade de legendar por cores os pins no mapa diferenciando os clientes pela sua atividade. Utilizado por : maxRoteirizador Relacionamento :

### (Mxsativi.Codativ

### Mxsclient.Codatv1).

## Página 19

Cidades Tabela

MXSCIDADE Coluna Tipo Tamanho Obrigatório

PK Observação

### Codcidade

### Varchar2

### S

S Código da cidade

### Codibge

VARCHAR2 s Código do IBGE

### Nomecidade

### Varchar2

S Nome

### Uf

### Varchar2

### S

UF Negócio: Responsável por armazenar as cidades IBGE chave de ligação com a tabela de clientes . No maxRoteirizador esta informação é utilizada na funcionalidade de agrupamento por cidade dos pedidos pendentes para roteirização. No maxMotorista é utilizada pa ra pre encher o campos cidade em telas de consultas de clientes. Utilizado por : maxMotorista e maxRoteirizador Relacionamento:

### (Mxscidade.Codcidade = Mxsclient.Codcidade).

## Página 20

Clientes Tabela

MXSCLIENT Coluna Tipo Tamanho Obrigatório

PK Observação

### Aceitavendafracao

### Varchar2

N Esta opção permite re

VARCHAR2 ir a um cliente a venda fracionada definida no cadastro do produto.

### Atualizasaldoccdescfin

### Varchar2

N Caso esta opção esteja marcada, durante o faturamento das vendas para o referido cliente não será atualizado o saldo de conta corrente do RCA, somente para vendas que utilizem saldo de conta corrente como desconto financeiro.

### Bairrocob

### Varchar2

N Bairro

### Bairrocom

### Varchar2

N Bairro

### Bairroent

### Varchar2

S Bairro

### Bloqueio

### Varchar2

S Bloqueado? (S ou N)

### Bloqueiodefinitivo

### Varchar2

N Flag que informa se o cliente está com bloqueio definitivo

### Bloqueiosefaz

### Varchar2

S Flag que informa se o cliente está bloqueado no SEFAZ

### Caixapostal

### Number

N Caixa Postal

### Calculast

### Varchar2

N Calcular ST (S ou N)

### Cepcob

### Varchar2

### N

CEP de cobrança.

### Cepcom

### Varchar2

### N

CEP comercial.

### Cepent

### Varchar2

### S

CEP de entrega.

### Cgcent

### Varchar2

S Digitar o CNPJ para pessoa jurídica e CPF para pessoa Física.

## Página 21

### Classevenda

### Varchar2

N Classe Venda Pode ser utilizado como legenda e classificador na listagem de clientes.

### Cliente

### Varchar2

S Nome do Cliente Pessoa Física ou Razão Social para Pessoa Jurídica.

### Clientefontest

### Varchar2

N Este campo indica quando o cliente é tributado com ST fonte (PCCLIENT.CLIENTEFONTEST).

### Clientemonitorado

### Varchar2

N Cliente monitorado

### Codatv1

### Varchar2

N Código da Atividade Econômica

### Codcidade

### Varchar2

S Código da Cidade

### Codcli

### Varchar2

### S

S Código do Cliente.

### Codcnae

### Varchar2

N Classificação Nacional das Atividades Econômicas

### Codclipalm

### Varchar2

N Código do cliente gerado no tablet

### Codcliprinc

### Varchar2

N Cliente Principal

### Codcob

### Varchar2

S Código cobrança

### Codfilialnf

### Varchar2

S Cod.Filial para emissão de NF’s do cliente.

### Codfornecfrete

### Number

N Transportadora Padrão

### Codfuncultalter

### Varchar2

N Último Funcionário a alterar o cadastro (Informar 1)

### Codplpag

### Varchar2

S Plano de Pagamento

### Codrota

### Varchar2

N Código da rota de entrega do cliente.

### Codpraca

### Varchar2

N Praça

### Codrede

### Number

N Rede de Cliente

### Codusur1

### Varchar2

S Código do Vendedor 1

### Codusur2

### Varchar2

N Código do Vendedor 2

### Complementocob

### Varchar2

N Complemento

### Complementocom

### Varchar2

N Complemento

### Complementoent

### Varchar2

S Complemento do endereço de entrega.

### Condvenda1

### Varchar2

N Tipo de venda 1 Venda Normal (S ou N)

## Página 22

### Condvenda11

### Varchar2

N Tipo de venda 11 Troca bonificada (S ou N)

### Condvenda13

### Varchar2

N Tipo de venda 13 Manifesto (S ou N)

### Condvenda14

### Varchar2

N Tipo de venda 14 Complemento Manifesto (S ou N)

### Condvenda20

### Varchar2

N Tipo de venda 20 Consignado (S ou N)

### Condvenda5

### Varchar2

N Tipo de venda 5 Bonificação (S ou N)

### Condvenda7

### Varchar2

N Tipo de venda 7 Entrega Futura (S ou N)

### Condvenda8

### Varchar2

N Tipo de venda 8 Simples Remessa (S ou N)

### Condvenda9

### Varchar2

N Tipo de venda 9 Venda Normal CFOP diferente da venda normal. (S ou N)

### Condvenda4

### Varchar2

N Tipo de venda 4 Broker (S ou N)

### Consumidorfinal

### Varchar2

N (S ou N)

### Contribuinte

### Varchar2

N Contribuinte

### Datacoleta

### Date

N Data de coleta

### Dtbloq

### Date

N Data do bloqueio

### Dtultcomp

### Date

N Data da Última Compra

### Dtvalidadeibama

### Date

N Data de validade do registro do cliente no IBAMA

### Dtvencalvara

### Date

N Alvará Psicotrópicos / Data de Vencimento do Alvará

### Dtvencalvaraanvisa

### Date

N Alvará ANVISA / Data de Vencimento do Alvará

### Dtvencalvarafunc

### Date

N Alvará Funcionamento / Data de Vencimento do Alvará

### Dtvencalvararetinoico

### Date

N Campo que define a data do alvará retinóico

### Dtvencalvarasus

### Date

N Data vencimento alvará SUS.

### Dtvenccrf

### Date

N Alvará CRF / Data de Vencimento do Alvará

### Dtvencsuframa

### Date

N Data de Vencimento Suframa

### Email

### Varchar2

### N

E mail

### Emailnfe

### Varchar2

### S

E mail NF e

## Página 23

### Endercob

### Varchar2

N Endereço Cobrança

### Endercom

### Varchar2

N Endereço comercial.

### Enderent

### Varchar2

S Endereço de entrega.

### Estcob

### Varchar2

N UF do Estado

### Estcom

### Varchar2

N UF do Estado

### Estent

### Varchar2

S UF do Estado

### Fantasia

### Varchar2

S Nome fantasia da empresa (Pessoa Jurídica).

### Faxcli

### Varchar2

N Fax

### Faxcom

### Varchar2

N Fax

### Fretedespacho

### Varchar2

N Caso a opção "Cupom Fiscal" esteja marcada para algumas operações os pedidos receberão condição de venda igual a 3. Caso a opção marcada seja "Nota Fiscal" ou "Ambos" os pedidos receberão condição de venda igual a 1.

### Ieent

### Varchar2

N Informar Inscrição Estadual. Caso não tenha, informar

### Isento.

### Iment

### Varchar2

N Insc. Municipal

### Isencaosuframa

### Varchar2

N Não será aplicada a redução referente ao item selecionado. Ex.: Não será aplicada redução de ICMS, IPI ou PIS/COFINS. Se for selecionada a opção "Aplica todas Reduções" serão aplicadas todos os % de desconto informados na rotina 514.

### Isentodifaliquotas

### Varchar2

N Isento de Diferença de Alíquotas

### Isentoicms

### Varchar2

N Isento de ICMS

### Isentoipi

### Varchar2

N Isento de IPI (S ou N)

### Isentotxboleto

### Varchar2

N Isento de Taxa de Boleto

## Página 24

### Ivafonte

### Number

N Este campo é utilizado para indicar o IVA Fonte para o cliente que tiver um IVA Fonte diferenciado do definido na tributação do produto na região, ou por estado.

### Latitude

### Varchar2

N Latitude

### Longitude

### Varchar2

N Longitude

### Municcob

### Varchar2

N Município

### Municcom

### Varchar2

N Município

### Municent

### Varchar2

S Município

### Numagencia1

### Number

N Agência nº

### Numagencia2

### Number

N Agência nº

### Numalvara

### Varchar2

N Alvará Psicotrópicos / Número Alvará

### Numalvaraanvisa

### Varchar2

N Alvará ANVISA / Número Alvará

### Numalvarafunc

### Varchar2

N Alvará Funcionamento / Número Alvará

### Numalvararetinoico

### Varchar2

N Campo que define o número do alvará retinóico

### Numalvarasus

### Varchar2

N Alvará SUS / Número Alvará

### Numbanco1

### Number

N Banco nº

### Numbanco2

### Number

N Banco nº

### Numccorrente1

### Varchar2

N Conta Corrente

### Numccorrente2

### Varchar2

N Conta Corrente

### Numcrf

### Varchar2

N Alvará CRF / Número Alvará

### Numerocob

### Varchar2

N Número

### Numerocom

### Varchar2

N Número

### Numeroent

### Varchar2

S Número

### Obs

### Varchar2

N Observação

### Obs2

### Varchar2

N Observação

### Obs3

### Varchar2

N Observação

### Obs4

### Varchar2

N Observação

### Obs5

### Varchar2

N Observação

## Página 25

### Obscredito

### Varchar2

N Observação de crédito

### Obsentrega1

### Varchar2

N Observações

### Obsentrega2

### Varchar2

N Observações

### Obsentrega3

### Varchar2

N Observações

### Obsgerencial1

### Varchar2

N Observações Gerenciais

### Obsgerencial2

### Varchar2

N Observações Gerenciais

### Obsgerencial3

### Varchar2

N Observações Gerenciais

### Orgaopub

### Varchar2

N Tipo de Órgão Público / Estadual

### Orgaopubfederal

### Varchar2

N Tipo de Órgão Público / Federal

### Orgaorg

### Varchar2

N Órgão emissor

### Origempreco

### Varchar2

N Origem de Preço de Mercadorias Monitoradas e Monitoradas de Alto Custo

### Paisent

### Varchar2

N Pais

### Percomcli

### Number

N % Comissão

### Perdesc

### Number

N % Desconto

### Perdescisentoicms

### Number

N % Desconto ICMS

### Plpagneg

### Varchar2

N Acessar Plano de Pagamentos Negociados

### Pontorefer

### Varchar2

N Ponto de Referência

### Prazoadicional

### Number

N Prazo adicional

### Predioproprio

### Varchar2

N Prédio Próprio

### Qtcheckout

### Number

N Qt. Check out

### Registroibama

### Varchar2

N Número do registro do cliente no IBAMA

### Repasse

### Varchar2

N Utiliza repasse

### Rg

### Varchar2

N Digitar o RG para cadastro de pessoa física.

### Simplesnacional

### Varchar2

N Aplicar Desconto Simples Nacional

### Site

### Varchar2

N Site

### Sulframa

### Varchar2

N Número Suframa do Cliente

### Telcob

### Varchar2

N Telefone Cobrança

## Página 26

### Telcom

### Varchar2

N Telefone

### Telent

### Varchar2

S Telefone Comercial

### Telent1

### Varchar2

N Telefone de entrega 1

### Tipodescisencao

### Varchar2

N Tipo de Desconto de Isenção de ICMS. Na edição de registros: Se PCCLIENT.PERDESCISENTOICMS > 0 o campo receberá "C". Se NVL(PCCLIENT.PERDESCISENTOICMS, 0) = 0, o campo receberá "N".

### Tipodocumento

### Varchar2

N Tipo de Documento

### Tipoempresa

### Varchar2

N Tipo de Empresa

### Tipofj

### Varchar2

S Indica se o cliente é pessoa física ou jurídica. (F ou J)

### Turnoentrega

### Varchar2

N Define o turno de entrega do pedido do cliente

### Usadebcredrca

### Varchar2

N Usa débito e crédito de RCA. (S ou N)

### Usadescfinseparadodesccom

### Varchar2

N Se esta opção estiver marcada, ao digitar um pedido de venda o desconto financeiro cadastrado na rotina 561 será gravado separado do desconto comercial, se não estiver marcado, o % de desconto financeiro será somado junto ao desconto comercial.

### Usadescontoicms

### Varchar2

N Se este parâmetro estiver marcado, o % de isenção do ICMS informado na rotina 514 será diminuído do preço de tabela do produto.

### Usaivafontediferenciado

### Varchar2

N Nos casos em que o cliente é tributado com fonte st, este parâmetro permite informar uma alíqTE).

### Utilizaiesimplificada

### Varchar2

N Utiliza IE Simplificada

## Página 27

### Validamaxvendapf

### Varchar2

N Valida máximo venda para Pessoa Física, Isento e Consumidor Final.

### Validarcampanhabrinde

### Varchar2

N Validar Campanha de Brinde

### Validarmultiplovenda

### Varchar2

N Validar Múltiplo de Venda

### Vip

### Varchar2

N Classificação

### Vlfrete

### Number

N Valor do Frete

### Vlmaxcobfrete

### Number

N Valor máximo do pedido para cobrança de frete Negócio: Responsável por armazenar os cadastros e informações de clientes Utilizador por : maxMotorista e maxRoteirizador. Relacionamento :

### (Mxs

### Client

### .Cod

### Cli

### = Mxsclient

### Endent

CODCLI Um cliente pode ter vários endereços alternativos Relacionamento entre o cliente e seus possíveis endereços de entrega alternativas.

### Mxshistoricopedc

### Codendentcli

### Mxs

### Client

### .Cod

CLI Um pedido poder ter um cliente. ClientesEnderecos Tabela

MXSCLIENTENDENT Coluna Tipo Tamanho Obrigatório

PK Observação

### Bairroent

### Varchar2

S Bairro

### Cepent

### Varchar2

### S

### Cep

### Codbairroent

### Number

S Código Bairro

### Codcli

### Varchar2

### S

S Código Cliente

### Codendentcli

### Number

### S

S Código Endereço

### Codpracaent

### Number

N Código Praça

### Complementoent

### Varchar2

N Complemento

## Página 28

### Enderent

### Varchar2

N Endereço

### Estent

### Varchar2

N Estado

### Municent

### Varchar2

N Município Negócio: Responsável por armazenar endereços de entrega adicionais ao cadastro do cliente, podendo haver vários registros de endereços de entrega para o mesmo cliente . Quando o cliente utilizada este processo o vendedor ao final do pedido indicar em qual endereço será realizado a entrega. Utilizador por : maxMotorista e maxRoteirizador. Relacionamento :

(MXSCLIENTENDENT.CODCLI = MXSCLIENT.CODCLI) Um cliente pode ter vários endereços alternativos Relacionamento entre o cliente e seus possíveis endereços de entrega alternativos.

### (Mxsclientendent.

### Codendentcli =

### Mxshistoricopedc

CODENDENTCLI Um pedido poder ter somente um endereço alternati vo Relacionamento entre o pedido que foi digitado e qual será o seu endereço de entrega caso o vendedor tenha indicado Caso este campo esteja nulo no cabeçalho do pedido a entrega será realizada e roteirizada no endereço de entrega padrão definido no ca dastro do cliente. Clientes/UltimaCompra Tabela

MXSULTCOMPCLIENTE Coluna Tipo Tamanho Obrigatório

PK Observação

### Codcli

### Varchar2

### S

S Código do cliente

### Dtultcomp

### Date

S Data da última compra Negócio: Tabela utilizada para armazenar a última compra do cliente (Informações faturadas) . É utilizada no maxRoteirizador para que se possa restringir quais clientes positivados em qual data terão seu endereço geocodificado s Utilizado por: maxRoteirizador Relac ionamento:

### Mxsultcompcliente

### .Codcli = Mxsclient.Codcli)

## Página 29

Cobrancas Tabela

MXSCOB Coluna Tipo Tamanho Obrigatório

PK Observação

### Boleto

### Varchar2

S Boleto bancário (S ou N)

### Cartao

### Varchar2

S Cartão de crédito (S ou N)

### Cobranca

### Varchar2

S Descrição

### Codcob

### Varchar2

### S

S Código

### Codfilial

### Varchar2

N Ao selecionar a filial será permitido o uso desta cobrança caso a filial de pedido seja igual a filial de cobrança

### Nivelvenda

### Number

S Nível de venda

### Prazomaximovenda

### Number

S Prazo máximo de venda

### Cobrancabroker

### Varchar2

N Gravar o valor “S” para indicar que a cobrança e do tipo de operação Broker.

### Vlminpedido

### Number 12,2

N Valor mínimo de venda Negócio: Responsável por armazenar as cobranças do sistema , esta informação é visualizada no detalhes dos pedidos. Utilizada por : maxMotorista e maxRoteirizador. Relacionamento :

### Mxscob

### .Cod

### Cob

### = Mxsclient.Co

DCOB e (MXSCOB.CODCOB =

### Mxshistoricopedc

### Codcob)

## Página 30

Contatos Tabela

MXSCONTATO Coluna Tipo Tamanho Obrigatório

PK Observação

### Cargo

### Varchar2

N Cargo

### Celular

### Varchar2

N Celular

### Cgccpf

### Varchar2

N Indica CNPJ/CPF sem máscara.

### Codcli

### Varchar2

### S

S Código Cliente

### Codcontato

### Number

### S

S Código Contato

### Dtnascconjuge

### Date

N Data Nasc. Cônjuge

### Dtnascimento

### Date

N Data Nascimento

### Email

### Varchar2

### N

E mail

### Hobbie

### Varchar2

N Hobbies

### Nomeconjuge

### Varchar2

N Nome Cônjuge

### Nomecontato

### Varchar2

S Nome Contato

### Obs

### Varchar2

N Indica a observação do contrato.

### Telefone

### Varchar2

N Telefone

### Time

### Varchar2

N Time

### Tipocontato

### Varchar2

N Tipo Contato Negócio : Responsável por armazenar os contatos relacionados ao cadastro do cliente, podendo haver vários contatos para o mesmo cliente É utilizado no maxMotorista para disponibilizar o contato do cliente no aplicativo para o motorista. Utilizado por : maxMotorista. Relacionamento

### (Mxscontato.Codcli

### Mxsclient.Codcli).

## Página 31

E mpr s Tabela

MXSEMPR Coluna Tipo Tamanho Obrigatório

PK Observação

### Codsetor

### Number

N Cód. do setor

### Nome

### Varchar2

S Nome

### Email

### Varchar2

### N

E mail

### Enviafv

### Varchar2

N Enviafv

### Matricul

### A

### Number

### S

S Matrícula

### Nome_Guerra

### Varchar2

N Apelido

### Fone

### Varchar2

N Telefone fixo do empregado

### Celular

### Varchar2

N Telefone celular do empregado

### Codfilial

### Varchar2

N Código da filial de alocação do empregado

### Tipo

### Varchar2

S S(Chave composta).

‘M’ = Motorista e ‘F’ = Funcionário.

### Data_Validade_Cnh

### Data

N Data de validade da CNH

### Dt_Exclusao

### Data

N Data de exclusão lógica do registro

### Cpf

### Varchar2

N Código Pessoa Física

### Situacao

### Varchar2

N Situação do empregado (Default = 'A' Ativo

, ‘I’ Inativo

### Codmotorista

### Number

N Código do motorista quando o empregado for do tipo . Este campo deve ser obrigatório quando o empregado for do tipo ‘M’ motorista Negócio: Responsável por armazenar informações dos funcionários e motoristas. Informação essencial para a utilização do maxMotorista e maxRoteirizador. Utilizada por : maxMotorista e maxRoteirizador

## Página 32

Relacionamento

### (Mxs

### Empr

### Codmotorista

MXSCARREG.CODMOTORISTA Vínculo entre o motorista e carregamento montado Como esta tabela/endPoint irá receber tanto motoristas como funcionários , o campo CODMOTORISTA não será obrigatório somente quando o empregado for do TIPO ‘M’ de motorista. Quando um empregado for do tipo ‘F’ Funcionário, será utilizado o campo MATRICULA para realizar o vinculo de cadastro de usuá rios no maxRoteirizador , pois para cr iar um usuário no maxRoteirizador o vínculo com um usuário do ERP é obrigatório. Filiais Tabela

MXSFILIAL Coluna Tipo Tamanho Obrigatório

PK Observação

### Aceitavendasemest

### Varchar2

N Aceita vendas sem estoque

### Alterarcobbkchautomatico

### Varchar2

N Altera cobrança boleto automaticamente

### Autoservico

### Varchar2

N Autosserviço

### Bairro

### Varchar2

N Bairro

### Bloquearpedidosabaixovlminimo

### Varchar2

N Bloquear pedidos com valor abaixo do mínimo

### Calcularipivenda

### Varchar2

N Calcular IPI na venda . (S ou N)

### Cep

### Varchar2

### N

### Cep

### Cgc

### Varchar2

### S

### Cnpj

### Cidade

### Varchar2

N Cidade

### Codcli

### Varchar2

S Código da filial como cliente

### Codigo

### Varchar2

### S

S Código

### Considerarcomissaozero

### Varchar2

N Caso esta opção seja selecionada, as comissões que estejam com valor igual a zero também serão utilizadas para a avaliação da comissão.

### Endereco

### Varchar2

N Endereço

### Fax

### Varchar2

N Fax

## Página 33

### Ie

### Varchar2

N Inscrição estadual

### Lancarfretepesoautfat

### Varchar2

N Indica se deve lançar o valor do frete referente ao peso das mercadorias automaticamente no faturamento

### Razaosocial

### Varchar2

S Razão social

### Telefone

### Varchar2

N Telefone

### Tipoavaliacaocomissao

### Number

N Caso a opção 2 Por Sobreposição seja selecionada, a ordem de avaliação das comissões será baseada conforme cadastro da 584

### Tipofreteauto

### Varchar2

N Forma de cálculo de frete

### Tipoprecificacao

### Varchar2

N Este parâmetro é utilizado para precificação automática do preço de atacado ou varejo multiplicando pelo índice preço . (A ou P)

### Uf

### Varchar2

### S

### Uf

### Usaestoquedepfechado

### Varchar2

N Utiliza filial retira

### Usawms

### Varchar2

S Usa WMS

### Utilizanfe

### Varchar2

N Utiliza o processo de Nota fiscal eletrônica

### Broker

### Varchar2

N Ao estar habilitado “S” indica que a Filial pode realizar venda Broker.

### Utilizavendaporembalagem

### Varchar2

N Parâmetro por filial para indicar o uso de venda por embalagem . (S ou N) Negócio: Responsável por armazenar informações de filial. Utilizado por : maxMotorista e maxRoteirizador

## Página 34

5.10 HistoricosPedidosCapas Tabela

MXSHISTORICOPEDC Coluna Tipo Tamanho Obrigatório

PK Observação

### Codfunccanc

### Number

N Código do funcionário do cancelamento do pedido

### Dtfat

### Date

N Data de faturamento

### Motivo

### Varchar2

N Motivo do cancelamento

### Dtinicialsep

### Date

N Data inicial da separação do pedido

### Codcli

### Varchar2

S Código do Cliente

### Numnota

### Number

N Número da nota fiscal

### Codfuncconf

### Number

N Código do funcionário da conferência do pedido

### Codfuncfat

### Number

N Código do funcionário que fez o faturamento

### Totpeso

### Number

N Total do peso

### Origemped

### Varchar2

S Origem do pedido Telemarketing Forca Venda,

W Web)

### Dtinicialcheckout

### Date

N Data inicial do checkout

### Minutofat

### Number

N Minuto da hora do faturamento

### Motorista

### Varchar2

N Nome do motorista

### Posicao

### Varchar2

S Posição do pedido

## Página 35

L Liberado( Pedidos que estão aptos a serem montados).

F Faturado, sankya ira gravar quando faturar.

M Montado, retorna quando gravarmos.

### Vltabela

### Number

S Valor de tabela do pedido

### Numped

### Number

### S

S Número do pedido

### Dtfinalsep

### Date

N Data final da separação

### Dtcancel

### Date

N Data do cancelamento

### Obsentrega

### Varchar2

N Observação de entrega

### Horafat

### Number

N Hora do faturamento

### Codfuncsep

### Number

N Código do funcionário da separação do pedido

### Condvenda

### Number

S Tipo de venda Normal, bonificada, futura, etc. Venda, 5 Bonificacao, 7 Venda Futura, 11 Troca, 13 NF Manifesto (Saida), 14 Venda Manifesto (Pronta Entrega)

### Codfilialnf

### Varchar2

N Código da filial virtual

### Codfilial

### Varchar2

S Código da filial

### Codusur

### Varchar2

S Código do Vendedor no ERP

### Vlatend

### Number

S Valor atendido

### Dtemissaomapa

### Date

N Data de emissão do mapa de separação

### Hora

### Number

N Hora do pedido

### Codcob

### Varchar2

S Código da cobrança

### Vltotal

### Number

S Valor total

### Codendentcli

### Varchar2

N Código do endereço de entrega.

### Data

### Date

S Data do pedido

### Codfunclibera

### Number

N Código do funcionário de liberação

### Numcar

### Number

N Número do carregamento

### Dtfinalcheckout

### Date

N Data final do checkout

## Página 36

### Numpedrca

### Number

N Número do pedido do RCA Integradora

### Minuto

### Number

N Minuto da hora do pedido

### Codfuncemissaomapa

### Number

N Código do funcionário da emissão do mapa

### Dtlibera

### Date

N Data de liberação

### Obs1

### Varchar2

N Observação

### Obs2

### Varchar3

N Observação

### Codfornecfrete

### Number

N Código do fornecedor Frete

### Obs

### Varchar2

N Observação

### Codplpag

### Varchar2

S Código do plano de pagamento

### Codfornecredespacho

### Number

N Código do fornecedor Redespacho

### Numseqmontagem

### Number

N Número de sequenciamento da montagem

### Restricaotransp

### Varchar2

N Define se o pedido é restrito por tipo de transporte, o campo recebe os valores S ou N.

### Codsupervisor

### Number

N Código do supervisor

### Dtwms

### Date

N Data do WMS

### Dtagendaentrega

### Date

N Data do agendamento de entrega do pedido

### Dtentrega

### Date

N Data de entrega do pedido

### Coddistrib

### Varchar2

N Código de distribuição

### Numtransvenda

### Number

N Número de transação da venda

### Totvolume

### Number 18,6

S Volume total do pedido

### Numseqentrega

### Number

N Número de sequenciamento da entrega

### Codpraca

### Number

N Código da praça de atendimento

### Codendent

### Number

N Código do endereço de entrega

### Numitens

### Number

N Número de itens do pedido

### Numviasmapasep

### Number

N Número de vias do mapa de separação Negócio: Responsável por armazenar os históricos de pedidos, podendo enviar informações de pedidos feitos em outros canais de venda ao dispositivo do vendedor como: ( telemarketing, call center e comerce Será nesta tabela/endpoint que o maxRoteirizador irá buscar os

## Página 37

pedidos na posição ‘L’(campo POSICAO) para montar e roteirizar carregamentos. Caso o cliente trabalhe com o conceito de “pra ça/rota” para a organização/agrupamento dos pedidos o campo CODPRACA deve vir preenchido obrigatoriamente. Utilizado por : maxMotorista e maxRoteirizador 5.11 HistoricosPedidosItens Tabela

MXSHISTORICOPEDI Coluna Tipo Tamanho Obrigatório

PK Observação

### Numped

### Number

### S

S Número do pedido

### Qt

### Number

S Quantidade do produto

### Numseq

### Number

### S

S Número sequencial

### Pvenda

### Number 18,6

S Preço de venda

### Codprod

### Varchar2

### S

S Código do produto

### Ptabela

### Number 18,6

S Preço tabela Negócio: Responsável por armazenar os históricos de itens por pedido. 5.12 HistoricosPedidosCortes Tabela

MXSHISTORICOPEDCORTE Coluna Tipo Tamanho Obrigatório

PK Observação

### Codprod

### Varchar

### S

S Código do produto

### Numped

### Number

### S

S Número do pedido

## Página 38

### Qtcortada

### Number

S Quantidade cortada Negócio: Responsável por armazenar os históricos de itens cortados por pedido. 5.13 HistoricosPedidosFaltas Tabela

MXSHISTORICOPEDFALTA Coluna Tipo Tamanho Obrigatório

PK Observação

### Qtfalta

### Number

S Quantidade de falta do produto

### Numped

### Number

### S

S Número do pedido

### Qtpedida

### Number

S Quantidade pedida

### Codprod

### Varchar2

### S

S Código do produto Negócio: Responsável por armazenar os históricos de itens com falta por pedido. 5.14 Doceletronico Tabela

MXSDOCELETRONICO EndPoint S wagger Não existe ainda Coluna Tipo Tamanho Obrigatório

PK Observação

### Num

### Nota

### Number

### Y

Y Número da Nota Fiscal

### Xmlnfe

### Clob

Y XML gerado pela Sefaz Negócio: Responsável por armazenar informações do XML da nota fiscal. Informação utilizada na funcionalidade de reenvio de XML da nota no maxMotorista. Utilizada por : maxMotorista Relacionamento

### (Mxs

### Doceletronico

### Numnota

### Mxs

### Nfsaid

NUMERO_NOTA 5.15 NotasSaidaCapas

## Página 39

Tabela/EndPoint

MXSNFSAID Coluna Tipo Tamanho Obrigatório

PK Observação

### Numero_Nota

### Number

Y Número da Nota Fiscal

### Numero_Transvenda

### Number

### Y

Y Número da transação gerada pela nota

### Especie

### Varchar2

Y Espécie

### Dtsaida

### Date

N Data de Saída da Nota

### Vltotal

### Number 12,2

Y Valor Total

### Codcli

### Number

Y Código do cliente

### Dtentrega

### Date

Y Data prevista de Entrega

### Codfilial

### Number

Y Código da Filial

### Totpeso

### Number 18,6

Y Peso Total

### Totvolume

### Number 18,6

Y Volume Total

### Numcar

### Number

Y Número do Carregamento/Romaneio

### Numped

### Number

Y Número do pedido

### Codcob

### Varchar2

N Código de cobrança

### Codplpag

### Number

N Código do plano de cobrança

### Obs

### Varchar2

N Observação

### Numitens

### Number

Y Quantidade de itens na nota

### Dtcancel

### Date

Y Data de cancelamento da nota

### Numseq

### Number

N Sequência do item

### Codusur

### Number

N Código do Vendedor do pedido

### Codsupervisor

### Number

N Código do Supervisor

### Dtfat

### Date

Y Data de Faturamento Negócio: Responsável por armazenar informações do cabeçalho da nota fiscal de saída. Informações essenciais para o funcionamento do maxMotorista. Utilizada por : maxMotorista

## Página 40

Relacionamento

### Mxs

### Nfsaid

### Numero_Nota =

MXSHISTORICOPEDC.NUMNOTA 5.16 NotasSaidaItens Tabela/EndPoint

ERP_MXSMOV Coluna Tipo Tamanho Obrigatório

PK Observação

### Codprod

### Number

Y Código do produto

### Numtransitem

### Number

### N

### Numtransvenda

### Number

### N

### Numnota

### Number

Y Número da nota

### Numseq

### Number

### N

### Qt

### Number 20,6

Y Quantidade do item na nota

### Punit

### Number 18,6

Y Preço unitário que saiu na nota

### Ptabela

### Number 18,6

Y Preço de tabela do produto Negócio: Responsável por armazenar informações de itens da nota fiscal de saída. Informações essenciais para o funcionamento do maxMotorista. Utilizada por : maxMotorista 5.17 PlanosPagamentos Tabela

### M

XSPLPAG Coluna Tipo Tamanho Obrigatório

PK Observação

### Codplpag

### Varchar2

### S

S Código do cliente

### Descricao

### Varchar2

S Descrição da condição de pagamento

### Numdias

### Number

S Prazo médio

### Numpr

### Number

S Número da coluna de preço default 1

## Página 41

### Pertxfim

### Number

S Acréscimo para a tabela de preço.

### Vendabk

### Varchar2

S Venda com Boleto (S ou N) Caso S, deve existir cobranças que aceitem BOLETO

### Vlminpedido

### Number 12,2

S Valor mínimo para a condição de pagamento

### Prazo1

### Number

S Margem mínima para a condição de pagamento

### Tipoprazo

### Varchar2

S Informar

N Normal, B Bonificado, I Inativo

### Entrada

### Varchar2

N Aceita entrada na condição de pagamento Negócio: Tabela utilizada para armazenar os planos de pagamentos “Condições Comerciais”. 5.18 Pracas Tabela

MXSPRACA Coluna Tipo Tamanho Obrigatório

PK Observação

### Codpraca

### Varchar2

### S

S Código

### Numregiao

### Varchar2

S Região

### Rota

### Number

S Rota

### Situacao

### Varchar2

S Situação (A=Ativo; I=Inativo)

### Praca

### Varchar2

S Praça Negócio: Tabela/EndPoint que grava as informações relacionadas as praças dos clientes. A informação de praça é usada para se realizar filtragem e agrupamento de pedidos de acordo com a praça do cliente. Por se tratar de uma informação/funcionalidade secundária seus campos/preenchimento não são obrigatórios. Caso seja alimentada, é necessário um vínculo do “código praça” na tabela de clientes. Utilizado por : maxMotorista e maxRoteirizador Relacionamento :

### Mxspraca.Codpraca

### Mxsclient.Codpraca.

## Página 42

Obs : Na tabela de cliente será preenchido o CODPRACA, onde através deste vínculo é possível descobrir qual é a rota do cliente (MX

SPRACA.ROTA = MXS_ROTA_EXP.CODROTA), ou também é possível indicar diretamente no cadastro do cliente q ual é sua rota(MXSCLIENT.CODROTA.

MXS_ROTA_EXP.CODROTA). Este relacionamento irá depender de qual ERP está se realizando a integração. 5.19 PrestacoesTitulos í tulos) Tabela

ERP_MXSPREST Coluna Tipo Tamanho Obrigatório

PK Observação

### Numbanco

### Number

S Número do banco

### Valordesc

### Number

N Valor de desconto

### Vpago

### Number

N Valor Pago

### Codcli

### Varchar2

S Código do cliente

### Valormulta

### Number

N Valor da Multa

### Codfilial

### Varchar2

S Código da filial

### Cartorio

### Varchar2

S Flag para informar se o título está em cartório (S ou N)

### Valor

### Number 18,6

S Valor do título

### Prest

### Varchar2

### S

S Número da prestação em caso de parcelamento

### Dtvencorig

### Date

S Data de vencimento original

### Codusur

### Varchar2

S Código do Vendedor

### Numtransvenda

### Number

### N

S Número de transação de venda (Identificador Unico

### Dtvenc

### Date

S Data de vencimento

### Dtpag

### Date

N Data de pagamento

### Vltxboleto

### Number

N Valor taxa de boleto

### Valororig

### Number 18,6

S Valor original

## Página 43

### Protesto

### Varchar2

S Flag para informar se o título está protestado (S ou N)

### Dtemissao

### Date

S Data de emissão do título

### Codcob

### Varchar2

S Código da cobrança

### Codplpag

### Number

S Código do plano de pagamento

### Percom

### Number

N Percentual de desconto comercial

### Duplic

### Number

S Número da duplicata

### Status

### Varchar2

S Situação do título Aberto ou P Pago)

### Nossonumbco

### Varchar2

S Código cliente no banco (Pronta Entrega)

### Boleto

### Varchar2

N Flag para informar se tem boleto Negócio: Tabela utilizada para armazenar os títulos financeiros em abertos ou fechados dos clientes , utilizado para disponibilizar informações de cobranças para o maxMotorista. Utilizado por : maxMotorista. Relacionamento :

(ERP_MXSPREST.CODCLI = MXSCLIENTE.CODCLI) 5.20 Produto s Tabela

MXSPRODUT Coluna Tipo Tamanho Obrigatório

PK Observação

### Aceitavendafracao

### Varchar2

N Aceita venda fracionada . (S ou N)

### Altura

### Number

N Altura do Produto

### Checarmultiplovendabnf

### Varchar2

N Checar múltiplo em vendas bonificadas. Verifica obrigatoriedade de venda em quantidades múltiplas no caso de pedido de venda bonificado/troca (TPS. 5, 6, 11 e 12).

### Classe

### Varchar2

N Classe produto

### Classificfiscal

### Varchar2

N Classificação fiscal (Tare DF) *SE Pronta Entrega.

## Página 44

### Codauxiliar

### Varchar2

N Indica qual é o código de barras do produto na unidade de venda , no caso de venda por embalagem se torna obrigatório.

### Codauxiliar2

### Varchar2

N Indica qual é o código de barras do produto na unidade master.

### Codcategoria

### Varchar2

N Código da Categoria vinculado ao produto

### Coddistrib

### Varchar2

N Indica o código da distribuição, utilizado para determinar se a separação será por Pedido ou por Rua

### Codepto

### Varchar2

N Código do departamento vinculado ao produto

### Codfab

### Varchar2

N Código do produto utilizado pelo fornecedor destacado na NF de entrada.

### Codfilial

### Varchar2

N Vincula o produto somente a uma filial, caso seja nulo (ESC), esse produto será utilizado em todas as filiais.

### Codfilialretira

### Varchar2

N Indica o código da filial retira padrão.

### Codfornec

### Varchar2

N Código do fornecedor vinculado ao produto

### Codlinhaprod

### Number

N indica qual é a linha que o produto pertence cadastro

### Codmarca

### Varchar2

N Código da Marca vinculado ao produto

### Codprincipativo

### Number

N Indica o princípio ativo do produto, geralmente medicamentos.

### Codprod

### Varchar2

### S

S Código identificador do produto

### Codprodprinc

### Varchar2

N Define se o produto é master (mesmo código de produto) ou filho (código diferente)

### Codsec

### Varchar2

N Código da Seção vinculado ao produto cadastro

## Página 45

### Codsubcategoria

### Varchar2

N Código da Subcategoria vinculado ao produto

### Confaz

### Varchar2

### N

### Confaz

### Controladoibama

### Varchar2

N Informa se o produto é controlado pelo IBAMA, se for, só será permitido vender para cliente que tenha registro no IBAMA.

### Custorep

### Number

N Preço de compra cadastrado pelo usuário ou atualizado pelas condições comerciais do pedido de compra.

### Custorepzfm

### Number

### N

### Custorepzfm

### Dadostecnicos

### Varchar2

N Informa os dados técnicos do produto.

### Descricao

### Varchar2

S Descrição do produto

### Dirfotoprod

### Varchar2

N Indica o caminho para que as demais rotinas localizem a imagem salva do produto.

### Dtcadastro

### Date

N Data do cadastro do produto

### Dtexclusao

### Date

N Data Exclusão

### Dtvenc

### Date

N Data Vencimento

### Embalagem

### Varchar2

S Unidade da embalagem de venda do produto (Unidade de Venda)

### Embalagemmaster

### Varchar2

S Unidade da embalagem de Master do produto (Unidade de Compra)

### Freteespecial

### Varchar2

N Usa frete especial

### Importado

### Varchar2

N Define se o produto é importado utilizado no módulo de importação.

### Informacoestecnicas

### Varchar2

N Informações técnicas

### Multiplo

### Number

S Indica qual é o múltiplo do produto, não poderá realizar operações se a quantidade não for múltipla ao informado nesse campo

## Página 46

### Nbm

### Varchar2

N Nomenclatura Comum do Mercosul que posiciona a mercadoria para efeitos tributação.

### Nomeecommerce

### Varchar2

N Nome do produto para e commerce

### Numoriginal

### Varchar2

N Número original

### Obs

### Varchar2

N Observação:

### Obs2

### Varchar2

N Define se o produto está fora de linha para compra

### Pcomext1

### Number

N % Vendedor externo

### Pcomint1

### Number

N % Vendedor interno

### Pcomrep1

### Number

N Representante

### Percbonificvenda

### Number

N % Bonificação de Venda

### Percdifaliquotas

### Number

N Indica o percentual de diferença de alíquota.

### Percdiferencakgfrio

### Number

N Indica o percentual de diferença no kg de produtos frios.

### Percipi

### Number

N Percentual IPI utilizado na entrada da mercadoria

### Percipivenda

### Number

### N

### Percipivenda

### Perindeniz

### Number

N Indenização

### Pesobruto

### Number 12,6

S Indica Peso Bruto do produto

### Pesobrutomaster

### Number

N Indica o peso bruto da embalagem master

### Pesoliq

### Number 12,6

S Indica Peso Líquido do produto

### Pesopeca

### Number

N Indica o peso médio de uma peça de produtos do tipo frios

### Pesovariavel

### Varchar2

N Indica se o peso e variável.

### Prazomediovenda

### Number

N Prazo Médio de Venda. O Produto não poderá ser vendido quando o Prazo Médio é maior que o informado.

### Precofixo

### Varchar2

N Preço fixo

### Precomaxconsum

### Number

N Preço máximo consumidor atual

## Página 47

### Precomaxconsumzfm

### Number

### N

### Precomaxconsumzfm

### Psicotropico

### Varchar2

N Psicotrópico

### Qtdemaxseparpedido

### Number

N Indica a quantidade máxima para separação por pedido.

### Qtminimaatacado

### Number

### N

### Qtminimaatacado

### Qtunit

### Number

S Quantidade unitária na embalagem de venda

### Qtunitcx

### Number

S Quantidade unitária de compra

### Revenda

### Varchar2

N Define se o produto é para revenda. (S ou N)

### Tipocomissao

### Varchar2

N Define se o produto utiliza Comissão Padrão ou Comissão por Lucratividade.

### Tipoestoque

### Varchar2

N Indica se o produto é frio (FR) ou padrão (PA)

### Tipomerc

### Varchar2

N Tipo de mercadoria

### Unidade

### Varchar2

S Unidade de venda (controle do estoque)

### Unidademaster

### Varchar2

S Unidade de compra junto ao fornecedor

### Usapmcbasest

### Varchar2

N Usa PMC para base de cálculo da ST

### Verifcramoativcalcst

### Varchar2

N Caso esteja marcado como sim(S), no momento do cálculo do ST, será verificado no ramo de atividade do cliente, se irá calcular o ST.

### Vlipiporkg

### Number

### N

### Vlipiporkg

### Vlipiporkgvenda

### Number

N Indica o IPI/KG venda.

### Vlpauta

### Number

N Valor de pauta para cálculo do ST utilizado na entrada da mercadoria

### Vlpautaipivenda

### Number

N Indica a pauta IPI venda.

### Pericm

### Number 10,2

### N

### % Icms

### Volume

### Number

S Indica o volume do produto m ³ Negócio: Responsável por armazenar os dados de produto.

## Página 48

5.21 Regioes Tabela

MXSREGIAO Coluna Tipo Tamanho Obrigatório

PK Observação

### Numregiao

### Varchar2

### S

S Código da região

### Perfrete

### Number

N % de frete

### Perfreteespecial

### Number

N % de frete especial

### Perfreteterceiros

### Number

N % de frete de terceiros

### Regiao

### Varchar2

S Descrição da Região

### Regiaozfm

### Varchar2

N Região ZFM

### Status

### Varchar2

S Indica se a região está ativa ou inativa (

A Ativa

I Inativa

### Vlfretekgvenda

### Number

N Valor do frete/Kg venda

### Uf

### Varchar2

S Unidade federativa (Estado)

### Codestabelecimento

### Varchar2

N Destinado ao processo Broker

### Numtabela

### Varchar2

N Destinado ao processo Broker Informar o código da tabela da indústria a ser visualizado pelo vendedor no aplicativo

### Codrepresentante

### Varchar2

N Destinado ao processo Broker

### Codfilial

### Varchar2

S Código da filial vinculada à região Negócio : Responsável por armazenar as regiões, utilizada para vínculo com a tabela de preço , porém também é utilizada para a funcionalidade de agrupamento no maxRoteirizador, que faz o processo de formatar automaticamente “pré carregamentos”. Utilizado por maxRoteirizador Relacionamento

### Mxsregiao.Numregiao

### Mxs

### Client

### .Numregiao.

## Página 49

5.22 RotasExps Tabela/EndPoint

### M

### Xs

ROTAEXP Coluna Tipo Tamanho Obrigatório

PK Observação

### Codrota

### Number

### S

Y Código da Rota

### Descricao

### Varchar2

S Descrição da rota

### Diasentrega

### Number

N Dias de entrega da rota.

### Tipocomissao

### Varchar2

N Tipo de comissão

### Kmrota

### Number 10,2

N KM Máximo da rota

### Vldiaria

### Number 10,4

N Valor da Diária

### Seqentrega

### Number

N Sequencia de entrega da rota

### Vlmincarreg

### Number 10,2

N Valor mínimo de carregamento da rota

### Qtentrega

### Number

N Quantidade máxima de entregas

### Vlfreteentrega

### Number 10,4

N Valor de frete da rota

### Situacao

### Varchar2

S ‘A’ Ativa e ‘I’ Inativa. Negócio Tabela/EndPoint que grava as informações relacionadas as rotas de entregas. A informação de rota é usada para se realizar filtragem e agrupamentos de pedidos de acordo com a rota do cliente. Mesmo de tratando de uma das principais informações que o maxRoteirizador utiliza as informações não são obrigatórias. Será utilizada somente caso o cliente trabalhe com o processo de organizar os clientes por rota. Caso seja alimentada, é necessário o vínculo do “código rota” na tabela de clientes. Utilizado por maxRoteirizador Relacionamento

### Mxsr

### Otaexp

### Codrota

### Mxs

### Client

CODROTA Obs : O vínculo de rota também poderá ser realizado através do relacionamento de praça x cliente. Explicação da regra no item 5.18 “Praças”.

## Página 50

5.23 Supervisores Tabela

MXSSUPERV Coluna Tipo Tamanho Obrigatório

PK Observação

### Codsupervisor

### Number

### S

S Código

### Cod_Cadrca

### Varchar2

N Código de vendedor com figura de supervisor

### Codgerente

### Varchar2

N Código do gerente

### Nome

### Varchar2

S Nome Negócio: Responsável por armazenar as informações de supervisores do sistema. Possui ligação com a tabela de vendedores Utilizado por : maxMotorista e maxRoteirizador. Relacionamento :

### Mxssuperv.Codsupervisor

MXSUSUARI.CODSUPERVISOR 5.24 Carregamentos Tabela/EndPoint

MXSCARREG Coluna Tipo Tamanho Obrigatório

PK Observação

### Numcar

### Number

### Y

Y Número do Carregamento

### Dtsaida

### Varchar2

N Data de Saída do carregamento.

### Codmotorista

### Number

Y Código do Motorista

### Codveiculo

### Number

Y Código do Veículo

### Totpeso

### Number

Y Peso total

### Totvolume

### Number

Y Volume Total

### Vltotal

### Number

Y Valor Total

### Dtfecha

### Date

N Data de fechamento do carregamento

### Obs_Destino

### Varchar

N Observação ou destino do carregamento

### Numnotas

### Number

Y Número de Notas

## Página 51

### Codconf

### Number

N Código do conferente

### Dt_Cancel

### Date

N Data de cancelamento

### Datamon

### Date

Y Data de montagem

### Codfuncmon

### Number

N Código do funcionário que montou o car.

### Dtfat

### Date

Y Data de faturamento do carregamento

### Dtsaidaveiculo

### Date

N Data de saída do carregamento. Negócio: Responsável por armazenar as informações de carregamentos que foram montados pelo ERP. Precisamos consultar estas informações do ERP por dois motivos : O maxRoteirizador possuir uma funcionalidade/fluxo onde é possível consultar um carregamento que foi montado no ERP e realiza r somente o processo de roteirização. Esta é uma tabela/en dpoint chave para o maxMotorista, pois é através dela que realizado uma série de validações no fluxo e comportamento da aplicação. Utilizado por : maxMotorista e maxRoteirizador. Relacionamento :

### Mxs

### Carreg

### Numcar

### Mxshistoricopedc

NUMCAR 5.25 Usuari s Tabela

MXSUSUARI Coluna Tipo Tamanho Obrigatório

PK Observação

### Areaatuacao

### Varchar2

N Área de Atuação

### Bloqueio

### Varchar2

S Bloqueio (S ou N)

### Coddistrib

### Varchar2

N Código de distribuição

### Codsupervisor

### Varchar2

S Supervisor

### Codusur

### Varchar2

### S

S Código

### Email

### Varchar2

### N

E Mail

### Nome

### Varchar2

S Nome

### Numserieequip

### Number

N Num. Série Equipamento

## Página 52

### Percacresfv

### Number

N % Acréscimo Venda

### Percent

### Number

N %Comissão VV

### Percent2

### Number

N Comissão VP

### Permaxvenda

### Number

N % Máx. Acréscimo

### Proxnumped

### Number

N Numeração de pedidos usada pelo sistema. Não pode se repetir. Dois RCA´s não podem ter mesmo número de pedido. A numeração do pedido é iniciada pelo código do RCA. Formato: RRRRNNNNNN, RRRR é o código do

RCA, NNNNNN é a numeração do pedido.

### Proxnumpedforca

### Number

N Esta numeração marca a sequência de pedidos do próprio RCA. Geralmente está numeração controla a numeração de pedidos no aparelho do RCA.

### Proxnumpedweb

### Number

N Esta numeração marca a sequência de pedidos do próprio RCA. Geralmente está numeração controla a numeração de pedidos no aparelho do RCA

### Qtpedprev

### Number

N Quantidade do pedido previsto

### Telefone1

### Varchar2

S Telefone 1

### Telefone2

### Varchar2

N Telefone 2

### Tipovend

### Varchar2

N Tipo de venda (I Interno, E Externo, R Representante, P Profissional)

### Usadebcredrca

### Varchar2

N Usa Déb. Crédito RCA? (esp. FV) (S ou N)

### Validaracrescdescprecofixo

### Varchar2

N Valida crédito e desconto preço fixo

### Vlvendaminped

### Number

N Valor venda mín. por pedido

### Proxnumnotacontigencia

### Number

N Próximo número da nota em contingência (Pronta Entrega)

## Página 53

### Seriecontigencia

### Number

N Serie da nota em contingência (Pronta Entrega) Negócio: Responsável por armazenar os cadastros de vendedores. Esta informação é utilizada para a utilização da funcionalidade de agrupamento por vendedor no maxRoteirizador. Informações como telefone do vendedor também são utilizadas no maxMotorista para disponibilizar este número para o motorista que está realizando entregas deste vendedor. Utilizado por : maxMotorista e maxRoteirizador. Relacionamento :

(MXSHISTORICOPEDC.CODUSUR = MXSUSUARI.CODUSUR) 5.26 Veiculos Tabela/EndPoint

ERP_MXSVEICUL Coluna Tipo Tamanho Obrigatório

PK Observação

### Codveiculo

### Number

### S

Y Identificador do veículo

### Descricao

### Varchar2

S Descrição do veículo

### Placa

### Varchar2

S Placa

### Marca

### Varchar2

N Marca do veículo

### Quantidade_Palete

### Number

N Quantidade de paletes

### Volume

### Number 10,4

S Capacidade de volume do veículo

### Peso

### Number 10,2

S Capacidade de peso do veículo

### Situacao

### Varchar2

S Situação do Veículo.

### Tipo_Veiculo_Erp

### Varchar2

N Tipo Veículo

### Proprio

### Varchar2

N Se o caminhão é próprio ou não

### Id_Filial

### Varchar2

S Filial

### Altura

### Number 10,3

N Altura do veículo

### Largura

### Number 10,3

N Largura do caminhão

### Comprimento

### Number 10,3

N Comprimento do veículo

### Observacao

### Varchar2

N Observação

### Rastreado

### Varchar2

N Rastreado

## Página 54

### Placa_Uf

### Varchar2

S UF da placa do veículo.

### Placa_Cidade

### Varchar2

S Cidade da placa. Negócio: Responsável por armazenar os cadastros veículos. Utilizado por : maxMotorista e maxRoteirizador. Relacionamento :

### M

### Sx

### _Veiculos

### Codveiculo

### Mxscarreg

### Codveic

### Ulo)

## Página 55

### Visão Geral De Endpoints Do

### Maxroteirizador

### (Saída

### Retorno

S Os carregamentos montados e roteirizados pelo maxRoteirizador serão disponibilizados em nossa API e devem ser consumidos pelo serviço do ERP. A responsabilidade da nossa API é manter os dados de carregamentos e pedidos sempre atualizados e disponíveis. A API é um simples ouvinte, o serviço de gravação de dados deve gerar requisições à nossa API solicitando os pedidos confecci onados e disponíveis para serem persistidos no banco de dados ERP. (Fluxo saída/retorno ao se salvar um carregamento no maxRot eirizador) Gravar informações no EndPoint Carregamentos Após este carregamento ser gravado, o cabeçalho do pedido será manipulado, onde será atualizado três campos no EndPoint HistoricosPedidosCapas numcar : inserindo o número de carregamento do pedido. posição : atualizar a posição para ‘M’ de montado. numseqentrega : com o número int de qual será ordem desta entrega (retornado pelo motor de cálculo do maxRoteirizador com a melhor rota). É responsabilidade do ERP voltar a posição dos pedidos para a posição liberado

L ’ e realizar outras persistências quando um carregamento for cancelado, para que os pedidos voltem a ficar aptos a serem montados e roteirizados. Obs : A solução maxMoto rista não retorna nenhuma informação diretamente para o ERP portando não haverá retornos/saídas relacionadas a este produto.

## Página 56

StatusPedido s (GET) Para obtenção dos pedidos pendentes de integração com o ERP, fazer chamadas GET no endpoint e parâmetros a seguir: http://URL_API_SAIDA:PORTA/api/v1/StatusPedidos/0,1,2,5,9/1 (Pedidos) http://URL_AP I_SAIDA:PORTA/api/v1/StatusPedidos/0,1,2,5,9/2 (Orçamentos) 6.1.1 Hierarquia 1 Objeto Raiz do Json Coluna Tipo Tamanho Obrigatório

PK Observação sucess

JSON Lista de pedidos prontos para importação error

JSON Lista de pedidos com algum erro

CONSIDERAÇÕES FINAIS Este documento é um mapeamento de nossa estrutura de dados, contudo podem existir a necessidade de ajustes em nossa interface de integração, bem como a criação e/ou alteração de rotas/endpoints. Qualquer necessidade de mudanças/alterações na API de integração ou serviço de extração os envolvidos deverão ser imediatamente notificados com antecedência.

## Página 58

HISTÓRICO DE ALTERAÇÕES NO LAYOUT Versão EndPoint/Seção Alteração

OBS 2019.06.1 Criação do layout de acordo com o novo formato. 2019.06.19 Clientes Inserção do campo CODROTA Necessário, pois alguns erps possuem esse vínculo direto sem a necessidade de relacionamento com praça. 2019.06.19 5.10 HistoricosPedidosCapas Inserção do campo

### Codendentcli

V ínculo entre o pedido e o endereço de entrega alternativo. 2019.07.02

5.8 Emprs Retirado o campo CODMOTORISTA como pk. Como esta tabela grava informações de motorista e empregados o campo codmotorista não pode ser obrigatório. 2019.07.02

5.8 Emprs Campo TIPO como chave composta. Além da MATRICULA ser pk , o campo TIPO também deve ser, pois um funcionário ou motorista sempre terá matricula e será pelo campo TIPO que iremos diferenciar cada tipo de usuário. 2019.07.02

5.10 HistoricoPedidosCapas Inserido OBS explicando os status do campo POSICAO. Conforme alinhado em reunião com a equipe Sanhya, iremos trabalhar com os tipos de POSICAO que foram inseridos na obs da explicação do campo.
