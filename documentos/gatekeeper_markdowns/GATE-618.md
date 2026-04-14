# GATE-618 - Falha ao tentar a exclusão de rotas

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: ROTVENDN - RCA - Transferir Rota
- Natureza: Dúvida
- Atualizado em: 2025-01-10T16:51:13.721-0300

## Contexto do Problema

## Passos para reproduzir
efetuar o acesso ao roteirizador do cliente;
buscar por todos os supervisores;
buscar pelo vendedor LUIZ FELIPE MENDONÇA DA SILVA e selecionar o RCA para o roteirizar;
Clicar para excluir a ROTA1 - EXCLUIR;
Observar o resultado.

## Resultado apresentado
ocorre a falha para a exclusão da rota como observado no anexo

## Resultado esperado
é esperado que a exclusão possa ocorrer sem falhas

## Descrição
Senhores, ao tentar efetuar a exclusão de rotas, o cliente tem apresentado a seguinte mensagem:

!image-2025-01-10-09-44-43-042.png!

Ao validarmos os logs em console dessa situação, ao tentar excluir apresenta o seguinte retorno:

!https://cdn.discordapp.com/attachments/1009929379322806302/1327250284615045130/image.png?ex=678261a6&is=67811026&hm=ba4cebadebb423b502607f5cdd355b58e57509a994e9d2cb5e96f15b7469a7ee&=!

A principio, foi avaliado que há a possibilidade de essa situação ocorrer devido a falta de calculo da respectiva rota que está sendo excluída, porém se acaso a situação em questão for essa, demandaria do cliente ter um indicativo dessa necessidade para efetuar a ação, para além do alerta genérico que é exibido.

## Comentarios do Gatekeeper

### 1. 2025-01-10T16:38:37.690-0300 | Filipe do Amaral Padilha

Será encaminhado para N3, eu tentei gerar uma rota para o cliente e depois apagar e continuou apresentando o erro.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review, requires_attachment_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
