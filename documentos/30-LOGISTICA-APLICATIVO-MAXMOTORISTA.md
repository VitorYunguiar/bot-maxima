# Aplicativo MaxMotorista

Base de conhecimento sobre telas, campos, regras, parâmetros e tabelas relacionadas ao aplicativo MaxMotorista.

**Fonte convertida**: `Aplicativo MaxMotorista (3).docx`.

## 1. Erros Comuns

Esta seção descreve erros frequentes reportados no MaxMotorista, suas causas raiz, consultas de diagnóstico e encaminhamento recomendado.

### 1.1 Produtos faltando ou divergentes na listagem de itens da nota

#### Descrição

Ao abrir a nota fiscal dentro da tela de realização de entrega, o número de produtos exibidos pode ser menor do que o total real da nota. Exemplo: a nota possui 26 itens, mas o aplicativo mostra apenas 4 ou 6.

#### Causa raiz

A listagem de itens faz um `INNER JOIN` entre `MXMD_ITENS_NOTA_FISCAL` e `MXMD_PRODUTOS` com condições restritivas. O produto precisa estar com o mesmo `ID_CARREGAMENTO`, `NUMTRANSVENDA` e `NUMTRANSITEM` da nota. Quando o parâmetro `TRABALHA_EMBALAGEM_ERP_APK` está desativado no servidor, os produtos podem ser sincronizados com o carregamento incorreto. Com isso, as condições do `JOIN` deixam de ser atendidas e os itens são descartados da listagem.

#### Como diagnosticar

Substituir `[NUMERO_NOTA]` pelo número da nota afetada.

1. Total de itens registrados no banco local:

```sql
SELECT COUNT(*) AS TOTAL_ITENS
FROM MXMD_ITENS_NOTA_FISCAL NF
INNER JOIN MXMD_NOTAS_FISCAIS NOTA
    ON NOTA.ID = NF.ID_NOTA_FISCAL
WHERE NOTA.NUMERO_NOTA = '[NUMERO_NOTA]';
```

2. Total que o aplicativo exibe usando o `JOIN` restritivo:

```sql
SELECT COUNT(*)
FROM MXMD_ITENS_NOTA_FISCAL NF
INNER JOIN MXMD_NOTAS_FISCAIS NOTA
    ON NOTA.ID = NF.ID_NOTA_FISCAL
INNER JOIN MXMD_PRODUTOS PROD
    ON PROD.ID = NF.ID_PRODUTO
   AND NOTA.ID_CARREGAMENTO = PROD.ID_CARREGAMENTO
   AND PROD.NUMTRANSVENDA = NOTA.NUMERO_TRANSVENDA
   AND PROD.NUMTRANSITEM = NF.NUMTRANSITEM
WHERE NOTA.NUMERO_NOTA = '[NUMERO_NOTA]';
```

3. Itens que estão sendo perdidos e motivo provável:

```sql
SELECT
    NF.ID_PRODUTO,
    PROD.DESCRICAO,
    PROD.ID_CARREGAMENTO,
    PROD.NUMTRANSVENDA,
    PROD.NUMTRANSITEM,
    NF.NUMTRANSITEM AS NF_NUMTRANSITEM,
    NOTA.NUMERO_TRANSVENDA,
    NOTA.ID_CARREGAMENTO AS CARREG_NOTA
FROM MXMD_ITENS_NOTA_FISCAL NF
INNER JOIN MXMD_NOTAS_FISCAIS NOTA
    ON NOTA.ID = NF.ID_NOTA_FISCAL
LEFT JOIN MXMD_PRODUTOS PROD
    ON PROD.ID = NF.ID_PRODUTO
WHERE NOTA.NUMERO_NOTA = '[NUMERO_NOTA]';
```

Se `ID_CARREGAMENTO`, `NUMTRANSVENDA` ou `NUMTRANSITEM` do produto divergirem dos valores da nota, o erro está confirmado.

#### Resolução

Verificar no servidor se o parâmetro `TRABALHA_EMBALAGEM_ERP_APK` está ativo para o cliente. Esse parâmetro garante que os produtos sejam sincronizados com o carregamento correto e também faz o aplicativo exibir a embalagem do produto conforme cadastro do ERP.

