# Campanha Progressiva no maxPedido

## Regra da campanha progressiva

### Visão geral

A **Campanha Progressiva de Desconto** é uma funcionalidade do produto **maxPedido** que permite aplicar descontos progressivos conforme critérios comerciais relacionados a **famílias de produtos** sejam atendidos no pedido ou durante o período de vigência da campanha.

O desconto progressivo evolui por **faixas percentuais**. Quanto maior for a quantidade de famílias de produtos contempladas na venda, maior poderá ser o percentual de desconto concedido.

A campanha passa a ficar ativa a partir do momento em que os critérios definidos para a venda por famílias são atendidos. Quando isso ocorre, inicia-se a progressão dos descontos por faixas.

### Pré-requisito obrigatório

Para utilizar Campanha Progressiva, é obrigatório que o parâmetro abaixo esteja habilitado na Central de Configurações do maxPedido:

- `USAR_CAMPANHA_DESCONTO_PROGRESSIVO`

#### Caminho para verificar o parâmetro

1. Acessar a **Central de Configurações do maxPedido**.
2. Clicar no **Menu lateral**.
3. Acessar **Configurações**.
4. Acessar **Parâmetros**.
5. Verificar se o parâmetro `USAR_CAMPANHA_DESCONTO_PROGRESSIVO` está habilitado.

### Família de produtos

As **famílias de produtos** são grupos previamente cadastrados no sistema. Elas são utilizadas como alvo dos critérios que ativam as faixas de desconto da campanha progressiva.

Cada família pode conter produtos específicos. A campanha avalia se os produtos vendidos pertencem às famílias configuradas para decidir se o desconto progressivo será ativado.

### Cadastro de famílias de produtos

#### Caminho de navegação

1. Acessar a **Central de Configurações do maxPedido**.
2. No menu lateral, acessar **Inteligência de Negócio**.
3. Clicar em **Família de Produto**.
4. Clicar no ícone de adição localizado no canto inferior direito da tela.

#### Tela: Família de Produto

Na tela de **Família de Produto**, são exibidas famílias já cadastradas em uma listagem. A tela possui opções de edição e exclusão para os registros existentes.

#### Aba Cadastro

Na aba **Cadastro**, o campo obrigatório é:

- **Descrição**: identifica a família de produto.

Os demais campos exibidos na tela são opcionais.

#### Opção Importar

Na tela de cadastro das famílias existe a opção **Importar**, utilizada como facilitador para importar produtos por meio de arquivo.

Essa opção permite cadastrar itens de forma mais rápida, sem necessidade de inserir todos manualmente.

### Item acelerador na família de produtos

Na aba **Item acelerador**, é possível cadastrar um ou mais itens aceleradores para a família.

#### Passo a passo para cadastrar item acelerador

1. Acessar a tela de **Família de Produto**.
2. Abrir a família desejada ou iniciar um novo cadastro.
3. Acessar a aba **Item acelerador**.
4. Preencher as informações necessárias do item acelerador.
5. Clicar em **Adicionar**.
6. Após finalizar o cadastro dos itens, clicar em **Salvar**.

### Regra do item acelerador

O desconto do item acelerador é acrescido ao desconto da família.

#### Exemplo

Se uma campanha concede **2% de desconto** para determinada família e o vendedor inclui no pedido um item configurado como acelerador com **5% de desconto**, o desconto final será a soma dos percentuais:

- Desconto da família: **2%**
- Desconto do item acelerador: **5%**
- Desconto resultante: **7%**

Representação:

```
2% + 5% = 7%
```

### Cadastro da campanha progressiva

#### Caminho de navegação

1. Acessar a **Central de Configurações do maxPedido**.
2. No menu lateral, acessar **Inteligência de Negócio**.
3. Clicar em **Campanhas Progressivas**.
4. Clicar no ícone de adição localizado no canto inferior direito da tela.

### Tela: Campanha Progressiva

A tela de **Campanha Progressiva** exibe uma listagem das campanhas cadastradas.

