# Guias e Procedimentos do maxPedido — Base de Conhecimento

**Palavras-chave**: maxPedido, configuração, parâmetros, perfil de usuários, data limite, atualização, liberar versão, RCA, vendedor, aplicativo, consultas, positivação de clientes, títulos, notificação de estoque, políticas comerciais, histórico de pedidos, aniversários, agrupamento por fornecedor, roteiro de visitas, mapa de oportunidades, pré‑pedido, compartilhar pedidos, PDF, XLS, download de imagens, campanhas de desconto, MQT, MIQ, SQP, FPU, bloqueio de cliente, visita avulsa, lucratividade, limite de itens, desmembramento de pedido, filial retira, solução de problemas, status do pedido, erro ao gerar arquivo, limpeza de base, reestruturação de base, criação de parâmetros, processamento de imagens, férias, controle de férias, consultas SQL, glossário, tabelas, permissões, conta corrente, broker, meta gráfico, espelho do pedido, boleto, previsão de faturamento, parâmetros, Winthor, rotinas

**Sistema**: maxPedido, Winthor

**Área**: Procedimentos, Configurações, Consultas, Campanhas, Troubleshooting, Suporte Técnico, Integração

---

## 1. Configurações Administrativas

### 1.1 Como configurar a data limite para atualização do maxPedido?

**Descrição**: Define o prazo máximo em que o RCA (vendedor) poderá usar uma versão liberada do aplicativo. Após essa data, ele será obrigado a atualizar para a versão mais recente.

**Pré‑requisitos**: Ter login e senha do portal maxSoluções.

