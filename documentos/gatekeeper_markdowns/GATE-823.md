# GATE-823 - DANF-E não está integrando os dados presente na PCDOCELETRONICO

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Atualização - Banco
- Natureza: Dúvida
- Atualizado em: 2025-02-19T14:17:42.259-0300

## Contexto do Problema

## Passos para reproduzir
NUMPED = 800017210
NUMTRANSVENDA = 2030479

## Resultado apresentado
Não é possível gerar com DANF-E
Ambiente já atualizado. Além disso, ao que parece não esta integrado em nosso banco.

## Resultado esperado
Conseguir gerar normalmente o DANF-E e ter as devidas informações na ERP_MXSDOCELETRONICO

## Descrição
vimos no banco local do cliente que mesmo com a tabela PCDOCELETRONICO preenchida, quando buscamos na ERP_MXSDOCELETRONICO não aparece nenhum dado

## Comentarios do Gatekeeper

### 1. 2025-02-19T11:23:18.547-0300 | Filipe do Amaral Padilha

Foi realizada normalização dos dados para descer a tabela PCDOCELETRONICO corretamente para o banco de dados nuvem. Conferi e agora os dados estão na ERP_MXSDOCELETRONICO corretamente. Na normalização eu também acatei outras notas que poderiam estar com problemas.

Após a descida na ERP_MXSDOCELETRONICO, a nossa job rodou e gerou a tabela MXSDOCELETRONICO que o maxPedido utiliza para fazer a geração da nota.

Para validar baixar uma base do zero e testar se gera corretamente o arquivo. No caso do RCA, é só ele sincronizar o maxPedido e realizar o teste.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 425180
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Isso impactava a geração da ERP_MXSDOCELETRONICO e, consequentemente, da MXSDOCELETRONICO' é inferência causal não explicitada no texto-fonte. | 'impedindo a geração do DANF-E' não aparece no texto-fonte. | 'A inconsistência estava no fluxo de envio dos dados da PCDOCELETRONICO para a nuvem' é uma reformulação interpretativa não afirmada literalmente no texto-fonte. | 'restabelecendo o processo necessário para emissão' não aparece no texto-fonte. | 'Responsável: RCA' não é informado no texto-fonte; o texto apenas diz que, no caso do RCA, ele deve sincronizar o maxPedido e testar.
