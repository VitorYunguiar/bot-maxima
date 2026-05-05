# Aplicativo MaxMotorista

Base de conhecimento sobre telas, campos, regras e tabelas relacionadas ao aplicativo MaxMotorista.

## 1. Entrega Transbordo

### Descrição

Tela exibida ao motorista quando ele inicia uma atividade do tipo Transbordo.

### Como acessar

O motorista acessa essa tela ao tocar em "Iniciar Atividade" na tela de detalhes de uma entrega do tipo Transbordo.

### Informações exibidas

#### Cabeçalho
- **Origem**: Código do ponto de origem da carga. Obtido da coluna CD_ORIGEM da tabela MXMD_INFO_TRANSBORDO.
- **Destino**: Código do ponto de destino da carga. Obtido da coluna CD_DESTINO da tabela MXMD_INFO_TRANSBORDO.
- **Carregamentos**: Quantidade de carregamentos envolvidos no transbordo. Obtido da coluna QT_CARREGAMENTOS da tabela MXMD_INFO_TRANSBORDO.

#### Cards de Resumo

- **Notas**: Quantidade de notas fiscais do transbordo. Obtido da coluna QT_NF da tabela MXMD_INFO_TRANSBORDO.
- **Peso**: Peso total da carga em kg. Obtido da coluna PESO da tabela MXMD_INFO_TRANSBORDO.
- **Volume**: Volume total da carga em m³. Obtido da coluna VOLUME da tabela MXMD_INFO_TRANSBORDO.
#### Observação de Montagem
- Campo exibido apenas quando existe uma observação cadastrada para o transbordo. Obtido da coluna OBSERVACAO da tabela MXMD_INFO_TRANSBORDO.

#### Assinatura Digital

- Botão que abre a tela de assinatura digital, onde o motorista registra a confirmação do recebimento da carga pelo destinatário.
#### Observação do Motorista
- Campo de texto livre onde o motorista pode registrar qualquer observação relevante sobre a atividade. Esse texto é salvo na coluna OBSERVACOES da tabela MXMD_ENTREGAS.

#### Foto

- Campo para registro fotográfico da entrega. A foto é salva na coluna FOTO_TRANSBORDO da tabela MXMD_ENTREGAS. Ao reabrir a tela, a foto registrada anteriormente é exibida automaticamente.

### Ações disponíveis

#### Finalizar (✓)
- Registra a conclusão do transbordo.
- Salva a observação do motorista e define a data/hora de término.
- Atualiza o status da entrega na tabela MXMD_ENTREGAS.
- Exibe diálogo de confirmação antes de executar.
- Após sucesso, fecha a tela automaticamente.

#### Cancelar (X)

- Cancela a atividade de transbordo.
- Atualiza o status da entrega para cancelado.
- Exibe diálogo de confirmação antes de executar.
- Após sucesso, fecha a tela automaticamente.
#### Botão Voltar do Celular
- Ao pressionar o botão voltar, o sistema exibe um aviso orientando o motorista a finalizar ou cancelar a atividade antes de sair. A tela permanece aberta após fechar o aviso.

### Regras de negócio

- A foto é opcional, salvo quando o parâmetro OBRIGAR_REGISTRO_FOTO_ENTREGA estiver ativo.
- A observação de montagem é exibida apenas quando o campo OBSERVACAO da tabela MXMD_INFO_TRANSBORDO não estiver vazio.
- Não é possível sair da tela sem antes finalizar ou cancelar a atividade.

## 2. Ponto de Parada

### Descrição

Tela exibida ao motorista quando ele inicia uma atividade do tipo Ponto de Parada. O ponto de parada representa uma parada programada na rota que não é necessariamente uma entrega — pode ser um posto de gasolina, uma parada obrigatória, um ponto de apoio, entre outros.

### Como acessar

O motorista acessa essa tela ao tocar em "Iniciar Atividade" na tela de detalhes de um Ponto de Parada.

### Informações exibidas

### Descrição

- Nome ou descrição do ponto de parada. Obtido da coluna DESCRICAO da tabela MXMD_PONTO_PARADA.
#### Observação de Montagem
- Informação adicional cadastrada para o ponto de parada, exibida em destaque quando disponível. Obtido da coluna OBSERVACAO da tabela MXMD_PONTO_PARADA. O campo é ocultado automaticamente quando não há observação cadastrada.

#### Atividade Executada?

