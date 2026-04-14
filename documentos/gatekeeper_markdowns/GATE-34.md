# GATE-34 - Ticket Anterior 56456 - Processos travando

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Integração - Integradora Winthor
- Natureza: N/A
- Atualizado em: 2024-10-11T17:02:59.414-0300

## Contexto do Problema

## Passos para reproduzir
conforme a descrição citada no ticket

## Descrição
Analisando o cenário da demanda citada desse ticket, o cliente reporta o seguinte:

"_Boa Tarde! Referente ao ticket anterior MXPED-56456, onde foi aberto que alguns processos travam devido uma função da PCMXINTEGRACAO, foi desmarcado uma opção nas configurações mais mesmo assim permanece, seria possivel nos processos da Maxintegradora, não fazer update nos pedidos que forem executados numa rotina Específica como tinha sido citado PCMOT9898, estamos com esses processos causando muita demora no faturamento_"

Na demanda citada em analise pelo departamento de backend, foi reportado o seguinte:

"_Como o comando especificado é o "delete from pcmxsintegracao", fica evidenciado que no processo de faturamento_
_a rotina alterou registros e comitou, e depois alterou novamente e não realizou o commit._
_com isso nosso processo sobe para nuvem o registro da pcmxsintegracao, e na hora de remover da pcmxsintegracao, ele está bloqueado pela rotina._
_Isso gera o aguardo evidenciado no anexo. Pelo print parece ser operações na tabela de carregamento (PCCARREG)_
_Pelo print, o cliente parece usar FUSION em vez do produto de logística da máxima._
_Sendo assim, para a tabela mencionada, podemos desativar o disparo da trigger, através do parâmetro UTILIZA_LOGISTICA_MXS._
_Parâmetro localizado na PCMXSCONFIGURACOES do banco MAXSOLUCOES. Para não disparar, ele precisa estar como N._"

Para além dessas configurações citadas, há alguma outra parametrização por parte do maxpedido que pode ser configurado para esse cenário do cliente? a rotina citada faz a manipulação de diversas tabelas  conforme relatado pelo cliente:

!image-2024-09-06-16-28-27-576.png!

!image-2024-09-06-16-30-03-799.png!

!image-2024-09-06-16-30-48-742.png!

## Comentarios do Gatekeeper

Nenhum comentario elegivel do assignee foi identificado.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, needs_review, requires_attachment_review
- Comentarios primarios: nenhum
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
