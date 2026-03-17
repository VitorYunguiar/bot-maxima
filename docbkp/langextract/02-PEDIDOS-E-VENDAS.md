# Pedidos e Vendas — Base de Conhecimento maxPedido/Winthor

**Palavras-chave:** pedidos, vendas, pre-pedido, orcamento, bloqueio cliente, quantidade maxima itens, compartilhar pedido, agrupamento fornecedor, desmembramento pedido, filial retira, status pedido, timeline, geracao arquivo PDF XLS, erro arquivo pedido, cliente bloqueado, SEFAZ, bloqueio definitivo

**Sistema:** maxPedido, Winthor, Outros ERPs

**Area:** Vendas, Comercial, Configuracao

---

## Pre-Pedido no maxPedido

### Visao Geral

A funcionalidade de Pre-Pedido permite criar um pedido previamente configurado, contendo informacoes como regiao, filial, itens e outras definicoes estrategicas. Esse pedido pode ser configurado como obrigatorio ou apenas como sugestao, orientando o vendedor no momento da venda e garantindo maior alinhamento com as estrategias comerciais.

### Beneficios do Pre-Pedido

- Direciona o vendedor com um modelo de pedido pronto, reduzindo erros e retrabalho
- Garante maior padronizacao nas vendas
- Agiliza o processo de montagem do pedido
- Apoia o cumprimento de campanhas, acordos comerciais e metas definidas

### Requisitos para Configuracao

E necessario ter o Login e Senha do maxSolucoes em maos para fazer as configuracoes. Em casos em que ha dois ambientes "Homologacao" e "Producao", deve-se escolher o ambiente desejado antes de prosseguir. Na maioria dos casos o correto e escolher o ambiente de "Producao", o ambiente de "Homologacao" e escolhido apenas em casos em que este ambiente esta validado para testes.

### Passo 1: Acessar o Portal maxSolucoes

1. Acessar o portal atraves do link: https://appsv.solucoesmaxima.com.br
2. Digitar o usuario e senha de acesso
3. Clicar na opcao maxVendas
4. Na tela seguinte clicar em maxPedido

### Passo 2: Habilitar Parametro UTILIZA_PRE_PEDIDO

1. No menu lateral (canto superior esquerdo), clicar em Configuracoes >> Parametros
2. Realizar busca atraves do Filtro pelo parametro UTILIZA_PRE_PEDIDO pelo nome
3. Tambem e possivel filtrar pelo tipo: Geral, por Usuario ou por Filial
4. Clicar no icone de edicao na coluna de Acoes
5. Arrastar para habilitar ou desabilitar o parametro
6. Clicar em Salvar

**Detalhes Importantes do Parametro:**

| Parametro | Tipo de Dado | Configuracao |
|-----------|--------------|--------------|
| UTILIZA_PRE_PEDIDO | Logico | Habilitar para usar pre-pedido |
| | | Atente-se ao tipo (por Filial se necessario) |

Caso necessario criar um parametro novo, consultar documentacao especifica sobre criacao de parametros no maxPedido.

### Passo 3: Cadastrar Pre-Pedido

1. No menu, clicar em Inteligencia de Negocio >> Recomendacao de produto >> Pre-Pedido
2. Para adicionar, clicar no icone de adicao (+) no canto inferior direito da tela
3. Preencher os dados nas tres abas: Dados do Pre-pedido, Clientes e Itens do pre-pedido
4. Apos concluido, clicar em Salvar Pre-Pedido

#### Aba 1: Dados do Pre-pedido

Nessa aba preencher as seguintes informacoes:

| Campo | Descricao |
|-------|-----------|
| Codigo | Codigo identificador do pre-pedido |
| Descricao | Descricao do pre-pedido |
| Data Inicial | Data de inicio da validade do pre-pedido |
| Data Final | Data de fim da validade do pre-pedido |
| Cor | Cor que representara os produtos do pre-pedido |
| Supervisor | Supervisor que tera acesso a esse pre-pedido |
| Filial | Filial a qual valerá esse pre-pedido |
| Ramo de Atividade | Ramo a qual esse pre-pedido sera utilizado |
| Regiao | Regiao a qual esse pre-pedido sera utilizado |
| Aplicar cor e ordenar produto | Quando marcada aplica a cor selecionada nos produtos e os ordena |
| Apresentar pop-up e ordenar produtos por cor | Quando marcada apresenta pop-up e ordena produtos pela cor |

**Observacao Importante sobre Ramo de Atividade:**

Quando se utiliza o cadastro do ramo de atividade do fornecedor, os ramos de atividade serao apresentados agrupados pelo ramo de atividade do fornecedor vinculado. Esse agrupamento pode ser realizado pela rotina 2571 do ERP Winthor ou pelo cadastro feito no modulo de Inteligencia de Negocios da Central de Configuracoes, para clientes que utilizam outros ERPs. Essa opcao funcionara como um agrupamento visual, a validacao no aplicativo continuara sendo feita pelo ramo de atividade do cliente.

#### Aba 2: Clientes

Nessa aba selecionar os clientes e adiciona-los ou importar os mesmos clicando na opcao de importacao. Os clientes selecionados nesta aba terao acesso ao pre-pedido cadastrado.

#### Aba 3: Itens do Pre-pedido

Nessa aba preencher as informacoes abaixo e posteriormente clicar em Adicionar ou Importar os itens:

| Campo | Descricao |
|-------|-----------|
| Departamento | Departamento a qual o item faz parte |
| Secao | Secao a qual o item faz parte |
| Categoria | Categoria a qual o item faz parte |
| Sub-categoria | Sub-categoria a qual o item faz parte |
| Produtos | O item desejado para o pre-pedido |
| Quantidade | Quantidade desse item que entrara no pre-pedido |

### Visualizacao no Aplicativo

#### Com Pop-up Habilitado

Quando a opcao "Apresentar pop-up e ordenar produtos por cor" estiver habilitada em conjunto com o parametro ORDENA_COR_PREPEDIDO habilitado, ao iniciar um pedido com o cliente que tem o pre-pedido configurado sera exibida uma tela de pop-up informando sobre o pre-pedido.

#### Na Listagem de Produtos

Na listagem de produtos da aba Tabela serao exibidos os itens de pre-pedido ordenados pela cor cadastrada. Por exemplo, se o pre-pedido foi cadastrado com a cor azul, os itens do pre-pedido aparecerao destacados nessa cor, facilitando a identificacao visual pelo vendedor.

---

## Quantidade Maxima de Itens no Pedido

### Visao Geral

E possivel definir uma quantidade maxima de itens permitidos em um pedido no maxPedido. Ao tentar inserir uma quantidade superior a cadastrada, o vendedor sera informado na tela de negociacao que a quantidade de produtos no pedido e o maximo permitido.

### Parametros Necessarios

**Atencao:** Os parametros mencionados sao complementares e precisam estar ambos configurados.

| Parametro | Funcao | Tipo |
|-----------|--------|------|
| VERIFICAR_QTD_MAX_ITENS_PEDIDO | Valida a funcionalidade de quantidade maxima | Logico (habilitar) |
| VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO | Define o numero maximo de itens permitidos | Numerico |

### Passo a Passo da Configuracao

1. Acessar a Central de Configuracoes do maxPedido
2. No menu lateral clicar em Configuracoes > Parametros
3. Buscar pelos parametros VERIFICAR_QTD_MAX_ITENS_PEDIDO e VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO
4. Clicar em Pesquisar (nao e possivel pesquisar dois parametros ao mesmo tempo em filtro)
5. Clicar no icone de edicao na coluna Acoes a frente de cada parametro
6. No parametro VERIFICAR_QTD_MAX_ITENS_PEDIDO marcar a opcao para habilitar e clicar em Salvar
7. No parametro VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO informar a quantidade maxima de itens que poderao conter o pedido e clicar em Salvar

### Comportamento no Aplicativo