Atenção: ativar esse parâmetro apenas para versões do aplicativo 4.43.0 ou superiores.

### 1.2 Entregas não aparecem na listagem

#### Descrição

O motorista abre o aplicativo com um romaneio iniciado, mas a lista de entregas aparece vazia.

#### Causa raiz

A causa principal é ausência de notas na base local do APK. A listagem de entregas exige registros vinculados em `MXMD_NOTAS_FISCAIS` e `MXMD_ITENS_NOTA_FISCAL` para cada entrega. Se as notas fiscais não foram sincronizadas para o dispositivo, as entregas são filtradas e não aparecem.

Outra causa possível é o parâmetro `DIAS_JOB_NOTAS_FISCAIS` no servidor, na tabela `MXMP_PARAMETROS`. Esse parâmetro define quantos dias retroativos a job considera para sincronizar notas fiscais. O padrão é 30 dias. Assim, só descem notas cujo `DTSAIDA` do carregamento seja maior ou igual à data atual menos a quantidade de dias configurada.

#### Como diagnosticar

Substituir `[ID_CARREGAMENTO]` pelo carregamento afetado.

1. Verificar se as entregas existem no banco local:

```sql
SELECT
    ent.ID,
    ent.ID_CARREGAMENTO,
    carreg.ID_ROMANEIO,
    ent.SITUACAO
FROM MXMD_ENTREGAS ent
INNER JOIN MXMD_CARREGAMENTOS carreg
    ON carreg.ID = ent.ID_CARREGAMENTO
WHERE ent.ID_CARREGAMENTO = '[ID_CARREGAMENTO]';
```

2. Verificar se as notas fiscais desceram:

```sql
SELECT COUNT(*) AS TOTAL_NOTAS
FROM MXMD_NOTAS_FISCAIS
WHERE ID_CARREGAMENTO = '[ID_CARREGAMENTO]';
```

3. Verificar notas e itens por entrega:

```sql
SELECT
    ent.ID AS ID_ENTREGA,
    (
        SELECT COUNT(*)
        FROM MXMD_NOTAS_FISCAIS NF
        WHERE NF.ID_ENTREGA = ent.ID
    ) AS QTD_NOTAS,
    (
        SELECT COUNT(*)
        FROM MXMD_ITENS_NOTA_FISCAL ITEM
        INNER JOIN MXMD_NOTAS_FISCAIS NF
            ON NF.ID = ITEM.ID_NOTA_FISCAL
        WHERE NF.ID_ENTREGA = ent.ID
    ) AS QTD_ITENS
FROM MXMD_ENTREGAS ent
WHERE ent.ID_CARREGAMENTO = '[ID_CARREGAMENTO]';
```

Se `QTD_NOTAS = 0` e `QTD_ITENS = 0`, as notas não foram sincronizadas. O problema está no servidor/sincronização e deve ser escalado ao backend.

4. Verificar o parâmetro de dias da job no servidor:

```sql
SELECT *
FROM MXMP_PARAMETROS
WHERE NOME = 'DIAS_JOB_NOTAS_FISCAIS';
```

Se a `DTSAIDA` do carregamento afetado for anterior ao limite configurado, as notas fiscais não serão sincronizadas para o dispositivo. Aumentar o valor do parâmetro pode resolver, mas só deve ser feito quando necessário, porque aumenta o volume de processamento.

#### Resolução

Escalar para o backend informando o ID do carregamento e o ID do romaneio afetados, caso a validação local confirme ausência de notas/itens ou a parametrização da job não explique o caso. O time deve verificar por que as notas fiscais não foram incluídas na sincronização para o dispositivo do motorista.

### 1.3 Entregas duplicadas na listagem

#### Descrição

O motorista visualiza o mesmo cliente duas vezes na lista de entregas, como se fossem entregas separadas quando deveriam estar agrupadas em um único card.

#### Causa raiz

O aplicativo agrupa entregas do mesmo cliente em um único card quando possuem o mesmo `ID_CLIENTE`, `ID_ENDERECO_ENT_PED` e situação. Se, no momento da geração das entregas pela job, um pedido estiver sem `CODENDENTCLI` e outro com `CODENDENTCLI` preenchido, o sistema interpreta os pedidos como endereços diferentes e gera duas entregas separadas.

