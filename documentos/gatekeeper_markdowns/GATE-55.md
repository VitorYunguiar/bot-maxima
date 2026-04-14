# GATE-55 - Travar pedido BNF sem Saldo CC

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Pedro Henrique Rodrigues Moura
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido - Bonificado
- Natureza: Dúvida
- Atualizado em: 2024-09-12T15:48:03.068-0300

## Contexto do Problema

## Passos para reproduzir
- Login: innova.208 (Cenário testado em base zero);

>> Iniciar Pedido para qualquer cliente;
>> Alterar para BNF;
>> Inserir qualquer item e aplicar desconto que ultrapasse o limite do RCA;

Apresenta que o mesmo não possui saldo, é enviado para o gestão, porém é barrado na Integradora. Cliente quer barrar esse cenário já no MaxPedido.

## Descrição
- Cliente estava se baseando no Parâmetro: ACEITA_BNF_SEM_SALDO_CC no qual irá barrar o pedido BNF caso o mesmo esteja sem saldo de conta corrente. Aparentemente o parâmetro se trata de MaxFarma, porém o mesmo deseja que todo pedido BNF / Trocas, no qual seja utilizado o saldo do RCA e o mesmo esteja negativo, seja barrado no MaxPedido.

## Comentarios do Gatekeeper

### 1. 2024-09-12T15:48:03.066-0300 | Filipe do Amaral Padilha

Versão validada 3.235.1, então acima vai validar tambémVersão validada 3.235.1, então acima vai validar também

Foi realizado teste, quando habilito parâmetros da forma que citei, o sistema apresenta a mensagem "produto excedeu crédito do RCA" nas *Bonificações*. No pedido normal deixa transmitir mesmo se ultrapassar.

Eu habilitei os parâmetros no ambiente dele, mas configurei de forma para não barrar, para que o cliente possa optar por definir na regra dele se quer usar a configuração recomendada ou não. Atualmente está configurado por usuário ambos parâmetros e dessa forma:

PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = S

IMPEDIR_ABATIMENTO_SEMSALDORCA = N

Primeiramente, esse parâmetro não valida na apk ACEITA_BNF_SEM_SALDO_CC. Ele nem existe para validar no maxPedido.

Para barrar no maxPedido, impedindo de salvar o pedido, nós temos os parâmetros:

PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N

IMPEDIR_ABATIMENTO_SEMSALDORCA = S

Se configurar com eles o sistema já vai barrar, impedindo o RCA de inserir o item no pedido caso ultrapasse o conta corrente disponível durante a bonificação.

Plus: Enviar para a autorização de pedido parâmetros (valida pedido e bonificação):

Se quiser enviar direto para a aprovação de pedidos quando o saldo do RCA estiver insuficiente e ele ultrapassar o limite da política de descontos: parâmetro ENVIAR_PEDIDO_SEMSALDO_AUTORIZACAO = S

Esse é caso o conta corrente seja insuficiente e o RCA digitou desconto no pedido independente de ter política: Validar conta corrente do vendedor quando o desconto for dentro do teto máximo, caso não possua saldo deverá enviar o pedido para autorização.VALIDAR_CC_APROV_PEDIDO = S

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, grounding_failed, needs_review
- Comentarios primarios: 394332
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "ACEITA_BNF_SEM_SALDO_CC não existe para validação na apk" — o texto-fonte diz: "esse parâmetro não valida na apk ACEITA_BNF_SEM_SALDO_CC. Ele nem existe para validar no maxPedido." Portanto, a inexistência é atribuída ao maxPedido, não à apk. | "Para impedir o salvamento do pedido no MaxPedido" — o texto-fonte diz "barrar no maxPedido, impedindo de salvar o pedido" e também "impedindo o RCA de inserir o item no pedido", mas não usa exatamente "impedir o salvamento" como conclusão isolada; a formulação é um pouco inferida. | "Próximo passo: Alinhar com o cliente..." — isso é recomendação/advisory e não está no texto-fonte.
