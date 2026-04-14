# GATE-182 - Informações de venda não aparecem na filial 5

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXGESN - Dashboard
- Natureza: Dúvida
- Atualizado em: 2024-10-15T13:35:24.662-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar maxGestão
>Painel Geral
>Filtrar data inicial 01/10 até dia atual
>Filtrar filial 5
>Pesquisar

---

SELECTS UTILIZADOS:

SELECT CODCOB, CODSUPERVISOR, CODOPERACAO, MXSHISTORICOPEDC.* FROM MXSHISTORICOPEDC WHERE CODFILIAL = 5 ORDER BY DATA DESC;

SELECT CODOPERACAO, MXSHISTORICOPEDI.* FROM MXSHISTORICOPEDI WHERE NUMPED IN(SELECT NUMPED FROM MXSHISTORICOPEDC WHERE CODFILIAL = 5) ORDER BY DATA DESC;

SELECT * FROM MXSSUPERV WHERE CODSUPERVISOR IN(44, 45, 42, 43, 27, 33, 39, 33);

SELECT * FROM MXSCOB WHERE CODCOB = 'BK';

SELECT * FROM ERP_MXSNFSAID WHERE CODFILIAL = 5 ORDER BY DTSAIDA DESC;

## Resultado apresentado
Ao pesquisar a filial 5 não retorna dados nos indicadores, permanecendo 0. O problema não ocorre nas outras filiais

## Resultado esperado
Entender o que está impedindo os dados de serem exibidos no maxGestão.

## Descrição
Bom dia Vitor/Filipe,

Estou com uma situação no maxGestão onde ao pesquisar as informações no Painel Geral, não retorna nada ao selecionar a filial 5.

Foi verificado na ERP_MXSNFSAID, MXSHISTORICOPEDC, MXSHISTORICOPEDI e os supervisores e cobranças utilizados nos pedidos, tudo parece estar correto, não encontrei o que está causando o problema de não gerar os dados.

## Comentarios do Gatekeeper

### 1. 2024-10-15T13:35:24.660-0300 | Filipe do Amaral Padilha

Para resolver a situação eu realizei uma atualização do ambiente nuvem do cliente e verifiquei se ele possuía todos os acessos a fornecedores na aba abaixo:

!image-2024-10-15-13-31-48-850.png!

Então após fazer esse procedimento, eu validei novamente os indicadores do mês atual usando o usuário sysmax e os dados foram apresentados normalmente, tanto na venda transmitida quanto na faturada para a Filial 5.

Outro detalhe, eu removi a licença do sysmax e coloquei novamente na aba de versões porque como ele tem dois ambientes, às vezes pode ocorrer algum problema ao fazer a troca de licenças para usar nos ambientes.

Se algum outro usuário do cliente ainda não estiver apresentnado dados, pode ser alguma questão de permissão de acesso no perfil do usuário específico.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 400920
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A indisponibilidade dos indicadores da Filial 5 no Painel Geral não foi confirmada como falha de dados nas tabelas consultadas. | A análise aponta para possível questão de permissão/acesso do usuário, incluindo acessos a fornecedores, e também possível impacto de licença do usuário `sysmax` em cenário com dois ambientes. | Como os indicadores foram exibidos normalmente com o usuário `sysmax`, a causa mais provável deixa de ser ausência de dados da filial. | Inconsistência de licença no uso do `sysmax` entre os dois ambientes. | Atualizar o ambiente nuvem do cliente. | Não foi identificado exatamente qual permissão estaria ausente no perfil do usuário afetado. | A possibilidade de falha na troca de licenças entre os dois ambientes foi registrada, porém sem detalhamento da condição exata. | Referência ao `Painel Geral`. | Referência a falha de dados nas tabelas consultadas.
