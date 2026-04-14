# Dicionário de Dados de Integração — Base de Conhecimento maxPedido

**Palavras-chave**: integração, API, endpoints, tabelas, campos, ERP, Winthor, maxPedido, maxGestão, maxMotorista, maxRoteirizador, dados, cadastros, pedidos, produtos, clientes, notas fiscais, tributação, estoque, financeiro, XML, JSON, REST, JWT, autenticação, extrator, retorno, saída, payload, obrigatoriedade, chave primária, relacionamento, layout, dicionário, dados, extração, carga, entrada, saída, Swagger, token, compactação

**Sistema**: maxPedido, maxGestão, maxMotorista, maxRoteirizador

**Área**: Integração

---

## 1. Apresentação e Objetivo

### Apresentação

Este documento fornece as informações necessárias das APIs de Integração da Máxima, com foco na integração de nossas soluções aos diversos ERPs do mercado atacadista distribuidor. As Web APIs da Máxima foram construídas sob a plataforma Microsoft .NET Core 2.2, padrão de comunicação REST, trafegando objetos JSON conforme padronizado no Layout de Integração Físico (PDF) ou online na própria API (Swagger). Possui controle de logs para cada registro enviado ou recebido, possibilitando à parte ativa da integração (extrator de dados do ERP) um melhor controle dos dados integrados. Utiliza JWT Bearer Token (RFC 7519) como forma padrão de autenticação (multi‑tenant) e aceita métodos de compactação do canal de dados pelos algoritmos GZIP ou Brotli. O cliente não precisa se preocupar com a infraestrutura para utilizar as soluções adquiridas — ela fica 100% na nuvem da Máxima na AWS (exceto clientes com ERP WinThor).

### Objetivo do Documento

O objetivo deste documento é fornecer os endpoints utilizados na integração de ERPs com a plataforma da Máxima Sistemas. O documento contém uma visão geral das informações integradas a nível de tabelas de banco de dados (via endpoints) e negócio. As tabelas do banco de dados das maxSoluções citadas podem não ser integradas em sua totalidade, sendo dependente de uma entrevista de negócio para definição do layout ideal de integração.

---

## 2. Clientes Winthor

A integração da Máxima Sistemas com o WinThor é composta por 3 Web APIs. Toda a comunicação entre as APIs é compactada, utiliza‑se JWT Bearer Token para autenticação de cada canal de comunicação, através de um login exclusivo de acesso de cada cliente Máxima. Cada token gerado tem a assinatura única do cliente; cada cliente será direcionado para seu banco de dados exclusivo (multi‑tenant). A responsabilidade da integração é 100% da Máxima.

### 2.1 API Extrator de Dados Máxima

A função da API Extrator é gerenciar o tráfego de dados entre o WinThor e a nuvem da Máxima, monitorando as inclusões/alterações/deleções de registros deste ERP, consolidando/trafegando somente dados que requerem atualização na nuvem, evitando o envio de dados já existentes ou desnecessários, garantindo que todas as soluções recebam os dados atualizados para funcionamento de seus recursos, além de gerir os dados enviados destas soluções pela nuvem da Máxima (pedidos, clientes entre outros) ao ERP. É recomendado que seja publicada na mesma infraestrutura de rede do WinThor, minimizando a latência no tráfego de dados entre a API e o banco de dados Oracle do WinThor; o servidor desta API deve ser Linux.

### 2.2 API de Integração Máxima (Entrada)

A função da API Integração da Máxima, única para todos os clientes, é receber dados oriundos da API Extrator de Dados da Máxima, respondendo 100% aos seus comandos de forma passiva. Persiste os dados no banco de dados exclusivo para cada cliente. Esta API é a porta de entrada dos dados a serem integrados com o WinThor.

### 2.3 API de Integração Máxima (Retorno/Saída)

A função da API Integração da Máxima, única para todos os clientes, é retornar dados à API Extrator de Dados da Máxima, respondendo 100% aos seus comandos de forma passiva. Esta API é a porta de saída dos dados a serem integrados com o WinThor.

---

## 3. Clientes Não Winthor (Outros ERPs)

A integração da Máxima Sistemas com ERPs, exceto WinThor, é composta por 2 Web APIs. Toda a comunicação com as APIs deverá ser compactada, utiliza‑se JWT Bearer Token para autenticação de cada canal de comunicação, através de um login exclusivo de acesso de cada cliente Máxima. Cada token gerado tem a assinatura única do cliente, e cada cliente será direcionado para seu banco de dados exclusivo (multi‑tenant). Cada requisição não poderá ter mais que 10 MB; sugere‑se fragmentar o envio de dados em pacotes de no máximo 5.000 registros. Para evitar erros de sobrecarga na API, o envio de todos os registros poderá acontecer somente no envio da carga total (início da implantação); para as atualizações é necessário enviar cargas incrementais, ou seja, é vedado o delete e envio de todos os registros nos endpoints. A responsabilidade da integração é 100% do parceiro/cliente, referente à criação de uma ferramenta de extração de dados do ERP.

### 3.1 API Extrator de Dados (responsabilidade do cliente)

O cliente deve construir, manter e dar garantia na consistência dos dados integrados com a nuvem da Máxima (necessário envio do Layout de Integração Máxima aos Clientes), conforme API Extrator de Dados Máxima (quando integrado com o WinThor).

### 3.2 API de Integração Máxima (Entrada)

A função da API Integração da Máxima, única para todos os clientes, é receber dados oriundos da API Extrator de Dados do Cliente, respondendo 100% aos seus comandos de forma passiva. Persiste os dados no banco de dados exclusivo para cada cliente. Esta API é a porta de entrada dos dados a serem integrados com o ERP do cliente.

### 3.3 API de Integração Máxima (Retorno/Saída)

A função da API Integração da Máxima, única para todos os clientes, é retornar dados à API Extrator de Dados do Cliente, respondendo 100% aos seus comandos de forma passiva. Esta API é a porta de saída dos dados a serem integrados com o ERP do cliente.

### 3.4 Integração com Cartão de Crédito

Processo de integração de cartão de crédito no maxPedido. A integração com as operadoras é toda feita pelo MaxPag; para a integração com outros ERPs precisamos apenas saber quando um pedido foi cancelado ou faturado. Existem dois endpoints para auxiliar:

- **GET** `https://intpdv-hmg.soluocoesmaxima.com.br:81/api/v1/MovimentacoesCartaoCredito/NumPeds/{status}`  
  Retorna os pedidos feitos com cartão de crédito, conforme o status da operação.  
  Status possíveis: 0 = Nenhum, 1 = Pré‑Autorizado, 2 = Estornado, 3 = Autorizado, 4 = Cancelado, 5 = Negado, 6 = Agendado, 7 = NãoFinalizado, 8 = Pendente, 9 = Abortado.

- **PUT** `https://intpdv-hmg.soluocoesmaxima.com.br:81/api/v1/MovimentacoesCartaoCredito`  
  Atualiza o status da operação de cartão de crédito, efetivando ou não a operação.  
  Corpo da requisição (JSON):
  ```json
  {
    "numPed": "string",
    "numPedRca": "string",
    "valorAtendido": 0,
    "posicao": "string"
  }
  ```
  Onde `posicao` pode ser "C" (Cancelado) ou "F" (Faturado). `valorAtendido` é o valor a ser debitado no cartão, podendo ser menor que o pré‑autorizado em caso de cortes ou faltas.

#### Fluxo adotado:
1. Aplicação no ERP consulta a cada 10 minutos pedidos pré‑autorizados (status = 1) via GET.
2. Obtém o estado desses pedidos no ERP (cancelado ou faturado) e atualiza com PUT.

---

## 4. Visão Geral dos Conceitos Integrados

### Conceitos e Responsabilidades

As informações enviadas aos endpoints abaixo são consultadas pelas soluções da Máxima Sistemas. Esses dados são provenientes do ERP e armazenados na base de dados do cliente na nuvem da Máxima. A entrada desses dados é dependente do extrator de dados. Os itens detalhados em amarelo são, a nível de dados, os requisitos mínimos de endpoints/campos.

A responsabilidade das ações GET (obter), PUT (atualizar), POST (adicionar) e DELETE (excluir) são do extrator de dados. As APIs de Integração da Máxima são passivas, ou seja, os dados são recebidos/retornados sob demanda de requisições da API Extrator de Dados para o ERP. A API é um simples ouvinte; portanto, é necessário que a API Extrator de Dados faça requisições às nossas APIs para sincronizar os dados com o ERP.

A responsabilidade da API é manter os dados atualizados em nosso banco de dados. Exemplo: o cadastro do cliente é alterado no ERP; nossa API aguarda a notificação/agendamento da API Extrator de Dados (GET, PUT, POST ou DELETE) para executar a ação. Outro exemplo: é confeccionado um pedido no aplicativo do vendedor; o pedido é inserido em nosso banco de dados e nossa API o disponibiliza para ser consumido pela API Extrator de Dados e inserido no banco de dados do ERP.

O serviço de extração e gravação de dados do/no ERP é de responsabilidade do cliente, exceto para o ERP WinThor. Neste documento são fornecidas todas as informações e orientações necessárias para a troca de informações entre os bancos da Máxima e os ERPs. Contudo, este é um documento vivo, em constante atualização; a versão mais atualizada estará disponível no Portal da Máxima.

Observa-se a necessidade do preenchimento de todos os campos que indicam obrigatoriedade. Em caso de o ERP não conter um ou mais campos, estes devem ser preenchidos com valor default (consulte a Máxima para mais detalhes).

---

## 5. Orientações Técnicas

### API: Endereços e Autenticação

- **Padrão**: HTTP REST, objetos JSON.
- **Operações**: GET, PUT, POST, DELETE.
- **Documentação online (Swagger)**:
  - Entrada (carga de dados): `http://URLEntrada:Porta/swagger`
  - Saída (retorno de pedidos, clientes etc.): `http://URLSaida:Porta/swagger`
- **Login (obter token JWT)**:
  - Endpoint: `http://URLEntrada:Porta/api/v(version)/Login` (ou similar para saída)
  - Exemplo de JSON de login:
    ```json
    {
      "login": "cole_seu_login_aqui",
      "password": "cole_sua_senha_aqui"
    }
    ```

### Exemplo de Requisição com Compactação GZIP (VB.NET)

```vbnet
Imports System.Net
Imports System.IO.Compression
Imports System.IO
Imports System.Text
Imports Newtonsoft.Json

Public Class Login
    Shared _retornologin As Retornologin

    Public Class Retornologin
        Public Success As Boolean
        Public Data_Criacao As DateTime
        Public Data_Expiracao As DateTime
        Public Token_De_Acesso As String
        Public Resposta As String
    End Class

    Private Sub EfetualoginAwsApi()
        Try
            If IsNothing(_retornologin) OrElse (Not IsNothing(_retornologin) AndAlso Now.AddMinutes(-60) >= _retornologin.Data_Expiracao) Then
                Dim token As New KeyValuePair(Of HttpStatusCode, String)
                Dim jsonLogin = "{""login"": ""xxxxxxxxxxxxxxx"", ""password"": ""xxxxxxxxxxxxxxx""}"
                Dim httpWebRequest As HttpWebRequest = CType(WebRequest.Create("http://URL_API:PORTA/Login"), HttpWebRequest)
                httpWebRequest.Headers.Add(HttpRequestHeader.AcceptEncoding, "gzip")
                httpWebRequest.Headers.Add(HttpRequestHeader.ContentEncoding, "gzip")
                httpWebRequest.ContentType = "application/json"
                httpWebRequest.Method = "POST"
                httpWebRequest.ContentLength = jsonLogin.Length
                Using streamWriter As New StreamWriter(httpWebRequest.GetRequestStream())
                    streamWriter.Write(jsonLogin)
                    streamWriter.Close()
                End Using

                Using response As HttpWebResponse = CType(httpWebRequest.GetResponse(), HttpWebResponse)
                    Dim receiveStream = response.GetResponseStream()
                    If response.ContentEncoding.ToLower().Contains("gzip") Then
                        receiveStream = New GZipStream(receiveStream, CompressionMode.Decompress)
                    End If
                    Dim readStream = New StreamReader(receiveStream, Encoding.UTF8)
                    token = New KeyValuePair(Of HttpStatusCode, String)(response.StatusCode, readStream.ReadToEnd)
                    response.Close()
                    readStream.Close()
                End Using
                If token.Key = HttpStatusCode.OK Then
                    _retornologin = JsonConvert.DeserializeObject(Of Retornologin)(token.Value)
                Else
                    Throw New Exception("Erro ao autenticar na Aws API Maxima.")
                End If
            End If
        Catch ex As Exception
            ' Tratamento de erro
        End Try
    End Sub
End Class
```

### Recomendações de Carga

- Cada requisição não pode ter mais que 10 MB.
- Sugere-se fragmentar o envio em pacotes de no máximo 5.000 registros.
- Para atualizações, **é vedado o DELETE e envio de todos os registros nos endpoints**; deve-se enviar cargas incrementais.

---

## 6. Introdução à Utilização do Dicionário de Dados

Abaixo segue o dicionário de dados utilizado para integração com outros ERPs. Cada endpoint/tabela faz parte de um contexto de negócio; algumas podem ser alimentadas via integração e outras por meio dos portais da Máxima (BackOffice).

O título (ex.: "5.1 Atividades") refere-se ao nome do endpoint utilizado na API de integração. A coluna "Coluna" descreve o nome técnico utilizado pela API; "Tipo" descreve o tipo de valor; "Tamanho" específica a quantidade máxima de caracteres; "Obrigatório" (S ou N) indica se o campo é obrigatório para o funcionamento da aplicação/funcionalidade; "PK" determina que o campo é obrigatório e é chave primária; "Observação" descreve de forma breve o contexto de negócio.

As tabelas/endpoints definidas na cor amarela (no original) são obrigatórias para o funcionamento básico das aplicações. Aqui, destacaremos essas obrigatoriedades no texto.

Caso não haja informação respectiva no ERP, estas deverão ser tratadas na integração para que sejam enviadas via dados default/fictícios, mantendo a integridade relacional entre as tabelas que compõem o negócio.

---

## 7. Endpoints de Entrada (maxPedido / maxGestão)

URL base: `http://URL_API_ENTRADA:PORTA/api/v2/NOME_ENDPOINT`

### 7.1 AcrescimosClientes — MXSACRESCIMOSCLIENTES

**Descrição**: Tabela utilizada para armazenar políticas de acréscimos por cliente.

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **DATAINI** (DATE): Data inicial de vigência.
- **DATAFIM** (DATE): Data final de vigência.
- **PERCACRESCIMO** (NUMBER, 22,8, obrigatório): Percentual de acréscimo sobre a tabela de preço.

**Relacionamentos**:
- FK para `MXSCLIENT` via `CODCLI`.

---

### 7.2 Mxsanexoclientes — MXSANEXOCLIENTES

**Descrição**: Tabela utilizada para armazenar os links dos anexos enviados para clientes.

**Campos principais**:
- **CGC** (VARCHAR2, 50, obrigatório, PK): CNPJ ou CPF do cliente.
- **CODIGOTIPO** (VARCHAR2, 50, obrigatório, PK): Código do tipo de documento cadastrado na central de configurações.
- **TIPO** (VARCHAR2, 200, obrigatório, PK): Descrição do tipo de documento.
- **HASH** (VARCHAR2, 4000, obrigatório, PK): Identificador único do arquivo.
- **LINK** (VARCHAR2, 4000): Link do anexo.
- **DTCADASTRO** (DATE): Data de cadastro.
- **CODUSUARIO** (NUMBER, 20): Código do usuário cadastrado no maxPedido.

---

### 7.3 Atividades — MXSATIVI

**Descrição**: Responsável por armazenar o ramo de atividade do cliente (ex.: Farmácia, Padaria, Bar). Obrigatório para o funcionamento básico.

**Campos principais**:
- **CODATIV** (VARCHAR2, 50, obrigatório, PK): Código.
- **RAMO** (VARCHAR2, 100, obrigatório): Descrição do ramo de atividades.
- **PERCDESC** (NUMBER, 5,2, obrigatório): % de acréscimo/desconto no preço de tabela.
- **CALCULAST** (VARCHAR2, 1, obrigatório): Flag para definir se irá calcular ST (S ou N).

**Relacionamentos**:
- FK em `MXSCLIENT` via `CODATV1`.

---

### 7.4 Brindes — MXSBRINDEEX

**Descrição**: Cabeçalho das campanhas de brinde.

**Campos principais**:
- **CODBREX** (VARCHAR2, 50, obrigatório, PK): Código de identificação da campanha.
- **DESCRICAO** (VARCHAR2, 200, obrigatório): Descrição da campanha.
- **DTINICIO** (DATE, obrigatório): Data início de vigência.
- **DTFIM** (DATE, obrigatório): Data final de vigência.
- **MOVCCRCA** (VARCHAR2, 1, obrigatório): Movimenta conta corrente do vendedor? (S ou N).
- **QTMAXBRINDES** (NUMBER, 18,6): Quantidade máxima de brindes.

---

### 7.5 BrindesPremios — MXSBRINDEEXPREMIO

**Descrição**: Itens que serão concedidos como brinde dentro da campanha.

**Campos principais**:
- **CODBREX** (VARCHAR2, 50, obrigatório, PK): Código da campanha.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **QT** (NUMBER, 18,6, obrigatório): Quantidade a ser concedida como brinde.
- **GRUPOREGRA** (NUMBER, 6, obrigatório, PK): Identificador do grupo de regra.
- **QTMAXBRINDES** (NUMBER, 18,6): Quantidade máxima do brinde (nível geral).
- **QTMAXBRINDESRCA** (NUMBER, 18,6): Quantidade máxima por vendedor.
- **QTMAXBRINDESCLI** (NUMBER, 18,6): Quantidade máxima por cliente.
- **QTMAXBRINDESSUPERV** (NUMBER, 18,6): Quantidade máxima por supervisão.

---

### 7.6 BrindesRestricoes — MXSBRINDEEXRESTRICOES

**Descrição**: Restrições das campanhas de brinde (ex.: campanha válida apenas para região Centro-Oeste).

**Campos principais**:
- **CODBREX** (VARCHAR2, 50, obrigatório, PK): Código da campanha.
- **CODIGOA** (VARCHAR2, 6, obrigatório, PK): Fixar "0".
- **CODIGO** (VARCHAR2, 50, obrigatório, PK): Código do tipo selecionado (região, filial, supervisor).
- **TIPO** (VARCHAR2, 2, obrigatório, PK): Tipo de restrição (R – Região, F – Filial, S – Supervisor).

---

### 7.7 BrindesValidacoes — MXSBRINDEEXVALIDACOES

**Descrição**: Validações das campanhas de brinde.

