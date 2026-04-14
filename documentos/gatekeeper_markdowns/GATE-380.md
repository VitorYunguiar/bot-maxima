# GATE-380 - divergencias em registro de positivação

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Dados Incorretos
- Natureza: Dúvida
- Atualizado em: 2024-11-25T17:01:08.398-0300

## Contexto do Problema

## Passos para reproduzir
realiza o filtro no painel de auditoria para o vendedor do exemplo para o dia 18/11/2024 e observar os resultados

## Resultado apresentado
estão sendo apresentados alguns valores de positivação que aparentemente estão inadequados.

## Resultado esperado
é esperado que os valores de positivação considerem cada cliente de forma unica, indiferente a quantidade de pedidos/visitas que tenham sido realizadas em um determinado dia.

## Descrição
Senhores, ao analisarmos a situação relatada pela cliente, estamos observando que os registros de positivação no painel de auditoria, está apresentando alguns valores que não condizem com a realidade do que é o conceito de positivação. No cenário de exemplo, estamos identificando que:

primeiramente, o numero de positivações tanto dentro de rota quanto fora de rota, apresentam valores que estão acima da quantidade de visitados, ou seja, o sistema está dando a entender que há positivação de clientes maior que a própria quantidade de visitas realizadas e isso é inviável de acontecer, uma vez que  para uma positivação acontecer, depende diretamente de uma visita:

!https://cdn.discordapp.com/attachments/1009929379322806302/1310598772958429194/image.png?ex=6745cdb9&is=67447c39&hm=3ed83f51fc80fd65011de2a9dca163370b8bbc69d7fcc1e6ccd7cd559eb71e29&=!

A seguir, ao analisarmos de forma analítica o que há para o RCA, observa-se que o numero de positivações é equivalente ao numero de pedidos realizados pelo RCA para os clientes dentro de rota, onde está sendo contabilizado um pedido que foi salvo e bloqueado pelo RCA em seu aparelho. Essa situação leva a crer que cada pedido enviado está gerando um registro de positivação, o que não apresenta o cenário real do numero de clientes positivados:

!https://cdn.discordapp.com/attachments/1009929379322806302/1310597290456649729/image.png?ex=6745cc57&is=67447ad7&hm=05e20dc4b3227d31d4074aa7fd626d140db280ea53876527408a36315ab61932&=!

Não identificamos parametrizações extras do gestão possam levar a algum comportamento que seja diferente do esperado:

!image-2024-11-25-11-08-37-820.png!

## Comentarios do Gatekeeper

### 1. 2024-11-25T16:40:37.485-0300 | Filipe do Amaral Padilha

Enviado para N3 para investigar a questão da positivação sendo contabilizada mais de uma vez no mesmo cliente e também dos rastros de pedidos que não estão sendo exibidos corretamente no Painel de Auditoria, inclusive, um problema pode estar ligado ao outro.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 408526
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificamos" dois comportamentos no Painel de Auditoria que precisam ser tratados em conjunto. | "O comportamento reportado não está aderente ao conceito esperado de positivação por cliente único". | "há evidência de duplicidade de contabilização no mesmo cliente". | "a exibição incorreta dos rastros de pedidos pode estar influenciando ou refletindo essa inconsistência no painel". | "Responsável: N3". | "O N3 deve" investigar a duplicidade, a falha na exibição e validar a relação entre os dois comportamentos.
