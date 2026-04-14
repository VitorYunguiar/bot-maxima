# GATE-162 - Resumo de venda não atualiza

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Sincronização - Atualizar Menu
- Natureza: Erro
- Atualizado em: 2024-10-09T17:12:08.863-0300

## Contexto do Problema

## Passos para reproduzir
>>Abrir a base do zero do RCA 158 ou outro
>>Clicar em atualizar menu

## Resultado apresentado
>>O sistema exibe o erro:
"Não foi possível atualizar o resumo de vendas.
Tente novamente mais tarde"

## Resultado esperado
>>Que o menu seja apresentado sem erros

## Descrição
>>Ao clicar em Atualizar menu o sistema exibe um erro

"Não foi possível atualizar o resumo de vendas.
Tente novamente mais tarde"

## Comentarios do Gatekeeper

### 1. 2024-10-09T16:28:29.996-0300 | Filipe do Amaral Padilha

Eu verifiquei juntamente com um desenvolvedor e acreditamos que para o menu de vendas atualizar com sucesso só está faltando o cadastro das datas no Winthor na Rotina 309, essa rotina alimenta a tabela PCDATAS que validamos ao fazer a requisição para atualizar esse menu da tela inicial. Dai teria de ser cadastado desse e dos outros meses para evitar que ocorra nos meses seguintes também.

No caso precisa orientar o cliente sobre esse cadastro da rotina 309 para o mês vigente, essa validação é importante para outras funcionalidades do força de vendas, além dessa atualização do Menu inicial. E feito isso no Winthor, pode estar validando a atualização do Menu inicial. Se por acaso continuar dando errado, por gentileza, nos acionar novamente.

Para validar, depois de cadastrar no Winthor as datas, acredito também que será necessário relogar no usuário no maxSoluções. Deslogar no usuário e depois logar novamente e então mandar atualizar.

*Não passar ao cliente: O link do cliente t-cloud no cadastro na nuvem do extrator dele estava com http e não https; http não é para ser. E como estava esse link errado então infelizmente precisa relogar no maxsoluções como expliquei acima*

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 399891
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "A falha ao atualizar o menu ocorre" — o texto-fonte diz que "acreditamos que" só está faltando o cadastro das datas; não afirma de forma conclusiva a causa. | "Na análise, foi confirmado que a atualização do menu depende da validação das datas cadastradas na PCDATAS" — o texto-fonte não diz que isso foi confirmado, apenas que validaram essa tabela ao fazer a requisição e que acreditam que falta o cadastro das datas.