**Campos principais**:
- **CODBREX** (VARCHAR2, 50, obrigatório, PK): Código da campanha.
- **TIPO** (VARCHAR2, 2, obrigatório, PK): Tipo do filtro (D – Departamento, S – Seção, F – Fornecedor).
- **CODIGO** (VARCHAR2, 50, obrigatório, PK): Código do tipo selecionado.
- **TIPOVALOR** (VARCHAR2, 2, obrigatório, PK): Tipo de validação (PE – Peso, QT – Quantidade, VL – Valor).
- **GRUPOREGRA** (NUMBER, 6, obrigatório, PK): Identificador do grupo de regra.
- **VLMAX** (NUMBER, 18,6, obrigatório): Valor máximo.
- **VLMIN** (NUMBER, 18,6, obrigatório): Valor mínimo.

---

### 7.8 Categorias — MXSCATEGORIA

**Descrição**: Categorias de produto (pode ser utilizado como grupos de produtos).

**Campos principais**:
- **CODCATEGORIA** (VARCHAR2, 50, obrigatório, PK): Código.
- **CATEGORIA** (VARCHAR2, 100, obrigatório): Descrição da categoria.
- **CODSEC** (VARCHAR2, 50, obrigatório): Código da seção.

**Relacionamentos**:
- FK para `MXSPRODUT` via `CODCATEGORIA`.
- FK para `MXSSECAO` via `CODSEC`.

---

### 7.9 Cidades — MXSCIDADE

**Descrição**: Cidades do IBGE. Obrigatório.

**Campos principais**:
- **CODCIDADE** (VARCHAR2, 50, obrigatório, PK): Código da cidade.
- **CODIBGE** (VARCHAR2, 50, obrigatório): Código do IBGE.
- **NOMECIDADE** (VARCHAR2, 100, obrigatório): Nome da cidade.
- **UF** (VARCHAR2, 2, obrigatório): UF.

**Relacionamentos**:
- FK em `MXSCLIENT` via `CODCIDADE`.

---

### 7.10 Clientes — MXSCLIENT

**Descrição**: Cadastro de clientes (pessoa física ou jurídica). É um dos principais cadastros, obrigatório.

**Campos principais** (seleção dos mais relevantes; a tabela possui muitos campos):
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CLIENTE** (VARCHAR2, 100, obrigatório): Nome/Razão Social.
- **CGCENT** (VARCHAR2, 18, obrigatório): CNPJ ou CPF.
- **FANTASIA** (VARCHAR2, 100): Nome fantasia.
- **TIPOFJ** (VARCHAR2, 1, obrigatório): 'F' para pessoa física, 'J' para jurídica.
- **CODATV1** (VARCHAR2, 50, obrigatório): Código da atividade econômica (ramo). Relaciona com `MXSATIVI`.
- **CODCIDADE** (VARCHAR2, 50, obrigatório): Código da cidade. Relaciona com `MXSCIDADE`.
- **CODCOB** (VARCHAR2, 50): Código da cobrança padrão. Relaciona com `MXSCOB`.
- **CODPLPAG** (VARCHAR2, 50): Plano de pagamento padrão. Relaciona com `MXSPLPAG`.
- **CODPRACA** (VARCHAR2, 50): Praça de atendimento. Relaciona com `MXSPRACA`.
- **CODROTA** (VARCHAR2, 50): Rota de entrega. Relaciona com `MXSROTAEXP`.
- **CODUSUR1** (VARCHAR2, 50): Código do vendedor 1. Relaciona com `MXSUSUARI`.
- **CODUSUR2** (VARCHAR2, 50): Código do vendedor 2.
- **DTULTCOMP** (DATE): Data da última compra.
- **ENDERENT**, **BAIRROENT**, **CEPENT**, **CIDADEENT**, **ESTENT**: Endereço de entrega (obrigatórios).
- **EMAIL** (VARCHAR2, 100): E-mail.
- **IEENT** (VARCHAR2, 15): Inscrição estadual. Se não tiver, informar "ISENTO".
- **LATITUDE**, **LONGITUDE** (VARCHAR2, 20): Coordenadas geográficas.
- **BLOQUEIO** (VARCHAR2, 1, obrigatório): 'S' ou 'N' indicando se cliente está bloqueado.

**Relacionamentos**:
- FK para `MXSATIVI` via `CODATV1`.
- FK para `MXSCIDADE` via `CODCIDADE`.
- FK para `MXSCOB` via `CODCOB`.
- FK para `MXSPLPAG` via `CODPLPAG`.
- FK para `MXSPRACA` via `CODPRACA`.
- FK para `MXSROTAEXP` via `CODROTA`.
- FK para `MXSUSUARI` via `CODUSUR1` e `CODUSUR2`.
- Pode ter múltiplos endereços em `MXSCLIENTEENDERECOS`.

---

### 7.11 ClientesCreditosDisponiveis — MXSCLIENTECREDDISP

**Descrição**: Tabela utilizada para armazenar os valores que compõem o crédito disponível por cliente.

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **VLLIMITE** (NUMBER, 18,2, obrigatório): Valor do limite de crédito.
- **VLTITULOS** (NUMBER, 18,2, obrigatório): Valor em aberto de títulos.
- **VLPEDIDOS** (NUMBER, 18,2, obrigatório): Valor dos pedidos em aberto (ainda não faturados).
- **VLCHEQUES** (NUMBER, 18,2, obrigatório): Valor dos cheques em aberto.
- **VLCREDITO** (NUMBER, 18,2, obrigatório): Valor de crédito disponível.
- **VLLIMITECREDSUPPLI** (NUMBER, 18,2): Valor de crédito de terceiros.

---

### 7.12 ClientesEnderecos — MXSCLIENTEENDERECOS

**Descrição**: Endereços de entrega adicionais ao cadastro do cliente. Um cliente pode ter vários endereços.

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CODENDENTCLI** (NUMBER, 22, obrigatório, PK): Código do endereço.
- **CODPRACAENT** (NUMBER, 22, obrigatório): Código da praça de entrega.
- **ENDERENT** (VARCHAR2, 40, obrigatório): Endereço.
- **BAIRROENT** (VARCHAR2, 40, obrigatório): Bairro.
- **CEPENT** (VARCHAR2, 9, obrigatório): CEP.
- **MUNICENT** (VARCHAR2, 15, obrigatório): Município.
- **ESTENT** (VARCHAR2, 2, obrigatório): Estado.
- **COMPLEMENTOENT** (VARCHAR2, 80): Complemento.
- **APELIDOUNIDADE** (VARCHAR2, 40): Apelido da unidade.
- **PONTOREFER** (VARCHAR2, 40): Ponto de referência.

---

### 7.13 ClientesLocalizacoes — MXMP_LOCALIZACAO_CLIENTE

**Descrição**: Armazena o posicionamento GPS dos clientes.

**Campos principais**:
- **ID** (NUMBER, 10, obrigatório, PK): Identificador.
- **ID_CLIENTE** (VARCHAR2, 50, obrigatório): Código do cliente.
- **LATITUDE** (VARCHAR2, 22, obrigatório): Latitude.
- **LONGITUDE** (VARCHAR2, 22, obrigatório): Longitude.
- **PRECISAO** (VARCHAR2, 20): Precisão das coordenadas.
- **POR_CEP** (VARCHAR2, 1): 'S' ou 'N' indicando se obtido por CEP.
- **COORD_FIXA** (VARCHAR2, 1): 'S' ou 'N' indicando se coordenada fixa.

**Relacionamentos**:
- FK para `MXSCLIENT` via `ID_CLIENTE`.

---

### 7.14 ClientesPorVendedores — ERP_MXSUSURCLI

**Descrição**: Vínculos entre clientes e vendedores.

**Campos principais**:
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor.
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.

**Relacionamentos**:
- FK para `MXSUSUARI` via `CODUSUR`.
- FK para `MXSCLIENT` via `CODCLI`.

---

### 7.15 ClientesRef — MXSCLIREF

**Descrição**: Referências comerciais ao cadastro do cliente (ex.: para aprovação de crédito).

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **NOME** (VARCHAR2, 100): Nome da referência.
- **TELEFONE** (VARCHAR2, 20): Telefone.
- **CONTATO** (VARCHAR2, 50): Contato.
- **OBS** (VARCHAR2, 255): Observações.

**Relacionamentos**:
- FK para `MXSCLIENT` via `CODCLI`.

---

### 7.16 ClientesRegioes — MXSCLIENTREGIAO

**Descrição**: Relacionamento entre clientes e regiões/tabelas de preço.

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **NUMREGIAO** (VARCHAR2, 50, obrigatório, PK): Número da região/tabela de preço.
- **PERDESCMAX** (NUMBER, 6,2): % de desconto máximo da tabela de preço.
- **VDEFAULT** (VARCHAR2, 1, obrigatório): 'S' ou 'N' indicando se é padrão.

**Relacionamentos**:
- FK para `MXSCLIENT` via `CODCLI`.
- FK para `MXSREGIAO` via `NUMREGIAO`.

---

### 7.17 Clientes (Última Compra) — MXSCLIENT

**Descrição**: Tabela utilizada para armazenar a última compra do cliente (informações faturadas). É o mesmo campo `DTULTCOMP` da tabela `MXSCLIENT`.

**Campo principal**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **DTULTCOMP** (DATE): Data da última compra.

---

### 7.18 Cnaes — MXSCNAE

**Descrição**: Classificação Nacional das Atividades Econômicas.

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CODATIV** (VARCHAR2, 50, obrigatório, PK): Código da atividade.
- **PRINCIPAL** (VARCHAR2, 1): 'S' ou 'N' indicando se é a atividade principal.

---

### 7.19 Cobrancas — MXSCOB

**Descrição**: Tipos de cobrança (boleto bancário, cheque, dinheiro, cartão, etc.).

**Campos principais**:
- **CODCOB** (VARCHAR2, 50, obrigatório, PK): Código da cobrança.
- **COBRANCA** (VARCHAR2, 30, obrigatório): Descrição.
- **BOLETO** (VARCHAR2, 1, obrigatório): 'S' ou 'N' – se é boleto.
- **CARTAO** (VARCHAR2, 1, obrigatório): 'S' ou 'N' – se é cartão.
- **NIVELVENDA** (NUMBER, 2, obrigatório): Nível de venda.
- **PRAZOMAXIMOVENDA** (NUMBER, 4, obrigatório): Prazo máximo de venda.
- **CODFILIAL** (VARCHAR2, 20): Filial a que se aplica (se nulo, aplica a todas).
- **COBRANCABROKER** (VARCHAR2, 1): 'S' para operação broker.
- **VLMINPEDIDO** (NUMBER, 12,2): Valor mínimo de venda.
- **TXJUROS** (NUMBER, 6,2): % taxa de juros ao dia (Pronta Entrega).
- **PERCMULTA** (NUMBER, 7,4): % multa (Pronta Entrega).
- **TIPOVENDA** (VARCHAR2, 2, obrigatório): 'VP' – venda a prazo, 'VV' – venda à vista.
- **TIPOCOBRANCA** (VARCHAR2, 2, obrigatório): 'B' (boleto), 'C' (cartão), 'CH' (cheque), 'D' (dinheiro), 'DU' (duplicata), 'T' (transferência bancária).

---

### 7.20 CobrancasClientes — MXSCOBCLI

**Descrição**: Cobranças vinculadas ao cadastro do cliente.

**Campos principais**:
- **CODCOB** (VARCHAR2, 50, obrigatório, PK): Código da cobrança.
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.

**Relacionamentos**:
- FK para `MXSCOB` via `CODCOB`.
- FK para `MXSCLIENT` via `CODCLI`.

---

### 7.21 CobrancasPlanosPagamentos — MXSCOBPLPAG

**Descrição**: Relações entre cobrança e plano de pagamento.

**Campos principais**:
- **CODCOB** (VARCHAR2, 50, obrigatório, PK): Código da cobrança.
- **CODPLPAG** (VARCHAR2, 50, obrigatório, PK): Código do plano de pagamento.

**Relacionamentos**:
- FK para `MXSCOB` via `CODCOB`.
- FK para `MXSPLPAG` via `CODPLPAG`.

---

### 7.22 ComissoesRegioes — MXSCOMISSAOREGIAO

**Descrição**: Comissões progressivas por região.

**Campos principais**:
- **CODFAIXA** (VARCHAR2, 50, obrigatório, PK): Código da faixa.
- **CODEPTO** (VARCHAR2, 50): Código do departamento.
- **CODFILIAL** (VARCHAR2, 20): Código da filial.
- **CODPROD** (VARCHAR2, 50): Código do produto.
- **CODSEC** (VARCHAR2, 50): Código da seção.
- **DTINICIO** (DATE, obrigatório): Data inicial.
- **DTFIM** (DATE, obrigatório): Data final.
- **NUMREGIAO** (NUMBER, 10): Número da região.
- **PERCOM** (NUMBER, 8,4): % comissão.
- **PERCOMEXT** (NUMBER, 8,4): % comissão externa.
- **PERCOMINT** (NUMBER, 8,4): % comissão interna.
- **PERDESCINI** (NUMBER, 12,6, obrigatório): % desconto inicial.
- **PERDESCFIM** (NUMBER, 12,6, obrigatório): % desconto final.
- **TIPO** (VARCHAR2, 2, obrigatório): Tipo de comissão: 'P' (produto), 'R' (região), 'RS' (região+seção), 'RD' (região+departamento).
- **TIPOVENDEDOR** (VARCHAR2, 1, obrigatório): 'I' (interno), 'E' (externo), 'R' (representante), 'P' (profissional).

---

### 7.23 ComissoesUsuarios — MXSCOMISSAOUSUR

**Descrição**: Comissões progressivas por produto e vendedor.

**Campos principais**:
- **CODFAIXA** (VARCHAR2, 50, obrigatório, PK): Código da faixa.
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor.
- **PERCDESCINI** (NUMBER, 18,6, obrigatório): Percentual de desconto inicial.
- **PERCDESCFIM** (NUMBER, 18,6, obrigatório): Percentual de desconto final.
- **PERCOM** (NUMBER, 8,4, obrigatório): % comissão.
- **CODPROD** (VARCHAR2, 50): Código do produto.
- **CODEPTO** (VARCHAR2, 50): Código do departamento.
- **CODSEC** (VARCHAR2, 50): Código da seção.
- **DTINICIO** (DATE, obrigatório): Data inicial.
- **DTFIM** (DATE, obrigatório): Data final.
- **TIPOCOMISSAO** (VARCHAR2, 2, obrigatório): 'P' (produto), 'D' (departamento), 'S' (seção).
- **TIPO** (VARCHAR2, 2, obrigatório): Fixar 'RP'.

---

### 7.24 Concorrentes — MXSCONCOR

**Descrição**: Cadastro de concorrentes.

**Campos principais**:
- **CODCONC** (VARCHAR2, 10, obrigatório, PK): Código do concorrente.
- **CONCORRENTE** (VARCHAR2, 40, obrigatório): Nome do concorrente.
- **ATIVO** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **TELEFONE** (VARCHAR2, 13): Telefone.

---

### 7.25 Cotacoes — MXSCOTACAO

**Descrição**: Cabeçalho da cotação.

**Campos principais**:
- **NUMCOTACAO** (VARCHAR2, 50, obrigatório, PK): Código da cotação.
- **NUMPED** (VARCHAR2, 50): Número do pedido vinculado.
- **DATA** (DATE, obrigatório): Data da cotação.
- **STATUS** (VARCHAR2, 1): 'A' – Aberta, 'F' – Finalizada.
- **CODFILIAL** (VARCHAR2, 50): Código da filial.
- **CODCLI** (VARCHAR2, 50): Código do cliente.

---

### 7.26 CotacoesItens — MXSCOTACAOITENS

**Descrição**: Itens da cotação.

**Campos principais**:
- **NUMCOTACAO** (VARCHAR2, 50, obrigatório, PK): Código da cotação.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **SEQUENCIA** (NUMBER, 10, obrigatório, PK): Sequência de inclusão.
- **CODCONC** (VARCHAR2, 50): Código do concorrente.
- **PRECO** (NUMBER, 18,6): Preço cotado.
- **PRECOUNITARIO** (NUMBER, 18,6): Preço unitário da embalagem.
- **PRECOTABELA** (NUMBER, 18,6): Preço de tabela.

---

### 7.27 Contatos — MXSCONTATO

**Descrição**: Contatos relacionados ao cadastro do cliente (vários por cliente).

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CODCONTATO** (VARCHAR2, 22, obrigatório, PK): Código do contato.
- **NOMECONTATO** (VARCHAR2, 40, obrigatório): Nome do contato.
- **CARGO** (VARCHAR2, 30): Cargo.
- **TELEFONE** (VARCHAR2, 18, obrigatório): Telefone.
- **CELULAR** (VARCHAR2, 18): Celular.
- **EMAIL** (VARCHAR2, 50): E-mail.
- **DTNASCIMENTO** (DATE): Data de nascimento.
- **TIPOCONTATO** (VARCHAR2, 1, obrigatório): 'I' (interno) ou 'E' (externo).

**Relacionamentos**:
- FK para `MXSCLIENT` via `CODCLI`.

---

### 7.28 ConfiguracoesErp — MXSCONFIGERP

**Descrição**: Parâmetros gerais do ERP que influenciam o comportamento do maxPedido. Muitos campos; listamos os principais.

**Campos principais** (seleção):
- **ACEITAVENDASEMEST** (VARCHAR2, 1): 'S' ou 'N' – aceitar venda sem estoque.
- **BLOQPRAZOMDVENDA** (VARCHAR2, 1): Bloquear prazo médio de venda.
- **CALCSTFONTEPF** (VARCHAR2, 1): Calcular ST para cliente fonte.
- **CALCSTPF** (VARCHAR2, 1): Calcular ST para pessoa física.
- **NUMCASASDECESTOQUE** (NUMBER, 2): Nº de casas decimais para estoque.
- **NUMCASASDECVENDA** (NUMBER, 2): Nº de casas decimais para preço de venda.
- **PERMAXDESCVENDA** (NUMBER, 5,2): % máximo de desconto médio.
- **PRAZOVALIDADEORCAMENTO** (NUMBER, 4): Prazo de validade do orçamento em dias.
- **TIPOCALCIPI** (VARCHAR2, 2): 'PV' (conf. casas decimais de venda) ou 'A2' (arredondar 2 casas).
- **TIPOCALCST** (VARCHAR2, 2): 'PV' ou 'A2'.
- **TIPOMOVCCRCA** (VARCHAR2, 2): 'FF' (débito/crédito no faturamento), 'VA' (débito na venda, crédito no acerto), 'VF' (débito na venda, crédito no faturamento), 'VV' (débito/crédito na venda).
- **USACREDRCA** (VARCHAR2, 1): Utiliza conta corrente de RCA.
- **USATRIBUTACAOPORUF** (VARCHAR2, 1): Usar tributação por UF.
- **UTILIZAVENDAPOREMBALAGEM** (VARCHAR2, 1): Usar venda por embalagem.
- **VLMAXVENDAPF** (NUMBER, 16,3): Valor máximo para pessoa física (/mês).

