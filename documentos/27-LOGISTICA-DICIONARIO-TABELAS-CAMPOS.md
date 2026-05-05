# Dicionário de Tabelas e Campos da Logística

Referência técnica de tabelas e campos usados pelos componentes de logística. O conteúdo está separado por base para facilitar recuperação no RAG.

## Tabelas do aplicativo maxMotorista

# Tabelas do Aplicativo maxMotorista

Dicionário de tabelas locais do aplicativo, com campos, tipos e chaves.

## Visão geral

Esta base contém **69 tabelas** e **560 campos**.

## Como usar esta referência

- Consulte pelo nome da tabela quando o problema envolver persistência, sincronização, integração ou diagnóstico técnico.
- Consulte pelo nome do campo quando o chamado mencionar coluna, chave, status, data, usuário, entrega, pedido, rota ou sincronização.
- Cada tabela fica em uma seção própria para manter o contexto dos campos no mesmo chunk.

## MXMD_AGENDAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DATA | DATE | permite nulo |  |  |
| HORA_INICIAL | VARCHAR(5) | permite nulo |  |  |
| HORA_FINAL | VARCHAR(5) | permite nulo |  |  |
| OBSERVACAO | VARCHAR(200) | permite nulo |  |  |
| ID_ENTREGA | INTEGER | permite nulo |  |  |

## MXMD_AJUDANTES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| MATRICULA | INTEGER | permite nulo |  |  |
| NOME | TEXT | permite nulo |  |  |

## MXMD_AUSENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DATA_INICIO | DATE | obrigatório |  |  |
| DATA_FIM | DATE | obrigatório |  |  |

## MXMD_CARREGAMENTOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório | PK |  |
| DESTINO | VARCHAR(20) | permite nulo |  |  |
| SEQUENCIADO | INTEGER | permite nulo |  |  |
| PLACA | VARCHAR(10) | permite nulo |  |  |
| ID_ROMANEIO | INTEGER(10) | permite nulo |  |  |
| POSICAO | VARCHAR(1) | permite nulo |  |  |
| ID_AJUDANTE1 | VARCHAR(50) | permite nulo |  |  |
| ID_AJUDANTE2 | VARCHAR(50) | permite nulo |  |  |
| ID_AJUDANTE3 | VARCHAR(50) | permite nulo |  |  |

## MXMD_CLIENTES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório | PK |  |
| CLIENTE | VARCHAR(60) | obrigatório |  |  |
| FANTASIA | VARCHAR(60) | permite nulo |  |  |
| CGC | VARCHAR(18) | obrigatório |  |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |
| EMAIL | VARCHAR(100) | permite nulo |  |  |
| EMAILNFE | VARCHAR(100) | permite nulo |  |  |
| TEMPO_MEDIO_CLIENTE | REAL | permite nulo |  |  |
| TEMPO_MEDIO_ENTREGA | REAL | permite nulo |  |  |

## MXMD_COB_PREVISTAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_ROMANEIO | INTEGER | permite nulo |  |  |
| CODCOB | STRING | permite nulo |  |  |
| NOME_COBRANCA | STRING | permite nulo |  |  |
| VALOR_TOTAL | REAL | permite nulo |  |  |
| QT_NF | INTEGER | permite nulo |  |  |

## MXMD_CONTROLE_SINC

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_ENTREGA | INTEGER | permite nulo | PK |  |
| SITUACAO | VARCHAR(2) | obrigatório |  |  |
| DT_ENVIO | DATETIME | permite nulo |  |  |

## MXMD_DESCANSO_JORNADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo |  |  |
| ID_JORNADA | INTEGER | permite nulo |  |  |
| INICIO_DESCANSO | DATE | permite nulo |  |  |
| FIM_DESCANSO | DATE | permite nulo |  |  |

## MXMD_DESCARGA_CANCELADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_ENTREGA | INTEGER | obrigatório |  |  |
| DATA_CHECKIN | DATE | obrigatório |  |  |
| DATA_INICIO_DESCARGA | DATE | permite nulo |  |  |
| DATA_CANCELAMENTO_DESCARGA | DATE | permite nulo |  |  |
| ID_MOTIVO_CANCELAMENTO | INTEGER | obrigatório |  |  |
| OBSERVACOES | STRING | permite nulo |  |  |
| FOTO_CHECKIN | BLOB | permite nulo |  |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER | permite nulo |  | padrão 0 |

## MXMD_DESCARGA_REAGENDADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DATA_CHECKIN | DATE | obrigatório |  |  |
| DATA_REAGENDAMENTO | DATE | permite nulo |  |  |
| ID_USUARIO | INTEGER | permite nulo |  |  |
| ID_MOTIVO_REAGENDAMENTO | INTEGER | obrigatório |  |  |
| ID_ENTREGA | INTEGER | obrigatório |  |  |
| OBSERVACOES | STRING | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER | permite nulo |  | padrão 0 |

## MXMD_DESPESAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_TIPO_DESPESA | INTEGER | obrigatório |  |  |
| ID_CARREGAMENTO | VARCHAR(50) | permite nulo |  |  |
| VALOR | REAL | obrigatório |  |  |
| OBSERVACAO | VARCHAR(100) | permite nulo |  |  |
| ID_USUARIO | INTEGER | obrigatório |  |  |
| DATA | DATETIME | obrigatório |  |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |
| FOTO | BLOB | permite nulo |  |  |
| NOME_FOTO | VARCHAR(20) | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER(1) | permite nulo |  | padrão 0 |

## MXMD_ENTREGAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| ID_CLIENTE | VARCHAR(50) | permite nulo |  |  |
| ID_CARREGAMENTO | VARCHAR(50) | permite nulo |  |  |
| DATA_CHECKIN | DATETIME | permite nulo |  |  |
| DATA_FILA_ESPERA | DATETIME | permite nulo |  |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |
| ACURACIA | REAL | permite nulo |  |  |
| DATA_INICIO_DESCARGA | DATETIME | permite nulo |  |  |
| DATA_TERMINO_DESCARGA | DATETIME | permite nulo |  |  |
| DATA_INICIO_RECEBIMENTO | DATETIME | permite nulo |  |  |
| DATA_TERMINO_RECEBIMENTO | DATETIME | permite nulo |  |  |
| SITUACAO | VARCHAR(2) | permite nulo |  |  |
| SITUACAO_ORIG | VARCHAR(2) | permite nulo |  |  |
| OBSERVACOES | VARCHAR(140) | permite nulo |  |  |
| FOTO_CHECKIN | BLOB | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER | permite nulo |  |  |
| FOTO_SINCRONIZADA | INTEGER | permite nulo |  |  |
| ID_MOTORISTA | INTEGER | obrigatório |  |  |
| CHECKIN_FORA_RAIO | INTEGER | permite nulo |  |  |
| VOU_ENTREGAR | DATETIME | permite nulo |  |  |
| VOU_ENTREGAR_SINC | DATETIME | permite nulo |  |  |
| ATUALIZA_LOC_CLIENTE | INTEGER(1) | permite nulo |  | padrão 1 |
| REAGENDADO | VARCHAR(1) | obrigatório |  |  |
| ID_ENDERECO_ENT_PED | NUMBER | permite nulo |  |  |
| ID_MOTIVO_FURO_SEQUENCIA | INTEGER | permite nulo |  |  |
| FOTO_ASS_DIGITAL | BLOB | permite nulo |  |  |
| FOTO_ASS_SINCRONIZADA | INTEGER | permite nulo |  |  |
| CPF | VARCHAR(14) | permite nulo |  |  |
| FOTO_TRANSBORDO | BLOB | permite nulo |  |  |
| LATITUDE_FIM_ENTREGA | REAL | permite nulo |  |  |
| FOTO_ENTREGA | BLOB | permite nulo |  |  |
| LONGITUDE_FIM_ENTREGA | REAL | permite nulo |  |  |
| CHECKOUT_FORA_RAIO | INTEGER(1) | permite nulo |  |  |
| DISTANCIA | REAL | permite nulo |  |  |
| POSSUI_AVULSO | BOOLEAN | permite nulo |  | padrão 0 |
| EM_DESLOCAMENTO | INTEGER(1) | permite nulo |  |  |
| EM_DESLOCAMENTO_SINC | INTEGER(1) | permite nulo |  |  |
| TRANSFERIDO | INTEGER(1) | permite nulo |  | padrão 0 |

## MXMD_EVENTOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| DATA | DATETIME | obrigatório |  |  |
| ID_USUARIO | INTEGER | obrigatório |  |  |
| ID_TIPO_EVENTO | INTEGER | obrigatório |  |  |
| OBSERVACOES | VARCHAR(200) | permite nulo |  |  |
| FOTO | BLOB | permite nulo |  |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |
| NOME_FOTO | VARCHAR(20) | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER(1) | permite nulo |  | padrão 0 |

## MXMD_EVENTO_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_ENTREGA | INTEGER | obrigatório |  |  |
| ID_EVENTO | INTEGER | obrigatório |  |  |

## MXMD_FILIAIS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório | PK |  |
| RAZAO_SOCIAL | VARCHAR(40) | obrigatório |  |  |

## MXMD_FOTOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_REGISTRO | VARCHAR(50) | permite nulo |  |  |
| TIPO_REGISTRO | VARCHAR(50) | permite nulo |  |  |
| CAMINHO_FOTO | VARCHAR(400) | permite nulo |  |  |
| HASH | VARCHAR(16) | obrigatório |  |  |
| FOTO | BLOB | permite nulo |  |  |
| ENVIADO | INTEGER(1) | permite nulo |  | padrão 1 |

## MXMD_HISTORICO_OCORRENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_OCORRENCIA | INTEGER | permite nulo |  |  |
| SITUACAO | VARCHAR(255) | permite nulo |  |  |
| DATA | DATE | permite nulo |  |  |
| LANCADO_TORRE | VARCHAR(1) | permite nulo |  |  |
| OBSERVACAO | VARCHAR(255) | permite nulo |  |  |
| ENVIADO | INTEGER(1) | permite nulo |  | padrão 1 |

## MXMD_HIST_ACEITE_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_MOTORISTA | INTEGER(50) | obrigatório |  |  |
| DATA_ACEITE | DATETIME | obrigatório |  |  |
| ID_ROMANEIO | INTEGER(10) | obrigatório |  |  |
| STATUS | VARCHAR(1) | obrigatório |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER(1) | permite nulo |  | padrão 0 |

## MXMD_HODOMETROS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| KM | INTEGER | obrigatório |  |  |
| DATA_CADASTRO | DATETIME | obrigatório |  |  |
| LATITUDE | REAL | obrigatório |  |  |
| LONGITUDE | REAL | obrigatório |  |  |
| ID_USUARIO | INTEGER | permite nulo |  |  |
| PLACA | VARCHAR(8) | permite nulo |  |  |
| IMAGEM | BLOB | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER | obrigatório |  |  |
| TIPO_HODOMETRO | INTEGER | permite nulo |  |  |
| ID_HODOMETRO_INICIO | INTEGER | permite nulo |  |  |
| ID_ROMANEIO | INTEGER | permite nulo |  |  |

## MXMD_INFO_TRANSBORDO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_TRANSBORDO | INTEGER | permite nulo | PK |  |
| ID_ROMANEIO | INTEGER | permite nulo |  |  |
| CD_ORIGEM | STRING | permite nulo |  |  |
| CD_DESTINO | STRING | permite nulo |  |  |
| QT_CARREGAMENTOS | INTEGER | permite nulo |  |  |
| QT_NF | INTEGER | permite nulo |  |  |
| PESO | REAL | permite nulo |  |  |
| VOLUME | REAL | permite nulo |  |  |
| VLTOTAL | REAL | permite nulo |  |  |
| OBSERVACAO | STRING | permite nulo |  |  |

## MXMD_INTRAJORNADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| FIM_ULTIMA_JORNADA | DATETIME | permite nulo |  |  |
| TEMPO_INTRAJORNADA | DATETIME | permite nulo |  |  |

## MXMD_ITEM_COMODATO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DESCRICAO | STRING | obrigatório |  |  |
| UND_MEDIDA | STRING | obrigatório |  |  |

## MXMD_ITEM_OCORRENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_OCORRENCIA | INTEGER | obrigatório |  |  |
| TIPO | VARCHAR(2) | obrigatório |  |  |
| ID_REGISTRO | INTEGER | obrigatório |  |  |
| QUANTIDADE | REAL | permite nulo |  |  |

## MXMD_ITENS_NOTA_FISCAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório | PK |  |
| ID_PRODUTO | INTEGER | obrigatório |  |  |
| QUANTIDADE | REAL | obrigatório |  |  |
| PRECO_UNITARIO | REAL | obrigatório |  |  |
| PRECO_TABELA | REAL | obrigatório |  |  |
| ID_NOTA_FISCAL | INTEGER | permite nulo |  |  |
| QUANTIDADE_FALTA | REAL | permite nulo |  |  |
| QUANTIDADE_AVARIA | REAL | permite nulo |  |  |
| QUANTIDADE_DEVOLUCAO | REAL | permite nulo |  |  |
| MARCADO_ENTREGA | VARCHAR(1) | permite nulo |  |  |

## MXMD_JANELA_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| DIA_SEMANA | INTEGER | obrigatório |  |  |
| HORA_INICIO | VARCHAR(5) | obrigatório |  |  |
| HORA_FIM | VARCHAR(5) | obrigatório |  |  |
| ID_CLIENTE | VARCHAR(50) | obrigatório |  |  |
| ID_ENDERECO_ENTREGA | VARCHAR(50) | permite nulo |  |  |

## MXMD_LANCAMENTOS_JORNADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_USUARIO | INTEGER | permite nulo |  |  |
| INICIO_JORNADA | DATE | permite nulo |  |  |
| INICIO_REFEICAO | DATE | permite nulo |  |  |
| FIM_REFEICAO | DATE | permite nulo |  |  |
| FIM_JORNADA | DATE | permite nulo |  |  |
| LAT_INICIO_JORNADA | REAL | permite nulo |  |  |
| LAT_INICIO_REFEICAO | REAL | permite nulo |  |  |
| LAT_FIM_REFEICAO | REAL | permite nulo |  |  |
| LAT_FIM_JORNADA | REAL | permite nulo |  |  |
| LNG_INICIO_JORNADA | REAL | permite nulo |  |  |
| LNG_INICIO_REFEICAO | REAL | permite nulo |  |  |
| LNG_FIM_REFEICAO | REAL | permite nulo |  |  |
| LNG_FIM_JORNADA | REAL | permite nulo |  |  |
| ID_AJUDANTE | INTEGER | permite nulo |  |  |
| AJUDANTE_NOME | VARCHAR(50) | permite nulo |  |  |
| SYNC | INTEGER | permite nulo |  | padrão 0 |

## MXMD_LANC_COMODATO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_CLIENTE | STRING | obrigatório |  |  |
| TIPO | STRING | obrigatório |  |  |
| ID_ITEM | INTEGER | obrigatório |  |  |
| QUANTIDADE | INTEGER | obrigatório |  |  |
| ID_ENTREGA | INTEGER | obrigatório |  |  |
| ID_ENDERECO_ENTREGA | STRING | permite nulo |  |  |
| DATA_LANC | DATE | permite nulo |  |  |
| FOTO | STRING | permite nulo |  |  |
| NOME_FOTO | STRING | permite nulo |  |  |
| ENVIADO | INTEGER(1) | permite nulo |  | padrão 0 |
| CAMINHO_FOTO | VARCHAR | permite nulo |  |  |

## MXMD_LOCALIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| DATA | DATETIME | obrigatório |  |  |
| LATITUDE | REAL | obrigatório |  |  |
| LONGITUDE | REAL | obrigatório |  |  |
| PRECISAO | REAL | permite nulo |  |  |
| DISTANCIA | REAL | permite nulo |  |  |
| VELOCIDADE | REAL | permite nulo |  |  |

## MXMD_LOG_CONEXAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| TIPO | VARCHAR(1) | obrigatório |  |  |
| DATA | DATETIME | obrigatório |  |  |
| ERRO | VARCHAR(50) | permite nulo |  |  |

## MXMD_MARKER_ROMANEIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_ROMANEIO | INTEGER | permite nulo |  |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |
| TIPO_MARKER | STRING | permite nulo |  |  |

## MXMD_MOTIVO_CANCELAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DESCRICAO | STRING | obrigatório |  |  |

## MXMD_MOTIVO_DE_CANHOTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DESCRICAO | STRING | obrigatório |  |  |

## MXMD_MOTIVO_FURO_SEQUENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DESCRICAO | STRING | obrigatório |  |  |

## MXMD_MOTIVO_OCORRENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DESCRICAO | VARCHAR(255) | permite nulo |  |  |
| TIPO | VARCHAR(50) | permite nulo |  |  |

## MXMD_MOTIVO_REAGENDAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DESCRICAO | STRING | obrigatório |  |  |

## MXMD_MOTORISTAS_PREPOSTOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_MOTORISTA | STRING | obrigatório |  |  |
| ID_MOTORISTA_PREPOSTO | STRING | obrigatório |  |  |
| NOME_MOTORISTA_PREPOSTO | STRING | obrigatório |  |  |

## MXMD_NOTAS_FISCAIS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório | PK |  |
| NUMERO_NOTA | INTEGER | obrigatório |  |  |
| NUMERO_TRANSVENDA | INTEGER | obrigatório |  |  |
| ESPECIE | VARCHAR(2) | permite nulo |  |  |
| DATA_SAIDA | DATETIME | permite nulo |  |  |
| VALOR | REAL | permite nulo |  |  |
| ID_CLIENTE | VARCHAR(50) | permite nulo |  |  |
| ID_RCA | VARCHAR(50) | permite nulo |  |  |
| ID_SUPERVISOR | VARCHAR(50) | permite nulo |  |  |
| DATA_ENTREGA | DATETIME | permite nulo |  |  |
| PESO | REAL | permite nulo |  |  |
| VOLUME | REAL | permite nulo |  |  |
| ID_CARREGAMENTO | VARCHAR(50) | permite nulo | PK |  |
| COBRANCA | VARCHAR(50) | permite nulo |  |  |
| DESCRICAO_COB | VARCHAR(50) | permite nulo |  |  |
| PLANO_PAGAMENTO | VARCHAR(50) | permite nulo |  |  |
| OBSERVACAO | VARCHAR(50) | permite nulo |  |  |
| OBSERVACAO_AVARIA | VARCHAR(50) | permite nulo |  |  |
| OBSERVACAO_DEVOLUCAO | VARCHAR(50) | permite nulo |  |  |
| SEQUENCIA_ENTREGA | INTEGER | permite nulo |  |  |
| SITUACAO | VARCHAR(2) | permite nulo |  |  |
| DATA_FOTO_ASSINATURA | DATETIME | permite nulo |  |  |
| LATITUDE_ASSINATURA | REAL | permite nulo |  |  |
| LONGITUDE_ASSINATURA | REAL | permite nulo |  |  |
| ID_ENTREGA | INTEGER | permite nulo | PK |  |
| FOTO_ASSINATURA | BLOB | permite nulo |  |  |
| FOTO_AVARIA | BLOB | permite nulo |  |  |
| FOTO_DEVOLUCAO | BLOB | permite nulo |  |  |
| ID_MOTIVO_DEVOLUCAO | VARCHAR(50) | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER | obrigatório |  |  |
| ID_CONTATO_PORTAL | VARCHAR(50) | permite nulo |  |  |
| ID_CONTATO_CLIENTE | VARCHAR(50) | permite nulo |  |  |
| OBSERVACAO_CANHOTO | VARCHAR(200) | permite nulo |  |  |
| OBS_CANHOTO_NAO_QUALIFICADO | VARCHAR(120) | permite nulo |  |  |
| LETRAS_WMS | VARCHAR(2) | permite nulo |  |  |
| POSSUI_FOTO_ASSINATURA | VARCHAR(1) | obrigatório |  | padrão 'N' |
| FOTO_SINCRONIZADA | VARCHAR(1) | obrigatório |  | padrão 'N' |
| CONDVENDA | INTEGER | permite nulo |  |  |
| QTD_PARCELAS | INTEGER | permite nulo |  |  |
| MAXPAG | INTEGER | permite nulo |  |  |
| OBSENTREGA | VARCHAR(200) | permite nulo |  |  |
| OBSENTREGA1 | VARCHAR(200) | permite nulo |  |  |
| OBSENTREGA2 | VARCHAR(200) | permite nulo |  |  |
| OBSENTREGA3 | VARCHAR(200) | permite nulo |  |  |
| REENTREGUE | VARCHAR(1) | permite nulo |  | padrão 'N' |
| ID_FILIAL | VARCHAR(50) | permite nulo |  |  |
| TIPO_AVULSO | VARCHAR(10) | permite nulo |  |  |
| ID_MOTIVO_CANHOTO_STATUS | INTEGER(10) | permite nulo |  |  |
| TRANSFERIDO | INTEGER(1) | permite nulo |  | padrão 0 |
| VALOR_FRETE_VENC | REAL | permite nulo |  | padrão 0.0 |

## MXMD_NOTA_REENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DATA | DATE | permite nulo |  |  |
| ID_NOTA | INTEGER | obrigatório |  |  |
| ID_USUARIO | INTEGER | obrigatório |  |  |
| ID_ENTREGA | INTEGER | obrigatório |  |  |
| OBSERVACAO | VARCHAR(200) | permite nulo |  |  |
| ID_JUSTIFICATIVA | VARCHAR(50) | permite nulo |  |  |

## MXMD_OCORRENCIAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_USUARIO | INTEGER | permite nulo |  |  |
| ID_REGISTRO | INTEGER | obrigatório |  |  |
| DATA_OCORRENCIA | DATE | permite nulo |  |  |
| SITUACAO | VARCHAR(255) | permite nulo |  |  |
| TIPO | VARCHAR(2) | permite nulo |  |  |
| ORIGEM | VARCHAR(1) | obrigatório |  |  |
| ID_MOTIVO | INTEGER | obrigatório |  |  |
| OBSERVACAO | VARCHAR(255) | permite nulo |  |  |
| HASH | VARCHAR(16) | obrigatório |  |  |
| ENVIADO | INTEGER(1) | permite nulo |  | padrão 1 |

## MXMD_PARCELAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| PARCELA | VARCHAR(4) | permite nulo |  |  |
| VALOR | REAL | permite nulo |  |  |
| DATA_VENCIMENTO | DATE | permite nulo |  |  |
| DATA_EMISSAO | DATE | permite nulo |  |  |
| DUPLICATA | REAL | permite nulo |  |  |
| NUMTRANSVENDA | INTEGER(22) | permite nulo |  |  |

## MXMD_POLYLINE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_ROMANEIO | INTEGER | permite nulo |  |  |
| POLYLINE | CLOB | permite nulo |  |  |

## MXMD_PONTO_PARADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_ROMANEIO | INTEGER | permite nulo |  |  |
| LOGRADOURO | STRING | permite nulo |  |  |
| NUMERO | STRING | permite nulo |  |  |
| BAIRRO | STRING | permite nulo |  |  |
| CEP | STRING | permite nulo |  |  |
| MUNICIPIO | STRING | permite nulo |  |  |
| ESTADO | STRING | permite nulo |  |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |
| SEQUENCIA | INTEGER | permite nulo |  |  |
| DESCRICAO | STRING | permite nulo |  |  |
| OBSERVACAO | STRING | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER(1) | permite nulo |  | padrão 0 |
| SITUACAO | STRING | permite nulo |  |  |
| EXECUTADO | BOOLEAN | permite nulo |  |  |
| OBSERVACAO_MOTORISTA | STRING | permite nulo |  |  |
| FOTO | BLOB | permite nulo |  |  |
| DATA_CHECKIN | DATE | permite nulo |  |  |
| LATITUDE_CHECKIN | REAL | permite nulo |  |  |
| LONGITUDE_CHECKIN | REAL | permite nulo |  |  |

## MXMD_PRODUTOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório | PK |  |
| DESCRICAO | VARCHAR(40) | obrigatório |  |  |
| EMBALAGEM | VARCHAR(12) | obrigatório |  |  |
| UNIDADE | VARCHAR(2) | obrigatório |  |  |
| QTUNIT | INTEGER | permite nulo |  |  |
| QTUNITCX | INTEGER | permite nulo |  |  |
| CODAUXILIAR | VARCHAR(20) | permite nulo |  |  |
| CODAUXILIAR2 | VARCHAR(20) | permite nulo |  |  |
| ID_CARREGAMENTO | VARCHAR(50) | permite nulo |  |  |
| VLBONIFIC | REAL | permite nulo |  |  |
| ID_FILIAL | VARCHAR(50) | permite nulo |  |  |
| NUMTRANSVENDA | INTEGER | permite nulo |  |  |

## MXMD_PRODUTOS_VOLUMES_ENTREGAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| VOLUME | TEXT | permite nulo |  |  |
| ID_ENTREGA | INTEGER | obrigatório |  |  |
| ID_PRODUTO | INTEGER | obrigatório |  |  |
| ID_NOTA_FISCAL | INTEGER | obrigatório |  |  |

