# Base de Conhecimento maxPedido/Winthor — Documentos RAG (PDFs 11/02/2026)

> Documento para ingestão em banco vetorial (RAG).
> Última atualização: **2026-02-11**
> **Sistema**: maxPedido | Winthor | maxSoluções | maxGestão
> **Área**: Parâmetros | Pedidos | Campanhas | Cadastros | Permissões | Rotas

---

## Sobre este documento

Este arquivo consolida e padroniza **vários artigos** (PDFs anexos) da base de conhecimento em um formato consistente para **RAG**. Consulte quando precisar **configurar funcionalidades**, **habilitar parâmetros**, **ajustar permissões** e **entender como aparece no aplicativo**.

**Palavras-chave (geral)**: maxPedido, winthor, central de configurações, parâmetros, permissões, perfil de usuários, comissão, desconto, combo, rota, cliente, negociação, estoque, bloqueio

---

## 1. Combo de Descontos no maxPedido

### 1.1 Descrição

A funcionalidade **Combo de Desconto** permite criar um **grupo de produtos previamente definido** associado a um **desconto específico**, aplicado **automaticamente** quando o combo é vendido **por completo**. Garante padronização da condição comercial na venda. 

### 1.2 Pré-requisitos

* Acesso à **Central de configurações do maxPedido**.
* Permissão para acessar o menu de **Inteligência de Negócio**.
* Definição prévia dos produtos/categorias e da política de desconto.

### 1.3 Passo a passo

1. Acesse: **Menu → Inteligência de Negócio → Combo de Descontos**. 
2. Clique em **(+)** para criar um novo combo (também é possível **editar/excluir** combos existentes). 
3. Na aba **Dados Gerais**, preencha os campos principais (descrição, vigência, limites, tipo/metodologia). 
4. Na aba **Restrições**, configure onde o combo poderá ser aplicado (filiais, regiões, ramos etc.). 
5. Após selecionar o **Tipo**, será liberada a aba **Itens** para adicionar os produtos/categorias do combo com quantidades e desconto. 
6. (Opcional) Em **Dados Gerais**, marque **Debitar do conta corrente** para debitar o combo do conta corrente do vendedor. 

### 1.4 Parâmetros relacionados

| Parâmetro           | Descrição                                                                      | Tipo | Tabela |
| ------------------- | ------------------------------------------------------------------------------ | ---: | ------ |
| ⚠️ Pendente/Validar | O PDF não informa parâmetros específicos para habilitar o “Combo de Descontos” |    — | —      |

### 1.5 Tabelas envolvidas

| Tabela              | Descrição                                                        | Rotina ERP |
| ------------------- | ---------------------------------------------------------------- | ---------- |
| ⚠️ Pendente/Validar | O PDF não cita tabelas Winthor específicas para a funcionalidade | —          |