Na listagem são exibidas informações como:

* código da campanha;
* descrição;
* data inicial;
* data final;
* opções de edição;
* opções de exclusão.

### Aba Geral da campanha progressiva

A aba **Geral** contém os principais campos de configuração da campanha.

#### Campos da aba Geral

##### Descrição

Campo utilizado para identificar a campanha.

Deve ser preenchido com um texto breve e objetivo.

##### Data Inicial

Define a data de início da vigência da campanha.

##### Data Final

Define a data final da vigência da campanha.

##### Tipo de Campanha

Define como os critérios da campanha serão avaliados.

Tipos disponíveis:

1. **Pedido**

   * Os critérios da campanha devem ser atendidos no pedido atual.
   * O desconto será concedido se o pedido em andamento cumprir a regra configurada.

2. **Acumulativa**

   * Os critérios podem ser atendidos ao longo de todo o período de vigência da campanha.
   * A faixa de desconto será concedida quando o cliente atingir os critérios dentro do período configurado.

##### Filial

Define qual filial participará da campanha.

##### Quantidade Família

Define a quantidade de famílias cadastradas na campanha.

##### Máximo em relação ao pedido

Define o valor máximo de desconto que pode ser acumulado em relação ao pedido.

##### Metodologia

Campo textual utilizado para descrever a mecânica da campanha com mais detalhes.

Exemplo de metodologia:

```
Compre 1 produto de cada família e ganhe 3% de desconto.
```

##### Valor mínimo de venda para ativação

Define um valor mínimo em reais que deve ser atingido para ativar a campanha.

##### Valor máximo de desconto para ativação

Define um valor máximo de desconto para ativação da campanha.

##### Somar descontos

Quando habilitado, permite que descontos sejam somados quando um produto estiver presente em mais de uma família e for positivado em múltiplas campanhas.

Regra explícita:

* Se um produto contido em mais de uma família for positivado em múltiplas campanhas, o desconto aplicado ao produto será a soma de todos os descontos contemplados nas campanhas.

### Seção: Famílias de produtos

Após os campos principais da aba Geral, existe a seção **Famílias de produtos**.

Essa seção define quais famílias farão parte da campanha e quais critérios cada família deve cumprir.

#### Campos da seção Famílias de produtos

##### Família de Produtos

Seleciona uma família de produto previamente cadastrada para inclusão na campanha.

##### Quantidade mínima

Define a quantidade mínima de produtos que devem ser vendidos da família selecionada.

##### Valor mínimo

Define o valor mínimo em reais que deve ser atingido para a família selecionada.

##### Obrigatória

Quando marcada, torna obrigatória a inclusão da família na negociação no aplicativo maxPedido.

##### Adicionar

Inclui a família selecionada na campanha.

Após a família ser adicionada, ela aparece listada abaixo com um resumo das configurações realizadas.

### Seção: Faixas progressivas

A seção **Faixas progressivas** é utilizada para cadastrar as faixas de desconto da campanha.

#### Campos da seção Faixas progressivas

##### Quantidade de famílias

Define a quantidade de famílias que devem ser vendidas para ativar a faixa de desconto.

##### % de desconto

Define o percentual de desconto aplicado à faixa cadastrada.

##### Adicionar

Adiciona a faixa de desconto à campanha.

Após a faixa ser adicionada, ela fica disponível em uma lista abaixo para visualização.

### Restrições da campanha

A aba **Restrições** é utilizada para definir restrições ou exclusividade da campanha.

As restrições são subdivididas em cinco itens.

#### Clientes

Os clientes adicionados nessa aba estarão restritos ou terão exclusividade para a campanha cadastrada.

#### Supervisores

Os supervisores adicionados nessa aba estarão restritos ou terão exclusividade para a campanha cadastrada.

#### Vendedores

Os vendedores adicionados nessa aba estarão restritos ou terão exclusividade para a campanha cadastrada.

#### Regiões