## MXMD_RASTRO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_RASTRO | INTEGER | permite nulo | PK |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |
| ACURACIA | REAL | permite nulo |  |  |
| VELOCIDADE | REAL | permite nulo |  |  |
| ACURACIA_VELOCIDADE | REAL | permite nulo |  |  |
| DATA_CAPTURA | DATE | permite nulo |  |  |
| DATA_ENVIO | DATE | permite nulo |  |  |

## MXMD_RCA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório |  |  |
| NOME | VARCHAR(40) | obrigatório | PK |  |
| TELEFONE1 | VARCHAR(13) | permite nulo |  |  |
| TELEFONE2 | VARCHAR(13) | permite nulo |  |  |

## MXMD_ROMANEIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER(10) | obrigatório | PK |  |
| DT_CRIACAO | DATETIME | obrigatório |  |  |
| ORIGEM | VARCHAR(3) | obrigatório |  |  |
| UNIDO | NUMBER(1) | obrigatório |  |  |
| SITUACAO | VARCHAR | obrigatório |  |  |
| DT_INICIO | DATETIME | permite nulo |  |  |
| DT_FIM | DATETIME | permite nulo |  |  |
| VLTOTAL | NUMBER | obrigatório |  |  |
| KM_PLANEJADO | REAL | obrigatório |  |  |
| TOTPESO | NUMBER | obrigatório |  |  |
| TOTVOLUME | NUMBER | obrigatório |  |  |
| QTD_ENTREGAS | NUMBER | obrigatório |  |  |
| QTD_NOTAS_FISCAIS | NUMBER | obrigatório |  |  |
| DESTINO | VARCHAR | obrigatório |  |  |
| VALOR_FRETE | NUMBER | obrigatório |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER(1) | permite nulo |  | padrão 0 |
| TRANSFERIDO | INTEGER(1) | permite nulo |  | padrão 0 |

## MXMD_SUPERVISORES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório |  |  |
| NOME | VARCHAR(40) | obrigatório | PK |  |
| TELEFONE | VARCHAR(13) | permite nulo |  |  |

## MXMD_TEMPO_SEMANA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| DOMINGO | INTEGER | permite nulo |  |  |
| JORNADA_DOMINGO | VARCHAR(1) | obrigatório |  | padrão 'N' |
| SEGUNDA | INTEGER | permite nulo |  |  |
| JORNADA_SEGUNDA | VARCHAR(1) | obrigatório |  | padrão 'N' |
| TERCA | INTEGER | permite nulo |  |  |
| JORNADA_TERCA | VARCHAR(1) | obrigatório |  | padrão 'N' |
| QUARTA | INTEGER | permite nulo |  |  |
| JORNADA_QUARTA | VARCHAR(1) | obrigatório |  | padrão 'N' |
| QUINTA | INTEGER | permite nulo |  |  |
| JORNADA_QUINTA | VARCHAR(1) | obrigatório |  | padrão 'N' |
| SEXTA | INTEGER | permite nulo |  |  |
| JORNADA_SEXTA | VARCHAR(1) | obrigatório |  | padrão 'N' |
| SABADO | INTEGER | permite nulo |  |  |
| JORNADA_SABADO | VARCHAR(1) | obrigatório |  | padrão 'N' |
| FINALIZAR_REFEICAO | INTEGER(1) | permite nulo |  | padrão 0 |

## MXMD_TIPO_DESPESA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| DESCRICAO | VARCHAR(50) | obrigatório |  |  |

## MXMD_TIPO_EVENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| DESCRICAO | VARCHAR(50) | obrigatório |  |  |

## MXMD_TITULOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMERO_TRANSVENDA | INTEGER | obrigatório | PK |  |
| PRESTACAO | VARCHAR(3) | obrigatório | PK |  |
| ID_MOTORISTA | INTEGER | obrigatório | PK |  |
| DUPLICATA | INTEGER | permite nulo |  |  |
| DATA_EMISSAO | DATETIME | permite nulo |  |  |
| DATA_VENCIMENTO | DATETIME | permite nulo |  |  |
| SITUACAO_BOLETO | VARCHAR(25) | permite nulo |  |  |
| VALOR | REAL | permite nulo |  |  |
| VALOR_DESCONTO | REAL | permite nulo |  |  |
| SALDO | REAL | permite nulo |  |  |
| VENCIDO | VARCHAR(1) | permite nulo |  |  |
| RECEBIDO | VARCHAR(1) | permite nulo |  |  |
| VALOR_RECEBIDO | REAL | permite nulo |  |  |
| ID_CLIENTE | VARCHAR(50) | obrigatório |  |  |
| ID_COBRANCA | VARCHAR(10) | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | VARCHAR(1) | permite nulo |  | padrão 'L' |
| BOLETO | VARCHAR(1) | permite nulo |  | padrão 'N' |

## MXMD_TOUR

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_TOUR | INTEGER | permite nulo | PK |  |
| DESCRICAO | STRING | permite nulo |  |  |
| RELEASE | STRING | permite nulo |  |  |
| VISUALIZADO | INTEGER | permite nulo |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER | permite nulo |  | padrão 0 |

## MXMD_VOLUMES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| VOLUME | TEXT | permite nulo |  |  |
| NUMERO_NOTA | INTEGER | permite nulo |  |  |
| ID_ENTREGA | INTEGER | permite nulo |  |  |
| ID_MOTORISTA | INTEGER | permite nulo |  |  |
| ID_CARREGAMENTO | VARCHAR(50) | permite nulo |  |  |

## MXMD_VOLUMES_CONF_ENT

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| VOLUME | TEXT | obrigatório |  |  |
| ID_ENTREGA | INTEGER | obrigatório |  |  |
| SITUACAO | TEXT | obrigatório |  |  |
| SITUACAO_SINCRONIZACAO | INTEGER(1) | permite nulo |  |  |

## MXMD_VOLUMES_ENTREGAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| VOLUME | TEXT | permite nulo |  |  |
| ID_ENTREGA | INTEGER | permite nulo |  |  |
| ID_MOTORISTA | INTEGER | permite nulo |  |  |
| ID_CARREGAMENTO | VARCHAR(50) | permite nulo |  |  |

## MXMD_VOLUMES_ENT_CONF_TEMP

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| VOLUME | VARCHAR(50) | permite nulo |  |  |
| SITUACAO | VARCHAR | obrigatório |  |  |
| ID_ENTREGA | INTEGER(10) | obrigatório |  |  |
| ID_MOTORISTA | INTEGER(10) | obrigatório |  |  |
| ID_CARREGAMENTO | INTEGER(10) | permite nulo |  |  |

## MXMI_COBRANCAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | obrigatório | PK |  |
| NOME | VARCHAR(30) | permite nulo |  |  |

## MXMI_CONTATOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | permite nulo |  |  |
| ID_CLIENTE | VARCHAR(50) | permite nulo |  |  |
| NOME | VARCHAR(40) | permite nulo |  |  |
| TIPO | VARCHAR(1) | permite nulo |  |  |
| TELEFONE | VARCHAR(18) | permite nulo |  |  |
| CELULAR | VARCHAR(18) | permite nulo |  |  |
| EMAIL | VARCHAR(50) | permite nulo |  |  |
| CPF | VARCHAR(18) | permite nulo |  |  |

## MXMI_MOTIVOS_DEVOLUCAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR(50) | obrigatório | PK |  |
| MOTIVO | VARCHAR(30) | permite nulo |  |  |

## MXMP_CONTATOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| NOME | VARCHAR(100) | obrigatório |  |  |
| TELEFONE | VARCHAR(15) | permite nulo |  |  |
| CPF | VARCHAR(14) | permite nulo |  |  |
| ID_CLIENTE | VARCHAR(50) | permite nulo |  |  |
| ID_FILIAL | VARCHAR(50) | permite nulo |  |  |

## MXMP_ENDERECO_ENTREGAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| ID_ENTREGA | INTEGER | permite nulo |  |  |
| ENDERECO | VARCHAR(100) | obrigatório |  |  |
| COMPLEMENTO | VARCHAR(100) | permite nulo |  |  |
| BAIRRO | VARCHAR(50) | permite nulo |  |  |
| MUNICIPIO | VARCHAR(50) | permite nulo |  |  |
| ESTADO | VARCHAR(30) | permite nulo |  |  |
| CEP | VARCHAR(15) | permite nulo |  |  |
| NUMERO | VARCHAR(5) | permite nulo |  |  |
| PONTO_REFERENCIA | VARCHAR(100) | permite nulo |  |  |
| LATITUDE | REAL | permite nulo |  |  |
| LONGITUDE | REAL | permite nulo |  |  |

## MXMP_ITEM_SOLICITACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_SOLICITACAO | INTEGER | obrigatório |  |  |
| TIPO | VARCHAR(2) | obrigatório |  |  |
| ID_REGISTRO | INTEGER | permite nulo |  |  |
| QUANTIDADE | REAL | permite nulo |  |  |

## MXMP_NOTIFICACAO_PORTAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_REGISTRO | INTEGER | permite nulo |  |  |
| TIPO | VARCHAR(2) | obrigatório |  |  |
| DATA | DATE | obrigatório |  |  |

## MXMP_PARAMETROS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NOME | VARCHAR(70) | obrigatório | PK |  |
| VALOR | VARCHAR(20) | permite nulo |  |  |
| TIPO | VARCHAR(1) | obrigatório |  |  |

## MXMP_RECEBIVEIS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMERO_TRANSVENDA | INTEGER | obrigatório | PK |  |
| TIPO | VARCHAR(2) | obrigatório |  |  |
| VALOR | REAL | permite nulo |  |  |
| CODIGO_BANCO | REAL | permite nulo |  |  |
| NUMERO_AGENCIA | REAL | permite nulo |  |  |
| NUMERO_CHEQUE | REAL | permite nulo |  |  |
| NUMERO_CONTA_CORRENTE | REAL | permite nulo |  |  |
| CPF_CHEQUE | VARCHAR(20) | permite nulo |  |  |
| OBSERVACOES | VARCHAR(200) | permite nulo |  |  |
| DATA_RECEBIMENTO | DATETIME | permite nulo |  |  |
| FOTO | BLOB | permite nulo |  |  |
| SEQUENCIA | INTEGER | obrigatório | PK |  |
| PRESTACAO | VARCHAR(3) | obrigatório | PK |  |
| SITUACAO_SINCRONIZACAO | INTEGER | obrigatório |  |  |
| ID_TRANSACAO | VARCHAR(22) | permite nulo |  |  |
| NSU | VARCHAR(14) | permite nulo |  |  |
| AUTHORIZATION_CODE | VARCHAR(8) | permite nulo |  |  |
| REFERENCE | VARCHAR(18) | permite nulo |  |  |
| RETURN_CODE | VARCHAR(5) | permite nulo |  |  |
| CONFIRMADO | BOOLEAN | obrigatório |  | padrão 0 |
| EXCLUIR | BOOLEAN | obrigatório |  | padrão 0 |

## MXMP_SOLICITACOES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | permite nulo | PK |  |
| ID_USUARIO | INTEGER | permite nulo |  |  |
| ID_CLIENTE | VARCHAR(50) | obrigatório |  |  |
| DATA_SOLICITACAO | DATE | permite nulo |  |  |
| LATITUDE_SOLICITACAO | REAL | permite nulo |  |  |
| LONGITUDE_SOLICITACAO | REAL | permite nulo |  |  |
| AUTORIZADO | VARCHAR(1) | permite nulo |  |  |
| DISTANCIA | REAL | permite nulo |  |  |
| ATUALIZA_LOCALIZACAO | INTEGER(1) | permite nulo |  |  |
| TIPO | VARCHAR(2) | permite nulo |  |  |
| OBSERVACAO | VARCHAR(200) | permite nulo |  |  |
| ENVIADO | INTEGER(1) | permite nulo |  | padrão 0 |

## MXMP_USUARIOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | INTEGER | obrigatório | PK |  |
| LOGIN | VARCHAR(20) | obrigatório |  |  |
| SENHA | VARCHAR(60) | permite nulo |  |  |
| NOME | VARCHAR(50) | obrigatório |  |  |
| NOME_MOTORISTA | VARCHAR(50) | permite nulo |  |  |
| DATA_CADASTRO | DATETIME | obrigatório |  |  |
| TIPO | VARCHAR(1) | obrigatório |  |  |
| DATA_ULTIMO_LOGON | DATETIME | permite nulo |  |  |
| TELEFONE | VARCHAR(15) | permite nulo |  |  |
| EXCLUIDO | VARCHAR(1) | permite nulo |  |  |
| APELIDO | VARCHAR(20) | permite nulo |  |  |
| ID_MOTORISTA | INTEGER | permite nulo |  |  |
| ID_APARELHO | INTEGER | permite nulo |  |  |
| ID_JORNADA | INTEGER | permite nulo |  |  |
| CARRETEIRO | VARCHAR(1) | permite nulo |  |  |
| FB_TOKEN | VARCHAR(30) | permite nulo |  |  |
| ID_USUARIO_MAXIMA | INTEGER | obrigatório |  |  |
| CONFIRMA_FRETE | BOOLEAN | permite nulo |  |  |

## android_metadata

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| locale | TEXT | permite nulo |  |  |

---

## Tabelas MXMP, MXS e ERP

# Tabelas MXMP, MXS e ERP

Dicionário de tabelas da base de logística/portal e estruturas relacionadas ao ERP.

## Visão geral

Esta base contém **326 tabelas** e **3138 campos**.

## Como usar esta referência

- Consulte pelo nome da tabela quando o problema envolver persistência, sincronização, integração ou diagnóstico técnico.
- Consulte pelo nome do campo quando o chamado mencionar coluna, chave, status, data, usuário, entrega, pedido, rota ou sincronização.
- Cada tabela fica em uma seção própria para manter o contexto dos campos no mesmo chunk.

## ERP_MXSMOV

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODPROD | VARCHAR2 | obrigatório |  | tamanho 50 |
| QT | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 6 |
| CUSTOFIN | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PTABELA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| ST | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PUNIT | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLBONIFIC | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLFRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLOUTRASDESP | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLDESCONTO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PERCOM | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| VLIPI | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| QTCONT | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 6 |
| VLREPASSE | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| CODOPER | VARCHAR2 | obrigatório |  | tamanho 2 |
| PUNITCONT | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLFRETE_RATEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLOUTROS | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PBONIFIC | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| NUMTRANSDEV | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DTCANCEL | DATE | permite nulo |  | tamanho 7 |
| NUMPED | NUMBER | permite nulo |  | tamanho 22, precis?o 15, escala 0 |
| NUMTRANSENT | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 0 |
| NUMTRANSVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 0 |
| NUMTRANSITEM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 0 |
| PBASERCA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PESOBRUTO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| TIPOITEM | VARCHAR2 | permite nulo |  | tamanho 1 |
| NUMNOTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| CUSTOREAL | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| CUSTOCONT | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| CUSTOREP | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| CUSTOFINEST | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| NUMLOTE | VARCHAR2 | permite nulo |  | tamanho 15 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFORNEC | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODEPTO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODDEVOL | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODPLPAG | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMREGIAO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| CODSEC | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTMOV | DATE | permite nulo |  | tamanho 7 |
| CODUSUR | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMSEQ | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| NUMCAR | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| CODAUXILIAR | VARCHAR2 | permite nulo |  | tamanho 50 |
| QTAVARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 6 |
| QTDEVOL | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 6 |
| ROTINACAD | VARCHAR2 | permite nulo |  | tamanho 100 |
| NUMCARANTERIOR | VARCHAR2 | permite nulo |  | tamanho 50 |

## ERP_MXSPREST

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMTRANSVENDA | NUMBER | obrigatório |  | tamanho 22, precis?o 22, escala 0 |
| DUPLIC | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| CODCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| PREST | VARCHAR2 | obrigatório |  | tamanho 4 |
| DTEMISSAO | DATE | permite nulo |  | tamanho 7 |
| DTVENC | DATE | permite nulo |  | tamanho 7 |
| STATUS | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODCOB | VARCHAR2 | permite nulo |  | tamanho 50 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VALORDESC | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| TXPERM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VPAGO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| DTVENCORIG | DATE | permite nulo |  | tamanho 7 |
| VALORORIG | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODUSUR | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTPAG | DATE | permite nulo |  | tamanho 7 |
| TXPERMPREVISTO | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 2 |
| NUMCHEQUE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| NUMBANCO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| PROTESTO | VARCHAR2 | permite nulo |  | tamanho 4 |
| PERCOM | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 5 |
| CARTORIO | VARCHAR2 | permite nulo |  | tamanho 1 |
| NOSSONUMBCO | VARCHAR2 | permite nulo |  | tamanho 30 |
| NOSSONUMBCO2 | VARCHAR2 | permite nulo |  | tamanho 30 |
| LINHADIG | VARCHAR2 | permite nulo |  | tamanho 4000 |
| LINHADIG2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| VALORMULTA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| BOLETO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CHEQUETERCEIRO | VARCHAR2 | permite nulo |  | tamanho 1 |
| VLTXBOLETO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| DTRECEBIMENTOPREVISTO | DATE | permite nulo |  | tamanho 7 |
| OPERACAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| NUMCAR | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCCXMOT | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTCXMOT | DATE | permite nulo |  | tamanho 7 |
| DTCXMOTHHMMSS | DATE | permite nulo |  | tamanho 7 |
| DTULTALTER | DATE | permite nulo |  | tamanho 7 |
| CODFUNCULTALTER | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTBAIXA | DATE | permite nulo |  | tamanho 7 |
| DTPAGCOMISSAO | DATE | permite nulo |  | tamanho 7 |
| VALORESTORNO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| DTESTORNO | DATE | permite nulo |  | tamanho 7 |
| PERMITEESTORNO | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODSUPERVISOR | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBS2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| AGENCIA | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODBARRA | VARCHAR2 | permite nulo |  | tamanho 100 |
| NUMCARTEIRA | VARCHAR2 | permite nulo |  | tamanho 100 |
| ID_ERP | VARCHAR2 | permite nulo |  | tamanho 50 |
| RECEBIVEL | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODCLIENTENOBANCO | VARCHAR2 | permite nulo |  | tamanho 50 |
| COMISSAO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| NUMCARANTERIOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMTRANSVENDAST | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| CODBANCOCM | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NSUPAGDIGITAL | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMTRANSPAGDIGITAL | VARCHAR2 | permite nulo |  | tamanho 50 |

## ERP_MXSVEICUL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODVEICULO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 80 |
| PLACA | VARCHAR2 | permite nulo |  | tamanho 10 |
| MARCA | VARCHAR2 | permite nulo |  | tamanho 40 |
| QTPALETE | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| VOLUME | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| PESOCARGAKG | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| TIPOVEICULO | VARCHAR2 | permite nulo |  | tamanho 1 |
| PROPRIO | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 50 |
| ALTURA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 3 |
| LARGURA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 3 |
| COMPRIMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 3 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 50 |
| RASTREADO | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODLOCALIZACAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| UFPLACAVEICULO | VARCHAR2 | permite nulo |  | tamanho 2 |
| CIDADEPLACAVEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| VEICULOGENERICO | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODROTAPRINC | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMPVCLIENTESRCA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODUSUR | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODCLI | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_AGENDAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| HORA_INICIAL | VARCHAR2 | obrigatório |  | tamanho 5 |
| HORA_FINAL | VARCHAR2 | obrigatório |  | tamanho 5 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 200 |
| ID_PEDIDO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_AGENDA_DINAMICA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_RCA | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_INICIO | DATE | obrigatório |  | tamanho 7 |
| DATA_FIM | DATE | obrigatório |  | tamanho 7 |
| HORA_INICIO | VARCHAR2 | obrigatório |  | tamanho 5 |
| TEMPO_MEDIO_VISITA | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| DATA_CRIACAO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| TEMPO_DESLOCAMENTO | NUMBER | permite nulo |  | tamanho 22, escala 0 |

## MXMP_AJUDANTE_COMPLEMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_EMPREGADO | NUMBER | permite nulo |  | tamanho 22 |
| CARGA_HORARIA | VARCHAR2 | permite nulo |  | tamanho 100 |
| CUSTO_HORA | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_AJUDANTE_CUSTO_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_AJUDANTE | NUMBER | obrigatório |  | tamanho 22, precis?o 8, escala 0 |
| ID_CUSTO_ROMANEIO_FRETE | NUMBER | obrigatório |  | tamanho 22 |
| CUSTO | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_APARELHOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CADASTRO | DATE | obrigatório |  | tamanho 7 |
| NUMERO_SERIE | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMERO_PATRIMONIO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CHAVE_ACESSO | VARCHAR2 | permite nulo |  | tamanho 100 |
| SERIAL_DISPOSITIVO | VARCHAR2 | permite nulo |  | tamanho 100 |
| PORCENTAGEM_BATERIA | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| VERSAO_APK | VARCHAR2 | permite nulo |  | tamanho 30 |
| MODELO | VARCHAR2 | permite nulo |  | tamanho 50 |
| API_ANDROID | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| DATA_ULTIMA_SINCRONIZACAO | DATE | permite nulo |  | tamanho 7 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| PERCENTUAL_RAM | VARCHAR2 | permite nulo |  | tamanho 5 |
| PERCENTUAL_ARMAZENAMENTO | VARCHAR2 | permite nulo |  | tamanho 5 |
| GPS_LIGADO | VARCHAR2 | permite nulo |  | tamanho 5 |
| STATUS_WIFI | VARCHAR2 | permite nulo |  | tamanho 50 |
| STATUS_REDE_MOBILE | VARCHAR2 | permite nulo |  | tamanho 50 |
| APPS_EM_USO | VARCHAR2 | permite nulo |  | tamanho 2000 |
| FB_TOKEN | VARCHAR2 | permite nulo |  | tamanho 200 |
| ID_NOTIFICACAO | VARCHAR2 | permite nulo |  | tamanho 100 |

## MXMP_APK

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CADASTRO | DATE | obrigatório |  | tamanho 7 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 100 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ARQUIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_AREAS_ATENDIMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| NOME | VARCHAR2 | permite nulo |  | tamanho 255 |
| COR | VARCHAR2 | permite nulo |  | tamanho 255 |
| POLYLINE | CLOB | permite nulo |  | tamanho 4000 |
| EDITAVEL | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_AREAS_ATENDIMENTO_DIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_AREAS_ATENDIMENTO | NUMBER | obrigatório |  | tamanho 22 |
| DIA | VARCHAR2 | obrigatório |  | tamanho 7 |

## MXMP_AREAS_ATENDIMENTO_FILIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_AREAS_ATENDIMENTO | NUMBER | obrigatório |  | tamanho 22 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 4000 |

## MXMP_AREAS_ATENDIMENTO_POLYLINE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| POLYLINE | CLOB | permite nulo |  | tamanho 4000 |
| ID_AREA_ATENDIMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_AREAS_ATENDIMENTO_VEICULO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_AREA_DE_ATENDIMENTO | NUMBER | obrigatório |  | tamanho 22 |
| ID_VEICULO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_ATUALIZACAO | DATE | permite nulo |  | tamanho 7 |
| PRIORIDADE | NUMBER | obrigatório |  | tamanho 22, precis?o 4, escala 0 |

## MXMP_ARQUIVOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ARQUIVO | BLOB | permite nulo |  | tamanho 4000 |
| REFERENCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 4 |
| CAMINHO_ABSOLUTO_NUVEM | VARCHAR2 | permite nulo |  | tamanho 200 |
| DATA_ULT_DOWNLOAD | DATE | permite nulo |  | tamanho 7 |

## MXMP_AUSENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_TIPO_AUSENCIA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_INICIO | DATE | obrigatório |  | tamanho 7 |
| DATA_FIM | DATE | obrigatório |  | tamanho 7 |
| JUSTIFICATIVA | VARCHAR2 | obrigatório |  | tamanho 500 |
| ID_MOTORISTA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_AJUDANTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| ABONA_HORAS | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_BAIXA_CARREGAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CARREGAMENTO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_PAGAMENTO | DATE | obrigatório |  | tamanho 7 |

## MXMP_BANCO_LOGISTICA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_VERSAO | DATE | permite nulo |  | tamanho 7 |
| NUM_VERSAO | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| ID_SOLUCAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_BASE_CALC_INFRACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPO_INFRACAO | VARCHAR2 | obrigatório |  | tamanho 20 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |

## MXMP_BASE_CARREGAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_CARREGAMENTO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_MOTORISTA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 2 |
| PESO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| VOLUME | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 4 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| UNIDO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ROTA_SEQUENCIA | CLOB | permite nulo |  | tamanho 4000 |
| ID_CUSTO | NUMBER | permite nulo |  | tamanho 22 |
| TIPO_CUSTO | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_CRIACAO_MODIFICACAO | DATE | permite nulo |  | tamanho 7 |
| QT_ENTREGAS | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| DATA_MONTAGEM | DATE | permite nulo |  | tamanho 7 |
| DATA_SAIDA | DATE | permite nulo |  | tamanho 7 |
| DT_ENTREGA_INICIAL | DATE | permite nulo |  | tamanho 7 |
| DT_ENTREGA_FINAL | DATE | permite nulo |  | tamanho 7 |
| HORARIO_FIM_OPERACAO | VARCHAR2 | permite nulo |  | tamanho 5 |
| SITUACAO_ROMANEIO | VARCHAR2 | permite nulo |  | tamanho 10 |
| ORIGEM_CAR | VARCHAR2 | permite nulo |  | tamanho 3 |

