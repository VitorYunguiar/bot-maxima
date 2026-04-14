# GATE-563 - Inconsistência de Dados

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Sankhya
- Assunto: MXPED - Plano de Pagamento
- Natureza: Dúvida
- Atualizado em: 2025-01-02T10:10:26.906-0300

## Contexto do Problema

## Passos para reproduzir
>>silbas.suzy
>Iniciar APK
>Clientes
>Tentar iniciar pedido no cliente 2922

## Resultado apresentado
Ao iniciar pedido é exibida uma mensagem informando que não foi possível iniciar o pedido devido a uma inconsistência nos dados, e que nenhum plano de pagamento pôde ser carregado para o pedido.

## Resultado esperado
Iniciar o pedido

## Descrição
Bom da Carlos / Filipe,

Preciso de ajuda para identificar um problema que está ocorrendo na SILBAS ao tentar iniciar um pedido para o cliente 2922. Durante o processo, é exibida uma mensagem informando que não foi possível iniciar o pedido devido a uma inconsistência nos dados, e que nenhum plano de pagamento pôde ser carregado para o pedido.

Realizei verificações preliminares nas tabelas MXSCLIENT e MXSPLPAGCLI e, em seguida, analisei os vínculos e as tabelas relacionadas aos planos e cobranças (MXSPLPAG e MXSCOB). Contudo, não consegui identificar a causa do problema.

## Comentarios do Gatekeeper

### 1. 2025-01-02T10:10:26.903-0300 | Filipe do Amaral Padilha

O plano de pagamento não carrega devido ao vínculo restritivo de plano e cobrança da tabela MXSCOBPLPAG.

No caso, o cliente 2922 inicia o pedido com o plano 15 e com a cobrança 2 (MXSCLIENT) e na tabela MXSCOBPLPAG a cobrança 2 só pode ser usada com o plano 11.

Para resolver nesse caso eu recomendo que o cliente altere no cadastro do cliente (MXSCLIENT), o plano para o 11. Vou explicar o motivo:

Ocorre que, não faz sentido vincular o plano 15 à cobrança 2, porque a cobrança é Dinheiro, que é utilizada para vendas A VISTA. Como no caso do plano 11 TIPOVENDA (VV)...

O plano 15 é do tipo venda a prazo, isso quem dita é o campo TIPOVENDA e também a descrição né, que é BOLETO 15 DIAS, ou seja, geralmente venda a prazo se utiliza com cobrança BOLETO mesmo.

Outra observação, a cobrança 15 já está vinculada na cobrança 4, se o RCA selecionar uma cobrança do tipo boleto (4), o plano 15 será exibido.

Consultas utilizadas:

SELECT CODCOB, CODCLI, CODPLPAG FROM MXSCLIENT WHERE CODCLI IN(2922);
SELECT * FROM MXSPLPAGCLI WHERE CODCLI IN(2922);
SELECT * FROM MXSCOBCLI WHERE CODCLI IN(2922);
SELECT * FROM MXSCOBPLPAG WHERE CODCOB IN('2');

SELECT * FROM MXSPLPAG WHERE CODPLPAG IN(15,11);--TIPOVENDA VP VENDA A PRAZO
SELECT * FROM MXSCOB WHERE CODCOB IN('2');

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414467
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "o pedido do cliente 2922 não inicia" — o texto-fonte diz que o plano de pagamento não carrega e que o cliente inicia o pedido com plano 15 e cobrança 2, mas não afirma que o pedido não inicia. | "Plano 11 possui TIPOVENDA = VV" — o texto-fonte menciona "Como no caso do plano 11 TIPOVENDA (VV)...", mas não apresenta isso como resultado das consultas nem de forma totalmente inequívoca; além disso, a própria lista de consultas traz comentário "TIPOVENDA VP VENDA A PRAZO", gerando ambiguidade. | "ajustar o cadastro do cliente (MXSCLIENT) para utilizar o plano 11 com a cobrança 2" — o texto-fonte recomenda alterar o plano para 11, mas não recomenda explicitamente alterar a cobrança, apenas mantê-la como já está. | "Caso a intenção seja usar o plano 15, selecionar uma cobrança do tipo boleto (4)" — o texto-fonte afirma que se o RCA selecionar a cobrança 4 o plano 15 será exibido, mas não formula isso explicitamente como recomendação ao cliente neste caso.
