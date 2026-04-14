# GATE-151 - Pedido não atualiza status com a sync automatica

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Timeline
- Natureza: N/A
- Atualizado em: 2024-10-07T11:46:05.037-0300

## Contexto do Problema

## Passos para reproduzir
Login: ttslz.erivan1006
>> Logar no maxPedido;
>> Verificar timeline de pedidos;

## Resultado apresentado
Status não são atualizados

## Resultado esperado
Status atualizando normalmente

## Descrição
Pedidos ja foram integrados e estão com status 4 porem na timeline de pedidos os status não são atualizados. Cliente usa sync automática e não pode fazer swipe.

Tratado no ticket MXPEDDV-81866

Base em anexo.

## Comentarios do Gatekeeper

### 1. 2024-10-07T11:44:06.901-0300 | Filipe do Amaral Padilha

Os pedidos não estavam tendo o status atualizado automaticamente porque o usuário em específico, não estava configurado para trabalhar com a sincronização automática.

*Não passar essa info abaixo em negrito para o cliente:*

*O campo USAMSGMAXSYNC não estava = S na MXSUSUARIOS do banco nuvem (Oracle) no CODUSUARIO 100967*

Então para resolver, a gente ativou essa configuração e reenviou os pedidos de forma a recriar a informação assíncrona para o usuário receber.

Então agora esse RCA já pode estar validando os pedidos 800012, 800011, 800010 se os status foi atualizado automaticamente e também validar os próximos pedidos realizados.

Lembrando como ele trabalha com sincronização automática, ele não pode usar otimização de bateria no maxPedido.

Recomendo cadastrar o parâmetro BLOQUEAR_UTILIZACAO_BATERIA_OTIMIZADA = S

### 2. 2024-10-07T11:46:05.037-0300 | Filipe do Amaral Padilha

Precisa ser o RCA diretamente para validar, não baixa a base dele porque senão você rouba a sincronização automática.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 399226, 399228
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: O usuário **ttslz.erivan1006** não estava configurado para trabalhar com sincronização automática. | O comportamento reportado foi que os pedidos já integrados, com status 4, não tinham a timeline atualizada automaticamente. | A análise textual confirmou que os pedidos usados na validação são **800012, 800011 e 800010**.