## MXMP_BASE_OCORRENCIAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_REGISTRO | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPO_REGISTRO | VARCHAR2 | permite nulo |  | tamanho 100 |
| TIPO_NOTIFICACAO | VARCHAR2 | permite nulo |  | tamanho 2 |
| MENSAGEM_NOTIFIACAO | VARCHAR2 | permite nulo |  | tamanho 255 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CADASTRO | DATE | permite nulo |  | tamanho 7 |

## MXMP_CAD_SEFAZ

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| UF | VARCHAR2 | permite nulo |  | tamanho 2 |
| VALOR | VARCHAR2 | obrigatório |  | tamanho 500 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 2 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_CANCELAMENTO_CHECKIN

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CHECKIN | DATE | obrigatório |  | tamanho 7 |
| DATA_CANCELAMENTO | DATE | obrigatório |  | tamanho 7 |

## MXMP_CARACTERISTICAS_COMPLEMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_VEICULO | VARCHAR2 | obrigatório |  | tamanho 20 |
| ID_CARACTERISTICA | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_CARACTERISTICAS_FILIAIS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_CARACTERISTICA | NUMBER | obrigatório |  | tamanho 22 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 4000 |

## MXMP_CARACTERISTICAS_VEICULO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 255 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXMP_CARACTERISTICAS_VEICULO_FILIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CARACTERISTICA_VEICULO_ID | NUMBER | obrigatório |  | tamanho 22 |
| FILIAL_ID | VARCHAR2 | obrigatório |  | tamanho 4000 |

## MXMP_CARREGAMENTO_CROSSDOCKING

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CARREGAMENTO_CROSSDOCKING | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_CARREGAMENTO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| DTCANCEL | DATE | permite nulo |  | tamanho 7 |

## MXMP_CARREGAMENTO_LOG

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |

## MXMP_CARREGAMENTO_TEMPORARIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_CARREGAMENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 1 |

## MXMP_CARREGAMENTO_TRANSBORDO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CARREGAMENTO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_CARREGAMENTO_TRANSBORDO | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| DTCANCEL | DATE | permite nulo |  | tamanho 7 |

## MXMP_CARREG_ENTREGA_INATIVO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_REGISTRO | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO_REGISTRO | VARCHAR2 | obrigatório |  | tamanho 1 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_INATIVACAO | DATE | obrigatório |  | tamanho 7 |

## MXMP_CARTEIRIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| CODUSUR | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODOPERACAO | VARCHAR2 | permite nulo |  | tamanho 2 |

## MXMP_CATEGORIA_PECAS_INSUMOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 400 |

## MXMP_CATEGORIA_SERVICO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 400 |

## MXMP_CD_USUARIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CD | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |

## MXMP_CENTROS_DISTRIBUICAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_CIDADE | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_ESTADO | VARCHAR2 | permite nulo |  | tamanho 2 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 100 |
| LOGRADOURO | VARCHAR2 | permite nulo |  | tamanho 100 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 50 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 9 |
| POR_CEP | VARCHAR2 | obrigatório |  | tamanho 1 |
| PRECISAO | VARCHAR2 | permite nulo |  | tamanho 20 |
| CROSS_DOCKING | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_CERT_DIGITAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_ARQUIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SENHA | VARCHAR2 | obrigatório |  | tamanho 250 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| DATA_VALIDADE | DATE | obrigatório |  | tamanho 7 |

## MXMP_CIDADE_TABELA_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| ID_CIDADE | VARCHAR2 | permite nulo |  | tamanho 50 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 5 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 20 |

## MXMP_CLIENTE_CENTRO_DISTRIBUICAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CODCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_ENDERECO_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CENTRO_DISTRIBUICAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_CLIENTE_COMPLEMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_MEDIO_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_TIPO_VEICULO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| PRIORIDADE_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| UTILIZAR_TEMPO_MEDIO_PADRAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| PRE_AGENDAMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| COR | VARCHAR2 | permite nulo |  | tamanho 10 |
| DATA_VERI_SEFAZ | DATE | permite nulo |  | tamanho 7 |
| MSG_STATUS_SEFAZ | VARCHAR2 | permite nulo |  | tamanho 2500 |

## MXMP_CODIGO_INFRACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODIGO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 1000 |
| INFRATOR | VARCHAR2 | obrigatório |  | tamanho 10 |
| GRAVIDADE | VARCHAR2 | obrigatório |  | tamanho 5 |
| FATOR_MULTIPLICADOR | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| PONTOS | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_CODIGO_RASTREIO_PEDIDO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMPED | NUMBER | obrigatório |  | tamanho 22, precis?o 15, escala 0 |
| CODIGO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_COD_END_FRETE_TRANSP_PED

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CODCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODENDENTCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODFORNECFRETE | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_CRIACAO | DATE | permite nulo |  | tamanho 7 |

## MXMP_COMBUSTIVEL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |
| PRECO_LITRO | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |

## MXMP_COMPLEMENTO_ROTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTA | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| COR | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_CONEXOES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CONEXAO | VARCHAR2 | obrigatório |  | tamanho 20 |
| IP | VARCHAR2 | permite nulo |  | tamanho 30 |
| PORTA | VARCHAR2 | permite nulo |  | tamanho 5 |

## MXMP_CONFIGURACAO_EMAIL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| HOST | VARCHAR2 | obrigatório |  | tamanho 100 |
| PORTA | VARCHAR2 | obrigatório |  | tamanho 10 |
| USUARIO | VARCHAR2 | obrigatório |  | tamanho 100 |
| SENHA | VARCHAR2 | obrigatório |  | tamanho 60 |
| HABILITA_ENVIO | VARCHAR2 | obrigatório |  | tamanho 1 |
| CAMPO_EMAIL_ERP | VARCHAR2 | obrigatório |  | tamanho 50 |
| REMETENTE | VARCHAR2 | permite nulo |  | tamanho 100 |
| AUTENTICACAO_SMTP | VARCHAR2 | obrigatório |  | tamanho 1 |
| ATIVAR_TSL | VARCHAR2 | obrigatório |  | tamanho 1 |
| EMPRESA | VARCHAR2 | permite nulo |  | tamanho 60 |
| HABILITA_ENVIO_TIMELINE | VARCHAR2 | obrigatório |  | tamanho 1 |
| ASSUNTO_EMAIL_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 200 |
| ASSINATURA_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 1000 |

## MXMP_CONFIGURACAO_ROTEIRIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ATIVO | VARCHAR2 | obrigatório |  | tamanho 5 |
| SERVICO | VARCHAR2 | permite nulo |  | tamanho 70 |
| ORDEM_PREFERENCIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_CONFIGURACAO_VISITAS_RCA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 18, escala 0 |
| HORA_INICIO | VARCHAR2 | obrigatório |  | tamanho 5 |
| TEMPO_MEDIO_VISITA | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| MES | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| ANO | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| DATA_INICIO | DATE | obrigatório |  | tamanho 7 |
| DATA_FIM | DATE | obrigatório |  | tamanho 7 |
| ID_ROTEIRIZACAO_RCA | NUMBER | obrigatório |  | tamanho 22 |
| SEQUENCIA_SEMANA | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| TEMPO_DESLOCAMENTO | NUMBER | permite nulo |  | tamanho 22, escala 0 |

## MXMP_CONFIG_EXIBICAO_CAMPOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22 |
| IDENTIFICADOR | VARCHAR2 | obrigatório |  | tamanho 100 |
| MODULO_SISTEMA | VARCHAR2 | obrigatório |  | tamanho 100 |

## MXMP_CONFIG_EXIBICAO_CAMPOS_ITEM

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| EXIBICAO | CHAR | permite nulo |  | tamanho 1 |
| ORDEM | NUMBER | obrigatório |  | tamanho 22, precis?o 22, escala 0 |
| ID_CONFIG_EXIBICAO_CAMPOS | NUMBER | obrigatório |  | tamanho 22 |
| CHAVECAMPO | VARCHAR2 | obrigatório |  | tamanho 100 |

## MXMP_CONFIG_FILTRO_CORES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| COR | VARCHAR2 | obrigatório |  | tamanho 100 |
| IDENTIFICADOR_FILTRO | VARCHAR2 | obrigatório |  | tamanho 100 |
| ID_CAMPO | VARCHAR2 | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 100 |
| OBSROTA | VARCHAR2 | permite nulo |  | tamanho 2000 |

## MXMP_CONFIG_MAXENTREGAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_UPDATE | DATE | obrigatório |  | tamanho 7 |
| NOME_APLICATIVO | VARCHAR2 | obrigatório |  | tamanho 30 |
| COPYRIGHT | VARCHAR2 | permite nulo |  | tamanho 50 |
| COR_TEXTO | VARCHAR2 | obrigatório |  | tamanho 15 |
| COR_BOTOES | VARCHAR2 | obrigatório |  | tamanho 15 |
| ID_LOGO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ICONE_512X512 | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ICONE_72X72 | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ICONE_96X96 | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ICONE_128X128 | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ICONE_144X144 | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ICONE_192X192 | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ICONE_384X384 | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ICONE_152X152 | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| URL | VARCHAR2 | obrigatório |  | tamanho 150 |
| ONESIGNAL_APP_ID | VARCHAR2 | permite nulo |  | tamanho 100 |
| ONESIGNAL_API_KEY | VARCHAR2 | permite nulo |  | tamanho 100 |

## MXMP_CONFIG_VISAO_USUARIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_CONFIG_VISAO_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| FILTROS_APLICADOS | BLOB | permite nulo |  | tamanho 4000 |
| GRAFICOS_APLICADOS | BLOB | permite nulo |  | tamanho 4000 |
| VISUALIZAR_AGRUPADO | VARCHAR2 | permite nulo |  | tamanho 1 |
| INTERVALO_VISUALIZACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |

## MXMP_CONTATOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 100 |
| TELEFONE | VARCHAR2 | permite nulo |  | tamanho 15 |
| CPF | VARCHAR2 | permite nulo |  | tamanho 14 |
| ID_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| EMAIL | VARCHAR2 | permite nulo |  | tamanho 64 |
| ISEMAILATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ID_FILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |

## MXMP_CONTROLE_EMAIL_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 20 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_CONTROLE_NOTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMERO_NOTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMERO_TRANSVENDA | NUMBER | obrigatório |  | tamanho 22, precis?o 22, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| QUANTIDADE_NOTAS | NUMBER | obrigatório |  | tamanho 22, precis?o 3, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CARREGAMENTO_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_CARREGAMENTO_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| SITUACAO_ORIGINAL_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 2 |

## MXMP_CONTROLE_SINC_MOTORISTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_MOTORISTA | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| OPERACAO | VARCHAR2 | obrigatório |  | tamanho 1 |
| SUCESSO | VARCHAR2 | obrigatório |  | tamanho 1 |

## MXMP_CORES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| VALOR | VARCHAR2 | obrigatório |  | tamanho 6 |

## MXMP_COTACAO_FORNECEDORES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 400 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 400 |
| SITUACAO | VARCHAR2 | obrigatório |  | tamanho 3 |
| ID_USUARIO_FINALIZACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_FINALIZACAO | DATE | permite nulo |  | tamanho 7 |
| ID_ARQUIVO_FOTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ARQUIVO_FOTO_2 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ARQUIVO_FOTO_3 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| HASH | VARCHAR2 | permite nulo |  | tamanho 30 |

## MXMP_CUSTO_CARREGAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| VALOR_CARGA | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| DESPESAS_VIAGEM | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| CUSTO_TOTAL | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| PERCENTUAL_CUSTO | NUMBER | obrigatório |  | tamanho 22, precis?o 5, escala 2 |
| CUSTO_PESSOAS | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| CUSTO_COMBUSTIVEL | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| VALOR_DIARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| QUANTIDADE_DIARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| QUANTIDADE_ALIMENTACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| VALOR_ALIMENTACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| VALOR_FRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| OUTRAS_DESPESAS | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| CUSTO_PESSOAS_CONSOLIDADO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| CUSTO_COMBUSTIVEL_CONSOLIDADO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| CUSTO_PESSOAS_PREVISTO_CONSOLIDADO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| CUSTO_COMBUSTIVEL_PREVISTO_CONSOLIDADO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| ID_CARREGAMENTO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_CUSTO_CIDADE_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CIDADE | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_CUSTO_ROMANEIO_FRETE | NUMBER | obrigatório |  | tamanho 22 |
| CUSTO | NUMBER | permite nulo |  | tamanho 22 |
| PESO | NUMBER | permite nulo |  | tamanho 22 |
| VALOR | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_CIDADE | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_CUSTO_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CARREGAMENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CLIENTE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CUSTO_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| CUSTO_KM_RODADO | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| PERCENT_CUSTO_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| ID_ENDERECO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_CUSTO_FAIXA_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CUSTO_ROMANEIO_FRETE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CUSTO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_FAIXA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO_FAIXA | VARCHAR2 | obrigatório |  | tamanho 255 |
| CODCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODENDENTCLI | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_CUSTO_MONTAGEM

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CUSTO_HORA_MOTORISTA | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| CUSTO_HORA_AJUDANTE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| CUSTO_COMBUSTIVEL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| CARGA_HORARIA | NUMBER | obrigatório |  | tamanho 22, precis?o 4, escala 2 |
| DESPESAS_VIAGEM | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| MEDIA_CONSUMO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| DURACAO_MONTAGEM | NUMBER | obrigatório |  | tamanho 22, precis?o 4, escala 2 |
| CUSTO_MAXIMO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |

## MXMP_CUSTO_ROMANEIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| VALOR_CARGA | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| DESPESAS_VIAGEM | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| CUSTO_TOTAL | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| PERCENTUAL_CUSTO | NUMBER | obrigatório |  | tamanho 22, precis?o 22, escala 2 |
| CUSTO_PESSOAS | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| CUSTO_COMBUSTIVEL | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| VALOR_DIARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| QUANTIDADE_DIARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| QUANTIDADE_ALIMENTACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| VALOR_ALIMENTACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| VALOR_FRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| OUTRAS_DESPESAS | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| CUSTO_PESSOAS_CONSOLIDADO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| CUSTO_COMBUSTIVEL_CONSOLIDADO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| CUSTO_PESSOAS_PREVISTO_CONSOLIDADO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| CUSTO_COMBUSTIVEL_PREVISTO_CONSOLIDADO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_CUSTO_ROMANEIO_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_TOTAL | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_ADICIONAL | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_ENTREGA | NUMBER | permite nulo |  | tamanho 22 |
| DIARIA | NUMBER | permite nulo |  | tamanho 22 |
| ALIMENTACAO | NUMBER | permite nulo |  | tamanho 22 |
| OUTRAS_DESPESAS | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_COMBUSTIVEL | NUMBER | permite nulo |  | tamanho 22 |
| TIPO_FAIXA | VARCHAR2 | permite nulo |  | tamanho 255 |
| INICIO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| FIM | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| VALOR_POR_TONELADA | NUMBER | permite nulo |  | tamanho 22 |
| TAXA_DIFICULDADE_ENT | NUMBER | permite nulo |  | tamanho 22 |
| TIPO_FAIXA_CIDADE | VARCHAR2 | permite nulo |  | tamanho 255 |
| CUSTO_MOTORISTA | NUMBER | permite nulo |  | tamanho 22 |
| ID_MOTORISTA | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| VALOR_MINIMO | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_FRETE_DIAS_UTEIS | NUMBER | permite nulo |  | tamanho 22 |
| QTD_DIAS_UTEIS_UTILIZADO | NUMBER | permite nulo |  | tamanho 22 |
| QTD_DIAS_VIAGEM | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_CUSTO_ROMANEIO_TERCEIRIZADO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| VLRTOTCUSTOPLANEJADO | NUMBER | permite nulo |  | tamanho 22, precis?o 19, escala 4 |
| PERCENTUALDECUSTO | NUMBER | permite nulo |  | tamanho 22, precis?o 19, escala 4 |
| VLRTOTPESO | NUMBER | permite nulo |  | tamanho 22, precis?o 19, escala 4 |
| VLRTOTPORENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 19, escala 4 |
| VLRTOTPESOPORCUBAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 19, escala 4 |
| IDTRANSPORTADORA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_DADOS_ENTREGA_NOTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| DATA_INICIO_ENTREGA | DATE | permite nulo |  | tamanho 7 |
| DATA_INICIO_DESCARGA | DATE | permite nulo |  | tamanho 7 |
| DATA_FIM_DESCARGA | DATE | permite nulo |  | tamanho 7 |
| COD_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| RAZAO_SOCIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ID_CARREGAMENTO | VARCHAR2 | permite nulo |  | tamanho 50 |
| SITUACAO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 2 |
| ID_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE_INICIO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 22 |
| LATITUDE_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LATITUDE_FIM_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE_INICIO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE_FIM_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 22 |
| COD_MOTORISTA | VARCHAR2 | permite nulo |  | tamanho 50 |
| NOME_MOTORISTA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| COD_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUM_SEQ_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| NUM_NOTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| NUM_TRANSVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 0 |
| STATUS | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |

## MXMP_DADOS_PERFIL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_PERFIL | NUMBER | obrigatório |  | tamanho 22 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 10 |
| ID_DADO | VARCHAR2 | obrigatório |  | tamanho 100 |
| ID_SOLUCAO | NUMBER | obrigatório |  | tamanho 22 |
| DATA_ATUALIZACAO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| ID_USUARIO_ATUALIZACAO | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_DADOS_USUARIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 10 |
| ID_DADO | VARCHAR2 | obrigatório |  | tamanho 100 |
| ID_SOLUCAO | NUMBER | obrigatório |  | tamanho 22 |
| DATA_ATUALIZACAO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| ID_USUARIO_ATUALIZACAO | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_DESCANSO_JORNADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_JORNADA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| INICIO_DESCANSO | DATE | permite nulo |  | tamanho 7 |
| FIM_DESCANSO | DATE | permite nulo |  | tamanho 7 |

## MXMP_DESCARGA_CANCELADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CHECKIN | DATE | obrigatório |  | tamanho 7 |
| DATA_INICIO_DESCARGA | DATE | obrigatório |  | tamanho 7 |
| DATA_CANCELAMENTO_DESCARGA | DATE | obrigatório |  | tamanho 7 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTIVO_CANCELAMENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| OBSERVACOES | VARCHAR2 | permite nulo |  | tamanho 200 |
| FOTO_CHECKIN | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |

## MXMP_DESCARGA_REAGENDADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CHECKIN | DATE | obrigatório |  | tamanho 7 |
| DATA_REAGENDAMENTO | DATE | obrigatório |  | tamanho 7 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTIVO_REAGENDAMENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| OBSERVACOES | VARCHAR2 | permite nulo |  | tamanho 200 |

## MXMP_DESPESAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CARREGAMENTO | VARCHAR2 | permite nulo |  | tamanho 50 |
| VALOR | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 100 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_TIPO_DESPESA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| ID_ARQUIVO_FOTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_FILIAL | VARCHAR2 | permite nulo |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_PLANO_CONTA | NUMBER | permite nulo |  | tamanho 22 |
| ID_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_USUARIO_PAGAMENTO | NUMBER | permite nulo |  | tamanho 22 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| NUMERO_NOTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_FORNECEDOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPO_DESPESA | VARCHAR2 | permite nulo |  | tamanho 4 |
| DATA_VENCIMENTO | DATE | permite nulo |  | tamanho 7 |
| DATA_PAGAMENTO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| PARCELA | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 2 |
| ID_ARQUIVO_FOTO_2 | NUMBER | permite nulo |  | tamanho 22 |
| ID_ARQUIVO_FOTO_3 | NUMBER | permite nulo |  | tamanho 22 |
| HASH | VARCHAR2 | permite nulo |  | tamanho 30 |
| ID_USUARIO_LANC | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| VALOR_PAGO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| DATA_ESTORNO | DATE | permite nulo |  | tamanho 7 |
| ID_USUARIO_ESTORNO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_DESPESA_ABASTECIMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| QUANTIDADE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| TIPO_COMBUSTIVEL | VARCHAR2 | permite nulo |  | tamanho 4 |
| HODOMETRO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| TANQUE_CHEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| TIPO_ABASTECIMENTO | VARCHAR2 | obrigatório |  | tamanho 1 |
| ID_TANQUE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_DESPESA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_DESPESA_INFRACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_INFRACAO | DATE | permite nulo |  | tamanho 7 |
| CODIGO_INFRACAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| VALOR_BASE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| FATOR_MULTIPLICADOR | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| GRAVIDADE | VARCHAR2 | permite nulo |  | tamanho 5 |
| VALOR_TOTAL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| AIT | VARCHAR2 | permite nulo |  | tamanho 50 |
| ENDERECO | VARCHAR2 | permite nulo |  | tamanho 256 |
| NUMERO | VARCHAR2 | permite nulo |  | tamanho 20 |
| CIDADE | VARCHAR2 | permite nulo |  | tamanho 256 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 256 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 30 |
| ESTADO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_DESPESA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_DEVOLUCOES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ITEM_NOTA_FISCAL | NUMBER | obrigatório |  | tamanho 22, precis?o 20, escala 0 |
| FALTAS | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| DEVOLUCOES | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| AVARIAS | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |

## MXMP_DIAS_ENT_CIDADE_EMITENTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CIDADE | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODFORNEC | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_ATUALIZACAO | DATE | permite nulo |  | tamanho 7 |
| QT_DIAS | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_DIA_MONTAGEM

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTA_COMP | NUMBER | obrigatório |  | tamanho 22 |
| DIA_SEMANA | NUMBER | permite nulo |  | tamanho 22 |
| HORA | VARCHAR2 | permite nulo |  | tamanho 5 |

## MXMP_DIA_MONTAGEM_CARGA_CLIENTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DIA_SEMANA | VARCHAR2 | obrigatório |  | tamanho 30 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_DISPOSICAO_GRID_PEDIDOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| POSICAO | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_ENDERECO_ENTREGAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ENDERECO | VARCHAR2 | permite nulo |  | tamanho 100 |
| COMPLEMENTO | VARCHAR2 | permite nulo |  | tamanho 100 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MUNICIPIO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ESTADO | VARCHAR2 | permite nulo |  | tamanho 30 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 15 |
| NUMERO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PONTO_REFERENCIA | VARCHAR2 | permite nulo |  | tamanho 100 |

## MXMP_ENDERECO_HIERARQUIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_ENDERECO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_HIERARQUIA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_ENTREGAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_CARREGAMENTO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_CHECKIN | DATE | permite nulo |  | tamanho 7 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| DATA_INICIO_DESCARGA | DATE | permite nulo |  | tamanho 7 |
| DATA_TERMINO_DESCARGA | DATE | permite nulo |  | tamanho 7 |
| DATA_INICIO_RECEBIMENTO | DATE | permite nulo |  | tamanho 7 |
| DATA_TERMINO_RECEBIMENTO | DATE | permite nulo |  | tamanho 7 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 2 |
| OBSERVACOES | VARCHAR2 | permite nulo |  | tamanho 255 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| FOTO_CHECKIN | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_FILA_ESPERA | DATE | permite nulo |  | tamanho 7 |
| VOU_ENTREGAR | DATE | permite nulo |  | tamanho 7 |
| DATA_GERACAO | DATE | permite nulo |  | tamanho 7 |
| ATUALIZA_LOC_CLIENTE | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ACURACIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| DATA_SINCRONIZACAO | DATE | permite nulo |  | tamanho 7 |
| ID_ENDERECO_ENT_PED | VARCHAR2 | permite nulo |  | tamanho 50 |
| REAGENDADO | VARCHAR2 | permite nulo |  | tamanho 1 |
| ID_MOTIVO_FURO_SEQUENCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| SITUACAO_ORIG | VARCHAR2 | permite nulo |  | tamanho 2 |
| ID_USUARIO_PRIMEIRA_SINCRONIZACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_PRIMEIRA_SINCRONIZACAO | DATE | permite nulo |  | tamanho 7 |
| FOTO_ASS_DIGITAL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE_CHECKIN | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE_CHECKIN | VARCHAR2 | permite nulo |  | tamanho 22 |
| CPF | VARCHAR2 | permite nulo |  | tamanho 14 |
| FOTO_TRANSBORDO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE_FIM_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE_FIM_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 22 |
| CHECKOUT_FORA_RAIO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| FOTO_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| EM_DESLOCAMENTO | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXMP_EVENTOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_TIPO_EVENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| OBSERVACOES | VARCHAR2 | permite nulo |  | tamanho 200 |
| FOTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |

## MXMP_FAIXA_TABELA_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 255 |
| INICIO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| FIM | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |

## MXMP_FAIXA_TRANSPORTADORA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_TRANSPORTADORA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| FAIXA_INICIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| FAIXA_FINAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_FAIXA | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| TIPO_FAIXA | VARCHAR2 | permite nulo |  | tamanho 200 |

## MXMP_FALHA_GEOCODE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENDERECO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 400 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| ID_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_FALHA_SINCRONIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 1 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_OBJETO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| INF_EXTRA | VARCHAR2 | permite nulo |  | tamanho 400 |
| JSON | BLOB | obrigatório |  | tamanho 4000 |