No aplicativo, ao tentar inserir uma quantidade de itens superior a cadastrada, o vendedor sera informado na tela de negociacao que a quantidade de produtos no pedido e o maximo permitido, impedindo a adicao de mais itens.

---

## Compartilhar Pedidos e Orcamentos

### Visao Geral

No maxPedido e possivel compartilhar um pedido ou um orcamento atraves de um arquivo PDF ou XLS (Excel). Esta funcionalidade permite que o vendedor envie o pedido ou orcamento para o cliente ou outras partes interessadas de forma rapida e pratica.

### Passo a Passo para Compartilhar

#### Passo 1: Acessar o Menu de Pedidos

Navegar ate o menu Pedidos na tela inicial do aplicativo.

#### Passo 2: Selecionar o Pedido ou Orcamento

Na tela de pedidos, selecionar o pedido ou orcamento que deseja compartilhar dando um clique longo sobre o mesmo.

#### Passo 3: Escolher a Opcao Compartilhar

No pop-up que surgir na tela, escolher a opcao Compartilhar.

#### Passo 4: Escolher o Formato do Arquivo

Na tela seguinte, escolher entre uma das opcoes de arquivo (PDF ou XLS) e logo em seguida clicar em Gerar.

#### Passo 5: Aguardar a Geracao do Arquivo

Um pop-up com barra de progresso indicara que o arquivo esta sendo gerado. Aguardar ate que carregue em 100%.

#### Passo 6: Compartilhar via Aplicativo

Assim que o processo for concluido, aparecerao as opcoes de aplicativos nos quais sera possivel compartilhar o pedido ou orcamento (WhatsApp, Email, etc.).

---

## Agrupamento de Produtos por Fornecedor

### Visao Geral

A funcionalidade de agrupamento de produtos por fornecedor permite visualizar e organizar os produtos do pedido agrupados por seus respectivos fornecedores, facilitando a gestao do mix de produtos e a estrategia de positivacao.

### Parametro Necessario

| Parametro | Valor Padrao | Configuracao |
|-----------|--------------|--------------|
| EXIBIR_AGRUPAMENTO_FORNECEDOR | SIM | Vem por default como SIM, caso nao queira utilizar a funcionalidade basta configurar como NAO |

**Localizacao:** Central de Configuracoes > Configuracoes > Parametros

### Passo a Passo no Aplicativo

1. No aplicativo clicar no Menu Clientes
2. Selecionar o cliente desejado
3. Iniciar um novo Pedido
4. No icone de tres pontos selecionar a opcao "Agrupar produtos por fornecedor"
5. Clicar sobre o Fornecedor para abrir a lista de produtos

### Informacoes Exibidas no Cabecalho do Fornecedor

Ao expandir um fornecedor, sera apresentado um cabecalho com as seguintes informacoes:

| Campo | Descricao |
|-------|-----------|
| Produtos Ideais | Quantidade de produtos ideais do fornecedor (pre-pedido) |
| Positivado | Quantidade de produtos ideais (pre-pedido) do fornecedor que foram positivados |
| Total Produtos | Quantidade total de produtos do fornecedor |
| Positivado | Quantidade total de produtos positivados do fornecedor |

Essa visualizacao permite ao vendedor acompanhar em tempo real o cumprimento das metas de positivacao por fornecedor.

---

## Desmembramento de Pedido por Filial Retira

### Visao Geral

A funcionalidade de desmembramento de pedido por filial retira permite que um pedido seja automaticamente dividido em multiplos pedidos quando forem selecionados produtos de diferentes filiais retira. Isso facilita a logistica e o atendimento do pedido quando os produtos sao retirados de diferentes centros de distribuicao.

### Parametro Necessario

| Parametro | Tipo | Funcao |
|-----------|------|--------|
| DESMEMBRAR_PED_FILIAL_RETIRA | Logico | Habilita o desmembramento automatico por filial retira |

**Localizacao:** Central de Configuracoes > Configuracoes > Parametros

