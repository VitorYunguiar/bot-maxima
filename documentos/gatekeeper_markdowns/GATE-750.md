# GATE-750 - Produto não aparece na base do RCA, porém aparece na base do zero

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2025-02-05T17:13:47.127-0300

## Contexto do Problema

## Passos para reproduzir
>>Gerar base do zero e base do RCA em anexo
>>Iniciar pedido para o cliente 10722 de exemplo
>>procurar o produto 5320

## Resultado apresentado
>>Na base do zero o produto aparece
>>na base do RCA o produto não aparece mesmo realizando carga

## Resultado esperado
>>Os produtos devem aparecer na base do RCA

## Descrição
>>Ao baixar a base do RCA em anexo vários produtos não aparecem para o RCA ex:5320

>>Não existe filtro aplicado

>>Realizei carga de atualizid nas seguintes tabelas porém mesmo sincronizando o problema não deixou de ocorrer:

(MXSPRODUT, MXSPRODFILIAL, MXSEMBALAGEM, MXSFORNEC, MXSDEPTO, MXSSECAO, MXSTABPR, MXSTABPRCLI e MXSRESTRICAOVENDA0)

Login: UDIMIX.gabriel62

Senha: Hash

## Comentarios do Gatekeeper

### 1. 2025-02-05T17:13:47.123-0300 | Filipe do Amaral Padilha

Realizada normalização dos dados que não eram apresentados para o RCA (produtos que não apareciam). Realizei o teste e após sincronizar o RCA conseguirá ver os produtos que não apareciam normalmente.

O problema foi causado por um erro de sincronização e uso de múltiplos aparelhos. Nos logs da MXSAPARELHOSCONNLOG, constam 2 aparelhos utilizados no mesmo usuário do RCA, e na sincronização que desceria os dados da região de preço do produto, ocorreu um erro.

Esses erros de sincronismo são tratados no nosso backend, foi feita uma correção para esse fluxo, onde, caso ocorra erro na sincronização, a próxima sincronização recebe novamente os dados para resolver o problema.

Porém, para receber essa correção, o banco de dados nuvem deve ser atualizado.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 421884
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que a ausência dos produtos na base do RCA 'não estava relacionada a filtro funcional informado no cenário' não aparece no texto-fonte. | A recomendação de 'sincronizar novamente o RCA após a atualização/correção' como passo necessário após atualizar o banco de dados nuvem não é afirmada explicitamente no texto-fonte. | A formulação de 'reenvio dos dados em caso de erro de sincronização' como próximo passo operacional não está explicitamente indicada como ação a executar; o texto-fonte apenas informa que o backend foi corrigido para que a próxima sincronização receba novamente os dados.
