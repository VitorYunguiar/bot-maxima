# GATE-163 - Clientes atendidos aumento depois de remover excluidos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Dados Incorretos
- Natureza: N/A
- Atualizado em: 2024-10-09T17:06:40.633-0300

## Contexto do Problema

## Passos para reproduzir
>> Abrir o painel de auditoria e filtrar de acordo com a imagem em anexo.

## Resultado apresentado
Valores divergentes da quantidade de agendamentos que constam no banco nuvem.

## Resultado esperado
Valores semelhantes.

## Descrição
Na MXSCOMPROMISSOS constam 18 agendamentos para esse RCA, está de acordo com o WInthor. Porem ao puxar o relatório no painel de auditoria ele retorna 24 atendimentos agendados, e ao selecionar a opção de remover excluídos retorna 29 atendimentos.

CODUSUARIO = 60797
CODUSUR = 9003

## Comentarios do Gatekeeper

### 1. 2024-10-09T16:39:59.219-0300 | Filipe do Amaral Padilha

Enviado para N3

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review, requires_attachment_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
