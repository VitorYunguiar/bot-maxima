# GATE-812 - Relatório Clientes sem vendas não gera dados

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatórios
- Natureza: Dúvida
- Atualizado em: 2025-02-17T15:16:19.865-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar portal executivo;
>> Buscar relatório de clientes sem vendas;
>> tentar gerar relatório.

## Resultado apresentado
Não é gerado nenhum dado para nenhum filtro inserido.

## Resultado esperado
Relatório gerando dados.

## Descrição
Subindo gate depois de alinhado com o gatekeeper Filipe Padilha.

Ao tentar gerar o relatório de Clientes sem vendas no portal executivo do maxGestão, independente dos filtros escolhidos não é gerado nenhum dado no relatório.

Login: himalaia.2500
Senha: paulo2500

## Comentarios do Gatekeeper

### 1. 2025-02-17T15:16:19.862-0300 | Filipe do Amaral Padilha

O relatório 'Relatório Clientes sem vendas' inicialmente utiliza essa consulta para carregar o grid de informações:

SELECT DISTINCT mxsclient.codcli,P.codusur,P.codsupervisor, mxsclient.cliente, mxsclient.fantasia,mxsclient.telent,
mxsclient.dtultcomp, mxsclient.bloqueio,mxsclient.obs, mxspraca.praca
FROM mxsclient,
mxspraca,
mxsusuari P,
mxsvclientesrca,
mxshistoricopedc
WHERE mxspraca.codpraca = mxsclient.codpraca
AND mxsclient.codcli = mxsvclientesrca.codcli
AND P.codusur = mxsvclientesrca.codusur
AND P.codsupervisor IN (SELECT keydados
FROM mxacessodados
WHERE coddados = 5
AND codusuario = :codusuario)
AND TRUNC(MXSHISTORICOPEDC.data) BETWEEN TO_DATE('01/02/2025','DD/MM/YYYY') AND TO_DATE('14/02/2025','DD/MM/YYYY')
AND ((trunc(sysdate) - MXSHISTORICOPEDC.data) <= :VNUMDIAS)
ORDER BY mxsclient.cliente;

Nessa consulta, se você preencher e executar ela, verá que o codusuario 107133 não retorna dados. Isso ocorre porque ele só possui acesso à equipe 2700.

Nessa equipe 2700, só tem 1 RCA vinculado, e esse RCA não possui vendas registradas em históricos.

Se você pegar por exemplo o nosso usuário sysmax e utilizar o mesmo relatório, verá que carregam dados, porque o Sysmax possui acesso à todas as equipes que possuem RCAs com vendas.

Possível solução:

O usuário precisa ter acesso a equipes onde existam RCAs vinculados a clientes e esses RCAs tenham vendido para os clientes, porque o que o relatório basicamente faz, é analisar os históricos de vendas dos RCAs, considerando, Supervisor e clientes.

Outra coisa que eu observei, o usuário em questão é o HIMALAIA.2500 PAULO CEZAR REIS DO AMARAL e nas permissões dele, ele só possui acesso à equipe 2700, sendo que a equipe dele próprio, seria a 2500, talvez se só mudar essa permissão, ele já consiga tirar o relatório que precisa.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 424503
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Para :codusuario = 107133, a consulta de acesso não retorna dados compatíveis para geração do relatório." — O texto-fonte diz que o usuário 107133 não retorna dados no relatório porque só possui acesso à equipe 2700, mas não afirma especificamente que a subconsulta de acesso 'não retorna dados compatíveis'. | "Conceder acesso a equipes que possuam RCAs vinculados a clientes com histórico de vendas." — Embora alinhado à 'possível solução', isso é formulado como recomendação imperativa e não exatamente como fato já estabelecido no texto-fonte. | "Após o ajuste de permissões, retestar a emissão do relatório para confirmar se passam a existir dados retornados." — Próximo passo sugerido não está presente no texto-fonte.