---

### 7.29 Departamentos — MXSDEPTO

**Descrição**: Departamentos relacionados ao cadastro de produto (grupo de produtos).

**Campos principais**:
- **CODEPTO** (VARCHAR2, 50, obrigatório, PK): Código do departamento.
- **DESCRICAO** (VARCHAR2, 50, obrigatório): Descrição.

**Relacionamentos**:
- FK em `MXSPRODUT` via `CODEPTO`.

---

### 7.30 Descontos — MXSDESCONTO

**Descrição**: Descontos extra flexível da tabela de preço, campanhas de desconto, desconto por quantidade ou faixa de valor.

**Campos principais** (seleção):
- **CODDESCONTO** (VARCHAR2, 50, obrigatório, PK): Código do desconto.
- **CODCLI** (VARCHAR2, 50): Cliente (se específico).
- **CODPROD** (VARCHAR2, 50): Produto.
- **CODUSUR** (VARCHAR2, 50): Vendedor.
- **DTINICIO** (DATE, obrigatório): Data de início.
- **DTFIM** (DATE, obrigatório): Data de fim.
- **PERCDESC** (NUMBER, 10,4, obrigatório): % de desconto comercial.
- **PERCDESCFIN** (NUMBER, 10,4): % de desconto financeiro.
- **QTINI** (NUMBER, 10,4): Quantidade inicial.
- **QTFIM** (NUMBER, 10,4): Quantidade final.
- **VLRMINIMO** (NUMBER, 18,6): Valor mínimo.
- **VLRMAXIMO** (NUMBER, 18,6): Valor máximo.
- **TIPO** (VARCHAR2, 1, obrigatório): 'C' (comercial), 'F' (financeiro).
- **PRIORITARIA** (VARCHAR2, 1): Forçar aplicação prioritária.

---

### 7.31 DescontosCapas — MXSDESCONTOC

**Descrição**: Cabeçalho de combos de desconto (campanhas de combo).

**Campos principais**:
- **CODIGO** (VARCHAR2, 50, obrigatório, PK): Código de identificação do combo.
- **DESCRICAO** (VARCHAR2, 100, obrigatório): Nome da campanha/combo.
- **DTINICIO** (DATE, obrigatório): Data início.
- **DTFIM** (DATE, obrigatório): Data fim.
- **TIPOCAMPANHA** (VARCHAR2, 3): 'MQT' (mix quantidade mínima), 'MIQ' (mix intervalo quantidade), 'SQP' (subcategoria, quantidade pedido), 'FPU' (faixas pedido unificada).
- **TIPODESCONTO** (VARCHAR2, 1): 'P' (percentual) ou 'F' (flexível) ou 'A' (automático) para FPU.
- **TIPOVALIDACAO** (VARCHAR2, 1): 'P' (peso), 'D' (dosagem), 'V' (valor).
- **PROPORCIONAL** (VARCHAR2, 1): 'S' ou 'N' – proporcionalidade.
- **QTDECOMBOCLIENTE** (NUMBER, 10): Limite por cliente.
- **QTDECOMBOUSUR** (NUMBER, 10): Limite por vendedor.

---

### 7.32 DescontosItens — MXSDESCONTOI

**Descrição**: Itens que compõem o combo de desconto.

**Campos principais**:
- **CODIGO** (NUMBER, 10, obrigatório, PK): Código do combo (relaciona com `MXSDESCONTOC`).
- **SEQUENCIA** (NUMBER, 10, obrigatório, PK): Sequência de exibição.
- **CODPROD** (VARCHAR2, 50, obrigatório): Código do produto.
- **QTMINIMA** (NUMBER, 12,6, obrigatório): Quantidade mínima no combo.
- **PERCDESC** (NUMBER, 12,6, obrigatório): Percentual de desconto.
- **QTMXIMA** (NUMBER, 12,6): Quantidade máxima.
- **TIPODESCONTO** (NUMBER, 2, obrigatório): 'A' (automático) ou 'F' (flexível).
- **CODAUXILIAR** (VARCHAR2, 50): Código de barras (obrigatório para venda por embalagem).

---

### 7.33 DescontoCategoria (Campanha SQP) — MXSDESCONTOCATEGORIA

**Descrição**: Categorias do tipo de campanha SQP.

**Campos principais**:
- **CODIGO** (NUMBER, 10, obrigatório, PK): Código do combo.
- **TIPO** (VARCHAR2, 100, obrigatório, PK): Tipo de filtro: 'F' (fornecedor), 'S' (seção), 'D' (departamento), 'C' (categoria), 'SC' (subcategoria), 'P' (produto).
- **TIPOVALOR** (VARCHAR2, 50, obrigatório): Código alfanumérico do tipo do filtro.
- **PERCDESC** (NUMBER, 12,6, obrigatório): Percentual de desconto.
- **INICIOINTERVALO** (NUMBER, 12,6, obrigatório): Intervalo inicial.
- **FIMINTERVALO** (NUMBER, 12,6, obrigatório): Intervalo final.
- **SEQ** (NUMBER, 10, obrigatório, PK): Sequencial.

---

### 7.34 DescontosCapasProdRelac — MXSDESCONTOCPRODRELAC

**Descrição**: Itens relacionados à campanha que podem ter desconto após a venda do combo inicial.

**Campos principais**:
- **CODIGOCAMPANHA** (NUMBER, 10, obrigatório, PK): Código do combo.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **PERCDESC** (NUMBER, 12,6, obrigatório): Percentual de desconto.
- **CODIGOGRUPOCOMBO** (NUMBER, 10): Código do grupo (agrupador) das campanhas.

---

### 7.35 DescontosRestricoes — MXSDESCONTORESTRICOES

**Descrição**: Restrições da campanha.

**Campos principais**:
- **CODIGO** (NUMBER, 10, obrigatório, PK): Código do combo.
- **TIPO** (NUMBER, 2, obrigatório, PK): Tipo de restrição: 1 (filial), 2 (região), 3 (ramo atividade), 4 (supervisor), 5 (vendedor), 6 (cliente), 7 (distribuição), 8 (plano de pagamento).
- **CODIGOA** (VARCHAR2, 4, obrigatório, PK): Código alfanumérico.
- **CODIGON** (NUMBER, 10, obrigatório, PK): Código numérico.

---

### 7.36 DiasUteis — MXSDIAUTIL

**Descrição**: Dias úteis considerados pelo sistema.

**Campos principais**:
- **DATA** (DATE, obrigatório, PK): Dia.
- **DIAUTIL** (VARCHAR2, 1, obrigatório): 'S' (útil) ou 'N'.

---

### 7.37 Estado — ERP_MXSESTADO

**Descrição**: Unidades da federação (UF). Obrigatório para maxGestão.

**Campos principais**:
- **UF** (VARCHAR2, 2, obrigatório, PK): Sigla da UF.
- **ESTADO** (VARCHAR2, 30, obrigatório): Nome do estado.

---

### 7.38 Embalagens — MXSEMBALAGEM

**Descrição**: Embalagens vinculadas ao produto (para venda por embalagem).

**Campos principais**:
- **CODAUXILIAR** (VARCHAR2, 50, obrigatório, PK): Código auxiliar da embalagem (código de barras).
- **CODPROD** (VARCHAR2, 50, obrigatório): Código do produto.
- **CODFILIAL** (VARCHAR2, 20, obrigatório, PK): Código da filial.
- **EMBALAGEM** (VARCHAR2, 12, obrigatório): Descrição da embalagem (ex.: CX, UN).
- **QTUNIT** (NUMBER, 18,6, obrigatório): Fator de conversão (quantidade de unidades na embalagem).
- **FATORPRECO** (NUMBER, 20,8): Fator de acréscimo ao preço de tabela.
- **UNIDADE** (VARCHAR2, 12): Unidade (ex.: CX, UN, LT).

---

### 7.39 Emprs — MXSEMPR

**Descrição**: Informações dos funcionários (incluindo motoristas).

**Campos principais**:
- **CODSETOR** (VARCHAR2, 22, obrigatório): Código do setor.
- **NOME** (VARCHAR2, 40, obrigatório): Nome.
- **MATRICULA** (NUMBER, 22, obrigatório, PK): Matrícula.
- **EMAIL** (VARCHAR2, 50): E-mail.
- **ENVIAFV** (VARCHAR2, 1): Envia para força de vendas? (S/N).
- **NOME_GUERRA** (VARCHAR2, 15): Apelido.
- **FONE** (VARCHAR2, 13): Telefone fixo.
- **CELULAR** (VARCHAR2, 13): Celular.
- **CODFILIAL** (VARCHAR2, 20, obrigatório): Código da filial.
- **TIPO** (VARCHAR2, 1, obrigatório): 'F' (funcionário) ou 'M' (motorista).
- **DATA_VALIDADE_CNH** (DATE): Data de validade da CNH.
- **DT_EXCLUSAO** (DATE): Data de exclusão lógica.
- **CPF** (VARCHAR2, 20): CPF.
- **SITUACAO** (VARCHAR2, 1, obrigatório): 'A' (ativo) por padrão.
- **CODEVICULO** (VARCHAR2, 50): Código do veículo relacionado (para motoristas).

---

### 7.40 Estoques — MXSET

**Descrição**: Informações de estoque por filial. Obrigatório.

**Campos principais**:
- **CODFILIAL** (VARCHAR2, 20, obrigatório, PK): Código da filial.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **QTESTGER** (NUMBER, 22,8, obrigatório): Quantidade de estoque gerencial.
- **QTRESERV** (NUMBER, 22,8, obrigatório): Quantidade reservada.
- **QTBLOQUEADA** (NUMBER, 20,6, obrigatório): Quantidade bloqueada.
- **QTPENDENTE** (NUMBER, 16,3, obrigatório): Quantidade pendente.
- **CUSTOREP** (NUMBER, 18,6, obrigatório): Custo de reposição.
- **CUSTOREAL** (NUMBER, 18,6, obrigatório): Custo real.
- **CUSTOFIN** (NUMBER, 18,6, obrigatório): Custo financeiro.
- **DTULTENT** (DATE): Data da última entrada.
- **VLULTENT** (NUMBER, 18,6): Valor da última entrada.
- **QTGIRODIA** (NUMBER, 16,3): Giro por dia.
- **ALIQICMS1ULTENT** (NUMBER, 12,4): Alíquota ICMS1 da última entrada.
- **IVAULTENT** (NUMBER, 22): IVA última entrada.

**Observação**: Estoque disponível = QTESTGER - QTRESERV - QTBLOQUEADA - QTPENDENTE (parâmetro pode incluir pendente). Todos os produtos devem ser enviados, mesmo com estoque zero.

---

### 7.41 FaixaComissaoVendedor — MXSFAIXACOMISSAOUSUR

**Descrição**: Faixas de comissão variáveis por vendedor.

**Campos principais**:
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **DTINICIO** (DATE, obrigatório): Data inicial.
- **DTFIM** (DATE, obrigatório): Data final.
- **NUMREGIAO** (VARCHAR2, 50, obrigatório, PK): Código da região (tabela de preço).
- **FAIXA_INI_COMISSAO** (NUMBER, 18,2, obrigatório): Faixa inicial.
- **FAIXA_FIM_COMISSAO** (NUMBER, 18,2, obrigatório): Faixa final.
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor (ou 0 para todos).
- **COMISSAO_PADRAO** (NUMBER, 18,2, obrigatório): Comissão padrão.

---

### 7.42 FeriasVendedor — ControleMXSUSUARIOS

**Descrição**: Controle de férias do vendedor.

**Campos principais**:
- **CODIGOVENDEDORERP** (NUMBER, 10, obrigatório, PK): Código do vendedor no ERP.
- **DATAINICIOFERIAS** (DATE, obrigatório): Data início das férias.
- **DATAFIMFERIAS** (DATE, obrigatório): Data fim das férias.

---

### 7.43 Filiais — MXSFILIAL

**Descrição**: Informações da filial/empresa.

**Campos principais**:
- **CODIGO** (VARCHAR2, 50, obrigatório, PK): Código da filial.
- **RAZAOSOCIAL** (VARCHAR2, 40, obrigatório): Razão social.
- **FANTASIA** (VARCHAR2, 25): Nome fantasia.
- **CGC** (VARCHAR2, 14, obrigatório): CNPJ.
- **IE** (VARCHAR2, 20): Inscrição estadual.
- **ENDERECO** (VARCHAR2, 40): Endereço.
- **BAIRRO** (VARCHAR2, 20): Bairro.
- **CIDADE** (VARCHAR2, 30): Cidade.
- **UF** (VARCHAR2, 2, obrigatório): UF.
- **CEP** (VARCHAR2, 11): CEP.
- **TELEFONE** (VARCHAR2, 18): Telefone.
- **FAX** (VARCHAR2, 18): Fax.
- **ACEITAVENDASEMEST** (VARCHAR2, 1): 'S' ou 'N'.
- **CALCULARIPIVENDA** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **TIPOAVALIACAOCOMISSAO** (NUMBER, 2): 2 (por sobreposição) etc.
- **USAWMS** (VARCHAR2, 1): 'S' ou 'N'.
- **UTILIZANFE** (VARCHAR2, 1): Utiliza NF-e.
- **BROKER** (VARCHAR2, 1): 'S' se filial pode realizar venda Broker.
- **UTILIZAVENDAPOREMBALAGEM** (VARCHAR2, 1): 'S' ou 'N'.

---

### 7.44 FilialRegiao — MXSFILIALREGIAO

**Descrição**: Relacionamento entre filiais e regiões/tabelas de preço.

**Campos principais**:
- **CODFILIAL** (VARCHAR2, 50, obrigatório, PK): Código da filial.
- **NUMREGIAO** (VARCHAR2, 50, obrigatório, PK): Número da região/tabela de preço.
- **PRIORITARIA** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.

**Relacionamentos**:
- FK para `MXSFILIAL` via `CODFILIAL`.
- FK para `MXSREGIAO` via `NUMREGIAO`.

---

### 7.45 FiltrarRegiaoRCA — MXSFILTROREGIAORCA

**Descrição**: Filtro de região por vendedor (RCA).

**Campos principais**:
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor.
- **NUMREGIAO** (VARCHAR2, 20, obrigatório, PK): Código da região.

---

### 7.46 FiliaisRetira — MXSFILIALRETIRA

**Descrição**: Relação das filiais de retirada de estoque com a filial de venda.

**Campos principais**:
- **CODFILIALRETIRA** (VARCHAR2, 20, obrigatório, PK): Filial que cede estoque.
- **CODFILIALVENDA** (VARCHAR2, 20, obrigatório, PK): Filial que vende.

---

### 7.47 Fornecedores — MXSFORNEC

**Descrição**: Cadastro de fornecedores.

**Campos principais**:
- **CODFORNEC** (VARCHAR2, 50, obrigatório, PK): Código.
- **FORNECEDOR** (VARCHAR2, 60, obrigatório): Razão social.
- **FANTASIA** (VARCHAR2, 60): Nome fantasia.
- **CGC** (VARCHAR2, 18, obrigatório): CNPJ/CPF.
- **ENDERECO** (VARCHAR2, 40, obrigatório): Endereço.
- **BAIRRO** (VARCHAR2, 20, obrigatório): Bairro.
- **CIDADE** (VARCHAR2, 15, obrigatório): Cidade.
- **ESTADO** (VARCHAR2, 2, obrigatório): UF.
- **BLOQUEIO** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **TELFAB** (VARCHAR2, 20, obrigatório): Telefone.
- **REVENDA** (VARCHAR2, 1, obrigatório): 'S' (permite vender), 'N' (não permite), 'T' (transportadora).
- **EREDESPACHO** (VARCHAR2, 1): 'S' se transportadora com redespacho.
- **EXIGEREDESPACHO** (VARCHAR2, 1): 'S' ou 'N'.
- **PERGRIS** (NUMBER, 22): % GRIS.
- **VLPEDAGIO** (NUMBER, 22): Valor do pedágio.

**Relacionamentos**:
- FK em `MXSPRODUT` via `CODFORNEC`.

---

### 7.48 Gerentes — ERP_MXSGERENTE

**Descrição**: Informações de gerentes. Obrigatório para maxGestão.

**Campos principais**:
- **CODGERENTE** (VARCHAR2, 50, obrigatório, PK): Código do gerente.
- **NOMEGERENTE** (VARCHAR2, 40, obrigatório): Nome.
- **COD_CADRCA** (VARCHAR2, 50, obrigatório): Código do vendedor padrão (relaciona com `MXSUSUARI`).

**Relacionamentos**:
- FK em `MXSSUPERV` via `CODGERENTE`.

---

### 7.49 GruposCampanhas — MXSGRUPOSCAMPANHAC

**Descrição**: Cabeçalho dos grupos no sistema (para campanhas).

**Campos principais**:
- **CODGRUPO** (VARCHAR2, 50, obrigatório, PK): Código do grupo.
- **TIPO** (VARCHAR2, 4, obrigatório): 'GP' (grupo de produtos) ou 'CL' (grupos de clientes).
- **CODFILIAL** (VARCHAR2, 20, obrigatório): Código da filial.
- **DESCRICAO** (VARCHAR2, 4000): Descrição do grupo.

---

### 7.50 GruposCampanhasItens — MXSGRUPOSCAMPANHAI

**Descrição**: Itens dos grupos de campanha.

**Campos principais**:
- **CODGRUPO** (VARCHAR2, 50, obrigatório, PK): Código do grupo (FK para `MXSGRUPOSCAMPANHAC`).
- **CODITEM** (VARCHAR2, 50, obrigatório, PK): Código do item (produto ou cliente, conforme tipo do grupo).

---

### 7.51 HistoricosPedidosCapas — MXSHISTORICOPEDC

**Descrição**: Histórico de pedidos (cabeçalho). Obrigatório para várias funcionalidades.

