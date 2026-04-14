# GATE-560 - Campo desconto

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Relatório - Personalizados
- Natureza: Dúvida
- Atualizado em: 2025-01-02T08:23:59.446-0300

## Contexto do Problema

## Passos para reproduzir
Login: viacerta.714
entrar no maxPedido e mandar gerar o boleto
alterar o campo VALORDESC nas tabelas ERP_MXSPREST e MXSTITULOSABERTOS

## Resultado apresentado
Campo desconto do boleto está em branco

## Resultado esperado
Estar com as informações presentes do desconto.

## Descrição
Campo de desconto não está com informação.

## Comentarios do Gatekeeper

### 1. 2024-12-30T16:45:37.671-0300 | Filipe do Amaral Padilha

Será enviado para N3 para verificar o motivo de a variável não estar mapeada no customizado do boleto

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414390
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que a 'causa identificada' é que o campo de desconto está em branco porque a variável não está mapeada no customizado do boleto não está totalmente suportada; o texto-fonte apenas diz que será enviado ao N3 para verificar o motivo. | As menções à reprodução informada, à alteração do campo `VALORDESC` nas tabelas `ERP_MXSPREST` e `MXSTITULOSABERTOS`, e que o desconto não é apresentado no boleto não constam no texto-fonte. | A afirmação de que 'a análise aponta que o problema não está no preenchimento do valor' não consta no texto-fonte. | A seção 'Responsável pelo tratamento: N3' não está explicitamente afirmada no texto-fonte, que apenas informa que será enviado para N3 para verificação.
