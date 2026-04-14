# GATE-722 - Quantidade de vendidos no mês não aparece na APK.

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Protheus
- Assunto: MXPED - Parametrização
- Natureza: Dúvida
- Atualizado em: 2025-02-03T09:54:50.489-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxPedido;
>> Iniciar pedido para cliente '05585470   0001' e filial '0101010';
>> Listar produtos;

## Resultado apresentado
Nenhum produto apresenta a informação de vendidos nos meses anteriores.

## Resultado esperado
Listagem de produtos exibindo as informações de vendidos nos meses anteriores.

## Descrição
A informação de quantidade de vendidos nos meses não está sendo exibida na APK. Atualmente nem os meses zerados são exibidos, apenas a informação "Sem venda registrada nos últimos 3 meses".

Vou verificar nos tickets anteriores que foi passado para o cliente corrigir as informações das tabelas ERP_MXSMOV e ERP_MXSNFSAID, e os campos citados constam no banco nuvem, porem não reflete correção na APK.

Verifiquei em clientes que fizeram pedidos nos últimos meses, com retorno correto para o banco nuvem.

Listados produtos que foram positivados no período.

Parâmetro NUNCA_EXIBIR_QUANTIDADE_VENDA_MES = N.

Login: AGROSANDRI.RCA.

Ocorrendo em base do zero.

## Comentarios do Gatekeeper

### 1. 2025-02-03T09:54:50.487-0300 | Filipe do Amaral Padilha

Cenário do cliente '05585470   0001'
CODFILIAL '0101010'

Produtos vendidos nos últimos 3 meses:

ALFFDV003, ALFFDV009, ALFFDV005

Produtos abaixo não foram vendidos nesse cliente nos últimos 3 meses, segundo dados que temos na nuvem, então por isso não tem informação de qtd vendida:

BIOFVT015, MATTJK021, MATTJK022

--Regra que está impedindo a geração dos dados:
--ERP_MXSMOV.CODFILIAL = ERP_MXSNFSAID.CODFILIAL

Eles continuam enviando a informação do ERP_MXSMOV.CODFILIAL = NULL.

Para conferir:

SELECT CODFILIAL FROM ERP_MXSMOV WHERE NUMTRANSVENDA = 3962734;
SELECT CODFILIAL FROM ERP_MXSNFSAID WHERE NUMTRANSVENDA = 3962734;
--
SELECT CODFILIAL FROM ERP_MXSMOV WHERE NUMTRANSVENDA = 3972784;
SELECT CODFILIAL FROM ERP_MXSNFSAID WHERE NUMTRANSVENDA = 3972784;
--
SELECT CODFILIAL FROM ERP_MXSMOV WHERE NUMTRANSVENDA = 3980984;
SELECT CODFILIAL FROM ERP_MXSNFSAID WHERE NUMTRANSVENDA = 3980984;

Para resolver eles precisam enviar o código da filial corretamente seguindo a regra conforme expliquei.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 420846
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "A informação de vendidos nos últimos 3 meses não está sendo gerada" — o texto-fonte diz que há produtos vendidos nos últimos 3 meses; ele apenas informa que alguns produtos não têm informação de quantidade vendida e aponta uma regra impedindo a geração dos dados, sem especificar exatamente que "a informação de vendidos" como um todo não está sendo gerada. | "A correção é de responsabilidade do cliente" — o texto-fonte diz que "eles precisam enviar o código da filial corretamente", mas não afirma explicitamente responsabilidade do cliente.