### 1.6 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O artigo não fornece SQL. Sugestão: consultar tabelas de campanhas/combos na base do cliente,
-- caso exista modelagem específica para "combo de descontos".
```

---

## 2. Ocultar valor máximo do produto na negociação

### 2.1 Descrição

Configuração de **permissão** para **ocultar** do vendedor a visualização de **Preço Máximo** e **Acréscimo Máximo** do produto durante a negociação no app. Disponível a partir da versão **3.111.0** do aplicativo maxPedido. 

### 2.2 Pré-requisitos

* Acesso ao maxPedido Web (Central de configurações).
* Permissão para editar **Perfil de usuários** (ou **Usuários**).
* App maxPedido em versão **≥ 3.111.0**.

### 2.3 Passo a passo

1. No maxPedido Web: **Cadastros → Perfil de usuários** e edite o perfil (ícone de edição). 
2. Abra **Permissões** (Acesso à Rotinas) e busque: **Ocultar Visualização do Preço Máx. e Acrés. Máx. do Produto**. 
3. Marque a permissão e salve. (Pode ser feito também por **usuário** em **Cadastros → Usuários**.) 
4. No app: **Clientes → selecionar cliente → novo pedido → Tabela → selecionar produto** e observar a tela de negociação. 

### 2.4 Como se comporta no aplicativo

* **Permissão habilitada**: mostra somente **Preço Mínimo** (aba Venda) e **Preço Mínimo + Desconto máximo** (aba Informações). 
* **Permissão desabilitada**: mostra **Preço Máximo** (aba Venda) e, em Informações, **Preço Mínimo, Preço Máximo, Desconto Máximo e Acréscimo Máximo**. 

### 2.5 Parâmetros relacionados

| Parâmetro           | Descrição                                          | Tipo | Tabela |
| ------------------- | -------------------------------------------------- | ---: | ------ |
| ⚠️ Pendente/Validar | Artigo trata de **permissão**, não cita parâmetros |    — | —      |

### 2.6 Tabelas envolvidas

| Tabela              | Descrição                       | Rotina ERP |
| ------------------- | ------------------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não cita tabelas Winthor | —          |

---

## 3. Comissão por profissional no maxPedido

### 3.1 Descrição

Fluxo para exibir no aplicativo do maxPedido a **comissão de profissionais** cadastrados no **ERP Winthor**, estejam eles **vinculados a um cliente** ou não. O maxPedido **integra e exibe**; cadastro e vínculo são feitos no Winthor. 

### 3.2 Pré-requisitos

* Profissionais cadastrados no **Winthor**.
* (Opcional) Vínculo **profissional ↔ cliente** cadastrado no Winthor.

### 3.3 Passo a passo (visualizar no app)

1. No app: **Clientes → selecionar cliente**. 
2. No menu lateral do pedido, iniciar **novo pedido** e no **cabeçalho** arrastar para baixo. 
3. Selecionar **Comissão por profissional** para abrir a listagem de profissionais. 

### 3.4 Regras de funcionamento

* Se existir vínculo **profissional ↔ cliente**, a tela já traz **os profissionais vinculados**. 
* Se **não** existir vínculo, ao digitar o nome, o app lista **todos os profissionais**; selecione e confirme. 

### 3.5 Parâmetros relacionados

| Parâmetro           | Descrição                                 | Tipo | Tabela |
| ------------------- | ----------------------------------------- | ---: | ------ |
| ⚠️ Pendente/Validar | Artigo não cita parâmetros de habilitação |    — | —      |

### 3.6 Tabelas envolvidas

| Tabela              | Descrição                                           | Rotina ERP |
| ------------------- | --------------------------------------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não cita tabelas; cadastro ocorre no Winthor | —          |

---

## 4. Exibir comissão progressiva na tela de negociação

### 4.1 Descrição

Permite que o vendedor identifique **descontos e comissão progressiva** cadastrados e escolha qual desconto/preço usar no pedido. Requer habilitar o parâmetro **EXIBIR_SUGESTAO_PRECO_COMISSAO**. Disponível a partir da versão **3.0** do app. 

### 4.2 Pré-requisitos

* Acesso à **Central de configurações** do maxPedido.
* Possibilidade de criar/editar parâmetros.
* App maxPedido em versão **≥ 3.0**.

### 4.3 Passo a passo

1. Central de configurações: **Configurações → Parâmetros**. 
2. Buscar o parâmetro **EXIBIR_SUGESTAO_PRECO_COMISSAO** e habilitar (ícone), depois salvar. 
3. No app: **Clientes → selecionar cliente → iniciar novo pedido**. 
4. Na aba **Tabela**, selecionar o produto e na negociação clicar em **Comissões** para ver as faixas; ao clicar numa linha, o preço/desconto é aplicado na negociação. 

### 4.4 Parâmetros relacionados

| Parâmetro                      | Descrição                                                                 | Tipo | Tabela              |
| ------------------------------ | ------------------------------------------------------------------------- | ---: | ------------------- |
| EXIBIR_SUGESTAO_PRECO_COMISSAO | Exibe sugestão de preço/comissão na negociação e permite selecionar faixa |  S/N | ⚠️ Pendente/Validar |

### 4.5 Tabelas envolvidas

| Tabela              | Descrição                              | Rotina ERP |
| ------------------- | -------------------------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não informa tabela do parâmetro | —          |

---

## 5. Visualizar a comissão de venda no aplicativo

### 5.1 Descrição

Define como **visualizar (ou ocultar)** a **comissão de venda** no aplicativo, envolvendo **parâmetros** e **permissões**. 

### 5.2 Pré-requisitos

* Acesso à Central de configurações do maxPedido.
* Permissão para editar **Parâmetros** e **Perfil de usuários** (ou Usuários).

### 5.3 Passo a passo (parâmetros)

1. Central: **Configurações → Parâmetros**. 
2. Buscar e configurar os parâmetros abaixo, habilitando e salvando. 

### 5.4 Passo a passo (permissões)

1. **Cadastros → Perfil de usuários** → editar perfil. 
2. Para **mostrar** comissão na confecção do pedido (Aba Totais): em **Permissões → Acesso à Rotinas → Clientes → Carteira de clientes/Confecção de pedidos**, marcar **Visualizar Valor de comissão de venda**. 
3. Para **não mostrar**: em **Clientes → Carteira de clientes/Confecção de pedidos**, marcar **Ocultar Informações de comissão**. 
4. (Alternativa) Pode ser feito por usuário em **Cadastros → Usuários**. 

### 5.5 Parâmetros relacionados

| Parâmetro                  | Descrição                                                                                                    | Tipo | Tabela              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ | ---: | ------------------- |
| OCULTAR_COMISSAO_MENU      | Controla se exibe a comissão prevista na aba objetivos do menu inicial; para **não trazer** deve estar **S** |  S/N | ⚠️ Pendente/Validar |
| RV_PREVISAO_COMISSAO_VENDA | Se **S**, exibe “Previsão Comissão de Venda” no resumo de venda (padrão S)                                   |  S/N | ⚠️ Pendente/Validar |



### 5.6 Como é apresentado no aplicativo

* Visualização na **Aba Totais** depende da permissão (visualizar/ocultar comissão). 
* Visualização no **Objetivos → Resumo de vendas → Resumo** depende dos parâmetros. 

### 5.7 Tabelas envolvidas

| Tabela              | Descrição                  | Rotina ERP |
| ------------------- | -------------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não informa tabelas | —          |

---

## 6. Cor por Classe de Venda para Clientes

### 6.1 Descrição

Permite exibir clientes com **cores** que diferenciam suas **classes de venda**, funcionando como **legenda/classificador** na listagem de clientes do maxPedido. O significado da cor e relacionamento é definido no ERP; o maxPedido cria classe/cor, mas o **vínculo cliente ↔ classe** é no Winthor. 

### 6.2 Pré-requisitos

* Acesso ao maxPedido via **maxSoluções** (Central de Configurações).
* Classe de venda e vínculo no **ERP Winthor** (para refletir no app). 

### 6.3 Passo a passo

1. Central: **Cadastros → Cor/Legenda de Campos**. 
2. Clique no ícone de **(+)** para adicionar. 
3. Selecione o campo **classe por venda**, escolha a **cor**, selecione a **classe** e salve. 
4. Após configurar no maxPedido e vincular no ERP, realizar **sincronização** para validar no app. 

### 6.4 Como funciona no aplicativo

* Na listagem de clientes, o círculo com as letras iniciais da razão social aparece com **cor diferenciada**. 
* Na aba de informações cadastrais, o campo **Classificação** indica a classe de venda do cliente. 

### 6.5 Parâmetros relacionados

| Parâmetro           | Descrição                              | Tipo | Tabela |
| ------------------- | -------------------------------------- | ---: | ------ |
| ⚠️ Pendente/Validar | Artigo não cita parâmetros específicos |    — | —      |

### 6.6 Tabelas envolvidas

| Tabela              | Descrição               | Rotina ERP |
| ------------------- | ----------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não cita tabelas | —          |

---

## 7. Cadastrar Perfil de Usuários no maxPedido

### 7.1 Descrição

Procedimento para criar **Perfis de Usuários** no maxPedido e configurar acessos (aba **Acesso**) e parâmetros do perfil (aba **Parâmetros**), incluindo **horários de sincronização** e bloqueios fora do horário. 

### 7.2 Pré-requisitos

* Acesso à Central de Configurações do maxPedido.
* Permissão para gerenciar **Cadastros → Perfil de Usuários**.

### 7.3 Passo a passo

1. Central: **Cadastros → Perfil de Usuários**. 
2. Clique no ícone **(+)** para criar. 
3. Se for **Perfil Administrador**, ao marcar, as demais opções não aparecem (acesso total). 
4. Se não for administrador: na aba **Acesso**, configure acesso a **Fornecedores, Departamentos, Seções, Regiões e Transportadoras**. 
5. Na aba **Parâmetros**, configure **horário de sincronização** e opções como **bloquear envio/recebimento fora do horário**, além de itens relacionados a maxTracking e Inteligência Geográfica. 

### 7.4 Parâmetros relacionados

| Parâmetro           | Descrição                                                                                | Tipo | Tabela |
| ------------------- | ---------------------------------------------------------------------------------------- | ---: | ------ |
| ⚠️ Pendente/Validar | Artigo menciona “Aba Parâmetros” do perfil, mas não lista nomes de parâmetros do sistema |    — | —      |

### 7.5 Tabelas envolvidas

| Tabela              | Descrição               | Rotina ERP |
| ------------------- | ----------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não cita tabelas | —          |

---

## 8. Vincular novo usuário cadastrado (perfil + representante ERP)

### 8.1 Descrição

Fluxo para vincular um **usuário** já cadastrado no **Portal maxSoluções** a um **perfil de acesso** e ao **Representante do ERP**, habilitando o vendedor a usar o maxPedido. 

### 8.2 Pré-requisitos

* Usuário cadastrado no **Portal maxSoluções** (verificação antes do vínculo). 
* Existência de perfis de acesso no maxPedido.
* Representante cadastrado no ERP.

### 8.3 Passo a passo

1. Central: **Cadastros → Usuários**. 
2. Localize o usuário e clique em **editar**. 
3. Aba **Permissões**: selecione um **perfil de acesso** e clique em **Aplicar**. 
4. Confirme o pop-up do vínculo (Sim). 
5. Na aba **Dados do Usuário**, selecione o **Representante do ERP** e clique em **Salvar Permissões**. 
6. Após isso, o vendedor pode baixar o app maxSoluções e logar com as credenciais. 

### 8.4 Parâmetros relacionados

| Parâmetro           | Descrição                  | Tipo | Tabela |
| ------------------- | -------------------------- | ---: | ------ |
| ⚠️ Pendente/Validar | Artigo não cita parâmetros |    — | —      |

### 8.5 Tabelas envolvidas

| Tabela              | Descrição               | Rotina ERP |
| ------------------- | ----------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não cita tabelas | —          |

---

## 9. Bloquear inserir item sem estoque no pedido

### 9.1 Descrição

Bloqueia a inserção de itens **sem estoque** no pedido via parâmetro **BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE**. Também pode ocultar produtos sem estoque via **VALIDA_RESTRICAO_ESTOQUE**. 

### 9.2 Pré-requisitos

* Acesso à Central de configurações do maxPedido.
* Permissão para editar parâmetros (e informar usuário responsável na edição).

### 9.3 Passo a passo

1. Central: **Configurações → Parâmetros**. 
2. Buscar o parâmetro **BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE** e pesquisar. 
3. Editar (ícone na coluna Ações), informar o usuário, marcar para habilitar e salvar. 
4. (Opcional) Para **não visualizar** produtos sem estoque no app, habilitar **VALIDA_RESTRICAO_ESTOQUE**. 

### 9.4 Parâmetros relacionados

| Parâmetro                                  | Descrição                                                 | Tipo | Tabela              |
| ------------------------------------------ | --------------------------------------------------------- | ---: | ------------------- |
| BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE          | Bloqueia inserção de item sem estoque no pedido           |  S/N | ⚠️ Pendente/Validar |
| VALIDA_RESTRICAO_ESTOQUE                   | Oculta produto sem estoque (não aparece para o vendedor)  |  S/N | ⚠️ Pendente/Validar |
| BLOQUEAR_VENDA_ACIMA_DO_ESTOQUE            | Bloqueia inserir item com quantidade acima da disponível  |  S/N | ⚠️ Pendente/Validar |
| BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE_CAMPANHA | Bloqueia inserir item sem estoque em campanha de desconto |  S/N | ⚠️ Pendente/Validar |
| OCULTAR_PROD_FL_SEM_ESTOQUE                | Oculta produto fora de linha sem estoque                  |  S/N | ⚠️ Pendente/Validar |



### 9.5 Tabelas envolvidas

| Tabela              | Descrição                            | Rotina ERP |
| ------------------- | ------------------------------------ | ---------- |
| ⚠️ Pendente/Validar | Artigo não cita tabelas do parâmetro | —          |

### 9.6 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O artigo não fornece SQL. Sugestão: auditar pedidos com itens sem estoque
-- consultando tabelas de saldo/estoque e itens do pedido conforme modelagem do cliente.
```

