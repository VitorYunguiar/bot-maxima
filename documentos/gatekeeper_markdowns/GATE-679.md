# GATE-679 - Após a carga das filiais 4, 5, 34 e 35 produtos carregam preço infinito

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: João Pedro Faria Cabral [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Erro
- Atualizado em: 2025-01-23T15:55:28.912-0300

## Contexto do Problema

## Passos para reproduzir
108459 || grupogeb.elilson-mendonca || 222

SELECT * FROM mxstabprcli WHERE CODFILIALNF IN (4,5,34,35);

## Resultado apresentado
Foi feita uma carga das filiais 4, 5, 34 e 35, no entanto mesmo tendo produto nas filiais 34 e 35 o preço não carrega

## Resultado esperado
CARGA

## Descrição
As filiais 4 e 5 carregam os produtos normal, mas as filiais 34 e 35 carregam os produtos infinitamente

## Comentarios do Gatekeeper

### 1. 2025-01-23T15:55:28.909-0300 | Filipe do Amaral Padilha

Foi realizada carga das filiais novas 4, 5, 34 e 35 e já foi finalizada, o cliente pode estar validando testando realizar pedidos nessas filiais via maxPedido e comparando preços e estoques dos produtos em relação ao Winthor.

## Resposta Canonica

Foi realizada a carga das filiais 4, 5, 34 e 35, e o processo já foi finalizado.

No momento, a validação indicada é de responsabilidade do cliente, realizando testes de pedidos via **maxPedido** nas filiais **4, 5, 34 e 35**, com comparação de **preços e estoques** dos produtos em relação ao **Winthor**.

**Próximo passo:**  
Validar os pedidos nas filiais 4, 5, 34 e 35 via maxPedido e comparar os preços e estoques com o Winthor.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 418711
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
