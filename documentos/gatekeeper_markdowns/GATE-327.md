# GATE-327 - Orçamento x Venda não exibe todos os pedidos no PWA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXGESN - Orçamento x Venda
- Natureza: Dúvida
- Atualizado em: 2024-11-13T10:42:24.706-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o maxGestão PWA do cliente (Utilizo o login gsa.pfilho - gsa.2022 (senha))
>Orçamento x Venda
>Filtrar 12/11
>Consultar
>Observar que os registro são exibidos até o horário das 16h

>Acessar o Orçamento x Venda pelo maxGestão Web (Esse pode ser visualizado utilizando o SysMax)
>Filtrar 12/11
>Consultar
>Observar que são exibidos todos os pedidos do dia

## Resultado apresentado
No ambiente PWA da GSA ao consultar todos os pedidos do dia na tela ORÇAMENTO X VENDA, ele não exibe todos os pedidos do dia, pois pelo visto existe um limite de registros a serem exibidos.

Na mesma tela, porém no maxGestão Web normal, ele exibe todos os registros do dia, independente da quantidade a ser carregada.

## Resultado esperado
Conseguir ver todos os registros também no PWA, já que alguns supervisores só estão conseguindo utilizar a função através do PWA, já que aceitaram o pop-up.

## Descrição
Bom dia Filipe,

No ambiente PWA da GSA ao consultar todos os pedidos do dia na tela ORÇAMENTO X VENDA, ele não exibe todos os pedidos do dia, pois pelo visto existe um limite de registros a serem exibidos.

Na mesma tela, porém no maxGestão Web normal, ele exibe todos os registros do dia, independente da quantidade a ser carregada.

## Comentarios do Gatekeeper

### 1. 2024-11-13T10:42:24.705-0300 | Filipe do Amaral Padilha

Enviado para N3 para verificarem se esse é o novo comportamento ou se está incorreto

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 406667
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Na tela **Orçamento x Venda** do **PWA**, foi reportado que a consulta do dia **12/11** exibe registros apenas até determinado horário, enquanto no **maxGestão Web** a mesma consulta retorna todos os pedidos do dia. | Até o momento, **não há causa identificada**, nem evidências técnicas conclusivas que confirmem limitação, erro ou comportamento esperado. | O caso deve ser **encaminhado ao N3** para verificar se: - este comportamento no **PWA** é o **novo comportamento esperado**, ou - trata-se de um **comportamento incorreto**. | **Aguardar a análise do N3** para confirmação do comportamento e definição da tratativa adequada.