## MXMP_FILA_GEOCODE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CODCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODENDENTCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| NUMPED | NUMBER | obrigatório |  | tamanho 22, precis?o 15, escala 0 |

## MXMP_FILA_MENSAGEM

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO_FILA | VARCHAR2 | obrigatório |  | tamanho 40 |
| ID_REGISTRO | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO_REGISTRO | VARCHAR2 | obrigatório |  | tamanho 40 |
| TIPO_MENSAGEM | VARCHAR2 | obrigatório |  | tamanho 100 |
| DATA_CRIACAO | DATE | obrigatório |  | tamanho 7 |
| QTD_TENTATIVAS | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| ID_VINCULO | NUMBER | permite nulo |  | tamanho 22 |
| TIPO_VINCULO | VARCHAR2 | permite nulo |  | tamanho 40 |
| STATUS | VARCHAR2 | permite nulo |  | tamanho 30 |

## MXMP_FILA_ROTEIRIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROMANEIO | NUMBER | obrigatório |  | tamanho 22 |
| DT_CRIACAO | TIMESTAMP(6) | obrigatório |  | tamanho 11, escala 6 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 100 |
| TIPO_ROTEIRIZACAO | VARCHAR2 | obrigatório |  | tamanho 30 |
| STATUS | VARCHAR2 | permite nulo |  | tamanho 30 |
| QT_TENTATIVAS | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_FILA_VERI_SEFAZ

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_CRIACAO | DATE | permite nulo |  | tamanho 7 |
| ID_FILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |

## MXMP_FILIAIS_VEICULOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_VEICULO | VARCHAR2 | permite nulo |  | tamanho 20 |
| ID_FILIAL | VARCHAR2 | permite nulo |  | tamanho 20 |

## MXMP_FILIAL_COTACAO_FORNECEDORES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_COTACAO | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_FILIAL_PLANO_MANUTENCAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_PLANO | NUMBER | obrigatório |  | tamanho 22 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_FILIAL_ROTA_COMP

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROTA_COMP | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_FILIAL | VARCHAR2 | permite nulo |  | tamanho 4 |

## MXMP_FILIAL_TABELA_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| ID_FILIAL | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_FILIAL_VISAO_GERENCIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_VISAO_GERENCIAL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_FOTOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_REGISTRO | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO_REGISTRO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_ARQUIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| HASH | VARCHAR2 | obrigatório |  | tamanho 16 |

## MXMP_GRUPO_RAMO_ATIVIDADE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_COR | VARCHAR2 | obrigatório |  | tamanho 7 |

## MXMP_HIERARQUIA_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 255 |
| HIERARQUIA | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_HISTORICO_CARREGAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMERO_NOTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMERO_TRANSVENDA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_CARREGAMENTO_NOVO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CARREGAMENTO_ANTIGO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| QUANTIDADE_NOTAS | NUMBER | obrigatório |  | tamanho 22, precis?o 3, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CHECKIN | DATE | permite nulo |  | tamanho 7 |
| DATA_INICIO_DESCARGA | DATE | permite nulo |  | tamanho 7 |
| DATA_TERMINO_DESCARGA | DATE | permite nulo |  | tamanho 7 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 2 |
| OBSERVACOES | VARCHAR2 | permite nulo |  | tamanho 255 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| FOTO_CHECKIN | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| FOTO_CANHOTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| OBS_NOTA | VARCHAR2 | permite nulo |  | tamanho 255 |

## MXMP_HISTORICO_ENTREGAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_CARREGAMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CHECKIN | DATE | permite nulo |  | tamanho 7 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| DATA_INICIO_DESCARGA | DATE | permite nulo |  | tamanho 7 |
| DATA_TERMINO_DESCARGA | DATE | permite nulo |  | tamanho 7 |
| DATA_INICIO_RECEBIMENTO | DATE | permite nulo |  | tamanho 7 |
| DATA_TERMINO_RECEBIMENTO | DATE | permite nulo |  | tamanho 7 |
| SITUACAO_ANTERIOR | VARCHAR2 | permite nulo |  | tamanho 2 |
| OBSERVACOES | VARCHAR2 | permite nulo |  | tamanho 255 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 1 |
| DATA | DATE | permite nulo |  | tamanho 7 |

## MXMP_HISTORICO_OCORRENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_OCORRENCIA | NUMBER | obrigatório |  | tamanho 22 |
| DATA_UTC | DATE | obrigatório |  | tamanho 7 |
| LANCADO_TORRE | VARCHAR2 | permite nulo |  | tamanho 1 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 255 |

## MXMP_HISTORICO_TANQUE_COMBUSTIVEL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_TANQUE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| QUANTIDADE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| NUMERO_NOTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| TIPO_MOVIMENTACAO | VARCHAR2 | obrigatório |  | tamanho 2 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_TANQUE_ORIGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_USER | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_HIST_ACEITE_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_MOTORISTA | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_ACEITE | DATE | obrigatório |  | tamanho 7 |
| ID_ROMANEIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| STATUS | CHAR | obrigatório |  | tamanho 1 |

## MXMP_HIST_REENTREGA_CARREGAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| NUMCAR | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_HODOMETROS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| KM | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| DATA_CADASTRO | DATE | obrigatório |  | tamanho 7 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| PLACA | VARCHAR2 | obrigatório |  | tamanho 8 |
| ID_MOTORISTA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_ARQUIVO_FOTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_MILISEGUNDOS | VARCHAR2 | permite nulo |  | tamanho 20 |
| TIPO_HODOMETRO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ID_HODOMETRO_INICIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_HORARIOS_TRABALHO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 100 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| ENDERECO | VARCHAR2 | permite nulo |  | tamanho 500 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 200 |
| CIDADE | VARCHAR2 | permite nulo |  | tamanho 200 |
| ESTADO | VARCHAR2 | permite nulo |  | tamanho 2 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 10 |
| NUMERO | VARCHAR2 | permite nulo |  | tamanho 10 |
| LIMITE_RAIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| UTILIZA_COORDENADAS | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_HORARIOS_TRABALHO_ITENS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_HORARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| INICIO | DATE | obrigatório |  | tamanho 7 |
| FIM | DATE | obrigatório |  | tamanho 7 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 25 |

## MXMP_IDENTIFICACAO_PERSONALIZADA_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_PRODUTO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_INFO_CROSSDOCKING

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CARREGAMENTO_CROSSDOCKING | VARCHAR2 | obrigatório |  | tamanho 50 |
| QT_PEDIDOS | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 200 |

## MXMP_INFO_TRANSBORDO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_CD_DESTINO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_CD_ORIGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| QT_CARREGAMENTOS | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 200 |

## MXMP_ITEM_COTACAO_FORNECEDORES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ITEM | NUMBER | obrigatório |  | tamanho 22 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 3 |
| ID_COTACAO | NUMBER | obrigatório |  | tamanho 22 |
| ID_FORNECEDOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| VALOR | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| QUANTIDADE | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| VALOR_DIARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_PEDAGIO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_ABASTECIMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_MAO_DE_OBRA | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| NOME_MAO_DE_OBRA | VARCHAR2 | permite nulo |  | tamanho 200 |
| APROVADO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| DATA_PRAZO_ENTREGA | DATE | permite nulo |  | tamanho 7 |

## MXMP_ITEM_MANUTENCAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 3 |
| ID_MANUTENCAO | NUMBER | obrigatório |  | tamanho 22 |
| ID_ITEM | NUMBER | obrigatório |  | tamanho 22 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| QUANTIDADE | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |

## MXMP_ITEM_OCORRENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_OCORRENCIA | NUMBER | obrigatório |  | tamanho 22 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 2 |
| ID_REGISTRO | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| QUANTIDADE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_ITEM_PLANO_MANUTENCAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_PLANO | NUMBER | obrigatório |  | tamanho 22 |
| ID_ITEM | NUMBER | obrigatório |  | tamanho 22 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 3 |
| KM | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| DIAS | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| ID_USUARIO_ATUALIZACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_ATUALIZACAO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| ORIGEM_ATUALIZACAO | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXMP_ITEM_SOLICITACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_SOLICITACAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 2 |
| ID_REGISTRO | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| QUANTIDADE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_ITENS_COMODATOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 200 |
| UND_MEDIDA | VARCHAR2 | obrigatório |  | tamanho 50 |
| STATUS | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXMP_JANELA_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DIA_SEMANA | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| HORA_INICIO | VARCHAR2 | obrigatório |  | tamanho 5 |
| HORA_FIM | VARCHAR2 | obrigatório |  | tamanho 5 |
| ID_CLIENTE_COMPLEMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_ENDERECO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_JORNADAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| SEGUNDA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TERCA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| QUARTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| QUINTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| SEXTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| SABADO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DOMINGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| FINALIZAR_REFEICAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| INTRA_JORNADA | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| JORNADA_ININTERRUPTA | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_LANCAMENTOS_JORNADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| INICIO_JORNADA | DATE | obrigatório |  | tamanho 7 |
| INICIO_REFEICAO | DATE | permite nulo |  | tamanho 7 |
| FIM_REFEICAO | DATE | permite nulo |  | tamanho 7 |
| FIM_JORNADA | DATE | permite nulo |  | tamanho 7 |
| LAT_INICIO_JORNADA | VARCHAR2 | permite nulo |  | tamanho 22 |
| LNG_INICIO_JORNADA | VARCHAR2 | permite nulo |  | tamanho 22 |
| LAT_INICIO_REFEICAO | VARCHAR2 | permite nulo |  | tamanho 22 |
| LNG_INICIO_REFEICAO | VARCHAR2 | permite nulo |  | tamanho 22 |
| LAT_FIM_REFEICAO | VARCHAR2 | permite nulo |  | tamanho 22 |
| LNG_FIM_REFEICAO | VARCHAR2 | permite nulo |  | tamanho 22 |
| LAT_FIM_JORNADA | VARCHAR2 | permite nulo |  | tamanho 22 |
| LNG_FIM_JORNADA | VARCHAR2 | permite nulo |  | tamanho 22 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_AJUDANTE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| EXCLUIDO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| JUSTIFICATIVA | VARCHAR2 | permite nulo |  | tamanho 1000 |

## MXMP_LANC_COMODATO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CODCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_ENDERECO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_ITEM | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 2 |
| QUANTIDADE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_LANC | DATE | permite nulo |  | tamanho 7 |
| ID_USUARIO_LANC | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTORISTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_LINK

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR2 | obrigatório |  | tamanho 70 |
| ID_SOLUCAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| URL | VARCHAR2 | obrigatório |  | tamanho 200 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_LOCALIZACAO_CLIENTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| PRECISAO | VARCHAR2 | permite nulo |  | tamanho 20 |
| POR_CEP | VARCHAR2 | obrigatório |  | tamanho 1 |
| COORD_FIXA | VARCHAR2 | permite nulo |  | tamanho 1 |
| DATA_GERACAO_GEOCODE | DATE | permite nulo |  | tamanho 7 |
| ZONA_DE_RISCO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| TAXA_DIFICULDADE_ENT | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ORIGEM | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_LOCALIZACAO_CLIENTE_VENDA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 20 |

## MXMP_LOCALIZACAO_END_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| ID_ENDERECO_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| PRECISAO | VARCHAR2 | permite nulo |  | tamanho 20 |
| POR_CEP | VARCHAR2 | permite nulo |  | tamanho 1 |
| COORD_FIXA | VARCHAR2 | permite nulo |  | tamanho 1 |
| ZONA_DE_RISCO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| CODCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_GERACAO_GEOCODE | DATE | permite nulo |  | tamanho 7 |
| TAXA_DIFICULDADE_ENT | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ORIGEM | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_LOCALIZACAO_MOTORISTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 15, escala 0 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 20 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 20 |
| ID_MOTORISTA | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| PRECISAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| DISTANCIA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| VELOCIDADE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |

## MXMP_LOCALIZACAO_RCA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_RCA | VARCHAR2 | obrigatório |  | tamanho 50 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 50 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_LOGO_EMPRESA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ARQUIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_LOG_ALTER_ARQUIVO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ARQUIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_LOG_BAIXA_TITULO_SINC

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| NUMTRANSVENDA_ACEITO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMTRANSVENDA_RECUSADO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| INSERIDO_PARA_BAIXA | VARCHAR2 | permite nulo |  | tamanho 1 |
| VALOR_CAPTURADO | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_PRESTACAO | NUMBER | permite nulo |  | tamanho 22 |
| NOTA_AGRUPADA | VARCHAR2 | permite nulo |  | tamanho 2 |
| MAXPAYMENTID | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DATA | DATE | permite nulo |  | tamanho 7 |

## MXMP_LOG_DIST_AUTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| QTD | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |

## MXMP_LOG_ERP_MXSCARREG

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ORIGEM_ALTERACAO | VARCHAR2 | permite nulo |  | tamanho 150 |
| DATA_DO_LOG | DATE | permite nulo |  | tamanho 7 |
| CODVEICULO_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODVEICULO_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODMOTORISTA_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODMOTORISTA_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMCAR_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMCAR_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTSAIDA_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DTSAIDA_NOVO | DATE | permite nulo |  | tamanho 7 |
| DTFECHA_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DTFECHA_NOVO | DATE | permite nulo |  | tamanho 7 |
| DATAMON_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DATAMON_NOVO | DATE | permite nulo |  | tamanho 7 |
| NUMNOTAS_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| NUMNOTAS_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DTSAIDAVEICULO_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DTSAIDAVEICULO_NOVO | DATE | permite nulo |  | tamanho 7 |
| TOTPESO_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| TOTPESO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| TOTVOLUME_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 4 |
| TOTVOLUME_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 4 |
| VLTOTAL_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 2 |
| VLTOTAL_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 2 |
| DESTINO_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 20 |
| DESTINO_NOVO | VARCHAR2 | permite nulo |  | tamanho 20 |
| DT_CANCEL_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DT_CANCEL_NOVO | DATE | permite nulo |  | tamanho 7 |
| NUMENT_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NUMENT_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| QTITENS_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| QTITENS_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| CARGASECUNDARIA_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 1 |
| CARGASECUNDARIA_NOVO | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODFUNCAJUD_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD2_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD2_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD3_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD3_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| OBSDESTINO_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 200 |
| OBSDESTINO_NOVO | VARCHAR2 | permite nulo |  | tamanho 200 |
| DTATUALIZ_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DTATUALIZ_NOVO | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| CODOPERACAO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| STATUS_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| STATUS_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| ID_ROMANEIO_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROMANEIO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ORIGEM_CAR_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 3 |
| ORIGEM_CAR_NOVO | VARCHAR2 | permite nulo |  | tamanho 3 |

## MXMP_LOG_ERROS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 100 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 4000 |
| INFORMACAO | VARCHAR2 | obrigatório |  | tamanho 100 |

## MXMP_LOG_HODOMETROS_ALTERACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_HODOMETRO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TIPO_ALTERACAO | VARCHAR2 | permite nulo |  | tamanho 10 |
| ID_ROMANEIO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROMANEIO_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO_MODIFICOU | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_ALTERACAO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| TIPO_HODOMETRO_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| TIPO_HODOMETRO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ID_HODOMETRO_INICIO_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_HODOMETRO_INICIO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| KM_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| KM_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| PLACA_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 8 |
| PLACA_NOVO | VARCHAR2 | permite nulo |  | tamanho 8 |
| ID_MOTORISTA_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_MOTORISTA_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_FOTO_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_FOTO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| LAT_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 22 |
| LAT_NOVO | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONG_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONG_NOVO | VARCHAR2 | permite nulo |  | tamanho 22 |
| DATA_CADASTRO_ORIGINAL | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |

## MXMP_LOG_HODOMETRO_VEICULO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DATA_ALTERACAO | TIMESTAMP(6) | obrigatório |  | tamanho 11, escala 6 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22 |
| ORIGEM | VARCHAR2 | permite nulo |  | tamanho 3 |
| FUNCIONALIDADE | VARCHAR2 | permite nulo |  | tamanho 3 |
| VALOR_ATUAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_ANTERIOR | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ID_VEICULO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_LOG_MONTAGEM_AUTOMATICA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| COD_MONTAGEM | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO_MONTAGEM | VARCHAR2 | permite nulo |  | tamanho 200 |
| DATA_CRIACAO_MONTAGEM | DATE | permite nulo |  | tamanho 7 |
| ID_USUARIO_CRIACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| METRICA_DE_CORTE | VARCHAR2 | permite nulo |  | tamanho 15 |
| DATA_ALTERACAO | DATE | permite nulo |  | tamanho 7 |
| ID_USUARIO_ALTERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| METRICA_USADA | VARCHAR2 | permite nulo |  | tamanho 15 |

## MXMP_LOG_MOTORISTA_PREPOSTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_REGISTRO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTORISTA_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_MOTORISTA_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 1 |
| DATA | DATE | permite nulo |  | tamanho 7 |

## MXMP_LOG_NOTIFICACAO_PORTAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| STATUS | VARCHAR2 | obrigatório |  | tamanho 3 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 500 |
| ID_NOTIFICACAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USR_RESPONSAVEL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO_DELEGADO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_LOG_NUMSEQ_NFSAID

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMCAR | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMPED | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| CODCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMSEQ | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| PROGRAMA | CHAR | permite nulo |  | tamanho 5 |

## MXMP_LOG_OPERACOES_ROMANEIO_ERP

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROMANEIO_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| NUMCAR | VARCHAR2 | permite nulo |  | tamanho 10 |
| ORIGEM_CAR | VARCHAR2 | permite nulo |  | tamanho 3 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 80 |
| SITUACAO_ROMANEIO | VARCHAR2 | permite nulo |  | tamanho 10 |
| SITUACAO_ROMANEIO_NOVO | VARCHAR2 | permite nulo |  | tamanho 10 |
| CODMOTORISTA | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODMOTORISTA_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODVEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODVEICULO_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMENT_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NUMENT | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| MODULE | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD2 | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD3 | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD2_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCAJUD3_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_LOG_OP_LOGISTICA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| IDENTIFICADOR | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO_IDENTIFICADOR | VARCHAR2 | obrigatório |  | tamanho 30 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| VALOR_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 500 |
| VALOR_NOVO | VARCHAR2 | permite nulo |  | tamanho 500 |
| TABELA | VARCHAR2 | permite nulo |  | tamanho 100 |
| CAMPO | VARCHAR2 | permite nulo |  | tamanho 100 |
| HASH | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_LOG_REGISTRO_JORNADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_REGISTRO_JORNADA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_DA_ALTERACAO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| ACAO | VARCHAR2 | permite nulo |  | tamanho 10 |
| INICIO_JORNADA_ANTIGO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| FIM_JORNADA_ANTIGO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| INICIO_REFEICAO_ANTIGO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| FIM_REFEICAO_ANTIGO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| INICIO_JORNADA_NOVO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| FIM_JORNADA_NOVO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| INICIO_REFEICAO_NOVO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| FIM_REFEICAO_NOVO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| JUSTIFICATIVA_ANTIGA | VARCHAR2 | permite nulo |  | tamanho 1000 |
| JUSTIFICATIVA_NOVA | VARCHAR2 | permite nulo |  | tamanho 1000 |

## MXMP_LOG_SITUACAO_ENTREGA_NOTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO_REGISTRO | VARCHAR2 | obrigatório |  | tamanho 1 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_E_HORA | DATE | obrigatório |  | tamanho 7 |
| SITUACAO_ANTERIOR | VARCHAR2 | obrigatório |  | tamanho 2 |
| SITUACAO_ATUAL | VARCHAR2 | obrigatório |  | tamanho 2 |
| ID_REGISTRO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_LOG_TRANSF

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_MOTIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMCAR_ORIGEM | VARCHAR2 | obrigatório |  | tamanho 50 |
| NUMCAR_DESTINO | VARCHAR2 | obrigatório |  | tamanho 50 |
| NUMPED | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMTRANSVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_MANUTENCAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 3 |
| ID_FILIAL | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_CRIACAO | DATE | permite nulo |  | tamanho 7 |
| DATA_INICIAL | DATE | permite nulo |  | tamanho 7 |
| DATA_FINAL | DATE | permite nulo |  | tamanho 7 |
| SITUACAO | VARCHAR2 | obrigatório |  | tamanho 3 |
| ID_VEICULO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_FORNECEDOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| HODOMETRO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| OBSERVACOES | VARCHAR2 | permite nulo |  | tamanho 400 |
| ID_FOTO1 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_FOTO2 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_FOTO3 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| VALOR_EXTRA | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_TOTAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ID_PLANO_CONTA | NUMBER | permite nulo |  | tamanho 22 |
| DATA_FINALIZACAO | DATE | permite nulo |  | tamanho 7 |
| ID_USUARIO_FINALIZACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_DESPESA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_COTACAO | NUMBER | permite nulo |  | tamanho 22 |
| ID_USUARIO_ATUALIZACAO | NUMBER | permite nulo |  | tamanho 22 |
| ORIGEM_ATUALIZACAO | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXMP_MARCA_PECAS_INSUMOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 400 |

## MXMP_MAXPAG_COB

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_MAXPAG_TOKEN | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| COD_COB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| FORMA_PAGAMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| ID_MOEDA | VARCHAR2 | permite nulo |  | tamanho 10 |
| ID_BANCO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODCOB_BAIXA | VARCHAR2 | permite nulo |  | tamanho 4000 |

## MXMP_MAXPAG_LINK

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMTRANSVENDA | NUMBER | obrigatório |  | tamanho 22, precis?o 22, escala 0 |
| NUMNOTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| PAGAMENTOID | VARCHAR2 | obrigatório |  | tamanho 100 |
| LINK | VARCHAR2 | obrigatório |  | tamanho 200 |
| VALOR | NUMBER | obrigatório |  | tamanho 22 |
| DATA_EXPIRACAO | DATE | obrigatório |  | tamanho 7 |
| QRCODEPIX | VARCHAR2 | permite nulo |  | tamanho 3000 |

## MXMP_MAXPAG_MOV

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMTRANSVENDA | NUMBER | obrigatório |  | tamanho 22 |
| PAGAMENTOID | VARCHAR2 | obrigatório |  | tamanho 60 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| DESCRICAO_STATUS | VARCHAR2 | obrigatório |  | tamanho 60 |
| CODIGO_STATUS | NUMBER | obrigatório |  | tamanho 22 |
| NSU | VARCHAR2 | permite nulo |  | tamanho 60 |
| TID | VARCHAR2 | permite nulo |  | tamanho 60 |
| VALORCAPTURADO | NUMBER | permite nulo |  | tamanho 22 |
| VALORPREAUTORIZADO | NUMBER | permite nulo |  | tamanho 22 |
| FORMA_PAGAMENTO | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_MAXPAG_TOKEN

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| COD_FILIAL | VARCHAR2 | obrigatório |  | tamanho 4000 |
| TOKEN | VARCHAR2 | obrigatório |  | tamanho 60 |
| AMBIENTE | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| DATA_CRIACAO | DATE | permite nulo |  | tamanho 7 |

## MXMP_MOTIVO_CANCELAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_MOTIVO_DE_CANHOTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 200 |

## MXMP_MOTIVO_FURO_SEQUENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_MOTIVO_OCORRENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 255 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| ID_FILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_MOTIVO_REAGENDAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_MOTIVO_TRANSF

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 150 |

## MXMP_MOTORISTAS_PREF_ROTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTA_COMP | NUMBER | obrigatório |  | tamanho 22 |
| ID_MOTORISTA | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_MOTORISTAS_PREPOSTOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_MOTORISTA | NUMBER | obrigatório |  | tamanho 22, precis?o 8, escala 0 |
| ID_MOTORISTA_PREPOSTO | NUMBER | obrigatório |  | tamanho 22, precis?o 8, escala 0 |

## MXMP_MOTORISTA_COMPLEMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_AJUDANTE1 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_AJUDANTE2 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_AJUDANTE3 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTORISTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CARGA_HORARIA | VARCHAR2 | permite nulo |  | tamanho 10 |
| CUSTO_HORA | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| CONFIRMA_FRETE | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_MOTORISTA_OMNILINK

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTORISTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CATEGORIA | VARCHAR2 | permite nulo |  | tamanho 20 |
| DRIVER_ID | VARCHAR2 | obrigatório |  | tamanho 45 |

## MXMP_NOTAS_FISCAIS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 2 |
| NUMERO_TRANSVENDA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMERO_NOTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTIVO_DEVOLUCAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_CONTATO_CLIENTE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_CONTATO_PORTAL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| FOTO_ASSINATURA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| OBSERVACAO_CANHOTO | VARCHAR2 | permite nulo |  | tamanho 200 |
| FOTO_AVARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| OBSERVACAO_AVARIA | VARCHAR2 | permite nulo |  | tamanho 200 |
| OBSERVACAO_DEVOLUCAO | VARCHAR2 | permite nulo |  | tamanho 200 |
| FOTO_DEVOLUCAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| OBS_CANHOTO_NAO_QUALIFICADO | VARCHAR2 | permite nulo |  | tamanho 200 |
| CONDVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 0 |
| ID_MOTIVO_CANHOTO_STATUS | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| STATUS_CANHOTO | VARCHAR2 | permite nulo |  | tamanho 20 |