As regiões adicionadas nessa aba estarão restritas ou terão exclusividade para a campanha cadastrada.

#### Faixas

As faixas adicionadas nessa aba estarão restritas ou terão exclusividade para a campanha cadastrada.

### Resultado esperado das restrições

Abaixo de cada aba de restrição serão listados os registros configurados, conforme o tipo de restrição selecionado.

Exemplos de registros listados:

* clientes;
* supervisores;
* vendedores;
* regiões;
* faixas.

Esses registros indicam quais entidades estão restritas ou possuem exclusividade na campanha.


## Cadastro de múltiplas campanhas progressivas no portal

### Visão geral

Esta seção explica como cadastrar uma ou mais campanhas progressivas no mesmo período, com a mesma família e com exclusividade.

O objetivo é permitir o uso de **desconto progressivo com múltiplas campanhas**.

### Objetivo

Cadastrar uma ou mais campanhas no mesmo período utilizando:

* mesma família;
* exclusividade;
* soma de descontos;
* múltiplas campanhas progressivas.

Essa configuração permite que o desconto progressivo seja aplicado considerando mais de uma campanha no mesmo intervalo de vigência.

### Cadastro de mais de uma campanha progressiva no mesmo período

#### Caminho de navegação no maxPedido Web

1. Acessar o **maxPedido Web**.
2. No menu lateral, clicar em **Inteligência de Negócio**.
3. Clicar em **Campanha Progressiva**.
4. Clicar no ícone de adição para iniciar o cadastro de uma nova campanha.

### Opção Somar Descontos

Durante o cadastro de uma nova campanha, existe a opção **Somar Descontos**.

Ao marcar essa opção, o sistema apresenta uma caixa de diálogo informativa.

#### Mensagem exibida ao marcar Somar Descontos

```text
Ao habilitar a soma dos descontos se um produto contido em mais de uma família seja positivado em múltiplas campanhas, o desconto do produto será a soma de todos os descontos contemplados nas campanhas.
```

#### Ação esperada

1. Marcar a opção **Somar Descontos**.
2. Ler a mensagem informativa apresentada.
3. Confirmar a ciência da regra na caixa de diálogo.
4. Clicar em **Salvar** para validar as informações cadastradas.

### Regra operacional da opção Somar Descontos

Quando a opção **Somar Descontos** está habilitada:

* o sistema soma os descontos das campanhas contempladas;
* o produto pode participar de mais de uma família;
* se o produto for positivado em múltiplas campanhas, o desconto final será a soma dos descontos das campanhas;
* a soma é considerada no acompanhamento da campanha progressiva no aplicativo.

### Atenção sobre produto em múltiplas famílias

O sistema **não impede** a inclusão de um produto em duas ou mais famílias.

Quando o usuário tenta inserir um produto que já existe em uma família, o sistema apresenta uma mensagem informando que o produto já está em uma ou mais famílias.

A mensagem também indica em qual ou quais famílias o produto foi inserido.

Se o usuário desejar prosseguir mesmo assim, deve clicar em **Sim**.

### Apresentação no aplicativo

#### Tela: Pedido

Ao iniciar um novo pedido, o vendedor deve acessar a aba **Tabela**.

Na listagem de produtos, é possível visualizar a legenda da campanha à qual o item pertence.

#### Comportamento da legenda da campanha

1. O produto participante de campanha exibe uma legenda ou identificação visual.
2. Ao clicar sobre a legenda, o aplicativo abre uma janela.
3. A janela informa a descrição da campanha e a família à qual o produto pertence.

#### Exemplo de informação exibida no aplicativo

Na tela do aplicativo, ao tocar na indicação da campanha, aparece uma janela com informação semelhante a:

```text
Produto presente na(s):
Campanha: [código]
[descrição da família/campanha]
```

### Tela: Acompanhamento de campanha progressiva

Quando a opção **Somar Descontos** estiver selecionada na Central de Configurações, a tela de acompanhamento da campanha progressiva exibe as campanhas por cards.

