# GATE-534 - Status de pedidos não atualiza

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Timeline
- Natureza: Dúvida
- Atualizado em: 2024-12-19T17:04:53.521-0300

## Contexto do Problema

## Passos para reproduzir
>> Login: acobrazil.savana.araujo
>> Acessar maxPedido, importar base de dados, ir na timeline de pedidos, procurar pedido 1947016199 (72362597).

## Resultado apresentado
>> Pedido 1947016199 ainda consta com status B, porém o mesmo já foi faturado no banco local.

## Resultado esperado
>> Status dos pedidos atualizem conforme for enviado pelo ERP.

## Descrição
O cliente está questionando a demora na atualização do status de pedidos bonificados.

Durante a análise, foram observados os pedidos 72362596 e 72362597:

- O pedido 72362596 já foi atualizado para o status "Faturado".
- Entretanto, o pedido 72362597 ainda consta com o status B no banco nuvem.
- Ao verificar no banco local, foi identificado que o pedido 72362597 já está registrado como "Faturado".

## Comentarios do Gatekeeper

### 1. 2024-12-19T17:04:53.519-0300 | Filipe do Amaral Padilha

O problema ocorreu porque o pedido foi alterado para origemped "T" na PCPEDC e na PCMXSCONFIGURACOES do banco deles, que é uma configuração para descida de informações para a nossa nuvem via extrator o parâmetro ENVIA_PEDIDOS_TELEMARKETING estava configurado como "N" (desligado).

Então nesse caso não é falha do sistema é uma falta de configuração para descer pedidos da origem "T" que foi uma alteração que ocorreu no Winthor nesse pedido.

Para resolver e atualizar corretamente na nuvem, então eu alterei o parâmetro ENVIA_PEDIDOS_TELEMARKETING = 'S' e fiz a normalização dos dados somente desse mês de Dezembro, enviando eles para a nuvem.

Dados reenviados da PCPEDC e PCPEDI, depois que a carga acabar, basta os RCAs realizarem o swipe que vai atualizar os status corretamente.

## Resposta Canonica

Causa identificada: não houve falha sistêmica. O pedido teve alteração no Winthor e passou a ter `origemped = "T"` na `PCPEDC`. No banco do cliente, o parâmetro `ENVIA_PEDIDOS_TELEMARKETING` na `PCMXSCONFIGURACOES` estava configurado como `"N"`, o que impedia a descida, via extrator, de pedidos dessa origem para a nuvem.

Evidências analisadas:
- O pedido foi alterado para `origemped = "T"` na `PCPEDC`.
- O parâmetro `ENVIA_PEDIDOS_TELEMARKETING` estava como `"N"` no banco do cliente.
- Por esse motivo, os dados desse pedido não estavam sendo enviados para a nuvem.
- Foi confirmado reenvio dos dados de `PCPEDC` e `PCPEDI` para a nuvem.

Ação realizada e orientação:
- O parâmetro deve permanecer como `ENVIA_PEDIDOS_TELEMARKETING = "S"` para permitir o envio de pedidos com origem `"T"`.
- Foi realizada a normalização e o reenvio dos dados necessários para a nuvem.
- A normalização foi feita somente para este mês de dezembro.

Próximo passo:
- Aguardar a conclusão da carga.
- Após isso, os RCAs devem realizar o swipe para que os status sejam atualizados corretamente na nuvem.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 413294
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
