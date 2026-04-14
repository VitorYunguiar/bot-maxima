# GATE-570 - Pedido não aparece na autorização

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Protheus
- Assunto: MXGESN - Autorização de Pedidos - Pedidos não aparecem para autorização
- Natureza: Dúvida
- Atualizado em: 2025-01-02T17:16:16.317-0300

## Contexto do Problema

## Passos para reproduzir
Entrar no maxGestão do cliente, usuáro SYSMAX, consultar o pedido 4817.

## Resultado apresentado
Ao consultar, é verificado que o mesmo não é apresentado para a autorização, mesmo que conste com status 8 na integração.

## Resultado esperado
É esperado que o pedido conste corretamente para a autorização.

## Descrição
Cliente relata que o pedido ID_PEDIDO 185559 (NUMPED 4817) não é apresentado no maxGestão para autorização. Foi verificado na MXSINTEGRACAOPEDIDO o pedido consta com status 8, e ao verificar na MXSINTEGRACAOPEDIDO_LOGST, é verificado que o pedido não teve outros status (0, 2, 6, etc).
Foi verificado também os vinculos do usuário que realizou o pedido com a equipe do supervisor 68.

## Comentarios do Gatekeeper

### 1. 2025-01-02T17:11:01.171-0300 | Filipe do Amaral Padilha

Leia com atenção, coloquei dados internos nossos sobre a Máxima

Nunca vi isso antes, não sei como pode ter ocorrido, mas basicamente o pedido está com status 8, sendo que não passou por 0 e nem 2, e nele CODUSUARIO está = 277 (e não existe nenhum)

CODPLPAG também está nulo no pedido

CODSUPERVISOR está nulo também

CODIFILIAL nulo

E por isso o pedido não é exibido para aprovação. Nesse caso, eu penso em duas possibilidades, ou a integração do ERP deles falhou muito e gravou um registro na nuvem direto com status 8 ou o nossos aplicativo (acho bem difícil) gerou um registro todo errado com codusuario errado e demais informações inconsistentes. Bem difícil o app ter feito isso porque o codusuario nem abre o maxPedido se não estiver correto...

Enfim, algum sistema falhou de forma bem grave que gerou esse pedido com informações inconsistentes.

Se esse pedido tiver sido feito no maxPedido, então vai estar no sistema do RCA "000277" que seria o RCA GUARAVES.Jose.Rinaldo Nome JOSE RINALDO DA SILVA ALVES

Nesse caso eu recomendo orientar o RCA a duplicar o pedido e enviar novamente, conferindo os itens e reinserindo se necessário, em anexo eu coloquei um resumo do que era o pedido de acordo com o JSON.

Eu oriento a fazermos isso porque estou achando que foi a integração deles que simplesmente colocou uma informação na nossa nuvem. E para contestar isso, caso o RCA tenha o pedido no aparelho ele vai conseguir nos mandar evidenciando com a base e vai conseguir refazer o pedido. Se ele não achar o pedido, então quer dizer que pode ter sido inconsistência da integração.

*Pedir a base do RCA para que possamos entender se foi uma falha nossa do maxPedido na hora de gerar o pedido para autorização e podermos realizar demais testes usando versão ponta.

Obs: Provavelmente eles não vão ter a base e então vamos jogar a responsabilidade para a integração deles de ter gravado um pedido diretamente na nossa API com status 8 e dados inconsistentes

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414567
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Foi identificado que o pedido ID_PEDIDO 185559 / NUMPED 4817 foi gerado com dados inconsistentes. | Isso impede sua exibição para aprovação no maxGestão. | Comportamento incompatível com o fluxo esperado. | A causa mais provável é falha grave na origem do registro. | Login = GUARAVES.Jose.Rinaldo. | Caso a base seja obtida, realizar testes em versão ponta. | Se o pedido não estiver no aparelho ou não houver base, tratar o caso como possível inconsistência da integração do ERP. | a contestação deve seguir para a integração do ERP, por possível gravação direta na API com status 8 e dados inconsistentes.
