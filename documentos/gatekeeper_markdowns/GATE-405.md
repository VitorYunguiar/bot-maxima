# GATE-405 - Status dos pedidos não atualizam

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Timeline
- Natureza: Erro
- Atualizado em: 2024-11-28T12:04:39.451-0300

## Contexto do Problema

## Passos para reproduzir
Login: ttslz.maria1227
>> Verificar pedido 223000698 na MXSHISTORICOPEDC

## Resultado apresentado
Posição L no banco nuvem nas não atualiza na base do RCA.

## Resultado esperado
Status de pedidos atualizando automaticamente.

## Descrição
Novamente os status dos pedidos não atualizam para os RCAs e ficam divergentes do banco nuvem.

Pedido ja consta na MXSHISTORICOPEDC com posição L, mas não é atualizado na base do RCA.

Cliente usa Sync automática.

## Comentarios do Gatekeeper

### 1. 2024-11-28T12:04:39.450-0300 | Filipe do Amaral Padilha

O problema já foi corrigido e acreditamos que seja um problema da questão da assinatura, porém o Desenvolvimento ainda não publicou porque é final de mês.

No caso nós vamos fazer o seguinte, eu vou reenviar os dados do pedido para o RCA receber novamente a assinatura e o aplicativo baixar automaticamente o status. Isso deve estar resolvendo o problema no momento.

A correção definitiva ainda será lançada para evitar que isso ocorra novamente e não precisaremos ficar intervindo.

Para valiadar o RCA deve estar verificando por conta própria se na timeline, esse pedido 223000698 foi atualizado para a posição "L".

Quando a janela de publicação dessa demanda, se você ou a CS precisarem saber dessa informação, teria que conversar com a Lorrayne. E o Brunão que fez o ajuste

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409263
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'divergência de status entre o banco nuvem e a base do RCA' não é mencionada no texto-fonte. | A referência ao login 'ttslz.maria1227' não aparece no texto-fonte. | 'correção parcial' não é afirmado explicitamente no texto-fonte; o texto diz apenas que o problema já foi corrigido no momento e que haverá uma correção definitiva depois.