**Campos principais** (seleção):
- **NUMPED** (NUMBER, 10, obrigatório, PK): Número do pedido.
- **CODCLI** (VARCHAR2, 50, obrigatório): Código do cliente.
- **DATA** (DATE, obrigatório): Data do pedido.
- **CODUSUR** (VARCHAR2, 50, obrigatório): Código do vendedor.
- **CODFILIAL** (VARCHAR2, 50, obrigatório): Código da filial.
- **CONDVENDA** (NUMBER, 2, obrigatório): Tipo de venda: 1 (normal), 5 (bonificação), 7 (venda futura), 11 (troca), 13 (manifesto), 14 (pronta-entrega), 24 (bonificação pronta-entrega).
- **POSICAO** (VARCHAR2, 2, obrigatório): L (liberado), B (bloqueado), F (faturado), M (montado), P (pendente), C (cancelado).
- **VLTOTAL** (NUMBER, 22, obrigatório): Valor total.
- **VLATEND** (NUMBER, 22): Valor atendido.
- **TOTPESO** (NUMBER, 22): Total peso.
- **TOTVOLUME** (NUMBER, 18,6): Volume total.
- **NUMNOTA** (NUMBER, 22): Número da nota fiscal (quando faturado).
- **DTFAT** (DATE): Data de faturamento.
- **NUMCAR** (VARCHAR2, 50): Número do carregamento.
- **NUMPEDRCA** (NUMBER, 10): Número do pedido no dispositivo (Máxima).
- **CODCOB** (VARCHAR2, 50): Código da cobrança.
- **CODPLPAG** (VARCHAR2, 50): Código do plano de pagamento.
- **CODSUPERVISOR** (VARCHAR2, 50): Código do supervisor.
- **NUMTRANSVENDA** (NUMBER, 10): Identificador único no ERP.
- **OBS** (VARCHAR2, 600): Observações.
- **DTENTREGA** (DATE): Data de entrega.
- **DTAGENDAENTREGA** (DATE): Data de agendamento.

**Relacionamentos**:
- FK para `MXSCLIENT` via `CODCLI`.
- FK para `MXSUSUARI` via `CODUSUR`.
- FK para `MXSFILIAL` via `CODFILIAL`.
- FK para `MXSCOB` via `CODCOB`.
- FK para `MXSPLPAG` via `CODPLPAG`.
- FK para `MXSSUPERV` via `CODSUPERVISOR`.
- Um pedido pode ter vários itens em `MXSHISTORICOPEDI`.

---

### 7.52 HistoricosPedidosItens — MXSHISTORICOPEDI

**Descrição**: Itens do histórico de pedidos.

**Campos principais**:
- **NUMPED** (NUMBER, 10, obrigatório, PK): Número do pedido (FK `MXSHISTORICOPEDC`).
- **NUMSEQ** (NUMBER, 20, obrigatório, PK): Sequência do item.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **QT** (NUMBER, 20, obrigatório): Quantidade.
- **PVENDA** (NUMBER, 18,6, obrigatório): Preço de venda.
- **PTABELA** (NUMBER, 18,6, obrigatório): Preço de tabela.
- **PERCOM** (NUMBER, 8,4): % comissão (obrigatório se usar comissão).
- **DATA** (DATE): Obrigatório para maxGestão.
- **POSICAO** (VARCHAR2, 2): F (faturado), M (montado), P (pendente), C (cancelado).
- **NUMCAR** (VARCHAR2, 8): Número do carregamento.
- **CODAUXILIAR** (VARCHAR2, 50): Código de barras (obrigatório para venda por embalagem).

---

### 7.53 HistoricosPedidosCortes — MXSHISTORICOPEDCORTE

**Descrição**: Itens cortados por pedido.

**Campos principais**:
- **NUMPED** (NUMBER, 10, obrigatório, PK): Número do pedido.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **QTCORTADA** (NUMBER, 22, obrigatório): Quantidade cortada.

---

### 7.54 HistoricosPedidosFaltas — MXSHISTORICOPEDFALTA

**Descrição**: Itens com falta por pedido.

**Campos principais**:
- **NUMPED** (NUMBER, 10, obrigatório, PK): Número do pedido.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **QTFALTA** (NUMBER, 22, obrigatório): Quantidade em falta.
- **QTPEDIDA** (NUMBER, 22, obrigatório): Quantidade pedida.

---

### 7.55 LimiteCombos — MXSLIMITECOMBOS

**Descrição**: Controle de uso de combos por pedido.

**Campos principais**:
- **NUMPED** (NUMBER, 10, obrigatório, PK): Número do pedido.
- **CODCOMBO** (VARCHAR2, 50, obrigatório, PK): Código do combo de desconto.

---

### 7.56 Lotes — MXSLOTE

**Descrição**: Lotes e validades de produtos.

**Campos principais**:
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **NUMLOTE** (VARCHAR2, 50, obrigatório, PK): Número do lote.
- **CODFILIAL** (VARCHAR2, 50, obrigatório, PK): Código da filial.
- **DATAFABRICACAO** (DATE, obrigatório): Data de fabricação.
- **DTVALIDADE** (DATE, obrigatório): Data de validade.
- **QT** (NUMBER, 22,8, obrigatório): Quantidade.

---

### 7.57 MarcacoesPonto — MXSMARCACOESPONTO

**Descrição**: Marcações de registro de jornada.

**Campos principais**:
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do usuário.
- **DATAMARCACAO** (DATE, obrigatório, PK): Data da marcação.
- **HORARIO** (VARCHAR2, 20, obrigatório, PK): Horário (entrada/saída turno).
- **LONGITUDE** (VARCHAR2, 50): Longitude da marcação.
- **LATITUDE** (VARCHAR2, 50): Latitude da marcação.

---

### 7.58 Marcas — MXSMARCA

**Descrição**: Marcas de produtos.

**Campos principais**:
- **CODMARCA** (VARCHAR2, 50, obrigatório, PK): Código da marca.
- **MARCA** (VARCHAR2, 50, obrigatório): Descrição da marca.

**Relacionamentos**:
- FK em `MXSPRODUT` via `CODMARCA`.

---

### 7.59 Mensagens — PCMXSMENSAGENS

**Descrição**: Troca de mensagens entre vendedores e equipe interna.

**Campos principais**:
- **CODMENSAGEM** (VARCHAR2, 50, obrigatório, PK): Código da mensagem.
- **MENSAGEM** (VARCHAR2, 4000, obrigatório): Conteúdo.
- **STATUS** (VARCHAR2, 1, obrigatório): 0 (enviado) ou 1 (lido).
- **CODREMETENTE** (VARCHAR2, 50, obrigatório): Código do usuário remetente.
- **CODUSUR** (VARCHAR2, 50, obrigatório): Código do vendedor destinatário.
- **DATA** (DATE, obrigatório): Data de envio.

---

### 7.60 Metas — ERP_MXSMETA

**Descrição**: Metas mensais por vendedor, produto, etc.

**Campos principais**:
- **CODMETA** (NUMBER, 20, obrigatório, PK): Identificador da meta.
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor.
- **TIPOMETA** (VARCHAR2, 50, obrigatório, PK): C – Cliente; D – Departamento; S – Seção; P – Produto; F – Fornecedor; A – Categoria; FP – Fornecedor Principal; M – Mensal Geral.
- **CODFILIAL** (VARCHAR2, 50, obrigatório, PK): Código da filial.
- **DATAINICIAL** (DATE, obrigatório): Data inicial.
- **DATAFINAL** (DATE, obrigatório): Data final.
- **CODIGO** (VARCHAR2, 50, obrigatório, PK): Identificador do registro vinculado ao tipo de meta.
- **VLVENDAPREV** (NUMBER, 22,8): Valor previsto de venda.
- **QTVENDAPREV** (NUMBER, 22,8): Quantidade prevista.
- **QTCAIXAPREV** (NUMBER, 14,2): Quantidade prevista por caixa.
- **MIXPREV** (NUMBER, 20): Mix previsto.
- **CLIPOSPREV** (NUMBER, 20): Clientes positivados previstos.
- **QTPESOPREV** (NUMBER, 20): Peso previsto.
- **QTDEPEDIDOSPREV** (NUMBER, 20): Quantidade de pedidos prevista.
- **VOLUMEPREV** (NUMBER): Volume previsto.

---

### 7.61 MixClientes — MXSMIXCLIENTES

**Descrição**: Mix vendido pelo vendedor a determinado cliente (visualizado no maxPedido).

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CODFILIAL** (VARCHAR2, 20, obrigatório, PK): Código da filial.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **CODPLPAG** (VARCHAR2, 50, obrigatório): Código do plano de pagamento.
- **QT** (NUMBER, 20, obrigatório): Quantidade.
- **PTABELA** (NUMBER, 22, obrigatório): Preço de tabela.
- **CODAUXILIAR** (VARCHAR2, 50, obrigatório, PK): Código de barras da embalagem (obrigatório para venda por embalagem).

---

### 7.62 MotivosNaoCompra — MXSMOTNAOCOMPRA

**Descrição**: Motivos de não compra (usado em justificativas de visita).

**Campos principais**:
- **CODMOTIVO** (NUMBER, 22, obrigatório, PK): Código.
- **DESCRICAO** (VARCHAR2, 40, obrigatório): Descrição.

---

### 7.63 MotivosVisitas — MXSMOTVISITA

**Descrição**: Motivos da visita do vendedor ao cliente.

**Campos principais**:
- **CODMOTIVO** (NUMBER, 22, obrigatório, PK): Código.
- **DESCRICAO** (VARCHAR2, 40, obrigatório): Descrição.

---

### 7.64 Mxsfiltroregiaorca — MXSFILTROREGIAORCA

**Descrição**: Usuários e suas regiões (filtro).

**Campos principais**:
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor.
- **NUMREGIAO** (VARCHAR2, 20, obrigatório, PK): Código da região.

---

### 7.65 Mxsintegracaoindenizacao — MXSINTEGRACAOINDENIZACAO

**Descrição**: Integração de indenizações geradas por pedidos.

**Campos principais**:
- **ID_INDENIZACAO** (NUMBER, 20, obrigatório, PK): Identificador da indenização.
- **ID_PEDIDO** (NUMBER, 20): Identificador do pedido.
- **INDENIZACAO** (CLOB): Campo para preenchimento da indenização.
- **DATA** (DATE): Data.
- **STATUS** (NUMBER, 4): Status.
- **CRITICA** (CLOB): Crítica.
- **CODCLI** (VARCHAR2, 50): Código do cliente.
- **CODUSUR** (NUMBER, 10): Código do vendedor ERP.
- **NUMPEDER** (NUMBER, 15): Número do pedido ERP.
- **NUMCRITICA** (NUMBER, 20): Número da crítica.
- **CODIGOPAIPEDIDOCOMPLEMENTAR** (NUMBER, 15): Código do pedido complementar pai.

---

### 7.66 NomesProfissionais — MXSNOMEPROFISSIONAL

**Descrição**: Profissionais e suas comissões.

**Campos principais**:
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do usuário no ERP.
- **NOME** (VARCHAR2, 4000, obrigatório): Nome do profissional.
- **PERCENT** (NUMBER, 22): Percentual de comissão.
- **PERCENT2** (NUMBER, 22): Percentual de comissão 2.
- **TIPOVEND** (VARCHAR2, 40): Tipo do vendedor (vindo do cadastro do usuário).
- **TERMINO** (DATE): Data de término da validação da comissão.

---

### 7.67 Notas Fiscais Devolvidas — (subseções)

#### 7.67.1 Devolucoes (Motivos de Devoluções) — ERP_MXSTABDEV

**Descrição**: Motivos de devoluções de NF. Obrigatório para maxGestão.

**Campos principais**:
- **CODDEVOL** (VARCHAR2, 50, obrigatório, PK): Código.
- **TIPO** (VARCHAR2, 2, obrigatório): Fixar "ED" (Entrada de Devolução de Cliente).
- **MOTIVO** (VARCHAR2, 100, obrigatório): Descrição.

#### 7.67.2 Nfent (NF Entrada/Devolução - Cabeçalho) — ERP_MXSNFENT

**Descrição**: Cabeçalho da nota de entrada/devolução. Obrigatório para maxGestão.

**Campos principais**:
- **NUMTRANSENT** (VARCHAR2, 50, obrigatório, PK): Sequencial único identificador da nota de devolução.
- **CODCONT** (VARCHAR2, 50, obrigatório): Código da conta contábil.
- **CODDEVOL** (VARCHAR2, 50, obrigatório): Código do motivo da devolução (se não existir, enviar 1).
- **CODFILIAL** (VARCHAR2, 50, obrigatório): Código da filial.
- **CODFISCAL** (NUMBER, 8, obrigatório): Código fiscal.
- **DTENT** (DATE, obrigatório): Data da entrada.
- **ESPECIE** (VARCHAR2, 2, obrigatório): Espécie da NF (ex.: NF).
- **SERIE** (VARCHAR2, 3, obrigatório): Série da NF de saída.
- **NUMNOTA** (NUMBER, 10, obrigatório): Número da NF de saída.
- **OBS** (VARCHAR2, 255): Observações.
- **CODMOTORISTADEVOL** (VARCHAR2, 50): Código do motorista.
- **CODUSURDEVOL** (VARCHAR2, 50): Código do vendedor emissor da NF de saída.
- **SITUACAONFE** (NUMBER, 10): Situação da NFe/Sefaz (0 se não existir).
- **UF** (VARCHAR2, 2): Estado.
- **TOTPESO** (NUMBER, 18,6): Peso (0 se não existir).
- **VLFRETE** (NUMBER, 18,6): Valor do frete (0 se não existir).
- **VLST** (NUMBER, 18,6): Valor do ST (0 se não existir).
- **GERANFDEVCLI** (VARCHAR2, 1): 'S' (gerado pela empresa) ou 'N' (gerado pelo cliente).
- **CODFORNEC** (VARCHAR2, 50): Código do cliente da devolução.
- **TIPODESCARGAVARCHAR2** (VARCHAR2, 1): Tipo da nota: 6 (devolução normal), 7 (dev. simples remessa), 8 (dev. simples fatura), T (dev. troca).

#### 7.67.3 EstornoComissao (Estorno de comissão e vínculo entre NF Devolvida e Saída) — ERP_MXSESTCOM

**Descrição**: Detalhes de estorno de comissão e vínculo entre NF de devolução e saída. Obrigatório para maxGestão.

**Campos principais**:
- **NUMTRANSENT** (VARCHAR2, 50, obrigatório, PK): Identificador da nota de devolução.
- **NUMTRANSVENDA** (NUMBER, 10, obrigatório, PK): Identificador do cabeçalho da nota de saída.
- **DTESTORNO** (DATE, obrigatório): Data do estorno.
- **CODUSUR** (VARCHAR2, 50, obrigatório): Código do vendedor emissor da NF de saída.
- **VLESTORNO** (NUMBER, 18,6): Valor do estorno de comissão (0 se não existir).
- **VLDEVOLUCAO** (NUMBER, 18,6): Valor da devolução.

#### 7.67.4 NotasSaidaItens (Itens de NF Entrada/Devolução) — ERP_MXSMOV

**Descrição**: Itens devolvidos de NF Entrada/Devolução. Obrigatório para maxGestão.

**Campos principais**:
- **NUMTRANSITEM** (NUMBER, 18, obrigatório, PK): Sequencial único dos itens.
- **CODPROD** (VARCHAR2, 50, obrigatório): Código do produto (valida em `MXSPRODUT`).
- **CODUSUR** (VARCHAR2, 50): Código do vendedor.
- **NUMSEQ** (NUMBER, 20, obrigatório): Sequência do item na NF.
- **CODOPER** (VARCHAR2, 2): Fixar "ED" (Entrada/Devolução).
- **QT** (NUMBER, 20,6, obrigatório): Quantidade de produtos.
- **QTCONT** (NUMBER, 20,6, obrigatório): Replicar QT.
- **NUMTRANSVENDA** (NUMBER, 22): Enviar nulo/vazio.
- **CODAUXILIAR** (VARCHAR2, 50): Código de barras (obrigatório para venda por embalagem).
- **NUMCAR** (VARCHAR2, 50, obrigatório): Número do carregamento/ordem de carga da NF de saída.
- **NUMNOTA** (NUMBER, 10, obrigatório): Número da NF de saída.
- **NUMPED** (NUMBER, 10, obrigatório): Número do pedido do ERP.
- **PTABELA** (NUMBER, 18,6, obrigatório): Preço de tabela.
- **PUNITCONT** (NUMBER, 18,6, obrigatório): Preço de venda.
- **PUNIT** (NUMBER, 18,6, obrigatório): Replicar PUNITCONT.
- **CUSTOFIN** (NUMBER, 18,6): Custo financeiro (0 se não existir).
- **VLIPI** (NUMBER, 18,6): Valor IPI (0 se não existir).
- **ST** (NUMBER, 18,6): Valor ST (0 se não existir).
- **CODDEVOL** (VARCHAR2, 50, obrigatório): Código do motivo da devolução (1 se não existir).
- **NUMTRANSENT** (NUMBER, 22, obrigatório): Sequencial da nota de devolução.
- **QTDEVOL** (NUMBER, 18,6): Fixar 0.
- **CODFILIAL** (VARCHAR2, 50, obrigatório): Código da filial.

---

### 7.68 NotasSaidaCapas (Cabeçalho de Nota) — ERP_MXSNFSAID

**Descrição**: Cabeçalhos das NF de saída. Obrigatório para maxGestão.

**Campos principais**:
- **NUMTRANSVENDA** (NUMBER, 10, obrigatório, PK): Sequencial único (cabeçalho da nota).
- **NUMCAR** (VARCHAR2, 50): Número do carregamento.
- **NUMNOTA** (NUMBER, 10, obrigatório): Número da nota fiscal.
- **SERIE** (VARCHAR2, 5, obrigatório): Série.
- **CODUSUR** (VARCHAR2, 50): Código do usuário.
- **CONDVENDA** (NUMBER, 5, obrigatório): Tipo de venda: 1 (normal), 5 (bonificação), 7 (venda futura), 11 (troca), 13 (manifesto), 14 (pronta-entrega), 24 (bonificação pronta-entrega).
- **DTSAIDA** (DATE, obrigatório): Data de saída (obrigatório se NUMCAR preenchido).
- **DTFAT** (DATE, obrigatório): Data de faturamento.
- **DTENTREGA** (DATE, obrigatório se NUMCAR preenchido): Data de entrega.
- **DTCANCEL** (DATE): Data de cancelamento.
- **VLTOTAL** (NUMBER, 12,2, obrigatório): Valor total.
- **ESPECIE** (VARCHAR2, 2, obrigatório): Espécie (ex.: NF).
- **CODCLI** (VARCHAR2, 50, obrigatório): Código do cliente.
- **NUMPED** (NUMBER, 10, obrigatório): Número do pedido.
- **CODCOB** (VARCHAR2, 50, obrigatório): Código da cobrança.
- **CODPLPAG** (VARCHAR2, 50, obrigatório): Código do plano de pagamento.
- **CODFILIAL** (VARCHAR2, 50, obrigatório): Código da filial.
- **NUMSEQ** (NUMBER, 20, obrigatório): Sequência de entrega (obrigatório se NUMCAR preenchido).
- **TOTPESO** (NUMBER, 18,6, obrigatório se maxRoteirizador/maxMotorista): Total peso.
- **COMISSAO** (NUMBER, 12,2): Valor da comissão.
- **TOTVOLUME** (NUMBER, 18,6, obrigatório se maxRoteirizador/maxMotorista): Total volume.
- **CODSUPERVISOR** (VARCHAR2, 50, obrigatório se NUMCAR preenchido): Código do supervisor.

