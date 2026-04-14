# GATE-464 - Erro na devolução do maxGestao

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral
- Natureza: Dúvida
- Atualizado em: 2024-12-05T17:04:32.087-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o 'prontu.admti' senha: 'lmhqeX8' (Ele tem acesso ao PWA)
>>Acessar o sysmax(Acesso ao maxGestão Web)
>>Pesquisar por data de faturamento
>>Dia 01 a 05
>>Selecionar uma equipe, ex. 7

## Resultado apresentado
>>O maxGestão exibe o valor de R$4.264,18 de devoluções, independente da equipe selecionada (A certa é a 1)
>>Ao clicar em "Deduzir devoluções" no PWA os valores ficam zerados e no WEB os valores desaparecem da tela.

## Resultado esperado
>>As devoluções no valor de R$4.264,18 devem aparecer para a equipe 1 apenas
>>O sistema deve mostrar o valor ao deduzir devoluções.

## Descrição
>>O valor de devolução que deveria ser apenas da equipe 1 aparece para todas as equipes

>>Ao colocar no maxGestao Web para deduzir as devoluções os valores somem da tela

>>Ao fazer o mesmo no PWA os valores ficam zerados

## Comentarios do Gatekeeper

### 1. 2024-12-05T17:04:32.086-0300 | Filipe do Amaral Padilha

Será enviado para N3 porque está com comportamento inconsistente

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
