# GATE-550 - Carga de dados - PCTABTRIB

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Tributação
- Natureza: Dúvida
- Atualizado em: 2024-12-26T08:18:26.938-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do vendedor, iniciar um pedido em um cliente qualquer, adicionar o produto 34119.

## Resultado apresentado
Ao inserir, é apresentado erro de tributação

## Resultado esperado
É esperado que o produto seja carregado normalmente, conforme rotina 316 do Winthor.

## Descrição
Cliente relata que ao inserir o produto 34119, é apresentado um erro de tributação.
Ao verificar na MXSTABTRIB, a tributação para o produto não existe, mas ao verificar na PCTABTRIB, a tributação consta para o produto, sendo necessário realizar a carga da tabela em questão.

Login para teste:

piarara.227

## Comentarios do Gatekeeper

### 1. 2024-12-26T08:17:56.726-0300 | Filipe do Amaral Padilha

Registro não havia integrado na nuvem provavelmente porque o produto estava inativo, com DTEXCLUSAO preenchido, marcado para ENVIARFORCAVENDAS = N, com REVENDA = N ou com OBS marcado = 'PV'; Dai o cliente mexeu na tributação primeiro e depois ativou o produto, com isso a tributação não sobe.

O ideal nesse cenário era o próprio cliente só alterar a tributação novamente, para ela integrar naturalmente. Mas para facilitar a gente fez a carga da PCTABTRIB completa, todas as filiais seguindo os critérios que citei acima, somente produtos ativos e que podem ser vendidos tiveram a tributação integrada.

### 2. 2024-12-26T08:18:26.938-0300 | Filipe do Amaral Padilha

Produto integrado com sucesso
{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSTABTRIB{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODPROD{color} {color:#739eca}IN{color}({color:#c0c0c0}34119{color}){color:#eecc64};{color}

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 413855, 413856
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'na MXSTABTRIB, a tributação do produto não existia antes da carga' não está explicitamente informado no texto-fonte. | 'na PCTABTRIB, a tributação constava para o produto' não está explicitamente informado no texto-fonte. | 'Validar se o produto 34119 está disponível no pedido sem erro de tributação após a integração' não consta no texto-fonte.