---

### 7.69 NotasSaidaItens (Itens de Nota) — ERP_MXSMOV

**Descrição**: Itens vendidos das NF de saída. Obrigatório para maxGestão.

**Campos principais**:
- **NUMTRANSITEM** (NUMBER, 18, obrigatório, PK): Sequencial único dos itens.
- **CODPROD** (VARCHAR2, 50, obrigatório): Código do produto (valida em `MXSPRODUT`).
- **CODOPER** (VARCHAR2, 2, obrigatório): 'S' (saída).
- **QT** (NUMBER, 20,6, obrigatório): Quantidade.
- **NUMSEQ** (NUMBER, 20, obrigatório): Sequência do item na nota.
- **QTCONT** (NUMBER, 20,6, obrigatório): Replicar QT.
- **NUMTRANSVENDA** (NUMBER, 10, obrigatório): Identificador do cabeçalho (FK `ERP_MXSNFSAID`).
- **CODAUXILIAR** (VARCHAR2, 50): Código de barras (obrigatório para venda por embalagem).
- **NUMCAR** (VARCHAR2, 50, obrigatório): Número do carregamento.
- **NUMNOTA** (NUMBER, 10, obrigatório): Número da nota fiscal.
- **NUMPED** (NUMBER, 10, obrigatório): Número do pedido do ERP.
- **PTABELA** (NUMBER, 18,6, obrigatório): Preço de tabela.
- **PUNITCONT** (NUMBER, 18,6, obrigatório): Preço de venda.
- **PUNIT** (NUMBER, 18,6, obrigatório): Replicar PUNITCONT.
- **CUSTOFIN** (NUMBER, 18,6): Custo financeiro (0 se não existir).
- **VLIPI** (NUMBER, 18,6): Valor IPI (0 se não existir).
- **ST** (NUMBER, 18,6): Valor ST (0 se não existir).

---

### 7.70 ObterDadosLogística — ERP_ENTREGA_Eventos

**Descrição**: Endpoint usado para apresentar dados de entrega dos produtos (maxPedido e Tá em rota). Necessário ter dados populados em `ERP_MXSCARREG` e `MXSEMPR`.

**Campos principais**:
- **ID_ERP** (NUMBER, 18, obrigatório, PK): Número de identificação do registro.
- **TIPO** (VARCHAR2, 100, obrigatório): Tipo de evento:
  - 1: Pedido em trânsito / saiu para entrega
  - 2: Chegou no cliente
  - 6: Início da entrega
  - 7: Pedido entregue
  - 8: Reentrega
  - 9: Devolução total
  - 10: Devolução parcial
- **DATAHORA** (DATE, obrigatório): Data/hora do evento.
- **SEQ_PEDIDO_ERP** (VARCHAR2, 50, obrigatório): Número do pedido no ERP.
- **CARGA_FORMADA_ERP** (VARCHAR2, 50, obrigatório): Número do carregamento.
- **CLIENTE_CODIGO_ERP** (VARCHAR2, 50, obrigatório): Código do cliente.

---

### 7.71 PlanosPagamentos — MXSPLPAG

**Descrição**: Planos de pagamento (condições comerciais).

**Campos principais**:
- **CODPLPAG** (VARCHAR2, 50, obrigatório, PK): Código.
- **DESCRICAO** (VARCHAR2, 40, obrigatório): Descrição.
- **NUMDIAS** (NUMBER, 4, obrigatório): Prazo médio.
- **NUMPR** (NUMBER, 6,2, obrigatório): Número da coluna de preço (default 1).
- **PERTXFIM** (NUMBER, 8,4, obrigatório): Acréscimo para tabela de preço.
- **VENDABK** (VARCHAR2, 1, obrigatório): 'S' ou 'N' – venda com boleto? (Se 'S', deve existir cobrança que aceite boleto.)
- **VLMINPEDIDO** (NUMBER, 12,2, obrigatório): Valor mínimo para condição.
- **PRAZO1** (NUMBER, 4, obrigatório): Prazo para primeira parcela (dias).
- **TIPOPRAZO** (VARCHAR2, 1, obrigatório): 'N' (normal), 'B' (bonificado), 'I' (inativo).
- **TIPOENTRADA** (VARCHAR2, 2): 3 (aceita entrada na condição), 10 (recebimento – pronta entrega).
- **TIPOVENDA** (VARCHAR2, 2, obrigatório): 'VP' (a prazo), 'VV' (à vista).
- **USAMULTIFILIAL** (VARCHAR2, 1): 'S' (verifica permissão em `PlanosPagamentosClientes`), 'N' (considera para todas as filiais).

---

### 7.72 PlanosPagamentosClientes — MXSPLPAGCLI

**Descrição**: Planos de pagamento por cliente (sobrescreve regras gerais).

**Campos principais**:
- **CODPLPAG** (VARCHAR2, 50, obrigatório, PK): Código do plano.
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.

---

### 7.73 PlanosPagamentosFiliais — MXSPLPAGFILIAL

**Descrição**: Planos de pagamento por filial.

**Campos principais**:
- **CODPLPAG** (VARCHAR2, 50, obrigatório, PK): Código do plano.
- **CODFILIAL** (VARCHAR2, 50, obrigatório, PK): Código da filial.

---

### 7.74 PlanosPagamentosProdutos — MXSPLPAGPRODUT

**Descrição**: Relações de plano de pagamento e item (produto).

**Campos principais**:
- **CODFILIAL** (VARCHAR2, 50, obrigatório, PK): Código da filial.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **DTINICIAL** (DATE, obrigatório): Data inicial.
- **DTFINAL** (DATE, obrigatório): Data final.
- **CODPLPAG** (VARCHAR2, 50, obrigatório, PK): Código do plano.

---

### 7.75 PlanosPagamentosRegioes — MXSPLPAGREGIAO

**Descrição**: Relações de regiões, planos de pagamentos e clientes.

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **NUMREGIAO** (VARCHAR2, 20, obrigatório, PK): Número da região/tabela de preço.
- **CODPLPAG** (VARCHAR2, 1, obrigatório, PK): Código do plano (porém tamanho parece pequeno; provavelmente deveria ser VARCHAR2(50) – verificar).

---

### 7.76 Pracas — MXSPRACA

**Descrição**: Praças de atendimento. Vinculado ao cliente e à região/tabela de preço.

**Campos principais**:
- **CODPRACA** (VARCHAR2, 50, obrigatório, PK): Código.
- **NUMREGIAO** (VARCHAR2, 50, obrigatório): Região (relaciona com `MXSREGIAO`).
- **ROTA** (NUMBER, 4): Rota.
- **SITUACAO** (VARCHAR2, 1, obrigatório): 'A' (ativo), 'I' (inativo).
- **PRACA** (VARCHAR2, 50, obrigatório): Nome da praça.

**Relacionamentos**:
- FK para `MXSREGIAO` via `NUMREGIAO`.
- FK em `MXSCLIENT` via `CODPRACA`.

---

### 7.77 PrazosAdicionais — MXSPRAZOADICIONAL

**Descrição**: Prazos adicionais com vigência por cliente e condição de pagamento.

**Campos principais**:
- **CODIGO** (NUMBER, 22, obrigatório, PK): Código.
- **CODATIV** (NUMBER, 22): Código da atividade.
- **CODCLI** (VARCHAR2, 50): Código do cliente.
- **CODFUNCLANC** (NUMBER, 22): Funcionário que cadastrou.
- **CODFUNCULTALTER** (NUMBER, 22): Último alterador.
- **CODPLPAG** (NUMBER, 22, obrigatório, PK): Código do plano de pagamento.
- **CODPRACA** (NUMBER, 22): Código da praça.
- **CODSUPERVISOR** (VARCHAR2, 22): Código do supervisor.
- **CODUSUR** (VARCHAR2, 50): Código do vendedor.
- **DATALANC** (DATE): Data do cadastro.
- **DATAULTALTER** (DATE): Data da última alteração.
- **DTFIM** (DATE, obrigatório): Fim da vigência.
- **DTINICIO** (DATE, obrigatório): Início da vigência.
- **NUMDIAS** (NUMBER, 22, obrigatório): Número de dias adicionais.
- **NUMREGIAO** (NUMBER, 22): Número da região.
- **ORIGEMPED** (VARCHAR2, 1): Origem do pedido (F, R, B).
- **SSNCFV** (VARCHAR2, 1): Enviar para FV?.
- **UTILIZADESCREDE** (VARCHAR2, 1): Utiliza desconto na rede de clientes.
- **VLMINVENDA** (NUMBER, 22): Valor mínimo de venda.

---

### 7.78 PrecosPromocoes — MXSPRECOPROM

**Descrição**: Políticas de preço fixo (promoções).

**Campos principais**:
- **CODPRECOPROM** (VARCHAR2, 50, obrigatório, PK): Código de identificação.
- **ACEITAACRESCIMOPRECOFIXO** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **ACEITADESCPRECOFIXO** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **AGREGARST** (VARCHAR2, 1, obrigatório): Agregar valor de ST?.
- **APENASPLPAGMAX** (VARCHAR2, 1): Aplica apenas no plano especificado.
- **APLICADESCONTOSIMPLES** (VARCHAR2, 1): Aplica desconto simples nacional.
- **CLASSEVENDA** (VARCHAR2, 1): Filtro por classe de venda do cliente.
- **CODATIV** (VARCHAR2, 50): Filtro por ramo de atividade.
- **CODAUXILIAR** (VARCHAR2, 50): Código da embalagem (para restrição por embalagem).
- **CODCLI** (VARCHAR2, 50): Filtro por cliente.
- **CODFILIAL** (VARCHAR2, 50, obrigatório): Filtro por filial.
- **CODPLPAGMAX** (VARCHAR2, 50): Filtro por plano de pagamento.
- **CODPRACA** (VARCHAR2, 50): Filtro por praça.
- **CODPROD** (VARCHAR2, 50, obrigatório): Produto.
- **CODREDE** (VARCHAR2, 50): Filtro por rede de cliente.
- **CODSUPERVISOR** (VARCHAR2, 50): Filtro por supervisor.
- **CODUSUR** (VARCHAR2, 50): Filtro por vendedor.
- **CONSIDERAPRECOSEMIMPOSTO** (VARCHAR2, 1): 'S' – preço sem imposto; calcula impostos depois.
- **DTFIMVIGENCIA** (DATE, obrigatório): Fim da vigência.
- **DTINICIOVIGENCIA** (DATE, obrigatório): Início da vigência.
- **NUMREGIAO** (VARCHAR2, 50, obrigatório): Região/tabela de preço.
- **ORIGEMPED** (VARCHAR2, 1): Origem do pedido.
- **PRECOFIXO** (NUMBER, 18,6, obrigatório): Preço fixo.
- **UTILIZAPRECOFIXOFAMILIA** (VARCHAR2, 1): Se usa família de produtos.
- **UTILIZAPRECOFIXOREDE** (VARCHAR2, 1): Se usa rede de clientes.
- **VLST** (NUMBER, 18,6): Valor de ST (se informado, campos `consideraPrecoSemImposto`='N', `aceitaDescPrecoFixo`='N', `aceitaAcrescimoPrecoFixo`='N', `agregarSt`='S').
- **ENVIAFV** (VARCHAR2, 1, obrigatório): Enviar para força de vendas?.

---

### 7.79 PrestacoesTitulos (Títulos) — ERP_MXSPREST

**Descrição**: Títulos financeiros (abertos ou fechados) dos clientes.

**Campos principais**:
- **NUMTRANSVENDA** (NUMBER, 10, obrigatório, PK): Sequencial do cabeçalho do pedido (origem).
- **PREST** (VARCHAR2, 4, obrigatório, PK): Número da prestação.
- **NUMBANCO** (NUMBER, 10, obrigatório): Código do banco.
- **VALORDESC** (NUMBER, 22): Valor de desconto.
- **VPAGO** (NUMBER, 22): Valor pago.
- **CODCLI** (VARCHAR2, 50, obrigatório): Código do cliente.
- **VALORMULTA** (NUMBER, 22): Valor da multa.
- **CODFILIAL** (VARCHAR2, 20, obrigatório): Código da filial.
- **CARTORIO** (VARCHAR2, 1, obrigatório): 'S' ou 'N' – em cartório.
- **VALOR** (NUMBER, 18,6, obrigatório): Valor do título.
- **DTVENCORIG** (DATE, obrigatório): Data de vencimento original.
- **CODUSUR** (VARCHAR2, 50, obrigatório): Código do vendedor.
- **DTVENC** (DATE, obrigatório): Data de vencimento.
- **DTPAG** (DATE): Data de pagamento.
- **VLTXBOLETO** (NUMBER, 12): Valor taxa de boleto.
- **VALORORIG** (NUMBER, 18,6): Valor original.
- **PROTESTO** (VARCHAR2, 1): 'S' ou 'N' – protestado.
- **DTEMISSAO** (DATE, obrigatório): Data de emissão.
- **CODCOB** (VARCHAR2, 50, obrigatório): Código da cobrança.
- **PERCOM** (NUMBER, 14): Percentual de comissão.
- **DUPLIC** (NUMBER, 10): Número da duplicata.
- **STATUS** (VARCHAR2, 1, obrigatório): 'A' (aberto) ou 'P' (pago).
- **NOSSONUMBCO** (VARCHAR2, 30): Nosso número no banco.
- **BOLETO** (VARCHAR2, 1): Se tem boleto.
- **RECEBIVEL** (VARCHAR2, 1): Se pode ser recebido pelo vendedor (Pronta Entrega).
- **COMISSAO** (NUMBER, 18,6): Valor da comissão.
- **AGENCIA** (VARCHAR2, 50, obrigatório se Pronta Entrega): Agência.
- **CODBARRA** (VARCHAR2, 100, obrigatório se Pronta Entrega): Código de barras do boleto.
- **NUMCARTEIRA** (VARCHAR2, 100, obrigatório se Pronta Entrega): Número da carteira.
- **LINHADIG** (VARCHAR2, 100, obrigatório se Pronta Entrega): Linha digitável.
- **ID_ERP** (VARCHAR2, 50): Identificador único do título no ERP.
- **CODCLIENTENOBANCO** (VARCHAR2, 50, obrigatório se Pronta Entrega): Código do cliente no banco.

---

### 7.80 PrevisaoRecebimentoMercadoria — MXSPREVRECMERC

**Descrição**: Previsão de recebimento de mercadoria.

**Campos principais**:
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **DTPREVENT** (DATE, obrigatório, PK): Data da previsão.
- **CODFILIAL** (VARCHAR2, 50, obrigatório, PK): Código da filial.
- **QTPENDENTE** (NUMBER, 10, obrigatório): Quantidade.
- **SITUACAO** (VARCHAR2, 2, obrigatório): 'PN' – produto normal.

---

### 7.81 Produtos — MXSPRODUT

**Descrição**: Cadastro de produtos. Obrigatório.

**Campos principais** (seleção):
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **DESCRICAO** (VARCHAR2, 100, obrigatório): Descrição.
- **CODEPTO** (VARCHAR2, 50, obrigatório): Departamento (FK `MXSDEPTO`).
- **CODSEC** (VARCHAR2, 50, obrigatório): Seção (FK `MXSSECAO`).
- **CODCATEGORIA** (VARCHAR2, 50): Categoria (FK `MXSCATEGORIA`).
- **CODMARCA** (VARCHAR2, 50): Marca (FK `MXSMARCA`).
- **CODFORNEC** (VARCHAR2, 50, obrigatório): Fornecedor (FK `MXSFORNEC`).
- **UNIDADE** (VARCHAR2, 2, obrigatório): Unidade de venda.
- **CODIGO** (VARCHAR2, 50): Código do produto (pode ser o mesmo).
- **CODAUXILIAR** (VARCHAR2, 50): Código de barras (obrigatório para venda por embalagem).
- **CLASSIFICFISCAL** (VARCHAR2, 20, obrigatório para Pronta Entrega): NCM.
- **PESOBRUTO** (NUMBER, 12,6, obrigatório): Peso bruto (>0).
- **PESOLIQ** (NUMBER, 12,6, obrigatório): Peso líquido (>0).
- **VOLUME** (NUMBER, 20,8): Volume (m³).
- **ALTURA** (NUMBER, 22): Altura.
- **QTUNIT** (NUMBER, 6,2, obrigatório): Quantidade unitária na embalagem de venda.
- **CUSTOREP** (NUMBER, 22): Preço de compra.
- **PERCIPI** (NUMBER, 22): % IPI na entrada.
- **PERCIPIVENDA** (NUMBER, 22): % IPI na venda.
- **ACEITAVENDAFRACAO** (VARCHAR2, 1): 'S' ou 'N'.
- **PESOVARIAVEL** (VARCHAR2, 1): 'S' ou 'N'.
- **REVENDA** (VARCHAR2, 1, obrigatório): 'S' (revenda) ou 'N'.
- **ENVIARFORCAVENDAS** (VARCHAR2, 1, obrigatório): 'S' ou 'N' – se envia para força de vendas.
- **RESTRICAOTRANSP** (VARCHAR2, 1): 'S' (inflamável), 'N' (normal), 'R' (refrigerado).
- **DTCADASTRO** (DATE, obrigatório para maxGestão): Data de cadastro.
- **DTEXCLUSAO** (DATE): Data de exclusão.

**Relacionamentos**:
- FK para `MXSDEPTO`, `MXSSECAO`, `MXSCATEGORIA`, `MXSMARCA`, `MXSFORNEC`, `MXSTRIBUT` (indiretamente via tabela de preço).
- Pode ter múltiplas embalagens em `MXSEMBALAGEM`.

---

### 7.82 ProdutosAgregados — MXSPRODAGREGADO

**Descrição**: Relação de produtos agregados (ex.: kits).

**Campos principais**:
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Produto principal.
- **CODPRODAGREGADO** (VARCHAR2, 50, obrigatório, PK): Produto agregado.

---

### 7.83 ProdutosFiliais — MXSPRODFILIAL

**Descrição**: Parâmetros de produto por filial.

**Campos principais**:
- **CODFILIAL** (VARCHAR2, 20, obrigatório, PK): Código da filial.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **ACEITAVENDAFRACAO** (VARCHAR2, 1): 'S' ou 'N'.
- **ENVIARFORCAVENDAS** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **MULTIPLO** (NUMBER, 22): Múltiplo para venda.
- **PCOMEXT1** (NUMBER, 22): % comissão externo.
- **PCOMINT1** (NUMBER, 22): % comissão interno.
- **PCOMREP1** (NUMBER, 22): % comissão representante.
- **PROIBIDAVENDA** (VARCHAR2, 2): '' ou 'PV' (proibido venda).
- **QTMAXPEDVENDA** (NUMBER, 22): Quantidade máxima por pedido.
- **QTMINIMAATACADO** (NUMBER, 22): Quantidade mínima atacado.

