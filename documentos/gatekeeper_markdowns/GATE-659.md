# GATE-659 - maxGestao divergente  da 146

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral - Dados Divergentes do ERP
- Natureza: Dúvida
- Atualizado em: 2025-01-20T11:19:25.279-0300

## Contexto do Problema

## Passos para reproduzir
>>Abrir o maxGestao
>>Colocar a data de 01/12 até 31/12 no filtro do painel geral

## Resultado apresentado
>>Na 146 aparece um valor de R$2.033.342,77
>>No painel geral o valor é de R$332.719,32

## Resultado esperado
>>O valor normalmente não bate entre a 146 e o Gestao, mas a diferença deve ser muito menor.

## Descrição
Verificada divergência entre a 146 e o maxGestao no mês de dezembro.

Na 111 o valor bate corretamente

## Comentarios do Gatekeeper

### 1. 2025-01-20T11:19:25.276-0300 | Filipe do Amaral Padilha

Provavelmente cliente foi implantando no Winthor T-Cloud e não realizaram a carga dos pedidos do mês passado para o banco nuvem.

SELECT SUM(VLATEND) FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('01/12/2024','DD/MM/YYYY') AND TO_DATE('31/12/2024','DD/MM/YYYY') AND CODFILIAL IN(1) AND POSICAO NOT IN('C');
Deu o mesmo resultado da 146, porque é de forma sintética o que a 146 faz. Resultando em R$2033342.77

SELECT SUM(QT*PVENDA) FROM PCPEDI WHERE NUMPED IN(SELECT NUMPED FROM PCPEDC WHERE TRUNC(DATA) BETWEEN TO_DATE('01/12/2024','DD/MM/YYYY') AND TO_DATE('31/12/2024','DD/MM/YYYY') AND CODFILIAL IN(1) AND POSICAO NOT IN('C')) AND POSICAO NOT IN('C');

Já por histórico de itens, (como o maxGestão faz), não bate igual a 146, porque o valor dá divergente: R$2056551.45. Então o maxGestão e a 146 irão ficar divergentes justamente porque existe uma divergência dos valores dos históricos no banco do Winthor entre PCPEDC e PCPEDI.

--Para comparar com a 146 realizar dedução de bonfiicações.

No momento, (que estou te integrando o ticket) os valores estão batendo entre 146 e maxGestão deduzindo bnf. Porém ainda temos 20 mil registros descendo via integração do banco local para a nuvem então esse valor pode variar, até considerando o que expliquei sobre divergência de valores entre PCPEDC e PCPEDI

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 417702
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "A divergência de dezembro entre a rotina 146 e o maxGestão está associada a duas condições identificadas" — o texto-fonte apresenta uma possibilidade sobre implantação no T-Cloud e uma divergência entre PCPEDC e PCPEDI, mas não afirma de forma conclusiva que ambas são causas identificadas da divergência de dezembro. | "o maxGestão apura com base no histórico de itens em PCPEDI" — o texto-fonte diz "Já por histórico de itens, (como o maxGestão faz)", mas não afirma explicitamente que a apuração do maxGestão é feita em PCPEDI. | "confirmando divergência entre as bases de apuração" — o texto-fonte fala em divergência dos valores dos históricos no banco do Winthor entre PCPEDC e PCPEDI; "bases de apuração" é uma reformulação interpretativa não literal. | "O próximo passo é aguardar a conclusão da integração da base local para a nuvem e revalidar os valores com esse mesmo critério" — o texto-fonte não traz essa orientação como próximo passo, apenas informa que os valores podem variar enquanto há registros sendo integrados.
