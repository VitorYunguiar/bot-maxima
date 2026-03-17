# Campanhas, Descontos e Lucratividade — Base de Conhecimento maxPedido/Winthor

**Palavras-chave:** campanhas, descontos, combos, lucratividade, MQT, SQP, MIQ, FPU, margem, cores, negociacao

**Sistema:** maxPedido, Winthor

**Area:** Vendas, Comercial, Inteligencia de Negocios

---

## 1. Visao Geral das Campanhas de Desconto

O maxPedido oferece diferentes tipos de campanhas de desconto que permitem criar regras promocionais flexiveis para incentivar vendas. As campanhas sao configuradas na Central de Configuracoes e aplicadas automaticamente no aplicativo mobile durante o processo de vendas.

### 1.1 Tipos de Campanhas Disponiveis

| Tipo | Sigla | Descricao |
|------|-------|-----------|
| Mix por Quantidade Minima | MQT | Venda de grupo de produtos com desconto em itens especificos a partir de quantidade minima |
| Quantidade Subcategoria no Pedido | SQP | Desconto baseado em quantidade de itens de subcategorias especificas |
| Mix por Intervalo de Quantidade | MIQ | Desconto aplicado quando produtos atingem intervalo especifico de quantidade (minima e maxima) |
| Faixa Unica de Pedido | FPU | Desconto baseado em faixas de quantidade com opcao de produtos obrigatorios |

---

## 2. Campanha MQT - Mix por Quantidade Minima

### 2.1 Conceito

A funcionalidade de Combo de Desconto MQT consiste na venda de um grupo de produtos obtendo desconto em determinados itens que compoem a regra, a partir de uma quantidade minima.

**Exemplo:** 3 itens precisam ser adicionados ao pedido obedecendo a quantidade minima para que se obtenha o desconto no produto "Coca Cola 2 Litros".

### 2.2 Como Cadastrar Campanha MQT

#### Passo 1: Acessar Menu de Campanhas
- Acesse a Central de Configuracoes do maxPedido
- Navegue ate: **Inteligencia de Negocio > Combo de Desconto**
- Clique no icone **+** no canto inferior direito

#### Passo 2: Preencher Dados Basicos

**Campos Obrigatorios:**
- **Descricao:** Nome identificador da campanha
- **Data Inicio:** Data de vigencia inicial
- **Data Fim:** Data de vigencia final
- **Tipo:** Selecione MQT
- **Filial:** Obrigatorio se a filial trabalhar com embalagem

**Campos Opcionais:**
- Metodologia

#### Passo 3: Configurar Restricoes (Aba Restricoes)

E possivel aplicar restricoes para limitar a campanha a:
- Filiais especificas
- Regioes
- Ramo de Atividade
- Supervisores
- Representantes
- Clientes especificos

#### Passo 4: Adicionar Itens (Aba Itens)

Para cada produto da campanha, configure:

| Campo | Descricao |
|-------|-----------|
| Produto | Codigo/nome do produto |
| Quantidade Minima | Quantidade minima necessaria para validar a regra |
| Desconto | Percentual de desconto a ser aplicado |
| Tipo de Desconto | **Automatico:** desconto nao pode ser alterado<br>**Flexivel:** desconto pode ser ajustado ate o limite definido |

### 2.3 Comportamento no Aplicativo

- A campanha aparece na aba **Campanhas de Desconto**
- Os produtos incluidos via campanha aparecem em cor diferente na aba Itens
- Nao e possivel editar itens da campanha pela aba Itens (deve usar a aba Campanhas)
- Ao tentar excluir um item, todos os produtos do combo serao excluidos

---

## 3. Campanha SQP - Quantidade Subcategoria no Pedido

### 3.1 Conceito

Campanha que aplica desconto baseado na quantidade de itens vendidos de subcategorias especificas, permitindo criar faixas com descontos diferenciados.

### 3.2 Como Cadastrar Campanha SQP