---

## 10. Cadastro e edição de Rota no cadastro de cliente via aplicativo

### 10.1 Descrição

Habilita no aplicativo a aba de **Roteiro de Visitas** durante **cadastro/edição de cliente**, permitindo criar/editar **rota**. Depende do parâmetro **HABILITA_CADASTRO_ROTA_CLIENTE** e de uma configuração de formulário que não pode estar oculta. 

### 10.2 Pré-requisitos

* Acesso à Central de configurações do maxPedido.
* Permissão para editar parâmetros e configurações de formulário.
* A opção do formulário “Roteiro de visita” não pode estar “Ocultar Ambos”. 

### 10.3 Passo a passo (configurar)

1. Central: **Configurações → Parâmetros**. 
2. Buscar **HABILITA_CADASTRO_ROTA_CLIENTE**, editar e habilitar, depois salvar. 
3. Central: **Configurações → Configurações → Aba Formulários → Clientes**. 
4. Em **Roteiro de visita**, garantir que **Ocultar Ambos** esteja **desmarcado**. 

### 10.4 Passo a passo (usar no app)

**Editar rota em cliente existente**

1. App: **Clientes → clique longo no cliente → Editar Cliente**. 
2. Confirmar edição → aba **Roteiro de Visitas** → alterar conforme necessário. 

**Criar rota em novo cliente**

1. App: **Clientes → ícone de criar novo cadastro** (barra superior). 
2. Aba **Roteiro de Visitas** → preencher dados solicitados. 
3. Salvar (ícone no canto superior direito). 

### 10.5 Campos / informações do roteiro

* **Data inicial**: início da geração de roteiros. 
* **Data final**: término da geração de roteiros. 
* **Data da próxima visita**: primeira data após cadastro quando deverá ocorrer a visita. 
* **Número da semana**: em qual semana deve ocorrer a visita. 
* **Periodicidade**: intervalo em dias (normalmente a cada 7 dias). 

### 10.6 Parâmetros relacionados

