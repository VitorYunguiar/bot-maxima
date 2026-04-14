# GATE-547 - produtos não aparecem - carga

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2024-12-23T12:42:29.210-0300

## Contexto do Problema

## Passos para reproduzir
Login: toledo.ernestopaes
Produto: 9075, 9076, 7, 9063, 9529, 9067, 5991

1 - Ir em produtos, selecionar filial 1 e pesquisar.

## Resultado apresentado
Apenas aparece 13 produtos, não são todos.

## Resultado esperado
Todos os 50 produtos que a base zerada nos mostra

## Descrição
Os produtos da filial 1 não estão aparecendo, a base do zero estão aparecendo os 50 produtos normalmente, porém, na base do RCA estão aparecendo apenas 13 (depois de ter feito uma carga interna)

## Comentarios do Gatekeeper

### 1. 2024-12-23T12:42:29.208-0300 | Filipe do Amaral Padilha

Realizei uma normalização de dados para liberar a RCA e permitir que ela consiga sincronizar e receber as informações dos produtos na base dela.

Então para resolver pode orientar a RCA a sincronizar.

--Não passar ao cliente esse detalhe abaixo:
Mesmo assim, vou enviar o ticket para N3 porque nos dados que verifiquei identifiquei um log de erro na sincronização.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 413644
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "permitir que a base consiga sincronizar e receber corretamente as informações dos produtos" — o texto-fonte diz que a RCA consiga sincronizar e receber as informações dos produtos na base dela; a formulação altera o sujeito e adiciona "corretamente". | "foi identificado um problema na sincronização" — o texto-fonte menciona especificamente "um log de erro na sincronização", não um problema de forma genérica. | "o que justifica o encaminhamento para tratativa especializada" — a justificativa e a expressão "tratativa especializada" não aparecem no texto-fonte. | "Encaminhar o ticket para o N3 para continuidade da análise" — o texto-fonte diz que o ticket será enviado para N3 porque foi identificado um log de erro na sincronização; "continuidade da análise" não consta no texto-fonte.