#### Passo 1: Acessar Menu de Campanhas
- Central de Configuracoes > **Inteligencia de Negocio > Combo de Desconto**
- Clique no icone **+**

#### Passo 2: Preencher Dados Basicos

**Campos Obrigatorios:**
- Descricao
- Data Inicio
- Data Fim
- Tipo: Selecione **SQP**

**Campos Opcionais:**
- Quantidade de combo por cliente
- Quantidade de combo por usuario
- Filial
- Metodologia

**Opcoes Adicionais:**
- **Considerar Familia de Produtos:** Marcar se desejar agrupar por familia
- **Debitar do conta corrente:** Marcar se aplicavel

#### Passo 3: Configurar Restricoes (Aba Restricoes)

Restricoes disponiveis:
- Filial
- Regioes
- Ramos de Atividade
- Supervisores
- Representantes
- Clientes
- Planos de pagamento

#### Passo 4: Configurar Categorias (Aba Categoria)

| Campo | Descricao |
|-------|-----------|
| Tipo | Tipo de validacao: Fornecedor, Secao, Departamento, Categoria, Sub-categoria, etc. |
| Valor | Depende do tipo selecionado (ex: se tipo = SUB-CATEGORIA, selecione a subcategoria) |
| Inicio da Faixa | Quantidade minima de itens para validar a campanha |
| Fim da Faixa | Quantidade maxima de itens |
| Desconto | Percentual de desconto aplicado quando a faixa for atingida |

**Observacao:** E possivel cadastrar multiplas faixas, cada uma com tipo, valor, inicio, fim e desconto especificos.

### 3.3 Comportamento no Aplicativo

- Ao clicar na campanha SQP, sao exibidas todas as regras cadastradas com diferentes faixas
- Ao informar quantidade que valida uma faixa, ela sera marcada como validada
- **Nao e obrigatorio validar todas as faixas** para inserir itens de uma faixa validada
- Produtos inseridos aparecem em cor diferente na aba Itens
- Edicao e exclusao devem ser feitas pela aba Campanhas de Desconto

---

## 4. Campanha MIQ - Mix por Intervalo de Quantidade

### 4.1 Conceito

Campanha que aplica desconto quando produtos especificos atingem um intervalo de quantidade (entre minimo e maximo).

### 4.2 Como Cadastrar Campanha MIQ

#### Passo 1: Acessar Menu de Campanhas
- Central de Configuracoes > **Inteligencia de Negocio > Combo de Desconto**
- Clique no icone **+**

#### Passo 2: Preencher Dados Basicos

**Campos Obrigatorios:**
- Descricao
- Data Inicio
- Data Fim
- Tipo: Selecione **MIQ**

**Campos Opcionais:**
- Quantidade de combo por cliente
- Quantidade de combo por usuario
- Filial

**Opcoes Adicionais:**
- Considerar Familia de Produtos
- Debitar do conta corrente

#### Passo 3: Configurar Restricoes (Aba Restricoes)

Restricoes disponiveis:
- Filial
- Regioes
- Ramos de Atividade
- Supervisores
- Representantes
- Clientes
- Planos de pagamento

#### Passo 4: Configurar Itens (Aba Itens)

| Campo | Descricao |
|-------|-----------|
| Produto | Selecione o produto para incluir no combo |
| Quantidade Minima | Quantidade minima necessaria no pedido |
| Quantidade Maxima | Quantidade maxima permitida no pedido |
| Desconto | Percentual de desconto aplicado |
| Tipo de Desconto | **Automatico:** representante nao pode alterar desconto<br>**Flexivel:** representante pode alterar desconto pre-estabelecido |

**Observacao:** E possivel cadastrar quantos produtos desejar, cada um com quantidade minima, maxima e desconto especificos.

### 4.3 Comportamento no Aplicativo

