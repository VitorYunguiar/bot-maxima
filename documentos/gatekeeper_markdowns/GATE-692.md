# GATE-692 - Pedido Historico

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Gleiciellen Pereira Leal [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Histórico
- Natureza: Erro
- Atualizado em: 2025-01-27T11:39:29.828-0300

## Contexto do Problema

## Passos para reproduzir
>> Foi analisado o banco do cliente na MXSINTEGRACAOPEDIDO
os dois pedidos 17211982,17211984 consta em status 4
>> Analisado o pedido na base do vendedor e não consta nenhum pedido 17211982, mesmo tirando todos os filtros do aplicativo.
>> Cliente relatou que pedidos não são feitos no maxPedido e sobem para o whinthor e que já ocorreu esse cenario mais de uma vez
>> De acordo com o cliente o rca fez apenas o pedido 17211984
>>login: cardoso.rodrigo
>> base do rca muito grande para adicionar nos anexos , encaminharei via WhatsApp ou discord

## Resultado apresentado
>> Pedido 17211982 não apareceu no maxPedido

## Resultado esperado
>> Pedido 17211982 aparecer no maxPedido

## Descrição
Pedido 17211982 não foi feito pelo RCA não aparece na aba de historico de pedidos, mas foi processado no whithor.

## Comentarios do Gatekeeper

### 1. 2025-01-27T11:39:29.827-0300 | Filipe do Amaral Padilha

Foi verificado no detalhe a confecção dos pedidos. Após verificação dos dados eu pude concluir que o RCA 172 fez de fato esses pedidos, nós temos os logs do celular e das datas que ele sincronizou o maxPedido, e essas informações estão compatíveis com a data de abertura dos pedidos.

Também gostaria de pontuar que o sistema não faz envio de pedidos de forma automática, isso depende de uma ação manual do RCA de digitar o pedido e então mandar salvar e enviar.

Pelos logs dos pedidos, não foi um pedido salvo e bloqueado, foi um pedido normal que foi salvo e enviado diretamente para integração com o Winthor.

Obs: não havia a base do RCA no ticket para análise, porém, se os pedidos não aparecem no maxPedido, na timeline por exemplo, pode ser porque o RCA excluiu os pedidos diretamente pelo maxPedido.

Mesmo tendo excluído eles vão constar na aba Consultas > histórico de Pedidos.
E se quiser restaurar eles na timeline de pedidos, basta habilitar o parâmetro
PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO = S e sincronizar o maxPedido

Abaixo coloquei as consultas realizadas na análise para entender o fluxo e ter dados mais concretos provando que o RCA 172 fez sim os pedidos.

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPED IN(17211982,17211984);

SELECT * FROM MXSUSUARIOS WHERE CODUSUARIO IN(75880);
SELECT * FROM MXSUSUARIOS WHERE CODUSUR IN(172);
--Registro da data de abertura dos pedidos no maxPedido do RCA
--DTABERTURAPEDPALM
--2025-01-14 08:29:25.000
--2025-01-14 08:31:49.000

SELECT * FROM MXSAPARELHOSCONNLOG WHERE CODUSUARIO IN(75880) ORDER BY DTATUALIZ DESC;
--O usuário estava usando esse aparelho e sincronizando normalmente para fazer pedidos durante o horário de confecção dos pedidos
--samsung	SM-A207M	20250114094910	2025-01-14 09:49:10.000
--samsung	SM-A207M	20250114084652	2025-01-14 08:46:52.000

SELECT * FROM MXSINTEGRACAOPEDIDO_LOGST WHERE ID_PEDIDO = 785452 ORDER BY DTATUALIZACAO ASC;
SELECT * FROM MXSINTEGRACAOPEDIDO_LOGST WHERE ID_PEDIDO = 785456 ORDER BY DTATUALIZACAO ASC;

SELECT * FROM MXSHISTORICOCRITICA m WHERE ID_PEDIDO = 785452 ORDER BY DATA ASC;

SELECT * FROM MXSHISTORICOCRITICA m WHERE ID_PEDIDO = 785456 ORDER BY DATA ASC;

SELECT ORIGEMPED,NUMPED,CODUSUR,CODCLI,DATA,DTFAT,DTABERTURAPEDPALM FROM MXSHISTORICOPEDC WHERE NUMPED IN(172006755, 172006631);
--Bate a data de abertura do pedido com o do maxPedido
--DTABERTURAPEDPALM
--2025-01-14 08:29:25.000
--2025-01-14 08:31:49.000

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 419188
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que o pedido 17211982 não aparece no maxPedido não está no texto-fonte. O texto-fonte fala genericamente: "se os pedidos não aparecem no maxPedido, na timeline por exemplo, pode ser porque o RCA excluiu os pedidos diretamente pelo maxPedido", sem vincular isso especificamente ao pedido 17211982. | A afirmação de que a análise foi "textual dos registros" não está explicitamente no texto-fonte; o texto-fonte diz que houve verificação detalhada e consultas/logs, mas não usa essa caracterização. | A formulação "ambos foram salvos e enviados normalmente" é uma inferência a partir de os pedidos 17211982 e 17211984 estarem na consulta e do comentário geral sobre "não foi um pedido salvo e bloqueado, foi um pedido normal que foi salvo e enviado", mas o texto-fonte não individualiza explicitamente "ambos".
