# GATE-500 - Indenização não aparece no Winthor

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Indenização
- Natureza: Dúvida
- Atualizado em: 2024-12-13T16:28:52.032-0300

## Contexto do Problema

## Passos para reproduzir
Entrar no banco local do cliente, verificar as tabelas PCINDC, PCINDCFV, PCINDI o registro NUMINDENIZACAO 80254.

## Resultado apresentado
É verificado que o registro não consta nas tabelas de integração do WINTHOR.

## Resultado esperado
É esperado que o registro seja apresentado corretamente no Winthor.

## Descrição
Cliente relata que as indenizações não estão sendo exibidas no Winthor. Foi verificado o cenário da indenização NUMINDENIZACAO 80254 (codusur 17 e codcli 219), onde foi retornada a crítica de sucesso no processamento mas ao pesquisar a indenização nas tabelas PCINDC, PCINDCFV e PCINDIFV, a indenização não existe.
Foi possível visualizar a indenização em questão apenas na MXSINTEGRACAOINDENIZACAO, onde consta também a crítica de sucesso de processamento do registro.

## Comentarios do Gatekeeper

### 1. 2024-12-13T16:01:42.817-0300 | Filipe do Amaral Padilha

Eu analisei o fluxo desde a apk usando o login deles 'sulfrios.mateus' e o processo para gerar a indenização é o seguinte:

O maxPedido utilizar o campo PROXNUMPEDFORCA para gerar o numindenizacao que é chave primária da indenização.

Então quando o usuário inicia uma indenização no maxPedido, o sistema faz o seguinte:

PROXNUMPEDFORCA + 1 = numdenizacao. Exemplo PROXNUMPEDFORCA = 803260, então numdenizacao = 803261.

Feito isso o maxPedido salva a indenização e manda para o backend processar.

O nosso backend pega o numdenizacao e converte para codindeniz que será gravado lá na PCINDCFV.

Campo que será gravado é o PCINDCFV.CODINDENIZ.

Te expliquei o fluxo para entendermos o que ocorreu com a indenização (803254). No caso, o numindenizacao é 803254 que foi gerado a partir do pedido 803253.

Como expliquei o numindenizacao é convertido para codindeniz. Então o nosso backend tentou gravar lá na tabela:

PCINDCFV.CODINDENIZ = 803254

Porém já existia uma indenização com esse código e não dá para reescrever os dados de uma indenização em cima da outra. No caso não é uma falha nossa (Máxima).

Isso seria uma questão de cadastro, onde, na Rotina 517 o PROXNUMPEDFORCA nunca pode ser igual ao de outro RCA e também não pode existir no banco de dados do Winthor, seja na PCINDC, PCINDCFV, PCPEDCFV ou PCPEDC.

Se ele já existir em alguma tabela de histórico, então vai ocorrer isso da indenização não ser apresentada corretamente, porque não tem como sobrescrever histórico de um codindeniz que já existia no banco do Winthor.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 412222
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "a gravação não foi concluída corretamente" | "o que explica a não apresentação do registro no Winthor" | "Ação recomendada:" e os itens de recomendação explícita de verificar/garantir/validar previamente antes de nova geração/gravação | "Próximo passo: ajustar o cadastro na Rotina 517 para eliminar duplicidade no PROXNUMPEDFORCA e conferir a existência prévia do código nas tabelas citadas antes de reprocessar a indenização"