- Ao clicar na campanha MIQ, abre listagem dos itens com quantidade minima pre-definida
- Se quantidade informada estiver **abaixo da minima ou acima da maxima**, sera exibida mensagem de erro e a quantidade nao sera salva
- A quantidade deve estar dentro do intervalo minimo-maximo para validar
- Produtos aparecem em cor diferente na aba Itens
- Edicao e exclusao devem ser feitas pela aba Campanhas de Desconto

---

## 5. Campanha FPU - Faixa Unica de Pedido

### 5.1 Conceito

Campanha baseada em faixas de quantidade com opcao de definir produtos obrigatorios. Todas as regras cadastradas devem ser validadas para incluir os itens.

### 5.2 Como Cadastrar Campanha FPU

#### Passo 1: Acessar Menu de Campanhas
- Central de Configuracoes > **Inteligencia de Negocio > Combo de Desconto**
- Clique no icone **+**

#### Passo 2: Preencher Dados Basicos

**Campos Obrigatorios:**
- Descricao
- Data Inicio
- Data Fim
- Tipo: Selecione **FPU**

**Campos Opcionais:**
- Quantidade de combo por cliente
- Quantidade de combo por usuario
- Filial

**Opcoes Adicionais:**
- Debitar do conta corrente

#### Passo 3: Configurar Restricoes (Aba Restricoes)

Restricoes disponiveis:
- Filial
- Regioes
- Ramos de Atividade
- Supervisores
- Representantes
- Clientes
- Planos de pagamento

#### Passo 4: Configurar Categorias (Aba Categoria)

| Campo | Descricao |
|-------|-----------|
| Tipo | Tipo de validacao: Fornecedor, Secao, Departamento, Categoria, Sub-categoria, etc. |
| Valor | Depende do tipo selecionado (ex: se tipo = SUB-CATEGORIA, selecione a subcategoria) |
| Inicio da Faixa | Quantidade minima de itens para validar |
| Fim da Faixa | Quantidade maxima de itens |
| Desconto | Percentual de desconto aplicado |
| Produtos Obrigatorios | Quantidade de produtos obrigatorios que devem ser incluidos |

**Observacao:** E possivel cadastrar multiplas faixas, cada uma com configuracoes especificas.

### 5.3 Comportamento no Aplicativo

- Ao clicar na campanha FPU, sao exibidos os dados cadastrados (faixa inicial, final, desconto e produtos obrigatorios)
- Clicando sobre a campanha, abre listagem dos produtos da subcategoria configurada
- Se quantidade inserida estiver **abaixo da minima**, sera exibida mensagem informando que nao atende a regra
- Sistema verifica se a quantidade de **produtos obrigatorios** foi atendida
- Quando todas as validacoes forem atendidas, a tela informa **"Regra foi validada"**

**Importante:** Na campanha FPU, **todas as regras devem estar validadas** antes de incluir os itens no pedido.

---

## 6. Lucratividade - Configuracoes e Calculos

### 6.1 Calculo de Lucratividade Padrao

O maxPedido utiliza o seguinte calculo para determinar a lucratividade:

```
Calculo atual (maxPedido):
((PVENDA - VLCUSTOFIN) / PVENDA) * 100
```

Onde:
- **PVENDA:** Preco de venda do produto
- **VLCUSTOFIN:** Custo financeiro do produto (campo CUSTOFIN)

### 6.2 Calculo de Lucratividade Alternativa

#### Objetivo

Aprimorar o calculo de lucratividade permitindo considerar o campo **VALORULTENT** da tabela **PCEST** em vez do **CUSTOFIN**, refletindo o custo real do item, ja que o VALORULTENT contempla tambem os impostos da ultima entrada.

#### Formula da Lucratividade Alternativa

```
Calculo lucratividade alternativa:
((PVENDA - VALORULTENT) / PVENDA) * 100
```

Onde:
- **PVENDA:** Preco de venda
- **VALORULTENT:** Valor da ultima entrada (tabela PCEST)

#### Como Configurar Lucratividade Alternativa

**Passo 1:** Acesse a Central de Configuracoes do maxPedido

**Passo 2:** Navegue ate: **Menu lateral > Configuracoes > Parametros**

