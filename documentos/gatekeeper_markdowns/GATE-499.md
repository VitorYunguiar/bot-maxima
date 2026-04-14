# GATE-499 - Erro ao autorizar pedidos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXGESN - Autorização de Pedidos - Limite Créd. Excedido
- Natureza: Dúvida
- Atualizado em: 2024-12-13T14:29:04.983-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Cliente relata que ao tentar autorizar um determinado pedido, a aplicação do maxGestão retornou uma mensagem de rejeição, onde caso o saldo do supervisor seja exatamente igual ao saldo a ser autorizado, a autorização não é validada.
Foi realizado teste com o cliente, onde caso o mesmo passe $1 a mais, a aplicação permite a autorização.
Foi realizado contato com o desenvolvedor Elisberto que trata-se de um erro nas casas decimais, onde não é possível realizar a comparação correta dos valores.

USUÁRIO: cardoso.renan SENHA: asd123

## Comentarios do Gatekeeper

### 1. 2024-12-13T14:29:04.981-0300 | Filipe do Amaral Padilha

Será enviado para N3 todas as evidências ficaram bem consistentes e ótimas

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
