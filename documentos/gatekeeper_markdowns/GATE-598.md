# GATE-598 - RCA não retorna na busca da jornada de trabalho.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Jornada de Trabalho
- Natureza: Dúvida
- Atualizado em: 2025-01-08T12:53:24.299-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar maxGestão;
>> Jornada de trabalho, Cadastro de Jornada;
>> Editar jornada "JORNADA PADRÂO";
>> Buscar RCA na listagem de usuários disponiveis para vinculo.

## Resultado apresentado
RCA não aparece na listagem de usuários do maxGestão, porem aparece no maxPedido.

## Resultado esperado
RCA sendo apresentado na listagem de usuários disponiveis para vinculo do maxGestão.

## Descrição
Ao tentar buscar um RCA para vincular a jornada de trabalho o RCA não é listado na busca do maxGestão.

Porem na busca do maxPedido ele é retornado e é possivel vincular o RCA a jornada.

Se o vinculo for realizado pelo maxPedido o RCA é apresentado na listagem de usuários vinculados do maxGestão normalmente e é possivel até remover ele da jornada pelo maxGestão, porem nunca é exibido na listagem de disponiveis para vinculo.

Testado no usuários sysmax e usuário do cliente, ambos com todas as permissões marcadas.

68361 - DOUGLAS RODIGUES GARCIA - 947

## Comentarios do Gatekeeper

### 1. 2025-01-08T12:53:24.298-0300 | Filipe do Amaral Padilha

Será encaminhado para N3.

Eu identifiquei o seguinte comportamento errado:
Se o usuário esperar a lista toda carregar e diretamente pesquisar o número correto desejado, seja 947 ou 68361, então a busca retorna o RCA. Porém se ele digitar errado ou o código de outro RCA primeiro: 570 (por exemplo) e depois tentar digitar 947, a busca não reinicia, por isso não retorna o usuário desejado.
--
Sobre o campo (Nome), ele busca pelo nome do login do usuário não pelo nome do usuário, se você colocar "DOUGLAS" nada retorna mesmo e isso está correto, no caso ele busca correto só se você esperar a lista carregar e depois escrever "HIMALAIA.947"

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 415652
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificada limitação na busca de usuários disponíveis para vínculo no maxGestão." — o texto-fonte não menciona "maxGestão" nem "usuários disponíveis para vínculo". | "A análise mostrou que o RCA não deixa de existir na listagem" — o texto-fonte não afirma isso explicitamente. | "Ação recomendada" com orientações como "aguardar a lista carregar totalmente antes de pesquisar", "pesquisar diretamente pelo número correto do RCA" e "no campo Nome, utilizar o login do usuário" — o texto-fonte descreve o comportamento observado, mas não apresenta essas orientações como recomendação formal.