**Passo 3:** Busque pelo parametro **HABILITA_LUCRATIVIDADE_ALTERNATIVA** usando filtro avancado e clique em pesquisar

**Passo 4:** Clique no icone de edicao na coluna Acoes e marque para habilitar, depois clique em salvar

#### Como Funciona no Aplicativo

1. Apos iniciar novo Pedido, clique na **Aba Tabela**
2. Selecione um produto clicando no mesmo
3. Ira abrir a tela de negociacao onde o maxPedido calculara a lucratividade considerando o campo **VALORULTENT** da tabela **PCEST**

---

## 7. Configuracao de Cores da Legenda de Lucratividade

### 7.1 Objetivo

Configurar cores que sinalizem visualmente quando o item esta dentro ou fora da margem de lucratividade desejada.

### 7.2 Configuracoes no Portal

#### Passo 1: Configurar Permissoes de Usuario

1. Apos acessar o maxSolucoes, clique em **maxPedido**
2. Clique no **Menu principal**
3. Acesse **cadastro**
4. Depois clique em **usuarios**
5. Clique no icone de **editar** um usuario especifico
6. Clique em **Permissoes** e configure:
   - **Desabilitar:** "Ocultar Informacoes sobre lucratividade"
   - **Habilitar:** "Habilitar Visualizacao de Margem/Lucratividade"

#### Passo 2: Cadastrar Cores da Legenda

1. Acesse **Cadastro > Cor - Legenda de campos**
2. Clique no icone de **adicionar** na parte inferior da tela
3. Configure as informacoes:
   - **Campo:** Campo a ser sinalizado
   - **Cor:** Cor da sinalizacao
   - **Faixa de Lucratividade:** Intervalo inicial e final (ex: 0% a 10%, 10% a 20%, etc.)

#### Passo 3: Gerenciar Legendas

Apos cadastrar as configuracoes, e possivel:
- **Editar:** Alterar cores e faixas cadastradas
- **Excluir:** Remover configuracoes

### 7.3 Visualizacao no Aplicativo

1. Sincronize o aplicativo apos realizar as configuracoes no portal
2. Inicie um pedido
3. Selecione um produto
4. Informe o desconto
5. Um simbolo quadrado com a cor referente a faixa de lucratividade aparecera antes mesmo de inserir o item

---

## 8. Lucratividade Total na Tela de Negociacao

### 8.1 Objetivo

Visualizar a lucratividade total do pedido na tela de negociacao do produto para que o vendedor saiba se ja atingiu a lucratividade minima do pedido no momento da negociacao.

**Versao:** Melhoria disponivel a partir da versao 3.44.0

### 8.2 Configuracao do Parametro

#### Passo 1: Habilitar Parametro

1. Acesse a Central de Configuracoes do maxPedido
2. Clique em **Configuracoes > Parametros**
3. Pesquise o parametro **MOSTRAR_LUCRATIVIDADE_TOTAL_NEGOCIACAO**
4. Habilite o parametro

**Funcao:** Quando ativo, exibe na tela de negociacao do produto no aplicativo o percentual de lucratividade total do pedido.

### 8.3 Configuracao de Permissao de Acesso

#### Passo 1: Habilitar Permissao

1. No menu **cadastro**, acesse **perfil de usuarios**
2. Selecione o perfil desejado
3. No icone de acoes, clique em **permissoes**
4. Busque a permissao **"Habilitar Visualizacao de Margem/Lucratividade"**
5. Habilite a permissao

#### Passo 2: Configurar Cores da Faixa (Opcional)

Se a permissao "Habilitar Visualizacao de Margem/Lucratividade" estiver habilitada:

1. Acesse **cadastro > Cor/Legenda de campo**
2. Configure as cores para trazer a faixa de lucratividade com cores personalizadas

### 8.4 Visualizacao no Aplicativo

Apos realizar a configuracao na Central de Configuracoes:

