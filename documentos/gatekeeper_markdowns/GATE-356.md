# GATE-356 - Não apresenta as observações e justificativa no painel de auditoria

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Eres Informática
- Assunto: MXGESN - Painel de Auditoria - Sem Informações
- Natureza: N/A
- Atualizado em: 2024-11-21T15:06:32.637-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o MaxGestão com o SysMax
>>Ir no painel de auditoria
>>Nos filtros colocar: Filial: 1; Supervisor: 1; Representante: 22546 - VENDEDOR LUIZ FILHO APARTIR DE 17/01/22; Período: 19/11/2024 a 20/112024
>>Pesquisar
>>Clicar em ações (no olhinho)
>>E clicar em imprimir
>>E assim irá ver que no relatório gerado não traz os dados de justificativa e observação.

Pode utilizar de exemplo o cliente 21950, ele consta a justificativa na API.

## Resultado apresentado
Não apresenta informações de justifica e observações nos relatórios do painel de auditoria

## Resultado esperado
Que apresente nos relatórios as justificativas e observações realizadas pelos vendedores

## Descrição
No painel de auditoria quando emitimos o relatório não está trazendo as informações de observações e justificativa, foi consultado com vendedores que estão na v2 e v3 e ambos não trazem essa informação, mais ao consultar na API para ambos tem as informações.

Por exemplo o RCA Luiz Filho está na versão 3.251.8, e o RCA BISMARQUE está na versão 2.32.0, ambos constam os dados na API mais no gestão no relatório não apresenta as informações de observações e justificativas.

## Comentarios do Gatekeeper

### 1. 2024-11-21T15:06:32.635-0300 | Filipe do Amaral Padilha

Enviado para N3 para averiguarem se analisamos corretamente o caso dos registros constarem na API de rastros porém não serem exibidos no Painel de Auditoria

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 407955
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Foi confirmado' que os registros constam na API de rastros e não estão sendo exibidos no relatório do Painel de Auditoria — o texto-fonte apenas diz que foi enviado para N3 para averiguarem esse caso, não confirma o fato. | Os tipos específicos de registros 'justificativa e observação' não são mencionados no texto-fonte. | A expressão 'relatório do Painel de Auditoria' não aparece no texto-fonte; o texto fala apenas em 'Painel de Auditoria'. | 'No estágio atual, não há causa identificada para o comportamento' não está explicitamente informado no texto-fonte. | 'O único direcionamento registrado' não está explicitamente informado no texto-fonte. | 'A análise do caso foi realizada corretamente' como formulação afirmativa não está no texto-fonte; o texto apenas diz que o N3 vai averiguar se analisamos corretamente o caso. | 'Os dados existem na API de rastros' é tratado como conclusão factual, mas isso não foi confirmado no texto-fonte. | 'A ausência ocorre na exibição pelo Painel de Auditoria' é tratada como conclusão factual, mas isso não foi confirmado no texto-fonte. | 'Não há detalhamento técnico da causa até o momento' não está explicitamente informado no texto-fonte. | As seções 'Ação recomendada' e 'Próximo passo' inferem recomendação e espera, enquanto o texto-fonte apenas registra que o caso foi encaminhado ao N3 para averiguação.
