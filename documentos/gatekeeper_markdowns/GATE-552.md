# GATE-552 - Mix do Cliente não aparecec

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Mix
- Natureza: Dúvida
- Atualizado em: 2024-12-26T15:39:49.248-0300

## Contexto do Problema

## Passos para reproduzir
Login: mmix.cicero
Cliente: 2563
(BASE NOS COMENTÁRIOS)
1 - Iniciar um pedido no cliente 2563
2 - Ver as informações presentes e tabelas e mix do cliente

## Resultado apresentado
Mesmo com as informações estarem presentes, tanto no inspect quanto no banco nuvem, os produtos e nem o mix aparecem.

## Resultado esperado
Aparecer todas as devidas informações

## Descrição
Mesmo com as informações no banco, o mix do cliente e a tabela (produtos) estão vazios. Está ocorrendo com apenas um cliente

## Comentarios do Gatekeeper

### 1. 2024-12-26T15:39:49.247-0300 | Filipe do Amaral Padilha

O cliente 2563 possui um vínculo na PCTABPRCLI, que integrou para a nossa nuvem na MXSTABPRCLI que é o registro da filialnf 3 vinculado na região 363.

Na região 363, não tem nenhum produto precificado (MXSTABPR) se você consultar vai retornar nulo:
SELECT * FROM MXSTABPR WHERE NUMREGIAO IN(363);

Inclusive eu verifiquei e essa região no banco local (PCREGIAO e PCTABPR) estão nulos também, essa região de preço nem existe.

O nosso aplicativo sempre prioriza esse vínculo que é realizado na Rotina 3314 do cliente à filial e à região de venda.

Como os dados estão nulos, nenhum produto é exibido nem na tabela e nem no mix do cliente.

Para resolver ele deve configurar corretamente a precificação do cliente, dessa forma os itens serão exibidos tanto na tabela quanto no mix do cliente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 413985
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que o problema ocorre apenas nesse cliente não está explicitamente suportada pelo texto-fonte. | A recomendação de ajustar o vínculo para uma região válida e com produtos precificados extrapola levemente o texto-fonte, que apenas diz para configurar corretamente a precificação do cliente. | A indicação explícita de 'Responsável pela ação: Cliente' não aparece literalmente no texto-fonte, embora seja uma inferência possível.
