# GATE-668 - Valores gravados incorretos no JSON do pedido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXPED - Campanha - Desconto Progressivo
- Natureza: Dúvida
- Atualizado em: 2025-01-21T12:50:11.613-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar banco nuvem
>Consultar (SELECT * FROM MXSINTEGRACAOPEDIDO m WHERE NUMPEDERP = '3408409997';)
>Observar os campos PrecoVenda e PrecoBase no JSON do pedido referente aos produtos 1935856002, 1935855003, 361003

>Consultar (SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED = 3408409997 AND CODPROD IN(1935856002, 1935855003, 361003);)
>Observar os campos PVENDA e PBASERCA

## Resultado apresentado
No JSON foi gravado o PrecoVenda = 35.52 que é o preço cheio, ou seja, 2,96 * 12 (fator) = 35,52. Enquanto o preço que deveria ter sido gravado é de 2,96.

## Resultado esperado
Saber como podemos corrigir isso nos pedidos que já foram processados

## Descrição
Bom dia, Carlos / Filipe,

Identifiquei um problema na DESTRO que possivelmente ocorreu antes da correção do MXPEDDV-86344.

No JSON, foi gravado o campo PrecoVenda como 35,52, que corresponde ao preço cheio (2,96 * 12 [fator] = 35,52). Contudo, o valor correto que deveria ter sido gravado é 2,96.

No contexto do MXPEDDV-86344, foi confirmado que se tratava de um erro já corrigido. Entretanto, outros pedidos criados antes dessa versão ainda não foram identificados pelo cliente, o que pode impactar relatórios futuros. Esse caso específico já gerou confusões nos relatórios do MaxGestão.

Detalhes do Pedido:

PEDIDO: 3408409997
CODPROD: 1935856002, 1935855003, 361003
CODUSUARIO: 20645

## Comentarios do Gatekeeper

### 1. 2025-01-21T12:50:11.609-0300 | Filipe do Amaral Padilha

Foram verificados dados específicos de dois RCAs da Destro:
Rcas desses pedidos ->
SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP IN(3408409997, 3408434351);

Durante a análise observei que estão usando versão 3.257.0 e nessa versão, ainda não existe a correção para a aplicação do desconto PRG feita no ticket (MXPEDDV-86344)

E acredito que as coisas estejam interligadas. Porque os itens entram no Json do pedido com descontoprogressivo = true, porém não sofrem a alteração do desconto. Isso já é suficiente para os itens gravarem no relatório. Porém como não tem o desconto progressivo, os itens ficam com o totalizar de desconto zerado.

Como no cenário do ticket informado os valores estavam negativos, eu fiz o ajuste do dado diretamente na MXSHISTORICOPEDI:
SELECT * FROM MXSHISTORICOPEDI WHERE NUMPED IN(3408409997) AND CODPROD IN(1935856002, 1935855003, 361003);

Antes o valor estava conforme o precoVenda do JSON e foi alterado para o pvenda e ptabela serem iguais.

Nesse caso, com os dados retroativos, não tem o que possa ser feito, o relatório vai apresentar inconsistências, itens sem desconto progressivo aplicado devido ao uso da versão antiga.

O ideal é que eles mudem de versão seja para a última antes da V4 ou para a própria V4. Digo isso só pela questão do Layout que muda. Eles precisam da migração em massa dos RCAs para o desconto progressivo funcionar corretamente tanto a nível de venda quanto de relatórios.

Feitas as mudanças de versão, é só acompanhar o relatório para ver se ainda terão casos de preço de venda = preço de tabela e desconto nulo

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 418019
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que, nesse cenário, o preço de venda acaba ficando igual ao preço cheio / preço de tabela não está totalmente suportada como regra geral. O texto-fonte diz que, no caso ajustado, o valor estava conforme o precoVenda do JSON e foi alterado para que pvenda e ptabela ficassem iguais, e recomenda acompanhar casos de preço de venda = preço de tabela e desconto nulo, mas não afirma que isso necessariamente ocorre sempre nesse cenário. | A formulação 'não há ação corretiva possível' é mais forte que o texto-fonte. O texto diz: 'com os dados retroativos, não tem o que possa ser feito, o relatório vai apresentar inconsistências', o que suporta a ideia prática, mas não literalmente como impossibilidade absoluta de ação corretiva em qualquer sentido.
