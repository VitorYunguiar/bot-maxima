# GATE-229 - Mesmo cumprindo o roteiro do dia anterior, está pedindo desbloqueio no outro dia

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: Dúvida
- Atualizado em: 2024-10-25T07:24:59.493-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Ir na tela de clientes
>>Tentar iniciar um pedido em qualquer cliente do roteiro de hoje dia 24/10
>>E assim retorna que não cumpriu todo o roteiro do dia anterior, solicitando o desbloqueio

login: ORCA. juliana
senha: orca2022

## Resultado apresentado
Mesmo RCA cumprindo todo o roteiro no dia anterior solicita desbloqueio informando não ter cumprido todo o roteiro do dia anterior

## Resultado esperado
Que não bloqueie a rota no dia seguinte, o RCA tendo cumprido todo o roteiro do dia anterior

## Descrição
O cliente voltou com a situação do RCA ter cumprido todo o roteiro do dia anterior e mesmo assim ter bloqueado no outro dia.

Pelo que analisei dentro do roteirizador de vendedores tinha 12 clientes no roteiro do dia 23/10, mas na MXSCOMPROMISSOS constam 15 clientes no roteiro, e gostaria de entender o porque dessa divergência.

## Comentarios do Gatekeeper

### 1. 2024-10-24T16:58:31.853-0300 | Filipe do Amaral Padilha

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXMI_AGENDA_RCA{color} {color:#739eca}WHERE{color} {color:#00b8b8}ID_RCA{color} {color:#739eca}IN{color}({color:#c0c0c0}9108{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#00b8b8}INICIO_VISITA{color}) = {color:#c1aa6c}TRUNC{color}({color:#b19b9b}SYSDATE{color},{color:#cac580}'DD'{color}) - {color:#c0c0c0}1{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}ERP_MXSROTACLI{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUR{color} {color:#739eca}IN{color}({color:#c0c0c0}9108{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSHISTORICOCOMPROMISSOS{color} {color:#b788d3}m{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}40740{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#b788d3}m{color}.{color:#00b8b8}DTINICIO{color}) = {color:#c1aa6c}TRUNC{color}({color:#b19b9b}SYSDATE{color},{color:#cac580}'DD'{color}) - {color:#c0c0c0}1{color}{color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCOMPROMISSOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUARIO{color} {color:#739eca}IN{color}({color:#c0c0c0}40740{color}) {color:#739eca}AND{color} {color:#c1aa6c}TRUNC{color}({color:#00b8b8}DTINICIO{color}) = {color:#c1aa6c}TRUNC{color}({color:#b19b9b}SYSDATE{color},{color:#cac580}'DD'{color}) - {color:#c0c0c0}1{color}{color:#eecc64};{color}

{color:#eecc65}--SELECTS NA BASE DA APK ABAIXO{color}
{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSCOMPROMISSOS{color} {color:#739eca}WHERE{color} {color:#739eca}date{color}({color:#00b8b8}dtinicio{color}) = {color:#739eca}date{color}({color:#cac580}'2024-10-23'{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSHISTORICOCOMPROMISSOS{color} {color:#739eca}WHERE{color} {color:#739eca}date{color}({color:#00b8b8}dtinicio{color}) = {color:#739eca}date{color}({color:#cac580}'2024-10-23'{color}){color:#eecc64};{color}

{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSUSUARIOS{color}{color:#eecc64};{color}

### 2. 2024-10-24T16:59:29.730-0300 | Filipe do Amaral Padilha

--Não finalizei a análise ainda, preciso entender porque o cliente apagou a rota no dia 23/10 às 15h e como isso pode impactar na geração da tabela MXSHISTORICOCOMPROMISSOS no dia seguinte.

### 3. 2024-10-25T07:24:59.484-0300 | Filipe do Amaral Padilha

Provavelmente será tratado como erro ou melhoria. Será encaminhado para desenvolvimento como Erro para eles avaliarem. O que aconteceu é que há registro de alteração da rota do RCA no dia 23/10 enquanto ela ainda estava vigente, e aparentemente o nosso sistema não tem nenhum mecanismo que reconheça que a rota foi editada no dia vigente e apague o histórico dos compromissos de forma compatível com as remoções realizadas.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 402957, 402958, 402996
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificada divergência entre o roteiro exibido no roteirizador e os compromissos considerados para bloqueio no dia seguinte." | "resultando na solicitação de desbloqueio no dia seguinte, mesmo com o roteiro aparentemente cumprido." | "Diante do cenário, o caso deve ser encaminhado para Desenvolvimento como Erro"
