# GATE-761 - API DE CANCELAMENTO COM ERRO

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXPED - API de Cancelamento
- Natureza: Dúvida
- Atualizado em: 2025-02-07T16:59:06.611-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar maxPedido com qualquer usuário, enviar pedidos e logo depois cancelar.

## Resultado apresentado
>> Não esta cancelando os pedidos, dando critica de API CANCELADA INVALIDA.

## Resultado esperado
>> Que os RCA consegui cancelar os pedidos enviados

## Descrição
Foi feita a troca de IP na stack do extrator: o IP antigo (192.168.0.9:8180) foi alterado para o novo IP (192.168.9.25:8180).

Mesmo após a mudança, o cliente ainda não consegue cancelar os pedidos no MaxPedido.

Foi realizado um teste utilizando o IP local para acessar o Winthor Anywhere, e o acesso foi realizado com sucesso.

## Comentarios do Gatekeeper

### 1. 2025-02-07T16:59:06.609-0300 | Filipe do Amaral Padilha

A autenticação não estava funcionando devido à identação da variável na Stack (compose) do cliente.

Para resolver eu fiz o seguinte:

Acessei o http://lutan.teleba.net.br:9000/

entrei na stack e substituí a variável:
LINK_API_WINTHOR_CANCELAMENTO: http://192.168.0.25:8180

Substituí por:
LINK_API_WINTHOR_CANCELAMENTO: http://192.168.0.25:8180/

Depois fiz o deploy, baixei o maxPedido na versão 4.000.8 e simulei o uso da API.

Pedido cancelado com sucesso via API:

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPEDRCA IN(282710440);

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 422488
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma 'autenticação da API de cancelamento', mas o texto-fonte menciona apenas 'a autenticação' e não especifica explicitamente 'API de cancelamento'. | A seção 'Ação recomendada' traz recomendações ('Manter a variável...', 'Realizar/garantir o deploy...', 'Validar com o cliente...') que não constam no texto-fonte. | A afirmação 'o cancelamento via API voltou a funcionar' é uma inferência. O texto-fonte confirma sucesso no teste ('Pedido cancelado com sucesso via API'), mas não diz explicitamente que 'voltou a funcionar' em termos gerais.