- Seleção entre Sim e Não, indicando se o motorista executou a atividade prevista no ponto de parada.
- O valor inicial é carregado da coluna EXECUTADO da tabela MXMD_PONTO_PARADA. Quando não há valor definido, o padrão é Sim.
- O valor selecionado pelo motorista é salvo ao finalizar a atividade.
#### Observação do Motorista
- Campo de texto livre para registro de qualquer observação do motorista sobre a parada. Salvo na coluna OBSERVACAO_MOTORISTA da tabela MXMD_PONTO_PARADA.

#### Foto

- Campo para registro fotográfico do ponto de parada. A foto é salva na coluna FOTO da tabela MXMD_PONTO_PARADA. Ao reabrir a tela, a foto registrada anteriormente é exibida automaticamente.

### Ações disponíveis

#### Finalizar (✓)
- Registra a conclusão do ponto de parada.
- Salva o valor de "Atividade Executada", a observação do motorista e define a data/hora de término.
- Atualiza o status do ponto na tabela MXMD_PONTO_PARADA.
- Exibe diálogo de confirmação antes de executar.
- Após sucesso, fecha a tela automaticamente.

#### Cancelar (X)

- Cancela a atividade do ponto de parada.
- Atualiza o status para cancelado na tabela MXMD_PONTO_PARADA.
- Exibe diálogo de confirmação antes de executar.
- Após sucesso, fecha a tela automaticamente.
#### Botão Voltar do Celular
- Ao pressionar o botão voltar, o sistema exibe um aviso orientando o motorista a finalizar ou cancelar a atividade antes de sair. A tela permanece aberta após fechar o aviso.

### Regras de negócio

- A foto é opcional.
- A observação de montagem é exibida apenas quando o campo OBSERVACAO não estiver vazio.
- O campo "Atividade Executada" sempre inicia marcado como Sim quando não há valor definido no banco.
- Não é possível sair da tela sem antes finalizar ou cancelar a atividade.

## 3. Recebíveis e Títulos

### Descrição

Tela exibida ao motorista para registrar o recebimento de títulos financeiros vinculados a uma entrega ou a um cliente. Permite lançar, editar e excluir recebimentos por título, com suporte a diferentes formas de pagamento.

### Como acessar

O motorista acessa essa tela ao tocar em "Informar Recebimentos" na tela de detalhes de uma entrega. Ao tocar, um diálogo é exibido com duas opções:
- Realizar recebimento somente das notas desta entrega — lista apenas os títulos vinculados às notas fiscais da entrega selecionada.
- Listar todos os títulos em aberto deste cliente — lista todos os títulos em aberto do cliente, independentemente da entrega.

### Informações exibidas

#### Cabeçalho do Cliente
- Código e razão social do cliente. Obtidos das colunas ID e CLIENTE da tabela MXMD_CLIENTES.
- Nome fantasia do cliente. Obtido da coluna FANTASIA da tabela MXMD_CLIENTES.
- Quantidade de notas fiscais e quantidade de itens da entrega.
#### Botão "RECEBER TODOS"
- Exibido logo abaixo do cabeçalho do cliente, com fundo acinzentado.
- Visível apenas quando a tela é aberta no contexto de uma entrega específica ("somente das notas desta entrega").
- Ao tocar, realiza automaticamente o recebimento de todos os títulos pendentes pelo valor exato do saldo restante de cada um.
- Títulos em processo de sincronização são ignorados e uma mensagem de aviso é exibida ao final.
#### Lista de Títulos

Cada título exibe as seguintes informações, obtidas da tabela MXMD_TITULOS:
- Nome da cobrança. Obtido da tabela MXMD_COBRANCAS via coluna ID_COBRANCA.
- Número da parcela. Obtido da coluna PRESTACAO.
- Número da nota fiscal. Obtido da coluna DUPLICATA.
- Valor total do título. Obtido da coluna VALOR.
- Juros. Calculado como diferença entre SALDO e VALOR.
- Saldo restante. Calculado como VALOR - VALOR_RECEBIDO.
- Data de emissão. Obtida da coluna DATA_EMISSAO.
- Data de vencimento. Obtida da coluna DATA_VENCIMENTO.
**A cor do nome da cobrança indica a situação do título**: 
- Verde — título totalmente quitado.
- Vermelho — título vencido.
- Azul — título pendente dentro do prazo.
Ao expandir um título, são exibidos os recebimentos já lançados, com tipo, ícone e valor. Recebimentos sincronizados com o servidor não podem ser excluídos.

#### Barra de Totais

**Exibida na parte inferior da tela com três colunas**: 
- Total — soma dos valores nominais de todos os títulos.
- Recebido — soma de todos os recebimentos lançados.
- Em Aberto — diferença entre Total e Recebido. Exibido em vermelho quando há saldo pendente e em preto quando zerado.
#### Dialog de Lançamento de Recebimento
Aberto ao tocar em "+ Adicionar" em um título expandido ou ao tocar em um recebível existente para edição.
#### Campos disponíveis

