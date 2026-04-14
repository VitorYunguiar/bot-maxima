# GATE-72 - Bloquear RCA de iniciar bonificação caso não tenha saldo de conta corrente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXPED - Pedido - Bonificado
- Natureza: Dúvida
- Atualizado em: 2024-09-18T14:59:49.095-0300

## Contexto do Problema

## Passos para reproduzir
>muffataosc.0973

>Acessar APK
>Iniciar pedido em algum cliente
>Enviar um pedido normal
>Enviar um pedido bonificado vinculando ao pedido normal

## Resultado apresentado
Mesmo o RCA tendo 11 mil reais negativos em saldo de conta corrente, o mesmo consegue enviar bonificações normalmente.

## Resultado esperado
Impedir o RCA de gastar o que não possui.

## Descrição
Bom dia, gostaria de saber qual a parametrização necessária para bloquear que o vendedor inicie/envie um pedido bonificado caso não tenha saldo de conta corrente para tal, ou também se possível, permitir que ele insiria produtos bonificados somente até onde vai seu saldo de conta corrente.

## Comentarios do Gatekeeper

### 1. 2024-09-18T14:59:38.908-0300 | Filipe do Amaral Padilha

Validado na versão 3.249.3, mas na do cliente também vai funcionar.

Para ter o comportamento desejado deve ser configurado o parâmetro PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = 'N' diretamente na nuvem porque ao sincronizar o aplicativo faz a leitura desse parâmetro e insere em uma tabela chamada MXSCONFIG a informação.
Por isso que só alterar o parâmetro na base da apk não resolve o caso, precisa ser alterado em nuvem e sincronizado o parâmetro PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N. Assim o comportamento já vai ser conforme solicitado. Ao colocar A venda Bonificação, se o saldo exceder ou for negativo, quando tentar inserir o item a mensagem será exibida: "Produto excedeu crédito do RCA." dessa forma impedindo de confeccionar o pedido Bonificado.

Cenário:
CODFILIAL 09
Tipo Venda Bonificação
Plano 26 - BONIFICACAO
Cobrança - BONIFICACAO

Aba TABELA qualquer produto, mas usei o 120812-2
Apertar para inserir, imagem em anexo do que ocorre (a msg)

### 2. 2024-09-18T14:59:49.095-0300 | Filipe do Amaral Padilha

!Screenshot_2.png|thumbnail! !Screenshot_1.png|thumbnail!

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 395450
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Para bloquear a inclusão de itens bonificados quando o RCA estiver com saldo de conta corrente negativo ou sem crédito disponível' — o texto-fonte menciona 'se o saldo exceder ou for negativo', mas não explicita 'sem crédito disponível' nem 'conta corrente'. | 'Próximo passo' com instrução de 'Validar novamente a inclusão de itens bonificados sem saldo' — é uma recomendação/inferência operacional não presente literalmente no texto-fonte.