| Parâmetro                      | Descrição                                                               | Tipo | Tabela              |
| ------------------------------ | ----------------------------------------------------------------------- | ---: | ------------------- |
| HABILITA_CADASTRO_ROTA_CLIENTE | Habilita aba de Roteiro de Visitas no cadastro/edição de cliente no app |  S/N | ⚠️ Pendente/Validar |

### 10.7 Tabelas envolvidas

| Tabela              | Descrição               | Rotina ERP |
| ------------------- | ----------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não cita tabelas | —          |

---

## Troubleshooting

### Problema: Não aparece “Roteiro de Visitas” no cadastro/edição de cliente

**Sintoma**: No app, ao editar/criar cliente, a aba de roteiro/rota não aparece. 
**Causa**:

* Parâmetro **HABILITA_CADASTRO_ROTA_CLIENTE** desabilitado **ou**
* No formulário de clientes, “Roteiro de visita” está como **Ocultar Ambos** (aba oculta mesmo com parâmetro habilitado). 
  **Solução**:

1. Habilitar o parâmetro **HABILITA_CADASTRO_ROTA_CLIENTE**. 
2. Em **Formulários → Clientes**, desmarcar **Ocultar Ambos** em “Roteiro de visita”. 

---

### Problema: Ainda consigo inserir item sem estoque

**Sintoma**: Vendedor consegue adicionar item sem estoque no pedido.
**Causa**: Parâmetro **BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE** não está habilitado para o usuário/contexto correto. 
**Solução**:

1. Habilitar **BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE** (editar parâmetro, informar usuário e salvar). 
2. Se o objetivo for não exibir itens sem estoque, habilitar também **VALIDA_RESTRICAO_ESTOQUE**. 
---
# Base de Conhecimento maxPedido/Winthor — Novos Documentos RAG (PDFs 11/02/2026)

> Documento para ingestão em banco vetorial (RAG).
> Última atualização: **2026-02-11**

---

## Sobre este documento

Este arquivo contém **somente os novos conteúdos** extraídos dos PDFs mais recentes anexados, padronizados para ingestão em RAG. Consulte quando precisar configurar/usar **Filial Retira**, **Campanha de Desconto Progressivo** (cadastro e uso no app) e **Cesta de Produtos Ideais**.

**Palavras-chave (geral)**: filial retira, filial de estoque, filial de venda, campanha progressiva, desconto progressivo, família de produtos, item acelerador, família obrigatória, acompanhar campanha, cesta ideal, adesão, faixas
**Sistema**: maxPedido | Winthor | maxSoluções
**Área**: Parâmetros | Pedidos | Campanhas | Cadastros | Permissões | Negociação

---

## 1. Como trabalhar com Filial Retira no maxPedido

### 1.1 Descrição

“**Filial Retira**” ocorre quando a **filial de venda** do pedido é diferente da **filial de estoque** (retira) usada para atender os itens (ex.: pedido na filial 5, estoque retirado da filial 6). 

### 1.2 Pré-requisitos

* Configuração necessária também no **ERP** antes do maxPedido. 
* Usuário/vendedor com acesso às filiais envolvidas (venda e estoque).
* Permissões habilitadas (quando aplicável) para alterar/visualizar filial retira.

### 1.3 Passo a passo

1. Central de Configurações: **Cadastros → Perfil de Usuários → (editar) → Permissões**. 
2. Em **Acesso a dados**, liberar **Filiais (venda e estoque)** para o vendedor (ex.: filial 1 e 2 precisam estar liberadas). 
3. Em **Acesso à rotinas**, ajustar permissões relevantes:

   * **Alterar filial retira do produto** (permite o vendedor alterar a filial retira). 
   * **Ocultar visualização da filial retira** (se habilitada, oculta a visualização para o vendedor). 
4. (Opcional por usuário) Repetir o processo via **Cadastros → Usuários**. 

### 1.4 Parâmetros relacionados

| Parâmetro                                | Descrição                                                                                         | Tipo | Tabela              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------- | ---: | ------------------- |
| DEFINE_FILIAL_RETIRA_PADRAO              | Define a filial retira padrão para todos os produtos, independente do Winthor                     |  S/N | ⚠️ Pendente/Validar |
| IGNORAR_ULTIMA_FILIAL_RETIRA_SELECIONADA | Se positivo ignora a última filial retira e usa a padrão; se negativo mantém a última selecionada |  S/N | ⚠️ Pendente/Validar |
| VALIDAR_FILIALRETIRADIFERENTE            | Valida para não retirar produtos de filial retira diferente ao inserir novo produto (vs. 1º item) |  S/N | ⚠️ Pendente/Validar |
| LISTAR_PROD_EST_RETIRA                   | Exibe o estoque da filial retira                                                                  |  S/N | ⚠️ Pendente/Validar |
| UTILIZAFILIALRETIRAFILIALESTOQUE         | Verifica registro de filial retira por filial do pedido; com permissão, lista opções para seleção |  S/N | ⚠️ Pendente/Validar |



### 1.5 Tabelas envolvidas

| Tabela              | Descrição                                                             | Rotina ERP |
| ------------------- | --------------------------------------------------------------------- | ---------- |
| ⚠️ Pendente/Validar | O artigo não informa tabelas do Winthor para filial retira/parâmetros | —          |

