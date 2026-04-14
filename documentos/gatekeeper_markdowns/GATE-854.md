# GATE-854 - app travar a negociação na embalagem master

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Embalagem
- Natureza: Dúvida
- Atualizado em: 2025-02-25T11:38:55.322-0300

## Contexto do Problema

## Passos para reproduzir
efetuar a negociação sobre o seguinte cenário:
- login: FLITS.74
- produto; 50
- cliente; 9799
- filial 1;
e observar o campo da embalagem

## Resultado apresentado
mesmo com o parametro habilitado a aplicação não está sendo forçada a utilizar a embalagem master do produto

## Resultado esperado
é esperado que ao iniciar a negociação, o campo de embalagem esteja travado com a embalagem master do produto.

## Descrição
Senhores, ao analisar o cenário citado, o cliente necessita que alguns de seus RCAS negociem os seus produtos apenas com a embalagem master do mesmo. Realizamos a parametrização no usuário habilitando o parâmetro FORCAR_UNIDADE_MASTER_PRODUTO mas ainda assim a aplicação exibiu ambas as embalagens:

!image-2025-02-25-08-29-00-801.png!

No cenário do cliente, qual a configuração que precisa ser realizada para que a aplicação se comporte com essa forma que o cliente deseja, para além do parâmetro citado?

## Comentarios do Gatekeeper

### 1. 2025-02-25T11:12:17.774-0300 | Filipe do Amaral Padilha

Foi considerado o cenário que o cliente gostaria de trabalhar e também a forma que o aplicativo permite trabalhar atualmente:

Então o que atenderia o cenário do cliente, ou seja, ele queria trabalhar de forma que o RCA pudesse vender somente uma embalagem específica do produto:

Então eles teriam que configurar restrições de venda usando o conceito do CODAUXILIAR da embalagem que não poderá ser vendido, eles podem fazer via central ou Winthor

E também precisam que o parâmetro do maxPedido esteja marcado RESTRINGIR_PRODUTOS_391 = 'N' por default ele oculta os produtos com restrição de venda, e vem = 'S'.

Outra possibilidade, seria trabalhar com a permissão Acesso ao controle de caixa fechada (Produto) = [X], ela força o RCA a vender o múltiplo cadastrado no campo QTUNITCX da MXSPRODUT.

Qualquer cenário diferente desse seria uma melhoria

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 426408
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: O comportamento esperado não é atendido apenas com o parâmetro `FORCAR_UNIDADE_MASTER_PRODUTO`. | Portanto, para o cenário informado, a orientação é validar com o cliente a aplicação de restrição por `CODAUXILIAR` da embalagem não permitida, com `RESTRINGIR_PRODUTOS_391 = 'N'`, ou avaliar o uso do controle de caixa fechada.