- Na tela de negociacao do produto, **no canto direito** estara a informacao da **Lucratividade Total**
- A informacao sera exibida na cor selecionada conforme configurado na legenda de cores

---

## 9. Ocultar Lucratividade do Produto

### 9.1 Objetivo

Ocultar a informacao de lucratividade na tela de negociacao para usuarios ou perfis especificos.

### 9.2 Como Configurar

#### Passo 1: Habilitar Parametro

1. Acesse a Central de Configuracoes do maxPedido
2. No menu lateral, navegue ate **Configuracoes > Parametros**
3. Busque pelo parametro **OCULTAR_LUCRATIVIDADE_PRODUTO**
4. Habilite o parametro atraves do icone de edicao na barra de acoes

**Observacao:** O parametro OCULTAR_LUCRATIVIDADE_PRODUTO vem por padrao (default) desabilitado, ou seja, configurado para mostrar a lucratividade.

### 9.3 Comportamento no Aplicativo

Com o parametro habilitado:

1. No aplicativo maxPedido, ao iniciar um pedido
2. Ao selecionar um item
3. Na tela de negociacao, **a lucratividade nao sera apresentada** (sera ocultada)

---

## 10. Tabela Resumo de Parametros

| Parametro | Funcao | Valor Padrao |
|-----------|--------|--------------|
| HABILITA_LUCRATIVIDADE_ALTERNATIVA | Calcula lucratividade usando VALORULTENT ao inves de CUSTOFIN | Desabilitado |
| MOSTRAR_LUCRATIVIDADE_TOTAL_NEGOCIACAO | Exibe lucratividade total do pedido na tela de negociacao | Desabilitado |
| OCULTAR_LUCRATIVIDADE_PRODUTO | Oculta informacao de lucratividade na tela de negociacao | Desabilitado (mostra lucratividade) |

---

## 11. Tabelas de Referencia Winthor

### 11.1 Tabelas Relacionadas a Lucratividade

| Tabela | Campo | Descricao |
|--------|-------|-----------|
| PCEST | VALORULTENT | Valor da ultima entrada (inclui impostos) |
| PCEST | CUSTOFIN | Custo financeiro do produto |
| PCPRODUT | PVENDA | Preco de venda do produto |

### 11.2 Tabelas Relacionadas a Campanhas

As campanhas de desconto sao gerenciadas pela Central de Configuracoes do maxPedido e sincronizadas com o aplicativo mobile. A estrutura de dados e mantida no banco do maxPedido.

---

## 12. Boas Praticas e Recomendacoes

### 12.1 Campanhas de Desconto

1. **Planejamento:** Defina claramente o objetivo da campanha antes de configurar (volume, mix, lucratividade, etc.)
2. **Periodo de Vigencia:** Configure datas de inicio e fim adequadas ao calendario comercial
3. **Restricoes:** Use restricoes para segmentar campanhas por cliente, regiao ou representante
4. **Tipo de Desconto:**
   - Use **Automatico** quando o desconto nao deve ser alterado
   - Use **Flexivel** para dar margem de negociacao ao vendedor
5. **Teste antes de Implementar:** Teste a campanha com um grupo restrito antes de liberar amplamente

### 12.2 Lucratividade

1. **Escolha o Calculo Adequado:**
   - Use lucratividade padrao (CUSTOFIN) para analise baseada em custo medio
   - Use lucratividade alternativa (VALORULTENT) quando precisar considerar impostos da ultima entrada
2. **Cores da Legenda:** Configure faixas de cores que facilitem a visualizacao rapida (ex: vermelho para prejuizo, amarelo para baixa margem, verde para margem adequada)
3. **Permissoes:** Controle quem pode visualizar lucratividade por perfil de usuario
4. **Treinamento:** Certifique-se de que os vendedores entendem como interpretar as informacoes de lucratividade

### 12.3 Sincronizacao

Sempre sincronize o aplicativo mobile apos realizar alteracoes:
- Parametros
- Campanhas
- Configuracoes de cores
- Permissoes de usuario