### 1.6 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O artigo não fornece SQL.
-- Sugestão: auditar itens por filial de estoque/retira conforme modelagem do cliente (itens do pedido x estoque).
```

---

## 2. Desconto progressivo no aplicativo

### 2.1 Descrição

No app, o vendedor consegue **identificar produtos em campanha progressiva**, **filtrar por campanha/família**, **acompanhar o progresso**, visualizar **itens aceleradores** e **famílias obrigatórias**, além de consultar **logs** do desconto aplicado. 

### 2.2 Pré-requisitos

* Existência de **Campanha Progressiva** configurada no maxPedido (famílias/itens/faixas).
* Vendedor com acesso para vender os itens/famílias da campanha.

### 2.3 Passo a passo

**Visualizar produtos que participam da campanha**

1. Na confecção do pedido (aba **Tabela**), identifique os produtos com ícone de campanha progressiva e veja **família + campanha** do item. 
2. Use o ícone de filtro na barra superior para listar apenas produtos que participam da campanha. 
3. No filtro avançado, é possível selecionar por **família**. 

**Acompanhar o progresso da campanha**

1. Após adicionar produtos, acesse **Menu → Acompanhar campanha progressiva**. 
2. No acompanhamento, toque nas informações para abrir as famílias da campanha (já positivadas em **verde** e pendentes em **branco**). 

**Itens aceleradores e famílias obrigatórias**

1. Na tela de acompanhamento, veja se há **item acelerador** e sua quantidade; filtre por “famílias com itens aceleradores”, “famílias obrigatórias” etc. 
2. Famílias obrigatórias não inseridas aparecem no acompanhamento; na listagem ficam com nome em **azul** para identificar. 

**Logs e confirmação**

1. No acompanhamento, há um ícone para acessar os **logs do desconto aplicado**. 
2. Ao **salvar** o pedido, aparece uma tela de **confirmação** do desconto progressivo; após confirmar, os descontos são aplicados por item. 

### 2.4 Regras importantes (item acelerador)

* Em família com item acelerador, o desconto do item acelerador (cadastrado na Central) é **somado** ao desconto da família (ex.: 2% + 5%). 

### 2.5 Parâmetros relacionados

| Parâmetro           | Descrição                                              | Tipo | Tabela |
| ------------------- | ------------------------------------------------------ | ---: | ------ |
| ⚠️ Pendente/Validar | Este artigo descreve uso no app e não lista parâmetros |    — | —      |

### 2.6 Tabelas envolvidas

| Tabela              | Descrição                  | Rotina ERP |
| ------------------- | -------------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não informa tabelas | —          |

### 2.7 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O artigo não fornece SQL.
```

---

## 3. Como trabalhar com a Cesta de Produtos Ideais

### 3.1 Descrição

A “**Cesta de produtos ideais**” sugere um conjunto de itens com **quantidades ideais**, calcula **percentual de adesão** e aplica **desconto por faixas** conforme a adesão (ex.: 60% de adesão → 6% de desconto). 

### 3.2 Pré-requisitos

* Parâmetro **HABILITA_CESTA_IDEAL_PRODUTOS** habilitado na Central. 

### 3.3 Passo a passo

1. No app: selecionar cliente e iniciar pedido. 
2. Na aba **Tabela**, abrir o menu lateral (canto direito) e selecionar **Cesta de produtos ideais**. 
3. Selecionar a cesta desejada para listar os itens. 
4. Na lista de itens, usar **visualizar faixas** para ver o mínimo de adesão e o desconto correspondente. 
5. Ajustar quantidades:

   * A quantidade vem preenchida com o **ideal**; pode reduzir (adesão/desconto diminuem). 
   * Não pode aumentar acima do ideal; para não vender, colocar **0** ou deixar em branco. 
6. Confirmar inclusão da cesta (app mostra adesão e desconto) para salvar. 
7. Importante: itens adicionados via cesta — ao excluir 1 produto, exclui **todos** da cesta; para editar, voltar à tela da cesta. 

### 3.4 Informações exibidas na tela da cesta

* Total de produtos, vigência (data início/fim) e pontos (soma dos pontos dos produtos). 
* No cabeçalho: percentual de adesão, desconto, opção de visualizar faixas e pontuação por item. 

### 3.5 Parâmetros relacionados

| Parâmetro                     | Descrição                                             | Tipo | Tabela              |
| ----------------------------- | ----------------------------------------------------- | ---: | ------------------- |
| HABILITA_CESTA_IDEAL_PRODUTOS | Habilita a funcionalidade de Cesta de produtos ideais |  S/N | ⚠️ Pendente/Validar |



### 3.6 Tabelas envolvidas

| Tabela              | Descrição                  | Rotina ERP |
| ------------------- | -------------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não informa tabelas | —          |

### 3.7 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O artigo não fornece SQL.
```

---

## 4. Campanha Progressiva de Desconto (cadastro e configurações)

### 4.1 Descrição

A **Campanha Progressiva de Desconto** aplica desconto em **faixas progressivas** conforme critérios por **famílias de produtos**. Quanto mais famílias atendidas na venda (e/ou conforme critérios), maior a faixa de desconto. 

### 4.2 Pré-requisitos

* Parâmetro **USAR_CAMPANHA_DESCONTO_PROGRESSIVO** habilitado. 
* Famílias de produtos definidas (com itens aceleradores quando aplicável).

### 4.3 Passo a passo (Famílias de produtos)

1. Central: **Inteligência de Negócio → Família de Produto → (+)**. 
2. Aba **Cadastro**: preencher **Descrição** (obrigatória); demais campos opcionais. 
3. Aba **Item acelerador**: cadastrar um ou mais itens aceleradores e salvar. 
4. (Opcional) Usar **Importar** para incluir produtos por arquivo. 

### 4.4 Passo a passo (Campanha progressiva)

1. Central: **Inteligência de Negócio → Campanhas Progressivas → (+)**. 
2. Aba **Geral**: preencher e configurar os campos principais. 

   * Tipo de campanha: **Pedido** (critérios no pedido atual) ou **Acumulativa** (critérios ao longo da vigência). 
   * Definir filial, quantidade de famílias, limites (máximo em relação ao pedido, valores mínimo/máximo), metodologia etc. 
3. Seção **Famílias de produtos**: para cada família, configurar quantidade/valor mínimo, marcar **Obrigatória** se necessário e **Adicionar**. 
4. **Faixas progressivas**: cadastrar faixas com **Quantidade de famílias** e **% de desconto** e adicionar. 
5. Aba **Restrições**: definir restrições/exclusividades por **Clientes, Supervisores, Vendedores, Regiões e Faixas**. 

### 4.5 Regras importantes (somar descontos e item acelerador)

* Item acelerador: desconto do item acelerador é **acrescido** ao desconto da família. 
* **Somar descontos**: quando habilitado, se um produto estiver em mais de uma família/campanha (positivado em múltiplas campanhas), o desconto do produto será a **soma** dos descontos contemplados. 

### 4.6 Parâmetros relacionados

| Parâmetro                          | Descrição                                        | Tipo | Tabela              |
| ---------------------------------- | ------------------------------------------------ | ---: | ------------------- |
| USAR_CAMPANHA_DESCONTO_PROGRESSIVO | Habilita uso de Campanha Progressiva de Desconto |  S/N | ⚠️ Pendente/Validar |



### 4.7 Tabelas envolvidas

| Tabela              | Descrição                  | Rotina ERP |
| ------------------- | -------------------------- | ---------- |
| ⚠️ Pendente/Validar | Artigo não informa tabelas | —          |

### 4.8 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O artigo não fornece SQL.
```

---

## Troubleshooting

