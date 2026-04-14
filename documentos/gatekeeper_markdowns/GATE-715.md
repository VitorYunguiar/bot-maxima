# GATE-715 - Graficos Desatualizados

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Gleiciellen Pereira Leal [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Timeline
- Natureza: N/A
- Atualizado em: 2025-01-30T08:28:54.848-0300

## Contexto do Problema

## Passos para reproduzir
>> Verificado que existem registros na ERP_MXSDATAS
>> Visto que existem registros no resumo de vendas
>> dois vendedores relataram o erro
>> login : Rafatiga.Antonio

## Resultado apresentado
>> Graficos não atualizam

## Resultado esperado
>> Graficos mostrando informações

## Descrição
Não aparece informações nos gráficos o numero de vendas, os itens vendidos e clientes atendidos,

## Comentarios do Gatekeeper

### 1. 2025-01-29T17:21:54.321-0300 | Filipe do Amaral Padilha

Dados corretos de conexão no cliente são:

RAFATIGA_3095_PRODUCAO
maxsolucoes-card.cm35ayc6yrqh.us-east-1.rds.amazonaws.com

identifiquei isso pelo ticket pai e também pelo login que existe na base citada e também é o mesmo do usuário logado, quando confere via inspect:

SELECT * FROM MXSUSUARIOS;

Dados do bd T-CLOUD:

189.126.154.116
CUG0DS_162882_W_high.paas.oracle.com
gdent17243ZRSPH@?

O gráfico do objetivo não atualiza porque o cliente não possui meta cadastrada para esse RCA.
Que seria a rotina 353 no Winthor.

SELECT * FROM PCMETARCA WHERE CODUSUR IN(2) ORDER BY DATA DESC;

Além disso, os demais gráficos não atualizam porque eles não possuem o cadastro na

SELECT * FROM PCDIASUTEIS ORDER BY DATA DESC;
e
SELECT * FROM PCDATAS ORDER BY DATA DESC;

Amanhã vou concluir a análise

### 2. 2025-01-30T08:28:54.843-0300 | Filipe do Amaral Padilha

Os dados que constam sobre o cliente no ticket estão parcialmente corretos:

Dados corretos de conexão no cliente são:

RAFATIGA_3095_PRODUCAO
maxsolucoes-card.cm35ayc6yrqh.us-east-1.rds.amazonaws.com

identifiquei isso pelo ticket pai e também pelo login que existe na base citada e também é o mesmo do usuário logado, quando confere via inspect:

SELECT * FROM MXSUSUARIOS;

Dados do bd T-CLOUD:

189.126.154.116
CUG0DS_162882_W_high.paas.oracle.com
gdent17243ZRSPH@?

O gráfico do objetivo não atualiza porque o cliente não possui meta cadastrada para esse RCA.
Que seria a rotina 353 no Winthor.

SELECT * FROM PCMETARCA WHERE CODUSUR IN(2) ORDER BY DATA DESC;

Além disso, os demais gráficos não atualizam porque eles não possuem o cadastro na PCDATAS para o ano e mês atual. (2025/01)

SELECT * FROM PCDATAS ORDER BY DATA DESC;

Depois de cadastrar a PCDATAS utilizando o Winthor, creio que a Rotina 309, poderá estar mandando atualizar o menu no maxPedido para conferir se os gráficos atualizam

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 420045, 420083
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma que os gráficos são do usuário **Rafatiga.Antonio**, mas o texto-fonte não menciona esse nome de usuário. | A resposta recomenda **cadastrar a meta do RCA na Rotina 353** do Winthor. O texto-fonte diz que a rotina 353 é a referente à meta, mas não explicita essa ação como recomendação. | A resposta inclui como ação recomendada **conferir se a Rotina 309 atualiza o menu no maxPedido**. No texto-fonte isso aparece como possibilidade conjectural ('creio que ... poderá estar mandando atualizar'), não como fato suportado. | A resposta apresenta a lista de consultas utilizadas incluindo **SELECT * FROM PCDIASUTEIS ORDER BY DATA DESC;** no contexto final da causa dos demais gráficos, mas no trecho consolidado do texto-fonte a causa final está associada apenas à **PCDATAS para o ano e mês atual (2025/01)**.