### Passo a Passo da Configuracao

1. Na central de configuracoes do maxPedido, clicar em Configuracoes > Parametros
2. Buscar pelo parametro DESMEMBRAR_PED_FILIAL_RETIRA
3. Clicar no icone de edicao para habilitar
4. Salvar a configuracao

### Passo a Passo no Aplicativo

1. Apos iniciar um pedido, clicar na aba Tabela para selecionar os itens
2. Ao clicar sobre o produto, selecionar a filial retira desejada
3. Repetir o processo para os demais produtos, podendo selecionar filiais retira diferentes
4. Clicar na opcao Salvar e Enviar o Pedido
5. Caso tenha inserido itens de filiais retira diferentes, o aplicativo fara a validacao e desmembrara automaticamente, tornando assim um pedido para cada filial retira selecionada

### Observacoes Importantes

**Atencao:** Todas as validacoes serao realizadas no pedido original, conforme e atualmente, ou seja, nenhuma validacao sera realizada nos pedidos que serao desmembrados. Nesse processo nao sera permitido utilizar nenhum tipo de autorizacao. Quando um pedido for entrar em algum processo de autorizacao, o mesmo nao sera desmembrado.

---

## Status do Pedido e Timeline (Clientes Outros ERPs)

### Problema: Status do Pedido Nao Atualizando no App

Caso a timeline de status do maxPedido nao esteja atualizando, considerando que seja cliente de Outros ERPs (nao Winthor), e necessario verificar a integracao correta das informacoes.

### Causa do Problema

As informacoes sao enviadas para o ambiente nuvem da Maxima atraves de APIs de integracao pelo proprio cliente. Para que a timeline funcione corretamente, a seguinte estrutura de dados deve estar configurada:

### Tabelas e Campos Necessarios

| Tabela | Campo | Descricao |
|--------|-------|-----------|
| MXSINTEGRACAOPEDIDO | DTABERTURAPEDPALM | Data de abertura do pedido enviada pelo maxPedido |
| MXSHISTORICOPEDC | DTABERTURAPEDPALM | Mesma data que deve ser devolvida pelo ERP |

### Como Funciona

1. O maxPedido envia o pedido com a data na coluna DTABERTURAPEDPALM da tabela MXSINTEGRACAOPEDIDO
2. Quando o ERP processa o pedido, ele precisa devolver essa data na tabela MXSHISTORICOPEDC
3. Essa informacao e usada na timeline do maxPedido, atualizando o status corretamente
4. A coluna DTABERTURAPEDPALM sempre deve estar preenchida na tabela MXSHISTORICOPEDC

### Verificacao

Essa informacao pode ser verificada no Layout de Integracao, item 5.48 - Historico Pedidos Capas. Consultar a documentacao completa do Layout de Integracao para detalhes sobre a estrutura de dados e campos obrigatorios.

---

## Correcao de Erro ao Gerar Arquivo do Pedido (PDF/XLS)

### Problema

Quando e necessario gerar PDF ou XLS de um pedido e o arquivo nao esta carregando, pode ser um problema relacionado ao componente WebView do Android.

### Solucao: Atualizar/Reinstalar WebView

#### Passo 1: Acessar Configuracoes de Aplicativos

Na tela de configuracoes do aparelho, clicar no menu Aplicativos.

**Observacao:** Os icones de acesso podem mudar de nomenclatura de acordo com o modelo do aparelho.

#### Passo 2: Desabilitar o Navegador Chrome

1. Clicar no aplicativo Chrome
2. Clicar em Desinstalar para desabilitar o navegador
3. Confirmar a acao

#### Passo 3: Atualizar ou Instalar WebView

1. Acessar a Play Store do aparelho
2. Procurar pelo aplicativo WebView
3. Caso esteja instalado, realizar a atualizacao do mesmo
4. Caso nao encontre o aplicativo WebView, realizar a instalacao

#### Passo 4: Reativar o Chrome

Ao finalizar o processo, ativar novamente o aplicativo Chrome.