Cada card apresenta informações da campanha e do desconto.

#### Informações exibidas na tela

A tela de acompanhamento pode exibir:

* valor do pedido;
* valor original do pedido;
* valor do desconto;
* percentual do desconto;
* cards de campanhas progressivas;
* valor mínimo da campanha;
* valor atendido;
* valor faltante;
* desconto máximo;
* valor usado;
* valor restante;
* famílias acumuladas;
* famílias no pedido;
* total de famílias;
* percentual da faixa;
* valor de desconto.

#### Observação sobre itens considerados

O valor do pedido exibido no acompanhamento leva em consideração somente os itens inclusos em campanha.

### Regra para itens repetidos em mais de uma campanha

É necessário verificar se existe item presente em mais de uma campanha, pois isso impacta o valor total do desconto.

Quando um item se repete em determinada campanha, é apresentado um símbolo à frente do nome da campanha.

#### Símbolo apresentado

O sistema mostra o símbolo:

```text
**
```

Esse símbolo aparece à frente do nome da campanha quando existe item repetido.

### Exemplo de soma de descontos entre campanhas

Cenário de soma de descontos:

* Existe um item que se repete em duas campanhas.
* Em uma campanha, o item recebeu **8% de desconto**.
* Em outra campanha, o item recebeu **3% de desconto**.
* O desconto total do item passa a ser **11%**.

Representação:

```text
8% + 3% = 11%
```

No exemplo:

* a primeira campanha possui um item com **8% de desconto**;
* existe também um item que se repete em ambas as campanhas;
* o item repetido soma os descontos e totaliza **11%**.

### Exemplo da tela de acompanhamento

A tela de acompanhamento mostra:

```text
Valor do Pedido
R$ 181.0
R$ 200.0
R$ 19.0 (-9.5%)
```

Também são exibidos cards de campanhas.

#### Card de campanha com símbolo de repetição

Exemplo de card:

```text
177 - Campanha Sprint 29 - D **
```

O símbolo `**` indica existência de item repetido.

#### Informações do card da campanha

O card exibe campos como:

* Valor Mínimo;
* Atendido;
* Falta;
* Desconto Máximo;
* Usado;
* Resta;
* Fam. acumuladas;
* neste Pedido;
* Total;
* %Faixa;
* Valor do Desconto.

#### Valores do exemplo

Exemplo de valores exibidos:

```text
Valor do Pedido: R$ 181.0
Valor original: R$ 200.0
Desconto: R$ 19.0 (-9.5%)
```

Em um dos cards:

```text
Valor Mínimo: R$ 100.0
Atendido: R$ 200.0
Falta: R$ 0.0
%Faixa: 8.0%
Valor do Desconto: R$ 19.0
```

Em outro card:

```text
177 - Campanha Sprint 29 - D **
Valor Mínimo: R$ 1.0
Atendido: R$ 100.0
Falta: R$ 0.0
Desconto Máximo: R$ 200.0
Usado: R$ 11.0
Resta: R$ 189.0
Fam. acumuladas: 0
neste Pedido: 1
Total: 1
%Faixa: 3.0%
Valor do Desconto: R$ 11.0
```

---

## Operação e acompanhamento no aplicativo maxPedido

### Visão geral

Esta seção mostra como o desconto progressivo é apresentado e acompanhado no aplicativo maxPedido.

O foco está na operação pelo vendedor durante a confecção do pedido, incluindo:

* visualização de produtos participantes da campanha;
* filtros de produtos em campanha;
* acompanhamento do progresso da campanha;
* visualização de famílias atendidas e não atendidas;
* itens aceleradores;
* famílias obrigatórias;
* logs do desconto aplicado;
* confirmação de aplicação do desconto ao salvar o pedido.

### Visualizando produtos da campanha no aplicativo

#### Tela: Pedido

Durante a confecção do pedido, o vendedor pode identificar os produtos participantes de uma campanha progressiva na aba **Tabela**.

