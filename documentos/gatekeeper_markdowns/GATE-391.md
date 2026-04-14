# GATE-391 - Produtos não aparecem na base do RCA (carga)

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2024-11-26T18:22:44.685-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxPedido;
>> Iniciar pedido para cliente 376618;
>> Validar que os produtos são exibidos normalmente;
>> Importar base do RCA;
>> Iniciar pedido para o mesmo cliente;

## Resultado apresentado
Na base do RCA nenhum produto é exibido para nenhum cliente.

## Resultado esperado
Produtos sendo exibidos na base do RCA.

## Descrição
Produtos sendo exibidos normalmente em base do zero, porem na base do RCA mesmo com sincronização parcial os produtos não são exibidos.

Base do RCA em anexo.

Login: topchicle.MARCUSL

## Comentarios do Gatekeeper

### 1. 2024-11-26T18:22:44.683-0300 | Filipe do Amaral Padilha

Foi realizada a carga dos dados para o RCA sincronizar e validar se agora os produtos são exibidos corretamente.

Foram reenvidas todas as dependências relacionadas aos produtos para garantir quetodos os produtos serão exibidos corretamente. Ou seja, em base zerada eram 169 disponíveis para venda no cliente e com a sincronização eu validei e isso vai descer para o RCA assim que ele realizar o processo.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 408866
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Causa identificada: as dependências relacionadas aos produtos não estavam sendo totalmente enviadas/sincronizadas no RCA." | "Em base zerada, o cliente 376618 possui 169 produtos disponíveis para venda." | "Após a sincronização, validar se os produtos passam a ser exibidos corretamente para o cliente 376618." | "Próximo passo: Aguardar ou executar a sincronização no RCA e validar a exibição dos produtos para o cliente 376618, login topchicle.MARCUSL."