### Resumo da Solucao

O problema ocorre quando o componente Android System WebView esta desatualizado ou corrompido. Como o maxPedido utiliza este componente para gerar arquivos PDF e XLS, e necessario garantir que ele esteja atualizado. Desabilitar temporariamente o Chrome permite atualizar ou reinstalar o WebView, resolvendo o problema.

---

## Venda para Cliente Bloqueado

### Visao Geral

O maxPedido permite configurar se sera ou nao permitido realizar vendas para clientes bloqueados. Existem diversos parametros que controlam esse comportamento, incluindo bloqueios temporarios, bloqueios de rede, bloqueios SEFAZ e bloqueios definitivos.

### Configuracao dos Parametros

#### Passo 1: Acessar Central de Configuracoes

1. Acessar a Central de Configuracoes do maxPedido
2. No icone do lado esquerdo da tela, clicar em Configuracoes
3. Clicar em Parametros

#### Passo 2: Pesquisar Parametros

Informar o parametro desejado na tela de Filtros Avancados e clicar em Pesquisar.

### Parametros para PERMITIR Venda para Cliente Bloqueado

Para permitir vendas para clientes bloqueados, os parametros abaixo devem estar configurados da seguinte forma:

| Parametro | Valor | Descricao |
|-----------|-------|-----------|
| ACEITAVENDAAVISTACLIBLOQ | S (Sim) | Aceita venda a vista para cliente bloqueado |
| ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO | S (Sim) | Aceitar digitar pedido quando o cliente rede estiver bloqueado |
| BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ | N (Nao) | Bloqueia a confeccao de pedido para cliente bloqueado |
| BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ | N (Nao) | Bloqueia a confeccao de pedido para cliente rede bloqueado |
| VERIFICABLOQUEIOSEFAZ | N (Nao) | Permite que usuario digite pedido de venda de cliente com restricao no SEFAZ |
| PERMITE_ORCAMENTO_CLIENTE_BLOQ | S (Sim) | Permite que inicie Orcamento para cliente bloqueado |
| BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ_DEFINITIVO | N (Nao) | Permite iniciar pedido para cliente com bloqueio definitivo |

**Para clientes Winthor:** O parametro CON_ACEITAVENDABLOQ (Aceita venda para cliente bloqueado) deve estar cadastrado como S (Sim) no ERP.

### Parametros para NAO PERMITIR Venda para Cliente Bloqueado

Para nao permitir vendas para clientes bloqueados, os parametros abaixo devem estar configurados da seguinte forma:

| Parametro | Valor | Descricao |
|-----------|-------|-----------|
| ACEITAVENDAAVISTACLIBLOQ | N (Nao) | Aceita venda a vista para cliente bloqueado |
| ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO | N (Nao) | Aceitar digitar pedido quando o cliente rede estiver bloqueado |
| BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ | S (Sim) | Bloqueia a confeccao de pedido para cliente bloqueado |
| BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ | S (Sim) | Bloqueia a confeccao de pedido para cliente rede bloqueado |
| VERIFICABLOQUEIOSEFAZ | S (Sim) | Nao permite que usuario digite pedido de venda de cliente com restricao no SEFAZ |
| PERMITE_ORCAMENTO_CLIENTE_BLOQ | N (Nao) | Nao permite que inicie Orcamento para cliente bloqueado |
| BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ_DEFINITIVO | S (Sim) | Impede de iniciar pedido para cliente com bloqueio definitivo |

### Visualizacao no Aplicativo pelo Representante

#### Identificacao de Cliente Bloqueado

Independente de como configurado (permitindo ou nao permitindo a venda para cliente bloqueado), o nome do cliente aparecera na listagem de clientes para o representante, porem acompanhado do icone de um cadeado representando o bloqueio.

#### Comportamento com Bloqueio Configurado

Caso configurado os parametros de Bloqueio (nao permitir venda), sera informado que nao e possivel realizar venda, com opcao para que o representante salve um orcamento.

#### Comportamento com Venda Permitida

