# GATE-536 - Deduzir bonificação aplicando efeito contrário

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatórios - Filtros/Pesquisa
- Natureza: Erro
- Atualizado em: 2024-12-20T10:49:48.975-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar maxGestão;
>> Relatórios, Portal Executivo, Venda por Equipe e Análise de Vendas;
>> Gerar relatório com os filtros anexados ao ticket.

## Resultado apresentado
Valores divergentes entre a 146/painel do maxGestão e o portal executivo;

## Resultado esperado
Valores semelhantes;

## Descrição
Cliente está fazendo uma busca na 146 e o valor está alinhado com o que é apresentado no painel do maxGestão, porem dentro do relatório do Portal executivo, com os mesmos filtros da 146, ao selecionar para deduzir bonificação ele retorna um valor divergente. Sem a dedução de bonificação no painel executivo o valor fica igual para todos.

146: R$19.348,63

Painel maxGestão: R$19.348,63

Portal executivo: R$17.966,21

Os 3 cenários com os exatos mesmos filtros.

Cliente deseja corrigir a divergencia no painel executivo.

## Comentarios do Gatekeeper

### 1. 2024-12-20T10:49:48.974-0300 | Filipe do Amaral Padilha

Será enviado para N3 porque de fato, o valor sem deduzir bonificação era para ser 20.731,05 e parece que no script por RCA, ao acessar, está já deduzindo a bonificação e quando você aplica o filtro deduz novamente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
