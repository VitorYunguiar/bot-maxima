# GATE-898 - Pedidos do dia 28/02/2025 não aparece no palm

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Mariel Araujo Souza
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Histórico
- Natureza: Dúvida
- Atualizado em: 2025-03-05T14:53:53.911-0300

## Contexto do Problema

## Passos para reproduzir
1-Entrar com o usuario gigavale.guilherme
2-Importar a base que segue em anexo
3-Consultar os pedido feitos do dia 28/02/2025

## Resultado apresentado
Na importação da base no meu aparelho mostrar todos os pedidos, porém no aparelho dele não mostra.

## Resultado esperado
Mostra-se os pedido do dia 28 no aparelho do vendedor.

## Descrição
Analisado com o vendedor no dia 28/02/2025 e verificando todos os filtros, os pedidos do dia 28 não aparece no palm do mesmo, porém ao importar a base do vendedor em meu aparelho, aparece todos os pedidos feito nesse dia. Fiz o teste na ponta e tambem na versão do vendedor ou outro teste em outra versão, na V3 ainda e com ele continua sem aparecer os pedidos e no meu equipamento aparece.

## Comentarios do Gatekeeper

### 1. 2025-03-05T14:53:53.909-0300 | Filipe do Amaral Padilha

Ao acessar a base do RCA, conforme descrito, realmente não há problemas na exibição dos pedidos, eles constam na base do RCA e portanto ao filtrar corretamente na timeline são exibidos sem problemas.

Nesse contexto, para ser um problema, ele precisa ser simulável. No vídeo que o cliente colocou no ticket principal, dá para observar que o RCA estava usando de filtros na timeline de pedidos aba (Pedidos), onde ele estava filtrando para mostrar somente Orçamentos, então pode estar ocorrendo uma dificuldade de uso do aplicativo, mas não há evidências de aparentes problemas.

Nesse caso eu recomendo os seguintes procedimentos:
1° Limpar os filtros da Timeline de Pedidos. Apesar de a limpeza resolver 95% dos casos, pode ter um caso de o filtro não ter sido limpo completamente por causa de algum problema de versão, então recomendo revisar todos os filtros referentes a datas e os tipos de pedidos que estão sendo apresentados. A maiora dos casos de problema de pedido que não aparece simplesmente é o usuário realizando filtros que depois não altera mais (Data Prevista Faturamento) são os casos mais comuns.

2° Reestruturar o banco do aplicativo em Ferramentas -> Reestruturar Banco

3° Se o usuário apagou os pedidos (o que é uma possibilidade em alguns casos) ele pode restaurar a timeline usando o parâmetro PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO = S.
Depois de ativo ao sincronizar busca e restaura o histórico de pedidos na timeline.

4° Atualizar a versão do maxPedido e limpar os filtros.

5° Se o problema persistir será necessário o cliente fornecer um cenário consolidado, com vídeo e a base problemática do RCA. Em último caso dá para fazer uma conexão remota no aparelho do RCA para identificar a real causa dos pedidos não estarem sendo exibidos

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 427786
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "o que caracteriza como causa mais provável uma dificuldade de uso relacionada aos filtros da timeline, e não um defeito de exibição" — o texto-fonte diz que "pode estar ocorrendo uma dificuldade de uso do aplicativo, mas não há evidências de aparentes problemas"; afirmar "causa mais provável" extrapola o suporte literal. | "repetir o teste com os filtros limpos" — essa ação não aparece explicitamente no texto-fonte. | "Responsável pela validação em campo: Cliente/usuário RCA." — não há qualquer menção a responsável pela validação em campo no texto-fonte.