Caso configurado os parametros permitindo a venda para cliente bloqueado, o pedido sera iniciado normalmente, mesmo com o cliente bloqueado.

### Cliente com Bloqueio Definitivo

Em caso de cliente com bloqueio definitivo, existe um parametro que pode ser configurado para que, a titulo de informacao, esse cliente seja visualizado ou nao na lista dos clientes do representante.

| Parametro | Descricao |
|-----------|-----------|
| LISTAR_CLIENTES_BLOQUEIO_DEFINITIVO | Se configurado como S (Sim): cliente sera visualizado na lista |
| | Se configurado como N (Nao): representante nao visualizara clientes com bloqueio definitivo |

### Observacao Importante

Para o funcionamento correto de todas as funcionalidades de bloqueio, e necessario realizar as devidas configuracoes no ERP. Caso os parametros aqui mencionados nao forem encontrados em pesquisa, e possivel criar o parametro atraves de opcao na tela de parametros.

---

## Consultas SQL Uteis

### Verificar Status de Pedidos (Outros ERPs)

```sql
-- Verificar se a data de abertura esta sendo retornada corretamente
SELECT
    DTABERTURAPEDPALM,
    NUMPEDPALM,
    NUMPED
FROM MXSHISTORICOPEDC
WHERE NUMPEDPALM = [numero_do_pedido]

-- Verificar pedido na tabela de integracao
SELECT
    DTABERTURAPEDPALM,
    NUMPEDPALM,
    CODCLI
FROM MXSINTEGRACAOPEDIDO
WHERE NUMPEDPALM = [numero_do_pedido]
```

### Verificar Parametros de Bloqueio de Cliente

```sql
-- Para Winthor: verificar parametro de aceitar venda para bloqueado
SELECT
    PARAMETRO,
    VALOR
FROM PCPARAMETROS
WHERE PARAMETRO = 'CON_ACEITAVENDABLOQ'
```

---

## Boas Praticas

### Pre-Pedidos

1. Definir pre-pedidos alinhados com campanhas e metas comerciais
2. Utilizar cores para diferenciar visualmente produtos estrategicos
3. Configurar datas de validade adequadas para cada campanha
4. Revisar periodicamente a performance dos pre-pedidos
5. Utilizar agrupamento por fornecedor para facilitar a positivacao

### Quantidade Maxima de Itens

1. Definir limites baseados na capacidade logistica
2. Comunicar os limites claramente para a equipe de vendas
3. Revisar periodicamente se os limites estao adequados
4. Considerar excecoes para pedidos especiais via autorizacao

### Compartilhamento de Pedidos

1. Orientar vendedores sobre quando usar PDF vs XLS
2. Verificar se o WebView esta atualizado nos aparelhos
3. Utilizar o compartilhamento para aprovacoes rapidas de clientes
4. Manter o aplicativo atualizado para evitar erros

### Desmembramento por Filial Retira

1. Utilizar apenas quando a logistica justificar
2. Orientar vendedores sobre o processo automatico
3. Evitar usar com pedidos que necessitam autorizacao
4. Documentar quais filiais retira estao ativas

### Cliente Bloqueado

1. Definir politica clara de vendas para clientes bloqueados
2. Configurar parametros alinhados com a politica de credito
3. Treinar vendedores sobre como proceder com clientes bloqueados
4. Revisar periodicamente clientes com bloqueio definitivo
5. Utilizar a opcao de orcamento como alternativa quando necessario

---

## Troubleshooting

### Problema: Pre-pedido nao aparece no aplicativo

**Solucoes:**
1. Verificar se o parametro UTILIZA_PRE_PEDIDO esta habilitado
2. Verificar se o parametro esta configurado para a Filial correta
3. Verificar se o cliente esta incluido na aba Clientes do pre-pedido
4. Verificar se a data de validade do pre-pedido esta vigente
5. Verificar se o supervisor configurado tem acesso ao vendedor

### Problema: Quantidade maxima de itens nao esta funcionando