---

## 13. Solucao de Problemas Comuns

### 13.1 Campanha nao Aparece no Aplicativo

**Possivel Causa:** Campanha nao sincronizada ou restricoes aplicadas

**Solucao:**
1. Verifique se o aplicativo foi sincronizado apos cadastro da campanha
2. Verifique as restricoes (Filial, Regiao, Cliente, etc.)
3. Confirme se a data atual esta dentro do periodo de vigencia
4. Verifique se o cliente/representante esta incluido na campanha

### 13.2 Lucratividade nao Exibida

**Possivel Causa:** Parametro ou permissao desabilitada

**Solucao:**
1. Verifique se o parametro OCULTAR_LUCRATIVIDADE_PRODUTO esta desabilitado
2. Confirme se a permissao "Habilitar Visualizacao de Margem/Lucratividade" esta habilitada para o perfil do usuario
3. Sincronize o aplicativo

### 13.3 Cores da Lucratividade nao Aparecem

**Possivel Causa:** Configuracao de cores ou permissao incorreta

**Solucao:**
1. Verifique se as cores foram cadastradas em "Cadastro > Cor - Legenda de campos"
2. Confirme se as faixas de lucratividade estao configuradas corretamente
3. Verifique se a permissao de visualizacao de margem esta habilitada
4. Sincronize o aplicativo

### 13.4 Nao Consigo Editar/Excluir Item da Campanha

**Comportamento Esperado:** Items de campanha nao podem ser editados pela aba Itens

**Solucao:**
1. Acesse a aba "Campanhas de Desconto" no pedido
2. Edite ou exclua pela interface da campanha
3. Lembre-se: ao excluir um item, todos os produtos do combo serao excluidos

### 13.5 Campanha FPU nao Permite Incluir Itens

**Possivel Causa:** Nem todas as regras foram validadas

**Solucao:**
1. Verifique se todas as faixas cadastradas foram validadas
2. Confirme se a quantidade de produtos obrigatorios foi atendida
3. Na campanha FPU, **todas as regras devem estar validadas** antes de incluir

---

## 14. Glossario de Termos

| Termo | Significado |
|-------|-------------|
| MQT | Mix por Quantidade Minima - Campanha que exige quantidade minima de produtos para desconto |
| SQP | Quantidade Subcategoria no Pedido - Campanha baseada em quantidade de subcategorias |
| MIQ | Mix por Intervalo de Quantidade - Campanha com intervalo minimo e maximo de quantidade |
| FPU | Faixa Unica de Pedido - Campanha com faixas e produtos obrigatorios |
| CUSTOFIN | Custo financeiro do produto (campo da tabela PCEST) |
| VALORULTENT | Valor da ultima entrada incluindo impostos (campo da tabela PCEST) |
| PVENDA | Preco de venda do produto |
| Desconto Automatico | Desconto que nao pode ser alterado pelo vendedor |
| Desconto Flexivel | Desconto que pode ser ajustado pelo vendedor ate o limite definido |
| Lucratividade | Percentual de margem de lucro calculado sobre o preco de venda |
| Sincronizacao | Processo de atualizacao de dados entre o portal e o aplicativo mobile |

---

## 15. Referencias e Artigos Relacionados

- Como trabalhar com desconto escalonado no maxPedido
- Como cadastrar e trabalhar com campanha de brindes maxPedido
- Campanha Progressiva de Desconto
- Desconto acima do permitido em venda Balcao Reserva
- Como Cadastrar Perfil de Usuarios no maxPedido
- Como Listar lote dos produtos do maxPedido
- Layout de integracao
- Como habilitar e configurar o pre pedido no maxPedido
- Como ativar Mix do Cliente no maxPedido

---

**Documento gerado em:** 2026-02-11

**Analistas responsaveis:** Cleyton Sousa, Cleyton Santana, Thais Cardoso, Rafael Rodrigues, Joao Pedro Alves

**Versao maxPedido:** 3.44.0+