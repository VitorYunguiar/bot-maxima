# GATE-439 - KMs incorretos no painel de auditoria

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Dados Incorretos
- Natureza: N/A
- Atualizado em: 2024-12-04T09:49:23.122-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxGestão;
>> Acessar painel de auditoria;
>> Buscar dados do dia 27/11/2024 para o vendedor 25853;

## Resultado apresentado
Informado que o KM total no dia foi de 10041 KM

## Resultado esperado
Dados corretos

## Descrição
Alguns RCAs estão contabilizando valores absurdos de KM total e KM trabalhado.

Prints em anexo.

Dados referentes ao dia 27/11 no painel de auditoria.

Ocorrendo com todos os RCAs.

## Comentarios do Gatekeeper

### 1. 2024-12-04T09:49:23.120-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 para a TECH investigar porque os dados do maxPedido rastreamentos, não batem com a API de rastros, então provavelmente está tendo algum problema de cálculo no km total (até onde eu sei, isso seria a TECH para verificar)

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410223
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "exibido no painel de auditoria" | "Responsável: TECH" como atribuição conclusiva de responsabilidade, além de "(até onde eu sei, isso seria a TECH para verificar)" | Estruturações interpretativas não explicitamente presentes no texto-fonte, como "evidência textual disponível" e "limitações da análise", embora em geral coerentes
