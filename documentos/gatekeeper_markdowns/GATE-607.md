# GATE-607 - Pedidos do RCA não aparecem

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Sincronização - Pedidos
- Natureza: Dúvida
- Atualizado em: 2025-01-10T07:29:35.313-0300

## Contexto do Problema

## Passos para reproduzir
Login: casapadim.LilianMacedo
Pedidos: 3201016992, 3201016993, 3201016994
É possível encontrar no banco nuvem através do select: SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPED IN (3201016992, 3201016993, 3201016994);

2 - Procurar os pedidos

## Resultado apresentado
Pedidos não aparecem

## Resultado esperado
Os pedidos que foram descritos deveriam aparecer.

## Descrição
Pedidos do RCA não estão aparecendo,  todos os vinculos tão corretos, os pedidos constam integrados, além disso, RCA não tem permissão de deletar o pedido. O pedido foi enviado da base do RCA mas não consta na MXSPEDIDO. Os filtros também foram limpos e nada.

## Comentarios do Gatekeeper

### 1. 2025-01-10T07:28:40.727-0300 | Filipe do Amaral Padilha

--Como os pedidos não estão na tabela MXSPEDIDO, então realmente o maxPedido não vai apresentar eles mais na timeline a não ser que uma parametrização seja realizada.

--Para os pedidos terem "sumido" dessa forma existem as seguintes possibilidades:
--RCA ter excluído os pedidos manualmente via timeline
--RCA ter importado alguma base de dados que possuía guardada, quando os pedidos não haviam sido digitados ainda
--RCA ter realizado uma limpeza dos dados do maxPedido

--Terem ativado a sincronização automática para testar e depois desativado, também pode causar essa situação onde os pedidos somem.

--Eu fiz um teste, salvei e bloqueei um pedido usando a versão da RCA, depois sincronizei e fiz swipe e não ocorreu de nenhum pedido sumir, o que levanta a hipótese de que esta realmente pode ter sido uma ação manual do usuário do sistema

--Não temos logs sobre essas ações realizadas no sistema atualmente
--Temos logs sobre erros, mas também nada foi registrado referente à falhas

--Não há evidências que o aplicativo apaga os pedidos sem ser por meio de ação manual do usuário, e também não foi possível reproduzir essa situação onde o sistema apagaria automaticamente.

--Nesse sentido, para resolver a situação recomendamos ativar o parâmetro 'PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO' porque ele vai restaurar os pedidos na timeline, provenientes do histórico de pedidos digitados pela RCA.

--Caso o cliente discorde ou algo nesse sentido, então solicite um vídeo comprovatório, exibindo o maxPedido apagando pedidos automaticamente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 416099
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Conclusão canônica" | "Foi confirmado textualmente" | "Causa apontada" | "Responsabilidade: RCA / usuário do sistema."