- Foto — registro fotográfico do recebimento. Exibida automaticamente quando já registrada.
- Tipo — forma de pagamento selecionada via dropdown: Dinheiro, Cartão Avulso, Pix Avulso, Cheque, Cartão.
- Campos de Cheque — exibidos condicionalmente ao selecionar o tipo Cheque: banco, agência, conta, número do cheque e CPF/CNPJ.
- Valor — valor do recebimento. Preenchido automaticamente com o saldo restante do título.

- Observações — campo de texto livre.
O tipo padrão ao abrir o dialog é sempre Dinheiro, independentemente do tipo de cobrança do título, salvo quando o parâmetro OPCAO_DE_RECEBIMENTO_CONFORME_CODCOB estiver ativo.
Recebimentos sincronizados com o servidor são exibidos em modo somente leitura, sem possibilidade de edição ou exclusão.

### Ações disponíveis

#### Salvar Recebimento

- Valida os campos obrigatórios conforme os parâmetros do sistema.
- Cria um novo recebível ou atualiza o existente na tabela MXMD_RECEBIVEIS.
- Atualiza o valor recebido do título na tabela MXMD_TITULOS.
- Atualiza os totalizadores da barra inferior em tempo real.

#### Excluir Recebimento

- Remove o recebível da tabela MXMD_RECEBIVEIS.
- Disponível apenas para recebimentos ainda não sincronizados com o servidor.
- Atualiza os totalizadores em tempo real.

#### Receber Todos

- Lança automaticamente um recebível para cada título pendente com saldo maior que zero.
- **O tipo de recebimento é definido automaticamente**: Cheque para cobrancas CHD1, CHD3, CHP, CHV, CH, CHDV, CHPC e DES2; Dinheiro para os demais.
- Títulos bloqueados por sincronização são ignorados.
#### Botão Voltar do Celular / Seta de Voltar
- Ao tentar sair, o sistema verifica se existem títulos com saldo ainda pendente.
- Caso existam, exibe um diálogo perguntando se o motorista deseja marcar a entrega como Recebimento Pendente.
- Confirmando, a situação da entrega é atualizada na tabela MXMD_ENTREGAS.
- Recusando, a tela é fechada sem alteração.
- Caso não haja títulos pendentes, a tela é fechada diretamente.

### Regras de negócio

- A tela só exibe títulos com ID_COBRANCA <> 'BNF'.
- No modo "somente desta entrega", os títulos são filtrados pelo join entre MXMD_TITULOS.DUPLICATA e MXMD_NOTAS_FISCAIS.NUMERO_NOTA para a entrega selecionada.
- O campo CPF/CNPJ do cheque é validado — apenas CPFs e CNPJs válidos são aceitos. Os caracteres não numéricos são removidos automaticamente antes da validação.
- O campo de observação é truncado automaticamente em 200 caracteres.
- Para recebimentos do tipo Dinheiro, Cartão Avulso e Pix Avulso, os campos de cheque são sempre ignorados mesmo que preenchidos.
#### Parâmetros que afetam o comportamento

- EXIBIR_RECEBIVEIS_NO_ANDROID — habilita a funcionalidade de recebíveis no aplicativo. Quando inativo, o botão de acesso à tela não é exibido.
- FOTO_RECEBIMENTO_DINHEIRO_OBRIGATORIA — quando ativo, impede salvar um recebimento do tipo Dinheiro sem foto registrada.
- FOTO_RECEBIMENTO_CHEQUE_OBRIGATORIA — quando ativo, impede salvar um recebimento do tipo Cheque sem foto registrada.
- CAMPOS_COMPLEMENTARES_RECEBIM_CHEQUE_OBRIGATORIOS — quando ativo, os campos banco, agência, conta, número do cheque e CPF/CNPJ tornam-se obrigatórios para recebimentos do tipo Cheque.
- OPCAO_DE_RECEBIMENTO_CONFORME_CODCOB — quando ativo, filtra os títulos exibidos para apenas os de cobrança Dinheiro (DINH, DH) e Cheque (CH). Também ajusta o tipo padrão e as opções disponíveis no dropdown conforme a cobrança do título: para cobrancas de cheque, exibe apenas a opção Cheque; para cobrancas de dinheiro, exibe Dinheiro, Cartão Avulso e Pix Avulso.
- OCULTAR_TITULO_COBRANCA_BOLETO — quando ativo, oculta títulos com cobrança Boleto (BK) da listagem.
