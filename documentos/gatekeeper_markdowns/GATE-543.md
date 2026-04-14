# GATE-543 - Ocultar produtos com restrição de venda

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Restrições
- Natureza: Dúvida
- Atualizado em: 2024-12-20T16:00:30.502-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base do rca, iniciar um pedido em um cliente qualquer e filtrar pelos produtos do departamento 33, conforme restrição 3488

## Resultado apresentado
É verificado que os produtos são apresentados mesmo havendo a restrição

## Resultado esperado
É esperado que os produtos sejam ocultados devido a restrição

## Descrição
Cliente relata que ao cadastrar restrições na rotina 391, os produtos ainda são apresentados no maxPedido. A restrição cadastrada foi para o departamento 33 e supervisor 2, onde foi verificado que ao filtrar pelo departamento na aba 'Tabela' do maxPedido, os produtos continuam a ser apresentados normalmente.

Login para teste:
columbia.1322

## Comentarios do Gatekeeper

### 1. 2024-12-20T16:00:30.501-0300 | Filipe do Amaral Padilha

No maxPedido existe o parâmetro 'RESTRINGIR_PRODUTOS_391', que quando setado com valor = 'N' apresenta o produto e informa qual a restrição cadastrada e quando o parâmetro estiver = 'S', não exibe o produto por causa da restrição de venda.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 413495
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Pelos fatos analisados, a apresentação dos produtos do departamento 33, mesmo com restrição cadastrada na rotina 391, é compatível com o cenário em que o parâmetro esteja configurado como `N`." | "Validar no maxPedido o valor configurado para o parâmetro `RESTRINGIR_PRODUTOS_391` e, se o comportamento esperado for ocultar os produtos com restrição, ajustá-lo para `S`."
