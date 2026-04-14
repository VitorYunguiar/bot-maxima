# GATE-460 - Compromissos não descem para a base do RCA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: Dúvida
- Atualizado em: 2024-12-05T17:09:21.854-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base zerada do vendedor, ir na aba 'Clientes' e selecionar a opção 'Roteiro' ou 'Roteiro hoje'

## Resultado apresentado
É verificado que o roteiro não é apresentado.

## Resultado esperado
É esperado que o roteiro seja apresentado para o vendedor.

## Descrição
Cliente relata que os roteiros do usuário codusur 3481 não estão sendo apresentados no aplicativo. Foi realizada a atualização de todo o ambiente do cliente e simulação em base zero, onde ao consultar a tabela MXSCOMPROMISSOS via inspect foi verificado que não constava nenhum registro, indicando que os dados não foram baixados do banco nuvem ao subir a base.
Foi realizada comparação dos registros da ERP_MXSROTACLI com a MXSCOMPROMISSOS no banco nuvem e observado que os registros do dia 05/12 em diante na MXSCOMPROMISSOS constavam com o CODOPERACAO = 2. Foi realizado o update nos registros acima do dia 05/12 e tentativa de subir a base novamente, onde os registros continuaram a não serem enviados para a base.

Login para teste:
refil.juliano

O cliente é Winthor e a situação ocorre também com o usuário refil.bento.

## Comentarios do Gatekeeper

### 1. 2024-12-05T16:37:02.710-0300 | Filipe do Amaral Padilha

O RCA que utilizamos como cenário foi o REFIL.juliano cujo CODUSUR é o 3481;

Ele possui rota cadastrar na ERP_MXSROTACLI para os clientes: (106917, 79299, 109903, 113916, 127567, 128772, 129278, 134842, 131826, 71451)

Nenhum desses clientes está na carteira do RCA 3481, por isso, a job roda e não gera os compromissos como ativos para o RCA na MXSCOMRPOMISSOS.

Para conferir que os clientes não estão na carteira:
SELECT CODCLI, CODUSUR1, CODUSUR2, CODUSUR3 FROM MXSCLIENT WHERE CODCLI IN(106917, 79299, 109903, 113916, 127567, 128772, 129278, 134842, 131826, 71451);
SELECT * FROM ERP_MXSUSURCLI WHERE CODCLI IN(106917, 79299, 109903, 113916, 127567, 128772, 129278, 134842, 131826, 71451) AND CODUSUR IN(3481);

Então para resolver e gerar os compromissos é obrigatório que os clientes sejam da carteira do RCA.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410624
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que "o roteiro não é apresentado no aplicativo" não está explicitamente no texto-fonte. | A recomendação de "Ajustar a carteira do RCA para incluir esses clientes" é uma inferência operacional; o texto-fonte apenas diz que é obrigatório que os clientes sejam da carteira do RCA para gerar os compromissos. | A recomendação de "Após o ajuste, gerar novamente os compromissos para que o roteiro passe a ser apresentado" não está explicitamente no texto-fonte, especialmente a parte sobre o roteiro ser apresentado.
