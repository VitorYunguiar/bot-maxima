# GATE-231 - Campanha de preço fixo - migração para v3

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Não Informado
- Assunto: MXPED - Política de Desconto - Preço Fixo
- Natureza: Dúvida
- Atualizado em: 2024-10-28T11:27:13.707-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do vendedor, iniciar um pedido em um cliente qualquer e inserir o produto 14377.

## Resultado apresentado
Na v3, a campanha de preço fixo não é apresentada, já na v2 é apresentada normalmente.

## Resultado esperado
Esperado que a campanha cadastrada funcione na v3.

## Descrição
Cliente está em processo de migração da v2 para a v3, e realizou um cadastro de uma campanha de preço fixo na Central de Configurações para o produto 14377, no valor de 24.49.
Entretanto, a mesma não é apresentada na v3, ao retornar para a v2 a campanha é apresentada normalmente.

Login para teste:
stk.marcioaparecido

## Comentarios do Gatekeeper

### 1. 2024-10-28T11:26:09.947-0300 | Filipe do Amaral Padilha

--Será encaminhado para N3

Foi identificado que a Query do maxPedido na V3 não trata a informação numregiao nula nas políticas de preço fixo assim como no SQL da V2 por isso acredito que deveria ser tratado como erro e precisa ser alinhado com o P.O visto que o cliente está em processo de migração da V2 para a V3.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 403365
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Na V3, a campanha de preço fixo não é apresentada para o produto 14377. | Na V2, a campanha é apresentada normalmente. | A divergência ocorre porque a query do maxPedido na V3 não trata numregiao nula nas políticas de preço fixo, diferentemente do SQL da V2, que contempla esse cenário. | O caso deve ser tratado como erro na V3.
