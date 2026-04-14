# GATE-529 - Preço mínimo sendo alterado a medida que altera a quantidade

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Política de Desconto - Comercial
- Natureza: Dúvida
- Atualizado em: 2024-12-19T07:30:18.689-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Iniciar um pedido em qualquer cliente
>>Ir na aba tabela e procurar pelo item 283062
>>Acessar a tela de negociação do item
>>Deixa a quantidade 1 no item e assim irá ver que o preço mínimo fica de 145,99
>>Alterar a quantidade para 12, e assim irá ver que o preço mínimo altera para 157,49

Login: megabrasil.17
senha: acesso temporário

## Resultado apresentado
Ao alterar a quantidade do 283062 para 12, ou qualquer outra quantidade acima de 1, o preço mínimo do item está ficando errado

## Resultado esperado
Que ao alterar a quantidade do item 283062 para qualquer quantidade acima de 1, puxe o preço mínimo correto.

## Descrição
O cliente possui a política de desconto 826321 configurada na rotina 561 do WinThor para o item 283062. No MaxPedido, ao adicionar uma quantidade de 1 unidade desse item, o preço mínimo exibido é de R$ 145,99. No entanto, ao alterar a quantidade para 2 ou qualquer valor acima de 1, o preço mínimo é ajustado para R$ 157,49, o que está incorreto. Segundo o cliente, o preço mínimo deveria permanecer em R$ 145,99 independentemente da quantidade.

## Comentarios do Gatekeeper

### 1. 2024-12-18T16:58:29.067-0300 | Filipe do Amaral Padilha

--Será encaminhado para N3 amanhã

{color:#cccccc}{color:#739eca}SELECT{color} * {color:#739eca}FROM{color} {color:#b788d3}MXSDESCONTO{color} {color:#739eca}WHERE{color} {color:#00b8b8}CODDESCONTO{color} {color:#739eca}IN{color}({color:#c0c0c0}826321{color}){color:#eecc64};{color}{color}

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 412981
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'conforme registrado em comentário técnico' não está explicitamente no texto-fonte | 'Responsável: N3' não está explicitamente afirmado no texto-fonte; o texto apenas diz que será encaminhado para N3 amanhã
