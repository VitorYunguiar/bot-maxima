# Rotas, Visitas e Consultas — Base de Conhecimento maxPedido/Winthor

**Palavras-chave:** rotas, roteiro, visitas, consultas, positivacao, titulos, estoque, politicas comerciais, historico pedidos, aniversarios, mapa oportunidades, visita avulsa, check-in, checkout

**Sistema:** maxPedido

**Area:** Vendas, Roteirizacao, Consultas

---

## 1. Cadastro e Edicao de Rota no Aplicativo

### 1.1. Configuracao de Parametros

Para habilitar o cadastro e edicao de rotas no aplicativo do maxPedido, e necessario configurar parametros na Central de Configuracoes.

#### Passos para Configuracao

1. Na Central de configuracoes, acesse Menu lateral > Configuracoes > Parametros
2. Busque pelo parametro `HABILITA_CADASTRO_ROTA_CLIENTE` e clique em pesquisar
3. Clique no icone de edicao da coluna Acoes, marque para habilitar e salve
4. Ainda na tela inicial da Central, clique em Configuracoes > Configuracoes > Aba Formularios > Clientes
5. Verifique se em Roteiro de visita a opcao "Ocultar Ambos" esta desmarcada

#### Observacoes Importantes

- O parametro `HABILITA_CADASTRO_ROTA_CLIENTE` habilita o cadastro de rotas durante o cadastro ou edicao do cliente no aplicativo do Pedido de Vendas
- Deve estar marcado para que a aba de Roteiro de Visitas apareca para ser alterada
- Caso a opcao de Ocultar em Ambos estiver marcada, nao sera possivel realizar cadastro e edicao de rota no aplicativo mesmo que o parametro estiver habilitado, pois ela estara oculta para o vendedor

### 1.2. Criar Rota para Novo Cadastro de Cliente

1. Na tela de clientes, clique no icone de adicionar para criar novo cadastro (fica na barra superior da tela)
2. Na aba Roteiro de Visitas, preencha os dados solicitados
3. Apos preenchimento de todas as informacoes, clique no icone de salvar que fica no canto direito superior da tela

#### Campos do Roteiro de Visitas

| Campo | Descricao |
|-------|-----------|
| Data inicial | Data de inicio da geracao de roteiros |
| Data final | Data de termino da geracao de roteiros |
| Data da proxima visita | A primeira data apos o cadastro quando devera ocorrer a visita |
| Numero da semana | Escolha em qual semana deve ocorrer a visita |
| Periodicidade | Intervalo em dias que deverao ocorrer as visitas, normalmente a cada 7 dias |

### 1.3. Editar Rota no Cadastro de Cliente

1. Na tela inicial do maxPedido Aplicativo, selecione a aba Clientes
2. Clique longo no cliente desejado
3. Selecione a opcao Editar Cliente
4. Confirme para editar o cadastro do cliente
5. Clique na aba Roteiro de Visitas e altere as informacoes conforme necessidade

---

## 2. Roteiro de Visita no Aplicativo

### 2.1. Visualizacao do Roteiro

A configuracao do Roteiro de Visita e realizada atraves do ERP. Apos configurado, o maxPedido ira validar o Roteiro la cadastrado.

#### Passos para Visualizar Roteiro

1. Na tela inicial do aplicativo do maxPedido, clique na Aba Clientes
2. Na tela de clientes, normalmente ira trazer os clientes do dia (quantidade mostrada ao final da tela)
3. Clique no icone de tres pontos e selecione "Ver todos" caso deseje alterar a visualizacao
4. Para voltar a mostrar os clientes do dia, clique na opcao "Roteiro Hoje"
5. No mesmo icone de tres pontos, clique na opcao "Roteiro" para visualizar o mesmo

### 2.2. Informacoes do Roteiro

Na tela do Roteiro e possivel visualizar:

- Dias da semana com todos os clientes agendados para cada dia
- Porcentagem de atendimento realizado (considerando os agendados)
- Porcentagem de positivacao com relacao aos realizados

### 2.3. Legendas do Sistema

1. Dentro do Roteiro, clique no icone de tres pontos
2. Clique em "Legendas"
3. Sera aberta tela com ilustracao de todos os icones que podem ser apresentados junto ao nome dos clientes e o significado de cada um

### 2.4. Acoes no Roteiro

Na tela do Roteiro, ao clicar no icone de tres pontos que fica a frente do nome do cliente, surgirao algumas opcoes:

