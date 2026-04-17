# GATE-47 - Preço Fixo não valida para Filial 07

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Pedro Henrique Rodrigues Moura
- ERP do cliente: Winthor
- Assunto: MXPED - Política de Desconto - Preço Fixo
- Natureza: Dúvida
- Atualizado em: 2024-09-11T13:11:50.982-0300

## Contexto do Problema

## Passos para reproduzir
- Login: comercialp.lfloriano

- Iniciar Pedido P/ Cliente: 4924;
- Filial 07;
- Produto: 8153;
- +Info / Politicas Comerciais;

## Descrição
- O preço fixo para o produto 8153 destinado a filial 07 e 50, não está sendo apresentado no APP;

- Foi feita a atualização do ambiente nuvem e local do cliente, no qual estava divergênte e nesse processo o preço fixo para filial 50 tornou a validar, porém para filial 07, mesmo com registro na base do RCA, não é apresentado;

## Comentarios do Gatekeeper

### 1. 2024-09-11T13:11:37.923-0300 | Filipe do Amaral Padilha

O problema ocorre porque ao trocar a filial de venda de 50 para 7, "por baixo dos panos", a filialNF não é alterada junto.

Na prática o que ocorre é o pedido inicia na filial 50 com filialnf 50. Quando o RCA troca para filial 7, a filialnf continua na 50. Com isso, a política de preço fixo não é validada porque a filial de venda é 7, mas a filialnf sendo 50, busca dados da região 50.

O responsável por mudar esse comportamento, é o parâmetro IGUALAR_FILIALNF_AO_ALTERAR_FILIAL que não está cadastrado para todos os RCAs nesse cliente. Verifique no bd nuvem:
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%IGUALAR_FILIALNF_AO_ALTERAR_FILIAL%';

Então uma das opções que eles tem para resolver essa situação é ativar esse parâmetro, colocando ele IGUALAR_FILIALNF_AO_ALTERAR_FILIAL = S.

Uma recomendação minha, nem precisa avisar ao cliente porque não vai ter impactos negativos. Desativar o parâmetro FILIALNF_DEFINE_FILIAL_PEDIDO.

Se o cliente quiser também optar por selecionar a filialnf nos pedidos, ele pode habilitar a permissão para os RCAs: "Permitir escolha da filial de emissão da NF"

Não vai ter impacto para esse cliente configurar o sistema dessa forma, porque ele não usa filialnf nos cadastros dos clientes dele.
Eu validei assim:
SELECT * FROM MXSCLIENT WHERE CODFILIALNF IS NOT NULL AND CODOPERACAO <> 2;

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, needs_review
- Comentarios primarios: 393985
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