## MXMP_NOTA_REENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_NOTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 200 |
| ID_JUSTIFICATIVA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_CARREGAMENTO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_NOTIFICACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| TITULO | VARCHAR2 | obrigatório |  | tamanho 50 |
| MENSAGEM | VARCHAR2 | obrigatório |  | tamanho 255 |
| CATEGORIA | VARCHAR2 | obrigatório |  | tamanho 50 |
| ICONE | VARCHAR2 | obrigatório |  | tamanho 50 |
| FOI_ABERTO | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_NOTIFICACAO_CARREGAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CARREGAMENTO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_NOTIFICACAO | DATE | obrigatório |  | tamanho 7 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_NOTIFICACAO_PORTAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_REGISTRO | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 3 |
| LIDA | VARCHAR2 | obrigatório |  | tamanho 1 |
| MENSAGEM | VARCHAR2 | obrigatório |  | tamanho 250 |
| ID_USR_RESPONSAVEL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| HASH | VARCHAR2 | permite nulo |  | tamanho 32 |
| STATUS | VARCHAR2 | obrigatório |  | tamanho 3 |
| TITULO | VARCHAR2 | permite nulo |  | tamanho 100 |
| CRITICIDADE | VARCHAR2 | permite nulo |  | tamanho 3 |
| ENTIDADE | VARCHAR2 | permite nulo |  | tamanho 100 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 500 |
| ID_USUARIO_DELEGADO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_NOTIFICACAO_PAI | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_NOTIFICACAO_ROTEIRIZADOR

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_REGISTRO | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 2 |
| LIDA | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| MENSAGEM | VARCHAR2 | obrigatório |  | tamanho 4000 |
| ID_USUARIO | NUMBER | permite nulo |  | tamanho 22, precis?o 19, escala 0 |

## MXMP_NOTIFICACAO_USER_RESPONSAVEL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_NOTIFICACAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_OCOREN

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| REMETENTE | VARCHAR2 | obrigatório |  | tamanho 35 |
| DESTINATARIO | VARCHAR2 | obrigatório |  | tamanho 35 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| INTERCAMBIO | VARCHAR2 | obrigatório |  | tamanho 12 |
| VERSAO | NUMBER | obrigatório |  | tamanho 22, precis?o 2, escala 0 |

## MXMP_OCOREN_ARQUIVO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_OCOREN | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 80 |
| CAMINHO | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_IMPORTACAO | DATE | permite nulo |  | tamanho 7 |
| DATA_CRIACAO | DATE | permite nulo |  | tamanho 7 |
| IMPORT_MANUAL | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_OCOREN_CODIGO_OCORRENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 3, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 200 |
| SITUACAO | VARCHAR2 | obrigatório |  | tamanho 5 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_OCOREN_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_OCOREN | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_DOCUMENTO | VARCHAR2 | obrigatório |  | tamanho 14 |
| ID_TRANSPORTADORA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_OCOREN_OCORRENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CNPJ_EMISSOR_NOTA | VARCHAR2 | permite nulo |  | tamanho 14 |
| SERIE_NOTA | VARCHAR2 | permite nulo |  | tamanho 3 |
| NUM_NOTA | NUMBER | obrigatório |  | tamanho 22, precis?o 9, escala 0 |
| COD_OCORRENCIA | NUMBER | obrigatório |  | tamanho 22, precis?o 3, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| COD_OBSERVACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| TEXTO_LIVRE | VARCHAR2 | permite nulo |  | tamanho 70 |
| CNPJ_CONTRATANTE | VARCHAR2 | permite nulo |  | tamanho 14 |
| FILIAL_EMISSORA | VARCHAR2 | permite nulo |  | tamanho 10 |
| SERIE_CONHECIMENTO | VARCHAR2 | permite nulo |  | tamanho 5 |
| NUM_CONHECIMENTO | VARCHAR2 | permite nulo |  | tamanho 12 |

## MXMP_OCOREN_TRANSPORTADORA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CNPJ | VARCHAR2 | obrigatório |  | tamanho 14 |
| RAZAO_SOCIAL | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_OCORRENCIAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_OCORRENCIA_UTC | DATE | obrigatório |  | tamanho 7 |
| DATA_INICIO | DATE | permite nulo |  | tamanho 7 |
| DATA_FIM | DATE | permite nulo |  | tamanho 7 |
| DATA_CANCEL | DATE | permite nulo |  | tamanho 7 |
| USUARIO_CANCEL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| USUARIO_INICIO_ATENDIMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| USUARIO_FINALIZOU_ATENDIMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 255 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 2 |
| ID_MOTIVO | NUMBER | permite nulo |  | tamanho 22 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 255 |
| HASH | VARCHAR2 | obrigatório |  | tamanho 16 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 2 |
| ID_REGISTRO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ORIGEM | VARCHAR2 | permite nulo |  | tamanho 10 |
| DATA_HORA_SINC | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |

## MXMP_OPERADORA_VALE_PEDAGIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| LOGIN | VARCHAR2 | permite nulo |  | tamanho 250 |
| SENHA | VARCHAR2 | permite nulo |  | tamanho 250 |
| TOKEN | VARCHAR2 | permite nulo |  | tamanho 800 |
| IDENTIFICADOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| CNPJ | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_ALTERACAO | DATE | permite nulo |  | tamanho 7 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_PALAVRA_CHAVE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CODIGO | VARCHAR2 | obrigatório |  | tamanho 64 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 256 |

## MXMP_PARAMETROS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NOME | VARCHAR2 | obrigatório |  | tamanho 70 |
| VALOR | VARCHAR2 | permite nulo |  | tamanho 100 |
| ALTERACAO | DATE | obrigatório |  | tamanho 7 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 1 |
| TIPO_PARAMETRO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ALERTA_SONORO | VARCHAR2 | permite nulo |  | tamanho 1 |
| VALOR2 | VARCHAR2 | permite nulo |  | tamanho 100 |

## MXMP_PARAMETROS_CALCULO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_TRANSPORTADORA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CALCULA_FRENTE_KM | VARCHAR2 | permite nulo |  | tamanho 2 |
| VALOR_KM_RODADO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ADICIONAR_VARIACAO_KM | VARCHAR2 | permite nulo |  | tamanho 2 |
| PERCENTUAL_VARICAO_KM | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| UTILIZA_VALOR_PREFIXADO | VARCHAR2 | permite nulo |  | tamanho 2 |
| VALOR_PRE_FIXADO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| CALCULAR_FRETE_PESO | VARCHAR2 | permite nulo |  | tamanho 2 |
| VALOR_FIXO_PESO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| CALCULAR_FRETE_CUBAGEM | VARCHAR2 | permite nulo |  | tamanho 2 |
| VALOR_FIXO_CUBAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ADICIONA_ENTREGA_REALIZADA | VARCHAR2 | permite nulo |  | tamanho 2 |
| VALOR_FIXO_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |

## MXMP_PARAMETROS_FILIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_PARAMETRO | VARCHAR2 | obrigatório |  | tamanho 70 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 4000 |
| VALOR | VARCHAR2 | permite nulo |  | tamanho 100 |
| ALTERACAO | DATE | permite nulo |  | tamanho 7 |
| ALERTA_SONORO | VARCHAR2 | permite nulo |  | tamanho 1 |
| VALOR2 | VARCHAR2 | permite nulo |  | tamanho 100 |

## MXMP_PARAMETROS_OMNILINK

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 2, escala 0 |
| HORAS_ALERTA_REFEICAO | NUMBER | obrigatório |  | tamanho 22, precis?o 4, escala 2 |
| MINUTOS_ALERTA_FIM_JORNADA | NUMBER | obrigatório |  | tamanho 22, precis?o 4, escala 0 |
| HORAS_ATE_FIM_JORNADA | VARCHAR2 | obrigatório |  | tamanho 20 |
| HORAS_DESCANSO_CARRETEIRO | NUMBER | obrigatório |  | tamanho 22, precis?o 4, escala 2 |
| HORAS_LEG_AMARELA | VARCHAR2 | obrigatório |  | tamanho 20 |
| HORAS_LEG_VERMELHA | VARCHAR2 | obrigatório |  | tamanho 20 |
| USUARIO | VARCHAR2 | obrigatório |  | tamanho 50 |
| SENHA | VARCHAR2 | obrigatório |  | tamanho 20 |
| URL_SERVICO | VARCHAR2 | permite nulo |  | tamanho 120 |

## MXMP_PARAMETROS_RESTRICAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_TRANSPORTADORA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DISTANCIA_KM_INICIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| DISTANCIA_KM_FINAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_TOTAL_INICIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_TOTAL_FINAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| PESO_TOTAL_INICIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| PESO_TOTAL_FINAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| PESO_CUBADO_INICIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| PESO_CUBADO_FINAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| QUANTIDADE_MAX_ENTREGAINICIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| QUANTIDADE_MAX_ENTREGAFINAL | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |

## MXMP_PARAMETROS_USUARIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_PARAMETRO | VARCHAR2 | obrigatório |  | tamanho 70 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| VALOR | VARCHAR2 | permite nulo |  | tamanho 100 |
| ALTERACAO | DATE | permite nulo |  | tamanho 7 |

## MXMP_PECAS_INSUMOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 400 |
| SITUACAO | VARCHAR2 | obrigatório |  | tamanho 1 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ID_CATEGORIA | NUMBER | obrigatório |  | tamanho 22 |
| ID_MARCA | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_PEDIDO_CROSSDOCKING

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CARREGAMENTO_CROSSDOCKING | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_PEDIDO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_PERFIL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_SOLUCAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 200 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| DATA_ATUALIZACAO | DATE | permite nulo |  | tamanho 7 |
| USUARIO_ATUALIZACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_PERFIL_ACESSO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ATIVO | VARCHAR2 | obrigatório |  | tamanho 1 |

## MXMP_PERFIL_ACESSO_PERMISSAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_PERFIL_ACESSO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_PERMISSAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_PERFIL_ROTEIRIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CHAVE | VARCHAR2 | obrigatório |  | tamanho 50 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 1000 |

## MXMP_PERMISSAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CODIGO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_PERMISSOES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_SOLUCAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 200 |

## MXMP_PERMISSOES_PERFIL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_PERMISSAO | NUMBER | obrigatório |  | tamanho 22 |
| ID_PERFIL | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_PERMISSOES_USUARIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_PERMISSAO | NUMBER | obrigatório |  | tamanho 22 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22 |
| DATA_ATUALIZACAO | DATE | obrigatório |  | tamanho 7 |

## MXMP_PLANEJAMENTO_VISITAS_RCA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| INICIO_VISITA | TIMESTAMP(6) | obrigatório |  | tamanho 11, escala 6 |
| FINAL_VISITA | TIMESTAMP(6) | obrigatório |  | tamanho 11, escala 6 |
| ID_CONFIGURACAO_VISITAS_RCA | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTEIRIZACAO_RCA_SEQUENCIA | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_PLANO_CONTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CODIGO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 1 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ID_GRUPO | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_PLANO_GRUPO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CODIGO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_PLANO_MANUTENCAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 100 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 400 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ID_TIPO_VEICULO | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_PNEUS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 50 |
| SITUACAO | VARCHAR2 | obrigatório |  | tamanho 3 |
| NUMERO_FOGO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_MARCA | NUMBER | obrigatório |  | tamanho 22 |
| MODELO | VARCHAR2 | obrigatório |  | tamanho 200 |
| DIMENSOES | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUM_SERIE | VARCHAR2 | permite nulo |  | tamanho 50 |
| RECAPAGEM | NUMBER | obrigatório |  | tamanho 22, precis?o 2, escala 0 |
| ID_ARQUIVO_FOTO_1 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ARQUIVO_FOTO_2 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ARQUIVO_FOTO_3 | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 500 |
| DATA_COMPRA | DATE | permite nulo |  | tamanho 7 |
| CUSTO_PNEU | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| ATIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_PONTOS_REFERENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 200 |
| SITUACAO | VARCHAR2 | obrigatório |  | tamanho 2 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ENDERECO | VARCHAR2 | permite nulo |  | tamanho 500 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 200 |
| CIDADE | VARCHAR2 | permite nulo |  | tamanho 200 |
| ESTADO | VARCHAR2 | permite nulo |  | tamanho 2 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 10 |
| NUMERO | VARCHAR2 | permite nulo |  | tamanho 10 |
| LATITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | obrigatório |  | tamanho 22 |

## MXMP_PONTO_PARADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 150 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 150 |
| TEMPO_MEDIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| LOGRADOURO | VARCHAR2 | permite nulo |  | tamanho 150 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 150 |
| NUMERO | VARCHAR2 | permite nulo |  | tamanho 150 |
| MUNICIPIO | VARCHAR2 | permite nulo |  | tamanho 150 |
| ESTADO | VARCHAR2 | permite nulo |  | tamanho 150 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 150 |
| LATITUDE | NUMBER | permite nulo |  | tamanho 22 |
| LONGITUDE | NUMBER | permite nulo |  | tamanho 22 |
| ULTIMA_PARADA | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_PONTO_PARADA_ROMANEIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 200 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 200 |
| LOGRADOURO | VARCHAR2 | permite nulo |  | tamanho 300 |
| NUMERO | VARCHAR2 | permite nulo |  | tamanho 50 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 300 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 20 |
| MUNICIPIO | VARCHAR2 | permite nulo |  | tamanho 100 |
| ESTADO | VARCHAR2 | permite nulo |  | tamanho 50 |
| SEQUENCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROTA_SEQUENCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ULTIMA_PARADA | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| TEMPO_MEDIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_POSICAO_TATICO_OPERACIONAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| POSICAO | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_PRACA_TABELA_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| ID_PRACA | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_PRACA_VISAO_GERENCIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_VISAO_GERENCIAL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_PRACA | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_PRE_ACERTO_MOTORISTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_NOTA_FISCAL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_PROBLEM_JSON

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 20, escala 0 |
| ID_PROBLEM | VARCHAR2 | obrigatório |  | tamanho 60 |
| ID_USUARIO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_VEICULO | VARCHAR2 | obrigatório |  | tamanho 50 |
| DT_ENVIO | TIMESTAMP(6) | obrigatório |  | tamanho 11, escala 6 |
| PROBLEM | BLOB | obrigatório |  | tamanho 4000 |
| JANELA_ENTREGA | NUMBER | permite nulo |  | tamanho 22, escala 0 |

## MXMP_RAKING_MOTORISTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| VALOR | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| PESO | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| VOLUME | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 2 |
| DISTANCIA_ESTIMADA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| DISTANCIA_PERCORRIDA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| QUANTIDADE_ENTREGAS | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| QUANTIDADE_DEVOLUCOES | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| ENTREGAS_FORA_CERCA | NUMBER | obrigatório |  | tamanho 22, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| DESVIO | NUMBER | obrigatório |  | tamanho 22, precis?o 5, escala 2 |
| PONTUACAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |

## MXMP_RAMO_ATIVIDADE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_GRUPO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_RAMO_ATIVIDADE_COMPLEMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| CODATIV | VARCHAR2 | obrigatório |  | tamanho 50 |
| COR | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_RASTREADOR

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| LOGIN | VARCHAR2 | permite nulo |  | tamanho 250 |
| SENHA | VARCHAR2 | permite nulo |  | tamanho 250 |
| TOKEN | VARCHAR2 | permite nulo |  | tamanho 800 |
| IDENTIFICADOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_ALTERACAO | DATE | permite nulo |  | tamanho 7 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_RECEBIVEIS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMERO_TRANSVENDA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SEQUENCIA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| PRESTACAO | VARCHAR2 | obrigatório |  | tamanho 3 |
| VALOR | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| CODIGO_BANCO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMERO_AGENCIA | NUMBER | permite nulo |  | tamanho 22 |
| NUMERO_CHEQUE | NUMBER | permite nulo |  | tamanho 22 |
| NUMERO_CONTA_CORRENTE | NUMBER | permite nulo |  | tamanho 22 |
| CPF_CHEQUE | VARCHAR2 | permite nulo |  | tamanho 20 |
| OBSERVACOES | VARCHAR2 | permite nulo |  | tamanho 200 |
| DATA_RECEBIMENTO | DATE | obrigatório |  | tamanho 7 |
| ID_ARQUIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 2 |
| ID_TRANSACAO | VARCHAR2 | permite nulo |  | tamanho 22 |
| NSU | VARCHAR2 | permite nulo |  | tamanho 14 |
| AUTHORIZATION_CODE | VARCHAR2 | permite nulo |  | tamanho 8 |
| REFERENCE | VARCHAR2 | permite nulo |  | tamanho 18 |
| RETURN_CODE | VARCHAR2 | permite nulo |  | tamanho 5 |

## MXMP_REGIAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 100 |
| OVERLAY_TP | VARCHAR2 | permite nulo |  | tamanho 2000 |
| OVERLAY_OBJ | VARCHAR2 | permite nulo |  | tamanho 2000 |

## MXMP_REGIAO_CLIENTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_REGIAO | NUMBER | permite nulo |  | tamanho 22 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 250 |
| FANTASIA | VARCHAR2 | obrigatório |  | tamanho 250 |

## MXMP_REGIOES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_REGIOES_ATENDIMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 100 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 20 |

## MXMP_REGIOES_ATENDIMENTO_CIDADE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_REGIOES_ATENDIMENTO | NUMBER | obrigatório |  | tamanho 22 |
| ID_CIDADE | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_REGIOES_ATENDIMENTO_PRACA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_REGIOES_ATENDIMENTO | NUMBER | obrigatório |  | tamanho 22 |
| ID_PRACA | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_REGIOES_ATENDIMENTO_ROTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_REGIOES_ATENDIMENTO | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTA | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_REGIOES_CIDADES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_REGIAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CIDADE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_REGIOES_ENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_REGIOES_ENTREGA_ROTAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_REGIAO_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_REGISTRO_PONTO_PARADA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| ID_MOTORISTA | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_PONTO_PARADA_ROMANEIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| EXECUTADO | VARCHAR2 | permite nulo |  | tamanho 255 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 255 |
| FOTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_REJEICAO_ROTA_AUTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTA | NUMBER | obrigatório |  | tamanho 22 |
| ID_REJEICAO | NUMBER | obrigatório |  | tamanho 22 |
| ID_CLIENTE | NUMBER | permite nulo |  | tamanho 22 |
| DATA_HORA | TIMESTAMP(6) | obrigatório |  | tamanho 11, escala 6 |
| ID_ROTA_COMPLEMENTO | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_REPROCESSAR_ROMANEIO_CD

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_CENTRO_DISTRIBUICAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |

## MXMP_RESPONSAVEL_MOTORISTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_USUARIO_RESPONSAVEL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO_MOTORISTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_RODIZIO_DIA_SEMANA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DIA_SEMANA | VARCHAR2 | obrigatório |  | tamanho 30 |

## MXMP_RODIZIO_FINAL_PLACA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_RODIZIO_DIA_SEMANA | NUMBER | obrigatório |  | tamanho 22 |
| FINAL_PLACA | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_RODIZIO_ROTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_RODIZIO_DIA_SEMANA | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTA | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_ROMANEIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DT_CRIACAO | TIMESTAMP(6) | obrigatório |  | tamanho 11, escala 6 |
| ORIGEM | VARCHAR2 | obrigatório |  | tamanho 3 |
| UNIDO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| DT_INICIO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| DT_FIM | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 10 |
| ROT_PENDENTE | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| RESPONSAVEL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ROT_PENDENTE_STATUS | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_ARQUIVO_ASSINATURA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_ASSINATURA | DATE | permite nulo |  | tamanho 7 |
| CPF_ASSINATURA | VARCHAR2 | permite nulo |  | tamanho 18 |
| ID_USUARIO_ASSINATURA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_ROTAS_TRANSPORTADORA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_TRANSPORTADORA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROTA | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_ROTA_COMPLEMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| PESO_MIN_MONTAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VOLUME_MIN_MONTAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALOR_MIN_MONTAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ID_CENTRO_DISTRIBUICAO | NUMBER | permite nulo |  | tamanho 22 |
| ROTA_MONITORADA | VARCHAR2 | permite nulo |  | tamanho 1 |
| MONT_AUTOMATICA | VARCHAR2 | permite nulo |  | tamanho 1 |
| QTD_DIAS_ENTREGA | NUMBER | permite nulo |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 200 |
| PERMITIR_SALVA_SEM_VEICULO | CHAR | permite nulo |  | tamanho 1 |
| METRICA_DE_CORTE | NUMBER | permite nulo |  | tamanho 22, escala 0 |
| ROTA_OU_PRACA | VARCHAR2 | permite nulo |  | tamanho 5 |
| ID_PRACAS | VARCHAR2 | permite nulo |  | tamanho 255 |
| PEDIDOS_CONFERIDOS | VARCHAR2 | permite nulo |  | tamanho 1 |
| ID_ROTA | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_ROTA_MONTAGEM_COMPLEMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | permite nulo |  | tamanho 22 |
| ID_ROTA_COMPLEMENTO | NUMBER | permite nulo |  | tamanho 22 |
| ID_PRACAS | VARCHAR2 | permite nulo |  | tamanho 255 |
| ID_ROTA | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_ROTA_ROMANEIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_MOTORISTA | VARCHAR2 | obrigatório |  | tamanho 22 |
| VOLUME | NUMBER | obrigatório |  | tamanho 22, precis?o 18, escala 6 |
| PESO | NUMBER | obrigatório |  | tamanho 22, precis?o 18, escala 2 |
| DATA_CRICACAO | DATE | obrigatório |  | tamanho 7 |
| ID_SOLUCAO_ROTEIRIZACAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| VALOR | NUMBER | obrigatório |  | tamanho 22, precis?o 16, escala 3 |
| DESTINO | VARCHAR2 | obrigatório |  | tamanho 200 |
| ROTA_INVERTIDA | VARCHAR2 | permite nulo |  | tamanho 1 |
| DT_TRAJETO_RECALCULADO | DATE | permite nulo |  | tamanho 7 |
| DT_ENTREGA_INICIAL | DATE | permite nulo |  | tamanho 7 |
| DT_ENTREGA_FINAL | DATE | permite nulo |  | tamanho 7 |
| ID_ROTA_COMPLEMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 7 |
| HORARIO_FIM_OPERACAO | VARCHAR2 | permite nulo |  | tamanho 5 |
| ID_ROMANEIO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ROTA_LOCAL | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ID_CLI_PRIM_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_CLI_ULT_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_END_ENT_CLI_PRIM_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_END_ENT_CLI_ULT_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| CALC_TEMPO_SAIDA_PONTO_PARTIDA | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| HORARIO_INICIO_ALMOCO | VARCHAR2 | permite nulo |  | tamanho 5 |
| HORARIO_FIM_ALMOCO | VARCHAR2 | permite nulo |  | tamanho 5 |
| ID_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_ROTA_SEQUENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SEQUENCIA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ATIVIDADE | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_CENTRO_DISTRIBUICAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DISTANCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DURACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENDERECO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_HORA_INICIO | DATE | permite nulo |  | tamanho 7 |
| DATA_HORA_FIM | DATE | permite nulo |  | tamanho 7 |
| ID_CLIENTE_CHEGADA | VARCHAR2 | permite nulo |  | tamanho 100 |
| ID_CLIENTE_PARTIDA | VARCHAR2 | permite nulo |  | tamanho 100 |
| TEMPO_ESPERA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROTA_ROMANEIO | VARCHAR2 | permite nulo |  | tamanho 50 |
| JANELA_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| POLYLINE | CLOB | permite nulo |  | tamanho 4000 |
| LATITUDE | NUMBER | permite nulo |  | tamanho 22 |
| LONGITUDE | NUMBER | permite nulo |  | tamanho 22 |
| ID_AGENDAMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_ROTA_SEQUENCIA_BKP

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SEQUENCIA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ATIVIDADE | VARCHAR2 | obrigatório |  | tamanho 50 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_CENTRO_DISTRIBUICAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DISTANCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DURACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENDERECO_ENTREGA | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_HORA_INICIO | DATE | permite nulo |  | tamanho 7 |
| DATA_HORA_FIM | DATE | permite nulo |  | tamanho 7 |
| ID_CLIENTE_CHEGADA | VARCHAR2 | permite nulo |  | tamanho 100 |
| ID_CLIENTE_PARTIDA | VARCHAR2 | permite nulo |  | tamanho 100 |
| TEMPO_ESPERA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROTA_CARREGAMENTO | VARCHAR2 | permite nulo |  | tamanho 50 |
| JANELA_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_ROTA_TABELA_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| ID_ROTA | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_ROTA_VISAO_GERENCIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_VISAO_GERENCIAL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROTA | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_ROTEIRIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_CARREGAMENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTORISTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_VEICULO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| PESO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| QTD_PEDIDOS | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| VOLUME | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| DATA_CRIACAO | DATE | obrigatório |  | tamanho 7 |
| ID_CENTRO_DISTRIBUICAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DISTANCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |

## MXMP_ROTEIRIZACAO_DIA_SEMANA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTEIRIZACAO_RCA | NUMBER | obrigatório |  | tamanho 22 |
| DIA_SEMANA | VARCHAR2 | permite nulo |  | tamanho 20 |
| LATITUDE_INICIAL | VARCHAR2 | permite nulo |  | tamanho 20 |
| LONGITUDE_INICIAL | VARCHAR2 | permite nulo |  | tamanho 20 |
| LATITUDE_FINAL | VARCHAR2 | permite nulo |  | tamanho 20 |
| LONGITUDE_FINAL | VARCHAR2 | permite nulo |  | tamanho 20 |
| DATA_ALTERACAO | DATE | permite nulo |  | tamanho 7 |
| TOTAL_KM_DIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |

