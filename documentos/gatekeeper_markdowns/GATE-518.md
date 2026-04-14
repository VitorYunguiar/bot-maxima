# GATE-518 - Central de configurações não retorna usuários

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Central de Configurações
- Natureza: Dúvida
- Atualizado em: 2024-12-17T15:42:22.332-0300

## Contexto do Problema

## Passos para reproduzir
Acessar central de configurações do maxPedido > Cadastros > Usuários

## Resultado apresentado
mensagem de erro informando "Usuário com login ja existente tioluiz.1004"

## Resultado esperado
Tela padrão de listagem dos usuários

## Descrição
Ao entrar na tela de cadastros da central de configurações não é apresentado nenhum usuário e retorna uma mensagem de erro informando "Usuário com login ja existente tioluiz.1004".

## Comentarios do Gatekeeper

### 1. 2024-12-17T15:42:22.330-0300 | Filipe do Amaral Padilha

Foi verificado que já ocorreu um erro assim anteriormente no MXPEDDV-78789 e foi tratado em N3 porque precisa ter acesso provavelmente ao banco Postgress para normalizar.

Então será encaminhado para N3

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 412708
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: O erro ao acessar Central de Configurações > Cadastros > Usuários | com a mensagem “Usuário com login já existente tioluiz.1004” | Há indicação de que a correção depende de normalização com acesso ao banco Postgress | A atuação fica condicionada a acesso ao banco Postgress para normalização | Direcionar o caso ao N3 para normalização em banco