Mesmo que o `CODENDENTCLI` seja corrigido posteriormente pela integração do cliente, essa alteração não refaz o agrupamento, porque as entregas já foram geradas.

#### Como diagnosticar

Substituir `[ID_CLIENTE]` pelo código do cliente afetado.

```sql
SELECT
    ID,
    ID_CLIENTE,
    ID_CARREGAMENTO,
    ID_ENDERECO_ENT_PED,
    SITUACAO,
    SITUACAO_ORIG
FROM MXMD_ENTREGAS
WHERE ID_CLIENTE = '[ID_CLIENTE]'
ORDER BY ID;
```

Se as duas entregas aparecerem com `ID_ENDERECO_ENT_PED` diferentes, por exemplo `NULL` e `1`, a duplicação é confirmada como problema de geração no backend.

#### Resolução

Escalar para backend/implantação informando os IDs dos pedidos afetados quando a causa não estiver clara. Se a divergência for `CODENDENTCLI`, orientar que o campo precisa estar corretamente preenchido antes da execução da job de montagem de carga e faturamento. Alterações posteriores nesse campo não afetam o agrupamento já criado no aplicativo.

## 2. Entrega Transbordo

### Descrição

Tela exibida ao motorista quando ele inicia uma atividade do tipo Transbordo.

#### Observação visual da imagem

A imagem mostra a tela **Entrega Transbordo** com barra superior azul, botões de cancelar e finalizar, origem/destino/carregamentos no cabeçalho, cards de notas/peso/volume, botão **ASSINATURA DIGITAL**, campo de observação preenchido e uma foto já anexada. Ela confirma que a tela combina dados resumidos do transbordo com ações de assinatura, observação e registro fotográfico antes da finalização.

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

- Campo para registro fotográfico da entrega. O comportamento varia conforme o parâmetro PERMITIR_REGISTRAR_15_FOTOS_TRANSBORDO:
- Parâmetro inativo (padrão): Exibe um campo de foto único. A foto é salva na coluna FOTO_TRANSBORDO da tabela MXMD_ENTREGAS. Ao reabrir a tela, a foto registrada anteriormente é exibida automaticamente.
- **Parâmetro ativo**: Exibe uma grade de até 15 fotos organizadas em 3 colunas. Cada foto pode ser visualizada, substituída ou excluída individualmente. As fotos são salvas na tabela MXMD_FOTOS com TIPO_REGISTRO = 'TB', identificadas por hash único. Ao reabrir a tela, todas as fotos registradas anteriormente são exibidas automaticamente. Fotos já sincronizadas com o servidor ficam bloqueadas para edição e exclusão.

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
- Ao cancelar a atividade, todas as fotos registradas na tabela MXMD_FOTOS para o transbordo são removidas automaticamente, além da limpeza do campo FOTO_TRANSBORDO da tabela MXMD_ENTREGAS.
- As fotos de transbordo registradas com o parâmetro ativo são enviadas ao servidor durante a sincronização, via S3 e endpoint v2/fotos. Enquanto não sincronizadas, permanecem com ENVIADO = 0 na tabela MXMD_FOTOS.

#### Parâmetros que afetam o comportamento

- **PERMITIR_REGISTRAR_15_FOTOS_TRANSBORDO** - quando ativo, substitui o campo de foto único por uma grade que suporta até 15 fotos por atividade de transbordo.

## 3. Ponto de Parada

### Descrição

Tela exibida ao motorista quando ele inicia uma atividade do tipo Ponto de Parada. O ponto de parada representa uma parada programada na rota que não é necessariamente uma entrega — pode ser um posto de gasolina, uma parada obrigatória, um ponto de apoio, entre outros.

#### Observação visual da imagem

A imagem mostra a tela **Ponto de Parada** com descrição do ponto, observação de montagem em destaque, seleção **Atividade Executada?** com Sim marcado, campo de observação do motorista e área de foto vazia com ícone de câmera. Ela confirma que a parada pode registrar execução, observação e foto mesmo quando não é uma entrega.

### Como acessar

O motorista acessa essa tela ao tocar em "Iniciar Atividade" na tela de detalhes de um Ponto de Parada.

### Informações exibidas

#### Descrição

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

## 4. Recebíveis e Títulos