#### Aba Tabela

Na listagem da aba **Tabela**, os produtos em campanha são identificados por ícone visual.

A tela exibe informações como:

* código do produto;
* nome do produto;
* embalagem;
* unidade;
* preço;
* estoque;
* ícones de identificação;
* nome da campanha;
* nome da família.

#### Exemplo de produto em campanha

Na tela do aplicativo aparece o produto:

```text
1372 - AÇUCAR COLORIDO BRANCO 500 GR
```

O produto apresenta indicação de campanha e família:

```text
Camp. 14 - Fam. 14-FAMÍLIA 1
```

Outro produto exibido:

```text
6552 - AÇUCAR CONFEITEI EASY PURATOS 2 KG
```

Na parte inferior da tela aparecem informações de resumo do pedido, como:

```text
Total do pedido
Saldo CC RCA
Quant. de itens
```

### Filtrar produtos participantes da campanha progressiva

Na barra superior da tela existe um ícone de filtro.

Ao clicar nesse ícone, é possível filtrar os produtos que estão participando da campanha progressiva.

#### Passo a passo para filtrar produtos em campanha

1. Abrir um pedido no aplicativo maxPedido.
2. Acessar a aba **Tabela**.
3. Clicar no ícone de filtro na barra superior.
4. Selecionar o filtro relacionado à campanha progressiva.
5. Confirmar a aplicação do filtro.

### Filtro avançado por família

Na tela de filtros existe a opção **Filtro Avançado**.

Dentro do Filtro Avançado, é possível selecionar produtos por **Família**.

#### Campos do Filtro Avançado

A aba **Seleção Avançada** apresenta os seguintes campos:

* Fornecedores;
* Departamentos;
* Seções;
* Famílias;
* Categoria;
* Subcategoria;
* Marca.

Ao lado de alguns campos aparece a ação **Limpar**.

Na parte inferior da tela existem os botões:

* **Cancelar**;
* **OK**.

#### Passo a passo para filtrar por família

1. Abrir o filtro de produtos.
2. Acessar **Filtro Avançado** ou **Seleção Avançada**.
3. Localizar o campo **Famílias**.
4. Selecionar a família desejada.
5. Clicar em **OK** para aplicar o filtro.

### Acompanhar campanha progressiva

O vendedor pode acompanhar o progresso da campanha após adicionar produtos ao pedido.

#### Caminho no aplicativo

1. Na tela do pedido, clicar no menu de opções.
2. Selecionar a opção **Acompanhar campanha progressiva**.

#### Tela: Acompanhamento de desconto progressivo

A tela de acompanhamento exibe a mecânica da campanha e o progresso atingido pelo pedido.

Informações apresentadas:

* valor do pedido;
* campanha progressiva;
* valor mínimo;
* valor atendido;
* valor faltante;
* desconto máximo;
* valor usado;
* valor restante;
* famílias acumuladas;
* famílias no pedido;
* total de famílias;
* percentual da faixa;
* valor do desconto.

### Visualização das famílias da campanha

Na tela de acompanhamento, ao clicar em qualquer parte das informações da campanha, o vendedor é direcionado para a visualização das famílias da campanha.

#### Status visual das famílias

As famílias são exibidas com cores diferentes:

* **verde**: famílias já positivadas;
* **branco**: famílias ainda não positivadas.

Essa visualização ajuda o vendedor a identificar quais famílias já foram contempladas no pedido e quais ainda faltam para ativar ou melhorar a faixa de desconto.

### Item acelerador na campanha progressiva

A tela de acompanhamento também permite visualizar se a campanha possui itens aceleradores.

#### Informações exibidas

A tela apresenta:

* existência de item acelerador;
* quantidade de itens aceleradores;
* indicação ao lado do nome da família;
* ícone com contagem no formato semelhante a `(0/1)`.

O ícone ou contador aparece à frente do nome da família.

### Filtros no menu lateral da tela de acompanhamento

