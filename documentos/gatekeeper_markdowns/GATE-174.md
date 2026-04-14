# GATE-174 - Replicador MXSUSUARIOS

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Extrator
- Natureza: N/A
- Atualizado em: 2024-10-11T16:09:29.918-0300

## Contexto do Problema

## Passos para reproduzir
Validar informações na descrição

## Resultado apresentado
Dados não estão sendo replicados

## Resultado esperado
Dados replicados.

## Descrição
Cliente informou que o registros dos RCAS 2543(cadastrado 07/10/2024) e 2544 (cadastrado 09/10/2024) não foram encontrados na tabela MAXSOLUCOES.MXSUSUARIOS, o que indica que a replicação não está funcionando.

Alinhado com o Filipe Padilha.

## Comentarios do Gatekeeper

### 1. 2024-10-11T16:09:29.916-0300 | Filipe do Amaral Padilha

Foi reativado o replicado do cliente que estava parado desde o dia 21/09/2024 por uma causa que ainda não identificamos; No caso o problema dos dados não aparecerem foi resolvido com a reativação do replicados mas a causa raíz para ter parado de funcionar ainda não, por isso vou enviar N3.

O cliente já pode estar verificando no banco dele que os dados desses RCAs que eles vão estar lá.
{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSUSUARIOS{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODUSUR{color} {color:#739eca}IN{color}({color:#c0c0c0}2543{color},{color:#c0c0c0}2544{color}){color:#eecc64};{color}

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 400414
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Essa indisponibilidade explica a ausência dos registros dos RCAs 2543 e 2544 na tabela `MXSUSUARIOS`." — o texto-fonte diz que o problema dos dados não aparecerem foi resolvido com a reativação, mas não afirma explicitamente que a indisponibilidade do replicado explica a ausência desses registros. | "Após a reativação do replicador, o problema de não apresentação dos dados foi normalizado" — o termo "normalizado" não aparece no texto-fonte; embora a ideia esteja próxima, é uma reformulação interpretativa. | "Próximo passo: encaminhar para o N3 para apuração da causa raiz da parada do replicador." — o texto-fonte diz "vou enviar N3", mas não explicita "para apuração da causa raiz".
