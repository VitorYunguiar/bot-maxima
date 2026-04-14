# GATE-336 - espelho de rota com campos fixos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: N/A
- Assunto: MXGESN - Espelho de Rotas
- Natureza: N/A
- Atualizado em: 2024-11-14T07:59:17.114-0300

## Contexto do Problema

## Passos para reproduzir
conforme descrição

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Senhrores, ao analisarmos o cenário da demanda citada, é possível identificar que o menu de impressão de espelho de rota no painel de auditoria, tem apresentado um comportamento que a principio, não é esperado. Quando acessamos o painel de auditoria, existe a possibilidade de configurar quais os campos que serão exibidos no ato da consulta. Porém ao realizar a impressão do espelho de rotas, isso não é levado em consideração e o espelho trás sempre um fomato padrão, com as mesmas colunas. A duvida é: ele deve ter esse comportamento de sempre trazer as colunas "padrão", ou deve trazer as colunas com base no que há no grid? Caso seja o cenário da segunda opção, ocorreram alterações no padrão desse espelho, uma vez que o cliente tem um exemplo de espelho de rotas "antigo" que possui mais colunas que o espelho atual (vide anexos)?

## Comentarios do Gatekeeper

### 1. 2024-11-14T07:50:27.862-0300 | Filipe do Amaral Padilha

Enviado para N3 para checarem se o comportamento mudou ou se seria uma falha;

Uma sugestão, o cliente ainda consegue extrair todos os dados do Grid, apertando no botão 'exportar dados do grid' que aparece ao aperta na flecha. (Não é o botão Imprimir), dai o grid é exportado conforme os campos configurados para exibição.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 406918
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "No momento, não há confirmação de que o comportamento atual do espelho de rota seja o esperado." | "O espelho impresso pelo botão \"Imprimir\" não está coberto pela validação já concluída." | "A orientação disponível no momento refere-se à exportação do grid, e não à impressão." | "Para obter os dados conforme os campos configurados no painel, utilizar o botão \"exportar dados do grid\"." | "Para a dúvida sobre o comportamento do espelho de rota na impressão, é necessário aguardar a validação do N3, que irá confirmar se houve alteração no padrão ou se existe falha."
