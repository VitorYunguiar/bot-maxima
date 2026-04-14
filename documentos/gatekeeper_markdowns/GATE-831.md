# GATE-831 - Supervisor não aparece no painel de auditoria

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Mariel Araujo Souza
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria
- Natureza: Erro
- Atualizado em: 2025-02-20T15:23:20.751-0300

## Contexto do Problema

## Passos para reproduzir
Entra no MAXGESTÃO---GEOLOCALIZAÇÃO---PAINEL DE AUDITORIA

Seleciona a filial 1
Supervisor: era para aparecer o 2500-PAULO CEZAR REIS DO AMARAL

## Resultado apresentado
Não aparece o supervisor

## Resultado esperado
Que fosse possivel selecionar o supervisor

## Descrição
O supervisor 2500-PAULO CEZAR REIS DO AMARAL não aparece no painel de auditoria para visualizar.

Foi visto as permissões e os usuários tem acesso ao supervisor, mesmo assim não aparece.

## Comentarios do Gatekeeper

### 1. 2025-02-20T15:23:20.749-0300 | Filipe do Amaral Padilha

No maxGestão (Painel de Auditoria) existe uma regra onde, os usuários são apresentados conforme a filial vinculada no RCA do Supervisor.
Abaixo vou explicar com exemplo para ficar mais claro:

Na tabela MXSSUPERV existe o campo COD_CADRCA que é o usuário de vendas vinculado ao supervisor.

No Painel de Auditoria todo Supevisor precisa ter seu usuário de vendas vinculado senão não carrega ele para ser selecionado no Painel.

Esse campo COD_CADRCA referencia o CODUSUR da outra tabela MXSUSUARI.

Além do vínculo que comentei, precisa ter outra configuração na tabela MXSUSUARI.

O campo CODFILIAL da MXSUSUARI deve ser preenchido com o código da filial específica, ou se não tiver uma filial específica do usuário, pode ser o código 99 que indica todas as filiais.

Compara como exemplo, dessa forma:

SELECT * FROM MXSSUPERV WHERE CODSUPERVISOR IN(2500,1000);
SELECT * FROM MXSUSUARI WHERE CODUSUR IN(1000, 2500);

O supervisor 1000 é um que aparece normalmente porque segue esses critérios, então o 2500 precisa desses ajustes no cadastro.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 425622
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: O supervisor 2500 - PAULO CEZAR REIS DO AMARAL não é exibido no Painel de Auditoria porque o carregamento dos supervisores depende de critérios de cadastro vinculados à filial. | Ajustar o cadastro do supervisor 2500 na tabela MXSSUPERV, garantindo vínculo de usuário de vendas no campo COD_CADRCA. | Comparar o cadastro do supervisor 2500 com o do supervisor 1000 nas tabelas MXSSUPERV e MXSUSUARI e corrigir COD_CADRCA e CODFILIAL conforme necessário para que o supervisor 2500 seja carregado no Painel de Auditoria.
