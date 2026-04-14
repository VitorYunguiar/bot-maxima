# GATE-588 - Pedidos com origem telemarketing não estão sendo enviados para o banco nuvem

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Histórico
- Natureza: N/A
- Atualizado em: 2025-01-07T17:27:05.851-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o banco do cliente
>>Realizar uma consulta na tabela MXSHISTORICOPEDC e procurar pelo pedido 513037598
>>E assim ele não consta no banco nuvem.

O mesmo tem ORIGEMPED = T e consta no banco local.

## Resultado apresentado
Pedidos do tipo telemarketing não estão sendo enviados para o banco nuvem

## Resultado esperado
Que os pedidos do tipo telemarketing sejam enviados para nosso banco nuvem

## Descrição
Os pedidos de origem telemarketing não estão sendo enviados para a MXSHISTORICOPEDC e MXSHISTORICOPEDI, foi habilitado na PCMXSCONFIGURACOES o parâmetro ENVIA_PEDIDOS_TELEMARKETING e atualizado todo o ambiente do cliente e mesmo assim os pedidos com ORIGEMPED = T não vieram para o banco nuvem.

## Comentarios do Gatekeeper

### 1. 2025-01-07T17:27:05.849-0300 | Filipe do Amaral Padilha

As informações dos pedidos retroativos não sobem somente ao alterar o parâmetro ENVIA_PEDIDOS_TELEMARKETING para = S na PCMXSCONFIGURACOES.

Ao ativar ele, somente pedidos feitos após a ativação vão subir via Extrator.

Então para resovler esse caso é somente fazendo carga dos retroativos.

Então foi feita carga da PCPEDC e PCPEDI referentes às filiais 1 e 3 e do mês passado inteiro e mês atual.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 415426
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'de telemarketing para a nuvem' não consta no texto-fonte | A menção a 'pedidos com ORIGEMPED = T' não consta no texto-fonte | A menção a 'MXSHISTORICOPEDC' e 'MXSHISTORICOPEDI' não consta no texto-fonte | 'Não se trata de falha no envio dos novos pedidos após a ativação do parâmetro' é uma interpretação não explicitamente afirmada no texto-fonte
