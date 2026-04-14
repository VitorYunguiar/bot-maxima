# GATE-641 - RCAs não conseguem visualizar produtos (nenhum)

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2025-01-15T12:47:36.526-0300

## Contexto do Problema

## Passos para reproduzir
Login: grupoaz.isabela128
Senha: isabela128
1 - ir em produtos, selecionar filtros:
FILIAL 2 e REGIÃO 3

## Resultado apresentado
Produtos não aparecem
Acontecendo com todos os RCA

## Resultado esperado
Aparecer os produtos normalmente

## Descrição
Produtos não estão aparecendo para todos os RCAs, ambiente atualizado e testado na última versão, cliente não utiliza filial retira.

## Comentarios do Gatekeeper

### 1. 2025-01-15T12:47:36.520-0300 | Filipe do Amaral Padilha

Na base da RCA 128 grande parte dos produtos que não apareciam cerca de 400 produtos, era devido a restrições de venda.

Então provavelmente o cliente observou isso e removeu as restrições do sistema para os produtos serem vendidos.

Fiz teste em base zerada da RCA 145 que foi comentado no discord e constatei que está funcional também trazendo os produtos de exemplo "Cid" - CIDENTAL.

Se a base da RCA estiver com divergências, dai eu precisaria da base dela e que um novo ticket de gate fosse aberto, mas acredito que eles resolvendo a questão das restrições deve ter normalizado para todos os RCAs.

Igual é importante dialogar com o cliente para entender isso.

## Resposta Canonica

Identificou-se que, na base da RCA 128, grande parte dos produtos que não apareciam — cerca de 400 itens — estava com restrições de venda, o que explica a ausência dos produtos no cenário informado.

Como validação, foi realizado teste em base zerada da RCA 145, e o comportamento foi funcional. Nesse teste, os produtos de exemplo com o termo "Cid" - CIDENTAL foram retornados normalmente, indicando que o problema não se reproduziu nesse ambiente.

Assim, a orientação é alinhar com o cliente se as restrições de venda foram verificadas e removidas do sistema. Caso a base da RCA apresente divergências, será necessário abrir um novo ticket de gate e disponibilizar a base para análise.

Limitação da conclusão: a normalização para todos os RCAs não está confirmada; trata-se apenas de um indicativo com base nos testes realizados.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 416959
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