## MXMP_ROTEIRIZACAO_LOG_RCA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_ALTERACAO | TIMESTAMP(6) | obrigatório |  | tamanho 11, escala 6 |
| ID_USUARIO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_RCA | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_ROTEIRIZACAO_PEDIDO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_PEDIDO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SEQUENCIA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CARREGAMENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DISTANCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |

## MXMP_ROTEIRIZACAO_RCA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 255 |
| ID_RCA | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_ALTERACAO | DATE | permite nulo |  | tamanho 7 |
| TOTAL_KM_ROTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |

## MXMP_ROTEIRIZACAO_RCA_SEQ

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTEIRIZACAO_RCA_DIA_SEMANA | NUMBER | obrigatório |  | tamanho 22 |
| ID_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| SEQUENCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DISTANCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| AGENDAMENTO | VARCHAR2 | permite nulo |  | tamanho 5 |

## MXMP_ROTEIRIZADOR_CONFIG

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ALTERACAO | DATE | obrigatório |  | tamanho 7 |
| SUPERVISOR_INATIVO | VARCHAR2 | obrigatório |  | tamanho 70 |
| CLIENTES_INATIVOS | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_SEGMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 20 |
| ID_COR | VARCHAR2 | obrigatório |  | tamanho 7 |

## MXMP_SEGMENTO_CLIENTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CLIENTE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_SEGMENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_SEM_PARAR_PRACAS_VIAGEM

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_VIAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 0 |
| CONCESSIONARIA | VARCHAR2 | permite nulo |  | tamanho 250 |
| PRACA | VARCHAR2 | permite nulo |  | tamanho 250 |
| DATA_ATUALIZACAO | DATE | permite nulo |  | tamanho 7 |
| RODOVIA | VARCHAR2 | permite nulo |  | tamanho 250 |
| PLACA | VARCHAR2 | permite nulo |  | tamanho 50 |
| TAG | VARCHAR2 | permite nulo |  | tamanho 100 |
| TARIFA | NUMBER | permite nulo |  | tamanho 22, precis?o 19, escala 2 |

## MXMP_SEM_PARAR_PRACA_PEDAGIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_SEM_PARAR | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_MAPLINK | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| CONCESSIONARIA | VARCHAR2 | permite nulo |  | tamanho 250 |
| PRACA | VARCHAR2 | permite nulo |  | tamanho 250 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| SENTIDO_VIA | VARCHAR2 | permite nulo |  | tamanho 10 |
| SENTIDO_PRACA | VARCHAR2 | permite nulo |  | tamanho 10 |
| DATA_ATUALIZACAO | DATE | permite nulo |  | tamanho 7 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_SEM_PARAR_VIAGEM

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_VIAGEM | NUMBER | obrigatório |  | tamanho 22, precis?o 12, escala 0 |
| ID_ROMANEIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| CAT_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CNPJ_EMISSOR | VARCHAR2 | permite nulo |  | tamanho 20 |
| CNPJ_TRANSP | VARCHAR2 | permite nulo |  | tamanho 20 |
| DATA_COMPRA | DATE | permite nulo |  | tamanho 7 |
| DATA_EXP | DATE | permite nulo |  | tamanho 7 |
| DATA_VIAGEM | DATE | permite nulo |  | tamanho 7 |
| NOME_EMISSOR | VARCHAR2 | permite nulo |  | tamanho 250 |
| NOME_ROTA | VARCHAR2 | permite nulo |  | tamanho 250 |
| NOME_TRANSP | VARCHAR2 | permite nulo |  | tamanho 250 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| RECIBO_EMITIDO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| STATUS | NUMBER | permite nulo |  | tamanho 22 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 50 |
| TOTAL | NUMBER | permite nulo |  | tamanho 22, precis?o 19, escala 2 |
| CANCELADO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ID_USER_COMPRA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO_CATEGORIA | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| TIPO_RODAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| ID_SEM_PARAR | VARCHAR2 | permite nulo |  | tamanho 20 |
| QTD_EIXOS | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| ID_VEICULO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_ROTA_ROMANEIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_CANCELAMENTO | DATE | permite nulo |  | tamanho 7 |
| ID_USER_CANCELAMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_SEQUENCIA_DINAMICA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| SEQUENCIA | NUMBER | obrigatório |  | tamanho 22 |
| ID_AGENDA_DINAMICA | NUMBER | permite nulo |  | tamanho 22 |
| ID_ROTA | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_SERVICO_GEOCODIFICACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ORDEM_PREFERENCIAL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SERVICO | VARCHAR2 | obrigatório |  | tamanho 50 |
| SITUACAO | CHAR | obrigatório |  | tamanho 1 |

## MXMP_SERVICO_ROTEIRIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ORDEM_PREFERENCIAL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SERVICO | VARCHAR2 | obrigatório |  | tamanho 50 |
| SITUACAO | CHAR | obrigatório |  | tamanho 1 |

## MXMP_SLA_CLIENTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_CLIENTE | VARCHAR2 | obrigatório |  | tamanho 50 |
| VALOR_SLA | NUMBER | obrigatório |  | tamanho 22, precis?o 3, escala 0 |

## MXMP_SLA_REDE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_REDE | VARCHAR2 | obrigatório |  | tamanho 50 |
| VALOR_SLA | NUMBER | obrigatório |  | tamanho 22, precis?o 3, escala 0 |

## MXMP_SLA_REGIAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| VALOR_SLA | NUMBER | obrigatório |  | tamanho 22, precis?o 3, escala 0 |
| ID_ROTA | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_SOLICITACOES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_SOLICITACAO | DATE | obrigatório |  | tamanho 7 |
| LATITUDE_SOLICITACAO | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE_SOLICITACAO | VARCHAR2 | permite nulo |  | tamanho 22 |
| AUTORIZADO | VARCHAR2 | permite nulo |  | tamanho 1 |
| DISTANCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| ATUALIZA_LOCALIZACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 2 |
| ID_USR_AUTORIZACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 200 |
| ID_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATA_AUTORIZADO_NEGADO | DATE | permite nulo |  | tamanho 7 |
| ID_ARQUIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_SOLUCAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_SOLUCAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 20 |

## MXMP_SOLUCAO_ROTEIRIZACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_SERVICO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_TRABALHADO_DIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_TRABALHADO_NOITE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_DESCARGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_TRABALHADO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_COLETA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| QUANTIDADE_JANELAS_DE_TEMPO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_DIRIGINDO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_DE_CARGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TOTAL_TEMPO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TOTAL_DISTANCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| MEDIA_VOLUME | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| MEDIA_PESO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| QUANTIDADE_REJEICOES | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_ESPERA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_TOTAL_DESCANSO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| QUANTIDADE_ROTAS | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_SUB_PERMISSOES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_PERMISSAO | NUMBER | obrigatório |  | tamanho 22 |
| ID_PERMISSAO_PAI | NUMBER | obrigatório |  | tamanho 22 |
| NIVEL | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_SUB_PERMISSOES_PERFIL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_SUB_PERMISSAO | NUMBER | obrigatório |  | tamanho 22 |
| ID_PERFIL | NUMBER | obrigatório |  | tamanho 22 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXMP_TABELA_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 255 |
| VALOR_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_ENTREGA | NUMBER | permite nulo |  | tamanho 22 |
| PERCENTUAL_ENTREGA | NUMBER | permite nulo |  | tamanho 22 |
| DIARIA | NUMBER | permite nulo |  | tamanho 22 |
| ALIMENTACAO | NUMBER | permite nulo |  | tamanho 22 |
| OUTRAS_DESPESAS | NUMBER | permite nulo |  | tamanho 22 |
| STATUS | VARCHAR2 | permite nulo |  | tamanho 50 |
| CONSIDERA_COMBUSTIVEL | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| TIPO_FAIXA | VARCHAR2 | permite nulo |  | tamanho 50 |
| VALOR_POR_TONELADA | NUMBER | permite nulo |  | tamanho 22 |
| CONSIDERA_HORA_MOTORISTA | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| CONSIDERA_HORA_AJUDANTE | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| VALOR_MINIMO | NUMBER | permite nulo |  | tamanho 22 |
| VALOR_FRETE_DIAS_UTEIS | NUMBER | permite nulo |  | tamanho 22 |
| CONSIDERA_VALOR_FRETE_DIAS_UTEIS | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_TAEMROTA_RESTRICAO_CODCOB

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| RESTRINGIR | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| CODCOB | VARCHAR2 | obrigatório |  | tamanho 4000 |

## MXMP_TAEMROTA_RESTRICAO_ORIGEM_PEDIDO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| RESTRINGIR | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 100 |
| ORIGEM | VARCHAR2 | obrigatório |  | tamanho 4000 |

## MXMP_TANQUE_COMBUSTIVEL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 4000 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 4 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 200 |
| CAPACIDADE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| ESTOQUE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 2 |
| ATIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_TEMPLATE_WHATSAPP

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_TEMPLATE | VARCHAR2 | obrigatório |  | tamanho 60 |
| TEXTO | NVARCHAR2 | obrigatório |  | tamanho 512 |
| ID_TIPO_TEMPLATE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_TEMPO_CLIENTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| TEMPO_CLIENTE | NUMBER | obrigatório |  | tamanho 22, precis?o 20, escala 0 |
| TEMPO_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 20, escala 0 |
| QUANTIDADE_ENTREGA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TEMPO_PEDIDO | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| VALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 2 |
| ID | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_CLIENTE | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_TEMPO_MEDIO_ATIVIDADE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| CODATIV | VARCHAR2 | obrigatório |  | tamanho 50 |
| TEMPO_MEDIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_TEMP_CARREG_KMINICIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ORIGEM | VARCHAR2 | permite nulo |  | tamanho 100 |
| NUMCAR_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMCAR_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| KMINICIAL_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| KMINICIAL_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| DATA_DO_LOG | DATE | permite nulo |  | tamanho 7 |
| OSUSER | VARCHAR2 | permite nulo |  | tamanho 100 |

## MXMP_TEMP_LOG_PEDC_NUMSEQENTREGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ORIGEM | VARCHAR2 | permite nulo |  | tamanho 100 |
| NUMSEQENTREGA_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| NUMSEQENTREGA_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| NUMPED | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| DATA_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DATA_NOVO | DATE | permite nulo |  | tamanho 7 |
| POSICAO_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| POSICAO_NOVO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMCAR_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMCAR_NOVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMNOTA_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| NUMNOTA_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| MOTORISTA_ANTIGO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MOTORISTA_NOVO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTATUALIZ_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DTATUALIZ_NOVO | DATE | permite nulo |  | tamanho 7 |
| NUMSEQMONTAGEM_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NUMSEQMONTAGEM_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NUMITENS_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| NUMITENS_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| CODMOTORISTA_ANTIGO | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| CODMOTORISTA_NOVO | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| DTFAT_ANTIGO | DATE | permite nulo |  | tamanho 7 |
| DTFAT_NOVO | DATE | permite nulo |  | tamanho 7 |
| DATA_DO_LOG | DATE | permite nulo |  | tamanho 7 |

## MXMP_TESTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODPROD | NUMBER | permite nulo |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMVERSAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATAATUALIZACAO | DATE | permite nulo |  | tamanho 7 |

## MXMP_TIME_LINE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_PEDIDO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA | DATE | obrigatório |  | tamanho 7 |
| SITUACAO | VARCHAR2 | obrigatório |  | tamanho 2 |
| EMAIL | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_EVENTO | DATE | obrigatório |  | tamanho 7 |

## MXMP_TIPOS_DEVOLUCAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_MOTIVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| STATUS | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_TIPO_AUSENCIA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 35 |
| ATIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| ABONA_HORAS | VARCHAR2 | obrigatório |  | tamanho 1 |

## MXMP_TIPO_CARGA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_TRANSPORTADORA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_PARAMETRO_RESTRICAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO_TIPO_CARGA | VARCHAR2 | permite nulo |  | tamanho 100 |

## MXMP_TIPO_DESPESA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ATIVO | VARCHAR2 | permite nulo |  | tamanho 1 |
| UTILIZA_TMS | VARCHAR2 | permite nulo |  | tamanho 1 |
| ID_CONTA | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_TIPO_EVENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_TIPO_JUSTIFICATIVA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 40 |
| TEXTO | VARCHAR2 | permite nulo |  | tamanho 256 |

## MXMP_TIPO_NOTIFICACAO_CARREGAMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_TIPO_SERVICO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 400 |
| SITUACAO | VARCHAR2 | obrigatório |  | tamanho 1 |
| FREQUENCIA_KM | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| FREQUENCIA_MENSAL | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| ID_CATEGORIA | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_TIPO_TEMPLATE_WHATSAPP

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 40 |
| MENSAGEM_PADRAO | NVARCHAR2 | obrigatório |  | tamanho 512 |
| ATIVO | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_TIPO_VEICULO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 30 |
| TAMANHO_VEICULO | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| ID_COMBUSTIVEL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_HIERARQUIA_ENTREGA | NUMBER | permite nulo |  | tamanho 22 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_TIPO_VENDA_TABELA_FRETE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22 |
| TIPO_VENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 0 |

## MXMP_TOKEN_VALIDACAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| UTILIZADO | NUMBER | obrigatório |  | tamanho 22, precis?o 1, escala 0 |
| DATA_EXPIRACAO | DATE | obrigatório |  | tamanho 7 |
| TIPO_FUNCIONALIDADE | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_SOLICITANTE | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_AUTORIZADOR | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TOKEN | VARCHAR2 | obrigatório |  | tamanho 20 |
| OBSERVACAO | VARCHAR2 | permite nulo |  | tamanho 400 |
| ID_REGISTRO | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPO_REGISTRO | VARCHAR2 | permite nulo |  | tamanho 1 |
| DATA_UTILIZADO | TIMESTAMP(6) | permite nulo |  | tamanho 11, escala 6 |

## MXMP_TOUR

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_TOUR | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 100 |
| ID_SOLUCAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| RELEASE | VARCHAR2 | obrigatório |  | tamanho 10 |
| TOUR_ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_TOUR_USUARIO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID_TOUR_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_TOUR | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DATA_EXECUCAO | DATE | obrigatório |  | tamanho 7 |

## MXMP_TRANSPORTADORA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| TIPO_PESSOA | VARCHAR2 | obrigatório |  | tamanho 1 |
| DOCUMENTO | VARCHAR2 | obrigatório |  | tamanho 20 |
| DESCRICAO_DOCUMENTO | VARCHAR2 | obrigatório |  | tamanho 500 |
| ID_ERP | VARCHAR2 | permite nulo |  | tamanho 1000 |
| CEP | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| LOGRADOURO | VARCHAR2 | obrigatório |  | tamanho 500 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 500 |
| NUMERO | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| COMPLEMENTO | VARCHAR2 | permite nulo |  | tamanho 100 |
| ID_ESTADO | VARCHAR2 | permite nulo |  | tamanho 2 |
| ID_CIDADE | VARCHAR2 | permite nulo |  | tamanho 50 |
| EMAIL | VARCHAR2 | permite nulo |  | tamanho 500 |
| TELEFONE | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |

## MXMP_USUARIOS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| LOGIN | VARCHAR2 | obrigatório |  | tamanho 500 |
| SENHA | VARCHAR2 | permite nulo |  | tamanho 60 |
| NOME | VARCHAR2 | obrigatório |  | tamanho 50 |
| DATA_CADASTRO | DATE | obrigatório |  | tamanho 7 |
| EXCLUIDO | VARCHAR2 | permite nulo |  | tamanho 1 |
| ID_EMPREGADO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TIPO | VARCHAR2 | obrigatório |  | tamanho 1 |
| PREFERENCIAS_ROTAS | VARCHAR2 | permite nulo |  | tamanho 2000 |
| APELIDO | VARCHAR2 | permite nulo |  | tamanho 500 |
| CARRETEIRO | VARCHAR2 | permite nulo |  | tamanho 1 |
| DATA_ULTIMO_LOGON | DATE | permite nulo |  | tamanho 7 |
| ENCARREGADO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_ARQUIVO | NUMBER | permite nulo |  | tamanho 22 |
| ID_JORNADA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_MOTORISTA | VARCHAR2 | permite nulo |  | tamanho 50 |
| TELEFONE | VARCHAR2 | permite nulo |  | tamanho 15 |
| ID_USUARIO_MAXIMA | VARCHAR2 | permite nulo |  | tamanho 50 |
| QTD_DIAS_BUSCA_PAINEL | VARCHAR2 | permite nulo |  | tamanho 20 |
| TIPO_USUARIO | VARCHAR2 | permite nulo |  | tamanho 3 |
| EMAIL | VARCHAR2 | permite nulo |  | tamanho 150 |
| CARGO | VARCHAR2 | permite nulo |  | tamanho 100 |
| ID_PERFIL | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_USUARIOS_ACESSO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_USUARIO_MAXIMA | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_OFERTA | NUMBER | obrigatório |  | tamanho 22 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXMP_USUARIOS_FILIAIS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_FILIAL | VARCHAR2 | obrigatório |  | tamanho 50 |

## MXMP_USUARIOS_ROTAS

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_ROTA | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_USUARIO_PERFIL_ACESSO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_PERFIL_ACESSO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_USUARIO_VISAO_GERENCIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_VISAO_GERENCIAL | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| ID_USUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| VALORES_VISIVEIS | BLOB | permite nulo |  | tamanho 4000 |

## MXMP_VEICULOS_PREF_ROTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_ROTA_COMP | NUMBER | obrigatório |  | tamanho 22 |
| ID_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_VEICULO_COMPLEMENTO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| QUANTIDADE_MAXIMA_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ID_TIPO_VEICULO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| HORA_INICIO_OPERACAO | VARCHAR2 | obrigatório |  | tamanho 5 |
| HORA_FIM_OPERACAO | VARCHAR2 | obrigatório |  | tamanho 5 |
| ID_MOTORISTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| CONSUMO_MEDIO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ID_TRANSPORTADORA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| VELOCIDADE_MAXIMA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| ID_TABELA_FRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| CHASSI | VARCHAR2 | permite nulo |  | tamanho 20 |
| VL_VEICULO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| RENAVAM | VARCHAR2 | permite nulo |  | tamanho 20 |
| CAPACIDADE_TANQUE | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| PROPRIEDADE | VARCHAR2 | permite nulo |  | tamanho 2 |
| ANO_FABRICACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| ANO_MODELO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| TIPO_CARROCERIA | VARCHAR2 | permite nulo |  | tamanho 2 |
| QTD_EIXOS | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| NOME_SEGURADORA | VARCHAR2 | permite nulo |  | tamanho 200 |
| VL_SEGURO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| VENC_SEGURO | DATE | permite nulo |  | tamanho 7 |
| UTILIZA_RODIZIO_PLACAS | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| VL_IPVA | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| VL_LICENCIAMENTO | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 2 |
| TIPO_CATEGORIA | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| TIPO_RODAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| ID_SEM_PARAR | VARCHAR2 | permite nulo |  | tamanho 20 |
| PEDAGIO_ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| HODOMETRO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| ID_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXMP_VEICULO_COTACAO_FORNECEDORES

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_VEICULO | VARCHAR2 | obrigatório |  | tamanho 50 |
| ID_COTACAO | NUMBER | obrigatório |  | tamanho 22 |

## MXMP_VEICULO_INDISPONIBILIDADE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| INICIO | DATE | obrigatório |  | tamanho 7 |
| FIM | DATE | obrigatório |  | tamanho 7 |
| ID_VEICULO_COMPLEMENTO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |

## MXMP_VEICULO_RASTREADOR

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| ID_VEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_RASTREADOR | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| IDENTIFICADOR_RASTREADOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| ATIVO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXMP_VERSAO_LOGISTICA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODPROD | NUMBER | permite nulo |  | tamanho 22 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMVERSAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATAATUALIZACAO | DATE | permite nulo |  | tamanho 7 |

## MXMP_VISAO_GERENCIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| DESCRICAO | VARCHAR2 | obrigatório |  | tamanho 255 |
| PERIODO_ENTREGAS_ATRASADAS | NUMBER | permite nulo |  | tamanho 22 |

## MXMP_VOLUMES_CONF_ENT

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| ID | NUMBER | obrigatório |  | tamanho 22 |
| VOLUME | VARCHAR2 | permite nulo |  | tamanho 100 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| ID_ENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |

## MXSATIVI

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODATIV | VARCHAR2 | obrigatório |  | tamanho 50 |
| RAMO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCDESC | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| CALCULAST | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| CODATIVPRINC | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXSCIDADE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODCIDADE | VARCHAR2 | obrigatório |  | tamanho 50 |
| NOMECIDADE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODIBGE | VARCHAR2 | permite nulo |  | tamanho 50 |
| UF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXSCLIENT

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODCLIPRINC | VARCHAR2 | permite nulo |  | tamanho 50 |
| CLIENTE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| FANTASIA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CLASSEVENDA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CGCENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTULTCOMP | DATE | permite nulo |  | tamanho 7 |
| BAIRROENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CEPENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MUNICENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| COMPLEMENTOENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ENDERENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMEROENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ESTENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODFILIALNF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| EMAIL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| IEENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| IMENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODPLPAG | VARCHAR2 | permite nulo |  | tamanho 50 |
| TELENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOFJ | VARCHAR2 | permite nulo |  | tamanho 4000 |
| UTILIZAIESIMPLIFICADA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONTRIBUINTE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONSUMIDORFINAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTVENCALVARAFUNC | DATE | permite nulo |  | tamanho 7 |
| BLOQUEIO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CALCULAST | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ATUALIZASALDOCCDESCFIN | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTBLOQ | DATE | permite nulo |  | tamanho 7 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCOMCLI | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| PERDESCISENTOICMS | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 2 |
| VALIDARMULTIPLOVENDA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| FRETEDESPACHO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODFORNECFRETE | VARCHAR2 | permite nulo |  | tamanho 50 |
| VLFRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| VLMAXCOBFRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| VALIDARCAMPANHABRINDE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBS2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBSENTREGA1 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBSENTREGA2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBSENTREGA3 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ACEITAVENDAFRACAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODPRACA | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODATV1 | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPODESCISENCAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERDESC | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| PLPAGNEG | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CLIENTEMONITORADO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ORGAOPUBFEDERAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ORGAOPUB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| IVAFONTE | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| USAIVAFONTEDIFERENCIADO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOEMPRESA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CLIENTEFONTEST | VARCHAR2 | permite nulo |  | tamanho 4000 |
| SULFRAMA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ISENTODIFALIQUOTAS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ISENTOIPI | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ISENTOICMS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODREDE | VARCHAR2 | permite nulo |  | tamanho 50 |
| CONDVENDA1 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA3 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA4 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA5 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA6 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA7 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA8 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA9 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA10 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA11 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA12 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA13 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA14 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA20 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA98 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONDVENDA99 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPODOCUMENTO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| SIMPLESNACIONAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| RG | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ORGAORG | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODCLIPALM | VARCHAR2 | permite nulo |  | tamanho 50 |
| PONTOREFER | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TELCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TELCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| FAXCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| FAXCLI | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PREDIOPROPRIO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBSCREDITO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TELENT1 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CAIXAPOSTAL | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 0 |
| NUMBANCO1 | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| NUMAGENCIA1 | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| NUMCCORRENTE1 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMBANCO2 | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| NUMAGENCIA2 | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| NUMCCORRENTE2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| QTCHECKOUT | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| SITE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBSGERENCIAL1 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBSGERENCIAL2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBSGERENCIAL3 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DATACOLETA | DATE | permite nulo |  | tamanho 7 |
| EMAILNFE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PAISENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| BAIRROCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CEPCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MUNICCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| COMPLEMENTOCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ENDERCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMEROCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ESTCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| BAIRROCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CEPCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MUNICCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| COMPLEMENTOCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ENDERCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMEROCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ESTCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTVENCSUFRAMA | DATE | permite nulo |  | tamanho 7 |
| NUMALVARA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMALVARAANVISA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMALVARAFUNC | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMALVARASUS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTVENCALVARA | DATE | permite nulo |  | tamanho 7 |
| DTVENCALVARAANVISA | DATE | permite nulo |  | tamanho 7 |
| DTVENCALVARASUS | DATE | permite nulo |  | tamanho 7 |
| OBS3 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBS4 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBS5 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ISENCAOSUFRAMA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| USADESCONTOICMS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| BLOQUEIOSEFAZ | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODCIDADE | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTVALIDADEIBAMA | DATE | permite nulo |  | tamanho 7 |
| REGISTROIBAMA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| BLOQUEIODEFINITIVO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODFUNCULTALTER | VARCHAR2 | permite nulo |  | tamanho 50 |
| PRAZOADICIONAL | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| VIP | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTVENCCRF | DATE | permite nulo |  | tamanho 7 |
| REPASSE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ORIGEMPRECO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| USADESCFINSEPARADODESCCOM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMALVARARETINOICO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTVENCALVARARETINOICO | DATE | permite nulo |  | tamanho 7 |
| NUMCRF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODUSUR1 | VARCHAR2 | permite nulo |  | tamanho 50 |
| VALIDAMAXVENDAPF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TURNOENTREGA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ISENTOTXBOLETO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| USADEBCREDRCA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| UTILIZACALCULOSTMT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODCNAE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| SALDOLIMCREDBROKER | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLLIMCREDBROKER | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| TIPOCLIMED | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTULTALTER | DATE | permite nulo |  | tamanho 7 |
| USACMVDIFERENCIADO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTVENCLIMCRED | DATE | permite nulo |  | tamanho 7 |
| FORCACLIPJ | CHAR | permite nulo |  | tamanho 1 |
| CODUSUR2 | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODUSUR3 | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTCADASTRO | DATE | permite nulo |  | tamanho 7 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| OBSENTREGA4 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| LIMCRED | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| DTEXCLUSAO | DATE | permite nulo |  | tamanho 7 |
| CODBAIRROENT | VARCHAR2 | permite nulo |  | tamanho 50 |
| PERDESCFIN | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 2 |
| NUMSEQ | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TELCELENT | VARCHAR2 | permite nulo |  | tamanho 1000 |
| HORARIORECEB | VARCHAR2 | permite nulo |  | tamanho 5 |
| EMITEDUP | VARCHAR2 | permite nulo |  | tamanho 1 |
| DTPRIMCOMPRA | DATE | permite nulo |  | tamanho 7 |
| RATINGSCI2 | VARCHAR2 | permite nulo |  | tamanho 2 |
| RATINGSCI1 | VARCHAR2 | permite nulo |  | tamanho 2 |
| RATINGSCI | VARCHAR2 | permite nulo |  | tamanho 2 |
| DTULTCONSULTASCI | DATE | permite nulo |  | tamanho 7 |
| DTULTCONSULTASERASA | DATE | permite nulo |  | tamanho 7 |
| NUMREGIAOCLI | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NUMDIASSEMVENDA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CGCENTSF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODROTA | VARCHAR2 | permite nulo |  | tamanho 50 |
| CONDVENDA24 | VARCHAR2 | permite nulo |  | tamanho 10 |
| DIA_VISITA_SEGUNDA | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIA_VISITA_TERCA | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIA_VISITA_QUARTA | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIA_VISITA_QUINTA | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIA_VISITA_SEXTA | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIA_VISITA_SABADO | VARCHAR2 | permite nulo |  | tamanho 1 |
| FORCECLIPF | VARCHAR2 | permite nulo |  | tamanho 1 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 1 |
| FAIXASORTIMENTO | VARCHAR2 | permite nulo |  | tamanho 50 |
| FIXARCOORDENADA | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| COZINHAINDUSTRIAL | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODROTAINSERVIVEL | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| CODPROMOCAOMED | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 0 |
| STOCODFILIAL | VARCHAR2 | permite nulo |  | tamanho 2 |
| RIOLOG | VARCHAR2 | permite nulo |  | tamanho 2 |
| PRECOUTILIZADONFE | VARCHAR2 | permite nulo |  | tamanho 50 |
| LIMITECREDSUPPLI | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 6 |
| UTILIZAPEDCLINFE | VARCHAR2 | permite nulo |  | tamanho 2 |
| CGCENTREGA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ATENDEDOMINGO | VARCHAR2 | permite nulo |  | tamanho 1 |
| ATENDESEGUNDA | VARCHAR2 | permite nulo |  | tamanho 1 |
| ATENDETERCA | VARCHAR2 | permite nulo |  | tamanho 1 |
| ATENDEQUARTA | VARCHAR2 | permite nulo |  | tamanho 1 |
| ATENDEQUINTA | VARCHAR2 | permite nulo |  | tamanho 1 |
| ATENDESEXTA | VARCHAR2 | permite nulo |  | tamanho 1 |
| ATENDESABADO | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODGRUPOTRIBUTCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| POSSUIBENFFISCAL | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXSCLIENTENDENT

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODENDENTCLI | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODBAIRROENT | VARCHAR2 | permite nulo |  | tamanho 50 |
| BAIRROENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MUNICENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ESTENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CEPENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ENDERENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| COMPLEMENTOENT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODPRACAENT | VARCHAR2 | permite nulo |  | tamanho 50 |
| APELIDOUNIDADE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| NUMEROENT | VARCHAR2 | permite nulo |  | tamanho 400 |
| PONTOREFER | VARCHAR2 | permite nulo |  | tamanho 400 |
| CODCIDADE | VARCHAR2 | permite nulo |  | tamanho 400 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 22 |
| NUMREGIAO | VARCHAR2 | permite nulo |  | tamanho 50 |

