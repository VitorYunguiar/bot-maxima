# GATE-716 - Embalagem divergente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Embalagem
- Natureza: Dúvida
- Atualizado em: 2025-01-30T15:18:01.704-0300

## Contexto do Problema

## Passos para reproduzir
Acessar o banco nuvem do cliente,  verificar o codauxiliar do produto na filial 3 e procurar pela embalagem 7899874103930, que está sendo enviada nos pedidos.

## Resultado apresentado
É verificado que a embalagem não consta na filial em questão, e que no Winthor a embalagem está inativa

## Resultado esperado
É esperado que seja enviada a embalagem correta dos produtos nos pedidos.

## Descrição
Cliente relata que ao enviar um pedido com o produto 733480, a integradora realiza o corte do produto e retorna a crítica de que a embalagem não é válida. Foi verificado que a situação ocorre pois a embalagem que está sendo enviada associada ao produto não está mais ativa no sistema, sendo necessário realizar uma carga de dados para normalizar o cenário e corrigir o codauxiliar dos produtos em questão.

## Comentarios do Gatekeeper

### 1. 2025-01-30T15:18:01.701-0300 | Filipe do Amaral Padilha

Foi realizada normalização das embalagens do cliente, todas as inativas foram setadas no banco nuvem corretamente para ficar espelhado com o banco local.

Embalagem
CODFILIAL 1	AUXULIAR 7899874103930	CODPROD 733480
setada para codoperacao = 2

SELECT * FROM MXSEMBALAGEM WHERE CODPROD IN(733480);

Para os RCAs validarem basta sincronizar o maxPedido

--Foram validados os logs e não foi identificada nenhuma causa em potencial para o ocorrido, por isso, coloquei los na TRIGGER que faz a replicação dos dados para a nossa nuvem para caso ocorra novamente, termos informações para analisar

## Resposta Canonica

Foi realizada a normalização das embalagens do cliente no banco nuvem, ajustando as embalagens inativas para espelhar o banco local. No caso validado, a embalagem **AUXULIAR 7899874103930** do produto **733480** na **CODFILIAL 1** foi definida com **codoperacao = 2**.

A validação indicou que não foi identificada causa potencial para a ocorrência nos logs analisados. Como medida de rastreabilidade, foram adicionados logs na trigger responsável pela replicação dos dados para a nuvem, para subsidiar nova análise caso o cenário volte a ocorrer.

SQL utilizada na validação:
```sql
SELECT * FROM MXSEMBALAGEM WHERE CODPROD IN(733480);
```

Ação recomendada: os **RCAs** devem sincronizar o **maxPedido** para validar a regularização. Se houver recorrência, a orientação é analisar os logs adicionados na trigger de replicação.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 420295
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