**Passo a passo**:
1. Acesse o portal em [https://apps.v.soluocoesmaxima.com.br](https://apps.v.soluocoesmaxima.com.br) e informe usuário e senha.
2. Se houver dois ambientes (Homologação e Produção), escolha o desejado (geralmente Produção).
3. No menu lateral, acesse **Cadastro > 304 – Liberar Versão**.
4. Clique em **Novo**.
5. Selecione o **Cliente**.
6. Selecione a **Rotina/Versão** que deseja liberar.
7. Escolha os **RCAs** que estarão na regra (pode selecionar todos, filtrar ou escolher um a um). Clique em **Adicionar Selecionados**.
8. Preencha o campo **Data Limite Atualização**.
9. Clique em **Salvar**.

**Resultado esperado**: A partir da data definida, os vendedores selecionados serão obrigados a atualizar o aplicativo antes de continuar usando.

---

### 1.2 Como vincular um novo usuário cadastrado

**Descrição**: Após cadastrar um usuário no portal, é necessário vinculá‑lo a um perfil de acesso e a um representante (vendedor) no ERP para que ele possa usar o maxPedido.

**Pré‑requisitos**: Usuário já cadastrado no portal maxSoluções.

**Passo a passo**:
1. Acesse a **Central de Configurações** do maxPedido.
2. No menu lateral, clique em **Cadastros > Usuários**.
3. Localize o usuário desejado e clique no ícone de **editar** (na coluna Ações).
4. Na tela de edição, vá para a aba **Permissões**.
5. Selecione um **perfil de acesso** e clique em **Aplicar**.
6. Um pop‑up perguntará se deseja confirmar o vínculo. Clique em **Sim**.
7. Você será direcionado à aba **Dados do Usuário**.
8. Selecione o **Representante do ERP** correspondente.
9. Clique em **Salvar Permissões**.

**Resultado esperado**: O vendedor agora pode baixar o aplicativo **maxSoluções** na Play Store e fazer login com as credenciais cadastradas.

---

### 1.3 Como habilitar e configurar o pré‑pedido no maxPedido

**Descrição**: A funcionalidade de pré‑pedido permite criar um modelo de pedido pré‑configurado (com itens, quantidades, região, filial etc.) que pode ser oferecido como sugestão ou obrigação ao vendedor, agilizando a venda e garantindo alinhamento com estratégias comerciais.

**Pré‑requisitos**: Login e senha do portal maxSoluções.

**Benefícios**:
- Direciona o vendedor com um modelo pronto, reduzindo erros.
- Garante padronização nas vendas.
- Agiliza a montagem do pedido.
- Apoia campanhas, acordos e metas.

#### 1.3.1 Habilitar o parâmetro
1. Acesse o portal (https://appsv.soluocoesmaxima.com.br) e faça login.
2. Escolha o ambiente (Produção ou Homologação).
3. Clique em **maxVendas** e depois em **maxPedido**.
4. No menu lateral, vá em **Configurações > Parâmetros**.
5. Pesquise pelo parâmetro **UTILIZA_PRE_PEDIDO** (pode usar filtros por nome e tipo).
6. No ícone de ações, arraste para habilitar (ou desabilitar) o parâmetro.
7. Clique em **Salvar**.
   - **Tipo de dado**: Lógico.
   - **Tipo do parâmetro**: Pode ser Geral ou por Filial, conforme necessidade.
   - Caso o parâmetro não exista, é possível criá‑lo (veja seção 1.11).

#### 1.3.2 Cadastrar um pré‑pedido
1. No menu lateral, acesse **Inteligência de Negócio > Recomendação de produto > Pré‑Pedido**.
2. Clique no ícone **+** (adicionar) no canto inferior direito.
3. Preencha as três abas:

**Aba Dados do Pré‑pedido**:
- **Código** e **Descrição** (identificação do pré‑pedido).
- **Data inicial** e **Data final** (vigência).
- **Cor** (os itens do pré‑pedido serão destacados com essa cor no aplicativo).
- **Supervisor** (que terá acesso a este pré‑pedido).
- **Filial** (à qual se aplica).
- **Ramo de atividade** (será usado para filtrar os clientes que receberão este pré‑pedido).
- **Região** (região de abrangência).
- Opções:
  - **Aplicar cor e ordenar produto**: aplica a cor nos itens e os ordena.
  - **Apresentar pop‑up e ordenar produtos por cor**: exibe um pop‑up com os itens coloridos no momento da venda.
  > Quando se utiliza o ramo de atividade do fornecedor, os ramos são agrupados conforme cadastro na rotina 2571 (Winthor) ou no módulo de Inteligência de Negócios da Central de Configurações. A validação no aplicativo continua sendo pelo ramo do cliente.

**Aba Clientes**:
- Selecione os clientes que terão acesso a este pré‑pedido.
- Utilize as opções **Adicionar** ou **Importar** para incluir a lista.

**Aba Itens do pré‑pedido**:
- Preencha os filtros desejados (departamento, seção, categoria, subcategoria) para localizar os produtos.
- Selecione o **produto** e informe a **quantidade**.
- Clique em **Adicionar** ou **Importar** para incluir os itens.

4. Após preencher todas as abas, clique em **Salvar Pré‑Pedido**.

#### 1.3.3 Visualização no aplicativo
- Se a opção **Apresentar pop‑up** estiver marcada e o parâmetro **ORDENA_COR_PREPEDIDO** estiver habilitado, ao iniciar um pedido com um cliente que possua pré‑pedido configurado, um pop‑up será exibido com os itens sugeridos.
- Na listagem de produtos (aba **Tabela**), os itens do pré‑pedido aparecerão destacados com a cor definida no cadastro e ordenados conforme configuração.

---

### 1.4 Parâmetros para venda a clientes bloqueados

**Descrição**: Controla se o vendedor pode ou não realizar vendas para clientes que estão bloqueados no ERP. Envolve vários parâmetros que devem ser configurados em conjunto.

**Pré‑requisitos**: Acesso à Central de Configurações e permissão para editar parâmetros.

#### 1.4.1 Parâmetros para **permitir** a venda para cliente bloqueado
Configure os seguintes parâmetros com os valores indicados:
- **ACEITAVENDAAVISTACLIBLOQ** = S (Sim)
- **ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO** = S (Sim)
- **BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ** = N (Não)
- **BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ** = N (Não)
- **VERIFICABLOQUEIOSEFAZ** = N (Não) – permite pedido mesmo com restrição no SEFAZ.
- **PERMITE_ORCAMENTO_CLIENTE_BLOQ** = S (Sim)
- **BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ_DEFINITIVO** = N (Não)

Para clientes Winthor, o parâmetro **CON_ACEITAVENDABLOQ** deve estar como **S** no ERP.

#### 1.4.2 Parâmetros para **não permitir** a venda para cliente bloqueado
- **ACEITAVENDAAVISTACLIBLOQ** = N (Não)
- **ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO** = N (Não)
- **BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ** = S (Sim)
- **BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ** = S (Sim)
- **VERIFICABLOQUEIOSEFAZ** = S (Sim) – bloqueia se houver restrição no SEFAZ.
- **PERMITE_ORCAMENTO_CLIENTE_BLOQ** = N (Não)
- **BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ_DEFINITIVO** = S (Sim)

#### 1.4.3 Visualização no aplicativo
Independentemente da configuração, o cliente bloqueado aparecerá na lista com um ícone de cadeado 🔒. Se a venda não for permitida, ao tentar iniciar um pedido, o vendedor verá uma mensagem informando que só é possível salvar como orçamento.

#### 1.4.4 Cliente com bloqueio definitivo
O parâmetro **LISTAR_CLIENTES_BLOQUEIO_DEFINITIVO** controla se clientes com bloqueio definitivo aparecem na lista:
- **S** (Sim): aparecem (com cadeado).
- **N** (Não): não aparecem.

Caso algum parâmetro não seja encontrado, consulte a seção **1.11 Como criar parâmetros**.

---

### 1.5 Visita Avulsa

**Descrição**: Permite ao vendedor registrar uma visita a um cliente sem a necessidade de um roteiro pré‑definido. Pode ser configurada para exigir check-in.

**Configuração**:
1. Na Central de Configurações, acesse **Cadastros > Usuários**.
2. Pesquise o usuário desejado e clique em **editar**.
3. Na aba **Permissões**, localize a permissão **Habilitar criação de visita avulsa** e habilite‑a.
4. (Opcional) Para obrigar o check-in em visitas avulsas, acesse **Configurações > Parâmetros**, busque por **OBRIGA_CHECKIN_VISITA_AVULSA**, edite e habilite para o usuário.

**Uso no aplicativo**:
1. Na tela inicial, acesse **Clientes**.
2. Pressione longamente sobre o cliente desejado e escolha **Gerar visita Avulsa**.
3. Confirme a ação. A visita será registrada e, se desejado, um novo pedido pode ser iniciado em seguida.

---

### 1.6 Cores da legenda de lucratividade

**Descrição**: Permite configurar cores para diferentes faixas de lucratividade dos produtos, facilitando a identificação visual no aplicativo.

**Configuração no portal**:
1. Acesse a Central de Configurações do maxPedido.
2. No menu lateral, vá em **Cadastros > Usuários**.
3. Selecione o usuário e clique em **editar**.
4. Na aba **Permissões**, desabilite as permissões:
   - "Habilitar Visualização de Margem / Lucratividade"
   - "Ocultar Informações sobre lucratividade"
5. Em seguida, acesse **Cadastro > Cor – Legenda de campos**.
6. Cadastre as faixas de lucratividade com as cores desejadas (é possível editar ou excluir posteriormente).

**Visualização no aplicativo**:
Após sincronizar, ao iniciar um pedido e selecionar um produto, um quadrado colorido aparecerá ao lado do item, indicando a faixa de lucratividade correspondente, mesmo antes de inserir o produto.

---

### 1.7 Cadastro de Perfil de Usuários

**Descrição**: Cria e configura perfis de acesso que determinam as permissões dos usuários no maxPedido.

**Passo a passo**:
1. Na Central de Configurações, acesse **Cadastros > Perfil de Usuários**.
2. Clique no ícone **+** no canto inferior direito.
3. Se for um **Perfil Administrador**, marque a opção correspondente – isso concede acesso total e oculta as demais configurações.
4. Caso contrário, preencha os dados básicos e vá para a aba **Acesso** para configurar permissões específicas (fornecedores, departamentos, seções, regiões, transportadoras).
5. Na aba **Parâmetros**, é possível configurar:
   - Horário de sincronização (bloquear envio/recebimento fora do horário).
   - Horário permitido para coleta de dados do maxTracking.
   - Parâmetros de Inteligência Geográfica.
6. Clique em **Salvar**.

---

### 1.8 Limite de itens por pedido

**Descrição**: Define uma quantidade máxima de itens que um pedido pode conter. Quando ultrapassada, o vendedor é alertado.

**Configuração**:
1. Acesse **Configurações > Parâmetros** na Central.
2. Pesquise pelos parâmetros:
   - **VERIFICAR_QTD_MAX_ITENS_PEDIDO** (habilita a validação)
   - **VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO** (define o número máximo)
3. Edite cada um:
   - No primeiro, marque para habilitar e salve.
   - No segundo, informe a quantidade máxima desejada e salve.
   > **Atenção**: Ambos os parâmetros são complementares e devem estar configurados.

**Comportamento no app**:
Ao tentar inserir uma quantidade de itens superior ao limite, o vendedor receberá uma mensagem informando que o máximo permitido foi atingido.

---

### 1.9 Lucratividade alternativa

**Descrição**: Permite que o cálculo de lucratividade do produto no aplicativo utilize o campo **VALORULTENT** (valor da última entrada) em vez do **CUSTOFIN**, refletindo um custo mais real (com impostos inclusos).

**Fórmulas**:
- Padrão: `((PVENDA - CUSTOFIN) / PVENDA) * 100`
- Alternativa: `((PVENDA - VALORULTENT) / PVENDA) * 100`

**Configuração**:
1. Acesse **Configurações > Parâmetros**.
2. Busque pelo parâmetro **HABILITA_LUCRATIVIDADE_ALTERNATIVA**.
3. Clique em editar, marque para habilitar e salve.

**No aplicativo**:
Após habilitar, ao iniciar um pedido e acessar a aba **Tabela**, a lucratividade exibida para cada produto será calculada com base no **VALORULTENT**.

---

### 1.10 Exibir lucratividade total do pedido na negociação

**Descrição**: Permite que o vendedor visualize, na tela de negociação de cada produto, a lucratividade total acumulada do pedido até o momento, auxiliando na tomada de decisão sobre descontos.

**Configuração**:
1. Acesse **Configurações > Parâmetros** na Central.
2. Busque pelo parâmetro **MOSTRAR_LUCRATIVIDADE_TOTAL_NEGOCIACAO**.
3. Habilite‑o (marque como Sim) e salve.
4. Além disso, é necessário que a permissão **Habilitar Visualização de Margem/Lucratividade** esteja ativa para o perfil do usuário (em **Cadastros > Perfil de Usuários**, edite o perfil, vá em **Permissões** e habilite).
5. Opcionalmente, configure as cores das faixas de lucratividade em **Cadastro > Cor/Legenda de campos** (veja seção 1.6).

**Visualização no aplicativo**:
- Ao iniciar um pedido e selecionar um produto, na tela de negociação (canto direito) aparecerá o percentual de lucratividade total do pedido até aquele momento, na cor correspondente à faixa configurada.

---

### 1.11 Ocultar lucratividade do produto

**Descrição**: Permite ocultar a informação de lucratividade na tela de negociação do produto, caso não seja desejável que o vendedor a visualize.

**Configuração**:
1. Acesse **Configurações > Parâmetros**.
2. Busque pelo parâmetro **OCULTAR_LUCRATIVIDADE_PRODUTO**.
3. Habilite‑o (marque como Sim) para ocultar a lucratividade. Por padrão, vem desabilitado (lucratividade visível).
4. Salve.

**Visualização no aplicativo**:
- Com o parâmetro habilitado, ao selecionar um produto, a informação de lucratividade não será exibida.

---

### 1.12 Gerenciar férias de vendedores

**Descrição**: Permite configurar períodos de férias para os vendedores. Durante as férias, o vendedor fica impossibilitado de usar o aplicativo (pedidos, captura de geolocalização, etc.). O controle pode ser feito por usuário.

**Pré‑requisitos**: Acesso à Central de Configurações.

**Passo a passo**:
1. **Habilitar o parâmetro de férias**:
   - Acesse **Configurações > Parâmetros**.
   - Busque por **HABILITA_FERIAS_VENDEDOR**.
   - Edite, selecione o usuário (ou mantenha em branco para todos), marque para habilitar e salve.
2. **Conceder permissão ao usuário** (se necessário):
   - Vá em **Cadastros > Usuários**.
   - Selecione o usuário e clique em **editar**.
   - Na aba **Permissões**, no quadro **Acesso a rotinas**, marque a opção **Férias** (dentro de Cadastro). Isso permite que o usuário visualize e gerencie o cadastro de férias (se for administrador).
3. **Cadastrar o período de férias**:
   - Acesse **Cadastro > Férias**.
   - Clique no ícone **+** para adicionar.
   - Selecione um ou múltiplos usuários que estarão de férias.
   - Informe a data de início e fim das férias.
   - Salve.

**Efeito no aplicativo**: Durante o período cadastrado, o vendedor não conseguirá acessar o aplicativo (será bloqueado). Após o término, o acesso é restabelecido automaticamente.

---

### 1.13 Como criar parâmetros

**Descrição**: Instruções para criar um novo parâmetro na Central de Configurações, caso ele não exista.

**Passo a passo**:
1. Acesse a Central de Configurações do maxPedido.
2. Vá em **Configurações > Parâmetros**.
3. Clique no botão **Criar parâmetro** (geralmente no canto inferior direito).
4. Preencha os campos:
   - **Título do parâmetro**: nome descritivo (apenas para identificação).
   - **Nome do parâmetro**: identificador técnico (exatamente como será usado, sem espaços, respeitando maiúsculas/minúsculas).
   - **Descrição**: breve resumo da funcionalidade.
   - **Categoria**: escolha entre as disponíveis (Venda, Configuração, Sincronismo, etc.).
   - **Tipo do parâmetro**: Geral, Por usuário ou Por filial.
   - **Tipo de dado**: Literal (texto), Inteiro (número) ou Lógico (booleano).
5. Clique em **Salvar**.

Após criado, o parâmetro aparecerá na lista e poderá ser configurado normalmente.

---

### 1.14 Desmembramento de pedido por filial retira

**Descrição**: Quando um pedido contém itens de diferentes filiais de retirada (estoque), o sistema pode desmembrá‑lo automaticamente em vários pedidos, um para cada filial.

**Configuração**:
1. Acesse **Configurações > Parâmetros**.
2. Busque pelo parâmetro **DESMEMBRAR_PED_FILIAL_RETIRA**.
3. Edite e habilite (marque como Sim). Salve.

**Uso no aplicativo**:
1. Ao iniciar um pedido, na aba **Tabela**, selecione um produto.
2. Escolha a filial retira desejada (se houver múltiplas opções).
3. Repita para outros produtos, possivelmente com filiais retira diferentes.
4. Ao salvar e enviar o pedido, o sistema validará e, se houver itens de filiais distintas, criará automaticamente um pedido para cada filial retira.
   > **Atenção**: Nenhuma validação adicional (como autorizações) será aplicada nos pedidos desmembrados. Se o pedido original exigir autorização, o desmembramento não ocorrerá.

---

## 2. Consultas no Aplicativo maxPedido

### 2.1 Positivação de Clientes

**Descrição**: Permite pesquisar clientes positivados (que já compraram) e não positivados (que nunca compraram), com filtros por período, cliente ou fornecedor.

**Passo a passo**:
1. No aplicativo, acesse a aba **Consultas** e clique em **Positivação de Clientes**.
2. Escolha o tipo de filtro:
   - **Positivado** (clientes com venda no período)
   - **Não positivado** (clientes sem venda)
3. Informe o período desejado e, opcionalmente, filtre por **Cliente** ou **Fornecedor**.
4. Clique em **Confirmar**.
5. A tela exibirá a lista de clientes e, para os positivados, os produtos vendidos a cada um.

Para sair da tela de resultado, utilize o botão **Voltar** do aparelho.

---

### 2.2 Consulta de Títulos

**Descrição**: Exibe a posição financeira dos clientes, com possibilidade de parametrização para mostrar títulos pagos/não pagos, gerados pelo vendedor ou não, e apenas vencidos.

**Passo a passo**:
1. No aplicativo, acesse **Consultas > Títulos**.
2. A consulta pode ser refinada com parâmetros definidos na parte administrativa (ex.: mostrar todos os títulos, apenas do vendedor, apenas vencidos).
3. A tela de resultados mostra a situação financeira dos clientes.
   - Ao tocar no ícone de **filtros**, é possível aplicar filtros adicionais.
   - O ícone de **legendas** mostra as cores que identificam o status de cada título (ex.: vencido, pago, em aberto).

---

### 2.3 Notificação de Estoque

**Descrição**: Permite consultar notificações enviadas pelo ERP sobre chegada ou término de mercadoria.

**Definições**:
- **Chegada de mercadoria**: estoque anterior = 0, estoque atual > 0.
- **Término de mercadoria**: estoque anterior > 0, estoque atual = 0.

**Passo a passo**:
1. No aplicativo, acesse **Consultas > Notificação de Estoque**.
2. Selecione o tipo de notificação (Chegada ou Término), a filial e o período (De / Até).
3. A tela exibirá as notificações recebidas conforme os filtros.

---

### 2.4 Políticas Comerciais

**Descrição**: Lista as políticas comerciais (descontos, condições especiais) cadastradas no ERP que foram liberadas para o força de vendas.

**Passo a passo**:
1. No aplicativo, acesse **Consultas > Políticas Comerciais**.
2. Será exibida uma lista com as políticas vigentes para a seleção atual (vendedor/cliente/filial).

---

### 2.5 Histórico de Pedidos

**Descrição**: Consulta pedidos já realizados, com filtro por período e opções de ordenação.

**Passo a passo**:
1. No aplicativo, acesse **Consultas > Histórico de Pedidos**.
2. Selecione o período desejado e clique em **Pesquisar**.
3. Os pedidos serão listados. É possível identificar o status pela cor (consulte as **Legendas do Sistema**).
4. Use a opção **Ordenação** para definir a ordem de exibição (crescente/decrescente).

---

### 2.6 Aniversários

**Descrição**: Exibe os contatos cadastrados para os clientes e suas respectivas datas de aniversário, conforme os filtros informados na tela inicial.

**Passo a passo**:
1. No aplicativo, acesse **Consultas > Aniversários**.
2. A tela trará a lista de contatos e suas datas de aniversário de acordo com a pesquisa feita.

---

### 2.7 Agrupamento de produtos por fornecedor

**Descrição**: No momento da venda, é possível agrupar a lista de produtos por fornecedor, facilitando a visualização e seleção.

**Configuração**:
- O parâmetro **EXIBIR_AGRUPAMENTO_FORNECEDOR** vem como **Sim** por padrão. Se desejar desabilitar, altere para **Não** na Central de Configurações (Configurações > Parâmetros).

**Uso no aplicativo**:
1. Acesse **Clientes**, selecione um cliente e inicie um novo pedido.
2. Na tela de produtos, toque no ícone de três pontos e escolha **Agrupar produtos por fornecedor**.
3. A lista será reorganizada, mostrando os fornecedores. Ao expandir um fornecedor, são exibidas informações:
   - **Produtos ideais**: quantidade de produtos do pré‑pedido para aquele fornecedor.
   - **Positivado**: quantos desses ideais já foram positivados.
   - **Total produtos**: quantidade total de produtos do fornecedor.
   - **Positivado**: total de produtos positivados do fornecedor.

---

### 2.8 Roteiro de Visitas – Visualização e gerenciamento

**Descrição**: O roteiro de visitas é configurado no ERP e sincronizado com o maxPedido. O vendedor pode visualizar os clientes agendados para cada dia, acompanhar percentuais de atendimento e positivação, e interagir com cada cliente (justificar visita, iniciar pedido, etc.).

**Pré‑requisitos**: Roteiro de visitas devidamente configurado no ERP e vinculado aos vendedores.

#### 2.8.1 Visualizar o roteiro do dia e de outros dias
1. Na tela inicial, acesse a aba **Clientes**.
2. Por padrão, são exibidos os clientes do dia (o rodapé mostra a quantidade).
3. Para ver todos os clientes (sem filtro de roteiro), clique no ícone de três pontos e escolha **Ver todos**.
4. Para voltar a exibir apenas os clientes do dia, escolha **Roteiro Hoje**.
5. Para visualizar o roteiro completo por dias da semana, clique no ícone de três pontos e escolha **Roteiro**.
   - Será exibida uma tela com os dias da semana e, ao expandir cada dia, a lista de clientes agendados.
   - Também são mostrados:
     - **Percentual de atendimento** (clientes visitados / agendados)
     - **Percentual de positivação** (clientes com venda / visitados)
6. Para visualizar o roteiro de uma data específica (passada ou futura), na tela do roteiro clique no ícone de três pontos e escolha **Selecionar Data**. Informe a data desejada. Se não houver roteiro para a data, a tela ficará em branco.

#### 2.8.2 Interagir com um cliente no roteiro
- Na lista de clientes (do dia ou do roteiro), ao lado do nome do cliente há um ícone de três pontos. Clicando nele, surgem opções como:
  - **Justificar Visita**: abre uma tela para registrar o motivo da não venda.
  - **Iniciar Pedido**: inicia um novo pedido para o cliente.
  - **Ver Histórico**: consulta pedidos anteriores.
  - **Editar Cliente**: permite alterar dados do cadastro (se houver permissão).
- Dependendo da configuração (check-in obrigatório), pode ser necessário realizar check-in antes de executar algumas ações.

#### 2.8.3 Legendas e ícones
- No roteiro, ao clicar no ícone de três pontos e depois em **Legendas**, é exibida uma tela com todos os ícones que podem aparecer ao lado dos clientes e seus significados (ex.: cliente bloqueado, pendência, etc.).

---

### 2.9 Mapa de Oportunidades

**Descrição**: Oferece ao vendedor uma visualização em mapa dos clientes positivados e de novas oportunidades de prospecção dentro de um raio definido, facilitando o planejamento de rotas.

**Disponível a partir da versão 4.011.3**.

**Benefícios**:
- Visualização estratégica da carteira.
- Identificação rápida de oportunidades próximas.
- Maior eficiência nas visitas.

#### 2.9.1 Configuração
1. Na Central de Configurações, acesse **Configurações > Parâmetros** e habilite o parâmetro **HABILITA_MAPA_OPORTUNIDADE**.
2. Ainda na Central, vá em **Cadastros > Perfil de usuários**.
3. Selecione o perfil desejado e edite.
4. Na aba **Configurações**, localize **Mapa de Oportunidades** e configure:
   - **CNAEs** (opcional): filtrar por CNAE.
   - **Capital social** (opcional).
   - **Distância máx. cadastro**: raio em metros para cadastrar uma oportunidade.
   - **Distância máx. pesquisa**: raio em quilômetros para buscar oportunidades.

#### 2.9.2 Uso no aplicativo
1. Na tela inicial, acesse **Clientes** > ícone de **Mais opções** > **Mapa de oportunidades**.
2. No mapa, utilize os botões:
   - **Clientes**: exibe todos os clientes da carteira (positivados ou não) no período.
   - **Prospects**: exibe oportunidades capturadas no raio configurado.
   - **Distância**: ajusta o raio de busca.
3. Ao clicar em um cliente/prospect, é possível:
   - **Cadastrar**: abre o formulário de cadastro do cliente.
   - **Traçar Rota**: abre o aplicativo de mapas padrão do aparelho para traçar a rota até o local.

---

## 3. Compartilhamento e Recursos

### 3.1 Compartilhar pedidos e orçamentos (PDF/XLS)

**Descrição**: Permite gerar um arquivo PDF ou XLS (Excel) de um pedido ou orçamento e compartilhá‑lo por diversos aplicativos.

**Passo a passo**:
1. Na tela inicial do aplicativo, acesse o menu **Pedidos**.
2. Localize o pedido ou orçamento desejado e faça um **toque longo** sobre ele.
3. No pop‑up que aparece, escolha **Compartilhar**.
4. Selecione o formato do arquivo: **PDF** ou **XLS**.
5. Clique em **Gerar**.
6. Aguarde a barra de progresso atingir 100%.
7. Aparecerão as opções de aplicativos para compartilhamento (e‑mail, WhatsApp, etc.). Escolha a desejada.

---

### 3.2 Download de imagens (processamento de fotos)

**Descrição**: Procedimento para baixar as imagens dos produtos no aplicativo, seja via Wi-Fi ou rede móvel.

**Pré‑requisitos**:
- Diretório das imagens compartilhado na mesma rede do extrator Linux.
- Ponto de montagem configurado no Linux (contate o suporte se necessário).

**Passo a passo**:
1. No aplicativo, acesse o menu superior direito e clique em **Ferramentas**.
2. Escolha **Baixar fotos**. O download será iniciado (por padrão, só permite via Wi-Fi).
3. Para permitir download via rede móvel (3G/4G), vá em **Configurações > Ver parâmetros** e marque **Enviar fotos usando redes móveis**.
4. Acompanhe o progresso na barra de notificações do Android.

---

## 4. Campanhas de Desconto

### 4.1 MQT – Mix por Quantidade Mínima

**Descrição**: A campanha MQT concede desconto em determinados itens quando um grupo de produtos atinge uma quantidade mínima. O desconto pode ser flexível (alterável) ou automático.

**Cadastro**:
1. Na Central de Configurações, acesse **Inteligência de Negócio > Combo de Desconto**.
2. Clique no ícone **+**.
3. Preencha os campos obrigatórios: **Descrição**, **Data Início**, **Data Fim** e **Tipo** (selecione MQT).
4. Opcionalmente, defina **Quantidade de combo por cliente/usuário**, **Filial**, e marque **Debitar do conta corrente** se desejado.
5. Na aba **Restrições**, adicione restrições por filial, região, ramo de atividade, supervisor, representante ou cliente.
6. Na aba **Itens**, adicione os produtos com:
   - **Produto**
   - **Quantidade Mínima**
   - **Desconto** (%)
   - **Tipo de Desconto**: Automático (não alterável) ou Flexível (alterável)
7. Clique em **Adicionar** para cada item e depois em **Salvar**.

**Visualização no app**:
- No pedido, acesse a aba **Campanhas de Desconto**. A campanha MQT aparecerá listada.
- Ao clicar, os itens da campanha são exibidos com suas quantidades mínimas. O vendedor deve inserir a quantidade adequada; se estiver fora do mínimo, uma mensagem de erro é exibida.
- Após inserir os itens, eles aparecem na aba **Itens** com uma cor diferente, indicando que fazem parte de uma campanha. Não é possível editar ou excluir individualmente pela aba Itens; deve‑se voltar à campanha.

---

### 4.2 MIQ – Mix por Intervalo de Quantidade

**Descrição**: Similar ao MQT, mas cada item possui uma quantidade mínima e máxima. O desconto é aplicado quando a quantidade do item está dentro do intervalo.

**Cadastro**:
1. Acesse **Inteligência de Negócio > Combo de Desconto** e clique em **+**.
2. Preencha **Descrição**, **Data Início**, **Data Fim** e **Tipo** (MIQ).
3. Configure restrições na aba **Restrições** (opcional).
4. Na aba **Itens**, adicione cada produto com:
   - **Produto**
   - **Quantidade Mínima**
   - **Quantidade Máxima**
   - **Desconto** (%)
   - **Tipo de Desconto** (Automático/Flexível)
5. Salve.

**Visualização no app**:
- A campanha aparece na aba **Campanhas de Desconto**.
- Ao abrir, os itens são listados com os intervalos. Se a quantidade informada estiver fora do intervalo, uma mensagem de erro impede a inserção.
- Itens inseridos são destacados na aba **Itens**.

---

### 4.3 SQP – Quantidade por Subcategoria

**Descrição**: A campanha é definida por subcategorias de produtos. Para cada subcategoria, são definidas faixas de quantidade (início e fim) e um percentual de desconto. O vendedor pode validar uma ou mais faixas independentemente.

**Cadastro**:
1. Acesse **Inteligência de Negócio > Combo de Desconto** e clique em **+**.
2. Preencha os dados básicos com **Tipo** = SQP.
3. Na aba **Restrições**, defina as restrições desejadas.
4. Na aba **Categoria**, configure:
   - **Tipo**: por exemplo, SUB‑CATEGORIA.
   - **Valor**: selecione a subcategoria.
   - **Início da Faixa** e **Fim da Faixa** (quantidades).
   - **Desconto** (%).
   - Clique em **Adicionar**. É possível cadastrar múltiplas faixas para a mesma ou diferentes subcategorias.
5. Salve.

**Visualização no app**:
- Na aba **Campanhas de Desconto**, a campanha SQP exibe as faixas cadastradas.
- Ao clicar em uma faixa, os produtos da subcategoria são listados. O vendedor informa a quantidade; se estiver dentro da faixa, a regra é validada.
- É possível inserir itens de uma faixa mesmo que outras não estejam validadas.
- Itens inseridos aparecem destacados na aba **Itens**.

---

### 4.4 FPU – Faixa Única de Pedido

**Descrição**: A campanha FPU define uma ou mais faixas de quantidade (geralmente baseadas em subcategorias) e um desconto. Diferentemente do SQP, **todas as regras devem ser validadas simultaneamente** para que os itens possam ser inseridos.

**Cadastro**:
1. Acesse **Inteligência de Negócio > Combo de Desconto** e clique em **+**.
2. Preencha com **Tipo** = FPU.
3. Na aba **Restrições**, adicione restrições se necessário.
4. Na aba **Categoria**, cadastre as faixas (similar ao SQP). É possível também definir **Produtos obrigatórios** para cada faixa.
5. Salve.

**Visualização no app**:
- Na aba **Campanhas de Desconto**, a campanha FPU exibe as faixas.
- O vendedor deve atender **todas as faixas** (quantidades mínimas/máximas e produtos obrigatórios) para que a campanha seja validada.
- Enquanto alguma regra não estiver satisfeita, o sistema impede a inserção dos itens.
- Após validação completa, os itens podem ser inseridos e aparecem destacados.

---

## 5. Solução de Problemas (Troubleshooting)

### 5.1 Status do pedido não atualizando no App (Clientes Outros ERPs)

**Descrição**: Para clientes que não utilizam Winthor, a atualização da timeline de status do pedido depende do preenchimento correto da coluna **DTABERTURAPEDPALM** na tabela **MXSHISTORICOPEDC** do banco de dados da Máxima. Esse campo deve conter a data/hora em que o pedido foi processado no ERP, que é enviada pela integração.

**Causa**: O ERP não está devolvendo essa informação na tabela de retorno.

**Solução**:
- Verifique no layout de integração (item 5.48 – Histórico Pedidos Capas) que o campo **DTABERTURAPEDPALM** deve ser preenchido.
- Garanta que, ao processar o pedido, o ERP retorne esse valor na tabela **MXSINTEGRACAOPEDIDO** e que ele seja gravado em **MXSHISTORICOPEDC**.
- Consulte o artigo *Layout de integração* para mais detalhes.

---

### 5.2 Erro ao gerar arquivo do pedido (PDF/XLS)

**Descrição**: Ao tentar gerar um PDF ou XLS de um pedido, o processo fica travado ou não conclui.

**Causa comum**: Problemas com o WebView do sistema Android.

**Solução**:
1. Nas configurações do aparelho, acesse **Aplicativos**.
2. Localize o aplicativo **Chrome** e **desinstale** (isso desabilita temporariamente).
3. Acesse a **Play Store** e procure por **WebView** (Android System WebView).
   - Se estiver instalado, atualize‑o.
   - Se não estiver, instale.
4. Após a atualização/instalação, reative o Chrome (se desejar).
5. Tente gerar o arquivo novamente.

---

### 5.3 Limpeza da base de dados

**Descrição**: Procedimento para apagar todos os dados locais do aplicativo (pedidos não enviados, configurações, etc.) e restaurar o estado inicial. Útil para corrigir problemas de banco de dados.

**Atenção**: Todos os dados não sincronizados serão perdidos.

**Passo a passo**:
1. Nas configurações do aparelho, acesse **Aplicativos**.
2. Vá para a aba **Gerenciar aplicativo** (ou equivalente).
3. Localize o aplicativo do maxPedido e clique sobre ele.
4. Selecione **Armazenamento**.
5. Clique em **Limpar dados** e confirme.

---

### 5.4 Reestruturação da base de dados

**Descrição**: Reestrutura o banco de dados do aplicativo, validando e remodelando as tabelas sem perder dados (diferente da limpeza). Pode resolver problemas de estrutura.

**Passo a passo**:
1. No aplicativo, acesse o menu superior direito e clique em **Ferramentas**.
2. Escolha **Backup e Restauração**.
3. Clique em **Reestruturar Banco**.
4. Confirme no pop‑up clicando em **SIM**.
5. Aguarde a conclusão.

---

## 6. Consultas SQL para Suporte

Esta seção reúne consultas SQL úteis para análise e diagnóstico no ambiente de banco de dados da Máxima (nuvem). Utilize com cuidado e apenas se tiver acesso apropriado.

### 6.1 Consultar versão do banco de dados na nuvem
```sql
SELECT * FROM MXSVERSAOBD ORDER BY DTATUALIZACAO DESC;
```

### 6.2 Verificar tabelas com erros de integração (status -1)
```sql
SELECT COUNT(1), TABELA 
FROM PCMXSINTEGRACAO 
WHERE STATUS = -1 
GROUP BY TABELA 
ORDER BY COUNT(1) DESC;
```

### 6.3 Consultar produtos positivados no mês para um vendedor
```sql
SELECT COUNT(DISTINCT CODPROD) 
FROM MXSPRODUTPOS 
WHERE TRUNC(DTPOSITIVACAO) BETWEEN TO_DATE('01/04/2024', 'DD/MM/YYYY') 
                               AND TO_DATE('30/04/2024', 'DD/MM/YYYY') 
  AND CODUSUARIO IN (SELECT CODUSUARIO FROM MXSUSUARIOS WHERE CODUSUR = 73);
```

### 6.4 Identificar região de um cliente
```sql
SELECT C.CODPRACA, R.NUMREGIAO, C.CODCLI, C.CLIENTE
FROM MXSCLIENT C
INNER JOIN MXSPRACA P ON P.CODPRACA = C.CODPRACA
INNER JOIN MXSREGIAO R ON R.NUMREGIAO = P.NUMREGIAO
WHERE CODCLI IN (12345);
```

### 6.5 Verificar estoque disponível e cotas de produto
```sql
-- Estoque disponível (considerando bloqueado, pendente, reservado)
SELECT (QTESTGER - QTBLOQUEADA - QTPENDENTE - QTRESERV) AS ESTOQUEDISP, MXSEST.*
FROM MXSEST
WHERE CODPROD IN (7072);

-- Verificar cotas de produto por cliente
SELECT * FROM MXSPRODUSUR 
WHERE CODCLI IN (19483) AND CODPROD IN (7072, 7081);
```

### 6.6 Consultar pedidos com produtos em JSON (MXSINTEGRACAOPEDIDO)
```sql
SELECT ID_PEDIDO, NUMPED, DATA, PJSON.CODPRODUTO, PJSON.DESCRICAO, 
       PJSON.QUANTIDADE, PJSON.PRECOVENDA
FROM MXSINTEGRACAOPEDIDO PED_TAB,
JSON_TABLE(OBJETO_JSON, '$.Produtos[*]'
  COLUMNS (
    ROW_NUMBER FOR ORDINALITY,
    CODPRODUTO VARCHAR(10) PATH '$.Codigo',
    DESCRICAO VARCHAR(2000) PATH '$.Descricao',
    QUANTIDADE VARCHAR(10) PATH '$.Quantidade',
    PRECOVENDA VARCHAR(100) PATH '$.PrecoVenda'
  )) PJSON
WHERE PED_TAB.CODUSUR IN (1206) 
  AND PED_TAB.CODCLI IN (6001) 
  AND PJSON.CODPRODUTO IN (8269);
```

### 6.7 Verificar se o serviço de agendamento do Oracle está rodando
```sql
SELECT sid, serial#, username, program, module
FROM v$session
WHERE program LIKE 'CJQ%' OR program LIKE 'J0%';
```

### 6.8 Consultar devoluções (resumo de vendas)
```sql
SELECT CODUSUR, DTENT DATA, 
       SUM(VLDEVOLUCAO 
           - DECODE(OBTER_PARAMETRO('REDUZIRST_DADOS_RELATORIO', NULL, 'N'), 'S', NVL(VLST,0), 0)
           - DECODE(OBTER_PARAMETRO('REDUZIRIPI_DADOS_RELATORIO', NULL, 'N'), 'S', NVL(VLIPI,0), 0)) AS VLDEVOL
FROM (
  SELECT DISTINCT
         ERP_MXSNFENT.DTENT,
         ERP_MXSNFENT.CODUSURDEVOL CODUSUR,
         ROUND(NVL(ERP_MXSMOV.QT,0) * 
               (NVL(ERP_MXSMOV.PUNIT,0) + NVL(ERP_MXSMOV.VLFREITE,0) + 
                NVL(ERP_MXSMOV.VLOUTRASDESP,0) + NVL(ERP_MXSMOV.VLFREITE_RATEIO,0) + 
                NVL(ERP_MXSMOV.VLOUTROS,0) - NVL(ERP_MXSMOV.VLREPASSE,0)), 2) VLDEVOLUCAO,
         ROUND(NVL(ERP_MXSMOV.QT,0) * NVL(ERP_MXSMOV.ST,0), 2) VLST,
         ROUND(NVL(ERP_MXSMOV.QT,0) * NVL(ERP_MXSMOV.VLIPI,0), 2) VLIPI
  FROM ERP_MXSNFENT
  INNER JOIN ERP_MXSESTCOM ON ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT
  INNER JOIN ERP_MXSMOV ON ERP_MXSESTCOM.NUMTRANSENT = ERP_MXSMOV.NUMTRANSENT
  INNER JOIN MXSPRODUT ON MXSPRODUT.CODPROD = ERP_MXSMOV.CODPROD
  WHERE ERP_MXSNFENT.CODOPERACAO != 2
    AND ERP_MXSMOV.CODOPERACAO != 2
    AND ERP_MXSNFENT.DTENT BETWEEN TRUNC(TO_DATE('01/06/2025', 'dd/MM/yyyy')) 
                               AND TRUNC(TO_DATE('30/06/2025', 'dd/MM/yyyy'))
    AND ERP_MXSNFENT.CODUSURDEVOL = 334
    AND ERP_MXSNFENT.CODFILIAL IN (3)
)
GROUP BY CODUSUR, DTENT;
```

### 6.9 Validar integridade de produtos (pendências em tabelas relacionadas)
```sql
SELECT P.CODPROD,
       CASE WHEN P.CODFORNEC IS NULL THEN 'P.CODFORNEC AUSENTE'
            WHEN F.CODFORNEC IS NULL THEN 'P.CODFORNEC INEXISTENTE EM MXSFORNEC'
            ELSE NULL END AS STATUS_CODFORNEC,
       CASE WHEN P.CODSEC IS NULL THEN 'P.CODSEC AUSENTE'
            WHEN S.CODSEC IS NULL THEN 'P.CODSEC INEXISTENTE EM MXSSECAO'
            ELSE NULL END AS STATUS_CODSEC,
       CASE WHEN P.CODEPTO IS NULL THEN 'P.CODEPTO AUSENTE'
            WHEN D.CODEPTO IS NULL THEN 'P.CODEPTO INEXISTENTE EM MXSDEPTO'
            ELSE NULL END AS STATUS_CODEPTO,
       CASE WHEN P.DTEXCLUSAO IS NOT NULL THEN 'P.DTEXCLUSAO PREENCHIDA' ELSE NULL END AS STATUS_P_DTEXCLUSAO,
       CASE WHEN P.ENVIARFORCAVENDAS <> 'S' THEN 'P.ENVIARFORCAVENDAS != S' ELSE NULL END AS STATUS_P_ENVIARFORCAVENDAS,
       CASE WHEN P.REVENDA <> 'S' THEN 'P.REVENDA != S' ELSE NULL END AS STATUS_P_REVENDA,
       CASE WHEN P.CODOPERACAO = 2 THEN 'P.CODOPERACAO = 2' ELSE NULL END AS STATUS_P_CODOPERACAO,
       CASE WHEN F.CODFORNEC IS NOT NULL AND F.CODOPERACAO = 2 THEN 'MXSFORNEC.CODOPERACAO = 2' ELSE NULL END AS STATUS_F_CODOPERACAO,
       CASE WHEN F.CODFORNEC IS NOT NULL AND F.REVENDA <> 'S' THEN 'MXSFORNEC.REVENDA != S' ELSE NULL END AS STATUS_F_REVENDA,
       CASE WHEN S.CODSEC IS NOT NULL AND S.CODOPERACAO = 2 THEN 'MXSSECAO.CODOPERACAO = 2' ELSE NULL END AS STATUS_S_CODOPERACAO,
       CASE WHEN D.CODEPTO IS NOT NULL AND D.CODOPERACAO = 2 THEN 'MXSDEPTO.CODOPERACAO = 2' ELSE NULL END AS STATUS_D_CODOPERACAO,
       CASE WHEN (P.CODFORNEC IS NULL OR F.CODFORNEC IS NULL OR
                  P.CODSEC IS NULL OR S.CODSEC IS NULL OR
                  P.CODEPTO IS NULL OR D.CODEPTO IS NULL OR
                  P.DTEXCLUSAO IS NOT NULL OR
                  P.ENVIARFORCAVENDAS <> 'S' OR
                  P.REVENDA <> 'S' OR
                  P.CODOPERACAO = 2 OR
                  F.CODOPERACAO = 2 OR
                  S.CODOPERACAO = 2 OR
                  D.CODOPERACAO = 2 OR
                  F.REVENDA <> 'S')
             THEN 'PENDENCIA ENCONTRADA'
             ELSE 'OK' END AS STATUS_GERAL
FROM MXSPRODUT P
LEFT JOIN MXSFORNEC F ON P.CODFORNEC = F.CODFORNEC
LEFT JOIN MXSSECAO S ON P.CODSEC = S.CODSEC
LEFT JOIN MXSDEPTO D ON P.CODEPTO = D.CODEPTO
WHERE P.CODPROD IN (284445);
```

---

## 7. Glossário e Parâmetros Relevantes

Esta seção consolida definições, tabelas e parâmetros importantes para entendimento e configuração do maxPedido.

### 7.1 Brindes
Tabelas envolvidas:
- `MXSBRINDEEX` – Cabeçalho da campanha de brinde.
- `MXSBRINDEEXPREMIO` – Itens que serão brindes.
- `MXSBRINDEEXRESTRICOES` – Restrições da campanha (regiões, filiais, etc.).
- `MXSBRINDEEXVALIDACOES` – Validações (peso, quantidade, valor).

### 7.2 Conta Corrente (CC / Flex)
Parâmetros e configurações:
- `EXIBIR_SALDOCC_DISPONIVEL = S` – Exibe saldo disponível.
- `CON_USACREDRCA = S` – Habilita uso de conta corrente.
- `CON_TIPOMOVCCRCA` – Define o momento do débito/crédito:
  - `VA` – Débito na venda, crédito no acerto.
  - `VF` – Débito na venda, crédito no faturamento.
  - `VV` – Débito/crédito na venda.
  - `FF` – Débito/crédito no faturamento.
- `MXSUSUARI.USADEBCREDRCA = S` – Por usuário, indica se usa débito/crédito.

### 7.3 Bloquear RCA de fazer bonificação sem saldo de C/C
Parâmetros:
- `CON_USACREDRCA = S`
- `CON_BONIFICALTDEBCREDRCA = S`
- `IMPEDIR_ABATIMENTO_SEMSALDORCA = S`
- `PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N`

### 7.4 Desconto Máximo / Limite de Desconto
Onde verificar:
- `MXSTABPR.PERDESCMAX` – Desconto máximo por produto/região.
- `MXSCLIENTREGIAO.PERDESCMAX` – Desconto máximo por cliente/região.
- Políticas de desconto do item (cadastradas no ERP).

### 7.5 Meta Gráfico
- Rotinas: 399 / 3305.
- Tabelas: `ERP_MXSMETARCA`, `PCMETARCA`, `PCMETA`.
- Observação: Para a rotina 3305, basta que a meta esteja na tabela `PCMETA` (não precisa descer para a nuvem). Pode não ser informada se a flag de dias úteis não estiver marcada.

### 7.6 Histórico de Pedidos – Parâmetros de Filtro
- `FILTRAR_HISTCOMPRAS_RCA = N` – Se `N`, mostra histórico de compras de todos os RCAs; se `S`, apenas do RCA logado.
- `FILTRAR_DADOS_RCA = N` – Mostra pedidos de todos os RCAs no cliente.
- `FILTRAR_DADOS_CONSULTA_POSITIVACAO_RCA = N` – Se `S`, na consulta de positivação, mostra apenas pedidos do RCA logado.
- `FILTRAR_DADOS_TITULOS_RCA = S` – `S` mostra títulos apenas do RCA logado; `N` mostra de todos.
- `GERAR_DADOS_MIX_CLIENTES_DIAS = 90` – Gera mix dos últimos 90 dias.
- `CATALOGO_PEDIDOS_DIAS_SYNC = 90` – Histórico de vendas dos últimos 90 dias.

### 7.7 Relatório Espelho do Pedido
- `EXIBIR_CAMPOS_ESPELHO_POR_EMBALAGEM = S` – Em conjunto com `EXIBIR_PRECO_UNIT_EMB`, exibe o campo "VL. UNIT EMB." mostrando o valor total da embalagem.

### 7.8 Imprimir Boleto no maxPedido
- `EXIBE_LINHA_DIGITAVEL = S` – Exibe a linha digitável do boleto na tela de título; ao clicar, gera PDF do boleto.

### 7.9 Previsão de Faturamento
Parâmetros:
- `OBRIGAR_PREVISAO_FATURAMENTO = N`
- `PRAZO_VALIDADE_PREVISAOFATURAMENTO = 30`
- `PREVISAO_FATURAMENTO_DIA_MAIS_UM = S`
- `CONSIDERAR_DATA_ATUAL_PREV_FAT = N`

### 7.10 Combos de Desconto – Links Úteis
- Configuração geral: [Como configurar Combo de Desconto](https://basedeconhecimento.maximatech.com.br/display/BMX/Como+configurar+Combo+de+Descontos)
- MIQ: [Como cadastrar Campanha MIQ](https://basedeconhecimento.maximatech.com.br/display/BMX/Como+cadastrar+Campanha+MIQ)
- SQP: [Como cadastrar Campanha SQP](https://basedeconhecimento.maximatech.com.br/display/BMX/Como+cadastrar+Campanha+SQP)
- MQT: [Como Cadastrar Campanha de Desconto MQT](https://basedeconhecimento.maximatech.com.br/display/BMX/Como+Cadastrar+Campanha+de+Desconto+MQT)
- FPU: [Como cadastrar Campanha FPU](https://basedeconhecimento.maximatech.com.br/display/BMX/Como+cadastrar+Campanha+FPU)

### 7.11 Tabelas de Permissões (Inspect)
- `MXSACESSODADOS` – Acesso às permissões da central (cobranças, planos de pagamento, filial de venda, etc.).
- `MXSACESSOENTIDADES` – Acesso da aba "acessos" nas permissões da central de configurações.

### 7.12 Venda Broker
- Referência: `MXPED-57813` (issue/chamado relacionado).

---

## 8. Catálogo de Parâmetros do maxPedido

Esta seção lista os principais parâmetros utilizados no maxPedido, com suas descrições, tipos e escopo. A configuração é feita na Central de Configurações > Configurações > Parâmetros.

### 8.1 Parâmetros de GPS e Localização
- **GPS_TRACKING_ENABLED**: Habilita a utilização do GPS e geração da base maxTracking, permitindo rastreamento dos RCAs. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GPS_TRACKING_INTERVAL**: Intervalo de envio de localizações (em segundos). Padrão é 5 segundos. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE**: Ao término da confecção de um pedido, questiona o usuário se deseja atualizar as coordenadas GPS do cliente. Atua com a permissão "SOLICITAR AUTORIZAÇÃO PARA ALTERAR COORDENADAS DO CLIENTE". (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GPS_IS_REQUIRED_CONFEC_PEDIDO**: Quando habilitado, não permite iniciar um pedido sem que o GPS esteja ativo. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GPS_EDGE_BLOCK**: Habilita a validação de cerca eletrônica. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GPS_EDGE_METERS_SIZE**: Define a tolerância da cerca eletrônica em metros. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GPS_TRACKING_STARTTIME**: Horário inicial do acompanhamento por GPS. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GPS_TRACKING_STOPTIME**: Horário final do acompanhamento por GPS. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GPS_UPDATE_COORDENADAS_SOMENTE_SE_NAO_PREENCHIDO**: Só altera as coordenadas do cliente se elas estiverem vazias. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.2 Parâmetros de Check-in/Check-out e Roteiro
- **UTILIZA_CHECKIN_CHECKOUT**: Habilita a funcionalidade de Check-in e Check-out no aplicativo. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **PERMITIR_PEDIDO_SEM_CHECKIN**: Permite realizar pedidos sem efetuar check-in para o cliente. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **OBRIGA_CHECKIN_CLIENTE_FORA_ROTA**: Obriga check-in se o cliente estiver fora do roteiro do dia. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **LIMITE_RAIO_CHECK_IN_OUT**: Define o raio (em metros) dentro do qual o check-in/out pode ser realizado. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **TEMPO_MIN_PERMANENCIA**: Tempo mínimo entre check-in e check-out (formato HH:MM). (Tipo: Literal, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **OBRIGAR_ATENDIMENTO_PARA_CHECKOUT**: Não permite check-out sem que tenha havido atendimento (pedido ou justificativa). (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **QTD_MAX_PED_FORA_ROTA**: Quantidade máxima de pedidos fora de rota aceitos. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **PERIODO_PED_FORA_ROTA**: Dias para zerar o contador de pedidos fora de rota. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_RCA_COM_ROTA_PENDENTE**: Bloqueia iniciar pedido se houver rotas pendentes do dia anterior. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_RETRO_DIAS_ROTEIRO**: Quantidade máxima de dias de atraso que podem ser visualizados no roteiro. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DIAS_ADIAMENTO_VISITA**: Limite de dias para adiamento de uma visita. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DIAS_ATENDI_ROTEIRO_SEMANAL**: Quantidade de dias que o RCA tem para atender a rota. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.3 Parâmetros de Bloqueio de Clientes e Pedidos
- **ACEITAVENDAAVISTACLIBLOQ**: Permite iniciar pedido para cliente bloqueado, mas só salva se for à vista e com cobranças específicas (Dinheiro, Cartão). (Tipo: Lógico, Escopo: Filial, Tabela: MXSPARAMFILIAL)
- **BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_BLOQ**: Bloqueia confecção de pedido se o cliente estiver bloqueado. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ**: Bloqueia pedido se o cliente principal (rede) estiver bloqueado. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO**: Permite ou bloqueia fazer pedidos quando o cliente da rede estiver bloqueado. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **CON_ACEITAVENDABLOQ** (Winthor): Bloqueia ou não venda para clientes bloqueados (configurado no ERP). (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMFILIAL)
- **HABILITA_CLIENTES_BLOQUEIO_DEFINITIVO**: Lista os clientes com bloqueio definitivo. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE**: Bloqueia pedido para cliente com títulos vencidos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQUEIA_PEDIDO_CLIENTE_SEMLIMITE**: Bloqueia pedido para cliente sem limite de crédito. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ALERTAR_TIT_VENCIDO**: Alerta o RCA, ao iniciar um pedido, se o cliente possui títulos vencidos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ALERTAR_TIT_INADIMPLENTE**: Alerta sobre títulos inadimplentes ao iniciar pedido. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **NUMERO_DIAS_CLIENTE_INADIMPLENTE**: Quantidade de dias que o cliente inadimplente terá o pedido bloqueado. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE**: Bloqueia pedido para cliente inadimplente. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.4 Parâmetros de Conta Corrente (CC/Flex)
- **CON_USACREDRCA**: Define se utiliza o processo de conta corrente. (Tipo: Lógico, Escopo: Filial, Tabela: MXSPARAMFILIAL)
- **EXIBIR_SALDOCC_DISPONIVEL**: Exibe o saldo de CC disponível. Se desabilitado, mostra "—". (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **APRESENTAR_CARD_CC**: Exibe o card de conta corrente na tela inicial, se o RCA usar CC. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GERAR_DADOS_CC_RCA**: Sincroniza movimentações de conta corrente (últimos 7 dias). (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DESCONTA_SALDOCCRCA_OFFLINE**: Define se pedidos bloqueados/pendentes (offline) influenciam no saldo de CC. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **IMPEDIR_ABATIMENTO_SEMSALDORCA**: Se 'N', permite debitar saldo de CC mesmo que negativo. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQUEAR_SALVAR_PEDIDO_SEMSALDORCA**: Bloqueia gravação de pedido se o RCA não tiver saldo de CC. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **PERMITE_INICIAR_PEDIDO_COMO_ORCAMENTO_NAO_MOV_CC**: Permite iniciar pedido como orçamento, que não movimenta CC. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_TODA_MOVIMENTACAO_CC**: Define se na aba de totais será exibida toda a movimentação de CC. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.5 Parâmetros de Estoque e Produtos
- **BLOQUEAR_INSERIR_ITEM_SEM_ESTOQUE**: Bloqueia inserção de item se não houver estoque. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQUEAR_VENDA_ACIMA_DO_ESTOQUE**: Impede venda de quantidade acima do estoque disponível. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DESABILITA_ALERTA_ESTOQUE**: Desabilita o alerta "Produto sem estoque suficiente". (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ENVIA_ESTOQUE_TODAS_FILIAIS**: Permite visualizar estoque de filiais que o RCA não tem acesso. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ENVIA_NOTIFICACAO_ESTOQUE_TODAS_FILIAIS**: Envia previsão de estoque de filiais sem acesso. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBE_ESTOQUE_FILIAL**: Permite visualizar estoque de outras filiais na opção '4- Inf.' do produto. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_ESTOQUE_BLOQUEADO**: Exibe o estoque bloqueado na listagem e no dialog de inserção. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_ESTOQUE_CONTABIL**: Exibe o estoque contábil na tela de inserção do produto. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBE_VALIDADE_PRODUTO_WMS**: Habilita visualização da validade de produtos WMS na opção '4- Info'. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ATIVAR_NOTIFICACAO_EMBALAGEM_MASTER**: Alerta que o produto possui embalagem master. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **USAR_MULTIPLO_QTDE**: Realiza cálculo da quantidade informada x múltiplo do produto. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **INICIA_QTDE_UM**: Define se sinaliza clientes sem compra há X dias. Trabalha com `QT_DIAS_SINALIZAR_CLIENTE`. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITAR_ARREDONDAMENTO_MULTIPLO**: Habilita opção de arredondamento para múltiplo. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **USA_EMBALAGEM_UNIDADE_PADRAO**: No processo de Fios, oculta a embalagem 'KG'. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_QUANTIDADE_SEM_FATOR_EMBALAGEM**: Faz a divisão da quantidade unitária pela quantidade da caixa. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITA_RECOMENDACAO_PRODUTOS**: Habilita recomendação de produtos por IA. Gera dados após 24h. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.6 Parâmetros de Pedido e Negociação
- **TRUNCAR_ITEM_PCPEDIDO**: Permite colocar o mesmo item várias vezes no pedido se 'S'. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **PERMITE_FILIAL_NF_NULA**: Aceita salvar pedidos sem Filial NF, que será idêntica à filial do cabeçalho conforme `COMPORTAMENTO_WHINTOR_FILIAL`. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GRAVAR_FILIAL_NF_NULO**: Se 'S' e não houver Filial NF no cliente/pedido, usa o preço da região do cliente. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **USA_FILIALNF_CLIENTE_PARA_DEFINIR_TRIBUTACAO**: Usa a filial de NF do cliente para definir tributação. (Tipo: Lógico, Escopo: Geral/Usuário/Filial, Tabela: MXSPARAMETRO)
- **FILIALNF_DEFINE_FILIAL_PEDIDO**: A filial de NF define a filial de venda. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **COMPORTAMENTO_WHINTOR_FILIAL**: Valida filiais de venda conforme comportamento do Winthor. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DEFINE_FILIAL_RETIRA_PADRAO**: Define a filial retira padrão para todos os produtos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EDITAR_VALOR_FRETE**: Permite editar o valor do frete no pedido. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITA_PED_CLI_NAO_SINC**: Permite fazer pedido para cliente recém-cadastrado, sem sincronizar com o ERP. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITA_PED_CLI_RECEM_CADASTRADO**: Permite iniciar pedido para clientes em pré-cadastro. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO**: Mostra pedidos do histórico na timeline de pedidos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITAR_DADOS_ENTREGA**: Habilita acompanhamento de entrega na timeline (requer maxMotorista). (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_ALTERACAO_PED_BONIFIC**: Bloqueia alteração de pedidos de bonificação (TV5) já salvos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DIAS_EDICAO_PEDIDO**: Quantidade de dias permitidos para editar um pedido. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ENVIA_PEDIDOS_BALCAO**: Envia histórico de pedidos de balcão. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ENVIA_PEDIDOS_CALL_CENTER**: Envia histórico de pedidos do call center. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ENVIA_PEDIDOS_TELEMARKETING**: Envia histórico de pedidos do telemarketing. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **INTERVALO_ENVIO_PEDIDOS_APK**: Intervalo em minutos para envio automático de pedidos. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.7 Parâmetros de Desconto e Campanhas
- **CON_ACEITADESCIPRECOFIXO**: Aceita aplicar desconto em política de preço fixo. (Tipo: Lógico, Escopo: Filial, Tabela: MXSPARAMFILIAL)
- **USAR_CAMPANHA_DESCONTO_PROGRESSIVO**: Ativa campanha de desconto progressivo. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **TIPO_DESC_PROGRESSIVO**: 'PRG' para campanha progressiva, 'PEG' para campanha P&G. (Tipo: Literal, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **APLICAR_CAMPANHA_DESCONTO_PRIORITARIA**: Questiona sobre aplicação de campanha de desconto prioritária (rotina 561). (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **VALIDAR_FILTRO_BRINDEX**: Valida restrições de brinde na tela de políticas de brinde. (Tipo: Lógico, Escopo: Usuário, Tabela: MXSPARAMETRO)
- **NOTIFICAR_PRODUTO_CAMPANHA_3306**: Notifica se o produto faz parte de campanha da rotina 3306. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.8 Parâmetros de Exibição e Relatórios
- **EXIBIR_PRECO_UNIT_EMB**: Exibe preço unitário no espelho do pedido. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **APRESENTAR_DESCONTOS_PEDIDO_EMAIL**: Exibe campos de desconto no espelho do pedido. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **OCULTAR_IMPOSTOS_PEDIDO_EMAIL**: Oculta impostos no espelho do pedido. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **OCULTAR_VALIDADE_PROPOSTA**: Oculta campo de validade da proposta no espelho. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_FOTO_DO_PRODUTO_PDF**: Exibe fotos dos produtos no layout padrão do espelho. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_FOTO_DO_PRODUTO_PERSONALIZADO_PDF**: Exibe fotos no layout personalizado. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DESABILITAR_ESPELHO_PED_PADRAO**: Se habilitado e houver layout customizado, não mostra o padrão. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBE_PREV_COMISSAO**: Exibe previsão de comissão na consulta de títulos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBE_SUGESTÃO_VENDA**: Exibe sugestão de venda. (Tipo: Lógico, Escopo: Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_SUGESTÃO_PRECO_COMISSAO**: Apresenta a diferença em reais da comissão conforme o desconto praticado. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_ALERTA_CREDITO_CLIENTE**: Exibe mensagem com o valor de crédito do cliente ao iniciar pedido. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIR_TAXABOLETO**: Informa se a taxa de boleto deve ser apresentada. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXIBIRTITULOSPAGOS**: Permite exibir títulos pagos na consulta. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITAR_SOMA_MULTA_TITULO**: Habilita soma da multa no saldo de títulos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **SOMAR_JUROS_TITULOS**: Soma o valor dos juros ao valor do título (automático). (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **APRESENTAR_MSG_POS_ENVIO**: Quando o RCA envia um recado, ele fica visível em Mensagens/Caixa de Saída. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_MARCAR_MSG_COMO_LIDA**: Bloqueia a opção "Marcar todas como lidas" em Mensagens. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **EXCLUIR_SOMENTE_LIDAS**: Impede exclusão de mensagens não lidas. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITAR_VISUALIZACAO_COD_FAB_PROD_TAB**: Exibe código de fábrica na listagem de produtos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **LIST_CLI_CPFCNPJ**: Mostra o CNPJ do cliente na listagem. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **OCULTAR_COMISSAO_MENU**: Oculta o menu de comissão na tela inicial. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_PERIODO_MENU_RCA**: Bloqueia a lupa de pesquisa (filtros) na tela de Resumo de Vendas. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.9 Parâmetros de Cadastro de Clientes
- **LISTAR_TODOS_PLANOS_PAGAMENTO**: Lista todos os planos de pagamento ao cadastrar um novo cliente. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ORDENACAO_PLANO_PAGAMENTO**: Ordena a lista de planos de pagamento. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DESATIVA_VALIDACAO_CNPJ_CADASTRADO**: Não valida se o cliente já existe por CNPJ/CPF no Winthor, permitindo salvar o cadastro do app. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **CLIENTESIMPLESNACIONAL_SIM**: Define se a opção "Cliente Simples Nacional" vem como "Sim" por padrão. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **CLIENTECONTRIBUINTE_SIM**: Define se "Cliente Contribuinte" vem como "Sim" por padrão. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DIAS_ATUALIZACAO_CADASTRO_CLIENTE**: Dias para considerar cadastro desatualizado (baseado em DTULALTER). Se > 0, questiona ou força edição. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **FORCAR_ATUALIZACAO_CADASTRO_CLIENTE**: Força a atualização do cadastro do cliente quando `DIAS_ATUALIZACAO_CADASTRO_CLIENTE` é atingido. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **DESABILITA_CADASTRO_PESSOA_FISICA**: Desabilita o cadastro de clientes pessoa física. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **FILTRAR_CLIENTES_CONSUMIDOR_FINAL**: Filtra se o RCA pode ver clientes consumidor final. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQUEIA_PRACA_PADRAO**: Bloqueia alteração de praça no cadastro de cliente. Trabalha com `COD_PRACA_PADRAO`. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **COD_PRACA_PADRAO**: Praça padrão para novos clientes. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.10 Parâmetros de Filtros de Dados
- **FILTRAR_DADOS_RCA_MIXVENDIDO**: Se 'S', filtra o mix do cliente por RCA. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **FILTRAR_DADOS_TITULOS_RCA**: 'S' mostra títulos apenas do RCA logado; 'N' mostra de todos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **FILTRAR_FILIAL_MIX**: Se 'S', só aparecem produtos da filial do pedido. Padrão 'S'. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ENVIAR_CLIENTES_RCA_9999**: Controla envio de clientes vinculados ao RCA 9999. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITA_ENVIAR_TODAS_AS_PRACAS_PARA_RCA**: Habilita envio de todas as praças. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **APENAS_TITULOS_FILIAIS_PERM**: Exibe títulos apenas das filiais permitidas. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **ENVIAR_APENAS_TITULOS_VENCIDOS**: Sobe para a nuvem apenas títulos vencidos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GERAR_DADOS_MIX_CLIENTES**: Gera dados de mix de clientes. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GERAR_DADOS_POS_CLIENTES**: Gera dados de positivação de clientes. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **GERAR_DADOS_POS_PRODUCTOS**: Gera dados de positivação de produtos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **AGRUPAR_RELPOSITIVCLIENTE_FORNEC**: Agrupa clientes positivados por fornecedor na consulta. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.11 Parâmetros de Sincronização e Bloqueio
- **BAIXAR_FOTOSPROD_APENAS_WIFI**: Baixa fotos de produtos apenas via Wi-Fi. Padrão: N. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMETRO)
- **BLK_CONN_CONSIDERAORCBLOQCOMOPEND**: Considera orçamento bloqueado como pendente para envio. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMETRO)
- **BLK_CONN_CONSIDERAPEDBLOQCOMOPEND**: Considera pedido bloqueado como pendente. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMETRO)
- **BLK_CONN_INTERVALOCONEXAO**: Intervalo entre conexões para bloquear novo pedido. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMETRO)
- **BLK_CONN_PRIMEIRACONEXAO**: Hora limite para efetuar a primeira sincronização. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMETRO)
- **BLK_CONN_QTDEORCPENDENTE**: Quantidade de orçamentos pendentes para bloquear novo. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMETRO)
- **BLK_CONN_QTDEPEDPENDENTE**: Quantidade de pedidos pendentes para bloquear novo. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMETRO)
- **BLK_SYNC_ROTEIRO_PENDENTE**: Alerta se houver clientes do roteiro não atendidos ao tentar sincronizar. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMETRO)
- **BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE**: Não deixa salvar pedido se ultrapassar limite de crédito e parâmetros de bloqueio. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_VENDA_FORA_HORARIO_COM**: Controla horários em que o RCA pode fazer pedidos. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_VENDA_FORA_HORARIO_COM_IM**: Hora de início da manhã (formato HHMM). (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_VENDA_FORA_HORARIO_COM_IT**: Hora de início da tarde. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_VENDA_FORA_HORARIO_COM_TM**: Hora de término da manhã. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQ_VENDA_FORA_HORARIO_COM_TT**: Hora de término da tarde. (Tipo: Numérico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **CONFIRMAR_PROCESSO_SYNC**: Pergunta se deseja realmente sincronizar ao clicar em "Comunicar". (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **HABILITAR_CONEXAO_SINC**: Habilita automaticamente uma rede (Wi-Fi/3G) para sincronizar e a desativa ao fim. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)
- **BLOQUEIA_ENVIO_ORCAMENTO_ERP**: Bloqueia envio de orçamento para o Winthor. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

### 8.12 Parâmetros Específicos Winthor
- **CON_PEREXCEDELIMCRED**: Percentual máximo para exceder o limite de crédito do cliente. (Tipo: Numérico, Escopo: Geral, Tabela: MXSPARAMFILIAL)
- **CON_CODPLPAGINCIAL**: Plano de pagamento padrão ao cadastrar clientes pelo força de vendas. (Tipo: Literal, Escopo: Geral, Tabela: MXSPARAMFILIAL)
- **CON_USATROACCOMPRECOVENDA**: Grava mercadorias a retirar com custo financeiro em trocas. (Tipo: Lógico, Escopo: Geral, Tabela: MXSPARAMFILIAL)
- **CON_VLMAXVENDAPF**: Valor máximo de pedidos para pessoa física no mês. (Tipo: Numérico, Escopo: Geral, Tabela: MXSPARAMFILIAL)
- **OBRIGATORIOVINCULARTV5COMTV1**: Obriga vínculo de pedido TV1 no pedido de bonificação. (Tipo: Lógico, Escopo: Filial, Tabela: MXSPARAMFILIAL)
- **PEDIR_AUTORIZACAO_TV5_VINCULADO_TV1**: Solicita aprovação do TV5 ao vincular um TV1. (Tipo: Lógico, Escopo: Geral/Usuário, Tabela: MXSPARAMETRO)

---

## 9. Mapeamento de Rotinas Winthor x Tabelas

Esta seção relaciona as principais rotinas do ERP Winthor com suas respectivas funcionalidades, módulos e tabelas envolvidas. É um guia de referência para consulta e entendimento da origem dos dados.

- **111 – Rotina de faturamento** (Módulo: Informações de Venda do Representante, Tabela: FUNC_RESUMOFATURAMENTO)
- **132 – Parâmetro que define média de desconto** (Módulo: Confecção de Pedidos, Tabelas: PCPARAMFILIAL / PCFILIAL)
- **146 – Resumo de Vendas** (Módulo: Informações de Venda do Representante, Tabela: PCMETASUP)
- **201 – Precificação de produto** (Módulo: Confecção de Pedidos, Tabela: PCTABPR)
- **203 – Cadastrar Produto** (Módulo: Rotinas Cadastros Básicos, Tabela: PCPRODUT)
- **238 – Manutenção do cadastro de produtos** (colocar múltiplo em filiais) (Módulo: Relacionamentos de Produtos, Tabela: PCPRODFILIAL)
- **283 – Cadastrar cotação de Concorrentes** (Módulo: Rotinas de Apoio, Tabela: PCCOTA)
- **285 – Analisar Cotação de Concorrentes** (Módulo: Rotinas de Apoio, Tabelas: PCCONCOR / PCCOTA)
- **292 – Cadastrar embalagem** (Módulo: Rotinas Cadastros Básicos, Tabela: PCEMBALAGEM)
- **297 – Produtos Similares** (Módulo: Relacionamentos de Produtos, Tabela: PCPRODSIMIL)
- **301 – Autorizar Preço de Venda** (Módulo: Confecção de Pedidos, Tabela: PCAUTORI)
- **302 – Cadastrar de clientes** (Módulo: Cadastrar de clientes, Tabela: PCCLIENT)
- **303 – Acompanhar Meta x Venda** (Módulo: Informações de Venda do Representante (Metas), Tabela: PCMETARCA)
- **308 – Alterar condição especial do cliente** (Módulo: Confecção de Pedidos, Tabela: PCPLPAGCLI)
- **309 – Cadastrar dias úteis de venda Produto** (Módulo: Rotinas Cadastros Básicos, Tabela: PCDATAS)
- **311 – Extrato, saldo do RCA** (Módulo: Informações de Venda do Representante, Tabelas: PCLOGRCA.VLCORRENTE / PCLOGRCA.VLCORRENTEANT)
- **313 – Cliente por RCA** (Módulo: Relacionamentos de Clientes, Tabelas: PCUSUARI / PCCLIENT)
- **317 – Imprimir Pedido** (Módulo: Confecção de Pedidos, Tabelas: PCPEDC / PCPEDI / PCMOV)
- **318 – Enviar Mensagem para RCA** (Módulo: Rotinas de Apoio, Tabela: PCMENS)
- **322 – Venda Por Departamento** (Módulo: Informações de Venda do Representante (Metas), Tabelas: PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...)
- **329 – Cancelamento do Pedido de Vendas** (Módulo: Confecção de Pedidos, Tabelas: PCNFCANITEM / PCNFCAN)
- **335 – Consultar Pedido de Venda** (Módulo: Confecção de Pedidos, Tabelas: PCPEDC / PCPEDI)
- **336 – Alterar Pedido de Vendas** (Módulo: Confecção de Pedidos, Tabela: PCVISITA)
- **344 – Consultar Visita** (Módulo: Relacionamentos de Clientes (Roteirização))
- **349 – Cadastrar Brindes** (Módulo: Relacionamentos de Produtos, Tabelas: PCPROMC / PCPROMI)
- **353 – Cadastrar Meta Diária por RCA (valor)** (Módulo: Informações de Venda do Representante (Metas), Tabelas: PCMETASUP / PCMETARCA)
- **354 – Cadastrar Rota de Visita e Cliente** (Módulo: Relacionamentos de Clientes (Roteirização), Tabela: PCROTACLI)
- **356 – Wizard de conta-corrente de RCA** (Módulo: Informações de Venda do Representante, Tabela: pc_pkg_controlarsaldorca (PCUSUARI))
- **357 – Cadastro preço fixo** (Módulo: Confecção de Pedidos, Tabela: PCPRECOPROM)
- **382 – Duplicar pedido de venda** (Módulo: Confecção de Pedidos, Tabelas: PCPEDC / PCPEDI) *(Rotina descontinuada, usar a 316)*
- **385 – Roteiro de visitas (cadastro de rotas)** (Módulo: Relacionamentos de Clientes (Roteirização), Tabelas: PCROTACLIFIXAC / PCROTACLIFIXAI)
- **387 – Desconto por quantidade** (Módulo: Confecção de Pedidos, Tabela: PCDESCQUANT) *(Rotina descontinuada, usar a 561)*
- **391 – Restrição de venda** (Módulo: Relacionamentos de Produtos, Tabela: PCRESTRICAOVENDA)
- **399 – Gerar Meta Mensal (Fornecedor - Sessão - Produto - Cliente)** (Módulo: Informações de Venda do Representante (Metas), Tabela: PCMETA)
- **407 – Rel. Fechamento de Carga** (Módulo: Pronta Entrega, Tabelas: PCPREST / PCCLIENT / PCCOB / PCMOVCR)
- **410 – Acertos** (Módulo: Pronta Entrega, Tabelas: PCCARREG / PCVEICUL)
- **417 – Mapa de Acerto** (Módulo: Pronta Entrega, Tabelas: PCMOV / PCNFSAID / PCPRODUT)
- **505 – Relacionar fornecedor por RCA** (Módulo: Relacionamentos de Produtos, Tabela: PCUSURFORNEC)
- **514 – Cadastro do tipo de tributação (acréscimo na tabela de pessoa física)** (Módulo: Confecção de Pedidos, Tabela: PCTRIBUTPARTILHA)
- **516 – Cadastrar Supervisor** (Módulo: Rotinas Cadastros Básicos, Tabela: PCSUPERV)
- **517 – Cadastrar RCA** (Módulo: Rotinas Cadastros Básicos, Tabela: PCUSUARI) *e também (Percentual Acréscimo/Desconto) no módulo Confecção de Pedidos.*
- **522 – Cadastrar tipo de cobrança** (Módulo: Rotinas Cadastros Básicos, Tabela: PCCOB)
- **523 – Cadastrar plano de pagamento** (Módulo: Rotinas Cadastros Básicos, Tabela: PCPLPAG)
- **528 – Cadastro de novos destinatários p/ envio de mensagem** (Módulo: Rotinas de Apoio, Tabela: PCEMPR)
- **530 – Permissões de acessos para cada usuário (usuário 8888)** (Módulo: Rotinas de Apoio)
- **535 – Cadastrar Filiais** (Módulo: Rotinas de Apoio, Tabela: PCFILIAL)
- **561 – Cadastrar política de Desconto** (Módulo: Confecção de Pedidos, Tabela: PCDESCONTO)
- **574 – Cadastrar tributação nos produtos** (Módulo: Relacionamentos de Produtos, Tabela: PCTRIBUT)
- **577 – Cadastrar Cidades e código IBGE** (Módulo: Relacionamentos de Clientes, Tabela: PCMOTNAOCOMPRA)
- **578 – Cadastrar Motivo de Não Compra** (Módulo: Relacionamentos de Clientes (Roteirização))
- **586 – Relacionamento Cliente X RCA** (Módulo: Relacionamentos de Clientes, Tabela: PCUSURCLI)
- **587 – Cadastrar Relacionamento de rca departamento e seção** (Módulo: Relacionamentos de Produtos, Tabela: PCUSURDEPSEC)
- **901 – Montar carga** (Módulo: Pronta Entrega, Tabela: PCCARREG)
- **904 – Cancelamento de carga** (Módulo: Pronta Entrega, Tabela: PCCARREG)
- **905 – Transferência de NFs do carregamento** (Módulo: Pronta Entrega, Tabela: PCNFSAID)
- **1203 – Extrato do cliente** (Módulo: Confecção de Pedidos, Tabela: PCPREST) *e também Tipo de cobrança, venda, plano padrão (Relacionamentos de Clientes, Tabela: PCCOBCLI)*
- **1213 – Títulos** (Módulo: Rotinas de Apoio, Tabelas: PCPREST / PCCLIENT / PCCOB / PCFILIAL)
- **1332 – Devolução pronta entrega (manifesto)** (Módulo: Pronta Entrega, Tabelas: PCTABDEV / PCNFBASE / PCMOV / PCNFENT)
- **1402 – Gerar Faturamento** (Módulo: Pronta Entrega, Tabela: PCCARREG)
- **2014 – Cadastrar embalagem (auto-serviço)** (Módulo: Rotinas Cadastros Básicos, Tabela: PCEMBALAGEM)
- **2316 – Digitar Pedido de Venda (medicamentos)** (Módulo: Confecção de Pedidos)
- **2323 – Cadastrar Promoção (Módulo Medicamentos)** (Módulo: Confecção de Pedidos, Tabela: PCPROMOCAOMED)
- **2500 – INTEGRADORA, APURARCAMPANHASBRINDES** (Módulo: Rotinas de Apoio, Tabelas: PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES, PROCEDURES, TRIGGERS, VIEWS)
- **3305 – Cadastrar Meta Mensal** (Módulo: Informações de Venda do Representante (Metas), Tabelas: PCMETA / PCMETAC)
- **3306 – Cadastrar campanha de desconto para Força de Vendas** (Módulo: Confecção de Pedidos, Tabelas: PCDESCONTOC / PCDESCONTOI / PCDESCONTORESTRICAO)
- **3307 – Cadastrar Cesta básica** (Módulo: Relacionamentos de Produtos, Tabela: PCFORMPROD)
- **3314 – Cadastrar Tab. De Preço Utilizada Pelo Cli** (Módulo: Relacionamentos de Clientes, Tabela: PCTABPRCLI)
- **3315 – Cadastro de RCA por Cliente** (Módulo: Relacionamentos de Clientes, Tabela: PCUISURCLI)
- **3320 – Cadastro de brinde Express** (Módulo: Relacionamentos de Produtos, Tabela: PCBRINDEEX)
- **3329 – Cadastro de tipos de Bonificações** (Módulo: Rotinas de Apoio, Tabela: PCTIPOBONIFIC)
- **Total cadastro de cotas por RCA** (Módulo: ?, Tabela: PCPRODUSUR)

---

## 10. Roteirização Complementar e Diagnóstico de Rotas

**Descrição**: Esta seção consolida conteúdos complementares sobre criação e edição de rotas no aplicativo, além de cenários de troubleshooting relacionados a roteiro, visita avulsa e mapa de oportunidades.

### 1. Cadastro e Edicao de Rota no Aplicativo

#### 1.1. Configuracao de Parametros

Para habilitar o cadastro e edicao de rotas no aplicativo do maxPedido, e necessario configurar parametros na Central de Configuracoes.

##### Passos para Configuracao

1. Na Central de configuracoes, acesse Menu lateral > Configuracoes > Parametros
2. Busque pelo parametro `HABILITA_CADASTRO_ROTA_CLIENTE` e clique em pesquisar
3. Clique no icone de edicao da coluna Acoes, marque para habilitar e salve
4. Ainda na tela inicial da Central, clique em Configuracoes > Configuracoes > Aba Formularios > Clientes
5. Verifique se em Roteiro de visita a opcao "Ocultar Ambos" esta desmarcada

##### Observacoes Importantes

- O parametro `HABILITA_CADASTRO_ROTA_CLIENTE` habilita o cadastro de rotas durante o cadastro ou edicao do cliente no aplicativo do Pedido de Vendas
- Deve estar marcado para que a aba de Roteiro de Visitas apareca para ser alterada
- Caso a opcao de Ocultar em Ambos estiver marcada, nao sera possivel realizar cadastro e edicao de rota no aplicativo mesmo que o parametro estiver habilitado, pois ela estara oculta para o vendedor

#### 1.2. Criar Rota para Novo Cadastro de Cliente

1. Na tela de clientes, clique no icone de adicionar para criar novo cadastro (fica na barra superior da tela)
2. Na aba Roteiro de Visitas, preencha os dados solicitados
3. Apos preenchimento de todas as informacoes, clique no icone de salvar que fica no canto direito superior da tela

##### Campos do Roteiro de Visitas

| Campo | Descricao |
|-------|-----------|
| Data inicial | Data de inicio da geracao de roteiros |
| Data final | Data de termino da geracao de roteiros |
| Data da proxima visita | A primeira data apos o cadastro quando devera ocorrer a visita |
| Numero da semana | Escolha em qual semana deve ocorrer a visita |
| Periodicidade | Intervalo em dias que deverao ocorrer as visitas, normalmente a cada 7 dias |

#### 1.3. Editar Rota no Cadastro de Cliente

1. Na tela inicial do maxPedido Aplicativo, selecione a aba Clientes
2. Clique longo no cliente desejado
3. Selecione a opcao Editar Cliente
4. Confirme para editar o cadastro do cliente
5. Clique na aba Roteiro de Visitas e altere as informacoes conforme necessidade

---

---

### 7. Solucao de Problemas Comuns

#### 7.1. Roteiro Nao Aparece no Aplicativo

**Possiveis causas:**
- Roteiro nao esta cadastrado no ERP para o dia selecionado
- Cliente nao pertence a carteira do vendedor
- Parametro `HABILITA_CADASTRO_ROTA_CLIENTE` nao esta habilitado
- Opcao "Ocultar Ambos" esta marcada na configuracao de formularios

**Solucao:**
- Verifique o cadastro de rotas no ERP
- Confirme a atribuicao de clientes ao vendedor
- Valide as configuracoes de parametros e formularios

#### 7.2. Nao Consegue Criar Visita Avulsa

**Possiveis causas:**
- Usuario nao possui permissao "Habilitar criacao de visita avulsa"
- Parametro de check-in obrigatorio pode estar impedindo

**Solucao:**
- Verifique e habilite a permissao no cadastro do usuario
- Ajuste o parametro `OBRIGA_CHECKIN_VISITA_AVULSA` conforme necessidade

#### 7.3. Mapa de Oportunidades Nao Mostra Prospects

**Possiveis causas:**
- Parametro `HABILITA_MAPA_OPORTUNIDADE` nao esta habilitado
- Configuracao de distancia ou CNAEs muito restritiva
- Nao ha prospects no raio configurado

**Solucao:**
- Habilite o parametro na central de configuracoes
- Ajuste os parametros de distancia e CNAEs no perfil de usuario
- Amplie o raio de pesquisa se necessario

---

**Documento compilado a partir de:** BMX-72024605, BMX-ComotrabalharcomVisitaAvulsanomaxPedido, BMX-ComotrabalharcomMapadeOportunidades, MAXPED-ComotrabalharcomRoteirodeVisitanoAplicativo, MAXPED-ComovisualizarroteirodeoutrosdiasnomaxPedido, BMX-9470417, BMX-9470423, BMX-9470427, BMX-9470431, BMX-9470439, BMX-9470443

**Ultima atualizacao:** Fevereiro 2026

---

## 11. MaxGestão — Operação, Usuários, Vendas e Geolocalização

**Descrição**: Conteúdo consolidado do MaxGestão, mantendo a organização original do documento-fonte e integrado à base principal para consulta unificada.

### 1. Visão Geral do MaxGestão

O MaxGestão é um portal web e aplicativo destinado a gestores e administradores que utilizam as soluções da Máxima Tech. Ele permite acompanhar o desempenho dos vendedores (RCAs), traçar rotas, visualizar relatórios de performance, gerenciar autorizações de pedidos, controlar contas correntes dos vendedores, monitorar geolocalização em tempo real e muito mais. Está disponível nas versões Web (PWA) e aplicativo mobile para Android e iOS.

---

### 2. Acesso e Instalação

#### 2.1 Acesso via Navegador (PWA)

O MaxGestão pode ser acessado diretamente pelo navegador através do link:
```
https://maxgestao-pwa.solucoesmaxima.com.br
```

A partir da versão PWA, o aplicativo é compatível com Android e iOS, podendo ser instalado na tela inicial do dispositivo.

#### 2.2 Instalação no Android

1. Acesse o link acima pelo navegador Chrome.
2. Faça o login com suas credenciais.
3. Após o login, você será redirecionado para uma tela com instruções de instalação.
   - **Importante:** Se o usuário optar por não instalar, ficará retido nesta tela.
4. Siga as orientações: clique no ícone de compartilhamento (ou menu) e selecione "Adicionar à tela inicial".
5. Confirme a instalação clicando em "Instalar".
6. Após a instalação, o aplicativo aparecerá na barra de notificações e estará disponível na tela inicial.

#### 2.3 Instalação no iOS

1. Acesse o link pelo navegador Safari.
2. Faça o login.
3. Siga as instruções na tela: clique no ícone de compartilhamento (parte inferior) e selecione "Adicionar à Tela de Início".
4. Confirme o nome do aplicativo (padrão: "maxGestão") e clique em "Adicionar".
5. O navegador será fechado e o aplicativo estará disponível na tela inicial.

#### 2.4 Primeiro Acesso e Termos de Uso

- Ao abrir o aplicativo pela primeira vez, será necessário fazer login novamente.
- Após o login, uma tela de **Termos de Uso** (LGPD) será exibida. O usuário deve aceitar os termos para prosseguir.

#### 2.5 Notificações

- Após aceitar os termos, o sistema perguntará se o usuário deseja habilitar notificações.
- **Importante:** Uma vez recusada, a habilitação não pode ser reativada. Recomenda-se permitir.
- No iOS, a opção de notificações aparece apenas em versões 16.4 ou superiores. Em versões anteriores, deve ser configurada manualmente nas configurações do dispositivo.
- Após permitir, uma tela de confirmação é exibida e o aplicativo está pronto para uso.

---

### 3. Cadastro e Gerenciamento de Usuários

#### 3.1 Cadastro de Usuários no maxSoluções

O cadastro de usuários é feito no portal maxSoluções:

1. Acesse o maxSoluções e clique em **Cadastros** no menu lateral.
2. Clique em **Usuários** e depois em **Novo usuário**.
3. Escolha o **Tipo de usuário**:
   - **Administrador:** terá acesso a todos os cadastros, liberação de versão, relatórios, etc.
   - **Usuário normal:** acesso restrito conforme permissões concedidas.
4. Preencha os dados do usuário e clique em **Salvar**.

#### 3.2 Liberação de Versão

Após criar o usuário, é necessário liberar a versão do MaxGestão para que ele tenha acesso:

1. No maxSoluções, clique em **Liberar Versão** no menu lateral e depois em **Novo**.
2. Em **Rotina/Versão**, selecione a opção **5 - maxGestão** para a versão Web.
3. Selecione os usuários desejados e clique em **Salvar**.
4. Confirme a liberação.
5. Repita o processo para a versão do aplicativo (rotina **20 - maxGestão**).

**Data Limite de Atualização:** pode ser definida para forçar os usuários a atualizarem para uma nova versão.

#### 3.3 Acesso ao Cadastro de Usuários no MaxGestão

1. No maxGestão, clique no ícone de menu e depois em **Cadastro de usuários**.
2. Serão listados todos os usuários cadastrados no maxSoluções.
3. No final da linha de cada usuário, há o ícone de edição para ajustar permissões e configurações.

#### 3.4 Perfis de Usuários

É possível criar perfis para facilitar a gestão de permissões:

1. Em **Cadastro > Perfil de usuários**, clique no ícone de adição.
2. Preencha os dados do perfil e configure as permissões (acesso a rotinas e acesso a dados).
3. Na aba **Configurações**, defina limites de desconto, lucratividade e valor máximo de pedido bonificado que o perfil pode autorizar.
4. Após salvar, os usuários vinculados a esse perfil herdarão as mesmas permissões.

#### 3.5 Permissões de Acesso

Ao editar um usuário ou perfil, há dois quadros de permissões:

##### 3.5.1 Quadro "Selecione acesso de rotinas"

Permissões relacionadas a funcionalidades do sistema que o usuário pode visualizar/alterar. Exemplos:
- **Administração:** Configurações do sistema, cadastro de perfis/usuários, controle de autorização de pedidos, etc.
- **Mapas:** Acesso à localização dos vendedores, trajetos e ações.
- **Painéis:** Acesso ao Painel Geral e Orçamento x Vendas, com subpermissões para cada card.
- **Inteligência Geográfica:** Mapa de oportunidades.
- **Relatórios:** Vendas, Comercial, Logística, Financeiro (cada relatório com suas ramificações).

##### 3.5.2 Quadro "Acesso a dados"

Permissões relacionadas a informações da empresa:
- **Planos de pagamento, Cobranças, Departamentos, Seções, Equipes, Filiais, Regiões, Fornecedores, Conta corrente**.
- Marcando um item, o usuário terá acesso àquela entidade. Isso afeta resultados, autorizações e relatórios.

##### 3.5.3 Permissões Específicas

- **Conta corrente:** subpermissões para acesso básico, alterar limite, lançar crédito/débito, transferir saldo.
- **Controle de autorização de pedidos:** subpermissões para debitar da conta corrente, habilitar opção "Sim" para débito automático.

#### 3.6 Ocultar Cards / Painéis

1. Em **Cadastro > Usuários** ou **Perfil de usuários**, edite o usuário/perfil.
2. Na aba **Permissões > Acesso a Rotinas > Painéis**, desmarque os cards que não devem ser visualizados.
3. Para que a ocultação funcione, é necessário habilitar o parâmetro **Ocultar Menus quando não houver permissão de acesso** em **Configurações do sistema > Configurações Gerais**.

---

### 4. Acompanhamento de Vendas e Desempenho

#### 4.1 Dashboard – Resumo de Vendas

1. No menu lateral, clique em **Dashboard**.
2. O gráfico **Resumo de vendas** exibe:
   - Resultados de vendas
   - Devoluções
   - Comissões
3. É possível marcar/desmarcar as legendas para adaptar a visualização.
4. O gráfico permite aproximação e, no canto superior direito, há um ícone para agrupar os dados por período mensal.

#### 4.2 Evolução de Vendas

- Gráfico que compara as vendas do período anterior com o atual.
- Permite marcar para mostrar um ou outro separadamente.
- Também possui aproximação e agrupamento mensal.
- Clicando no gráfico, exibe o valor da venda do mês anterior e do atual, conforme o filtro.

#### 4.3 Posição dos Pedidos

- Gráfico com a posição dos pedidos: pendentes, liberados, faturados, bloqueados, montados, cancelados.
- Possui legenda em cores e permite marcar para mostrar apenas um tipo de posição.

#### 4.4 Filtros para Análise

No canto superior direito, o ícone de filtro permite:
- Data de emissão ou data de faturamento
- Equipe
- Representante
- Período (início/fim)
- Filial
- Tipo de venda
- Deduzir devoluções, ST, IPI, bonificação

Para data de emissão, há opções adicionais: todos os pedidos, apenas faturados ou apenas não faturados.

#### 4.5 Indicadores da Equipe no Aplicativo

No aplicativo maxGestão, a tela inicial exibe:
- Valor total de vendas
- Devoluções
- Quantidade de pedidos
- Quantidade de itens
- Toneladas e cubagem
- Status dos pedidos na nuvem (parados, bloqueados, aguardando autorização, autorizados, recusados)
- Status dos pedidos no ERP (importados, aprovados, com erro)
- Status de entregas (no caminhão, em trânsito, entregues)

**Importante:** Para que esses dados apareçam, o usuário deve ter permissão para acessar os painéis (configurado no maxGestão Web).

#### 4.6 Rankings e Mapas

- **Ranking de supervisores e vendedores:** exibe resultado em valor e percentual. Clique em "Ver mais" para expandir.
- **Ranking por fornecedor, departamento, seção, categoria:** role a tela para baixo e alterne entre as abas.
- **Mapa dos vendedores:** mostra a localização em tempo real (requer GPS habilitado no app de vendas).
- **Mapa de calor de vendas:** indica regiões com maior intensidade de vendas (vermelho = alta, verde = baixa).

---

### 5. Geolocalização e Mapas

#### 5.1 Acessando os Mapas

1. No menu lateral do maxGestão, clique em **Geolocalização > Mapas**.
2. O mapa será aberto mostrando os ícones dos vendedores.

#### 5.2 Visualização da Posição do Vendedor

- Aumente o zoom para ver a localização exata.
- Ao selecionar um vendedor, é possível:
  - Ver cliente: consultar endereço da casa do vendedor (ponto de partida).
  - Se não houver endereço cadastrado, o sistema sugere a configuração.
- Para cadastrar/editar o endereço do vendedor, clique no ícone de configuração no mapa e depois no ícone de edição.

#### 5.3 Clientes Visitados e Positivados Fora da Agenda

- No card do vendedor (tela inicial ou no mapa), ao clicar no ícone do vendedor, é exibida uma janela com:
  - Clientes visitados fora da agenda
  - Clientes positivados fora da agenda

#### 5.4 Visualizando Clientes do Vendedor

- No mapa, clique no ícone do vendedor e depois em **Ver cliente**.
- Os clientes do vendedor aparecerão no mapa.
- Clique em um cliente para ver seus dados.

#### 5.5 Ícones e Legendas

No canto superior direito do mapa, clique no ícone de informações para abrir a legenda com os significados dos ícones e cores.

#### 5.6 Trajeto Planejado e Executado

- Após selecionar um vendedor e clicar em **Ver cliente**, no canto superior esquerdo é possível escolher:
  - **Trajeto planejado:** mostra a rota planejada para o dia.
  - **Trajeto executado:** mostra o trajeto real percorrido.
- Para o trajeto executado, um ícone no canto inferior direito abre uma janela com todas as ações em ordem cronológica.

#### 5.7 Informações de Clientes no Trajeto Executado

Ao selecionar um trajeto executado, as informações do cliente (razão social, fantasia, endereço, telefone, data da venda, observações) são exibidas.

#### 5.8 Comparação entre Trajeto Planejado e Executado

- Marque ambas as opções (planejado e executado) para visualizar os dois trajetos no mapa.
- Ícones no canto inferior direito abrem janelas com os detalhes de cada um, permitindo comparar se o executado corresponde ao planejado.

#### 5.9 Exibição dos Clientes no Mapa

- Após selecionar um vendedor e clicar em **Ver cliente**, os clientes são exibidos no mapa.
- Se a posição do cliente não estiver correta, é necessário verificar o cadastro de latitude/longitude e endereço no ERP.

#### 5.10 Filtros no Mapa

No canto superior direito, o ícone de filtro permite pesquisar por:
- Equipe
- Representante
- Data
- Positivação (positivados ou não positivados)
- Tipo de cliente (pessoa física ou jurídica)

#### 5.11 Linha do Tempo do Roteiro Executado

- No mapa, selecione um vendedor e marque **Trajeto executado**.
- No canto inferior direito, um ícone abre uma janela com a linha do tempo das ações, em ordem cronológica, com ícones representativos e descrições. Abaixo de cada evento, constam o nome do cliente e endereço.

#### 5.12 Acurácia das Coordenadas

##### 5.12.1 O que é Acurácia

Acurácia é a medida da proximidade entre as coordenadas capturadas e as coordenadas reais, expressa em metros. Quanto menor o valor, mais precisa é a captura.

##### 5.12.2 Como é Calculada

A acurácia é calculada em metros. Por exemplo, se o rastro tem acurácia 100, significa que a latitude/longitude pode estar em qualquer ponto dentro de um raio de 100 metros.

##### 5.12.3 Como Funciona a Captura das Coordenadas

- A API do Google retorna a captura, que é armazenada no banco de dados da Máxima.
- O tempo de coleta padrão é de 5 segundos (mínimo), podendo ser aumentado por parametrização.
- O percentual de confiabilidade da Google é de 68% combinado com a acurácia.

##### 5.12.4 Fatores que Comprometem a Captura Precisa

**Hardware:**
- Tipo de GPS do aparelho (AGPS, GLONASS, BEIDOU, GALILEO). Alguns aparelhos usam múltiplas tecnologias.

**Software:**
- Modo avião ativado
- Cobertura da operadora (triangulação de rede móvel)
- Wi-Fi desativado
- Bluetooth desativado
- Versão do Android (a partir da versão 10, as permissões são mais complexas)
- Versão do Google Play Services (mínimo 11.6)
- Economia de bateria ativada
- A partir do Android 8, a Google limita a quantidade de acessos à API de rastro
- No Android 12, há opção de fornecer localização aproximada em vez de exata
- Forçar a parada do aplicativo interrompe a captura

**Ambiente:**
- Região de captura (prédios, pontes, locais subterrâneos)
- Fatores climáticos

##### 5.12.5 Verificação no Painel de Auditoria

No Painel de Auditoria do maxGestão Web, é possível visualizar as colunas:
- **Acurácia:** precisão da captura.
- **Margem de erro:** calculada com base na acurácia, indicando uma faixa de variação para o KM total.

---

### 6. Painel de Auditoria

#### 6.1 Acesso

1. No maxGestão, menu lateral > **Geolocalização > Painel de Auditoria**.

#### 6.2 Legendas

No canto superior direito, clique no ícone de informações para ver as legendas dos ícones da página.

#### 6.3 Visualização por Filial

1. Em **Filtros avançados**, selecione Filial, data inicial e final.
2. Clique em Pesquisar.
3. Para personalizar as colunas, clique no ícone de configuração e depois em **Configuração de exibição**.
4. Marque/desmarque as informações desejadas e clique em Salvar.

#### 6.4 Visualização por Supervisor

1. Em **Filtros avançados**, selecione Filial, Gerente, Coordenador, Supervisor, data inicial e final.
2. Pesquise e personalize a exibição.

#### 6.5 Visualização por Vendedor (RCA)

1. Em **Filtros avançados**, selecione Filial, Gerente, Coordenador, Supervisor, Representante, data inicial e final.
2. Pesquise e personalize.
3. Para uma visão diferente, clique no ícone de alternar visualização no canto inferior direito. Isso exibe os resultados separados por RCA. Clique novamente para voltar.

#### 6.6 Informações de Clientes no Painel de Auditoria

- Após a pesquisa por RCA, na coluna Ações, clique no ícone correspondente ao RCA.
- Abrirá uma janela com dados do RCA, ações realizadas e clientes agendados.

#### 6.7 KM Total x KM Trabalhado

- **KM Total:** todo trajeto percorrido.
- **KM Trabalhado:** por padrão, do primeiro ao último cliente da agenda.
- Para usar ponto inicial/final do roteirizador: acesse **Configurações do sistema > Configurações Gerais** e marque **Utilizar ponto inicial/final do Roteirizador**.

#### 6.8 Usuários Inativos

- Para incluir usuários inativos nos filtros, em **Configurações do sistema > Painel de auditoria**, habilite **Habilitar usuários inativos**.

#### 6.9 Visualização de Agendamento

- No filtro avançado, a opção **Remover agendamentos excluídos**:
- Marcada: mostra apenas agendamentos ativos.
- Desmarcada: mostra todos, incluindo excluídos.
# Base de Conhecimento MaxGestão – Documento Completo e Autocontido (continuação)

### 7. Conta Corrente do RCA no MaxGestão

#### 7.1 Acesso para Supervisor Movimentar Conta Corrente

1. Na página inicial do maxGestão, clique no ícone de menu no canto superior direito e selecione **Cadastros de Usuários**.
2. Localize o supervisor desejado e clique no ícone de edição na linha correspondente.
3. Na aba **Permissões**, localize a seção **Conta Corrente**.
4. Habilite as permissões necessárias:
   - **Acesso Básico** – permite visualizar a gestão de conta corrente.
   - **Alterar limite de Crédito** – permite modificar o limite de crédito do RCA.
   - **Lançar Crédito** – permite adicionar crédito à conta do RCA.
   - **Lançar Débito** – permite debitar valores da conta do RCA.
   - **Transferência de saldo** – permite transferir saldo entre RCAs.

#### 7.2 Configurar Saldo de Conta Corrente do RCA

1. No menu principal, acesse **Conta Corrente > Gestão de Conta Corrente**.
2. A tela exibe a lista de RCAs com seus respectivos saldos e limites.
3. Para lançar crédito ou débito para um RCA específico:
   - Clique no ícone de ação (lápis ou similar) na linha do RCA.
   - Será aberta uma janela para lançamento.
   - Informe o valor e o tipo de movimentação (crédito/débito).
   - Clique em Salvar.
4. Esta ação altera o saldo apenas do RCA selecionado.

#### 7.3 Busca por Equipe ou Representante

No canto superior direito da tela de Gestão de Conta Corrente, clique no ícone de filtro. É possível marcar as equipes (supervisores) e RCAs desejados para refinar a consulta.

#### 7.4 Transferência de Saldo entre RCAs

1. Na Gestão de Conta Corrente, na última coluna da linha do RCA de origem, clique no ícone de transferência (seta dupla ou similar).
2. Será aberta uma janela com os dados do RCA de origem e seu saldo disponível.
3. Preencha:
   - **RCA de destino** – selecione o RCA que receberá o saldo.
   - **Valor a transferir** – informe o montante.
   - **Motivo** – descreva o motivo da transferência.
4. Clique em **Salvar** para concluir.

**Observação:** Não é possível transferir saldo de supervisor para vendedor, apenas de vendedor para vendedor.

#### 7.5 Relatório do Saldo da Conta Corrente

- **Para um RCA específico:** Na linha do RCA, clique no ícone de impressão. Escolha entre:
  - **Relatório Sintético** – resumo do saldo.
  - **Relatório Analítico** – detalhamento das movimentações.
  - Ambos.
- **Para múltiplos RCAs:** No canto inferior direito da tela, clique no ícone de impressão em massa. Selecione os RCAs desejados marcando as caixas correspondentes e escolha o tipo de relatório.
- Para relatórios analíticos, é possível informar:
  - Data inicial e final
  - Filtrar por número de pedido
  - Filtrar por código do cliente
  - Ordenar por pedidos

---

### 8. Autorização de Pedidos

#### 8.1 Objetivo

A autorização de pedidos permite que o supervisor analise e aprove (ou rejeite) pedidos que estão fora das condições padrão, como:
- Desconto acima do permitido
- Margem de lucratividade abaixo do mínimo
- Venda bonificada
- Cliente bloqueado ou com limite de crédito excedido

O supervisor pode, durante a autorização:
- Debitar o valor do pedido (ou de itens específicos) da conta corrente do RCA.
- Alterar a comissão do item.
- Definir porcentagens de autorização conforme hierarquia.

#### 8.2 Acesso aos Pedidos Aguardando Autorização

- **Via notificação:** Clique no ícone de sino (notificações) no canto superior direito. Uma janela exibirá alguns pedidos pendentes. Clique em "Ver todas as notificações" para acessar a tela completa.
- **Via menu:** Na página principal, clique no menu lateral e depois em **Autorizações > Autorização de pedidos**.

#### 8.3 Interface da Tela de Autorização

A tela exibe um grid com as seguintes colunas:
- Número do pedido
- Código do cliente
- Nome do cliente / Razão social
- VIP (classificação do cliente)
- Data do pedido
- Data de envio para aprovação
- RCA
- Supervisor
- Filial
- Plano de pagamento
- % de desconto do pedido
- % de lucratividade
- Valor atendido
- Motivo da autorização
- Usuário que autorizou

É possível reorganizar as colunas arrastando seus cabeçalhos.

No canto direito da tela, há ícones para:
- **Configurar exibição** – escolher quais colunas aparecem.
- **Ajustar intervalo de atualização** – definir a frequência de refresh da tela.
- **Exportar dados** – gerar arquivo CSV com as informações do grid.

#### 8.4 Configurar Usuário para Autorizar Pedidos

1. No menu principal, acesse **Cadastro > Usuários**.
2. Role a tela horizontalmente até o final e clique no ícone de editar do usuário desejado.
3. Na aba **Acesso a rotinas**, localize **Administração** e expanda.
4. Marque a opção **Controle de autorização de pedidos**.
5. (Opcional) Dentro dessa opção, é possível marcar subpermissões, como **Debitar da conta corrente do RCA**.

#### 8.5 Configurar Débito em Conta Corrente na Autorização

Ainda na tela de permissões do usuário, dentro de **Controle de autorização de pedidos**, há a opção **Debitar da conta corrente do RCA**. Marque-a para que o supervisor possa optar por debitar o valor do pedido da conta do vendedor ao autorizar.

#### 8.6 Configurar Percentuais de Desconto e Lucratividade

1. Em **Cadastro > Usuários**, edite o usuário.
2. Na aba **Configurações**, é possível definir:
   - **Máximo de desconto permitido em autorização de pedido**
   - **Mínimo de lucratividade permitido em autorização de pedido**
   - **Valor máximo do pedido bonificado que o usuário pode autorizar**
   - **Valor máximo de pedido com troca**

Esses valores são aplicados diretamente ao gestor para limitar o que ele pode aprovar.

#### 8.7 Aceitar ou Rejeitar Pedidos

- Na tela de autorização, os pedidos pendentes são exibidos na aba "Pendentes".
- Para aceitar ou rejeitar rapidamente, arraste o pedido para a direita: aparecerão os ícones de aceitar (check) e rejeitar (x).
- Para mais detalhes, clique no ícone de informação (i) ao lado do pedido. Será aberta uma janela com os itens do pedido.
- Na janela de detalhes, é possível:
  - Visualizar cada item com nome do produto, preço de tabela, preço autorizado, preço mínimo, % de desconto autorizado, % lucratividade e % comissão.
  - Ajustar a % de comissão do vendedor (deve ser menor que a informada no pedido e positiva).
  - Aceitar ou rejeitar o pedido.

#### 8.8 Status "Pendente" na Autorização

O sistema permite que o supervisor coloque um pedido em status "pendente" para análise posterior.

**Configuração:**
1. Clique no ícone de configurações no canto superior direito e acesse **Configurações Gerais**.
2. Habilite o parâmetro **Utiliza status pendente na autorização de Pedido**.
3. Opcionalmente, habilite **Editar período máximo de duração para pedidos pendentes** e defina o prazo em dias.

**Uso:**
- Na tela de autorização, ao lado do pedido, aparecerá o ícone de pendente (relógio ou similar).
- Clicando nele, é possível inserir observações sobre o motivo do status.
- No filtro avançado, há a opção "Solicitações pendentes" para visualizar apenas esses pedidos.
- Se o parâmetro for desabilitado, todos os pedidos pendentes serão automaticamente rejeitados (o sistema exibirá um alerta antes de confirmar).

#### 8.9 Debitar Saldo do Vendedor por Item

1. Ao clicar em aceitar um pedido, abrirá uma janela com as seguintes opções:
   - **Observações da autorização**
   - **Debitar da conta corrente do RCA** – se marcado, o valor total do pedido será debitado.
   - **Produtos para Débito** – se a opção anterior não estiver marcada, é possível selecionar itens específicos para débito.
2. A opção de debitar só estará disponível se o usuário tiver a permissão correspondente e se o pedido não for bonificado com o parâmetro `CON_BONIFICALTDEBCREDRCA` desabilitado (rotina 132 do Winthor). Nesse caso, a flag fica desabilitada.

#### 8.10 Autorização para Cliente Bloqueado ou com Limite Excedido

- No filtro avançado da tela de autorização, é possível pesquisar por motivos como "Cliente bloqueado" ou "Limite de crédito excedido".
- Os pedidos com esses motivos aparecem na lista e podem ser autorizados ou rejeitados normalmente.
- Essa funcionalidade permite que o vendedor envie pedidos para clientes bloqueados ou sem limite, e o supervisor decida se aprova.

#### 8.11 Motivos de Rejeição

##### 8.11.1 Configuração

1. No maxGestão Web, clique no ícone de configurações no canto superior direito.
2. Na aba **Configurações Gerais**, marque a opção **Utilizar motivos de rejeição de pedido**. Sem essa opção, a aba de cadastro de motivos não fica disponível.
3. Conceda permissão ao usuário ou perfil:
   - Em **Cadastro > Usuários** ou **Perfil de usuários**, edite.
   - Na aba **Permissões > Acesso a rotinas**, em **Administração**, marque **Cadastrar Motivos de Rejeição**.
4. No menu lateral, acesse **Cadastro > Motivos Rejeição de Pedido**.
5. Clique no ícone de adição no canto inferior direito, insira o nome do motivo e clique em Salvar.

##### 8.11.2 Uso no Aplicativo

- No aplicativo maxGestão, ao rejeitar um pedido pendente, será aberta uma janela para selecionar o motivo da rejeição.
- Após rejeitar, na aba "Rejeitados", o motivo informado será exibido junto com as demais informações do pedido.

---

### 9. Jornada de Trabalho

#### 9.1 Acesso

No menu lateral do maxGestão, acesse **Jornada de trabalho > Cadastro de horários**.

#### 9.2 Criando e Alterando Horários

- A tela exibe uma grade com os horários já cadastrados, contendo: **Código**, **Descrição** e **Ações** (editar, excluir).
- Para criar um novo horário, clique no ícone de adição no canto inferior direito.
- Na tela de cadastro, preencha os campos necessários (ex.: descrição, hora de início, hora de fim, intervalo). É importante criar horários separados para cada período da jornada (manhã, tarde, intervalo).
- Após preencher, clique em **Adicionar** para gravar na grade.
- Repita o processo para todos os horários necessários.
- Ao final, clique em **Salvar** e escolha a opção desejada (continuar ou sair).

#### 9.3 Montando a Jornada de Trabalho

1. Acesse **Jornada de trabalho > Cadastro de Jornada**.
2. Na primeira vez, será exibido um termo de uso da LGPD. Após aceitar, a tela é liberada.
3. A tela exibe as jornadas já cadastradas com as colunas: Código, Nome, Dias úteis, Horas Semanais, Impede de Acesso fora de horário e Ações.
4. Para criar uma nova jornada, clique no ícone de adição.
5. Preencha os campos:
   - **Nome da jornada**
   - **Impedir acesso ao sistema fora da jornada** – se marcado, o usuário não poderá acessar o sistema fora do horário definido.
   - **Horário de trabalho** – para cada dia da semana, selecione os horários previamente cadastrados. O sistema soma automaticamente as horas totais.
   - **Dia de Folga** – marque para os dias que não são trabalhados.
6. Role a tela para baixo para vincular os funcionários:
   - Na lista **Usuários para vincular**, clique no sinal de adição ao lado do funcionário desejado.
   - Os vinculados aparecem em **Usuários vinculados**. Para remover, clique no ícone de lixeira.
   - É possível filtrar os vendedores por código ou nome.
7. Clique em **Salvar Jornada** e confirme a operação.

#### 9.4 Acompanhamento de Jornada

1. Acesse **Jornada de trabalho > Relatório de jornada**.
2. Informe os filtros:
   - Data inicial e final
   - Equipe (obrigatório se não informar representante)
   - Representante (opcional)
3. Clique em **Pesquisar**.
4. O relatório exibe as informações de forma analítica. **Não há relatório sintético**, nem informações sobre horas negativas.
5. No ícone de detalhes (lupa ou similar), é possível acessar:
   - Marcações extras
   - Detalhes de horários e localização
   - Detalhes de liberações
6. No ícone de justificativa (lápis), o campo de justificativa pode ser editado para inserir motivo de alteração no horário. **A justificativa só pode ser inserida no dia atual**; para datas anteriores, o campo fica indisponível.
7. O relatório está disponível apenas em formato analítico.

---

### 10. Inteligência Geográfica – Mapa de Oportunidades

#### 10.1 Permissão de Acesso

1. No menu lateral do maxGestão, acesse **Cadastro > Cadastro de usuários** ou **Perfil de usuários**.
2. Selecione o usuário/perfil e clique em editar.
3. Na aba **Permissões**, no quadro **Acesso a Rotinas**, marque **Inteligência Geográfica > Mapa de oportunidades**.

#### 10.2 Acessando o Mapa de Oportunidades

1. No menu lateral, clique em **Inteligência Geográfica > Mapa de oportunidades**.
2. No filtro avançado, preencha:
   - **CNAE** – até 10 códigos. CNAE significa Classificação Nacional de Atividades Econômicas.
   - **CNAEs secundários** – opcional, marcar se deseja incluir atividades secundárias.
   - **Capital social** – valor inicial e final para filtrar empresas por porte.
   - **Mostrar clientes cadastrados** – se marcado, os clientes já cadastrados aparecerão no mapa (pinos verdes); se desmarcado, apenas potenciais clientes (pinos vermelhos).
3. No mapa, escolha a forma de seleção da área (retângulo, polígono, círculo) no canto superior direito.
4. Delimite a área desejada no mapa.
5. Clique em **Consultar**.

**Importante:** Mesmo com todos os filtros preenchidos, se nenhuma área for selecionada no mapa, a pesquisa não retornará resultados.

#### 10.3 Resultados

- Pontos **azuis** indicam agrupadores de várias empresas próximas. Ao aproximar o zoom, os pinos individuais aparecem.
- Pinos **vermelhos** representam empresas que ainda não são clientes (potenciais prospects).
- Pinos **verdes** representam clientes já cadastrados (se a opção estiver marcada).
- Clicando em um pino, é possível visualizar informações como razão social e CNPJ.
- Ícones na parte superior do mapa:
  - **Ocultar/exibir informações** – alterna a exibição dos dados dos pinos.
  - **Exportar** – gera um arquivo CSV com as informações dos resultados.

---

### 11. Configurações do Sistema

#### 11.1 Acesso

1. No maxSoluções, clique no ícone do maxGestão.
2. Dentro do maxGestão, clique no ícone de engrenagem no canto superior direito.
3. Selecione **Configurações do sistema**.

#### 11.2 Configurações Gerais

- **Painel de Auditoria:**
  - **Visão de Gerente na hierarquia** – habilita a exibição de gerentes nos filtros.
  - **Visão de Coordenador na hierarquia** – habilita a exibição de coordenadores.
  - **Exibir sequência prevista e realizada das rotas agendadas** – mostra a ordem planejada e a executada.
  - **Incluir logomarca da empresa nos relatórios** – insira a URL da imagem para que a logo apareça.
  - **Exibir nome fantasia nos relatórios** – se marcado, o nome fantasia é exibido em vez da razão social.

- **Painel Geral:**
  - **Painel Geral dia atual** – por padrão, habilitado. Mostra informações do dia corrente. Se desabilitado, o painel exibe o primeiro dia do mês vigente e o dia atual.
  - **Realizar atualização automática do Painel Geral** – habilita e defina a frequência em minutos.

- **Notificações:**
  - **Apresentar notificações de Check-in/Check-out dos vendedores** – exclusivo para a versão web. Depende da configuração do parâmetro correspondente no maxPedido.

- **Dias úteis:**
  - **Utilizar dias úteis** – para clientes de outros ERPs (não Winthor). Clientes Winthor devem utilizar a rotina 309.

- **Logoff automático:**
  - **Logoff automático por inatividade no Painel de Auditoria** – habilite e defina o tempo em minutos. Após o período de inatividade, o usuário será desconectado.

#### 11.3 Tipos de Cobrança

- Nesta seção, é possível parametrizar a inadimplência por tipo de cobrança, definindo a quantidade de dias para que um título seja considerado inadimplente.
- Após as alterações, clique em **Salvar**.

---

### 12. Relatórios

#### 12.1 Análise de Resultados

1. No menu lateral, clique em **Relatórios > Vendas**.
2. Selecione **Análise de resultados**.
3. Preencha os filtros:
   - Período (data inicial e final)
   - Filial
   - Opções de dedução (impostos, ST, etc.)
   - Tipo de pedido (todos, apenas faturados, apenas não faturados)
4. Clique em **Pesquisar**.
5. O relatório exibe, entre outras informações, a **porcentagem de inadimplência**, calculada como (valor da inadimplência total do dia) / (valor da venda total do dia). Essa porcentagem pode ser visualizada para o período todo ou por dia (clicando no supervisor desejado).

#### 12.2 Análise de Débito e Crédito

1. Em **Relatórios > Vendas**, selecione **Análise de débito e crédito**.
2. Preencha os filtros:
   - Período
   - Filial
   - Opção de destacar alvos com débito superior a uma porcentagem definida.
3. Clique em **Pesquisar**.
4. O relatório apresenta as seguintes colunas:
   - **Equipe** (nome do supervisor)
   - **Quantidade de RCAs** na equipe
   - **Clientes atendidos**
   - **Pedidos realizados**
   - **Itens vendidos**
   - **Valor de venda** e **valor de tabela**
   - **Débito** e **Crédito** (valor e percentual)
   - **% total de Débito e Crédito** (participação do representante no total da empresa)
5. **Valor DC:** venda - tabela.
6. **%DC:** (venda - tabela) * tabela / 100.
7. **%DC total:** (venda do representante) / (valor total de vendas da empresa) * 100.
8. Valores negativos indicam débito; positivos, crédito.

#### 12.3 Acompanhamento de Metas no Aplicativo

1. Na tela inicial do aplicativo maxGestão, acesse o menu lateral e selecione **Venda prevista vs Realizada**.
2. Por padrão, a tela exibe metas por RCA, com:
   - Valor de venda
   - Quantidade de itens
   - Quantidade de pedidos
3. Para detalhar por supervisor, clique em **Detalhar supervisores**. Para voltar aos RCAs, clique em **Detalhar RCA**.
4. No filtro, é obrigatório preencher:
   - **Tipo de meta** (RCA, fornecedor, departamento, seção, produto)
   - **Modo de análise** (todos os pedidos de venda ou apenas faturados)
5. Opções adicionais:
   - Mostrar apenas alvos com metas definidas
   - Ocultar dados de representantes inativos
   - Desconsiderar venda Manifesta (tipo 13)
   - Converter quantidade para embalagem master
6. Selecione a filial desejada e as opções de dedução (ST, IPI, repasse, devoluções, bonificação).
7. Clique em **Aplicar** para visualizar os resultados.

---

### 13. Permissões de Acesso Detalhadas

#### 13.1 Diferença entre os Quadros de Permissões

- **Selecione acesso de rotinas:** Permissões relacionadas a funcionalidades do sistema que o usuário pode visualizar/alterar (ex.: relatórios, mapas, painéis, administração).
- **Acesso a dados:** Permissões relacionadas a informações da empresa (ex.: planos de pagamento, cobranças, departamentos, equipes, filiais, regiões, fornecedores, conta corrente).

Ambos os quadros possuem ferramenta de pesquisa. Clicando na seta ao lado do nome da permissão, é possível expandir e marcar subpermissões específicas.

#### 13.2 Permissões de Relatórios (Aba Vendas)

Cada relatório tem permissões principais e ramificações. Exemplos:

- **Análise de resultados:**
  - Acesso Básico
  - Exportar Grids Gerais
  - Exportar Grid de Análise
  - Visualizar %Débito/Crédito
  - Visualizar %Lucratividade
- **Venda por equipe e análise de vendas** (com ramificações)
- **Positivação de clientes** (com ramificações)
- **Venda por prazo (plano de pagamento)**
- **Venda por código de cobrança**
- **Posição, tipos de venda e origem de pedidos**
- **Projeção de venda**
- **Venda por praça/rota**
- **Analítico de Vendas**
- **Análise de débito e crédito**
- **Acompanhamento venda prevista x realizada**
- **Venda por ramo de atividade**
- **Consulta por representante**
- **Consultar clientes**

#### 13.3 Permissões de Relatórios (Aba Comercial)

- **Entrada de produtos:**
  - Acesso Básico
  - Exportar Grid Produtos
  - Mostrar Coluna Quantidade
- **Produtos em falta** (com ramificações)
- **Produtos sem giro**
- **Produtos mais vendidos**
- **Venda por fornecedor**
- **Consultar produto, estoque e preço**
- **Venda por departamento, seção e categoria**
- **Consultar carregamento** (com diversas ramificações de exportação e visualização)
- **Buscar produto, pedido em carregamento**

#### 13.4 Demais Permissões do Quadro "Acesso a Rotinas"

- **Administração:**
  - Configurações do sistema
  - Cadastrar perfil de usuários
  - Cadastrar usuários
  - Controle de autorização de pedidos (com subpermissões para debitar da conta corrente, etc.)
  - Cadastro de autorizações por margem de lucratividade
  - Relatórios personalizados
- **Mapas:** Acesso à localização dos vendedores, trajetos e ações. Funciona em conjunto com permissões de filial e equipe.
- **Painéis:** Acesso ao Painel Geral e Orçamento x Vendas. Cada card (Indicadores, Quantidade de pedidos, Ranking, etc.) tem permissão individual.
- **Inteligência Geográfica > Mapa de oportunidades** (já detalhado).

#### 13.5 Quadro "Acesso a Dados"

- **Planos de pagamento:** Permite acesso a planos específicos. Afeta autorização de pedidos e resultados.
- **Cobrança:** Permite acesso a tipos de cobrança. Afeta resultados e autorização.
- **Departamento de produtos:** Permite acesso a departamentos. Afeta resultados e autorização.
- **Seção de produtos:** Permite acesso a seções.
- **Equipes (Supervisores):** Define quais equipes o usuário pode visualizar. Impacta todos os resultados (indicadores, pedidos, mapas, etc.).
- **Filiais:** Define quais filiais o usuário pode acessar.
- **Regiões:** Define quais regiões, dentro das filiais permitidas, o usuário pode acessar.
- **Fornecedores:** Permissão principal para acesso a todos os fornecedores (ou pode ser restrita marcando individualmente).
- **Conta corrente:** Permissão principal para acesso à Gestão de conta corrente. Subpermissões:
  - Acesso Básico
  - Alterar limite de crédito
  - Lançar crédito
  - Lançar débito
  - Transferência de saldo

---

### 14. Relatório de Acesso

#### 14.1 Objetivo

Monitorar os acessos realizados dentro do Painel de Auditoria do maxGestão.

#### 14.2 Acesso

Menu lateral > **Cadastro > Relatório de Acesso**.

#### 14.3 Funcionalidades

- Por padrão, exibe os relatórios do dia atual.
- Em **Filtros avançados**, é possível selecionar:
  - Data inicial e final
  - Filial
  - Gerente
  - Supervisor
  - Opções: "apenas dias úteis" e "considerar usuários sem registro de acesso"
- Após a pesquisa, o sistema mostra a quantidade de acessos no período.
- Selecionando um ou mais usuários (marcando a caixa à esquerda), ativa-se a opção **Frequência de Acesso** no canto inferior direito.
- Ao clicar, é exibida a frequência detalhada dia a dia:
  - **Verde:** houve acesso
  - **Vermelho:** não houve acesso

#### 14.4 Logoff Automático

- Configurável em **Configurações do sistema > Configurações Gerais**, com a opção **Logoff automático por inatividade no Painel de Auditoria** e tempo em minutos.
- Se habilitado, o usuário será desconectado após o tempo de inatividade no painel.

---

### 15. Acompanhamento no Aplicativo MaxGestão

#### 15.1 Indicadores da Equipe

Na tela inicial do aplicativo, é possível visualizar:
- Valor total de vendas
- Devoluções
- Quantidade de pedidos
- Quantidade de itens
- Toneladas e cubagem
- Status dos pedidos na nuvem (parados, bloqueados, aguardando autorização, autorizados, recusados)
- Status dos pedidos no ERP (importados, aprovados, com erro)
- Status de entregas (no caminhão, em trânsito, entregues)

**Importante:** Todos os números são importados do maxPedido. Para que as informações apareçam, é necessário dar permissão no maxGestão Web (Cadastro de usuários > Permissões > Painéis > marcar os cards desejados).

#### 15.2 Legendas

No canto superior direito do aplicativo, clique no ícone de informações e selecione **Legendas** para ver o significado dos ícones.

#### 15.3 Quantidade de Pedidos e Clientes Positivados

- **Gráfico de pedidos:** mostra todos os pedidos (bloqueados, recusados, faturados) no período selecionado.
- **Gráfico de clientes positivados:** mostra a quantidade de clientes que tiveram vendas no período.

#### 15.4 Ranking de Supervisores e Vendedores

- Exibe o resultado em valor e percentual por supervisor e vendedor.
- Clique em "Ver mais" no final do card para expandir a lista.

#### 15.5 Ranking por Fornecedor, Departamento, Seção, Categoria

- Role a tela para baixo para visualizar esses rankings.
- É possível alternar entre as opções clicando na aba desejada (fornecedor, departamento, seção, categoria).

#### 15.6 Mapa dos Vendedores

- Mostra a localização dos vendedores em tempo real (desde que o GPS esteja habilitado no aplicativo de vendas e o rastreamento esteja ativo).

#### 15.7 Mapa de Calor de Vendas

- Indica as regiões com maior intensidade de vendas.
- Pontos vermelhos indicam alta concentração; verdes, menor.

#### 15.8 Filtros no Aplicativo

No canto superior direito, o ícone de filtro permite refinar as informações por:
- Data de emissão ou data de faturamento
- Equipe
- Representante
- Período (início/fim)
- Filial
- Tipo de venda
- Deduzir impostos (devolução, bonificação, ST, IPI)

---

### 16. Glossário de Termos

| Termo | Significado |
|-------|-------------|
| RCA | Representante Comercial Autônomo – vendedor |
| PWA | Progressive Web App – aplicativo que funciona via navegador e pode ser instalado |
| Acurácia | Medida de precisão das coordenadas GPS, em metros. Quanto menor, melhor |
| KM Total | Todo trajeto percorrido pelo vendedor, independente de roteiro |
| KM Trabalhado | Trajeto considerado do primeiro ao último cliente da agenda (ou do ponto inicial ao final, se configurado) |
| Aderência | Percentual da rota planejada que foi executada |
| Painel de Auditoria | Ferramenta para acompanhamento detalhado das ações dos vendedores |
| Inteligência Geográfica | Módulo para busca de oportunidades de novos clientes com base em CNAE e localização |
| Conta Corrente (CC) | Saldo flexível do vendedor para descontos e bonificações |
| Autorização de Pedido | Processo de aprovação de pedidos com condições especiais |
| Jornada de Trabalho | Configuração de horários de trabalho e folgas dos vendedores |
| Logoff Automático | Desconexão automática por inatividade no sistema |
| CNAE | Classificação Nacional de Atividades Econômicas |
| DC | Débito/Crédito – diferença entre valor de venda e valor de tabela |

---

**Fim do documento consolidado do MaxGestão.**


---

## 12. MaxPag — Fluxo Técnico, Integração e Diagnóstico

**Descrição**: Consolidação do fluxo MaxPag com foco em diagnóstico técnico, etapas assíncronas do processamento e pontos de validação no ERP e na mensageria.

### Fonte
- Fluxograma técnico apresentado pelo time de desenvolvimento (Back-end MaxPedido)
- Documento interno consolidado para suporte e desenvolvimento
- Bibliotecas:
  - https://biblioteca.maximatech.com.br/display/MS/Documento+de+suporte+maxPag
  - https://basedeconhecimento.maximatech.com.br/display/BMX/Como+trabalhar+com+o+maxPag

---

### Metadados

- Tipo detectado: `documentação funcional + técnica`
- Domínio: `Financeiro / Integração ERP / Mensageria`
- Natureza do fluxo: `Assíncrono`
- Dependências:
  - Mensageria (fila)
  - JOBs de Extração
  - Banco Local
  - Banco Nuvem
  - Operadora de pagamento
- Ambiente executado em: `Cluster de servidores`

---

### Objetivo do Documento

Este documento consolida o fluxo completo do MaxPag desde a criação do pedido até:

- Faturamento no ERP
- Cancelamento do pedido
- Estorno ou captura financeira

A visão é estruturada para:

- Diagnóstico de tickets
- Identificação de falhas (local, nuvem ou mensageria)
- Entendimento técnico do fluxo assíncrono

---

# Conhecimento Extraído

---

# 1. Início do Fluxo – APK (MaxPedido)

[etapa] O pedido é criado na APK.

[condição] Deve ser selecionado o tipo de cobrança vinculado ao MaxPag:

- PIX (vinculado ao MaxPag)
- Cartão de Crédito (vinculado ao MaxPag)

⚠️ Observação:
Existem formas de pagamento PIX e Cartão que **não utilizam o MaxPag**.  
A configuração correta deve estar vinculada à biblioteca do MaxPag.

---

# 2. Validação no Server PDV

[processo] O pedido é enviado ao Server PDV.

[validações]
- Regras comerciais
- Horário de operação
- Limite de crédito
- Regras fiscais

---

### 2.1 Autorização Prévia (Antes do MaxPag)

Se o pedido exigir autorização (ex: desconto):

- Server envia pedido ao MaxGestão
- Aguarda retorno
- Se autorizado → fluxo continua
- Se bloqueado → fluxo interrompido

⚠️ Essa etapa ocorre antes da geração do link de pagamento.

---

# 3. Geração do Link – MaxPag

[etapa] Server PDV solicita geração do link ao MaxPag.

[integracao]
- MaxPag comunica-se com a operadora
- Operadora valida e retorna
- MaxPag gera link

[mensageria]
- Evento é publicado em fila
- Qualquer servidor do cluster pode consumir

⚠️ O ambiente roda em cluster.
O consumo da fila pode ocorrer por qualquer instância ativa.

---

# 4. Crítica do Link – Server PDV

[processamento]
- Server consome evento da fila
- Registra link
- Envia crítica para APK
- Atualiza status para:

    Aguardando Pagamento

---

# 5. Pagamento pelo Cliente

[ação]
- RCA realiza swipe na APK
- Cliente recebe link
- Efetua pagamento

[estado]
A partir deste momento, o sistema apenas aguarda retorno da operadora.

---

# 6. Confirmação de Pagamento – MaxPag

Após pagamento:

[PIX]
- Autorização direta

[Cartão]
- Pré-autorização

[evento]
- MaxPag publica evento na mensageria
- Server PDV processa confirmação

[efeitos]
- Atualiza status do pedido
- Gera registros financeiros
- Notifica APK

Estado final desta etapa:

    Aguardando integração no ERP

---

# 7. JOB Extrator – Integração ERP

### Parâmetros de Controle

- ATIVAR_JOBMAXPAG_EXTRATOR
- PERMITIR_VENDA_CARTAO_CREDITO
- AMBIENTE_MAXPAYMENT (0=Hmg / 1=Prod)

---

### Função do JOB

[job]
Busca pedidos:

- Autorizados
- Pré-autorizados
- Ainda não integrados

---

### Integração Técnica

[consulta]
Int-PDV acessa:

- Banco de Dados Nuvem

⚠️ Diagnóstico importante:
Erros podem estar em:

- Banco Local
- Banco Nuvem
- Endpoint de integração
- Fila de mensageria

---

### Envio ao ERP

[processo]
- Extrator envia pedidos
- ERP passa a reconhecer pedido oficialmente

---

# 8. Monitoramento Pós-ERP

Um novo JOB monitora:

- Pedidos faturados
- Pedidos cancelados

Verifica se fluxo financeiro no MaxPag foi finalizado.

---

# 9. Cenários Pós-ERP

---

### 9.1 Pedido Cancelado

[ação]
Extrator solicita via Int-PDV:

- Cancelamento
- Estorno
- Cancelamento de pré-autorização

[MaxPag executa]
- Estorno total
ou
- Cancelamento de pré-autorização

[evento]
Atualização publicada via mensageria.

---

### 9.2 Pedido Faturado

Verifica:

Houve corte?

---

#### Não Houve Corte

PIX:
- Finaliza sem estorno

Cartão:
- Captura total
- Pré-autorizado → Autorizado

---

#### Houve Corte

PIX:
- Estorno parcial dos itens cortados

Cartão:
Se valor atendido < valor total:

- Captura parcial
- Cancelamento do saldo da pré-autorização

Observação importante:

No cartão de crédito, quando ocorre captura parcial, o valor excedente é liberado automaticamente pela operadora no limite do cliente.  
Não existe estorno adicional.

---

# 10. Pontos de Diagnóstico (Suporte / Dev)

Ao analisar um ticket, verificar:

1. Pedido foi autorizado no MaxGestão?
2. Link foi gerado pelo MaxPag?
3. Evento entrou na fila?
4. Server consumiu evento?
5. Confirmação de pagamento foi publicada?
6. JOB Extrator está ativo?
7. Pedido foi enviado ao ERP?
8. ERP retornou faturado ou cancelado?
9. Estorno/captura foi executado?

---

# 11. Tabelas para Análise

- MXSMAXPAYMENTMOV
- MXSINTEGRACAOPEDIDO_LOGST

Boa prática:

Comparar:

- Data da movimentação financeira
- Data de mudança de status do pedido

---

# 12. Resumo Executivo do Fluxo

1. Pedido criado
2. Validação
3. Autorização (se necessário)
4. Geração de link
5. Pagamento
6. Confirmação financeira
7. Integração ERP
8. Faturamento ou cancelamento
9. Ajuste financeiro (captura ou estorno)

---

# 13. Encerramento

O fluxo é finalizado quando:

- Server PDV registra as últimas movimentações
- MaxPag conclui captura ou estorno
- ERP consolida status final

---

## 13. Permissões e Funcionalidades da Central de Configurações

**Descrição**: Catálogo consolidado de permissões, módulos e funcionalidades disponíveis na Central de Configurações e demais áreas relacionadas.

### Catálogo eletrônico
Módulo para confecção de catálogos eletrônicos do Portal Executivo Sales

#### Catálogos
- **Criar novo catálogo**: Habilita a criação de um novo catálogo
- **Editar catálogo**: Permite a edição de um catálogo já existente
- **Publicar catálogo**: Publica as alterações pendentes para esse catálogo
- **Excluir catálogo**: Apaga um catálogo existente

#### Sessões
- **Criar página**: Inicia a criação de uma nova página
- **Editar sessão**: Permite a edição de uma Sessão já existente
- **Excluir sessão**: Exclui uma sessão existente
- **Reordenar sessões**: Habilita o processo de reordenação de sessões

#### Páginas
- **Criar página**: Inicia a criação de uma nova página
- **Excluir página**: Exclui uma página existente
- **Reordenar páginas**: Habilita o processo de reordenação de páginas

#### Marcações
- **Editar marcação de texto**: Permite alterar uma marcação de texto já existente
- **Criar marcação de produto**: Habilita controles responsáveis por realizar a marcação de um produto na página
- **Criar marcação de vídeo**: Habilita controles responsáveis por realizar a marcação de um vídeo na página
- **Criar marcação de texto**: Habilita controles responsáveis por realizar a marcação de um texto na página
- **Excluir marcação de produto**: Permite a exclusão de uma marcação de produto
- **Excluir marcação de vídeo**: Permite a exclusão de uma marcação de vídeo
- **Excluir marcação de texto**: Permite a exclusão de uma marcação de texto
- **Editar marcação de produto**: Permite alterar uma marcação de produto já existente
- **Editar marcação de vídeo**: Permite alterar uma marcação de vídeo já existente

### Geolocalização
Módulo para acompanhamento da geolocalização de representantes, clientes e pedidos
- **Consultar geolocalização**: Acesso básico ao sistema de geolocalização
- **Bloquear captura de informações de geolocalização**: Acesso básico para bloquear a captura de informações de geolocalização

### Principal
Módulo principal
- **Página principal (Métricas do sistema)**: Acesso básico à rotina. Página principal do sistema, com diversas métricas sobre o funcionamento do mesmo.
- **Página principal (Vendas realizadas)**: Acesso básico à rotina. Página principal, com diversas informações sobre as vendas realizadas.

### Cadastro
Módulo de cadastro de usuários
- **Usuários**: Acesso básico à rotina. Cadastro dos usuários que podem utilizar o sistema, com definições de permissões de acesso a rotinas, dados e aparelhos.
- **Perfil de usuários**: Acesso básico à rotina. Cadastro de perfis dos usuários do sistema.
- **Recomendação de produtos para pesquisa**: Acesso básico à rotina.
- **Restringir cobrança por filial**: Acesso básico à rotina.

### Clientes
Módulo clientes

#### Carteira de clientes/confecção de pedidos
- **Acesso básico**: Acesso básico à rotina.
- **Bloquear alteração das condições comerciais do pedido**: Impede que o representante altere as condições comerciais padrão, definidas no momento do carregamento do pedido.
- **Alterar filial retira do produto**: Permite ao representante alterar a filial retira de um produto, no momento da inserção.
- **Permitir escolher modo de processamento do pedido**: Permite ao RCA, no momento da confecção do pedido de venda, escolher se o pedido será normal ou balcão reserva.
- **Acesso ao controle de caixa fechada (Cabeçalho)**: Permite ao representante alterar o pedido para utilizar caixa fechada.
- **Permitir acesso aos Dados de transporte**: Permite ao RCA, no momento da confecção do pedido de venda, alterar a transportadora.
- **Utilizar recurso de abatimento**: Permite ao RCA utilizar o recurso de abatimento ao finalizar o pedido de venda.
- **Bloquear alteração da filial do pedido**: Impede que o representante altere a filial predefinida para o pedido.
- **Exibir valor total**: Exibe o valor total do produto na confecção do pedido ao invés de exibir o valor unitário.
- **Exibir desconto de cabeçalho**: Permite ao RCA inserir um desconto de cabeçalho ao iniciar um pedido.
- **Ocultar valores de débito e crédito**: Oculta valores de débito e crédito do RCA no cabeçalho e total do pedido.
- **Habilitar visualização de estoque**: Permite que o estoque disponível seja apresentado durante a consulta dos produtos.
- **Bloquear campo "Previsão de Faturamento"**: Evita que o usuário possa definir a data de previsão de faturamento do pedido.
- **Permitir inserção de produtos sem estoque (Online)**: Permite que sejam inseridos itens sem estoque disponível no Versão Online, para que o corte seja dado posteriormente (no momento da gravação do pedido no sistema).
- **Permitir escolha da filial de emissão da NF**: Permite ao usuário escolher, quando aplicável, a filial que será usada para emissão da NF.
- **Bloquear alteração nas condições comerciais do produto**: Impede que o representante altere as condições comerciais padrão, definidas no momento do carregamento do produto.
- **Ocultar preços mínimos e máximos na tela de informações adicionais**: Impede que sejam apresentadas as informações de preços mínimos e máximos durante a inserção de produtos.
- **Habilitar utilização do recurso "Agrupamento de Pedidos"**: Permite que o RCA escolha esse pedido como sendo 'Agrupável'.
- **Bloquear alteração do Código de Cobrança do Pedido**: Impede que o RCA altere a cobrança do pedido apenas.
- **Ocultar campo crédito do cliente**: Permite visualização do campo durante a manipulação do pedido.
- **Permitir selecionar endereço de entrega**: Permite selecionar o endereço de entrega ao finalizar o pedido.
- **Permitir selecionar o cliente autorizado**: Permite selecionar o cliente autorizado cadastrado na rotina 390 do winthor.
- **Bloquear seleção do tipo de bonificação**: Bloqueia seleção do tipo de bonificação ao salvar o pedido.
- **Desativar bloqueio de conexão por pedidos pendentes**: [Descrição não fornecida]
- **Permitir solicitação de autorização de preço no aplicativo**: Permite que o RCA aplique um desconto maior do que o permitido para o produto pelas políticas de desconto, gerando assim uma autorização de preço. Esta autorização de preço deve ser autorizada pelo supervisor do RCA que solicitou, no Portal Executivo.
- **Solicitar confirmação para conceder os brindes**: Após a validação do pedido no aparelho do RCA, é solicitado confirmação para conceder os brindes para aquele pedido.
- **Solicitar autorização para checkin fora do raio**: É solicitado confirmação para conceder autorização para checkin fora do raio.
- **Solicitar autorização para atender cliente fora da rota**: É solicitado confirmação para atender cliente fora da rota.
- **Solicitar autorização para alterar coordenadas do cliente**: Solicitar autorização para alterar coordenadas do cliente.
- **Compartilhar pedidos/orçamento**: Compartilhar pedidos/orçamento.
- **Permitir solicitação de autorização por margem de lucratividade**: Permitir solicitação de autorização por margem de lucratividade.
- **Solicitar aprovação para pedidos bonificados**: [Descrição não fornecida]
- **Solicitar autorização para check-in e check-out em cliente fora do raio**: [Descrição não fornecida]
- **Habilita a visualização dos dados de estoque disponível dos produtos apresentados**: [Descrição não fornecida]
- **Solicitar aprovação para pedidos com cliente bloqueado**: Permite que o vendedor possa realizar pedidos para cliente bloqueado, gerando uma solicitação de aprovação no maxGestão.
- **Solicitar aprovação para pedidos com limite de crédito excedido**: Permite que o vendedor possa realizar pedidos para cliente com limite de crédito excedido, gerando uma solicitação de aprovação no maxGestão.
- **Habilitar Visualização de Margem/Lucratividade**: Habilita as informações relacionadas às margens/lucratividade dos produtos e do pedido.
- **Bloquear Pedidos Abaixo da Margem Mínima**: Caso marcada e a lucratividade do pedido seja menor que a margem mínima definida para o plano de pagamento selecionado, o pedido é salvo, mas como bloqueado. Caso contrário, o sistema não permite que o mesmo seja salvo.
- **Permitir alterar observações do pedido**: Permite que as observações do pedido sejam editadas pelo representante.
- **Ocultar visualização da filial retira**: Oculta a visualização da filial retira que será utilizada durante o processamento do produto.
- **Apresentar somente produtos com estoque disponível**: Quando habilitado, por padrão, o sistema apresenta somente os produtos com estoque disponível nas pesquisas.
- **Desabilita alternar visualização de produtos com estoque/sem estoque**: Impede que o usuário escolha se quer visualizar a relação completa de produtos ou somente os produtos disponíveis para venda.
- **Visualizar valor de comissão de venda**: Permite que o usuário veja o valor de comissão no total do pedido.
- **Mostrar painel com totalizadores do pedido (Online e Offline)**: Apresenta, no rodapé da tela de confecção do pedido, um painel com alguns totalizadores do pedido. Somente para as versões Online e Offline do sistema.
- **Rotina utilizada para acessar informações sobre clientes e iniciar um Novo Pedido/Orçamento**: [Descrição não fornecida]

#### Cadastro/Manutenção da carteira de clientes
- **Acesso básico**: Acesso básico à rotina.
- **Habilitar Inclusão de clientes**: Permite o cadastramento de novos clientes na carteira.
- **Habilitar alteração de clientes**: Permite que o cadastro de clientes existentes seja alterado.
- **Habilitar manipulação de contatos de clientes**: Permite o Cadastro/edição de contatos de clientes.
- **Habilitar manipulação de referências comerciais**: Permite o cadastro/edição de referências comerciais.
- **Ocultar informações de cliente contribuinte**: Ocultar informações do Simples Nacional.
- **Ocultar informações da cidade IBGE**: [Descrição não fornecida]
- **Ocultar aba de endereço de cobrança**: [Descrição não fornecida]
- **Ocultar aba de endereço de entrega**: [Descrição não fornecida]
- **Ocultar aba de endereço comercial**: [Descrição não fornecida]
- **Ocultar aba de observações gerenciais**: [Descrição não fornecida]
- **Habilitar aba de cadastro de anexos**: [Descrição não fornecida]
- **Habilitar solicitação de aumento limite crédito**: Solicitar a autorização do aumento do limite do cliente no aplicativo do maxPedido junto com o maxGestão.
- **Modulo que permite a manutenção da carteira de clientes do RCA, incluindo-se o cadastro de novos clientes**: [Descrição não fornecida]

### Roteirização/Justificativas de não Venda
- **Bloquear venda de clientes fora da rota**: Impede que sejam confeccionados pedidos para clientes que não façam parte da rota do dia.
- **Obrigar sequenciamento de visitas**: Quando habilitado, obriga o RCA a emitir pedidos/justificativas segundo roteiro estabelecido.
- **Permitir justificativas de clientes fora da rota**: Quando habilitado, permite que o RCA envie justificativas de clientes que estão fora da rota de visita atual.
- **Permitir antecipar roteiro de visitas**: Quando habilitado, permite que o RCA antecipe compromissos futuros para a data atual.
- **Habilitar criação de visita avulsa**: Permite ao RCA criar uma visita no dia atual para qualquer cliente da listagem.
- **Requer autorização para antecipação do roteiro de visitas**: Exige que o usuário entre em contato com a empresa, solicitando permissão para a antecipação de visita do cliente selecionado.
- **Requer autorização para checkout fora do raio do cliente**: Exige que o usuário entre em contato com a empresa, solicitando permissão para o checkout fora do raio do cliente.
- **Parametriza o módulo de roteirização e justificativas de não venda**: [Descrição não fornecida]

### Orçamentos
Módulo orçamentos

#### Orçamentos efetuados
- **Acesso básico**: Acesso básico à rotina.
- **Ocultar Informações sobre lucratividade**: Oculta informações sobre a lucratividade do pedido.
- **Ocultar informações sobre débito/crédito**: [Descrição não fornecida]
- **Ocultar Informações de comissão**: Oculta informações sobre a comissão gerada para o pedido.
- **Ocultar informações sobre a margem de contribuição**: Ocultar informações sobre a margem de contribuição do pedido.
- **Ocultar informações sobre o desconto geral**: Ocultar informações sobre o desconto geral do pedido.
- **Ocultar informações sobre pos. carteira de clientes**: Ocultar informações sobre pos. carteira de clientes do pedido.
- **Ocultar informações sobre o limite de conta corrente**: Ocultar informações sobre o saldo da conta corrente.
- **Ocultar informações sobre o prazo médio de vendas**: Ocultar informações sobre o prazo médio de vendas do pedido.
- **Permite listar, alterar, excluir, imprimir e enviar e-mails dos orçamentos existentes no sistema**: [Descrição não fornecida]

#### Impressão/Envio de orçamentos por e-Mail
- **Orçamento completo**: Permite o envio/impressão do orçamento completo.
- **Orçamento simplificado**: Permite o envio/impressão do orçamento simplificado.
- **Orçamento simplificado com foto**: Permite o envio/impressão do orçamento simplificado com foto.
- **Orçamento simplificado com ficha técnica**: Permite o envio/impressão do orçamento simplificado com ficha técnica.
- **Controla as permissões de impressão e envio de orçamentos por e-Mail**: [Descrição não fornecida]
- **Pedido simplificado com ficha técnica**: Permite o envio/impressão do pedido simplificado com ficha técnica.

### Consultas
Modulo principal
- **Criticas de pedidos**: Acesso básico a consulta de críticas de pedidos. Permitir que as críticas dos pedidos enviados pelo sistema possam ser consultadas.

### Pedidos
Módulo pedidos

#### Pedidos efetuados
- **Acesso básico**: Acesso básico à rotina.
- **Ocultar Informações sobre lucratividade**: Oculta informações sobre a lucratividade do pedido.
- **Ocultar informações sobre débito/crédito**: [Descrição não fornecida]
- **Ocultar informações de comissão**: Oculta informações sobre a comissão gerada para o pedido.
- **Bloquear alteração/reenvio de pedido enviado**: Impede que pedidos enviados sejam editados e/ou reenviados.
- **Permitir duplicar pedido de venda**: Permite acesso ao recurso de duplicação de pedidos de venda.
- **Gerar indenizações de pedido de venda**: Permite acesso ao recurso de geração de indenizações para pedidos de venda.
- **Habilitar filtro por filial**: Habilita ou não o filtro de pedidos e orçamentos por uma filial específica.
- **Ocultar informações sobre a margem de contribuição**: Ocultar informações sobre a margem de contribuição do pedido.
- **Ocultar informações sobre o desconto geral**: Ocultar informações sobre o desconto geral do pedido.
- **Ocultar informações sobre pos. carteira de clientes**: Ocultar informações sobre pos. carteira de clientes do pedido.
- **Ocultar informações sobre o limite de conta corrente**: Ocultar informações sobre o saldo da conta corrente.
- **Ocultar informações sobre o prazo médio de vendas**: [Descrição não fornecida]
- **Permitir excluir pedidos do aparelho**: Esta opção não é válida para todas integrações.
- **Ocultar informações sobre o prazo médio de vendas do pedido**: [Descrição não fornecida]
- **Disponibiliza diversas operações para os pedidos atualmente salvos no sistema, como consulta de críticas de envio, alterações e bloqueios**: [Descrição não fornecida]

#### Impressão/Envio de pedidos por e-Mail
- **Pedido completo**: Permite o envio/impressão do pedido completo.
- **Pedido simplificado**: Permite o envio/impressão do pedido simplificado.
- **Pedido simplificado com foto**: Permite o envio/impressão do pedido simplificado com foto.
- **Pedido simplificado com ficha técnica**: Permite o envio/impressão do pedido simplificado com ficha técnica.
- **Controla as permissões de impressão e envio de pedidos por e-Mail**: [Descrição não fornecida]

### Produtos
Módulo produtos/tabela de preços
- **Consultar produtos**: Acesso básico à rotina. Permite consulta a diversas informações sobre um determinado produto, sem a necessidade de se iniciar um novo pedido.
- **Habilitar visualização de estoque**: Permite que o estoque disponível seja apresentado durante a consulta dos produtos.

### CRM
Módulo principal
- **Página principal**: Acesso básico à rotina.
- **Cadastro de manifestações**: Acesso básico. Permite ao usuário cadastrar manifestações no sistema.
- **Pesquisa de manifestações**: Acesso básico. Permite ao usuário pesquisar manifestações no sistema.

### Mensagens
Módulo responsável pelo envio de mensagens e recados para o sistema.
- **Envio de recados e mensagens**: Acesso básico à rotina.
- **Enviar recados**: Permite ao usuário enviar Recados diretamente para o ERP do usuário selecionado.
- **Enviar e-Mails**: Permite ao usuário enviar E-mails para os destinatários aos quais ele possui acesso.
- **Permite a comunicação direta entre os RCAs e os Usuários do ERP**: [Descrição não fornecida]

### Consultas do Sistema
Módulo de consultas do sistema
- **Consultas do sistema**: Acesso básico a seção de consultas. Acesso as Consultas do sistema.
- **Notificação de estoque**: Acesso básico as notificações de estoque. Acesso as notificações de estoque.
  - **Ocultar quantidade na listagem dos produtos**: Determina se na listagem de produtos da notificação de estoque, a informação sobre quantidade deve ser ocultada.
- **Histórico de pedidos**: Acesso básico as consultas de pedidos. Acesso as consultas de pedidos.
- **Políticas comerciais**: Acesso básico as políticas comerciais. Consultas as políticas comerciais dos produtos.
- **Consulta aniversariantes**: Acesso básico a consulta de aniversariantes. Consulta os aniversariantes baseado no período estipulado.
- **Gerar arquivos remessa mondelez**: Acesso básico a geração de arquivos mondelez. Gerar arquivos baseado no período estipulado.
- **Títulos em Aberto**: Acesso básico. Consulta todos os títulos em aberto do cliente. Acesso aos títulos em aberto.

### Configurações
Módulo de configurações do sistema
- **Configurações**: Acesso básico à rotina. Permite a definição de diversas configurações da plataforma de Pedidos Máxima Sistemas.
- **Planos de Pagamento**: Planos de pagamento disponíveis no sistema.
- **Códigos de cobrança**: Códigos de cobrança disponíveis no sistema.
- **Tipos de venda**: Tipos de venda disponíveis no sistema.
- **Filiais (venda)**: Filiais (venda) disponíveis no sistema.
- **Destinatários de mensagens/e-mails**: Destinatários disponíveis para envio de recados e e-Mails.
- **Emissão de NF**: Tipo de NF enviada pelo RCA selecionado.
- **Listar produtos das filiais selecionadas**: Exibe no tablet somente os produtos das filiais selecionadas.
- **Filiais (estoque)**: Filiais (estoque) disponíveis no Sistema.
- **Consulta clientes sem venda**: Acesso a clientes sem venda.
- **Consulta Pedido por Região Atendimento**: Acesso básico ao Consulta Pedidos por Região.
- **Consulta trajeto RCA**: Acesso básico ao consulta trajeto RCA.
- **Permitir selecionar o cliente autorizado**: Permite selecionar o cliente autorizado cadastrado na rotina 390 do winthor.
- **Consulta Acompanhamento vendas**: Acesso básico ao consulta acompanhamento vendas.

### Manutenção
Efetue manutenção no sistema da máxima como limpeza, backup, etc
- **Atualizar estrutura do banco**: Acesso básico à rotina. Manutenção do banco de dados.
- **Restruturação do banco de dados**: Acesso básico à rotina. Restruturação do banco de dados.
- **Atualizar definição de objetos Máxima**: Acesso básico à rotina. Atualizar definição de objetos Máxima.
- **Disponibilizar nova versão para os RCA's**: Acesso básico à rotina. Disponibilizar nova versão para os RCA's.
- **Atualizar definição de licenças**: Acesso básico à rotina. Atualizar definição de licenças.
- **Enviar configuração inicial para os RCA's**: Acesso básico à rotina. Enviar configuração inicial para os RCA's.
- **Atualizar aplicativos disponíveis**: Acesso básico à rotina. Atualizar aplicativos disponíveis.
- **Sincroniza informações sobre os usuários com o servidor em nuvem**: Acesso básico à rotina. Sincroniza informações sobre os usuários com o servidor em nuvem.
- **Validação de entidades/relacionamentos**: Acesso básico à rotina. Validação de entidades/relacionamentos.
- **Solicitação de base de dados**: Acesso básico à rotina. Solicitação de base de dados.
- **Horários de trabalho**: Acesso básico à rotina. Cadastro de horário de trabalho.
- **Jornada de trabalho**: Acesso básico à rotina. Cadastro de jornada de trabalho.
- **Registros de jornada**: Acesso básico a consulta de registro de jornada. Permitir que os registro de jornada possam ser consultadas.
- **Pedidos com cobrança cartão de crédito**: Acesso básico a consulta de pedidos com cobrança cartão de crédito. Permitir que sejam feitas consulta de pedidos com cobrança cartão de crédito.
- **Metas**: Acesso básico à rotina. Habilita metas.
- **Combo de Descontos**: Acesso básico aos combos de desconto. Habilita Combo de Descontos.
- **Inteligência de Negócio**: Permite visualizar e alterar os acessos às funcionalidades relacionadas a inteligência de negócios.
- **Campanha de Brindes**: Acesso básico à rotina. Acesso as campanhas de brindes.
- **Recomendação de produtos**: Acesso à recomendação de produtos.
- **Pré-pedido**: Acesso ao cadastro de pré-pedidos.
- **Mix Ideal**: Acesso ao cadastro de mix ideal.
- **Cadastros gerais**: Acesso básico à rotina. Acesso aos cadastros gerais.
- **Família de produtos**: Acesso básico à rotina. Acesso ao cadastro de família de produtos.
- **Campanha progressiva**: Acesso básico à rotina. Acesso ao cadastro de campanha progressiva.
- **Desconto escalonado**: Acesso básico à rotina. Acesso ao cadastro de desconto escalonado.
- **Detalhes de produtos**: Acesso básico à rotina. Acesso ao cadastro de detalhes de produtos.
- **Dias Úteis**: Acesso básico à rotina. Acesso ao cadastro de dias úteis.
- **Campanha de Brindes**: Acesso básico à rotina. Acesso ao cadastro de campanha de brindes.
- **Cadastro de Grupos**: Acesso básico à rotina. Acesso ao cadastro de grupos.
- **Tipos de Anexos**: Acesso básico à rotina. Acesso ao cadastro de tipos de anexos.

### Restrições
- **Restrições de Venda**: Acesso ao cadastro de restrições de Venda.
- **Restrições de tipo de venda**: Acesso ao cadastro de restrições de tipo de venda.
- **Restrições de visualização de produtos sem estoque por seção**: Acesso ao cadastro de restrições de visualização de produtos sem estoque por seção.
- **Restrições de conta corrente por filial**: Acesso ao cadastro de restrições de conta corrente por filial.
- **Restrições de unidades de embalagem por tipo de venda**: Acesso ao cadastro de restrições de unidades de embalagem por tipo de venda.
- **Importação de arquivo de negociação**: Acesso básico à rotina. Acesso à importação de arquivo de negociação.
- **Embalagens**: Acesso básico à rotina. Acesso ao cadastro de embalagens.
- **Permitir editar pedidos enviados**: [Descrição não fornecida]
- **Permitir cancelar pedidos enviados**: [Descrição não fornecida]
- **Solicitar aprovação para pedidos de troca**: [Descrição não fornecida]
- **Permitir solicitação de autorização por margem de lucratividade e fornecedor**: [Descrição não fornecida]
- **Ocultar Visualização do Preço Máx. e Acrés. Máx. do Produto**: [Descrição não fornecida]

### Categoria de parâmetros
- **Acesso básico**: Acesso básico à rotina. Cadastro de categoria de parâmetros.

### Parâmetros
- **Acesso básico**: Acesso básico à rotina. Cadastro de parâmetros.

### Parâmetros da jornada de trabalho
- **Acesso básico**: Acesso básico à rotina. Cadastro de parâmetros da jornada de trabalho.

### Mensagem Circular
- **Acesso básico**: Acesso básico à rotina. Cadastro de mensagem circular.

### Campos customizados
- **Acesso básico**: Acesso básico à rotina. Cadastro de campos customizados.

### Acesso ao controle de caixa fechada (Produto)
- Habilita controle de caixa fechada na tela de negociação do produto (Unidade master)

### Requer autorização para checkout fora do tempo cadastrado
- Exige que o usuário entre em contato com a empresa, solicitando permissão para o checkout fora do tempo cadastrado

### Cor/Legenda de campos
- **Acesso básico**: Acesso básico à rotina. Cadastro de cor/Legenda de campos.

### Períodos
- **Acesso básico**: Acesso básico à rotina. Cadastro de períodos.

### maxPag
- **Tokens**: Acesso ao cadastro de Tokens do maxPag.
- **Cadastros do maxPag**: [Descrição não fornecida]

### Logs de desbloqueio
- **Acesso básico**: Acesso básico à rotina. Permitir que os logs de desbloqueio sejam consultados.

### Motivo de não venda para os pré-pedidos
- **Acesso básico**: Acesso básico à rotina. Permitir que os [aaa] sejam consultados. (descrição incompleta)

### Extrato Pronta Entrega
- **Acesso básico**: Acesso básico à rotina. Permitir que os registros do Extrato Pronta Entrega sejam consultados.

### Apuração de Campanha Progressiva
- **Acesso básico**: Acesso básico à rotina. Permitir que os registros da apuração de campanha Progressiva sejam consultados.

### Extrato de Caixa
- **Acesso básico**: Acesso básico à rotina. Permitir que os registros do extrato de caixa progressiva sejam consultados.

### Pedidos
- **Acesso básico**: Acesso básico à rotina. Permitir que os registros de pedidos sejam consultados.

### Pedidos bloqueados (Nuvem)
- **Acesso básico**: Acesso básico à rotina. Permitir que os registros dos pedidos bloqueados (Nuvem) sejam consultados.

### Anexo de cliente
- **Acesso básico**: Acesso básico à rotina. Permitir que os registros dos anexo de cliente sejam consultados.

### Justificativa de Visitas
- **Acesso básico**: Acesso básico à rotina. Permitir que os registros dos justificativa de visitas sejam consultados.

### Extras
- **Acesso básico**: Acesso básico à rotina. Acesso ao menu de extras.

### Upload rápido de fotos de produtos
- **Acesso básico**: Acesso básico à rotina. Acesso ao upload rápido de fotos de produtos.

### Upload manual de fotos de produtos
- **Acesso básico**: Acesso básico à rotina. Acesso ao upload manual de fotos de produtos.

### Relatórios
- **Acesso ao básico**: Acesso básico à rotina. Acesso ao básico.

### Desbloqueios
- **Acesso básico**: Acesso básico à rotina. Permite a geração de códigos utilizados no desbloqueio manual de dispositivos que não atendem às políticas de frequência de conexão.

### Restrições por plano de pagamento
- Acesso ao cadastro de restrições por plano de pagamento.

### Documento de apoio
- **Acesso básico**: Acesso básico à rotina. Acesso ao documento de apoio.

### Objetivos de visitas
- Acesso ao cadastro do Depara do motivo de não venda.

### Depara do motivo de não venda
- **Acesso básico**: Acesso ao cadastro de objetivos de visitas.

### Tempo de visita
- Acesso ao cadastro de tempo de visita. Acesso básico à rotina. Acesso básico.

### Permitir liberar pedidos bloqueados para o ERP
- [Descrição não fornecida]

### Permitir cancelar pedidos bloqueados
- [Descrição não fornecida]

### Permite liberar pedidos para serem integrados no ERP
- [Descrição não fornecida]

### Permitir que os registros dos pedidos bloqueados (Nuvem) sejam consultados
- [Descrição não fornecida]

### Indústria
- **Tipo de documento**: Acesso básico à rotina. Acesso ao cadastro do tipo de documento.
- **Envio de documento**: Acesso básico à rotina. Acesso ao envio de documento.
- **Solicitar aprovação para pedidos com itens bonificados**: Permite solicitar aprovação para pedidos com itens bonificados.

### Gerenciador de jobs
- **Controle de execução**: Acesso ao controle de execução de jobs do extrator.
- **Tempo de execução**: Acesso ao controle do tempo de execução.
- **Acesso ao gerenciador de jobs do extrator**: [Descrição não fornecida]
- **Acesso à rotina**: [Descrição não fornecida]
- **Acesso ao cadastro de férias para o vendedor**: [Descrição não fornecida]

### Cobranças
- Acesso ao cadastro de Cobranças do maxPag.

### Log de Parâmetros
- **Acesso básico**: Acesso básico à rotina. Permitir que as alterações dos parâmetros sejam consultadas.

---

## 14. Validação de Produtos Próximos ao Vencimento

**Descrição**: Regras e parâmetros da funcionalidade de alerta e legenda para produtos próximos ao vencimento.

### Visão Geral

A funcionalidade implementa uma validação parametrizável de produtos próximos ao vencimento, realizando a análise automática da data de validade no momento da inclusão do item no pedido.

### Objetivos da Solução

- Analisar automaticamente a data de validade do produto;
- Exibir alertas claros e objetivos conforme o status:
  - Produto vencido;
  - Produto próximo ao vencimento;
- Adicionar legenda visual para identificação rápida na listagem;
- Permitir utilização da informação como filtro na busca de produtos;
- Não gerar impacto negativo na performance do aplicativo.

Essa funcionalidade proporciona mais segurança ao vendedor e melhora a experiência do cliente.

---

### Campos de Validade Considerados

A validação pode utilizar um dos seguintes campos:

- **P** = `MXSPRODUT.DTVENC`  
  Validade do produto

- **W** = `MXSVALIDADEWMS.DATA`  
  Validade via WMS

- **L** = `MXSLOTE.DTVALIDADE`  
  Validade por lote

---

### Parametrização

#### DIAS_PRODUTO_PROXIMO_VENCIMENTO
- Define a quantidade de dias considerada para geração da legenda (≤).

#### TIPO_LEGENDA_DATA_VENCIMENTO
- Define qual data de vencimento será considerada para gerar a legenda.
- Valores possíveis: `P`, `W` ou `L`.

#### HABILITA_ALERTA_PROD_PROXIMO_VENCIMENTO
- Habilita o alerta ao adicionar um produto próximo ao vencimento.

---

### Funcionamento

Com os parâmetros:
- `DIAS_PRODUTO_PROXIMO_VENCIMENTO` preenchido;
- `TIPO_LEGENDA_DATA_VENCIMENTO` definido;
- `HABILITA_ALERTA_PROD_PROXIMO_VENCIMENTO` ativo;

O sistema passa a:

- Exibir o produto na aba tabela com ícone identificador de proximidade de vencimento;
- Permitir uso da informação como filtro na busca;
- Exibir alerta ao tentar adicionar o produto ao pedido, informando:
  - Quantos dias faltam para o vencimento; ou
  - Se o produto já está vencido.

---

### Pré-requisito

- O aplicativo deve estar na versão mais recente (versão ponta).
- A versão já foi disponibilizada no ambiente para validação.

---

## 15. Regras de Negócio Canônicas para Atendimento N1

**Descrição**: Regras estáveis de negócio utilizadas como referência operacional para atendimento, troubleshooting e validação de fluxo.

Este documento e um contexto fixo para o bot N1. Ele resume regras estaveis de negocio ja presentes na base.

### 1) Escopo do produto
- O maxPedido e um app mobile de forca de vendas integrado ao ERP do cliente.
- O fluxo de pedido depende de configuracoes do maxPedido e, em alguns cenarios, de parametros do ERP (ex.: Winthor).
- O bot N1 deve priorizar orientacoes praticas: configuracao, validacao de dados e trilha de troubleshooting.

### 2) Fluxo macro de pedido e integracao
- O pedido sai do app para a nuvem da Maxima.
- A integracao com ERP consome o pedido e devolve status/critica.
- A timeline do pedido depende do retorno correto do ERP para as estruturas de historico.
- Em cenarios de "status nao atualiza", validar cadeia completa: envio, processamento ERP, retorno de status.

### 3) Tabelas frequentemente envolvidas (consulta operacional)
- MXSINTEGRACAOPEDIDO: registro de integracao do pedido.
- MXSHISTORICOPEDC: historico/status usado na timeline.
- MXSINTEGRACAOPEDIDOLOG e MXSINTEGRACAOPEDIDO_LOGST: logs de integracao.
- MXSHISTORICOCRITICA: historico de criticas.

Observacao:
- Nome de tabela/campo deve sempre ser confirmado nos trechos recuperados.
- Se a pergunta pedir SQL, priorizar consultas ja documentadas na base.

### 4) Regras recorrentes de negocio
- Cliente bloqueado: comportamento depende de combinacao de parametros no maxPedido e, em Winthor, tambem no ERP.
- Filial retira/desmembramento: pode gerar multiplos pedidos por filial quando configurado.
- Pedido em autorizacao pode impedir ou alterar fluxo esperado de desmembramento/processamento.
- Parametros de check-in/check-out/GPS podem bloquear confeccao do pedido quando exigidos.

### 5) Regra de atendimento N1
- Responder com base no que estiver documentado.
- Se faltar informacao critica para fechar diagnostico, listar verificacoes objetivas e indicar escalonamento para N2.
- Evitar recomendacoes genericas sem validacao de parametro/tabela/processo.

---

**Documento consolidado automaticamente a partir dos arquivos enviados pelo usuário, com deduplicação parcial e reorganização de títulos para busca semântica.**