### Descrição

Tela exibida ao motorista para registrar o recebimento de títulos financeiros vinculados a uma entrega ou a um cliente. Permite lançar, editar e excluir recebimentos por título, com suporte a diferentes formas de pagamento.

#### Observação visual da imagem

A imagem mostra a tela **Recebíveis** de uma entrega, com dados do cliente, botão **RECEBER TODOS**, um título listado com cobrança, parcela, número do título, valor, juros, saldo devedor, emissão e vencimento. A barra inferior consolida **Total**, **Recebido** e **Em Aberto**, destacando o saldo pendente em vermelho.

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

A cor do nome da cobrança indica a situação do título:
- Verde — título totalmente quitado.
- Vermelho — título vencido.
- Azul — título pendente dentro do prazo.

Ao expandir um título, são exibidos os recebimentos já lançados, com tipo, ícone e valor. Recebimentos sincronizados com o servidor não podem ser excluídos.

#### Barra de Totais

Exibida na parte inferior da tela com três colunas:
- Total — soma dos valores nominais de todos os títulos.
- Recebido — soma de todos os recebimentos lançados.
- Em Aberto — diferença entre Total e Recebido. Exibido em vermelho quando há saldo pendente e em preto quando zerado.

#### Dialog de Lançamento de Recebimento

Aberto ao tocar em "+ Adicionar" em um título expandido ou ao tocar em um recebível existente para edição.

Campos disponíveis:
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
- **O tipo de recebimento é definido automaticamente**: Cheque para cobranças CHD1, CHD3, CHP, CHV, CH, CHDV, CHPC e DES2; Dinheiro para os demais.
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

- **EXIBIR_RECEBIVEIS_NO_ANDROID** - habilita a funcionalidade de recebíveis no aplicativo. Quando inativo, o botão de acesso à tela não é exibido.
- **FOTO_RECEBIMENTO_DINHEIRO_OBRIGATORIA** - quando ativo, impede salvar um recebimento do tipo Dinheiro sem foto registrada.
- **FOTO_RECEBIMENTO_CHEQUE_OBRIGATORIA** - quando ativo, impede salvar um recebimento do tipo Cheque sem foto registrada.
- **CAMPOS_COMPLEMENTARES_RECEBIM_CHEQUE_OBRIGATORIOS** - quando ativo, os campos banco, agência, conta, número do cheque e CPF/CNPJ tornam-se obrigatórios para recebimentos do tipo Cheque.
- **OPCAO_DE_RECEBIMENTO_CONFORME_CODCOB** - quando ativo, filtra os títulos exibidos para apenas os de cobrança Dinheiro (DINH, DH) e Cheque (CH). Também ajusta o tipo padrão e as opções disponíveis no dropdown conforme a cobrança do título: para cobranças de cheque, exibe apenas a opção Cheque; para cobranças de dinheiro, exibe Dinheiro, Cartão Avulso e Pix Avulso.
- **OCULTAR_TITULO_COBRANCA_BOLETO** - quando ativo, oculta títulos com cobrança Boleto (BK) da listagem.

## 5. Despesas

### Descrição

Tela exibida ao motorista para registrar despesas operacionais realizadas durante a jornada, como abastecimento, pedágio, alimentação, entre outros. Permite lançar, editar e excluir despesas com suporte a foto e localização GPS.

#### Observação visual da imagem

A imagem mostra a lista de **Despesas**, com botão de voltar, filtro por calendário, itens de despesa com foto/ícone, tipo, data, carregamento e valor. O primeiro item exibe ícone de exclusão, indicando registro ainda editável ou não sincronizado, e há botão flutuante **NOVA DESPESA** para criar lançamento.

### Como acessar

O motorista acessa essa tela pelo menu principal do aplicativo, tocando na opção “Despesas”.

### Informações exibidas

#### Lista de Despesas

