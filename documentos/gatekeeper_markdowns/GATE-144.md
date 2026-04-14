# GATE-144 - Vinculo de grupo de cliente MXSPRECOPROM

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - Política de Desconto - Preço Fixo
- Natureza: N/A
- Atualizado em: 2024-10-09T09:35:20.266-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Bom dia, gostaria de saber qual tabela faz o vinculo dos clientes do grupo que é utilizado no MXSPRECOPROM.CODGRUPOCLI

## Comentarios do Gatekeeper

### 1. 2024-10-04T09:57:51.936-0300 | Filipe do Amaral Padilha

A Laredo é um cliente que usava essa função com a MXSDESCONTO, então em versões recentes isso precisa funcionar, na dúvida atualiza para a ponta. A ideia é que as política de preço fixo sejam validadas com grupos de clientes cadastrados.

A gente integra esses grupos e relação com as campanhas nas tabelas MXSGRUPOSCAMPANHAC e MXSGRUPOSCAMPANHAI. Abaixo eu coloquei a relação que elas têm com a MXSPRECOPROM para validação dos preços fixos por grupo de clientes:

MXSGRUPOSCAMPANHAC.codgrupo = mxsprecoprom.codgrupocli
MXSGRUPOSCAMPANHAI.codgrupo = mxsprecoprom.codgrupocli
MXSGRUPOSCAMPANHAI.coditem = codcli

--Se não estiver integrando corretamente do bd local para a nuvem ou não estiver funcionando conforme o esperado, por gentileza, me informar que eu posso estar revisando a funcionalidade.

## Resposta Canonica

O vínculo do grupo de clientes utilizado em `MXSPRECOPROM.CODGRUPOCLI` é feito pelas tabelas:

- `MXSGRUPOSCAMPANHAC`
- `MXSGRUPOSCAMPANHAI`

Relacionamentos informados:

- `MXSGRUPOSCAMPANHAC.codgrupo = MXSPRECOPROM.CODGRUPOCLI`
- `MXSGRUPOSCAMPANHAI.codgrupo = MXSPRECOPROM.CODGRUPOCLI`
- `MXSGRUPOSCAMPANHAI.coditem = codcli`

Contexto funcional:
- Em versões recentes, isso precisa funcionar.
- A validação das políticas de preço fixo considera os grupos de clientes cadastrados.
- Os grupos e a relação com as campanhas são integrados nas tabelas `MXSGRUPOSCAMPANHAC` e `MXSGRUPOSCAMPANHAI`.

Ação recomendada:
- Validar esse vínculo nessas tabelas.
- Verificar se a integração do BD local para a nuvem está ocorrendo corretamente.
- Em caso de não funcionamento ou comportamento diferente do esperado, informar para revisão da funcionalidade.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 398947
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
