# GATE-664 - Compartilhamento de pedidos bloqueados não gera itens.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Central de Configurações
- Natureza: Dúvida
- Atualizado em: 2025-01-21T09:54:48.782-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar central de configurações do maxPedido;
>> Menu lateral, CONSULTAS, PEDIDOS BLOQUEADOS (NUVEM);
>> Filtrar pedidos do dia 20/01/2025;
>>Escolher qualquer pedido, AÇÕES , COMPARTILHAR;

## Resultado apresentado
não apresenta os itens do pedido, mesmo com eles sendo apresentados na opção de itens, listados no JSON do pedido e ativos no banco nuvem.

## Resultado esperado
Função de compartilhar funcionando corretamente.

## Descrição
A opção de compartilhar pedidos bloqueados em nuvem na central de configurações não apresenta os itens do pedido, mesmo com eles sendo apresentados na opção de itens, listados no JSON do pedido e ativos no banco nuvem.

## Comentarios do Gatekeeper

### 1. 2025-01-21T09:41:56.603-0300 | Filipe do Amaral Padilha

Será enviado para N3 porque a princípio era para a consulta buscar os produtos dentro do JSON do pedido salvo e bloqueado para exibir no compartilhamento

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