## MXSCOB

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODCOB | VARCHAR2 | obrigatório |  | tamanho 4000 |
| COBRANCA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NIVELVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| CARTAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| BOLETO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| VLMINPEDIDO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PRAZOMAXIMOVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| COBRANCABROKER | VARCHAR2 | permite nulo |  | tamanho 4000 |
| COBSUPPLIERCARD | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NAOVALIDAPRAZOMEDIO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCMULTA | NUMBER | permite nulo |  | tamanho 22, precis?o 7, escala 4 |
| DIASCARENCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| TXJUROS | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| CALCJUROSCOBRANCA | VARCHAR2 | permite nulo |  | tamanho 1 |
| MXINAD | VARCHAR2 | permite nulo |  | tamanho 1 |
| MXDIASINAD | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| TIPOCOMISSAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| PAGCOMISSAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| NUMDIASPROTESTO | VARCHAR2 | permite nulo |  | tamanho 2 |
| TIPOVENDA | VARCHAR2 | permite nulo |  | tamanho 2 |
| TIPOCOBRANCA | VARCHAR2 | permite nulo |  | tamanho 2 |
| CODMOEDA | VARCHAR2 | permite nulo |  | tamanho 4 |
| VALIDALIMITECREDITO | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXSCONTATO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODCONTATO | VARCHAR2 | obrigatório |  | tamanho 50 |
| CODCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| NOMECONTATO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOCONTATO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CGCCPF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTNASCIMENTO | DATE | permite nulo |  | tamanho 7 |
| HOBBIE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIME | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NOMECONJUGE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTNASCCONJUGE | DATE | permite nulo |  | tamanho 7 |
| CARGO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TELEFONE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CELULAR | VARCHAR2 | permite nulo |  | tamanho 4000 |
| EMAIL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXSDOCELETRONICO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODUSUARIO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| NUMPED | NUMBER | obrigatório |  | tamanho 22, precis?o 15, escala 0 |
| NUMTRANSACAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| SEQUENCIA | NUMBER | obrigatório |  | tamanho 22, precis?o 5, escala 0 |
| DADOS | VARCHAR2 | obrigatório |  | tamanho 4000 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 1 |

## MXSEMPR

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| MATRICULA | NUMBER | obrigatório |  | tamanho 22, precis?o 8, escala 0 |
| NOME | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODSETOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| ENVIAFV | VARCHAR2 | permite nulo |  | tamanho 4000 |
| EMAIL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| CODVEICULO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NOME_GUERRA | VARCHAR2 | permite nulo |  | tamanho 400 |
| FONE | VARCHAR2 | permite nulo |  | tamanho 400 |
| CELULAR | VARCHAR2 | permite nulo |  | tamanho 400 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 10 |
| TIPO | VARCHAR2 | permite nulo |  | tamanho 1 |
| DTVALIDADECNH | DATE | permite nulo |  | tamanho 7 |
| DT_EXCLUSAO | DATE | permite nulo |  | tamanho 7 |
| CPF | VARCHAR2 | permite nulo |  | tamanho 20 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| USUARIOBD | VARCHAR2 | permite nulo |  | tamanho 400 |
| CODUSUR | VARCHAR2 | permite nulo |  | tamanho 400 |
| TIPOMOTORISTA | VARCHAR2 | permite nulo |  | tamanho 5 |
| ENDERECO | VARCHAR2 | permite nulo |  | tamanho 100 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CIDADE | VARCHAR2 | permite nulo |  | tamanho 50 |
| ESTADO | VARCHAR2 | permite nulo |  | tamanho 2 |

## MXSFILIAL

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODIGO | VARCHAR2 | obrigatório |  | tamanho 4000 |
| RAZAOSOCIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CGC | VARCHAR2 | permite nulo |  | tamanho 4000 |
| IE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ENDERECO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CIDADE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| UF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TELEFONE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| FAX | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOAVALIACAOCOMISSAO | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| CONSIDERARCOMISSAOZERO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ACEITAVENDASEMEST | VARCHAR2 | permite nulo |  | tamanho 4000 |
| BLOQUEARPEDIDOSABAIXOVLMINIMO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ALTERARCOBBKCHAUTOMATICO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| UTILIZAVENDAPOREMBALAGEM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOFRETEAUTO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| LANCARFRETEPESOAUTFAT | VARCHAR2 | permite nulo |  | tamanho 4000 |
| UTILIZANFE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CALCULARIPIVENDA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| USAESTOQUEDEPFECHADO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| USAWMS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| AUTOSERVICO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOPRECIFICACAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| BROKER | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOBROKER | VARCHAR2 | permite nulo |  | tamanho 4000 |
| USADIAUTILFILIAL | VARCHAR2 | permite nulo |  | tamanho 1 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| CODGRUPOFILIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| FANTASIA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCACRESCIMOBALCAO | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 6 |
| CONTROLENFEPORROTA | VARCHAR2 | permite nulo |  | tamanho 2 |
| CONTROLENFEPORSERIE | VARCHAR2 | permite nulo |  | tamanho 2 |

## MXSHISTORICOPEDC

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMPED | NUMBER | obrigatório |  | tamanho 22, precis?o 15, escala 0 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| VLTOTAL | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| VLTABELA | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| VLATEND | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| CODCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODUSUR | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODFILIALNF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| POSICAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMCAR | VARCHAR2 | permite nulo |  | tamanho 50 |
| CONDVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 0 |
| CODPLPAG | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODCOB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMNOTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ORIGEMPED | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MOTORISTA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODFORNECFRETE | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFORNECREDESPACHO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFUNCLIBERA | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTLIBERA | DATE | permite nulo |  | tamanho 7 |
| CODFUNCCANC | VARCHAR2 | permite nulo |  | tamanho 50 |
| DATACANC | DATE | permite nulo |  | tamanho 7 |
| MOTIVO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTEMISSAOMAPA | DATE | permite nulo |  | tamanho 7 |
| CODFUNCEMISSAOMAPA | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTINICIALSEP | DATE | permite nulo |  | tamanho 7 |
| DTFINALSEP | DATE | permite nulo |  | tamanho 7 |
| CODFUNCSEP | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTINICIALCHECKOUT | DATE | permite nulo |  | tamanho 7 |
| DTFINALCHECKOUT | DATE | permite nulo |  | tamanho 7 |
| CODFUNCCONF | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTFAT | DATE | permite nulo |  | tamanho 7 |
| HORAFAT | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| CODFUNCFAT | VARCHAR2 | permite nulo |  | tamanho 50 |
| TOTPESO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 2 |
| MINUTOFAT | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| HORA | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| MINUTO | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| OBSENTREGA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMPEDRCA | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| NUMORCA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| MOTORISTACONTATO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODEMITENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| DTABERTURAPEDPALM | DATE | permite nulo |  | tamanho 7 |
| DTWMS | DATE | permite nulo |  | tamanho 7 |
| NUMSEQENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| NUMSEQMONTAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NUMSEQROTA | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| NUMVIASMAPASEP | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| OBS1 | VARCHAR2 | permite nulo |  | tamanho 100 |
| OBS2 | VARCHAR2 | permite nulo |  | tamanho 100 |
| OBSENTREGA1 | VARCHAR2 | permite nulo |  | tamanho 100 |
| OBSENTREGA2 | VARCHAR2 | permite nulo |  | tamanho 100 |
| OBSENTREGA3 | VARCHAR2 | permite nulo |  | tamanho 100 |
| RESTRICAOTRANSP | VARCHAR2 | permite nulo |  | tamanho 1 |
| TOTVOLUME | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VENDAASSISTIDA | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODENDENTCLI | VARCHAR2 | permite nulo |  | tamanho 50 |
| NUMTRANSVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 0 |
| CODPRACA | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTCANCEL | DATE | permite nulo |  | tamanho 7 |
| NUMPEDENTFUT | NUMBER | permite nulo |  | tamanho 22, precis?o 15, escala 0 |
| CODENDENT | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODSUPERVISOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| DTFECHAMENTOPEDPALM | DATE | permite nulo |  | tamanho 7 |
| CODDISTRIB | VARCHAR2 | permite nulo |  | tamanho 10 |
| DTENTREGA | DATE | permite nulo |  | tamanho 7 |
| DTAGENDAENTREGA | DATE | permite nulo |  | tamanho 7 |
| NUMITENS | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| VLCUSTOFIN | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 2 |
| VLBONIFIC | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| VLFRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| VLOUTRASDESP | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 3 |
| CODMOTORISTA | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| USACREDRCA | VARCHAR2 | permite nulo |  | tamanho 1 |
| NUMCAIXA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| QTLITRAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLST | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 4 |
| PERCCOMMED | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 4 |
| MOTIVOPOSICAO | VARCHAR2 | permite nulo |  | tamanho 60 |
| NUMREGIAO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PERCOM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| COMISSAO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| NUMVOLUME | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| XMLGEN | VARCHAR2 | permite nulo |  | tamanho 100 |
| NUMPEDTV1 | NUMBER | permite nulo |  | tamanho 22, precis?o 15, escala 0 |
| NUMPEDORIGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 15, escala 0 |
| DATA_IMPORTACAO_XML | DATE | permite nulo |  | tamanho 7 |
| EMITENTE | VARCHAR2 | permite nulo |  | tamanho 100 |
| NUMCARANTERIOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| BRINDE | VARCHAR2 | permite nulo |  | tamanho 1 |
| TURNOENTREGA | VARCHAR2 | permite nulo |  | tamanho 5 |
| FRETEDESPACHO | VARCHAR2 | permite nulo |  | tamanho 10 |
| TIPOPRIORIDADEENTREGA | VARCHAR2 | permite nulo |  | tamanho 1 |
| NUMCUPOM | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| TIPODOCUMENTO | VARCHAR2 | permite nulo |  | tamanho 1 |
| INDENIZADO | VARCHAR2 | permite nulo |  | tamanho 1 |

## MXSHISTORICOPEDCORTE

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMPED | NUMBER | obrigatório |  | tamanho 22, precis?o 15, escala 0 |
| CODPROD | VARCHAR2 | obrigatório |  | tamanho 50 |
| QTCORTADA | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 2 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXSHISTORICOPEDFALTA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMPED | NUMBER | obrigatório |  | tamanho 22, precis?o 15, escala 0 |
| CODPROD | VARCHAR2 | obrigatório |  | tamanho 50 |
| QTPEDIDA | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 2 |
| QTFALTA | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 2 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXSHISTORICOPEDI

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMPED | NUMBER | obrigatório |  | tamanho 22, precis?o 15, escala 0 |
| CODPROD | VARCHAR2 | obrigatório |  | tamanho 50 |
| NUMSEQ | NUMBER | obrigatório |  | tamanho 22, precis?o 20, escala 0 |
| QT | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 6 |
| PVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PTABELA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| CODAUXILIAR | VARCHAR2 | permite nulo |  | tamanho 50 |
| QT_DEVOLVIDA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| POSICAO | VARCHAR2 | permite nulo |  | tamanho 2 |
| NUMCAR | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 0 |
| TIPOENTREGA | VARCHAR2 | permite nulo |  | tamanho 2 |
| ST | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLCUSTOFIN | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLBONIFIC | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLREPASSE | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLIPI | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| DATA | DATE | permite nulo |  | tamanho 7 |
| PBONIFIC | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| BONIFIC | VARCHAR2 | permite nulo |  | tamanho 2 |
| TRUNCARITEM | VARCHAR2 | permite nulo |  | tamanho 1 |
| VLSUBTOTITEM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 2 |
| VLFRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLOUTRASDESP | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PBASERCA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PERCOM | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| QTLITRAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| NUMCARANTERIOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| BRINDE | VARCHAR2 | permite nulo |  | tamanho 1 |
| QTDIFPESO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 0 |
| CODFILIALRETIRA | VARCHAR2 | permite nulo |  | tamanho 2 |
| QTUNITCX | NUMBER | permite nulo |  | tamanho 22 |

## MXSPLPAG

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODPLPAG | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMDIAS | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| DTVENC1 | DATE | permite nulo |  | tamanho 7 |
| DTVENC2 | DATE | permite nulo |  | tamanho 7 |
| DTVENC3 | DATE | permite nulo |  | tamanho 7 |
| PRAZO1 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO2 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO3 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO4 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO5 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO6 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO7 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO8 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO9 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO10 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO11 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PRAZO12 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| VLMINPEDIDO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| NUMPR | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPORESTRICAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODRESTRICAO | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPOVENDA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MARGEMMIN | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| PERTXFIM | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| TIPOPRAZO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOENTRADA | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| VENDABK | VARCHAR2 | permite nulo |  | tamanho 4000 |
| FORMAPARCELAMENTO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| VLMINPARCELA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| DIASMINPARCELA | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| DIASMAXPARCELA | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| NUMPARCELAS | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 0 |
| NUMITENSMINIMO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| USAMULTIFILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| TIPOPLANO | VARCHAR2 | permite nulo |  | tamanho 1 |
| REPLICADO | VARCHAR2 | permite nulo |  | tamanho 10 |
| USASUPPLICARD | VARCHAR2 | permite nulo |  | tamanho 10 |
| LETRAPLPAG | VARCHAR2 | permite nulo |  | tamanho 10 |

## MXSPRACA

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODPRACA | VARCHAR2 | obrigatório |  | tamanho 50 |
| PRACA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMREGIAO | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| ROTA | VARCHAR2 | permite nulo |  | tamanho 50 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| SEQROTA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| POPULACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 0 |
| VLMINCARREG | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |

## MXSPRODUT

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODPROD | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| EMBALAGEM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| UNIDADE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PESOLIQ | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 6 |
| PESOBRUTO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 6 |
| CODEPTO | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODSEC | VARCHAR2 | permite nulo |  | tamanho 50 |
| PCOMINT1 | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| QTUNIT | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| OBS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PCOMREP1 | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| PCOMEXT1 | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| CODFORNEC | VARCHAR2 | permite nulo |  | tamanho 50 |
| CLASSE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| QTUNITCX | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 2 |
| REVENDA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTEXCLUSAO | DATE | permite nulo |  | tamanho 7 |
| CODPRODPRINC | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFAB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODCATEGORIA | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| MULTIPLO | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| TIPOMERC | VARCHAR2 | permite nulo |  | tamanho 10 |
| ACEITAVENDAFRACAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| INFORMACOESTECNICAS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| FRETEESPECIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DIRFOTOPROD | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PRAZOMEDIOVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 0 |
| TIPOCOMISSAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TIPOESTOQUE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODDISTRIB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODMARCA | VARCHAR2 | permite nulo |  | tamanho 50 |
| VLPAUTAIPIVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLIPIPORKGVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PERCIPIVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| CODLINHAPROD | VARCHAR2 | permite nulo |  | tamanho 50 |
| OBS2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODFILIALRETIRA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| IMPORTADO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCDIFALIQUOTAS | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| VLPAUTA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| VLIPIPORKG | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PERCIPI | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 4 |
| CHECARMULTIPLOVENDABNF | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODAUXILIAR | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODAUXILIAR2 | VARCHAR2 | permite nulo |  | tamanho 50 |
| CUSTOREP | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PRECOMAXCONSUM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| QTMINIMAATACADO | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| PSICOTROPICO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| QTDEMAXSEPARPEDIDO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PESOPECA | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 8 |
| PESOBRUTOMASTER | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 3 |
| PESOVARIAVEL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCDIFERENCAKGFRIO | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 4 |
| UNIDADEMASTER | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODPRINCIPATIVO | VARCHAR2 | permite nulo |  | tamanho 50 |
| NOMEECOMMERCE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERINDENIZ | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| NUMORIGINAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONTROLADOIBAMA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NBM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DADOSTECNICOS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTVENC | DATE | permite nulo |  | tamanho 7 |
| CUSTOREPZFM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| PERCBONIFICVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| PRECOMAXCONSUMZFM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| CODSUBCATEGORIA | VARCHAR2 | permite nulo |  | tamanho 50 |
| USAPMCBASEST | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CONFAZ | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTCADASTRO | DATE | permite nulo |  | tamanho 7 |
| VOLUME | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 8 |
| CLASSIFICFISCAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PRECOFIXO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| ALTURA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 6 |
| EMBALAGEMMASTER | VARCHAR2 | permite nulo |  | tamanho 4000 |
| VERIFCRAMOATIVCALCST | VARCHAR2 | permite nulo |  | tamanho 4000 |
| VERIFCDESCCAIXAFECHADA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCDESCCAIXAFECHADA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| DESCRICAO2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NATUREZAPRODUTO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| UTILIZAPRECOMAXCONSUMIDOR | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PRAZOMAXVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 0 |
| CLASSEVENDA | VARCHAR2 | permite nulo |  | tamanho 1 |
| PAISORIGEM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| LETRAPAGINA | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODLINHA | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODPRODMASTER | VARCHAR2 | permite nulo |  | tamanho 50 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| ISBRINDE | VARCHAR2 | permite nulo |  | tamanho 1 |
| LITRAGEM | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| ENVIARFORCAVENDAS | VARCHAR2 | permite nulo |  | tamanho 1 |
| PRINCIPIOATIVO | VARCHAR2 | permite nulo |  | tamanho 100 |
| ALTURAPAL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| LOTEPRODUCAO | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 2 |
| PERACRESCMAX | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| ID_CLIENTE | NUMBER | permite nulo |  | tamanho 22 |
| RESTRICAOTRANSP | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODCA | VARCHAR2 | permite nulo |  | tamanho 100 |
| ISENTOSTCOZINHAINDUSTRIAL | VARCHAR2 | permite nulo |  | tamanho 1 |
| ACEITATROCAINSERVIVEL | VARCHAR2 | permite nulo |  | tamanho 1 |
| CODINSERVIVEL | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| CODAUXILIARTRIB | VARCHAR2 | permite nulo |  | tamanho 50 |
| QTMINSUGCOMPRA | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 8 |

## MXSREGIAO

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| NUMREGIAO | NUMBER | obrigatório |  | tamanho 22, precis?o 10, escala 0 |
| REGIAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERFRETEESPECIAL | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| PERFRETETERCEIROS | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| VLFRETEKGVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| PERFRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| REGIAOZFM | VARCHAR2 | permite nulo |  | tamanho 4000 |
| STATUS | VARCHAR2 | permite nulo |  | tamanho 4000 |
| NUMTABELA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODESTABELECIMENTO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| VLMINFATBK | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 6 |
| VLMINFATCH | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 6 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODREPRESENTANTE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| VLFRETEKG | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| UF | VARCHAR2 | permite nulo |  | tamanho 2 |

## MXSROTAEXP

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODROTA | VARCHAR2 | obrigatório |  | tamanho 50 |
| DESCRICAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| SITUACAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DIASENTREGA | NUMBER | permite nulo |  | tamanho 22 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| PERCAJUDA | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| VLAJUDA | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| RASTREADA | VARCHAR2 | permite nulo |  | tamanho 1 |
| TIPOCOMISSAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| PRAZOPREVENT | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| KMROTA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| NUMDIARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| VLDIARIA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| SEQENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| VLMINCARREG | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| CODROTAPRINCIPAL | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| PERCOMMOT | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 2 |
| PERCOMMOT2 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 2 |
| PERCOMMOT3 | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 2 |
| VALORCOMMOT | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| QTENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| PERFRETEVALOR | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| VLFRETEENTREGA | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| ALIQICMSFRETE | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| VLFRETETON | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 4 |
| DIASEG | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIATER | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIAQUA | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIAQUI | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIASEX | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIASAB | VARCHAR2 | permite nulo |  | tamanho 1 |
| DIADOM | VARCHAR2 | permite nulo |  | tamanho 1 |
| OBSROTA | VARCHAR2 | permite nulo |  | tamanho 2000 |

## MXSSUPERV

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODSUPERVISOR | VARCHAR2 | obrigatório |  | tamanho 50 |
| NOME | VARCHAR2 | permite nulo |  | tamanho 4000 |
| EMAIL | VARCHAR2 | permite nulo |  | tamanho 400 |
| REGIONAL | NUMBER | permite nulo |  | tamanho 22, precis?o 2, escala 0 |
| COD_CADRCA | VARCHAR2 | permite nulo |  | tamanho 50 |
| POSICAO | VARCHAR2 | permite nulo |  | tamanho 1 |
| PERCPARTVENDAPREV | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| PERCMARGEMPREV | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 4 |
| CODGERENTE | VARCHAR2 | permite nulo |  | tamanho 50 |
| TIPOSUPERVISOR | VARCHAR2 | permite nulo |  | tamanho 1 |
| PERCOMISSAO | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 2 |
| DTADMISSAO | DATE | permite nulo |  | tamanho 7 |
| DTDEMISSAO | DATE | permite nulo |  | tamanho 7 |
| CPF | VARCHAR2 | permite nulo |  | tamanho 50 |
| CODCOORDENADOR | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| VLCORRENTE | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 6 |
| VLLIMCRED | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 6 |
| USADEBCRED | VARCHAR2 | permite nulo |  | tamanho 1 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |

