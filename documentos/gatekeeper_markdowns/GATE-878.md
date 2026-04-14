# GATE-878 - Permissões do usuário 5600

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Mariel Araujo Souza
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatórios
- Natureza: Dúvida
- Atualizado em: 2025-03-05T08:33:34.948-0300

## Contexto do Problema

## Passos para reproduzir
Entrar no gestão com o usuario: rbcomercio.5600 e senha: qwe123
1-Ir na opção RELATORIOS
2-Vai abrir o PWA
3-Ir em relatorios
4-Abrir outra aba com relatorios do GESTÃO
5-Ir em VENDAS-----RESUMO DE DEVOLUÇÃO
Selecionar:
Filial=2
Data: inicio do mês até a data atual
Pesquisar

## Resultado apresentado
Apresenta o relatorio do supervisor de codigo 56 e 57, onde 56 é a permissão que o supervisor tem em seu cadastro no Gestão.

## Resultado esperado
Mostra-se apenas dados do supervisor 56

## Descrição
Verificado o supervisor de codigo 5600, onde o mesmo no gestão tem apenas acesso ao seu código no seu usuário, porem ao consultar os relatórios de devolução esta apresentando os dados do supervisor 5600 e 5700, onde o mesmo não tem aceso ao supervisor 57 e sim acesso somente ao supervisor 56.

## Comentarios do Gatekeeper

### 1. 2025-03-05T08:01:53.021-0300 | Filipe do Amaral Padilha

Será encaminhado para N3, durante a análise observei que pode ser um problema da VIEW que é utilizada para apurar os dados nesse relatório ou também de registros divergentes entre nuvem e local

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 427589
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta especifica que o problema é na 'VIEW utilizada para apuração dos dados do relatório de devolução', mas o texto-fonte menciona apenas 'nesse relatório', sem identificar que é de devolução. | A resposta afirma que 'No momento, a causa raiz não está confirmada; tratam-se de hipóteses técnicas observadas na análise', o que é uma interpretação plausível, mas não está explicitamente declarado no texto-fonte. | A resposta diz que o N3 é 'responsável por aprofundar a investigação na VIEW do relatório e na possível divergência de registros entre nuvem e local', mas o texto-fonte apenas informa que será encaminhado para N3, sem detalhar essa responsabilidade.
