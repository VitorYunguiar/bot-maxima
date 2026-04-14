# GATE-530 - Relatório em excel gerando corrompido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatório - 800
- Natureza: Dúvida
- Atualizado em: 2024-12-19T11:53:25.353-0300

## Contexto do Problema

## Passos para reproduzir
Gerar relatório com os filtros do print em anexo.

## Resultado apresentado
Arquivos sendo gerados corrompidos.

## Resultado esperado
Arquivo sendo gerado corretamente.

## Descrição
Ao gerar o relatório 8065 em excel, as duas opções de formato geram um arquivo corrompido. Em PDF está sendo gerado normalmente.

Arquivos gerados em .xls e .xlsx em anexo.

## Comentarios do Gatekeeper

### 1. 2024-12-19T11:53:25.352-0300 | Filipe do Amaral Padilha

Foi feito mudança no gerador do relatório para corrigir o problema de arquivo corrompido ao gerar o Excel e Excel XLSX;

Foi realizado o teste e agora os dados estão sendo gerados corretemente.

Diferente do PDF, quando é gerado com cabeçalho e demais informações. No caso o Excel gera só os dados brutos tabelados e está correta a geração

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 413134
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A geração em PDF permanecia normal. | Causa identificada: havia um problema no gerador do relatório que corrompia os arquivos ao gerar nos formatos Excel (.xls) e Excel XLSX (.xlsx). | Ação recomendada: | - Aplicar a correção no gerador do relatório. | - Validar a geração do relatório após a alteração. | - Confirmar com o solicitante se, no Excel, a saída apenas com dados brutos tabelados atende à necessidade.
