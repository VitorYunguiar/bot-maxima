# GATE-633 - Valor UN do produto está incorreto

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Preço Divergente
- Natureza: Dúvida
- Atualizado em: 2025-01-15T15:46:08.595-0300

## Contexto do Problema

## Passos para reproduzir
>> Login : macrolub.TI
>> Acessar maxPedido, iniciar pedido para cliente 29555, ou qualquer outro
>> Pesquise pelo produto 701

## Resultado apresentado
>> Produto 701, na parte de valor Un esta incorreto, trazendo valor dividido

## Resultado esperado
>> Não dividir o valor UN. Valor correto

## Descrição
Produto 701 na aba de negociação esta com o Valor UN dividido. Ex:
Valor : 84,99 , valor UN 44,50

## Comentarios do Gatekeeper

### 1. 2025-01-15T15:46:08.593-0300 | Filipe do Amaral Padilha

Para exibir o valor cheio do produto conforme a QTUNIT cadastrada no item que é de QTUNIT.MXSPRODUT = 2, basta habilitar a permissão "Exibir valor total" na Central de Configurações do usuário.

Outra opção que eles possuem, é ficar com a permissão desativada "Exibir valor total" e configurar o produto na rotina 201 (integra na MXSPRODUT) para QTUNIT = 1, assim o valor unitário não será dividido por 2 resultando em 42,50.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 417013
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'No caso do produto 701' — o texto-fonte não menciona o produto 701. | 'Com a permissão "Exibir valor total" desativada, o sistema divide o valor unitário por 2 na apresentação.' — o texto-fonte só suporta isso no contexto da alternativa com QTUNIT = 1, ao dizer que assim 'o valor unitário não será dividido por 2', mas não afirma explicitamente de forma geral que com a permissão desativada e QTUNIT=2 o sistema divide o valor por 2 na apresentação. | 'Limitação: Se a permissão "Exibir valor total" continuar desativada e o produto permanecer com QTUNIT = 2, o valor unitário continuará sendo dividido por 2.' — essa conclusão não está explicitamente declarada no texto-fonte.
