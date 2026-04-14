# GATE-647 - Falha ao gerar roteiro de visitas

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: ROTVENDN - RCA - Montagem de Rotas
- Natureza: Dúvida
- Atualizado em: 2025-01-16T14:36:44.030-0300

## Contexto do Problema

## Passos para reproduzir
>> efetuar o login no portal do roteirizador do cliente;
>> buscar pelo RCA LEANDRO DIAS FERREIRA;
>> efetuar a roteirização do RCA;
>> clicar em agenda e selecionar agenda dinamica;
>> definir as regras conforme o print em anexo e no planejamento semanal escoler a rota SEMANA 2;
>> Clicar em "add sequencia";
>> observar o alerta retornado;
>> voltar as rotas do RCA e editar a SEMANA 2;
>> observar as listas de clientes definidos nessa respectiva rota.

## Resultado apresentado
está ocorrando um alerta de que a rota selecionada não possui uma sequencia de clientes para agendamento, mesmo que os dias da semana tenham clientes selecionados.

## Resultado esperado
é esperado que a sequencia ocorra sem falhas ao ser selecionada essa rota.

## Descrição
Senhores, ao analisar o cenário do ticket referido eu não identifiquei o que gera esse alerta abaixo:

!image-2025-01-15-14-41-56-578.png!

onde mesmo que a configuração da semana tenha clientes definidos nos dias, não permite a geração da agenda por não encontrar uma sequencia:

!image-2025-01-15-14-44-34-722.png!

Nesse cenário, o que falta de ser configurado no sistema pelo cliente para que a agenda possa ser gerada? ou se trata de algum erro no comportamento da aplicação?

## Comentarios do Gatekeeper

### 1. 2025-01-16T12:08:16.504-0300 | Filipe do Amaral Padilha

A mensagem de não permitido adicionar "Rota SEMANA 1 não possui sequência de clientes para agendar visitas."

Ocorre porque o cliente não finalizou o cadastro do Roteiro, que seria o percurso em Km Total que é gerado pela posição dos clientes no mapa.

Esse cliente trabalha com "Regiões cadastradas" no Roteirizador e esse conceito fica habilitado para ser selecionado na hora de cadastrar a rota.

Então para gerar a Roteirização ele precisa selecionar uma região em pelo menos um dia da semana na Rota cadastrada e depois apertar para Roteirizar;

Feito isso o Km Total será gerado e ele conseguirá adicionar a Rota na Semana para geração de Agenda Dinâmica.

Se eles não quiserem trabalhar com esse conceito, teriam que excluir as regiões cadastras no Roteirizador.

Se ele contestar por qualquer outro motivo, por gentileza, me contatar para a gente conversar.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 417223
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Sem essa etapa concluída, a rota pode apresentar a mensagem de que não possui sequência de clientes para agendar visitas, mesmo havendo clientes definidos nos dias da semana." — a parte "mesmo havendo clientes definidos nos dias da semana" não consta no texto-fonte. | "Limitação da análise: não há detalhamento adicional sobre tela, campo, validação interna, logs ou evidências técnicas complementares." — essa observação não está suportada explicitamente pelo texto-fonte. | "Caso o cliente conteste por outro motivo, o próximo passo é contatar o autor do comentário técnico para aprofundamento." — o texto-fonte diz para contatar "me contatar para a gente conversar", mas não menciona "autor do comentário técnico" nem "aprofundamento".