- Justificar Visita: abrira nova tela para que o vendedor preencha o motivo de nao venda e salve
- Outras opcoes seguirao o mesmo padrao, executando a acao desejada

#### Observacao sobre Check-in/Check-out

Dependendo de como estiver configurado, ao clicar nas opcoes (por exemplo, para justificar visita) pode estar atrelada a obrigatoriedade de realizar check-in antes, caso trabalhe com check-in/check-out.

### 2.5. Visualizar Roteiro de Outros Dias

#### Passos para Acessar

1. Ao acessar a tela inicial do aplicativo do maxPedido, clique na aba Clientes
2. Clique no icone de opcoes na barra superior da listagem e selecione a opcao "Roteiro"
3. Apos clicar em roteiro, no mesmo icone de opcoes na barra superior da tela de roteiro, clique na opcao "Selecionar Data"
4. Ira abrir opcao para que determine a data a qual deseja visualizar o respectivo roteiro
5. Selecione e clique em OK

#### Observacoes Importantes

- Caso nao tenha roteiro para o dia selecionado, o mesmo apenas ficara em branco nao contendo nenhuma informacao
- Caso o roteiro nao aparecer, verifique se o roteiro criado e de clientes da base do vendedor ou se ja existe uma carteira de clientes atribuida a ele
- Ao clicar em um dia da semana (por exemplo, sabado) e nao for apresentado nenhuma informacao, significa que nao ha Roteiro cadastrado para o dia em questao no ERP

---

## 3. Visita Avulsa

### 3.1. Configuracao de Permissoes

#### Habilitacao da Permissao no Usuario

1. Na tela inicial do maxPedido, acesse o Menu Cadastros > Usuarios
2. Busque pelo usuario que deseja e clique em pesquisar
3. Clique no icone de edicao na coluna acoes
4. Em permissoes do usuario, clique na aba permissoes
5. No quadro de Acesso a rotinas, busque pela permissao "Habilitar criacao de visita avulsa" e habilite

#### Configuracao do Parametro de Check-in

1. No menu Configuracoes > Parametro, busque pelo parametro `OBRIGA_CHECKIN_VISITA_AVULSA`
2. Para habilitar a opcao, clique no icone de edicao na coluna acoes
3. Selecione o usuario, habilite e clique em salvar

#### Observacao sobre Check-in em Visita Avulsa

Existe parametro que obriga o vendedor a realizar check-in em casos de visita avulsa. Verifique se o mesmo esta habilitado, pois ele influencia no processo dependendo de como deseja que seja realizado (ou seja, que ele faca ou nao check-in nesses casos).

### 3.2. Geracao de Visita Avulsa no Aplicativo

1. Na tela inicial do aplicativo, acesse o Menu Clientes
2. Selecione o cliente pressionando sobre o nome dele
3. Clique em "Gerar visita Avulsa"
4. Confirme para gerar visita avulsa e posteriormente iniciar novo pedido

---

## 4. Mapa de Oportunidades

Disponivel a partir da versao 4.011.3

### 4.1. Visao Geral

O Mapa de Oportunidades oferece ao vendedor uma interface visual em formato de mapa, permitindo visualizar de forma clara todos os clientes ja positivados de sua carteira, alem de identificar novas oportunidades de prospeccao dentro de um raio pre-definido.

Essa funcionalidade amplia a autonomia do vendedor, facilita o planejamento de rotas e melhora a eficiencia nas visitas comerciais.

### 4.2. Beneficios

- Visualizacao estrategica da carteira e de potenciais clientes
- Maior agilidade na organizacao das visitas e na definicao de prioridades
- Identificacao rapida de oportunidades de prospeccao proximas
- Aumento da eficiencia operacional e do aproveitamento da rota de vendas

### 4.3. Configuracao do Mapa de Oportunidades

#### Habilitacao do Parametro

1. Acesse a Central de configuracoes do maxPedido, clique no Menu lateral > Configuracoes > Parametros
2. Busque pelo Parametro `HABILITA_MAPA_OPORTUNIDADE` e clique em pesquisar
3. Clique sobre o icone de edicao da coluna Acoes e habilite o parametro, clique em salvar

#### Configuracao no Perfil de Usuarios

1. Ainda na Central de Configuracoes do maxPedido, clique em Cadastros > Perfil de usuarios
2. Selecione o perfil dos usuarios clicando no icone de edicao da coluna Acoes
3. Acesse a Aba Configuracoes > Mapa de Oportunidades
4. Faca a configuracao de CNAEs, Capital social (Opcional) e Distancia

