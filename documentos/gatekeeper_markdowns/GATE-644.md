# GATE-644 - Relatório de clientes com roteiro detalhado com calculo inadequado

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: ROTVENDN - Relatórios
- Natureza: Dúvida
- Atualizado em: 2025-01-15T17:00:48.037-0300

## Contexto do Problema

## Passos para reproduzir
Acessar o roteirizador do cliente e efetuar as consultas conforme os prints que foram apresentados no decorrer da historia contada na descrição.

## Resultado apresentado
divergencia na quantidade de KMs planejado entre relatorios, com um comportamento inadequado sendo apresentado no relatorio "clientes com roteiro detalhado".

## Resultado esperado
é esperado que ambos os relatorios sejam de registros equivalentes.

## Descrição
Senhores, ao analisar o cenário abaixo:

_"Boa tarde!_

_Como conversado em reunião, buscamos uma forma de obter o KM planejado inserido no sistema, essa forma de obter o KM planejado (clientes com roteiro detalhado últimos 30 dias) nos ajudaria em partes pois possui uma coluna referente ao KM planejado por vendedor, porém quando emitimos desta forma possui uma divergência no resultado final._

_Utilizando o RCA 10 como exemplo quando emitimos os últimos 30 dias, o valor total é 4084,88, quando emitimos através da opção Clientes com roteiro e somamos o KM da um total de 2318,64, sendo o cálculo: 568,97 (semana 1) + 590,35 (semana 2) = 1159,32 *2 (levando em considerando que a semana 1 e 2 vão se repetir na 2ª quinzena do mês) = 2318,64._

_Se conseguirmos ajustar esta planilha "clientes com roteiro detalhado últimos 30 dias" com a valor correto do KM planejado, ao emitir em uma só planilha os dados de toda equipe, supriria a nossa deficiência desses dados neste momento._

_Segue prints em anexo."_

Identifiquei que o seguinte relatório, tem um comportamento de apresentação do KM planejado anormal:

!image-2025-01-15-12-49-21-889.png!

Ao fazermos a consulta com base no cenário descrito pelo cliente, é identificado que existem valores de KM se repetindo para clientes diferentes:

!image-2025-01-15-12-51-14-014.png!

E ao validar os dados que são trazidos no relatório de clientes com roteiro:

!image-2025-01-15-12-52-15-419.png!

Se constata que os valores repetidos se referem ao apanhado geral de km planejado do dia da semana:

1 semana quarta:

!image-2025-01-15-12-54-07-054.png!

1 semana terça:

!image-2025-01-15-12-55-22-613.png!

2 semana segunda:

!image-2025-01-15-12-56-26-253.png!

Ou seja, o relatorio "clientes com roteiro detalhado" está com um comportamento no calculo em que está trazendo em cada cliente o km planejado para o dia inteiro e não o valor em especifico do cliente em si e Isso está gerando a divergência de valores que o cliente está reportando. Essa situação é algo esperado que o sistema tenha? ou se trata de alguma parametrização que o roteirizador possui?

## Comentarios do Gatekeeper

### 1. 2025-01-15T16:20:55.198-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 para que o time de desenvolvimento possa opinar junto do P.O

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review, requires_attachment_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