**Solucoes:**
1. Verificar se ambos os parametros estao configurados (VERIFICAR_QTD_MAX_ITENS_PEDIDO e VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO)
2. Verificar se o parametro VERIFICAR_QTD_MAX_ITENS_PEDIDO esta habilitado (valor logico)
3. Verificar se o parametro VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO tem um valor numerico valido
4. Reiniciar o aplicativo para carregar as novas configuracoes

### Problema: Erro ao gerar arquivo PDF/XLS do pedido

**Solucoes:**
1. Desabilitar o navegador Chrome temporariamente
2. Acessar a Play Store e atualizar o Android System WebView
3. Se nao encontrar o WebView na Play Store, instalar
4. Reativar o navegador Chrome
5. Tentar gerar o arquivo novamente

### Problema: Status do pedido nao atualiza (Outros ERPs)

**Solucoes:**
1. Verificar se a coluna DTABERTURAPEDPALM esta preenchida na tabela MXSHISTORICOPEDC
2. Verificar se o ERP esta retornando a mesma data enviada na MXSINTEGRACAOPEDIDO
3. Consultar o Layout de Integracao item 5.48 para validar a estrutura
4. Verificar logs de integracao do ERP
5. Contatar o suporte tecnico para revisar as APIs de integracao

### Problema: Desmembramento nao ocorre mesmo com parametro habilitado

**Solucoes:**
1. Verificar se o pedido nao esta em processo de autorizacao (pedidos em autorizacao nao sao desmembrados)
2. Verificar se realmente foram selecionadas filiais retira diferentes
3. Verificar se o parametro DESMEMBRAR_PED_FILIAL_RETIRA esta habilitado corretamente
4. Reiniciar o aplicativo

### Problema: Cliente bloqueado consegue fazer pedido (ou vice-versa)

**Solucoes:**
1. Revisar todos os parametros de bloqueio listados neste documento
2. Verificar se ha conflito entre parametros (alguns em SIM e outros em NAO)
3. Para clientes Winthor, verificar o parametro CON_ACEITAVENDABLOQ no ERP
4. Verificar se o tipo de bloqueio (temporario, SEFAZ, definitivo) esta sendo tratado corretamente
5. Sincronizar o aplicativo para carregar as configuracoes atualizadas

---

## Integracao com ERP

### Winthor

Para clientes Winthor, alem das configuracoes no maxPedido, alguns parametros devem ser configurados diretamente no ERP:

- **CON_ACEITAVENDABLOQ**: Aceita venda para cliente bloqueado (S/N)
- **Rotina 2571**: Agrupamento de ramo de atividade por fornecedor

### Outros ERPs

Para clientes que utilizam outros ERPs, a integracao e feita via APIs. Pontos importantes:

1. Tabela MXSINTEGRACAOPEDIDO: recebe pedidos do maxPedido
2. Tabela MXSHISTORICOPEDC: retorna historico de status dos pedidos
3. Campo DTABERTURAPEDPALM: deve ser devolvido corretamente para atualizar timeline
4. Consultar Layout de Integracao para detalhes completos da estrutura de dados

---

## Anexos e Referencias

### Links Importantes

- Portal maxSolucoes: https://appsv.solucoesmaxima.com.br
- Layout de Integracao: Consultar documentacao especifica item 5.48 (Historico Pedidos Capas)
- Documentacao de criacao de parametros no maxPedido

### Rotinas Winthor Relacionadas

- Rotina 2571: Agrupamento de ramo de atividade por fornecedor

### Tabelas de Banco de Dados

- MXSINTEGRACAOPEDIDO: Integracao de pedidos (entrada)
- MXSHISTORICOPEDC: Historico de pedidos (saida)
- PCPARAMETROS: Parametros do Winthor

---

**Documento gerado para uso em sistema RAG (Retrieval-Augmented Generation)**

**Ultima atualizacao:** Fevereiro 2026

**Fonte:** Base de Conhecimento MaximaTech - Documentacao maxPedido/Winthor