#### Parametros de Distancia

| Parametro | Descricao |
|-----------|-----------|
| Distancia max. cadastro | Raio em metros maximo que o usuario pode cadastrar uma oportunidade prospectada |
| Distancia max. pesquisa | Raio maximo em quilometros para obtencao das oportunidades |

### 4.4. Utilizacao do Mapa de Oportunidades no Aplicativo

1. Na tela inicial do Aplicativo, acesse Clientes > icone de Mais opcoes > Mapa de oportunidades
2. Ao clicar no mapa de oportunidades, conseguira ver os seguintes botoes:
   - **Clientes**: Todos os clientes positivados ou nao na sua carteira no periodo
   - **Prospects**: Oportunidades capturadas no raio configurado da central
   - **Distancia**: Permite selecionar a distancia do raio em quilometros para as buscas dos clientes
3. Ao clicar em um cliente, podera clicar em "Cadastrar" (ira para a tela de formulario de cadastro) ou clicar em "Tracar Rota" (ira abrir o aplicativo padrao de Geolocalizacao do aparelho do vendedor)

---

## 5. Consultas no Aplicativo

### 5.1. Positivacao de Clientes

#### Acesso e Funcionalidade

1. Ao acessar o aplicativo do maxPedido, clique na aba Consultas
2. Clique em "Positivacao de Clientes"

Em positivacao de clientes, pode ser pesquisado os clientes positivados e nao positivados, ou seja, os clientes que ja tiveram e os que nao tiveram venda.

#### Utilizacao dos Filtros

Ao selecionar este menu, sera aberta uma nova tela para a escolha do tipo de filtro:

- Positivado ou Nao positivado
- Periodo que deseja ser pesquisado
- Filtros por Cliente ou Fornecedor

Ao preencher os campos desejados, clique em "Confirmar" para que seja impresso na tela o cliente e os produtos vendidos para este cliente.

#### Tipos de Pesquisa

**Pesquisa de Clientes Positivados:**
- Mostra clientes que tiveram vendas no periodo selecionado
- Lista os produtos vendidos para cada cliente

**Pesquisa de Clientes Nao Positivados:**
- Mostra clientes que nao tiveram vendas no periodo selecionado
- Permite identificar oportunidades de venda

#### Observacao

Para sair da tela de resultado da pesquisa de Clientes Positivados ou Nao Positivados, clique no botao voltar do seu aparelho.

---

### 5.2. Consulta de Titulos

#### Acesso

1. Ao acessar o aplicativo do maxPedido, clique na aba Consultas
2. Clique em "Titulos"

#### Configuracao e Parametrizacao

A consulta de titulos pode ser parametrizada para trazer:

- Todos os titulos do cliente (pagos e nao pagos)
- Titulos gerados apenas pelo vendedor ou nao
- Titulos apenas vencidos

Esta e uma parametrizacao feita dentro da parte administrativa.

#### Utilizacao

1. Ao pesquisar os titulos, sera impresso uma tela com a posicao financeira dos clientes
2. Ao selecionar o icone de filtros, sera exibido a opcao "Selecione os filtros" com opcoes de filtros para pesquisa
3. Clicando em "Mais filtros", ira abrir a tela de filtros adicionais para aprimorar a pesquisa

#### Legendas do Sistema

Ao selecionar o icone de legendas, sera mostrado todas as legendas do sistema, sendo possivel identificar pela cor o status do titulo do cliente.

---

### 5.3. Notificacao de Estoque

#### Acesso

1. Ao acessar o aplicativo do maxPedido, clique na aba Consultas
2. Clique em "Notificacao de Estoque"

#### Funcionalidade

Na opcao de Notificacao de Estoque, podera ser pesquisado as notificacoes de:

- Chegada de Mercadoria
- Termino de mercadoria

Esta notificacao e enviada pelo ERP.

#### Utilizacao

1. Selecione o tipo de notificacao
2. Selecione a filial
3. Informe a data de inicio e fim (De: / Ate:)
4. Sera impresso na tela as notificacoes recebidas

#### Como Funciona a Notificacao de Estoque

A notificacao de estoque consiste em verificar a tabela de estoque determinando a chegada de mercadoria/Termino de mercadoria:

