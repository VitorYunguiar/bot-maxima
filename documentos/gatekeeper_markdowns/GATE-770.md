# GATE-770 - Parâmetro não é vinculado a filial

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: TOTVS EMS-DATASUL
- Assunto: MXPED - Parametrização
- Natureza: Dúvida
- Atualizado em: 2025-02-10T15:35:55.623-0300

## Contexto do Problema

## Passos para reproduzir
Reproduzir passos do vídeo em anexo.

## Resultado apresentado
Mesmo deletando o registro da filial 99 a APK apresenta o valor da indenização = 0 mas não puxa o valor vinculado a filial 3.

## Resultado esperado
APK puxando o valor do parâmetro CON_PERMAXINDENIZPEDIDO para a filial 3.

## Descrição
Parâmetro CON_PERMAXINDENIZPEDIDO está vinculado a filial 3, porem o pedido da filial 3 não puxa o valor de indenização que consta no parâmetro mesmo estando correto dentro da base da APK.

Na base consta o parâmetro CON_PERMAXINDENIZPEDIDO para a filial 99 e filial 3. Mesmo deletando o registro da filial 99 a APK apresenta o valor da indenização = 0 mas não puxa o valor vinculado a filial 3.

Em anexo vídeo do processo e a base utilizada.

Ocorrendo também em base do zero.

## Comentarios do Gatekeeper

### 1. 2025-02-10T11:49:48.947-0300 | Filipe do Amaral Padilha

O parâmetro CON_PERMAXINDENIZPEDIDO e original do Winthor, por isso existe esse conceito no força de vendas da Máxima.
Porém no próprio Winthor, ele é um parâmetro geral e não pode ser configurado por Filial, por este motivo, nós atualmente apenas replicamos esse comportamento:
https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050979453-WINT-Qual-fun%C3%A7%C3%A3o-do-par%C3%A2metro-2369-da-rotina-132

Nesse sentido: O maxPedido realmente não valida essa configuração de indenização por filial, para alteração desse comportamento teríamos de avaliar como possibilidade de Melhoria para o sistema.

Cenário:
CODCLI: 73718
Região 70000
CODPLPAG 6
CODPROD:
973727 QT 4

Ps: faltou o login só 🙂 na próxima lembra de colocar

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 422675
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Assim, mesmo existindo configuração para a filial 3" — o texto-fonte não menciona existência de configuração para a filial 3. | "a expectativa de que a APK busque o valor da filial 3" — o texto-fonte não menciona APK nem expectativa relacionada à filial 3. | "Não foi identificada falha de processamento com base na regra vigente." — o texto-fonte não afirma explicitamente que não houve falha de processamento; apenas descreve o comportamento atual. | "Encaminhar a demanda para avaliação de melhoria do sistema" — o texto-fonte menciona que seria necessário avaliar como possibilidade de melhoria, mas não recomenda explicitamente encaminhamento da demanda.
