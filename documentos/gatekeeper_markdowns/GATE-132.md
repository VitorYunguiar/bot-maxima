# GATE-132 - Erro Recorrente de Fotos que vieram do Upload de Fotos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Henrique Torres Andrade [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Fotos - Central
- Natureza: Dúvida
- Atualizado em: 2024-10-03T11:42:40.227-0300

## Contexto do Problema

## Passos para reproduzir
>> Abrir o banco nuvem do cliente
>> Consultar na tabela MXSPRODUTOSFOTOS os produtos 3856, 3857, 3858, 3859 (existem mais) e tentar abrir as fotos no navegador
>> Depois disso consultar os produtos (1496,4305,4322,4333,4382,4416,4432,3415,4238,3392,3414,4301,3999,4328,4329,4240,4418,3378,4239,4386,4388)

## Resultado apresentado
>> Problema está acontecendo com muita recorrência, em vários clientes diferentes
>> Proutos 3856, 3857, 3858, 3859 não estão duplicados, porém quando se tenta abrir a foto do produto no navegador aparece um erro informando que está sem acesso para acessar o link. Não são somente estes produtos que estão sem acesso, existem mais (alguns estão no print do erro no maxPedido)
>> Os demais produtos que foram citados anteriormente estão duplicados na MXSPRODUTOSFOTOS. Fazer delete nesses registros e falar para o cliente cadastrar as fotos novamente não é solução, uma vez que o problema vai acontecer novamente no mesmo cliente ou em outros clientes. É necessário enteder uma causa raiz do problema.

## Resultado esperado
>> Fotos de Produtos que NÃO estão duplicados estarem acessíveis, uma vez que o cliente fez o upload das fotos na Central
>> Fotos de produtos NÃO serem duplicados

## Descrição
Algumas fotos que *não* estão duplicadas na MXSPRODUTOSFOTOS não estão acessíveis pelo link que aparece no registro.

Além disso, algumas fotos aparecem duplicadas. (erro bastante recorrente)

Por conta disso, aparece o erro de Acesso Negado para os RCAs quando o maxPedido tenta baixar as fotos.

## Comentarios do Gatekeeper

### 1. 2024-10-03T11:42:40.225-0300 | Filipe do Amaral Padilha

Será enviado para N3

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review, requires_attachment_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
