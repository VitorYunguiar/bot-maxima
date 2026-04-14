# GATE-595 - clientes em especifico utilizarem apenas uma determinada filial

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: N/A
- Assunto: MXPED - Pedido/Orçamento - Histórico
- Natureza: Dúvida
- Atualizado em: 2025-01-08T10:04:38.867-0300

## Contexto do Problema

## Passos para reproduzir
efetuar o login e analise conforme a descrição

## Resultado apresentado
pedidos sendo gerados em filiais que o cliente não espera que sejam realizadas.

## Resultado esperado
é esperado que o aplicativo não permita a negociação do pedido de determinados clientes para determinadas regiões.

## Descrição
Senhores, ao analisar a demanda citada, observei a seguinte situação: o cliente vem enfrentando um cenário em que pedidos de determinados clientes estão sendo gerados de forma inadequada para uma de suas filiais. No cenário de exemplo, o cliente reporta que o cliente 5523 não deveria ter pedidos negociados através da filial 1:

!image-2025-01-07-17-59-38-257.png!

porém existem pedidos que estão saindo pela filial citada:

!image-2025-01-07-18-01-29-640.png!

Ao analisar o cenário no aplicativo, observei que o app disponibiliza as duas filiais para o RCA selecionar, o que permite com que o pedido possa ser negociado em ambas as filiais:

!image-2025-01-07-18-02-42-010.png!

Nesse cenário, qual a configuração que o cliente pode estar realizando para que restrinja no ato da negociação a nível de cliente e filial, para impedir que esses clientes consigam negociar pedidos na filial 1, mas sem remoção de permissões ou cadastrando as restrições para a venda via 521? quais as tabelas que seriam utilizadas para efetuar a configuração desejada pelo cliente?

login: pld.jairo

cliente: 5223

## Comentarios do Gatekeeper

### 1. 2025-01-08T10:04:38.865-0300 | Filipe do Amaral Padilha

Como o cliente é usuário do ERP Winthor, então teríamos duas opções que eu me recordo referente a restringir o acesso de filial durante a negociação no cliente. Seriam essas:

Rotina 3314: Grava na PCTABPRCLI que integramos na MXSTABPRCLI e a regra é que o cliente só vai ter acesso a filial que está vinculada ao código dele e também a região de preço determinada nessa rotina.

Rotina 391: É possível cadastrar também uma restrição por cliente, onde o cliente não pode acessar determinada filial. A que não possuir restrição, ele conseguirá acessar normalmente. Grava na PCRESTRICAOVENDA e sobe para a MXSRESTRICAOVENDA.

Ambas regras devem funcionar no maxPedido.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 415557
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A disponibilização de duas filiais no aplicativo ocorre porque a restrição de negociação por filial depende de configuração no ERP Winthor. | Pelas informações analisadas, há duas frentes de configuração que podem atender ao cenário. | Verificar no ERP Winthor, para o cliente afetado, se existe configuração nas rotinas abaixo: | Validar no Winthor se o cliente está configurado na rotina 3314 e/ou na rotina 391, e aplicar a regra de restrição por cliente x filial conforme a necessidade do cenário. | As rotinas 3314 e 391 foram citadas como opções lembradas no comentário, sem confirmação de que sejam as únicas possibilidades.