Exibe as despesas do dia atual por padrão, podendo ser filtradas por data. Cada item da lista exibe as seguintes informações, obtidas da tabela MXMD_DESPESAS:
- **Foto**: Imagem circular associada à despesa. Obtida da coluna NOME_FOTO da tabela MXMD_DESPESAS.
- **Tipo**: Descrição do tipo de despesa. Obtido da coluna DESCRICAO da tabela MXMD_TIPO_DESPESA via coluna ID_TIPO_DESPESA.
- **Data e hora**: Data e hora do lançamento da despesa. Obtido da coluna DATA da tabela MXMD_DESPESAS.
- **Carregamento**: Identificador do carregamento vinculado. Obtido da coluna ID_CARREGAMENTO da tabela MXMD_DESPESAS. Exibido apenas quando preenchido.
- **Valor**: Valor da despesa. Obtido da coluna VALOR da tabela MXMD_DESPESAS.
- **Observação**: Observação registrada pelo motorista. Obtido da coluna OBSERVACAO da tabela MXMD_DESPESAS. Exibida apenas quando preenchida.

#### Formulário de Lançamento de Despesa

Aberto ao tocar em “NOVA DESPESA” ou ao tocar em uma despesa editável da lista. Campos disponíveis:
- **Foto**: Campo para registro fotográfico da despesa. Ao tocar, abre a câmera diretamente quando não há foto registrada, ou exibe o preview da foto existente com opção de manter ou substituir. A foto é salva na coluna FOTO e seu nome na coluna NOME_FOTO da tabela MXMD_DESPESAS.
- **Valor**: Valor monetário da despesa. Campo obrigatório. Salvo na coluna VALOR da tabela MXMD_DESPESAS.
- **Tipo de Despesa**: Seleção do tipo via dropdown. Campo obrigatório. Os tipos disponíveis são carregados da tabela MXMD_TIPO_DESPESA. Salvo na coluna ID_TIPO_DESPESA da tabela MXMD_DESPESAS.
- **Carregamento**: Seleção do carregamento ao qual a despesa está vinculada via dropdown. Exibe o identificador e o destino do carregamento. Obrigatório conforme parâmetro. Salvo na coluna ID_CARREGAMENTO da tabela MXMD_DESPESAS.
- **Observação**: Campo de texto livre para registro de qualquer observação sobre a despesa. Salvo na coluna OBSERVACAO da tabela MXMD_DESPESAS.

### Ações disponíveis

#### NOVA DESPESA

- Botão flutuante na parte inferior da tela. Abre o formulário de lançamento em branco.
- Valida os campos obrigatórios antes de salvar. Erros são exibidos inline no formulário.
- Registra a localização GPS no momento do lançamento. Salvo nas colunas LATITUDE e LONGITUDE da tabela MXMD_DESPESAS.
- Após salvar com sucesso, a despesa aparece no topo da lista e o formulário é fechado automaticamente.

#### Editar Despesa

- Disponível apenas para despesas ainda não sincronizadas com o servidor.
- Ao tocar em uma despesa sincronizada, exibe a mensagem “Esse registro já foi enviado e não pode ser editado”.
- Abre o formulário com os dados da despesa preenchidos. Atualiza o registro na tabela MXMD_DESPESAS ao salvar.

#### Excluir Despesa

- Ícone de exclusão exibido apenas para despesas ainda não sincronizadas.
- Exibe diálogo de confirmação antes de executar.
- Remove o registro da tabela MXMD_DESPESAS e atualiza a lista automaticamente.

#### Filtro por Data

- Ícone de calendário na barra superior. Abre um seletor de data.
- Ao aplicar, recarrega a lista exibindo apenas despesas do dia selecionado. A data padrão é o dia atual.

### Regras de negócio

- A listagem exibe separadamente despesas locais (ainda não sincronizadas) e despesas já enviadas ao servidor, obtidas via API pelo endpoint consultaDespesas.
- Despesas sincronizadas não podem ser editadas nem excluídas pelo motorista.
- A foto é comprimida automaticamente antes de ser salva localmente.
- Ao editar uma despesa sem alterar a foto, a imagem existente é preservada automaticamente.
- A lista é ordenada por data de lançamento de forma decrescente.

#### Parâmetros que afetam o comportamento

- **LANCAR_DESP_SEM_CARREG** - quando ativo, o campo de carregamento não é obrigatório. O label do campo exibe “Carregamento” sem asterisco.
- **OBRIGAR_REGISTRO_FOTO_DESPESAS** - quando ativo, impede salvar uma despesa sem foto registrada. A mensagem de erro é exibida inline no formulário.