No menu lateral da tela de acompanhamento, o vendedor pode filtrar as famílias por diferentes situações.

#### Opções de filtro apresentadas

* Atendidas;
* Inseridas;
* Não inseridas;
* Famílias com itens aceleradores;
* Famílias obrigatórias;
* Todas.

### Família obrigatória na campanha progressiva

Se a campanha possuir alguma família cadastrada como obrigatória e ela ainda não tiver sido inserida no pedido, essa informação será apresentada na tela de acompanhamento.

#### Identificação visual

Na listagem, as famílias obrigatórias aparecem com o **nome em azul** para facilitar a identificação.

### Regra do item acelerador no aplicativo

Quando uma família possui item acelerador, o desconto configurado para esse item na Central de Configurações é acrescido ao desconto da família.

#### Exemplo

Se uma família concede **2% de desconto** e o vendedor vende um item acelerador com **5% de desconto**, os descontos são somados.

Resultado:

```text
2% + 5% = 7%
```

### Logs do desconto aplicado

Na tela de acompanhamento existe um ícone no canto direito que permite acessar os **logs do desconto aplicado**.

#### Ação disponível

1. Acessar a tela **Acompanhamento de desconto progressivo**.
2. Clicar no ícone localizado no canto direito da tela.
3. Visualizar os logs relacionados ao desconto aplicado.

### Confirmação ao salvar o pedido

Ao salvar o pedido, o aplicativo apresenta uma tela de confirmação do desconto progressivo.

Após a confirmação, os descontos são aplicados em cada item do pedido.

#### Mensagem de confirmação exibida

A caixa de diálogo exibe o título:

```text
Confirmação
```

Mensagem exibida:

```text
Existem itens no pedido que compõem a mecânica de Campanha Progressiva com novos descontos referentes as famílias vendidas. Deseja aplicar estes descontos automaticamente ao pedido Camp. 14 - OK
```

Botões disponíveis:

* **NÃO**
* **SIM**

#### Resultado esperado

* Ao confirmar em **SIM**, o sistema aplica automaticamente os descontos progressivos aos itens do pedido.
* Ao selecionar **NÃO**, a aplicação automática dos descontos não é confirmada naquele momento.

---

## Observações gerais

### Conceitos centrais

A Campanha Progressiva no maxPedido depende de três componentes principais:

1. **Famílias de produtos**

   * Agrupam produtos que serão avaliados pela regra da campanha.

2. **Faixas progressivas**

   * Definem percentuais de desconto conforme a quantidade de famílias atendidas.

3. **Critérios comerciais**

   * Determinam condições como quantidade mínima, valor mínimo, vigência, filial, obrigatoriedade e restrições.

### Aplicação do desconto

O desconto progressivo pode ser aplicado quando os critérios da campanha forem atendidos no pedido ou durante o período de vigência, conforme o tipo de campanha configurado.

### Tipo Pedido

No tipo **Pedido**, os critérios precisam ser cumpridos no pedido atual.

### Tipo Acumulativa

No tipo **Acumulativa**, os critérios podem ser cumpridos durante todo o período de vigência da campanha.

### Soma de descontos

A opção **Somar Descontos** permite que produtos presentes em mais de uma família ou campanha tenham os descontos somados.

Essa regra é especialmente importante em cenários com múltiplas campanhas vigentes no mesmo período.

### Produto em mais de uma família

O sistema não bloqueia automaticamente a inclusão de um mesmo produto em mais de uma família.

Ao detectar que o produto já existe em uma ou mais famílias, o sistema apresenta uma mensagem informativa. O usuário pode decidir se deseja continuar com a inclusão.

### Item acelerador

O item acelerador aumenta o desconto da família.

O desconto do item acelerador é somado ao desconto já concedido pela família.

### Família obrigatória

Uma família pode ser marcada como obrigatória.

Quando isso ocorre, ela precisa ser considerada na negociação no aplicativo maxPedido.

No acompanhamento, famílias obrigatórias são destacadas com nome em azul.

