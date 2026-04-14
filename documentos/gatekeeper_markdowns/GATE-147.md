# GATE-147 - Pedido de brinde sendo enviado junto com o TV1

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Sankhya
- Assunto: MXPED - Pedido - Bonificado
- Natureza: Dúvida
- Atualizado em: 2024-10-04T15:09:13.232-0300

## Contexto do Problema

## Passos para reproduzir
Login: dismartins.joao93
Cliente 10119
Produto 3911 - 15 unidades a R$155
Pedido TV1: 1022
Pedido TV5: 1023

## Resultado apresentado
O pedido TV5 so subiu para a nuvem depois que o pedido TV1 passou para LIBERADO na apk.

## Resultado esperado
TV5 enviado para integração juntamente com o TV1, sem a necessidade de aguardar a liberação do pedido original.

## Descrição
Ao gerar um pedido com brinde é criado um pedido TV5 automaticamente, porem ele so é enviado para a nuvem depois que o pedido TV1 é liberado pelo ERP. Cliente deseja que os dois pedidos sejam enviados ao mesmo tempo, sem que o TV5 precise aguardar a liberação do TV1.

Cenário utilizado:

Login: dismartins.joao93
Cliente 10119
Produto 3911 - 15 unidades a R$155
Pedido TV1: 1022
Pedido TV5: 1023
Base em anexo.

## Comentarios do Gatekeeper

### 1. 2024-10-04T15:09:13.230-0300 | Filipe do Amaral Padilha

Sobre o comportamento do maxPedido: o pedido de bonificação é gerado e somente enviado para a nuvem da Máxima após o retorno do numpederp na crítica do pedido pai (TV1) no endpoint StatusPedidos.

Mesmo que o erp dê o retorno instantaneamente pela api, para que essa informação seja carregada na aplicação é necessário que o RCA realize o swipe. Então existe atualmente uma dependência com o RCA realizar o swipe para essas bonificações serem enviadas para a nuvem da Máxima.

O ERP pode rapidamente retornar a crítica do pedido com o NUMPEDERP no pedido principal, porém, somente depois que o RCA faz o swipe no maxPedido é que ele recebe essa informação no pedido principal e posteriormente realiza novamente o swipe, assim possibilitando o envio da bonificação para a nuvem.

No momento, infelizmente, não temos configurações disponíveis para alterar esse comportamento, se o cliente quiser bater o pé, teria de ser analisado como Melhoria, dai você mesmo pode abrir a melhoria para N3.

Um paliativo muito útil: temos trabalhado em uma novidade e tínhamos a intenção e previsão de liberar a sincronização automática dos pedidos e de outras informações do sistema já nesse mês. Com isso, ajuda nesses cenários onde a bonificação não sobe por dependência com o usuário do maxPedido, ela subindo de forma automática o sistema fica mais fluido. --Você pode também conversar com o cliente para ver se isso já ajuaria eles e se o cliente quiser depois alinhar diretamente com o Cleyton.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 399037
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma especificamente que o pedido de bonificação é "TV5". O texto-fonte menciona apenas "pedido de bonificação" e "pedido pai (TV1)", sem citar TV5. | A resposta inclui o cenário específico "TV1: pedido 1022" e "TV5: pedido 1023", que não aparece no texto-fonte. | A resposta diz que "TV5 só subir para a nuvem após o TV1 ficar liberado na APK". O texto-fonte não menciona "APK" nem "ficar liberado". | A resposta afirma que a mudança desejada seria para que "TV1 e TV5 sejam enviados juntos". O texto-fonte não descreve esse envio conjunto dessa forma. | A resposta menciona "responsável indicado" de forma genérica; embora o texto-fonte cite Cleyton, a formulação da resposta omite o nome e mantém a recomendação, mas isso não é propriamente um problema factual. Ainda assim, a ideia central está parcialmente suportada.
