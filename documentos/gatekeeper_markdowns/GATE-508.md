# GATE-508 - Divergência nos valores do gestão com a rotina 1464e rotina 111

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral - Dados Divergentes do ERP
- Natureza: N/A
- Atualizado em: 2024-12-16T17:11:28.328-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o MaxGestão
>>No painel geral aplicar os filtros: Data: 01/12/2024 a 12/12/2024, Filtrar por data de faturamento do pedido, e deduzir as devoluções
>>E assim retorna um valor de 8.419.332,14 e  389.509,47 de devoluções.
>>Enquanto na rotina 111 e 1464 deduzindo as devoluções traz um valor de 8.413.047,81

## Resultado apresentado
Valores no painel geral ficando divergente das rotina 1464 e 111 quando deduzimos as devoluções

## Resultado esperado
Que os valores no painel geral fique conforme as rotina 1464 e 111, quando aplicarmos nos filtros para deduzir as devoluções

## Descrição
Dentro do MaxGestão quando colocamos para deduzir as devoluções está ficando divergente os valores com a rotina 1464 e 111.

## Comentarios do Gatekeeper

### 1. 2024-12-16T17:11:28.327-0300 | Filipe do Amaral Padilha

Será enviado para N3 a carga fez com que algumas informções a mais fossem apresentadas mas não resolveu a divergência de dados. Será necessária uma análise mais aprofundada para entedermos a causa da divergência e possível solução.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 412518
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "não eliminou a divergência de valores" — o texto-fonte fala em "divergência de dados", não especificamente de valores. | "entre o painel geral do MaxGestão e as rotinas 111 e 1464 ao deduzir devoluções" — esses sistemas/rotinas não são mencionados no texto-fonte. | "a causa raiz não foi identificada" — o texto-fonte diz que será necessária análise mais aprofundada para entender a causa, mas não usa a expressão causa raiz. | "avaliação da possível correção" — o texto-fonte menciona possível solução, não especificamente correção.
