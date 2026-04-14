# GATE-334 - mix cliente 180 dias

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Adriel Gonçalves Peixoto
- ERP do cliente: Winthor
- Assunto: MXPED - Parametrização
- Natureza: Dúvida
- Atualizado em: 2024-11-14T06:54:02.376-0300

## Contexto do Problema

## Passos para reproduzir
Configurar o parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS para 180 dias

## Resultado apresentado
Atualmente o parâmetro é de no máximo 90 dias

Cliente solicitou um aumento para 360 dias, porem o o P.O sugeriu analise pela equipe de desenvolvimento para liberar 180 dias

## Resultado esperado
Configurar o parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS para 180 dias

## Descrição
Com a atualização do prazo máximo do mix do cliente (90 dias), alguns vendedores sentiram dificuldade para realizar consulta de itens. Afinal, esse é uma das funções mais utilizadas do MaxPedido.

Tendo em vista o retorno que o PO passou no ticket anterior MXPED-61460, gostaria que fosse avaliado pelo time de desenvolvimento a possibilidade de ampliar para o prazo de 180 dias.

## Comentarios do Gatekeeper

### 1. 2024-11-14T06:37:46.489-0300 | Filipe do Amaral Padilha

Eu decidi escalar a demanda para N3 como dúvida para pegar a opinião e envolver mais pessoas.

O caso é que se fosse tecnicamente falando, o nosso DBA informou que não seria viável os 180 dias porque geraria muito processamento de dados para o banco e pode gerar instabilidade para o cliente.

Atualmente eles usam o parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS = 90, o que gera 35 mil registros.

Com o parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS = 180, os dados gerados seriam de 95 mil registros.

--Se você tiver alguma ponderação do CS ou alguma outra percepção que recebeu do cliente, por gentileza, nos informar.

A gente precisa medir os dois lados, o que seria vital para o cliente de informações, a negativa que já veio da melhoria e agora uma segunda negativa para os 180 dias. E o que seria viável para a Máxima no quesito de alteração do parâmetro.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 406914
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Não é recomendada a alteração do parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS para 180 dias no momento.' — o texto-fonte não afirma explicitamente essa recomendação; apenas relata inviabilidade técnica informada pelo DBA e necessidade de ponderação. | 'Até o momento, o cenário permanece com duas negativas' — o texto-fonte menciona 'a negativa que já veio da melhoria e agora uma segunda negativa para os 180 dias' como contexto a ser medido, mas não afirma literalmente que o cenário permanece com duas negativas consolidadas. | 'Conclusão: com os fatos atuais, o limite de 90 dias deve ser mantido' — o texto-fonte não traz essa conclusão explícita, apenas informa que atualmente usam 90 dias. | 'qualquer reavaliação depende de novos subsídios do CS/cliente' — o texto-fonte pede ponderações do CS e fala em medir os dois lados, mas não estabelece essa dependência de forma explícita.
