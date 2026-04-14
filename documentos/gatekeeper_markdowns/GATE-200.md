# GATE-200 - Painel de Auditoria não exibe filial 1 e 5

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria
- Natureza: Dúvida
- Atualizado em: 2024-10-18T07:35:42.280-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar maxGestão da GP DONIZETE WINTHOR
>Geolocalização
>Painel de Auditoria
>Tentar filtrar filial 5 ou 1

## Resultado apresentado
Mesmo o usuário sysMax tendo permissão de acesso para todas as filiais, elas não são apresentadas nos filtros.

na MXSUSUARI existem RCAs vinculados a filial 5 e com supervisores também vinculados e ativos.

## Resultado esperado
Entender o motivo de não apresentar as outras filiais.

## Descrição
Boa tarde Filipe, estou com uma situação no maxGestão onde no painel de auditoria não aparece as filiais 1 e 5, fiz uma validação na MXSUSUARI e MXSSUPERV e os vinculos com a filial 5 estão feitos normalmente, não consgui identificar o motivo de não exibir as outras filiais.

## Comentarios do Gatekeeper

### 1. 2024-10-18T06:19:38.764-0300 | Filipe do Amaral Padilha

*Não passar as querys para o cliente são dados sensíveis nossos*

A Query definitiva é essa:
{color:#739eca}SELECT{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}AS{color} {color:#00b8b8}CODIGO{color},

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}RAZAOSOCIAL{color} {color:#00b8b8}DESCRICAO{color}

{color:#739eca}FROM{color} {color:#b788d3}MXSUSUARI{color}

{color:#739eca}INNER{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSSUPERV{color} {color:#b788d3}S{color}

{color:#739eca}ON{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODSUPERVISOR{color} = {color:#b788d3}S{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#739eca}LEFT{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSFILIAL{color}

{color:#739eca}ON{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} = {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODFILIAL{color}

{color:#739eca}WHERE{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color} ({color:#739eca}SELECT{color} {color:#00b8b8}KEYDADOS{color} {color:#739eca}FROM{color} {color:#b788d3}MXACESSODADOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDADOS{color} = {color:#cac580}'6'{color} {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} = {color:#7ebad3}:CODUSUARIO{color})

{color:#739eca}AND{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODSUPERVISOR{color} {color:#739eca}IN{color} ({color:#739eca}SELECT{color} {color:#00b8b8}KEYDADOS{color} {color:#739eca}FROM{color} {color:#b788d3}MXACESSODADOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDADOS{color} = {color:#cac580}'5'{color} {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} = {color:#7ebad3}:CODUSUARIO{color} )

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} <> {color:#cac580}'0'{color}

{color:#739eca}AND{color} {color:#9e9e9e}FUNCAO_INDICE{color} ({color:#00b8b8}CODFILIAL{color}) {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#9e9e9e}FUNCAO_INDICE{color} ({color:#00b8b8}DTTERMINO{color}) {color:#739eca}IS{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}BLOQUEIO{color} = {color:#cac580}'N'{color}

{color:#739eca}AND{color} {color:#b788d3}S{color}.{color:#00b8b8}COD_CADRCA{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}GROUP{color} {color:#739eca}BY{color} {color:#00b8b8}CODIGO{color}, {color:#00b8b8}RAZAOSOCIAL{color}{color:#eecc64};{color}

O código de usuário do sysmax é
{color:#669768}--82572{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSUSUARIOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}NOME{color} {color:#739eca}LIKE{color} {color:#cac580}'%Sys%'{color}{color:#eecc64};{color}

Caso você queria rodar a Query no bd deles;

O que a Query faz?
R: Ela busca os RCAs vinculados aos supervisores pelo codsupervisor e verifica se a filial cadastrada existe na MXSFILIAL para ser apresentada. A base da consulta é essa:
{color:#739eca}SELECT{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}AS{color} {color:#00b8b8}CODIGO{color},

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}RAZAOSOCIAL{color} {color:#00b8b8}DESCRICAO{color}

{color:#739eca}FROM{color} {color:#b788d3}MXSUSUARI{color}

{color:#739eca}INNER{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSSUPERV{color} {color:#b788d3}S{color}

{color:#739eca}ON{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODSUPERVISOR{color} = {color:#b788d3}S{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#739eca}LEFT{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSFILIAL{color}

{color:#739eca}ON{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} = {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODFILIAL{color}

Abaixo então eu peguei a mesma base e só editei colocando mais informações e também adicionando apenas uma clásula WHERE para você visualizar que não tem nenhum RCA vinculado em outras filiais a não ser a 4 e a 5:
{color:#739eca}SELECT{color}

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}AS{color} {color:#00b8b8}CODIGO{color},

{color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}RAZAOSOCIAL{color} {color:#00b8b8}DESCRICAO{color},

{color:#b788d3}S{color}.{color:#00b8b8}CODSUPERVISOR{color},

{color:#b788d3}S{color}.{color:#00b8b8}COD_CADRCA{color},

{color:#b788d3}S{color}.{color:#00b8b8}NOME{color},

{color:#b788d3}U{color}.{color:#00b8b8}CODUSUR{color},

{color:#b788d3}U{color}.{color:#00b8b8}NOME{color},

{color:#b788d3}U{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#739eca}FROM{color} {color:#b788d3}MXSUSUARI{color} {color:#b788d3}U{color}

{color:#739eca}INNER{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSSUPERV{color} {color:#b788d3}S{color}

{color:#739eca}ON{color} {color:#b788d3}U{color}.{color:#00b8b8}CODSUPERVISOR{color} = {color:#b788d3}S{color}.{color:#00b8b8}CODSUPERVISOR{color}

{color:#739eca}LEFT{color} {color:#739eca}JOIN{color} {color:#b788d3}MXSFILIAL{color}

{color:#739eca}ON{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} = {color:#b788d3}U{color}.{color:#00b8b8}CODFILIAL{color}

{color:#739eca}WHERE{color} {color:#b788d3}U{color}.{color:#00b8b8}CODFILIAL{color} {color:#739eca}NOT{color} {color:#739eca}IN{color}({color:#c0c0c0}4{color},{color:#c0c0c0}5{color}){color:#eecc64};{color}

Mas e porque se tem a 5 não mostra ela?

Por causa das outras clásulas que estão no WHERE da consulta principal e original:
{color:#739eca}WHERE{color} {color:#00b8b8}CODFILIAL{color} {color:#739eca}IN{color} ({color:#739eca}SELECT{color} {color:#00b8b8}KEYDADOS{color} {color:#739eca}FROM{color} {color:#b788d3}MXACESSODADOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDADOS{color} = {color:#cac580}'6'{color} {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} = {color:#7ebad3}:CODUSUARIO{color})

{color:#739eca}AND{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}CODSUPERVISOR{color} {color:#739eca}IN{color} ({color:#739eca}SELECT{color} {color:#00b8b8}KEYDADOS{color} {color:#739eca}FROM{color} {color:#b788d3}MXACESSODADOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDADOS{color} = {color:#cac580}'5'{color} {color:#739eca}AND{color} {color:#00b8b8}CODUSUARIO{color} = {color:#7ebad3}:CODUSUARIO{color} )

{color:#739eca}AND{color} {color:#00b8b8}CODFILIAL{color} <> {color:#cac580}'0'{color}

{color:#739eca}AND{color} {color:#9e9e9e}FUNCAO_INDICE{color} ({color:#00b8b8}CODFILIAL{color}) {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#9e9e9e}FUNCAO_INDICE{color} ({color:#00b8b8}DTTERMINO{color}) {color:#739eca}IS{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#b788d3}MXSUSUARI{color}.{color:#00b8b8}BLOQUEIO{color} = {color:#cac580}'N'{color}

{color:#739eca}AND{color} {color:#b788d3}S{color}.{color:#00b8b8}COD_CADRCA{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}AND{color} {color:#b788d3}MXSFILIAL{color}.{color:#00b8b8}CODIGO{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color}

{color:#739eca}GROUP{color} {color:#739eca}BY{color} {color:#00b8b8}CODIGO{color}, {color:#00b8b8}RAZAOSOCIAL{color}{color:#eecc64};{color}

Especificamente a regra {color:#cccccc} AND{color} {color:#b788d3}S{color}.{color:#00b8b8}COD_CADRCA{color} {color:#739eca}IS{color} {color:#739eca}NOT{color} {color:#739eca}NULL{color} que significa que todos os supervisores que estão vinculados a RCAs que estão na filial 5, não possuem essa informação COD_CADRCA na tabela MXSSUPERV deles. Então como é is not null, ele remove as filiais desses supervisores nessas condições, no caso a 5.

Então como o cliente pode fazer para resolver?

Eles podem estar resolvendo, vinculando os RCAs nas filiais que eles desejam que sejam apresentadas na MXSUSUARI Rotina 517 e elas precisam exisitir na MXSFILIAL 535 e estarem sendo integradas à Máxima. E eles precisam vincular esses RCAs na Rotina também 517 aos supervisores que existam na Rotina 516. E por fim, na Rotina 516 eles precisam vincular o Supervisor a um RCA, pode ser qualquer RCA, mas quem define essa regra de qual vai ser são eles (Geralmente os clientes colocam o próprio código de supervisor exemplo: Supervisor 10 código de RCA 10 – Eu acho mais correto porque fica organizado).

*Outra opção que eles tem:* Eles podem na rotina 517, colocar todos os RCAs sem exceção vinculados ao conceito de filial 99 (que pertencem a todas as filiais); – Não sei que impactos isso pode ter no Winthor. Mas aqui no Painel de Auditoria o que vai acontecer é que nenhuma filial mais será apresentada no filtro de filiais. Porém todos os supervisores estarão vinculados a filial 99 e serão exibidas todas as equipes ao apertar no filtro de supervisor. Assim meio que você intuiliza o filtro de filial já que os supervisores estão vinculadas à 99 (todas). E continua considerando a regra do COD_CADRCA, os supervisores precisam estar vinculados a alguma RCA próprio deles na 516.

## Resposta Canonica

Identificamos que a filial 5 não é exibida no filtro do Painel de Auditoria porque a consulta utilizada para montar a lista de filiais considera apenas registros que atendem, entre outras regras, ao critério de supervisor com `COD_CADRCA` preenchido. No cenário analisado, os supervisores vinculados aos RCAs da filial 5 não possuem essa informação na `MXSSUPERV`, o que exclui a filial do resultado.

Além disso, a análise dos vínculos mostrou que não há RCA vinculado em outras filiais além da 4 e da 5. A montagem do filtro também depende dos acessos do usuário em `MXACESSODADOS`, tanto para filial quanto para supervisor, e ainda exige que a filial seja válida, ativa e existente na `MXSFILIAL`, além de usuário não bloqueado e sem término.

Consulta base avaliada:
```sql
SELECT MXSFILIAL.CODIGO AS CODIGO, MXSFILIAL.RAZAOSOCIAL DESCRICAO
FROM MXSUSUARI
INNER JOIN MXSSUPERV S ON MXSUSUARI.CODSUPERVISOR = S.CODSUPERVISOR
LEFT JOIN MXSFILIAL ON MXSFILIAL.CODIGO = MXSUSUARI.CODFILIAL
WHERE CODFILIAL IN (
    SELECT KEYDADOS
    FROM MXACESSODADOS
    WHERE CODDADOS = '6'
      AND CODUSUARIO = :CODUSUARIO
)
AND MXSUSUARI.CODSUPERVISOR IN (
    SELECT KEYDADOS
    FROM MXACESSODADOS
    WHERE CODDADOS = '5'
      AND CODUSUARIO = :CODUSUARIO
)
AND CODFILIAL <> '0'
AND FUNCAO_INDICE(CODFILIAL) IS NOT NULL
AND FUNCAO_INDICE(DTTERMINO) IS NULL
AND MXSUSUARI.BLOQUEIO = 'N'
AND S.COD_CADRCA IS NOT NULL
AND MXSFILIAL.CODIGO IS NOT NULL
GROUP BY CODIGO, RAZAOSOCIAL;
```

Próximo passo recomendado:
- validar na `MXSSUPERV` os supervisores relacionados à filial 5 e preencher o `COD_CADRCA`;
- revisar os vínculos de RCAs, filiais e supervisores nas rotinas 517, 535 e 516.

Como alternativa, é possível vincular os RCAs à filial 99, porém essa configuração pode fazer com que nenhuma filial seja apresentada no filtro de filiais e com que o filtro de supervisor passe a exibir todas as equipes. Mesmo nessa alternativa, os supervisores continuam precisando estar vinculados a um RCA na rotina 516.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 401541
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