---

### 7.84 ProdutosSimilares — MXSPRODSIMIL

**Descrição**: Relação de produtos similares.

**Campos principais**:
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Produto principal.
- **CODSIMIL** (VARCHAR2, 50, obrigatório, PK): Produto similar.
- **TIPOPROD** (VARCHAR2, 1, obrigatório): 'S' (similar) ou 'A' (alternativo).

---

### 7.85 ProdutosUsuarios — MXSPRODUSUARIO

**Descrição**: Cotas de produtos por vendedor/cliente (promoções).

**Campos principais**:
- **CODIGO** (NUMBER, 22, obrigatório, PK): Identificador do cadastro.
- **CODCLI** (VARCHAR2, 50): Código do cliente (se por cliente).
- **CODPROD** (VARCHAR2, 50, obrigatório): Código do produto.
- **CODUSUR** (VARCHAR2, 50): Código do vendedor (se por vendedor).
- **DATAINICIO** (DATE, obrigatório): Data inicial da vigência.
- **DATAFIM** (DATE, obrigatório): Data final da vigência.
- **QTMAXVENDA** (NUMBER, 22, obrigatório): Quantidade máxima de venda.
- **CODFILIAL** (VARCHAR2, 50): Código da filial.

---

### 7.86 ProfissionaisClientes — MXSPROFISSIONALCLI

**Descrição**: Profissionais vinculados a cada cliente.

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do usuário (profissional).
- **CODUSUR2** (VARCHAR2, 50): Código do usuário 2.
- **CODUSUR3** (VARCHAR2, 50): Código do usuário 3.

---

### 7.87 RedesClientes — MXSREDECLIENTE

**Descrição**: Redes de clientes (ex.: Carrefour, Walmart).

**Campos principais**:
- **CODREDE** (NUMBER, 22, obrigatório, PK): Código da rede.
- **DESCRICAO** (VARCHAR2, 60, obrigatório): Descrição.
- **CODFUNCCAD** (NUMBER, 22): Funcionário que cadastrou.
- **CODFUNCULTALT** (NUMBER, 22): Último alterador.
- **DTCADASTRO** (DATE): Data de cadastro.
- **DTULTALT** (DATE): Data da última alteração.

**Relacionamentos**:
- FK em `MXSCLIENT` via `CODREDE`.

---

### 7.88 Regioes — MXSREGIAO

**Descrição**: Regiões (vinculadas a tabelas de preço).

**Campos principais**:
- **NUMREGIAO** (VARCHAR2, 50, obrigatório, PK): Código da região.
- **REGIAO** (VARCHAR2, 40, obrigatório): Descrição.
- **PERFRETE** (NUMBER, 22): % frete.
- **PERFRETEESPECIAL** (NUMBER, 22): % frete especial.
- **PERFRETETERCEIROS** (NUMBER, 22): % frete terceiros.
- **STATUS** (VARCHAR2, 1, obrigatório): 'A' (ativa), 'I' (inativa).
- **VLFRETEKGVENDA** (NUMBER, 22): Valor frete/kg venda.
- **UF** (VARCHAR2, 2): UF.
- **CODESTABELECIMENTO** (VARCHAR2, 3): Destinado a Broker.
- **NUMTABELA** (VARCHAR2, 20): Código da tabela da indústria (Broker).
- **CODREPRESENTANTE** (VARCHAR2, 4): Código do representante (Broker).
- **CODFILIAL** (VARCHAR2, 20): Filial vinculada à região.

**Relacionamentos**:
- FK em `MXSPRACA` via `NUMREGIAO`.
- FK em `MXSTABPR` via `NUMREGIAO`.

---

### 7.89 RestricoesVendas — MXSRESTRICAOVENDA

**Descrição**: Restrições de venda (ex.: vendedor não pode vender produto X na região Y).

**Campos principais**:
- **CODRESTRICAO** (NUMBER, 22, obrigatório, PK): Código.
- **CODATIV** (NUMBER, 22): Ramo de atividade.
- **CODAUXILIAR** (VARCHAR2, 50): Código da embalagem.
- **CODCLI** (VARCHAR2, 50): Cliente.
- **CODCOB** (VARCHAR2, 50): Cobrança.
- **CODEPTO** (NUMBER, 22): Departamento.
- **CODFILIAL** (VARCHAR2, 20): Filial.
- **CODFORNEC** (NUMBER, 22): Fornecedor.
- **CODMARCA** (NUMBER, 22): Marca.
- **CODPLPAG** (NUMBER, 22): Plano de pagamento.
- **CODPRACA** (NUMBER, 22): Praça.
- **CODPROD** (VARCHAR2, 50): Produto.
- **CODSEC** (VARCHAR2, 50): Seção.
- **CODSUPERVISOR** (VARCHAR2, 22): Supervisor.
- **CODUSUR** (VARCHAR2, 50): Vendedor.
- **CONDVENDA** (NUMBER, 22): Tipo de venda.
- **NUMREGIAO** (NUMBER, 22): Região.
- **ORIGEMPED** (VARCHAR2, 1, obrigatório): Origem do pedido (F – Força de Vendas).
- **TIPOFJ** (VARCHAR2, 1): Tipo de pessoa.
- **VALORMINIMOVENDA** (NUMBER, 22): Valor mínimo de venda.
- **CODLIPRINC** (VARCHAR2, 50): Cliente principal.
- **CODREDE** (VARCHAR2, 50): Rede do cliente.
- **CODBNF** (VARCHAR2, 5): Tipo de bonificação.
- **CODCIDADE** (VARCHAR2, 50): Cidade.

---

### 7.90 RotaCliente — ERP_MXSROTACLI

**Descrição**: Informações de visita dos vendedores (roteiro).

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor.
- **CODCOMPROMISSO** (VARCHAR2, 50, obrigatório, PK): Identificador do registro.
- **DTPROXVISITA** (DATE, obrigatório): Data da próxima visita.
- **HORAVISITA** (NUMBER, 2): Hora da visita.
- **MINUTOVISITA** (NUMBER, 2): Minuto da visita.
- **PERIODICIDADE** (VARCHAR2, 2, obrigatório): Periodicidade (1,7,14,15,21,28,30,35,42,45).
- **SEQUENCIA** (NUMBER, 6): Sequência para ordenação.
- **DTINICIO** (DATE): Início de vigência.
- **DTFINAL** (DATE): Fim de vigência.
- **NUMSEMANA** (NUMBER, 10, obrigatório): Número da semana (1 a 4).
- **DIASEMANA** (VARCHAR2, 50, obrigatório): Dia da semana (SEGUNDA, TERCA, ...).

**Observação**: Duas formas de uso:
1. ERP informa `DTPROXVISITA` (já calculada) e `NUMSEMANA`=1.
2. Máxima calcula: `DTPROXVISITA` deve ser o primeiro dia do mês; usa `DIASEMANA` e `NUMSEMANA` para calcular.

---

### 7.91 SaldosContasCorrentesRcas — MXSSALDOCCRCA

**Descrição**: Saldo de conta corrente do vendedor.

**Campos principais**:
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor.
- **SALDOCC** (NUMBER, 18,6, obrigatório): Saldo.
- **LIMCREDCC** (NUMBER, 18,6, obrigatório): Limite de crédito.

---

### 7.92 Secoes — MXSSECAO

**Descrição**: Seções de produto.

**Campos principais**:
- **CODSEC** (VARCHAR2, 50, obrigatório, PK): Código da seção.
- **CODEPTO** (VARCHAR2, 50, obrigatório): Código do departamento.
- **DESCRICAO** (VARCHAR2, 40, obrigatório): Descrição.

**Relacionamentos**:
- FK para `MXSDEPTO` via `CODEPTO`.
- FK em `MXSPRODUT` via `CODSEC`.
- FK em `MXSCATEGORIA` via `CODSEC`.

---

### 7.93 Setores — MXSSETOR

**Descrição**: Setores da empresa (para funcionários).

**Campos principais**:
- **CODSETOR** (VARCHAR2, 50, obrigatório, PK): Código do setor.
- **DESCRICAO** (VARCHAR2, 40, obrigatório): Descrição.

---

### 7.94 Subcategorias — MXSSUBCATEGORIA

**Descrição**: Subcategorias de produto.

**Campos principais**:
- **CODSUBCATEGORIA** (VARCHAR2, 50, obrigatório, PK): Código.
- **CODCATEGORIA** (VARCHAR2, 50, obrigatório, PK): Código da categoria.
- **CODSEC** (VARCHAR2, 50, obrigatório, PK): Código da seção.
- **SUBCATEGORIA** (VARCHAR2, 40, obrigatório): Descrição.

**Relacionamentos**:
- FK para `MXSCATEGORIA` via `CODCATEGORIA`.
- FK para `MXSSECAO` via `CODSEC`.

---

### 7.95 Supervisores — MXSSUPERV

**Descrição**: Supervisores.

**Campos principais**:
- **CODSUPERVISOR** (VARCHAR2, 50, obrigatório, PK): Código.
- **COD_CADRCA** (VARCHAR2, 50, obrigatório): Código do vendedor que é supervisor (FK `MXSUSUARI`).
- **CODGERENTE** (VARCHAR2, 50, obrigatório): Código do gerente (FK `ERP_MXSGERENTE`).
- **NOME** (VARCHAR2, 100, obrigatório): Nome.
- **POSICAO** (VARCHAR2, 1, obrigatório): 'A' (ativo) ou 'I' (inativo).

**Relacionamentos**:
- FK em `MXSUSUARI` via `CODSUPERVISOR`.

---

### 7.96 TabelasPrecos — MXSTABPR

**Descrição**: Tabela de preço por região (praça). Obrigatório.

**Campos principais**:
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **NUMREGIAO** (VARCHAR2, 50, obrigatório, PK): Código da região (praça).
- **PVENDA** (NUMBER, 18,6, obrigatório): Preço de venda sem impostos.
- **PVENDA1** (NUMBER, 18,6, obrigatório): Preço bruto (com impostos).
- **CODST** (VARCHAR2, 50): Código da tributação (FK `MXSTRIBUT`).
- **VLIPI** (NUMBER, 18,6, obrigatório): Valor do IPI.
- **VLST** (NUMBER, 18,6): Valor ST.
- **PERDESCMAX** (NUMBER, 10,2, obrigatório): % desconto máximo.
- **PERDESCMAXBALCAO** (NUMBER, 10,2): % desconto máximo balcão.
- **PVENDAATAC** (NUMBER, 18,6): Preço especial atacado.
- **PTABELA** (NUMBER, 18,6): Preço de tabela.
- **DTINICIOVALIDADE** (DATE): Data início validade.
- **DTFIMVALIDADE** (DATE): Data fim validade.
- **CALCULARIPI** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **PERCIPI** (NUMBER, 14,4): % IPI.
- **CALCULARFECPSTVENDA** (VARCHAR2, 1): 'S' ou 'N' – habilita cálculo FECP.
- **ALIQ_ICMS** (NUMBER, 18,6): Alíquota ICMS (SAP).
- **VALR_ICMS_ST_NORMAL** (NUMBER, 18,6): Valor ST calculado (SAP).
- **VALR_ICMS_ST_SIMPLES** (NUMBER, 18,6): Valor ST para simples nacional (SAP).

**Relacionamentos**:
- FK para `MXSPRODUT` via `CODPROD`.
- FK para `MXSREGIAO` via `NUMREGIAO`.
- FK para `MXSTRIBUT` via `CODST`.

---

### 7.97 TabelasPrecosClientes — MXSTABPRCLI

**Descrição**: Tabela de preço por região e filial (para preço diferenciado no processo de filial NF).

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CODFILIALNF** (VARCHAR2, 20, obrigatório, PK): Código da filial de emissão.
- **NUMREGIAO** (NUMBER, 10, obrigatório, PK): Região.

---

### 7.98 TabelasTributacoesERP — MXSTABTRIB

**Descrição**: Cenários tributários utilizados na venda.

**Campos principais**:
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **CODFILIALNF** (VARCHAR2, 20, obrigatório, PK): Filial de emissão da nota.
- **UFDESTINO** (VARCHAR2, 2, obrigatório, PK): UF de destino (cliente).
- **CODOPER** (NUMBER, 10, obrigatório, PK): Tipo de operação (1 – venda normal, 5 – bonificada, 13 – manifesto, 14 – pronta entrega). Se não usar, fixar 0.
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente (ou 0).
- **CODGRUPOTRIBUT** (VARCHAR2, 50, obrigatório, PK): Código do grupo de tributação. Se usar produto, enviar '0'.
- **CODST** (VARCHAR2, 50): Código da tributação (FK `MXSTRIBUT`).

---

### 7.99 TiposBonificacoes — MXSTIPOBONIFIC

**Descrição**: Tipos de bonificação (brinde, doação, degustação, troca, etc.).

**Campos principais**:
- **CODBNF** (VARCHAR2, 50, obrigatório, PK): Código.
- **DESCRICAO** (VARCHAR2, 60, obrigatório): Descrição.
- **MOVIMENTACCRCA** (VARCHAR2, 1): 'S' ou 'N'.
- **CALCULAIPI** (VARCHAR2, 1): 'S' ou 'N'.

---

### 7.100 Tributos — MXSTRIBUT

**Descrição**: Tributações por região (alíquotas e regras).

**Campos principais** (seleção):
- **CODST** (VARCHAR2, 50, obrigatório, PK): Código da figura tributária.
- **OBS** (VARCHAR2, 100, obrigatório): Descrição.
- **SITTRIBUT** (VARCHAR2, 3, obrigatório para Pronta Entrega): Situação tributária (ex.: 00 – tributado integralmente, 10 – ST, etc.).
- **SITTRIBUTPF** (VARCHAR2, 3, obrigatório para Pronta Entrega): Situação tributária para pessoa física.
- **ALIQICMS1** (NUMBER, 8,4, obrigatório): Alíquota ICMS 1.
- **ALIQICMS2** (NUMBER, 8,4): Alíquota ICMS 2.
- **ALIQICMS1FONTE** (NUMBER, 8,4): ICMS 1 fonte.
- **ALIQICMS2FONTE** (NUMBER, 8,4): ICMS 2 fonte.
- **IVA** (NUMBER, 8,4, obrigatório): IVA.
- **IVAFONTE** (NUMBER, 8,4): IVA fonte.
- **PAUTA** (NUMBER, 18,6): Valor de pauta.
- **PERCBASERED** (NUMBER, 8,4): % base reduzida ICMS.
- **PERCBASEREDST** (NUMBER, 8,4): % redução base ST.
- **PERCBASEREDSTFONTE** (NUMBER, 8,4): % redução base ST fonte.
- **PERDIFEREIMENTOICMS** (NUMBER, 8,4): % diferimento ICMS.
- **PERCDESCCOFINS** (NUMBER, 12,4): % desconto COFINS.
- **PERCDESCPIS** (NUMBER, 12,4): % desconto PIS.
- **PERCDESCSUFRAMA** (NUMBER, 8,4): % desconto Suframa.
- **PERCREDPVENDASIMPLESNAC** (NUMBER, 8,4): % redução para simples nacional.
- **AGREGARIPICALCULOST** (VARCHAR2, 1): Agrega IPI ao ST.
- **USAVALORULTENTBASEST** (VARCHAR2, 1): Usa valor da última entrada como base ST.
- **CODFISCALVENDAPRONTAENT** (NUMBER, 10, obrigatório para Pronta Entrega): CFOP venda pronta entrega dentro do estado.
- **CODFISCALVENDAPRONTAENTINTER** (NUMBER, 10, obrigatório para Pronta Entrega): CFOP interestadual.
- **CODFISCALBONIFIC** (NUMBER, 10, obrigatório para Pronta Entrega): CFOP bonificação dentro do estado.
- **CODFISCALBONIFICINTER** (NUMBER, 10, obrigatório para Pronta Entrega): CFOP bonificação interestadual.
- **FORMULAPVENDA** (VARCHAR2, 50): Fórmula para cálculo FECP.
- **UTILIZAMOTORCALCULO** (VARCHAR2, 1): Usa motor de cálculo da Máxima.
- **ALIQICMSFECP** (NUMBER, 8,4): Alíquota FECP.

**Relacionamentos**:
- FK em `MXSTABPR` via `CODST`.

---

### 7.101 Tributos – Regra de negócio para tabela de preço e impostos

**Explicação**: A tabela de preço do maxPedido é definida por região. Não há ligação direta entre cliente e tabela de preço. Para relacionar o cliente à tabela de preço, utiliza-se as tabelas de praça e região:
- `MXSCLIENT.CODPRACA` → `MXSPRACA.CODPRACA`
- `MXSPRACA.NUMREGIAO` → `MXSREGIAO.NUMREGIAO`
- `MXSREGIAO.NUMREGIAO` → `MXSTABPR.NUMREGIAO`

Caso o ERP não trabalhe com região/praça, é necessário enviar essas informações mesmo que fictícias.

O aplicativo maxPedido espera dois preços:
- `PVENDA` (preço líquido sem impostos) – base para formação do preço final com incidência de impostos.
- `PVENDA1` (preço bruto) – usado na listagem de produtos.

Além disso, a tributação (alíquotas, ST, etc.) é definida em `MXSTRIBUT` e vinculada via `CODST` na tabela de preço. Para determinar a tributação correta na venda, o sistema consulta `MXSTABTRIB` com base no produto, filial de emissão e UF de destino do cliente.

Exceções (benefícios) podem ser definidas nas entidades:
- **Filial**: `MXSFILIAL` – parâmetros como "Não calcula IPI", "Não calcula ST para pessoa física".
- **Cliente**: `MXSCLIENT` – campos como `SIMPLESNACIONAL`, `SUFRAMA`, `ISENTOPIS`, `ISENTOCOFINS`, etc. As alíquotas correspondentes vêm de `MXSTRIBUT`.
- **Produto**: `MXSPRODUT` – alíquotas diferenciadas por produto (sobrescrevem tributação padrão).

---

### 7.102 Transportadoras — MXSTRANSP

**Descrição**: Cadastro de transportadoras.

**Campos principais**:
- **CODTRANSP** (VARCHAR2, 50, obrigatório, PK): Código.
- **TRANSPORTADORA** (VARCHAR2, 50, obrigatório): Razão social.
- **FANTASIA** (VARCHAR2, 60): Nome fantasia.
- **CGC** (VARCHAR2, 50, obrigatório): CNPJ/CPF.
- **ENDERECO** (VARCHAR2, 50, obrigatório): Endereço.
- **BAIRRO** (VARCHAR2, 20, obrigatório): Bairro.
- **CIDADE** (VARCHAR2, 100, obrigatório): Cidade.
- **UF** (VARCHAR2, 2, obrigatório): UF.
- **TELEFONE** (VARCHAR2, 50, obrigatório): Telefone.
- **BLOQUEIO** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **EREDESPACHO** (VARCHAR2, 1, obrigatório): 'S' ou 'N' – redespacho.
- **EXIGEREDESPACHO** (VARCHAR2, 1): 'S' ou 'N'.
- **PERGRIS** (NUMBER, 18,6): % GRIS.
- **VLPEDAGIO** (NUMBER, 18,6): Valor pedágio.
- **REVENDA** (VARCHAR2, 1, obrigatório): 'T' (transportadora).

