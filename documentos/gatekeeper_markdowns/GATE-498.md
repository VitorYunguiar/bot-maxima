# GATE-498 - Ocultar aba títulos pendentes

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Títulos
- Natureza: Dúvida
- Atualizado em: 2024-12-13T10:55:48.818-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Ir na tela de clientes
>>Clicar em qualquer cliente
>>Ir na aba de títulos pendentes

Logo o cliente quer ocultar essa aba de títulos pendentes.

usuário: pwclub.geovanna
Senha: asd123

## Resultado apresentado
Aba de títulos pendentes está aparecendo no aplicativo

## Resultado esperado
Que oculto a aba de títulos pendentes

## Descrição
O cliente gostaria de ocultar no cadastro do cliente a aba de títulos pendentes. Gostaria de saber se é possível ocultar.

## Comentarios do Gatekeeper

### 1. 2024-12-13T10:55:48.817-0300 | Filipe do Amaral Padilha

CLIENTE_EXIBIR_TITULOS - existe o parâmetro e ele oculta a aba de Títulos ao apertar para ver informações do cliente (antes de iniciar o pedido)

Parâmetro deve ser configurado CLIENTE_EXIBIR_TITULOS = Não para ocultar;

Depois de alterar lembre de sincronziar para validar no maxPedido

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 412115
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma que é possível ocultar a aba de títulos pendentes no aplicativo; o texto-fonte menciona apenas a aba de Títulos nas informações do cliente antes de iniciar o pedido, sem especificar 'títulos pendentes' nem generalizar para o aplicativo como um todo. | A resposta traz 'Causa identificada: A aba está sendo exibida porque o parâmetro CLIENTE_EXIBIR_TITULOS não está configurado como Não.' O texto-fonte informa como ocultar a aba, mas não afirma a causa do problema atual.
