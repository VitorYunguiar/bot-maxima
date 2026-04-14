# GATE-581 - Busca por descrição ou marca não retorna nome completo da marca

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: ALF
- Assunto: MXPED - Produto - Pesquisa
- Natureza: Dúvida
- Atualizado em: 2025-01-06T15:42:13.854-0300

## Contexto do Problema

## Passos para reproduzir
>> Iniciar pedido para cliente 7908;
>> Selecionar busca por "DESCRIÇÃO OU MARCA";
>> Marcar flag "Pesq. qualquer parte do campo"
>> Buscar marca "ELMA CHIPS";
>> Buscar marca "ELMA";

## Resultado apresentado
Ao buscar "ELMA CHIPS não é retornado produto algum, porem ao buscar somente "ELMA" a busca retorna os produtos da marca ELMA CHIPS

## Resultado esperado
Ja que a flag "Pesq. qualquer parte do campo" está ativa, a busca pelo nome completo da marca deveria retornar os produtos corretamente.

## Descrição
Ao buscar o nome completo de uma marca na busca da aba TABELA a busca não retorna itens. Porem ao buscar apenas metade do nome da marca os itens são retornados corretamente.

Login: 3sertoes.ISABELA

Ocorrendo em base do zero.

## Comentarios do Gatekeeper

### 1. 2025-01-06T15:42:13.853-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 porque acredito que os filtros deveriam trazer resultados quando pesquisado as informações de marca conforme os exemplos "ELMA CHIPS".

Paliativamente, se o cliente quiser pesquisar por marca, o filtro só de "Marca" está funcionando normalmente

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 415032
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A menção à aba **TABELA** não aparece no texto-fonte. | A referência ao filtro **“DESCRIÇÃO OU MARCA”** não aparece no texto-fonte. | A referência à flag **“Pesq. qualquer parte do campo”** ativa não aparece no texto-fonte. | A afirmação de que foi validado que a busca pela marca completa não retorna os itens conforme esperado extrapola o texto-fonte, que apenas diz que os filtros deveriam trazer resultados. | A formulação de que houve 'testes informados' não está explicitamente no texto-fonte.
