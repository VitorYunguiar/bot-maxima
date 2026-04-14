# GATE-407 - KMs incorretos no painel de auditoria

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Dados Incorretos
- Natureza: N/A
- Atualizado em: 2024-12-02T10:55:54.757-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxGestão;
>> Acessar painel de auditoria;
>> Buscar dados do dia 27/11/2024 para o vendedor 25851;

## Resultado apresentado
Informado que o KM total no dia foi de 13015 km.

## Resultado esperado
Dados corretos

## Descrição
Alguns RCAs estão contabilizando valores absurdos de KM total e KM trabalhado.

Prints em anexo.

Dados referentes ao dia 27/11 no painel de auditoria.

## Comentarios do Gatekeeper

### 1. 2024-11-28T09:05:13.428-0300 | Filipe do Amaral Padilha

Eu fiz uma pré-análise, os dados na API de rastros estão constando com esse km total de 34mil;
Nesse caso, eu vou precisar da base maxTracking e também do maxPedido das opções em Ferrametas:
>> Exportar Banco
>> Exportar Banco MaxTracking

Porque eu preciso verificar se saiu inconsistente da base do RCA esses rastros.

Pode ser só as bases do RCA:
25851 - ELTON VENICIO DE OLIVEIRA

Feito isso por gentileza, abrir um novo gate, que dai eu vou dar continuidade

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409184
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "o que indica que a divergência pode estar na origem dos rastros e precisa ser validada diretamente nas bases do RCA" | "Identificada, em pré-análise, inconsistência nos dados de rastros"
