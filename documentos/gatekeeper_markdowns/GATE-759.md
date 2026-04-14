# GATE-759 - Erro ao inserir item

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Estoque
- Natureza: Dúvida
- Atualizado em: 2025-02-07T16:16:47.195-0300

## Contexto do Problema

## Passos para reproduzir
login: lpdi.186
Produto: 3614

Tentar inserir o produto em algum pedido, gerando a mensagem de "erro"

## Resultado apresentado
Mensagem presente nos anexos

## Resultado esperado
Conseguir inserir normalmente.

## Descrição
+texto sublinhado+Ao tentar inserir o item 3614 está tendo um erro, porém, na 316 está passando normalmente. Está ocorrendo com todos os usuários.

## Comentarios do Gatekeeper

### 1. 2025-02-07T16:16:47.194-0300 | Filipe do Amaral Padilha

Ao realizar o teste na versão 3.230.0 que o cliente está utilizando, de fato o problema ocorre, mas não deveria.

Então eu testei na versão 4.000.8 e funcionou normalmente, então isso quer dizer que houve correção para que o item fosse carregado com sucesso em versões posteriores à 3.230.0.

Nesse sentido, recomendo atualizar a versão do maxPedido para a 4, porém se o cliente quiser se manter na 3, ele pode atualizar para a 3.269.2 (última da v3) ou até anteriores como a 3.258.0, por exemplo

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 422467
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A causa do erro ao inserir o produto 3614 está relacionada à versão 3.230.0 do maxPedido utilizada pelo cliente. | O comportamento apresentado não está ligado a cadastro do produto ou usuário, mas à versão do sistema em uso pelo cliente. | orientar a atualização para a 3.269.2 ou outra versão posterior à 3.230.0 dentro da linha 3.
