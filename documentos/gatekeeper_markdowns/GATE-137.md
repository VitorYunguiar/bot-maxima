# GATE-137 - Transferência de flex

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Pedro Henrique Rodrigues Moura
- ERP do cliente: Winthor
- Assunto: MXGESN - Conta Corrente - Transferência de Saldo
- Natureza: Dúvida
- Atualizado em: 2024-10-03T17:44:45.308-0300

## Contexto do Problema

## Passos para reproduzir
- Login: caete.fabiano
- Senha: Fabiano123

>> Acessar MaxGestão WEB ou APP;
>> Conta Correte / Gestão de conta corrente;
>> Procurar usuário Edcarlos;

## Resultado apresentado
>> Não apresenta o Edcarlos;

## Resultado esperado
>> Visto que o representante Edcarlos é vinculado ao seu usuário de supervisor, e o Fabiano tem acesso a sua equipe no seu perfil, logo era para aparecer no MaxGestão;

## Descrição
Usuário Fabiano não está tendo acesso ao saldo CC do Edcarlos, para fazer transferência de de conta correte;

## Comentarios do Gatekeeper

### 1. 2024-10-03T17:43:25.885-0300 | Filipe do Amaral Padilha

Como o RCA EDCARLOS (como RCA) não tem nenhuma licença do maxPedido, então ele é considerado um "Usuário Geral" no maxGestão, e para movimentar o conta corrente dele usando o maxGestão, então o usuário do fabiano no maxGestão, precisa ter a permissão "Permite movimentar Conta Corrente do Usuário Geral para Vendedores" que fica localizada em Usuários >> Editar >> Permissões >> Conta Corrente >> Permite movimentar Conta Corrente do Usuário Geral para Vendedores

Com essa permissão, na aba de Gerenciar Conta corrente ele vai conseguir ver o usuário EDCARLOS como RCA para movimentar o conta corrente dele.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 398882
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A ausência do EDCARLOS na gestão de conta corrente é compatível com a falta dessa permissão no perfil do Fabiano. | Sem ela, o maxGestão não exibe o usuário EDCARLOS como RCA para movimentação de conta corrente. | Após habilitar a permissão, acessar a aba Gerenciar Conta corrente e validar se o usuário EDCARLOS passa a aparecer como RCA para movimentação. | Responsável: Administração de permissões do usuário Fabiano no maxGestão.