- **Chegada de mercadoria**: Estoque anterior = 0 e estoque atual > 0
- **Termino de mercadoria**: Estoque anterior > 0 e estoque atual = 0

Ou seja:
- Tinha estoque anteriormente e agora o estoque ficou zerado = "Termino de mercadoria"
- Produtos que estavam com estoque igual a zero e a partir da movimentacao ficou maior que zero = "Chegada de mercadoria"

---

### 5.4. Politicas Comerciais

#### Acesso

1. Ao acessar o aplicativo do maxPedido, clique na aba Consultas
2. Clique em "Politicas Comerciais"

#### Funcionalidade

Em Politicas Comerciais sera emitida uma lista de politicas caso tenha alguma cadastrada para esta selecao.

#### Observacao Importante

As politicas comerciais sao cadastradas no ERP. Serao vistas as que foram liberadas para o forca de vendas, ou todos os tipos de vendas.

---

### 5.5. Historico de Pedidos

#### Acesso

1. Ao acessar o aplicativo do maxPedido, clique na aba Consultas
2. Clique em "Historico de Pedidos"

#### Utilizacao

1. Ao clicar em Historico de Pedidos, abrira uma nova tela solicitando que seja selecionado o periodo que deseja pesquisar os pedidos
2. Ao clicar em "Pesquisar", ja serao emitidos os pedidos na tela

#### Legendas do Sistema

Em legendas do Sistema e possivel identificar pela cor o status do Pedido.

#### Ordenacao

Em ordenacao podera ser selecionado a forma que serao posicionados os pedidos gerados na tela, e a ordem conforme a flag ordem decrescente:

- Caso desmarcada, sera em ordem crescente
- Caso marcada, sera em ordem decrescente

---

### 5.6. Consulta de Aniversarios

#### Acesso

1. Ao acessar o aplicativo do maxPedido, clique na aba Consultas
2. Clique em "Consulta de Aniversarios"

#### Funcionalidade

A consulta de Aniversarios ira trazer os contatos cadastrados para o cliente e suas datas de aniversarios de acordo com a pesquisa feita na tela inicial.

#### Observacao

Os contatos devem estar previamente cadastrados no ERP para que aparecem na consulta.

---

## 6. Boas Praticas e Recomendacoes

### 6.1. Gerenciamento de Rotas

- Sempre configure rotas no ERP antes de utilizar no aplicativo
- Verifique se os clientes estao atribuidos corretamente a carteira do vendedor
- Mantenha a periodicidade de visitas atualizada conforme mudancas no territorio

### 6.2. Uso de Visitas Avulsa

- Configure adequadamente as permissoes para evitar uso indevido
- Avalie a necessidade de obrigar check-in em visitas avulsas
- Utilize visitas avulsas para oportunidades nao programadas no roteiro

### 6.3. Consultas e Relatorios

- Utilize a consulta de positivacao para identificar clientes inativos
- Monitore regularmente a posicao de titulos dos clientes antes de realizar visitas
- Configure notificacoes de estoque para produtos estrategicos
- Aproveite o historico de pedidos para entender o padrao de compra dos clientes

### 6.4. Mapa de Oportunidades

- Configure o raio de pesquisa adequado ao territorio de cada vendedor
- Utilize CNAEs especificos para filtrar prospects qualificados
- Integre o mapa de oportunidades ao planejamento semanal de rotas

---

## 7. Solucao de Problemas Comuns

### 7.1. Roteiro Nao Aparece no Aplicativo

**Possiveis causas:**
- Roteiro nao esta cadastrado no ERP para o dia selecionado
- Cliente nao pertence a carteira do vendedor
- Parametro `HABILITA_CADASTRO_ROTA_CLIENTE` nao esta habilitado
- Opcao "Ocultar Ambos" esta marcada na configuracao de formularios

**Solucao:**
- Verifique o cadastro de rotas no ERP
- Confirme a atribuicao de clientes ao vendedor
- Valide as configuracoes de parametros e formularios

### 7.2. Nao Consegue Criar Visita Avulsa

**Possiveis causas:**
- Usuario nao possui permissao "Habilitar criacao de visita avulsa"
- Parametro de check-in obrigatorio pode estar impedindo

**Solucao:**
- Verifique e habilite a permissao no cadastro do usuario
- Ajuste o parametro `OBRIGA_CHECKIN_VISITA_AVULSA` conforme necessidade

### 7.3. Mapa de Oportunidades Nao Mostra Prospects

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