### Problema: Campanha Progressiva não aparece/funciona no app

**Sintoma**: Produtos não sinalizam campanha, não há acompanhamento, desconto não evolui.
**Causa**: Parâmetro **USAR_CAMPANHA_DESCONTO_PROGRESSIVO** desabilitado. 
**Solução**:

1. Central → **Configurações → Parâmetros** e habilitar **USAR_CAMPANHA_DESCONTO_PROGRESSIVO**. 

---

### Problema: Não consigo selecionar/alterar a Filial Retira

**Sintoma**: Vendedor não vê ou não consegue mudar a filial retira.
**Causa**:

* Vendedor sem acesso às filiais (venda/estoque). 
* Permissão **Alterar filial retira do produto** não habilitada. 
* Permissão **Ocultar visualização da filial retira** habilitada (oculta a informação). 
  **Solução**:

1. Liberar filiais em **Acesso a dados → Filiais (venda e estoque)**. 
2. Habilitar **Alterar filial retira do produto** e revisar **Ocultar visualização da filial retira**. 

---

### Problema: Menu “Cesta de produtos ideais” não aparece

**Sintoma**: Opção não existe no menu durante o pedido.
**Causa**: Parâmetro **HABILITA_CESTA_IDEAL_PRODUTOS** desabilitado. 
**Solução**:

1. Central → **Configurações → Parâmetros** e habilitar **HABILITA_CESTA_IDEAL_PRODUTOS**. 

---
# Base de Conhecimento maxPag / maxGestãoPlus — Novos Documentos RAG (PDFs 11/02/2026)

> Documento para ingestão em banco vetorial (RAG).
> Última atualização: **2026-02-11**

---

## Sobre este documento

Conteúdo **somente dos novos PDFs** anexados, reescrito e estruturado para RAG. Cobre: **maxPag** (configuração + uso no maxPedido + adquirentes + parâmetros + vínculo de cobranças), **Histórico de Transações no maxPag** e **Roteirizador de Vendedor** no **maxGestãoPlus** (carteira, coordenadas, roteirização, impressão, agenda).

**Palavras-chave (geral)**: maxPag, link de pagamento, pix, cartão de crédito, token, gateways, adquirentes, maxPayment Tokens, ambiente homologação produção, validade link, pré-autorização, captura, estorno, transações, roteirizador, maxGestãoPlus, coordenadas, latitude longitude, carteira de clientes, rota, agenda dinâmica
**Sistema**: maxPedido | Winthor | maxSoluções | maxPag | maxGestãoPlus
**Área**: Parâmetros | Pagamentos | Integração | Cadastros | Rotas | Operação

---

## 1. Como trabalhar com maxPag (link de pagamento Pix/Cartão) integrado ao maxPedido

### 1.1 Descrição

O **maxPag** permite que o vendedor **gere e compartilhe um link de pagamento** a partir do sistema. O cliente abre um **checkout web seguro** e paga conforme as opções habilitadas (**Pix** ou **Cartão de Crédito**). Também pode integrar com **maxPedido** e **maxMotorista** para apoiar o fluxo de pedidos e pagamentos. 

> Observação importante do PDF: houve integração antiga com “TINO”, mas foi encerrada por descontinuação do serviço. 

### 1.2 Pré-requisitos

* Produto maxPag contratado (via consultoria comercial, conforme PDF). 
* Acesso ao **maxSoluções** para configurar maxPag e maxPedido. 
* Configuração no **ERP** (Winthor ou outros) para o **vínculo de cobranças** (ver seção 1.7). 

### 1.3 Passo a passo

#### A) Liberar versão para usuários (maxSoluções)

1. Menu **Cadastro → Usuários → Editar** e selecione a versão liberada para o usuário. 
2. Para liberar para vários usuários: **Liberações → Gerenciar Versão → Novo** → selecione usuários e a versão. (As telas ilustram o fluxo; ver imagens do PDF nas primeiras páginas.) 

#### B) Acessar o maxPag no maxSoluções

1. No menu inicial do maxSoluções, clique na tela do **maxPag**. (Imagem do PDF mostra o card do produto no painel.) 

#### C) Configurar Filiais, Token e Gateways no maxPag

1. No maxPag: **Configuração → Filiais** e clique em **Iniciar**. 
2. Cadastro da filial:

   * Defina **logo**, **nome da filial**, **CNPJ** e **cor de fundo** (identidade visual mostrada no link de pagamento). 
3. **Token**:

   * Habilite token, defina um **nome**, gere o token e selecione **permissões** (ex.: gerar pagamento, estornar, etc.).
   * Para múltiplos tokens na mesma filial, use o botão/ícone de **“+”** (imagem do PDF ilustra). 
4. **Gateways**:

   * Habilite, informe **adquirentes**, **ambiente** (Homologação/Produção), **prioridade (1–20)** e **forma de pagamento** (Cartão/Pix). 
   * Regra de prioridade: se a adquirente “prioridade 1” falhar, cai para “prioridade 2” e assim por diante. 

> Nota do PDF: preencher corretamente é crítico, pois o **token** também será usado como vínculo no maxPedido. 

#### D) Vincular token do maxPag no maxPedido (maxPayment Tokens)

1. Copie o **token** gerado no maxPag. 
2. No maxSoluções: acesse **maxVenda → maxPedido**. 
3. Na central de configurações do maxPedido: **Cadastros → maxPayment Tokens**. 
4. Clique em **“+”** para inserir, selecione a **filial** e cole o **token**. Salve. 

**Validação importante**: se o token não for o mesmo gerado para a filial selecionada (CNPJ), o maxPag nega a requisição por falta de vínculo. 

### 1.4 Parâmetros relacionados

| Parâmetro                        | Descrição                                                                                                           | Tipo | Tabela              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---: | ------------------- |
| AMBIENTE_MAXPAYMENT              | Define se dados do cartão usados na pré-autorização são de **homologação** ou **produção** (NUMBER: 0=HMO, 1=PROD)  |    N | ⚠️ Pendente/Validar |
| VALIDADE_LINK_MAXPAYMENT         | Validade do link (em horas), máximo **168**; se **0**, usa padrão **24h**                                           |    N | ⚠️ Pendente/Validar |
| PERC_ACRESC_PREAUTORI_CATAO_CRED | % adicional reservado na pré-autorização do cartão (opcional)                                                       |    N | ⚠️ Pendente/Validar |
| PERMITIR_VENDA_CARTAO_CREDITO    | Habilita venda por cartão (por usuário). PDF menciona “Versão mínima 20”                                            |  S/N | ⚠️ Pendente/Validar |
| MODO_HOLOGACAO_API_CARTAO        | Habilita cobrança “cartão de crédito” via link (fluxo antigo citado como descontinuável)                            |  S/N | ⚠️ Pendente/Validar |
| ATIVAR_JOBMAXPAG_EXTRATOR        | Ativa jobs que analisam faturamento/cancelamento para finalizar fluxo (ativar em todos os clientes que usam maxPag) |  S/N | ⚠️ Pendente/Validar |

