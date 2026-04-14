# GATE-286 - Falha acesso Max Gestão PWA via web

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: N/A
- Assunto: MXGESN - Não Acessando
- Natureza: Dúvida
- Atualizado em: 2024-11-06T18:04:51.713-0300

## Contexto do Problema

## Passos para reproduzir
acessar https://maxgestao-pwa.solucoesmaxima.com.br/ e tentar o login com a seguinte credencial
login: vjr.gestao
senha: Gestao@2024
observar os resultados

## Resultado apresentado
falha de acesso via PWA através da web

## Resultado esperado
que  o acesso ocorra normalmente sem falhas

## Descrição
Senhores, estão acontecendo as seguintes falhas de acesso ao PWA via web em alguns momentos:

!image-2024-11-06-10-52-12-168.png!

onde mesmo que o usuário esteja ativo e acessando o appsv e com versão liberada:

!image-2024-11-06-10-53-02-594.png!

ocorre falha no login

!image-2024-11-06-10-53-40-431.png!

## Comentarios do Gatekeeper

### 1. 2024-11-06T17:10:47.280-0300 | Filipe do Amaral Padilha

Foi alinhado com o P.O Thiago Castro que esses problemas de 401 e também de falha de autenticação ao tentar usar o PWA no comuputador como se fosse WEB é considerado normal. No caso o PWA mobile está acessando normalmente.
Nessa segunda será lançada uma versão do PWA para WEB e então vai normalizar esses acessos web, até isso ocorrer nós recomedamos usar o maxGestão WEB acessando pelo portal appsv mesmo para computador e para celular usar o PWA que seria o correto.

## Resposta Canonica

A falha de acesso ocorre porque o PWA está sendo utilizado no computador como se fosse uma aplicação WEB, antes do lançamento da versão WEB do PWA. Nesse cenário, os retornos 401 e as falhas de autenticação são considerados comportamentos esperados, conforme alinhado com o P.O. Thiago Castro.

Pontos validados:
- O acesso pelo PWA mobile está funcionando normalmente.
- A limitação ocorre especificamente no uso do PWA em computador como se fosse WEB.
- Até o lançamento da versão WEB do PWA, os acessos web por esse caminho não estão normalizados.

Orientação:
- Para uso em computador, acessar o maxGestão WEB pelo portal Appsv.
- Para uso em celular, utilizar o PWA.
- Aguardar o lançamento da versão do PWA para WEB, previsto para segunda-feira, quando os acessos web deverão ser normalizados.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 405399
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
