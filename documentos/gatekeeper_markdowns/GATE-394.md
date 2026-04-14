# GATE-394 - maxGestão apresentando coluna "Agendados" com valor zerado no Painel de Auditoria

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Henrique Torres Andrade [X]
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Dados Incorretos
- Natureza: Erro
- Atualizado em: 2024-11-27T16:32:02.844-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar o Painel de Auditoria do maxGestão
>> Pesquisar todos os supervisores, neste mês, nos dias 25 e 26
>> Observar a coluna "Agendados"

## Resultado apresentado
>> maxGestão apresenta valor zerado na coluna "Agendados" tanto para supervisores quanto para RCAs, sendo que os supervisores possuem RCAs com visitas agendadas para estes dias
>> Realizei testes com um supervisor/usuário em específico também, CODSUPERVISOR = 17 e CODUSUR = 537. O usuário possui agendamentos para o dia 25, mas não mostra a quantidade de agendados nem pesquisando pelo supervisor e nem pelo RCA
>> Verificado que quando clica no ícone do "olho", que é a coluna "Positivados", última coluna, o ícone de "Cliente agendado" também mostra ícone de "x", indicando que os clientes listados no relatório não estão agendados, sendo que estão

## Resultado esperado
>> maxGestão mostrar quantidade de agendamentos de acordo com os filtros inseridos na coluna "Agendados"

## Descrição
>> maxGestão está apresentando valores zerados na coluna "Agendados" para supervisores e para RCAs
>> Atualizado ambiente nuvem do cliente

## Comentarios do Gatekeeper

### 1. 2024-11-27T16:32:02.843-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 as evidências apresentadas são sólidas, eu também, complementei a análise e avaliei que esse não é comportamento normal do Painel de Auditoria

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409093
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma especificamente que há uma divergência na coluna “Agendados”, exibida com valor zerado, inclusive quando há indicação de agendamentos. O texto-fonte não menciona a coluna “Agendados” nem esse comportamento específico. | A resposta afirma que as evidências foram consideradas consistentes para confirmar a divergência informada. O texto-fonte diz apenas que as evidências são sólidas, sem mencionar confirmação de uma divergência específica. | A resposta menciona que o N3 é o responsável pela continuidade da análise e correção do caso. O texto-fonte apenas informa que será encaminhado para N3, sem detalhar responsabilidades. | A resposta apresenta como próximo passo 'encaminhar o caso para o N3'. Embora compatível com o texto-fonte, isso é uma recomendação/estrutura adicional não explicitamente formulada dessa maneira no texto original.
