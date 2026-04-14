# GATE-472 - Política de desconto não se aplica ao cliente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Política de Desconto - Comercial
- Natureza: Dúvida
- Atualizado em: 2024-12-10T14:11:39.205-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar a base do zero do RCA 103 ou base em anexo
>>Iniciar pedido para o cliente 1425
>>Clicar no produto 66060
>>Mais info> Políticas comerciais

## Resultado apresentado
>>É exibida mensagem que não existe política vigente para este produto
>>Na 316 como segue prints, a política é incluída automaticamente.

## Resultado esperado
>>As políticas de desconto devem ser validadas para o cliente

## Descrição
>>No maxPedido as políticas de desconto 7799 e 13723 da rotina 561 não aparecem para os clientes, ex. 1425 mesmo na base do zero

>>Produto 66060

>>RCA 103(uai.103)

>>Na 316 a política de desconto é aplicada ao cliente

>>Sem restrições de venda (Testei deletando via inspect)

## Comentarios do Gatekeeper

### 1. 2024-12-10T14:11:39.204-0300 | Filipe do Amaral Padilha

O problema ocorreu devido a falta de informações que não integraram para a nossa nuvem da tabela MXSGRUPOSCAMPANHAI.

Provavelmente era uma falha da versão antiga do banco de dados, porque esse cliente estava na versão 3.1.3.243, sendo que, foi atualizado a última vez em 2023.

Então para resolver eu atualizei o banco de dados deles e fiz carga das tabelas MXSGRUPOSCAMPANHAC e MXSGRUPOSCAMPANHAI.

Para validar no maxPedido basta realizar a sincronização.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 411367
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A ausência das políticas de desconto no maxPedido está associada à falta de informações da tabela MXSGRUPOSCAMPANHAI. | Esse cenário explica a não apresentação das políticas para o cliente no maxPedido. | Realizar a sincronização no maxPedido para confirmar se as políticas passam a ser exibidas corretamente.
