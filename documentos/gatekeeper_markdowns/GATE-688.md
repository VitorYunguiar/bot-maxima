# GATE-688 - [BACKEND] Documentos de apoio deletados na central de configurações não são excluidos na nuvem

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXPED - Central de Configurações
- Natureza: Dúvida
- Atualizado em: 2025-01-24T12:01:33.116-0300

## Contexto do Problema

## Passos para reproduzir
Boa tarde Filipe,

Gostaria que fosse verificado se há um erro no fluxo dos cadastros de documento de apoio, visto que foi cadastrado o documento de apoio 101 anteriormente, que foi deletado porém continua com CODOPERACAO = 1 na MXSALERTARESTRICOES, impedindo que um determinado cliente seja cadastrado em outro documento de apoio.

>>Acessar Central de Configurações da GSA
>Extras -> Documento de Apoio
>Criar novo documento de apoio
>Selecionar todos os ramos de atividade
>Selecionar região "SEM TABELA VINCULADA"
>Selecionar o cliente 17484 - RB AGUIAR
>Salvar

SELECT CODOPERACAO, MXSALERTACLIENTE.* FROM MXSALERTACLIENTE WHERE CODIGO = 101;

SELECT * FROM MXSALERTARESTRICOES WHERE CODIGO = 101 AND ID_REGISTRO = '17484';

## Resultado apresentado
Ao salvar é exibido um pop-up informando que o cadastro não pode ser salvo por que o cliente está vinculado ao documento de apoio 101, porém esse documento já foi deletado.

Na MXSALERTARESTRICOES foi alterado apenas a coluna ENVIAFV para N, o CODOPERACAO continua sendo 1.

## Resultado esperado
Que ao deletar o cadastro na central de configurações ele também seja deletado no banco nuvem.

## Comentarios do Gatekeeper

### 1. 2025-01-24T12:01:33.114-0300 | Filipe do Amaral Padilha

Foi verificado que o problema de exclusão já foi solucionado, ou seja, quando o cabeçalho do documento é excluído as restrições também devem ser excluídas.

Porém haviam registros retroativos com problemas. Porque na versão antiga, não ocorria exclusão conforme regra citada.

Para resolver o cenário foi feita normalização dos registros, agora todos os cabeçalhos excluídos possuem restrições excluídas e foi feito teste e de fato está excluindo

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, grounding_failed, needs_review
- Comentarios primarios: 418911
- Secoes ausentes: Descrição
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "documento de apoio" — o texto-fonte menciona apenas "cabeçalho do documento", sem especificar "documento de apoio". | "Pela análise realizada" — o texto-fonte não descreve uma análise, apenas relata verificações e ações executadas. | "o comportamento reportado está associado a inconsistências retroativas de versões anteriores, e não à regra atual de exclusão" — a primeira parte é suportada, mas a formulação "comportamento reportado" e a conclusão comparativa "e não à regra atual" não aparecem explicitamente no texto-fonte. | "Ação recomendada:" e os itens subsequentes — o texto-fonte não traz recomendações, apenas descreve o que foi feito. | "validar em ambiente se novos casos de exclusão continuam removendo também as restrições" — recomendação não presente no texto-fonte. | "confirmar que os registros retroativos afetados foram normalizados" — recomendação não presente no texto-fonte. | "Limitações da análise:" e os itens subsequentes — o texto-fonte não apresenta seção de limitações nem discute ausência de informações. | "não foi informado o responsável pela correção" — ausência de informação inferida, não afirmada pelo texto-fonte. | "não foram detalhados quais registros retroativos foram normalizados" — ausência de informação inferida, não afirmada pelo texto-fonte. | "não foram apresentados parâmetros ou SQL da correção" — ausência de informação inferida, não afirmada pelo texto-fonte.
