# GATE-893 - duplicidade de pedidos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Timeline
- Natureza: Dúvida
- Atualizado em: 2025-02-28T14:06:56.720-0300

## Contexto do Problema

## Passos para reproduzir
efetuar a carga para aplicação normalizar os registros duplicados

## Resultado apresentado
pedidos em duplicidade no historico

## Resultado esperado
que não sejam apresentados registros duplicados.

## Descrição
Senhores o cliente 746 - MEGA DISTRIBUIDORA está com a mesma situação de duplicidade que foi apresentada na demandas GATE-892, GATE-869, GATE-843 e GATE-777 onde realizamos a atualização do ambiente do cliente mas há a necessidade do envio da carga de dados com o script que corrige a tabela MXSHISTORICOPEDC.

!image-2025-02-28-12-18-04-910.png!

## Comentarios do Gatekeeper

### 1. 2025-02-28T14:06:56.716-0300 | Filipe do Amaral Padilha

Foi feita a normalização das bases dos RCAs, para validar o cliente e RCAs só precisam sincronizar o maxPedido.

Visto que estamos tendo vários casos como esse, eu solicitei ao dev que adicione a tratativa no atualizador do maxPedido, não é garantido que vão colocar ainda, depois eu trago a notícia, mas essa parte de identificar a necessidade e solicitar foi feita

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 427402
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "a duplicidade no histórico está relacionada à necessidade de normalização das bases dos RCAs" — o texto-fonte não menciona duplicidade no histórico nem estabelece essa relação causal. | "a ação recomendada neste momento é: ... incluir essa tratativa no atualizador do maxPedido" — o texto-fonte informa que isso foi solicitado ao dev, mas não apresenta como recomendação explícita ao destinatário. | "Próximo passo: aguardar retorno do desenvolvimento sobre a inclusão da tratativa no atualizador do maxPedido" — o texto-fonte diz apenas "depois eu trago a notícia", sem formular isso explicitamente como próximo passo.