---

### 7.103 Usuaris — MXSUSUARI

**Descrição**: Cadastro de vendedores (usuários). Obrigatório.

**Campos principais**:
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código.
- **NOME** (VARCHAR2, 100, obrigatório): Nome.
- **CODSUPERVISOR** (VARCHAR2, 50, obrigatório): Supervisor (FK `MXSSUPERV`).
- **CODFILIAL** (VARCHAR2, 50, obrigatório): Filial.
- **TIPOVEND** (VARCHAR2, 2, obrigatório): 'I' (interno), 'E' (externo), 'R' (representante), 'P' (profissional).
- **BLOQUEIO** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.
- **EMAIL** (VARCHAR2, 100): E-mail.
- **TELEFONE1** (VARCHAR2, 13): Telefone.
- **PERCENT** (NUMBER, 4,2): % comissão (vv).
- **PERCENT2** (NUMBER, 6,2): % comissão (vp).
- **PERMAXVENDA** (NUMBER, 18,6): % máximo acréscimo.
- **QTPEDPREV** (NUMBER, 6): Quantidade prevista de pedidos.
- **USADEBCREDRCA** (VARCHAR2, 1): Usa débito/crédito RCA?.
- **VALIDARACRESCDESCPRECOFIXO** (VARCHAR2, 1): Valida crédito/desconto preço fixo.
- **VLVENDAMINPED** (NUMBER, 22): Valor mínimo por pedido.

---

### 7.104 VisitaFv — ERP_MXSVISITAFV

**Descrição**: Visitas realizadas ao cliente pelo vendedor.

**Campos principais**:
- **CODCLI** (VARCHAR2, 50, obrigatório, PK): Código do cliente.
- **CODUSUR** (VARCHAR2, 50, obrigatório, PK): Código do vendedor.
- **DATA** (DATE, obrigatório, PK): Data da visita.
- **CODMOTIVO** (NUMBER, 6, obrigatório): Justificativa da visita (FK `MXSMOTVISITA`).
- **CGCCLI** (VARCHAR2, 18, obrigatório): CPF/CNPJ do cliente.
- **HORAINICIAL** (NUMBER, 2): Hora início.
- **HORAFINAL** (NUMBER, 2): Hora fim.
- **MINUTOINICIAL** (NUMBER, 2): Minuto início.
- **MINUTOFINAL** (NUMBER, 2): Minuto fim.

---

### 7.105 ValidadesWms — MXSVALIDADEWMS

**Descrição**: Validade dos produtos no WMS.

**Campos principais**:
- **CODFILIAL** (VARCHAR2, 50, obrigatório, PK): Código da filial.
- **CODPROD** (VARCHAR2, 50, obrigatório, PK): Código do produto.
- **DATA** (DATETIME, obrigatório, PK): Data de validade.
- **QTDE** (NUMBER, 26,8, obrigatório): Quantidade disponível.

---

## 8. Endpoints de Saída (Retornos) do maxPedido

Os pedidos e cadastros de clientes confeccionados no Força de Vendas da Máxima são disponibilizados via API e devem ser consumidos pelo serviço do ERP. A API é um simples ouvinte; o serviço de gravação de dados do ERP deve gerar requisições à API de Saída, solicitando os pedidos disponíveis para serem persistidos no ERP. Para cada pedido ou cadastro de cliente processado pelo ERP, é necessário enviar um retorno no padrão da Máxima, para manutenção do status.

### 8.1 StatusPedidos (GET) — Consulta de pedidos pendentes

**Endpoint**: `http://URL_API_SAIDA:PORTA/api/v1/StatusPedidos/0,1,2,9/1` (pedidos) ou `/2` (orçamentos)

**Descrição**: Retorna lista de pedidos/orçamentos pendentes de integração.

**Estrutura de retorno (JSON)**:

- **id_pedido** (NUMBER, 20, obrigatório): Identificador do pedido na nuvem (Máxima).
- **numped** (NUMBER, 10): Número do pedido no maxPedido.
- **objeto_json** (String JSON): Objeto completo do pedido (deserializar para navegar).
- **status** (NUMBER, 4): Status atual:
  - 0: Pedido recebido pelo servidor (Máxima)
  - 1: Pedido enviado para API (Máxima)
  - 2: Pedido enviado para o ERP (Máxima)
  - 3: Pedido em processamento pelo ERP
  - 4: Pedido importado pelo ERP
  - 5: Pedido com erro ao importar no ERP
  - 9: Pedido liberado para envio ao ERP
- **data** (DATE): Data da última atualização.
- **critica** (String JSON): Objeto crítica do pedido.
- **tipopedido** (NUMBER, 3): 1 (pedido normal) ou 2 (orçamento).
- **codusur** (VARCHAR2, 50): Código do usuário no ERP.
- **codusuario** (NUMBER, 10): Código do usuário na Máxima.
- **numcritica** (NUMBER, 16): Número da crítica (yyyyMMddHHmmssSS).
- **tipocritica** (NUMBER, 10): 0 (sucesso) ou 2 (erro).

**Objeto_json**: Ver modelo disponível em `https://maxsolucoes-versoes.s3.amazonaws.com/LayoutIntegracaoModelos/Objeto_Json.txt`. Contém todas as informações do pedido: cliente, itens, totais, pagamentos, etc.

---

### 8.2 StatusPedidos (PUT) — Atualização do status do pedido

**Endpoint**: `http://URL_API_SAIDA:PORTA/api/v1/StatusPedidos`

**Descrição**: Após processar o pedido (sucesso ou erro), enviar a mesma estrutura retornada pelo GET, com alterações nos campos indicados.

**Campos a alterar**:
- **status**: 4 (processado) ou 5 (erro).
- **critica**: Objeto JSON preenchido com detalhes.
- **numcritica**: Gerar novo número (formato yyyyMMddHHmmssSS).
- **tipocritica**: 0 (sucesso) ou 2 (erro).
- **numpederp** (NUMBER, 10): Número do pedido no ERP (se gerado).

**Estrutura da crítica (JSON)**:
```json
{
  "numPedido": 123,
  "codigoPedidoNuvem": 456,
  "numPedidoERP": 789,
  "numCritica": 2025030614301500,
  "codigoUsuario": 10,
  "data": "2025-03-06T14:30:15",
  "tipo": "Sucesso",
  "posicaoPedidoERP": "Liberado",
  "codigoTipoVenda": 1,
  "statusDaAssinatura": 0,
  "excluirPedido": false,
  "salvarCritica": true,
  "enviarEmailPedidoAutomaticoParaSupervisor": false,
  "salvarJustificativaNaoVendaPrePedido": false,
  "atualizacaoPosPedido": true,
  "cancelado": false,
  "houveExcessao": false,
  "packageValida": true,
  "Itens": [
    { "id": 0, "ordem": 0, "mensagem": "Pedido Importado com Sucesso" }
  ]
}
```

---

### 8.3 StatusCriticas (PUT) — Atualização de críticas de pedidos

**Endpoint**: `http://URL_API_SAIDA:PORTA/api/v1/StatusCriticas`

**Descrição**: Para atualizações de status/críticas posteriores à importação.

**Campos** (similar ao PUT de StatusPedidos, mas sem `objeto_json`):
- **id_pedido** (NUMBER, 20, obrigatório)
- **status** (NUMBER, 4): 4 ou 5
- **data** (DATE)
- **critica** (String JSON)
- **numcritica** (NUMBER, 16)
- **tipocritica** (NUMBER, 10)
- **numpederp** (NUMBER, 10)

---

### 8.4 StatusClientes (GET) — Consulta de clientes pendentes

**Endpoint**: `http://URL_API_SAIDA:PORTA/api/v1/StatusClientes/0,1,2,5,9`

**Descrição**: Retorna cadastros de clientes pendentes de integração.

**Estrutura de retorno**:
- **id_cliente** (NUMBER, 10, obrigatório): Identificador do cliente na nuvem.
- **data** (DATE): Data/hora do cadastro.
- **objeto_json** (String JSON): Objeto completo do cliente.
- **status** (NUMBER, 4): Status semelhante ao de pedidos.

**Objeto_json**: Modelo em `https://maxsoluocoes-versoes.s3.amazonaws.com/LayoutIntegracaoModelos/Objeto_Json_Cli.txt`.

---

### 8.5 StatusClientes (PUT) — Atualização do status do cliente

**Endpoint**: `http://URL_API_SAIDA:PORTA/api/v1/StatusClientes`

**Descrição**: Após processar o cadastro, enviar a estrutura com alterações.

**Campos a alterar**:
- **objeto_json**: Editar as propriedades:
  - "Codigo": informar o código do cliente no ERP.
  - "CriticaImportacao": descrição do status.
  - "RetornoImportacao": 1 (pendente), 2 (sucesso), 3 (erro).
- **status**: 4 (processado), 5 (erro), 7 (bloqueado/cancelado).

---

## 9. Endpoints Exclusivos do Processo Pronta Entrega (Entrada)

URL base: `http://URL_API_ENTRADA:PORTA/api/v2/NOME_ENDPOINT`

### 9.1 Banco — MXSBANCO

**Descrição**: Cadastro de bancos (código BACEN).

**Campos principais**:
- **CODBANCO** (NUMBER, 10, obrigatório, PK): Código do banco (BACEN).
- **NOME** (VARCHAR2, 200, obrigatório): Nome do banco.

---

### 9.2 CategoriaDespesas (Naturezas) — MXSCATEGORIADESPESAS

**Descrição**: Categorias de despesas para lançamento no Pronta Entrega.

**Campos principais**:
- **CODCATEGORIADESPESA** (NUMBER, 10, obrigatório, PK): Código.
- **DESCRICAO** (VARCHAR2, 300, obrigatório): Descrição.
- **ATIVO** (VARCHAR2, 1, obrigatório): 'S' ou 'N'.

---

### 9.3 ContasBancarias — MXSCONTASBANCARIAS

**Descrição**: Contas bancárias da empresa.

**Campos principais**:
- **CODCONTA** (VARCHAR2, 40, obrigatório, PK): Código da conta.
- **CODBANCO** (VARCHAR2, 40, obrigatório): Código do banco (FK `MXSBANCO`).
- **AG** (VARCHAR2, 40, obrigatório): Agência.
- **NUMCONTA** (VARCHAR2, 40, obrigatório): Número da conta.
- **CODFILIAL** (VARCHAR2, 50, obrigatório): Filial.
- **DESCRICAO** (VARCHAR2, 60, obrigatório): Descrição.
- **TIPO** (VARCHAR2, 4, obrigatório): 'A' (aplicação), 'C' (conta corrente), 'D' (adiantamento), 'E' (empréstimo), 'G' (garantida), 'M' (comissões), 'O' (outros), 'S' (sócios), 'X' (caixa/tesouraria), 'Z' (caixa PDV).

---

### 9.4 Cfos — MXSCFO

**Descrição**: Cadastro de CFOP.

**Campos principais**:
- **CODFISCAL** (VARCHAR2, 50, obrigatório, PK): Código fiscal.
- **DESCCFO** (VARCHAR2, 100, obrigatório): Descrição.

---

### 9.5 Carregamentos — ERP_MXSCARREG

**Descrição**: Carregamentos (ordens de carga). Ver descrição completa na seção 7.2 (pois é usado também por maxRoteirizador).

**Campos adicionais no contexto Pronta Entrega**:
- **ORIGEM_CAR** (VARCHAR2, 50, obrigatório): 'ERP', 'PRO' (Pronta Entrega) ou 'ROT' (maxRoteirizador).

---

### 9.6 NotasSaidaCapas (Manifestos/Cabeçalho de Nota) — ERP_MXSNFSAID

Ver seção 7.68.

---

### 9.7 NotasSaidaItens (Movimentação/Itens de Nota) — ERP_MXSMOV

Ver seção 7.69.

---

### 9.8 Doceletronico — MXSDOCELETRONICO

**Descrição**: XML das NF de saída (para reimpressão).

**Campos principais**:
- **NUMTRANSACAO** (NUMBER, 10, obrigatório, PK): Sequencial (mesmo de `NotasSaidaCapas.NUMTRANSVENDA`).
- **XMLNFE** (CLOB, obrigatório): XML da nota.
- **NUMPED** (NUMBER, 10): Número do pedido.

---

## 10. Endpoints Exclusivos do Processo Pronta Entrega (Saída)

URL base: `http://URL_API_ENTRADA:PORTA/api/v2/NOME_ENDPOINT` (GET)

### 10.1 PrestacaoContasCapas — MXSPRESTACAOCONTASC

**Descrição**: Controle de caixa (prestação de contas) do vendedor/motorista.

**Campos principais**:
- **CODPRESTACAOCONTAC** (VARCHAR2, 40, obrigatório, PK): Código.
- **STATUS** (NUMBER, 1, obrigatório): 1 (aberto) ou 2 (fechado).
- **NUMCARMANIF** (VARCHAR2, 50): Número do carregamento.
- **CODUSUR** (VARCHAR2, 50): Código do vendedor.
- **DATAABERTURA** (DATE, obrigatório): Data de abertura.
- **DATAFECHAMENTO** (DATE): Data de fechamento.
- **NUMLACRE** (VARCHAR2, 50): Número do lacre do malote.
- **OBS** (VARCHAR2, 400): Observação.
- **TOTAL** (NUMBER, 18,6): Total geral.
- **TOTALDESPESAS** (NUMBER, 18,6): Total de despesas.
- **TOTALRECEBIMENTOS** (NUMBER, 18,6): Total de recebimentos.
- **TOTALDEPOSITOS** (NUMBER, 18,6): Total de depósitos.

---

### 10.2 PrestacaoContasItens — MXSPRESTACAOCONTASI

**Descrição**: Itens da prestação de contas (despesas, recebimentos, etc.).

**Campos principais**:
- **CODPRESTACAOCONTASI** (VARCHAR2, 40, obrigatório, PK): Código do item.
- **CODPRESTACAOCONTAC** (VARCHAR2, 40, obrigatório): FK para o cabeçalho.
- **CODCATEGORIADESPESA** (VARCHAR2, 40): Código da categoria (se despesa).
- **DATALANCAMENTO** (DATE, obrigatório): Data.
- **TIPO** (NUMBER, 1, obrigatório): 1 (despesa), 2 (recebimento), 3 (depósito), 4 (ajuste), 5 (malote).
- **CODCONTA** (VARCHAR2, 50): Conta bancária (se aplicável).
- **FORMAPAGAMENTO** (VARCHAR2, 1, obrigatório): 1 (dinheiro), 2 (cheque), 3 (cartão).
- **OBS** (VARCHAR2, 200): Observação.
- **NUMTRANSVENDA** (NUMBER, 10): Número da transação da venda (se recebimento).
- **DUPLIC** (NUMBER, 10): Duplicata.
- **PREST** (VARCHAR2, 4): Prestação do título.
- **VALOR** (NUMBER, 18,6, obrigatório): Valor.
- **VLDESCONTO** (NUMBER, 18,6): Desconto.
- **VLIUROS** (NUMBER, 18,6): Juros.
- **NUMPEDRCA** (NUMBER, 10): Número do pedido na Máxima.
- **EXCLUIDO** (VARCHAR2, 1): 'S' ou 'N'.
- **ID_ERP** (VARCHAR2, 50, obrigatório): Identificador único do título no ERP.

---

### 10.3 StatusPedidos (Pronta Entrega)

**Descrição**: Mesma estrutura do endpoint de pedidos (seção 8), porém com campos específicos da operação Pronta Entrega.

**Campos adicionais no objeto_json**:
- **TipoVenda.Codigo**: 14 (Venda Pronta Entrega) ou 24 (Bonificação Pronta Entrega).
- **DadosProntaEntrega** (objeto, presente se nota em contingência):
  - UtilizaSeloSefaz (boolean)
  - NumeroFormularioIni (number)
  - NumeroFormularioEnd (number)
  - NumeroSeloIni (number)
  - NumeroSeloEnd (number)
  - NumeroAIDF (string)
  - NumNotaFiscal (number)
  - SerieNotaFiscal (string)
  - NumCarregamento (string)
  - GerarNFe (boolean)
  - GerarBoletos (boolean)
  - Contigencia (boolean)
  - JustificativaContigencia (string)
  - DataHoraEntradaContigencia (date)
  - ChaveAcessoNFe (string)
- **Produtos[i].Impostos** (objeto com detalhes dos impostos calculados):
  - ValorST, ValorST_Tabela, ValorIPI_Tabela, ValorIPI, ValorBaseST, MargemPrecificacao, ValorSTClienteGNRE, TributacaoFonteSTAtiva, DescontoReducaoPIS, DescontoReducaoPISEntrada, PercDescontoPIS, DescontoReducaoCofins, DescontoReducaoCofinsEntrada, PercDescontoCofins, ValorDescontoSUFRAMA, ValorDescontoSUFRAMAEntrada, ValorDescontoPISSUFRAMA, ValorDescontoICMSInsencao, PercDescontoIsentoICMS, ValorDiferencaAliquotas, BaseDiferencaAliquotas, PercDiferencaAliquotas, ValorReducaoSimplesNacional, ValorReducaoCMVSimplesNacional, PercReducaoSimplesNacional, ValorDescAcrescPlanoPagamento, ValorBaseICMS, ValorICMS, ValorSTSemReducaoSimples, ValorFECP, BaseFECP.

---

## 11. Endpoints do maxMotorista e maxRoteirizador (Entrada)

URL base: `http://URL_API_ENTRADA:PORTA/api/v2/NOME_ENDPOINT`

Muitos endpoints já foram descritos nas seções anteriores. Aqui estão os específicos ou com observações adicionais.

### 11.1 Atividades — MXSATIVI

Ver seção 7.3. Utilizado para filtrar pedidos por atividade e legendar pins no mapa.

### 11.2 Carregamentos — ERP_MXSCARREG

Ver seção 9.5. Essencial para motorista e roteirizador.

### 11.3 Cidades — MXSCIDADE

Ver seção 7.9. Obrigatório.

### 11.4 Clientes — MXSCLIENT

Ver seção 7.10. Obrigatório.

### 11.5 ClientesEnderecos — MXSCLIENTEENDERECOS

Ver seção 7.12.

### 11.6 Clientes (Última Compra) — MXSCLIENT

Ver seção 7.17. Usado para geocodificação de clientes que compraram em determinada data.

### 11.7 Cobrancas — MXSCOB

Ver seção 7.19.

### 11.8 Contatos — MXSCONTATO