Parâmetros adicionais citados para meio de pagamento **Marvin** (agenda de recebíveis):
CODCOB_MARVIN; HABILITA_LIMITE_RECEBIVEIS_MARVIN; CONSULTA_MAXPAG_ADQUIRENTE_MARVIN (Marvin=7); CONSULTA_MAXPAG_SERVICO_ADQUIRENTE_MARVIN (Consultar Agenda Recebíveis=1); CODFILIAL_RECEBIVEIS_MARVIN. 

### 1.5 Tabelas envolvidas

| Tabela              | Descrição                                                       | Rotina ERP |
| ------------------- | --------------------------------------------------------------- | ---------- |
| ⚠️ Pendente/Validar | PDFs não informam tabelas de persistência dos parâmetros/tokens | —          |

### 1.6 Fluxo no aplicativo do maxPedido (gerar link e acompanhar pagamento)

1. No app do maxPedido: **Clientes → selecione cliente → inicie pedido** e inclua itens na aba Tabela. 
2. No **Cabeçalho / Informações do pedido**, selecione: **filial**, **plano de pagamento** e a **cobrança Pix ou Cartão de crédito**. (Imagens do PDF mostram a seleção na tela.) 
3. **Salvar e enviar pedido**. O app orienta acessar o menu **Pedidos** para obter o link. 
4. Em **Pedidos**, o pedido pode aparecer como “**Aguardando link de pagamento**”; após atualizar, o link fica disponível. 
5. Compartilhar link:

   * Clique longo no pedido → opção de compartilhar **ou**
   * Toque no ícone de cartão/pix → abre **Status do Pagamento** com opção de compartilhar. 
6. Em **Status do Pagamento**, o quadro **Movimentações** mostra eventos (pré-autorizado, autorizado etc.). Para atualizar, faça **swipe para baixo** (arrastar de cima para baixo). As imagens do PDF ilustram a tela. 

### 1.7 Vínculo de cobranças no ERP (Winthor e outros)

**Winthor**

* Para **Pix**: cobrança com **código = “PIX”**. 
* Para **Cartão de Crédito**: flag **“Cartão de crédito”** habilitada. (PDF mostra exemplo em tela de cadastro de cobrança.) 

**Outros ERPs**

* Para Pix: endpoint **Cobranças**, `CODCOB = PIX`
* Para cartão: endpoint **Cobranças**, `CARTAO = 'S'` 

### 1.8 Listagem de adquirentes (provedores)

A tabela abaixo aparece no PDF como referência de provedores/serviços integráveis (formas de pagamento). 

| Provedor                 | Forma de pagamento         |
| ------------------------ | -------------------------- |
| Banco do Brasil          | Pix                        |
| Bradesco                 | Pix                        |
| GerenciaNET/Efi          | Pix                        |
| Sicoob                   | Pix                        |
| PaymentCore TOTVS        | Pix                        |
| Itaú                     | Pix                        |
| Sicredi                  | Pix                        |
| Cielo                    | Cartão de Crédito          |
| GetNet                   | Cartão de Crédito          |
| Rede                     | Cartão de Crédito          |
| Sofware Express          | Cartão de Crédito          |
| Sofware Express Checkout | Cartão de Crédito / Pix    |
| Marvin                   | Saldo de máquina de cartão |
| Konduto                  | Antifraude                 |
| ClearSale                | Antifraude                 |

### 1.9 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O PDF não fornece SQL.
-- Sugestão: caso exista base local, auditar vínculos (filial x token) e transações por status.
```

---

## 2. Histórico de Transações no maxPag

### 2.1 Descrição

A funcionalidade **Histórico de Transações** permite acompanhar, de forma centralizada, transações de pagamento feitas via maxPedido ou maxMotorista (Pix ou Cartão). Na tela, é possível **ver movimentos**, **capturar pagamento**, **estornar**, **sincronizar status** e até **incluir transações manuais isoladas** (para gerar link de pagamento). 

### 2.2 Pré-requisitos

* Acesso ao portal do maxPag.
* Transações geradas via maxPedido/maxMotorista (ou inseridas manualmente).

### 2.3 Passo a passo

1. No portal do maxPag, menu lateral: **Transações**. 
2. Na listagem, na coluna **Ações**, use os ícones para:

   * visualizar movimentos
   * capturar pagamento
   * estornar pagamento
   * sincronizar status 
3. Para criar transação isolada: clique no ícone **“+”** e preencha para gerar link; ela passa a aparecer na lista junto das demais. 
4. Personalizar colunas: ícone de **engrenagem** (marcar/desmarcar campos) e salvar. (Imagem do PDF mostra o painel de personalização.) 
5. Exportar: botão **Exportar** para gerar Excel com as transações. (Imagem do PDF mostra a ação de exportação.) 

### 2.4 Parâmetros relacionados

| Parâmetro           | Descrição                                          | Tipo | Tabela |
| ------------------- | -------------------------------------------------- | ---: | ------ |
| ⚠️ Pendente/Validar | PDF não cita parâmetros específicos para esta tela |    — | —      |

### 2.5 Tabelas envolvidas

| Tabela              | Descrição            | Rotina ERP |
| ------------------- | -------------------- | ---------- |
| ⚠️ Pendente/Validar | PDF não cita tabelas | —          |

### 2.6 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O PDF não fornece SQL.
```

---

## 3. Roteirizador de vendedor no maxGestãoPlus

### 3.1 Descrição

O **Roteirizador de vendedor** é um módulo do maxGestãoPlus para:

* gerenciar **carteira de clientes** por vendedor
* gerar/ajustar **coordenadas (latitude/longitude)**
* criar **rotas** (roteirização) por dia da semana
* **imprimir** rotas
* montar **agenda de visitas** (semanal e dinâmica) 

