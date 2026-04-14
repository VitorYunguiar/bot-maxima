# GATE-856 - Relatório de entrada de produtos não apresenta dados

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatórios - Dados Divergentes do ERP
- Natureza: Dúvida
- Atualizado em: 2025-02-25T12:45:20.417-0300

## Contexto do Problema

## Passos para reproduzir
Verificar tabelas do banco nuvem e banco local.

## Resultado apresentado
Relatório não retorna dados

## Resultado esperado
Relatório retornando dados;

## Descrição
Relatório de entrada de produtos não apresenta dados mesmo com registros na MXSESTPEND.

Tambem foi verificados os registros locais na PCMOV e PCNFENT, que constam para a data selecionada, porem no relatório do portal executivo não retorna nenhum dado.

Cliente TCLOUD.
Senha maxsolucoes: sgzvc58629MWANS?@

HOST: 177.136.11.103
SERVICE: CTDQ2Z_186152_W_high.paas.oracle.com

## Comentarios do Gatekeeper

### 1. 2025-02-25T12:45:20.409-0300 | Filipe do Amaral Padilha

Foi verificado que o relatório utiliza dados da ERP_PCNFENT (PCNFENT) e ERP_MXSMOV (PCMOV) para gerar os dados, porém o parâmetro UTILIZA_GESTAO_LOGISTICA = N foi alterado no cliente em 15-FEB-25. Com o parâmetro = N os dados dessas tabelas não são integrados à Nuvem da Máxima.

Nesse caso eu ativei o parâmetro diretamente no banco local dele via Winthor Nuvem na nossa tabela PCMXSCONFIGURACOES.

E fiz a carga só desse Mês de fevereiro em todas as filiais que integram com a Máxima nas tabelas PCMOV e PCNFENT

Para validar é só esperar agora os registros terminarem de ser integrados:
https://padeirao.extratormaxima.com.br/registrospendentes

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 426452
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Por isso, mesmo existindo registros localmente em PCMOV e PCNFENT, o relatório no portal executivo não retorna dados.' | 'O relatório de entrada de produtos' | 'Ação recomendada' como recomendação explícita não aparece no texto-fonte; o texto diz apenas 'Para validar é só esperar agora os registros terminarem de ser integrados'. | 'Após a conclusão da integração, validar novamente o relatório para confirmar se os dados passam a ser apresentados.'
