# GATE-566 - Política não apresentada

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Política de Desconto - Comercial
- Natureza: Dúvida
- Atualizado em: 2025-01-02T15:40:07.891-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do rca, iniciar o pedido no cliente 512, filial 4 e acessar o produto 1009, verificando as políticas vinculadas a ele.

## Resultado apresentado
É verificado que a aplicação não exibe nenhuma política para o produto.

## Resultado esperado
É esperado que a política seja exibida corretamente.

## Descrição
Cliente relata que as políticas comerciais cadastradas no Winthor não estão sendo exibidas no maxPedido.
Foi realizado teste com a política 37800, que está disponível para os vendedores do supervisor 15 e clientes com o codatv1 = 20. No teste, foi utilizado o cliente 512 que está no codatv1 20 e o RCA 258, que pertence a equipe do supervisor 15, verificando o produto 1009.
No teste, foi verificado que a política não é carregada para o produto, mesmo que esteja no período de vigência definido para a política. O teste foi realizado em base zero e verificado que a política consta no banco do apk.

Os testes foram realizados em base zero.

OBS: O cliente realiza alterações diretamente via banco, foi orientado que não é um processo correto e que pode gerar problemas de sincronização do banco local com o nuvem. Talvez seja necessário realizar uma carga manual das políticas de desconto.

Login para teste:
mix.258

## Comentarios do Gatekeeper

### 1. 2025-01-02T15:39:20.471-0300 | Filipe do Amaral Padilha

Será enviado para N3 porque constatei no SQL que carrega as políticas, uma situação onde só exibe a política caso o campo CODPROD e COGRUPO estejam preenchidos na MXSDESCONTO. No caso, somente o CODGRUPO está preenchido e o CODPROD NULL com isso, a política não é exbida, e no momento esse comportamento diverge do Winthor 316

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414538
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que 'a política não é exibida no maxPedido' não está explicitamente mencionada no texto-fonte; o texto apenas diz 'a política não é exibida'. | A seção 'Evidência da análise' introduz uma formulação interpretativa e o bloco de pseudo-SQL não está presente literalmente no texto-fonte. | 'Ação recomendada: Encaminhar para o N3 para análise da divergência de comportamento e tratamento da regra de exibição da política' extrapola o texto-fonte, que apenas diz 'Será enviado para N3'.