> Observação do PDF (reforçada em destaque nas páginas com imagens): alterações de endereço feitas para gerar coordenadas **não alteram o endereço no ERP**; servem apenas para cálculo de coordenadas no roteirizador. 

### 3.2 Pré-requisitos

* Acesso ao maxGestão e ao módulo Roteirizador (maxGestãoPlus).
* Selecionar **Supervisor** nos filtros (obrigatório para pesquisar carteira/roteirização). 
* Para visualizar clientes no mapa: clientes precisam ter **coordenadas geradas**. 

### 3.3 Passo a passo

#### A) Acessar o roteirizador

1. No maxGestão, clique no ícone no canto esquerdo e depois em **Roteirizador**. 
2. Isso abre o módulo do maxGestãoPlus para roteirização/carteira/regiões. 

#### B) Trabalhar com carteira de clientes e mapa

1. Em **Carteira de clientes**, no filtro avançado selecione obrigatoriamente o **Supervisor** e clique em **Pesquisar**. 
2. Verifique a coluna/indicador de **Clientes sem Coordenadas** para saber o que falta gerar. 
3. Pins no mapa e cards indicam vendedores por **cores** (clientes do vendedor herdam a cor do pin). 
4. Use **Gerenciar coordenadas** (ícone no card do RCA) para listar:

   * clientes sem coordenadas
   * clientes com coordenadas
   * todos os clientes 
5. Gerar/atualizar coordenadas:

   * **Importar do ERP** (se o ERP tiver lat/long) **ou**
   * **Gerar coordenadas** (aproximação via endereço: rua/bairro/município/estado/CEP) **ou**
   * inserir manualmente lat/long clicando no pin e salvando (conforme descrito). 
6. “Casa do vendedor”:

   * Em **Gerenciar casa do vendedor**, altere endereço ou insira lat/long para definir o ponto de referência do RCA (sem alterar endereço no ERP). 
7. Legendas (informação destacada nas telas com imagem):

   * pin **cinza**: cliente ainda não caracterizado
   * pin **preto**: cliente caracterizado para mais de um vendedor
   * ícone de casa: ponto “casa do vendedor”
   * ícone de seleção: clientes selecionados 
8. Ao selecionar vendedor e clientes no mapa, aparecem ações para:

   * incluir cliente na carteira
   * remover cliente da carteira
   * limpar última marcação
   * remover todas as marcações 

#### C) Realizar roteirização (criar rota e distribuir visitas por dia)

1. Em **Roteirização**, preencha filtros (filial/supervisor/vendedor; supervisor obrigatório). 
2. Selecione o vendedor e clique em **Roteirizar RCA** (botão mostrado nas imagens do PDF). 
3. Crie uma rota: **Criar Rota → preencher descrição/nome → Salvar**. 
4. Selecione a rota criada e escolha o **dia da semana** (balões coloridos por dia). 
5. Selecione clientes no mapa usando o modo de seleção (ícones no canto superior direito do mapa). 
6. Regiões:

   * Na coluna **Regiões**, selecione uma região cadastrada para o vendedor e clique em **Roteirizar**. Linha tracejada indica ausência de regiões. 
7. Ponto inicial/final:

   * Por padrão, o ponto inicial é a casa do vendedor; é possível alterar ponto inicial/final no “gerenciar dia da semana” (ícone mostrado nas imagens). 
8. Sequência de visitas:

   * O sistema sugere a melhor rota (menor km).
   * É possível reordenar manualmente arrastando clientes na aba Resultado e clicando em **Reordenar**. 
9. Adicionar mais clientes depois:

   * Use o botão **Cliente** para inserir clientes na ordenação; o sistema pode perguntar se deseja reordenar automaticamente (sim recalcula; não adiciona ao final). 

#### D) Imprimir rota

1. Na aba roteirização, selecione o supervisor e na listagem clique no ícone de **emitir relatório**. 
2. Selecione tipo de impressão (clientes sem roteiro / com roteiro) e clique em **Imprimir**. 

#### E) Montar agenda de visita

**Agenda semanal (manual)**

1. No canto esquerdo superior, clique em **Roteiro de visitas**. 
2. Informe vendedor (com roteiro criado), configure **mês/ano**, **semana do mês**, selecione o **roteiro**, defina **hora início** e **tempo médio de visita**; clique **Adicionar** para criar agenda semanal. 
3. Você pode excluir a agenda e também “Gerar” para incluir no planejamento do vendedor. 
4. No planejamento, bolinhas representam clientes; a rota aparece com símbolo/cor correspondente e hover mostra o nome do cliente (conforme descrito). 

**Agenda dinâmica**

1. Na tela de roteirização, clique em **Agenda Dinâmica**. 
2. Configure:

   * período (data início/fim),
   * hora início jornada,
   * **TMD** (tempo médio deslocamento) e **TMV** (tempo médio visita),
   * planejamento semanal (selecionar rota e adicionar sequência),
   * clique em **Gerar Agenda**. 

### 3.4 Parâmetros relacionados

| Parâmetro           | Descrição                               | Tipo | Tabela |
| ------------------- | --------------------------------------- | ---: | ------ |
| ⚠️ Pendente/Validar | PDF não cita parâmetros do roteirizador |    — | —      |

### 3.5 Tabelas envolvidas

| Tabela              | Descrição            | Rotina ERP |
| ------------------- | -------------------- | ---------- |
| ⚠️ Pendente/Validar | PDF não cita tabelas | —          |

### 3.6 SQL útil

```sql
-- ⚠️ Pendente/Validar
-- O PDF não fornece SQL.
```

---

## Troubleshooting

### Problema: Clientes não aparecem no mapa do roteirizador

**Sintoma**: Mapa sem pins/sem clientes para o vendedor.
**Causa**: Coordenadas não foram geradas/importadas; o PDF indica que para apresentar no mapa é obrigatório gerar coordenadas. 
**Solução**:

1. Abrir “Gerenciar coordenadas” e gerar/importar lat/long (ERP ou aproximação por endereço). 

---

### Problema: maxPag nega requisição ao tentar usar no maxPedido

**Sintoma**: Erro/negação ao gerar/usar pagamento pelo maxPedido.
**Causa**: Token informado não possui vínculo com o CNPJ da filial selecionada (token diferente do gerado para aquela filial). 
**Solução**:

1. Conferir token no maxPag (filial correta) e recadastrar em **Cadastros → maxPayment Tokens** no maxPedido com a filial correspondente. 

---


