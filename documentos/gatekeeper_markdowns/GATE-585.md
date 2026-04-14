# GATE-585 - Mesmo com todas as informações corretas a API de cancelamento não funciona

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Editar
- Natureza: Dúvida
- Atualizado em: 2025-01-07T14:10:06.243-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o maxPedido em base do zero ou na base em anexo
>>Iniciar um pedido para um cliente qualquer ex.1124
>>Incluir algum produto ex. 57
>>Salvar e enviar
>>Ir na timeline de pedidos
>>Segurar sobre o pedido e solicitar cancelamento

## Resultado apresentado
>>No maxPedido o pedido aparece como cancelado, porém ao verificar na MXSHISTORICOPEDC o pedido ainda consta com posição = L
>>Na MXSINTEGRACAOPEDIDO o pedido aparece como CANCELADO = S

## Resultado esperado
>>Tanto na MXSHISTORICOPEDC quanto no aparelho do RCA, os pedidos devem ser cancelados pela API

## Descrição
>>Mesmo com todas as informações corretas a API de cancelamento do cliente Tcloud não funciona

>>IP enviado pelo cliente [http://201.157.197.15:80|http://201.157.197.15/] (Testei com e sem a porta)

>Usuário: JOAO

>Senha: 0497 Criptografada: (8RLCic66YyfVSKrrN66faQ==)

Usuário maxPedido: BRITOTARGI.rca

Senha: Temporária

## Comentarios do Gatekeeper

### 1. 2025-01-07T14:10:06.241-0300 | Filipe do Amaral Padilha

O problema era causado pela configuração do IP no extrator (Jenkins) do cliente. Foi necessário colocar o IP "http://201.157.197.15/" dessa forma, sem a porta, porque no Workspace ele só acessa o WTA do cliente se não tiver a porta. É comum isso em alguns casos (quando o cliente não tem acesso externo liberado para a porta do WTA).

Feito isso eu reiniciei o extrator e atualizei a versão de banco. Também executei o teste no maxPedido e cancelou com sucesso via API de cancelamento.

O parâmetro UTLIZA_API_CANCEL_WINTHOR para testar eu habilitei ele para todos os RCAs = S.

Já o parâmetro PERMITE_CANCELAR_PEDIDO_ERP eu deixei para Geral NULL, nesse fluxo que ele vai trabalhar não precisa desse parâmetro.

Para validar o cliente só precisa sincronizar os RCAs e liberar as permisões de edição ou cancelamento de pedidos na central. Com isso já vão conseguir cancelar pedidos com posição diferente de "M" "C" e "F".

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 415310
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que a configuração do IP no extrator estava 'incorreta' não está explicitamente no texto-fonte; o texto apenas diz que o problema era causado pela configuração do IP e que foi necessário informar sem a porta. | A afirmação específica de configurar sem ':80' não está no texto-fonte; o texto apenas diz 'sem a porta', sem mencionar a porta 80. | A seção 'Parâmetros validados' usa a palavra 'validados', o que não está explicitamente afirmado no texto-fonte. | A afirmação 'Com essa configuração, o cancelamento via API funciona para pedidos com posição diferente de M, C e F' extrapola o texto-fonte, que diz que para validar o cliente precisa sincronizar os RCAs e liberar permissões na central; só então conseguirão cancelar pedidos com posição diferente de M, C e F. | A afirmação 'Responsável pela ação: cliente' não está explicitamente no texto-fonte.