Ver seção 7.27.

### 11.9 Emprs — MXSEMPR

Ver seção 7.39. Obrigatório (para motoristas).

### 11.10 Filiais — MXSFILIAL

Ver seção 7.43. Obrigatório.

### 11.11 HistoricosPedidosCapas — MXSHISTORICOPEDC

Ver seção 7.51. Obrigatório.

### 11.12 HistoricosPedidosItens — MXSHISTORICOPEDI

Ver seção 7.52.

### 11.13 HistoricosPedidosCortes — MXSHISTORICOPEDCORTE

Ver seção 7.53.

### 11.14 HistoricosPedidosFaltas — MXSHISTORICOPEDFALTA

Ver seção 7.54.

### 11.15 Doceletronico — MXSDOCELETRONICO

Ver seção 9.8. Usado para reenvio de XML ao motorista.

### 11.16 NotasSaidaCapas — ERP_MXSNFSAID

Ver seção 7.68. Obrigatório.

### 11.17 NotasSaidaItens — ERP_MXSMOV

Ver seção 7.69. Obrigatório.

### 11.18 PlanosPagamentos — MXSPLPAG

Ver seção 7.71.

### 11.19 PrestacoesTitulos (Títulos) — ERP_MXSPREST

Ver seção 7.79. Para consulta de títulos no motorista.

### 11.20 Produtos — MXSPRODUT

Ver seção 7.81. Obrigatório.

### 11.21 Regioes — MXSREGIAO

Ver seção 7.88. Para agrupamento.

### 11.22 RotasExps — MXSROTAEXP

**Descrição**: Rotas de entrega.

**Campos principais**:
- **CODROTA** (NUMBER, 4, obrigatório, PK): Código da rota.
- **DESCRICAO** (VARCHAR2, 40, obrigatório): Descrição.
- **DIASENTREGA** (NUMBER, 3): Dias de entrega.
- **TIPOCOMISSAO** (VARCHAR2, 1): Tipo de comissão.
- **KMROTA** (NUMBER, 10,2): KM máximo da rota.
- **VDIARIA** (NUMBER, 10,4): Valor da diária.
- **SEQENTREGA** (NUMBER, 4): Sequência de entrega.
- **VLMINCARREG** (NUMBER, 10,2): Valor mínimo de carregamento.
- **QTENTREGA** (NUMBER, 4): Quantidade máxima de entregas.
- **VLFRETEENTREGA** (NUMBER, 10,4): Valor do frete.
- **SITUACAO** (VARCHAR2, 1, obrigatório): Situação.

**Relacionamentos**:
- FK em `MXSCLIENT` via `CODROTA`.

### 11.23 Supervisores — MXSSUPERV

Ver seção 7.95.

### 11.24 Usuaris — MXSUSUARI

Ver seção 7.103. Obrigatório.

### 11.25 Veiculos — ERP_MXSVEICUL

**Descrição**: Cadastro de veículos.

**Campos principais**:
- **CODEVICULO** (VARCHAR2, 50, obrigatório, PK): Identificador.
- **DESCRICAO** (VARCHAR2, 80, obrigatório): Descrição.
- **PLACA** (VARCHAR2, 10, obrigatório): Placa.
- **MARCA** (VARCHAR2, 40): Marca.
- **QTPALETE** (NUMBER, 4): Quantidade de paletes.
- **VOLUME** (NUMBER, 10,4, obrigatório): Capacidade de volume (m³).
- **PESOCARGAKG** (NUMBER, 10,2, obrigatório): Capacidade de peso (kg).
- **SITUACAO** (VARCHAR2, 1, obrigatório): 'V' (viagem), 'O' (oficina), 'B' (bloqueado), 'L' (livre), 'I' (inativo).
- **TIPOVEICULO** (VARCHAR2, 1): 'L' (leve), 'M' (médio), 'P' (pesado), 'E' (extra pesado).
- **PROPRIO** (VARCHAR2, 1): 'S' ou 'N'.
- **CODFILIAL** (VARCHAR2, 50, obrigatório): Filial.
- **ALTURA** (NUMBER, 10,3): Altura.
- **LARGURA** (NUMBER, 10,3): Largura.
- **COMPRIMENTO** (NUMBER, 10,3): Comprimento.
- **OBS** (VARCHAR2, 50): Observação.
- **RASTREADO** (VARCHAR2, 1): 'S' ou 'N'.
- **UFPLACAVEICULO** (VARCHAR2, 2): UF da placa.
- **CIDADEPLACAVEICULO** (VARCHAR2, 30): Cidade da placa.

---

## 12. Endpoints de Saída do maxRoteirizador

### 12.1 Carregamentos (GET) — Pendentes

**Endpoint**: `URL/Carregamentos/Pendentes`

**Descrição**: Retorna carregamentos montados no ERP que precisam de roteirização.

**Campos retornados** (mesma estrutura de `ERP_MXSCARREG`):
- NUMCAR, DTSAIDA, CODMOTORISTA, CODEVICULO, TOTPESO, TOTVOLUME, VLTOTAL, DTFECHADO, OBS_DESTINO, NUMNOTAS, CODCONF, DT_CANCEL, DATAMON, CODFUNCMON, DTFAT, DTSAIDAVEICULO.

### 12.2 HistoricosPedidosCapas (GET) — Por número de carregamento

**Endpoint**: `URL/HistoricosPedidosCapas/PorNumeroDoCarregamento/{NumCar}`

**Descrição**: Retorna os pedidos associados a um carregamento.

**Campos**: mesmos de `MXSHISTORICOPEDC`.

**Uso**: Após roteirização, o sistema atualiza os pedidos com `numcar`, `posicao='M'` e `numsequentrega`.

### 12.3 Carregamentos (PUT) — Atualização de status

**Endpoint**: `URL/Carregamentos`

**Descrição**: Atualiza informações do carregamento (cancelamento, fechamento, etc.).

**Campos a enviar**:
- NUMCAR (obrigatório)
- DTSAIDA (se houver)
- DTFECHADO (se houver)
- NUMNOTAS (quantidade de notas)
- DT_CANCEL (se cancelado)
- DTFAT (se faturado)

---

## 13. Considerações Finais

Este documento é um mapeamento da estrutura de dados da Máxima. Podem existir ajustes na interface de integração, bem como criação/alteracão de rotas/endpoints. Qualquer necessidade de mudanças nas APIs ou serviço de extração será comunicada com antecedência aos envolvidos.

---

## 14. Histórico de Alterações no Layout

| Versão     | EndPoint/Seção               | Descrição                                                                 |
|------------|------------------------------|---------------------------------------------------------------------------|
| 2025.10.09 | HistoricosPedidosItens       | Adicionado campo NUMCAR                                                   |
| 2025.09.24 | ObterDadosLogística          | Renomeado endpoint                                                        |
| 2025.09.17 | FiltrarRegiaoRCA             | Adicionado o endpoint FiltrarRegiaoRCA                                    |
| 2025.07.22 | Outros                       | Adicionado informativo de estrutura do JSON                               |
| 2025.07.03 | FeriasVendedor               | Adicionado endpoint de controle de férias do vendedor                     |
| 2025.06.17 | Vários                       | Correções ortográficas nas regras de tributação                           |
| 2025.06.13 | Erp_entrega_eventos          | Adicionado endpoint de eventos de entrega                                 |
| 2025.05.23 | Erp_Mxsnfent                 | Excluído a linha CODOPERACAO do layout                                    |
| 2025.05.20 | Erp_Mxsnfent                 | Ajustes no campo CODOPERACAO para NUMBER                                  |
| 2025.04.29 | Mxsclient                    | Adicionado o campo DTULTALTER                                              |
| 2025.02.12 | Mxshistoricopedc             | Adicionado o campo DTABERTURAPEDPALM                                      |
| 2025.02.12 | Erp_mxsmeta                  | Adicionado o campo QTCAIXAPREV                                            |
| 2025.02.12 | Mxsrestricaoenda             | Ajustado no campo CODSEC para VARCHAR2(50)                                |
| 2025.02.12 | NotasSaidaCapas              | Adicionado campo COMISSAO na tabela                                       |
| 2025.02.12 | Mxsintegracaoindenizacao     | Adicionado endpoint de integração das indenizações                        |
| 2025.02.03 | DiasUteis                    | Adicionado endpoint de dias úteis                                         |
| 2024.11.05 | Hierarquia 1 e Hierarquia 2  | Ajustes no tamanho dos campos numpederp e numpedidoerp                    |
| 2024.05.23 | Vários                       | Adicionado descrições do maxRoteirizador e maxMotorista                   |
| 2024.02.16 | MxsfiltroregiaoRCA           | Adicionado o endpoint do filtro de região por vendedor                    |
| 2023.11.30 | Mxsanexoclientes             | Adicionado endpoint dos anexos de clientes                                |
| 2023.10.04 | RestricoesVendas             | Adicionado o campo CODBNF                                                 |
| 2023.09.28 | RotaCliente                  | Ajustada as chaves primárias do endPoint                                  |
| 2023.09.28 | MixClientes                  | Ajustado o campo NUMTRANSVENDA com a opção PK com S                       |
| 2023.09.28 | TabelasPrecos                | Adicionado o campo PERDESCMAXBALCAO                                       |
| 2023.09.28 | HistoricosPedidosCapas       | Ajuste na descrição do campo POSICAO                                      |
| 2023.06.16 | 5.9 Clientes                 | Inserida nova descrição no campo PAISENT                                  |
| 2022.12.28 | ComissoesUsuarios            | Ajustado os campos PERCDESCIFIM e PERCDESCINI                             |
| 2022.11.29 | MixClientes                  | Remoção do campo CODUSUR                                                  |
| 2022.11.29 | Hierarquia 1 e Hierarquia 2  | Ajuste dos status informados                                              |
| 2022.11.14 | Produtos                     | Adicionado o campo CODGRUPOTRIBUT                                         |
| 2022.10.19 | TabelasPrecos                | Adicionado o campo PERCIPI                                                |
| 2022.09.27 | TabelasPrecos                | Adicionado o campo CALCULARFECPSTVENDA (habilita cálculo FECP)            |
| 2022.09.27 | Tributos                     | Adicionado o campo ALIQICMSFECP (alíquota FECP)                           |
| 2022.08.17 | 6.2 StatusPedidos (PUT)      | Correção no campo status                                                  |
| 2022.08.17 | 6.1 StatusPedidos (GET)      | Correção no campo status                                                  |
| 2022.08.12 | GruposCampanhasItens         | Incluído o endpoint GruposCampanhasItens                                  |
| 2022.08.12 | GruposCampanhas              | Incluído o endpoint GruposCampanhas                                       |
| 2022.07.18 | 2.2 CLIENTES NÃO WINTHOR     | Nova informação sobre a carga incremental                                 |
| 2022.07.08 | Devolucoes                   | Alteração do tamanho do campo MOTIVO                                      |
| 2022.07.07 | NotasSaidaItens              | Alteração do tamanho dos campos NUMTRANSENT e NUMTRANSVENDA              |
| 2022.07.04 | TabelasTributacoesERP        | Adicionado o campo CODGRUPOTRIBUT como obrigatório                        |
| 2022.06.20 | Produtos                     | Adicionado campo ENVIARFORCAVENDAS como obrigatório                       |
| 2021.10.21 | Setores                      | Ajuste nome tabela                                                        |
| 2021.10.21 | Hierarquia 2                 | Ajuste no campo status                                                    |
| 2021.07.02 | Hierarquia 1                 | Ajuste no campo status                                                    |
| 2021.06.16 | Setores                      | Incluída os dados do endpoint de setores                                  |
| 2021.06.10 | Carregamentos (PUT)          | Ajuste no status                                                          |
| 2021.04.06 | Tributos                     | Adicionado o campo PERDIFEREIMENTOICMS                                    |
| 2021.04.01 | PlanosPagamentos             | Adicionado o campo USAMULTIFILIAL                                         |
| 2021.03.31 | Tributos                     | Adicionado o campo SITTRIBUTPF, obrigatório para pronta entrega          |
| 2021.03.23 | Nfent (NF Entrada/Devolução) | Alterado o campo CODFISCAL para ser obrigatório                           |
| 2021.02.18 | NomesProfissionais           | Incluído o endpoint NomesProfissionais                                    |
| 2021.02.18 | ProfissionaisClientes        | Incluído o endpoint ProfissionaisClientes                                 |
| 2019.10.28 | Nfent                        | Removida obrigatoriedade do campo CODFISCAL                               |
| 2019.10.28 | Nfent                        | Incluído campo TIPODESCARGAR (tipo da nota)                               |
| 2019.10.24 | Estado                       | Incluído Endpoint para UF                                                 |
| 2019.10.24 | Geral                        | Ajustes no layout (maxMotorista e maxRoteirizador)                        |
| 2019.10.21 | FilialRegiao                 | Incluído Endpoint para vínculos entre Regiões e Filiais                   |
| 2019.10.08 | PlanosPagamentosFiliais      | Incluído Endpoint para vínculos entre Planos de pagamentos e Filiais      |
| 2019.10.07 | Metas                        | Remoção de campos data como chave primária                                |
| 2019.10.01 | Geral                        | Ajustado obrigatoriedade de tabelas e colunas (maxGestão)                 |
| 2019.09.27 | Lotes                        | Incluído endpoint para receber informações de lotes                       |
| 2019.09.23 | Tributos                     | Mudança da observação dos códigos fiscais/CFOPs                           |
| 2019.09.17 | VisitaFv                     | Alterado a identificação do Endpoint Visitas para VisitaFv                |
| 2019.09.12 | ClientesLocalizações         | Incluído endpoint para retornar coordenadas GPS de clientes               |
| 2019.09.12 | NF Devolução                 | Incluído endpoints para receber NF de devolução                           |
| 2019.09.05 | ValidadesWms                 | Incluído Endpoint de Validade de produtos do WMS                          |
| 2019.09.02 | Marcas, Gerentes, PrestacoesTítulos, HistoricosPedidosCortes | Removida obrigatoriedade dos Endpoints                  |
| 2019.09.02 | Filiais                      | Removida obrigatoriedade do campo CODCLI                                  |
| 2019.08.30 | Diversos                     | Alteração realizada em Restrição de Venda, Visitas, DescontoCapa          |
| 2019.08.28 | ComissoesRegioes             | Incluído legenda com tipos de desconto e tipo de vendedor                 |
| 2019.08.28 | DescontosItens               | Incluído legenda de tipo de desconto                                      |
| 2019.08.28 | Produtos                     | Removida obrigatoriedade dos campos CODCATEGORIA, CODMARCA, CODSUBCATEGORIA |
| 2019.08.28 | ProdutosAgregados            | Incluído EndPoint Produtos Agregados                                      |
| 2019.08.23 | PlanosPagamentos             | Incluído o campo TIPOVENDA (VP/VV)                                        |
| 2019.08.19 | Produtos                     | Incluído a opção de restrição de transporte                               |
| 2019.08.19 | PrestacoesTítulos, HistoricoPedidosCapas | Acionado os campos PERCOM e COMISSAO                           |
| 2019.08.19 | Cotacao e ItensCotacao       | Adicionado os dois EndPoints                                              |
| 2019.08.15 | Endpoint MaxMotorista        | Ajuste de campos MaxMotorista                                             |
| 2019.08.08 | DescontoCategoria            | Ajuste no nome do Endpoint, de DescontoCampanhaSQP para DescontoCategoria |
| 2019.08.05 | DescontosCapa                | Detalhamento dos tipos de campanha                                        |
| 2019.08.01 | ProdutosSimilares            | Inclusão                                                                  |
| 2019.07.30 | PrestacaoContasCapas, PrestacaoContasItens | Alteração/Inclusão de campos na estrutura de Prestação de Contas |
| 2019.07.26 | Metas                        | Alteração na estrutura de metas                                           |
| 2019.07.22 | Tributos                     | Adicionado colunas FORMULAPVENDA e UTILIZAMOTORCALCULO                    |
| 2019.07.16 | Cfos                         | Criação do EndPoint/Tabela para CFOP                                      |
| 2019.07.16 | ContasBancarias              | Adicionado novo campo ‘TIPO’                                              |
| 2019.07.16 | PrecosPromocoes              | Criação do EndPoint/Tabela para políticas de preço fixo                   |
| 2019.07.15 | Concorrentes                 | Criação do EndPoint/Tabela para concorrentes                              |
| 2019.07.15 | ClientesRegioes              | Criação do EndPoint/Tabela para Clientes x Regiões                        |
| 2019.07.15 | TipoOperacao                 | Criação do EndPoint/Tabela para Tipo de Operação                          |
| 2019.07.15 | PlanosPagamentosRegioes      | Criação do EndPoint/Tabela para vínculo entre plano de pagamento e regiões |
| 2019.07.15 | Geral                        | Ordenação alfabética dos itens do sumário                                 |
| 2019.07.08 | PlanosPagamentosProdutos     | Criação do EndPoint/Tabela para vínculo entre plano de pagamento e produto |
| 2019.07.03 | RotaCliente                  | Inclusão da tabela ERP_MXSROTACLI                                         |
| 2019.06.26 | MarcacoesPonto               | Adicionada a tabela de marcações do controle de jornada                   |
| 2019.06.25 | 9.X Visão geral, 10.X Visão geral | Adicionado Itens 9 e 10 referentes aos endpoints de logística         |
| 2019.06.25 | ClientesPorVendedores        | Adicionado novo endpoint                                                  |
| 2019.06.18 | HistoricosPedidosCapas       | Corrigido tamanho do campo NUMPED (22 para 10)                            |
| 2019.06.18 | HistoricosPedidosCapas       | Corrigido tamanho do campo NUMPEDRCA (22 para 10)                         |
| 2019.06.18 | HistoricosPedidosCortes      | Corrigido tamanho do campo NUMPED (22 para 10)                            |
| 2019.06.18 | HistoricosPedidosFaltas      | Corrigido tamanho do campo NUMPED (22 para 10)                            |
| 2019.06.18 | Usuaris                      | Corrigido tamanho dos campos PROXNUMPED, PROXNUMPEDFORCA, PROXNUMPEDWEB (22 para 10) |
| 2019.06.18 | Usuaris                      | Tirado a obrigatoriedade de PROXNUMNOTACONTIGENCIA e SERIECONTIGENCIA    |
| 2019.05.30 | Clientes/UltimaCompra        | Nomenclatura do Endpoint mudou                                            |
| 2019.05.30 | Banco                        | Nomenclatura do Endpoint mudou                                            |
| 2019.05.30 | 8.X Visão geral              | Inclusão das estruturas de saída para integrar Pronta Entrega            |
| 2019.05.30 | 7.X Visão geral              | Inclusão das estruturas de entrada para integrar Pronta Entrega          |
| 2019.05.30 | 6.X Visão geral              | Inclusão das estruturas de retornos de Pedidos e Clientes                |