### Acompanhamento no aplicativo

O vendedor consegue acompanhar o progresso da campanha diretamente no pedido, acessando a opção **Acompanhar campanha progressiva**.

A tela de acompanhamento exibe:

* progresso da campanha;
* valores atendidos;
* valores faltantes;
* descontos aplicados;
* famílias contempladas;
* famílias pendentes;
* itens aceleradores;
* famílias obrigatórias;
* logs do desconto aplicado.

### Confirmação antes da aplicação do desconto

Ao salvar o pedido, o aplicativo solicita confirmação para aplicar automaticamente os novos descontos relacionados à campanha progressiva.

---

## Glossário de termos e campos

### Campanha Progressiva

Regra comercial que concede descontos por faixas conforme critérios de venda são atendidos.

### Desconto progressivo

Desconto que aumenta conforme o pedido atende mais critérios, especialmente a quantidade de famílias de produtos configuradas.

### Família de produtos

Grupo de produtos previamente cadastrado e utilizado como critério para ativar descontos progressivos.

### Item acelerador

Produto configurado para adicionar um desconto extra ao desconto da família.

### Família obrigatória

Família marcada como obrigatória na campanha. Deve ser considerada na negociação no aplicativo.

### Faixa progressiva

Configuração que define o percentual de desconto conforme a quantidade de famílias atendidas.

### Quantidade de famílias

Número de famílias que devem ser vendidas para ativar determinada faixa de desconto.

### Percentual de desconto

Valor percentual aplicado como desconto na faixa progressiva.

### Tipo de campanha: Pedido

Tipo de campanha em que os critérios devem ser atendidos no pedido atual.

### Tipo de campanha: Acumulativa

Tipo de campanha em que os critérios podem ser atendidos durante o período de vigência.

### Somar descontos

Configuração que permite somar descontos de múltiplas campanhas quando um produto estiver presente em mais de uma família ou campanha.

### Valor mínimo de venda para ativação

Valor mínimo em reais necessário para ativar a campanha.

### Valor máximo de desconto para ativação

Valor máximo de desconto definido para ativação da campanha.

### Máximo em relação ao pedido

Limite máximo de desconto que pode ser acumulado em relação ao pedido.

### Metodologia

Descrição textual da mecânica da campanha.

### Restrições

Configurações que definem clientes, supervisores, vendedores, regiões ou faixas restritas ou exclusivas para a campanha.

### Clientes

Entidades que podem ser restringidas ou configuradas com exclusividade para a campanha.

### Supervisores

Supervisores que podem ser restringidos ou configurados com exclusividade para a campanha.

### Vendedores

Vendedores que podem ser restringidos ou configurados com exclusividade para a campanha.

### Regiões

Regiões que podem ser restringidas ou configuradas com exclusividade para a campanha.

### Faixas

Faixas que podem ser restringidas ou configuradas com exclusividade para a campanha.

### Acompanhar campanha progressiva

Opção do aplicativo maxPedido que permite visualizar o andamento da campanha dentro do pedido.

### Logs do desconto aplicado

Registro visual acessado pela tela de acompanhamento, utilizado para consultar informações do desconto aplicado.

### Positivada

Situação em que uma família foi contemplada no pedido ou atingiu os critérios necessários.

### Atendida

Família ou condição que já teve os critérios cumpridos.

### Não inserida

Família que ainda não foi incluída no pedido.

### Inserida

Família que foi incluída no pedido.

### Valor atendido

Valor já alcançado em relação ao critério da campanha.

### Valor faltante

Valor que ainda falta para atingir o critério definido.

### Valor usado

Valor de desconto já utilizado.

### Valor restante

Saldo restante em relação ao limite de desconto.

### Desconto máximo

Limite máximo de desconto permitido na campanha.

### Valor do desconto

Valor monetário do desconto aplicado.

### Símbolo `**`

Indicação visual apresentada no aplicativo quando existe item repetido em determinada campanha.