## MXSUSUARI

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| CODUSUR | VARCHAR2 | obrigatório |  | tamanho 50 |
| NOME | VARCHAR2 | permite nulo |  | tamanho 4000 |
| CODDISTRIB | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERMAXVENDA | NUMBER | permite nulo |  | tamanho 22, precis?o 18, escala 6 |
| TIPOVEND | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCENT | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 2 |
| PERCENT2 | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 2 |
| CODSUPERVISOR | VARCHAR2 | permite nulo |  | tamanho 50 |
| BLOQUEIO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| VLVENDAMINPED | NUMBER | permite nulo |  | tamanho 22, precis?o 12, escala 2 |
| AREAATUACAO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| USADEBCREDRCA | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TELEFONE1 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| TELEFONE2 | VARCHAR2 | permite nulo |  | tamanho 4000 |
| EMAIL | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PROXNUMPED | NUMBER | permite nulo |  | tamanho 22, precis?o 14, escala 2 |
| PROXNUMPEDFORCA | NUMBER | permite nulo |  | tamanho 22, precis?o 13, escala 0 |
| PROXNUMPEDWEB | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 0 |
| VALIDARACRESCDESCPRECOFIXO | VARCHAR2 | permite nulo |  | tamanho 4000 |
| PERCACRESFV | NUMBER | permite nulo |  | tamanho 22, precis?o 8, escala 2 |
| NUMSERIEEQUIP | NUMBER | permite nulo |  | tamanho 22, precis?o 20, escala 0 |
| QTPEDPREV | NUMBER | permite nulo |  | tamanho 22, precis?o 6, escala 0 |
| LATITUDE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| LONGITUDE | VARCHAR2 | permite nulo |  | tamanho 4000 |
| DTTERMINO | DATE | permite nulo |  | tamanho 7 |
| CODFILIAL | VARCHAR2 | permite nulo |  | tamanho 50 |
| CPF | VARCHAR2 | permite nulo |  | tamanho 50 |
| ATUALIZID | NUMBER | permite nulo |  | tamanho 22, precis?o 16, escala 0 |
| DTATUALIZ | DATE | permite nulo |  | tamanho 7 |
| CODOPERACAO | NUMBER | permite nulo |  | tamanho 22, precis?o 1, escala 0 |
| BLOQCOMIS | VARCHAR2 | permite nulo |  | tamanho 1 |
| INDICERATEIOCOMISSAO | NUMBER | permite nulo |  | tamanho 22, precis?o 5, escala 2 |
| NUMDVCCORRENTE | VARCHAR2 | permite nulo |  | tamanho 2 |
| NUMCCORRENTE | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 0 |
| NUMDVAGENCIA | VARCHAR2 | permite nulo |  | tamanho 1 |
| NUMAGENCIA | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NUMBANCO | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| OBSBLOQ | VARCHAR2 | permite nulo |  | tamanho 30 |
| DTULTVENDA | DATE | permite nulo |  | tamanho 7 |
| DTINICIO | DATE | permite nulo |  | tamanho 7 |
| VLLIMCRED | NUMBER | permite nulo |  | tamanho 22, precis?o 10, escala 2 |
| VLCORRENTE | NUMBER | permite nulo |  | tamanho 22, precis?o 24, escala 6 |
| NUMDVCCORRENTEPOUP | VARCHAR2 | permite nulo |  | tamanho 2 |
| NUMCCORRENTEPOUP | NUMBER | permite nulo |  | tamanho 22, precis?o 22, escala 0 |
| NUMDVAGENCIAPOUP | VARCHAR2 | permite nulo |  | tamanho 1 |
| NUMAGENCIAPOUP | NUMBER | permite nulo |  | tamanho 22, precis?o 4, escala 0 |
| NUMBANCOPOUP | NUMBER | permite nulo |  | tamanho 22, precis?o 3, escala 0 |
| EMAIL2 | VARCHAR2 | permite nulo |  | tamanho 100 |
| NUMCONSELHO | VARCHAR2 | permite nulo |  | tamanho 20 |
| DTULTPAGCONSELHO | DATE | permite nulo |  | tamanho 7 |
| INSCMUNICIPAL | VARCHAR2 | permite nulo |  | tamanho 15 |
| PRACA2 | VARCHAR2 | permite nulo |  | tamanho 80 |
| PRACA1 | VARCHAR2 | permite nulo |  | tamanho 80 |
| ENDERECO2 | VARCHAR2 | permite nulo |  | tamanho 40 |
| OBS2 | VARCHAR2 | permite nulo |  | tamanho 80 |
| OBS1 | VARCHAR2 | permite nulo |  | tamanho 80 |
| DTINFORMATIZA | DATE | permite nulo |  | tamanho 7 |
| BAIRRO | VARCHAR2 | permite nulo |  | tamanho 25 |
| CGC | VARCHAR2 | permite nulo |  | tamanho 20 |
| FIRMA | VARCHAR2 | permite nulo |  | tamanho 40 |
| MOTIVO | VARCHAR2 | permite nulo |  | tamanho 40 |
| FAX | VARCHAR2 | permite nulo |  | tamanho 13 |
| CI | VARCHAR2 | permite nulo |  | tamanho 20 |
| CEP | VARCHAR2 | permite nulo |  | tamanho 9 |
| ESTADO | VARCHAR2 | permite nulo |  | tamanho 2 |
| CIDADE | VARCHAR2 | permite nulo |  | tamanho 15 |
| ENDERECO | VARCHAR2 | permite nulo |  | tamanho 40 |
| SENHA | VARCHAR2 | permite nulo |  | tamanho 10 |
| CODCLIRCA | VARCHAR2 | permite nulo |  | tamanho 50 |
| PERMITEPRODSEMDISTRIBUICAO | VARCHAR2 | permite nulo |  | tamanho 1 |

## TABLE_NAME

| Campo | Tipo | Obrigatório/Nulo | Chave | Detalhes |
| --- | --- | --- | --- | --- |
| COLUMN_NAME | DATA_TYPE | NULLABLE |  | tamanho DATA_LENGTH, precis?o DATA_PRECISION, escala DATA_SCALE |

---

## Lista auxiliar de tabelas do aplicativo

### TABELAS APLICATIVO

### MXMD_AGENDAMENTO
### MXMD_AJUDANTES
### MXMD_AUSENCIA
### MXMD_CARREGAMENTOS
### MXMD_CLIENTES
### MXMD_COB_PREVISTAS
### MXMD_CONTROLE_SINC
### MXMD_DESCANSO_JORNADA
### MXMD_DESCARGA_CANCELADA
### MXMD_DESCARGA_REAGENDADA
### MXMD_DESPESAS
### MXMD_ENTREGAS
### MXMD_EVENTOS
### MXMD_EVENTO_ENTREGA
### MXMD_FILIAIS
### MXMD_FOTOS
### MXMD_HISTORICO_OCORRENCIA
### MXMD_HIST_ACEITE_FRETE
### MXMD_HODOMETROS
### MXMD_INFO_TRANSBORDO
### MXMD_INTRAJORNADA
### MXMD_ITEM_COMODATO
### MXMD_ITEM_OCORRENCIA
### MXMD_ITENS_NOTA_FISCAL
### MXMD_JANELA_ENTREGA
### MXMD_LANCAMENTOS_JORNADA
### MXMD_LANC_COMODATO
### MXMD_LOCALIZACAO
### MXMD_LOG_CONEXAO
### MXMD_MARKER_ROMANEIO
### MXMD_MOTIVO_CANCELAMENTO
### MXMD_MOTIVO_DE_CANHOTO
### MXMD_MOTIVO_FURO_SEQUENCIA
### MXMD_MOTIVO_OCORRENCIA
### MXMD_MOTIVO_REAGENDAMENTO
### MXMD_MOTORISTAS_PREPOSTOS
### MXMD_NOTAS_FISCAIS
### MXMD_NOTA_REENTREGA
### MXMD_OCORRENCIAS
### MXMD_PARCELAMENTO
### MXMD_POLYLINE
### MXMD_PONTO_PARADA
### MXMD_PRODUTOS
### MXMD_PRODUTOS_VOLUMES_ENTREGAS
### MXMD_RASTRO
### MXMD_RCA
### MXMD_ROMANEIO
### MXMD_SUPERVISORES
### MXMD_TEMPO_SEMANA
### MXMD_TIPO_DESPESA
### MXMD_TIPO_EVENTO
### MXMD_TITULOS
### MXMD_TOUR
### MXMD_VOLUMES
### MXMD_VOLUMES_CONF_ENT
### MXMD_VOLUMES_ENTREGAS
### MXMD_VOLUMES_ENT_CONF_TEMP
### MXMI_COBRANCAS
### MXMI_CONTATOS
### MXMI_MOTIVOS_DEVOLUCAO
### MXMP_CONTATOS
### MXMP_ENDERECO_ENTREGAS
### MXMP_ITEM_SOLICITACAO
### MXMP_NOTIFICACAO_PORTAL
### MXMP_PARAMETROS
### MXMP_RECEBIVEIS
### MXMP_SOLICITACOES
### MXMP_USUARIOS
android_metadata

### TABELAS INTEGRAÇÃO

MXSATIVI
MXSCIDADE
MXSCLIENT
MXSCLIENTENDENT
MXSULTCOMPCLIENTE
MXSCOB
MXSCONTATO
MXSEMPR
MXSFILIAL
MXSHISTORICOPEDC
MXSHISTORICOPEDI
MXSHISTORICOPEDCORTE
MXSHISTORICOPEDFALTA
MXSDOCELETRONICO
MXSNFSAID
ERP_MXSMOV
MXSPLPAG
MXSPRACA
ERP_MXSPREST
MXSPRODUT
MXSREGIAO
MXSROTAEXP
MXSSUPERV
MXSCARREG
MXSUSUARI
ERP_MXSVEICUL

### TABELAS WEB MOTORISTA/ROTEIRIZADOR

### MXMP_AGENDA_DINAMICA
### MXMP_AGENDAMENTO
### MXMP_AJUDANTE_COMPLEMENTO
### MXMP_AJUDANTE_CUSTO_FRETE
### MXMP_APARELHOS
### MXMP_APK
### MXMP_AREAS_ATENDIMENTO
### MXMP_AREAS_ATENDIMENTO_DIA
### MXMP_AREAS_ATENDIMENTO_FILIAL
### MXMP_AREAS_ATENDIMENTO_POLYLINE
### MXMP_AREAS_ATENDIMENTO_VEICULO
### MXMP_ARQUIVOS
### MXMP_AUSENCIA
### MXMP_BAIXA_CARREGAMENTO
### MXMP_BANCO_LOGISTICA
### MXMP_BASE_CALC_INFRACAO
### MXMP_BASE_CARREGAMENTO
### MXMP_BASE_OCORRENCIAS
### MXMP_CAD_SEFAZ
### MXMP_CANCELAMENTO_CHECKIN
### MXMP_CARACTERISTICAS_COMPLEMENTO
### MXMP_CARACTERISTICAS_FILIAIS
### MXMP_CARACTERISTICAS_VEICULO
### MXMP_CARACTERISTICAS_VEICULO_FILIAL
### MXMP_CARREGAMENTO_CROSSDOCKING
### MXMP_CARREGAMENTO_LOG
### MXMP_CARREGAMENTO_TEMPORARIO
### MXMP_CARREGAMENTO_TRANSBORDO
### MXMP_CARREG_ENTREGA_INATIVO
### MXMP_CARTEIRIZACAO
### MXMP_CATEGORIA_PECAS_INSUMOS
### MXMP_CATEGORIA_SERVICO
### MXMP_CD_USUARIO
### MXMP_CENTROS_DISTRIBUICAO
### MXMP_CERT_DIGITAL
### MXMP_CIDADE_TABELA_FRETE
### MXMP_CLIENTE_CENTRO_DISTRIBUICAO
### MXMP_CLIENTE_COMPLEMENTO
### MXMP_COD_END_FRETE_TRANSP_PED
### MXMP_CODIGO_INFRACAO
### MXMP_CODIGO_RASTREIO_PEDIDO
### MXMP_COMBUSTIVEL
### MXMP_COMPLEMENTO_ROTA
### MXMP_CONEXOES
### MXMP_CONFIG_EXIBICAO_CAMPOS
### MXMP_CONFIG_EXIBICAO_CAMPOS_ITEM
### MXMP_CONFIG_FILTRO_CORES
### MXMP_CONFIG_MAXENTREGAS
### MXMP_CONFIGURACAO_EMAIL
### MXMP_CONFIGURACAO_ROTEIRIZACAO
### MXMP_CONFIGURACAO_VISITAS_RCA
### MXMP_CONFIG_VISAO_USUARIO
### MXMP_CONTATOS
### MXMP_CONTROLE_EMAIL_ENTREGA
### MXMP_CONTROLE_NOTA
### MXMP_CONTROLE_SINC_MOTORISTA
### MXMP_CORES
### MXMP_COTACAO_FORNECEDORES
### MXMP_CUSTO_CARREGAMENTO
### MXMP_CUSTO_CIDADE_FRETE
### MXMP_CUSTO_ENTREGA
### MXMP_CUSTO_FAIXA_FRETE
### MXMP_CUSTO_MONTAGEM
### MXMP_CUSTO_ROMANEIO
### MXMP_CUSTO_ROMANEIO_FRETE
### MXMP_CUSTO_ROMANEIO_TERCEIRIZADO
### MXMP_DADOS_ENTREGA_NOTA
### MXMP_DADOS_PERFIL
### MXMP_DADOS_USUARIO
### MXMP_DESCANSO_JORNADA
### MXMP_DESCARGA_CANCELADA
### MXMP_DESCARGA_REAGENDADA
### MXMP_DESPESA_ABASTECIMENTO
### MXMP_DESPESA_INFRACAO
### MXMP_DESPESAS
### MXMP_DEVOLUCOES
### MXMP_DIA_MONTAGEM
### MXMP_DIA_MONTAGEM_CARGA_CLIENTE
### MXMP_DIAS_ENT_CIDADE_EMITENTE
### MXMP_DISPOSICAO_GRID_PEDIDOS
### MXMP_ENDERECO_ENTREGAS
### MXMP_ENDERECO_HIERARQUIA
### MXMP_ENTREGAS
### MXMP_EVENTOS
### MXMP_FAIXA_TABELA_FRETE
### MXMP_FAIXA_TRANSPORTADORA
### MXMP_FALHA_GEOCODE
### MXMP_FALHA_SINCRONIZACAO
### MXMP_FILA_GEOCODE
### MXMP_FILA_MENSAGEM
### MXMP_FILA_ROTEIRIZACAO
### MXMP_FILA_VERI_SEFAZ
### MXMP_FILIAIS_VEICULOS
### MXMP_FILIAL_COTACAO_FORNECEDORES
### MXMP_FILIAL_PLANO_MANUTENCAO
### MXMP_FILIAL_ROTA_COMP
### MXMP_FILIAL_TABELA_FRETE
### MXMP_FILIAL_VISAO_GERENCIAL
### MXMP_FOTOS
### MXMP_GRUPO_RAMO_ATIVIDADE
### MXMP_HIERARQUIA_ENTREGA
### MXMP_HIST_ACEITE_FRETE
### MXMP_HISTORICO_CARREGAMENTO
### MXMP_HISTORICO_ENTREGAS
### MXMP_HISTORICO_OCORRENCIA
### MXMP_HISTORICO_TANQUE_COMBUSTIVEL
### MXMP_HIST_REENTREGA_CARREGAMENTO
### MXMP_HODOMETROS
### MXMP_HORARIOS_TRABALHO
### MXMP_HORARIOS_TRABALHO_ITENS
### MXMP_IDENTIFICACAO_PERSONALIZADA_ENTREGA
### MXMP_INFO_CROSSDOCKING
### MXMP_INFO_TRANSBORDO
### MXMP_ITEM_COTACAO_FORNECEDORES
### MXMP_ITEM_MANUTENCAO
### MXMP_ITEM_OCORRENCIA
### MXMP_ITEM_PLANO_MANUTENCAO
### MXMP_ITEM_SOLICITACAO
### MXMP_ITENS_COMODATOS
### MXMP_JANELA_ENTREGA
### MXMP_JORNADAS
### MXMP_LANCAMENTOS_JORNADA
### MXMP_LANC_COMODATO
### MXMP_LINK
### MXMP_LOCALIZACAO_CLIENTE
### MXMP_LOCALIZACAO_CLIENTE_VENDA
### MXMP_LOCALIZACAO_END_ENTREGA
### MXMP_LOCALIZACAO_MOTORISTA
### MXMP_LOCALIZACAO_RCA
### MXMP_LOG_ALTER_ARQUIVO
### MXMP_LOG_BAIXA_TITULO_SINC
### MXMP_LOG_DIST_AUTO
### MXMP_LOG_ERP_MXSCARREG
### MXMP_LOG_ERROS
### MXMP_LOG_MONTAGEM_AUTOMATICA
### MXMP_LOG_MOTORISTA_PREPOSTO
### MXMP_LOG_NUMSEQ_NFSAID
### MXMP_LOGO_EMPRESA
### MXMP_LOG_OPERACOES_ROMANEIO_ERP
### MXMP_LOG_OP_LOGISTICA
### MXMP_LOG_REGISTRO_JORNADA
### MXMP_LOG_SITUACAO_ENTREGA_NOTA
### MXMP_LOG_TRANSF
### MXMP_MANUTENCAO
### MXMP_MARCA_PECAS_INSUMOS
### MXMP_MAXPAG_COB
### MXMP_MAXPAG_LINK
### MXMP_MAXPAG_MOV
### MXMP_MAXPAG_TOKEN
### MXMP_MOTIVO_CANCELAMENTO
### MXMP_MOTIVO_DE_CANHOTO
### MXMP_MOTIVO_FURO_SEQUENCIA
### MXMP_MOTIVO_OCORRENCIA
### MXMP_MOTIVO_REAGENDAMENTO
### MXMP_MOTIVO_TRANSF
### MXMP_MOTORISTA_COMPLEMENTO
### MXMP_MOTORISTA_OMNILINK
### MXMP_MOTORISTAS_PREF_ROTA
### MXMP_MOTORISTAS_PREPOSTOS
### MXMP_NOTA_REENTREGA
### MXMP_NOTAS_FISCAIS
### MXMP_NOTIFICACAO
### MXMP_NOTIFICACAO_CARREGAMENTO
### MXMP_NOTIFICACAO_PORTAL
### MXMP_NOTIFICACAO_ROTEIRIZADOR
### MXMP_OCOREN
### MXMP_OCOREN_ARQUIVO
### MXMP_OCOREN_CODIGO_OCORRENCIA
### MXMP_OCOREN_ENTREGA
### MXMP_OCOREN_OCORRENCIA
### MXMP_OCOREN_TRANSPORTADORA
### MXMP_OCORRENCIAS
### MXMP_OPERADORA_VALE_PEDAGIO
### MXMP_PALAVRA_CHAVE
### MXMP_PARAMETROS
### MXMP_PARAMETROS_CALCULO
### MXMP_PARAMETROS_FILIAL
### MXMP_PARAMETROS_OMNILINK
### MXMP_PARAMETROS_RESTRICAO
### MXMP_PARAMETROS_USUARIO
### MXMP_PECAS_INSUMOS
### MXMP_PEDIDO_CROSSDOCKING
### MXMP_PERFIL
### MXMP_PERFIL_ACESSO
### MXMP_PERFIL_ACESSO_PERMISSAO
### MXMP_PERFIL_ROTEIRIZACAO
### MXMP_PERMISSAO
### MXMP_PERMISSOES
### MXMP_PERMISSOES_PERFIL
### MXMP_PERMISSOES_USUARIO
### MXMP_PLANEJAMENTO_VISITAS_RCA
### MXMP_PLANO_CONTA
### MXMP_PLANO_GRUPO
### MXMP_PLANO_MANUTENCAO
### MXMP_PONTO_PARADA
### MXMP_PONTO_PARADA_ROMANEIO
### MXMP_PONTOS_REFERENCIA
### MXMP_POSICAO_TATICO_OPERACIONAL
### MXMP_PRACA_TABELA_FRETE
### MXMP_PRACA_VISAO_GERENCIAL
### MXMP_PRE_ACERTO_MOTORISTA
### MXMP_PROBLEM_JSON
### MXMP_RAKING_MOTORISTA
### MXMP_RAMO_ATIVIDADE
### MXMP_RAMO_ATIVIDADE_COMPLEMENTO
### MXMP_RASTREADOR
### MXMP_RECEBIVEIS
### MXMP_REGIAO
### MXMP_REGIAO_CLIENTE
### MXMP_REGIOES
### MXMP_REGIOES_ATENDIMENTO
### MXMP_REGIOES_ATENDIMENTO_CIDADE
### MXMP_REGIOES_ATENDIMENTO_PRACA
### MXMP_REGIOES_ATENDIMENTO_ROTA
### MXMP_REGIOES_CIDADES
### MXMP_REGIOES_ENTREGA
### MXMP_REGIOES_ENTREGA_ROTAS
### MXMP_REGISTRO_PONTO_PARADA
### MXMP_REJEICAO_ROTA_AUTO
### MXMP_REPROCESSAR_ROMANEIO_CD
### MXMP_RESPONSAVEL_MOTORISTA
### MXMP_RODIZIO_DIA_SEMANA
### MXMP_RODIZIO_FINAL_PLACA
### MXMP_RODIZIO_ROTA
### MXMP_ROMANEIO
### MXMP_ROTA_COMPLEMENTO
### MXMP_ROTA_MONTAGEM_COMPLEMENTO
### MXMP_ROTA_ROMANEIO
### MXMP_ROTA_SEQUENCIA
### MXMP_ROTA_SEQUENCIA_BKP
### MXMP_ROTAS_TRANSPORTADORA
### MXMP_ROTA_TABELA_FRETE
### MXMP_ROTA_VISAO_GERENCIAL
### MXMP_ROTEIRIZACAO
### MXMP_ROTEIRIZACAO_DIA_SEMANA
### MXMP_ROTEIRIZACAO_LOG_RCA
### MXMP_ROTEIRIZACAO_PEDIDO
### MXMP_ROTEIRIZACAO_RCA
### MXMP_ROTEIRIZACAO_RCA_SEQ
### MXMP_ROTEIRIZADOR_CONFIG
### MXMP_SEGMENTO
### MXMP_SEGMENTO_CLIENTE
### MXMP_SEM_PARAR_PRACA_PEDAGIO
### MXMP_SEQUENCIA_DINAMICA
### MXMP_SERVICO_GEOCODIFICACAO
### MXMP_SERVICO_ROTEIRIZACAO
### MXMP_SLA_CLIENTE
### MXMP_SLA_REDE
### MXMP_SLA_REGIAO
### MXMP_SOLICITACOES
### MXMP_SOLUCAO
### MXMP_SOLUCAO_ROTEIRIZACAO
### MXMP_SUB_PERMISSOES
### MXMP_SUB_PERMISSOES_PERFIL
### MXMP_TABELA_FRETE
### MXMP_TAEMROTA_RESTRICAO_CODCOB
### MXMP_TAEMROTA_RESTRICAO_ORIGEM_PEDIDO
### MXMP_TANQUE_COMBUSTIVEL
### MXMP_TEMP_CARREG_KMINICIAL
### MXMP_TEMPLATE_WHATSAPP
### MXMP_TEMP_LOG_PEDC_NUMSEQENTREGA
### MXMP_TEMPO_CLIENTE
### MXMP_TEMPO_MEDIO_ATIVIDADE
### MXMP_TESTE
### MXMP_TIME_LINE
### MXMP_TIPO_AUSENCIA
### MXMP_TIPO_CARGA
### MXMP_TIPO_DESPESA
### MXMP_TIPO_EVENTO
### MXMP_TIPO_JUSTIFICATIVA
### MXMP_TIPO_NOTIFICACAO_CARREGAMENTO
### MXMP_TIPOS_DEVOLUCAO
### MXMP_TIPO_SERVICO
### MXMP_TIPO_TEMPLATE_WHATSAPP
### MXMP_TIPO_VEICULO
### MXMP_TIPO_VENDA_TABELA_FRETE
### MXMP_TOKEN_VALIDACAO
### MXMP_TOUR
### MXMP_TOUR_USUARIO
### MXMP_TRANSPORTADORA
### MXMP_USUARIO_PERFIL_ACESSO
### MXMP_USUARIOS
### MXMP_USUARIOS_ACESSO
### MXMP_USUARIOS_FILIAIS
### MXMP_USUARIOS_ROTAS
### MXMP_USUARIO_VISAO_GERENCIAL
### MXMP_VEICULO_COMPLEMENTO
### MXMP_VEICULO_COTACAO_FORNECEDORES
### MXMP_VEICULO_INDISPONIBILIDADE
### MXMP_VEICULO_RASTREADOR
### MXMP_VEICULOS_PREF_ROTA
### MXMP_VERSAO_LOGISTICA
### MXMP_VISAO_GERENCIAL
### MXMP_VOLUMES_CONF_ENT
