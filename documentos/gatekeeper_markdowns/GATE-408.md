# GATE-408 - Painel de auditoria sem dados

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Pedro Henrique Rodrigues Moura
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Sem Informações
- Natureza: Dúvida
- Atualizado em: 2024-11-28T11:09:44.103-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar MaxGestão (SysMax);
>> Geolocalização / Painel de auditoria
>> Filtro: Filial 01 / Supervisor: Todos / RCA: Marcos Eli / Data: 27/11
>> Acessar dados do RCA;

## Resultado apresentado
>> Durante toda a rota do RCA ao longo do dia, só captou rastro do mesmo a partir das 16:43 e finalizou as 16:45, apresentando quase os mesmos valores em 4 vendas diferentes;

## Resultado esperado
>> Visto que o RCA realizou uma rota de mais de 10 clientes, no qual teve vendas sendo transmitidas e deslocamento, os dados referente à quilometragem era para estar sendo validado.

## Descrição
>> Ao validar informações do rastro do RCA no painel de auditoria, só consta informações a partir das 16:43 à 16:45, o restante do dia sem rastro nenhum;

## Comentarios do Gatekeeper

### 1. 2024-11-28T11:09:38.876-0300 | Filipe do Amaral Padilha

Enviar para N3 e vincular na demanda MXGESNDV-15096
As evidências revelaram que o problema já foi identificado e está em processo de correção;
Será importante acompanhar se depois que voltar do N3 se o problema foi resolvido de fato.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409245
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'no painel de auditoria' — o texto-fonte não menciona painel de auditoria. | 'sem SQL associado' / 'Não há SQL disponível' — o texto-fonte não menciona SQL. | 'Não foram informados parâmetros de validação' — o texto-fonte não menciona parâmetros de validação.
