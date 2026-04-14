# GATE-148 - Roteiro não gera na MXSCOMPROMISSOS

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: Dúvida
- Atualizado em: 2024-10-04T16:13:31.761-0300

## Contexto do Problema

## Passos para reproduzir
>>dztm.ce3844
>Acessar APK
>Clientes
>Roteiro

--- BANCO NUVEM ---

SELECT * FROM MXSCOMPROMISSOS WHERE CODUSUARIO = 101402;

SELECT * FROM ERP_MXSROTACLI WHERE CODUSUR = 3844 ORDER BY DTPROXVISITA DESC;

## Resultado apresentado
Roteiro não é gerado na MXSCOMPROMISSOS

## Resultado esperado
Gerar os roteiros.

## Descrição
Cliente é OERPs, o registro foi enviado para a ERP_MXSROTACLI e parece estar enviado corretamente, porém o roteiro não é gerado na MXSCOMPROMISSOS, tentei atualizar o banco nuvem porém não adiantou.

## Comentarios do Gatekeeper

### 1. 2024-10-04T16:13:25.641-0300 | Filipe do Amaral Padilha

Estava com problema para gerar os compromissos no banco nuvem, foi corrigido com a atualização, assim que você atualizou e a job de compromissos rodou, foi gerada a agenda normalmente, para verificar você pode conferir sincronizando o maxPedido.

Ou também consultando no {color:#cccccc}{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCOMPROMISSOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} = {color:#c0c0c0}101402{color}{color:#eecc64};{color}{color}

atualizado --3.1.3.353

--2024-10-04 15:52:43.000

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 399072
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "O roteiro havia sido enviado para a base de origem" — o texto-fonte não menciona roteiro nem base de origem. | "A validação deve ser feita consultando diretamente a tabela de compromissos para o usuário informado" — o texto-fonte diz que pode ser verificado sincronizando o maxPedido ou consultando a tabela; não estabelece que deve ser feita diretamente pela consulta. | "Verificar se a agenda foi gerada após a sincronização do maxPedido ou pela consulta direta na MXSCOMPROMISSOS" — a formulação 'após a sincronização' não está explicitamente dita; o texto apenas sugere conferir sincronizando o maxPedido ou consultando a tabela.
