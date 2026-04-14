# GATE-514 - ferramenta de desbloqueio não gerando a senha de desbloqueio

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXGESN - Autorização de Pedidos - Permissões
- Natureza: N/A
- Atualizado em: 2024-12-17T08:00:29.828-0300

## Contexto do Problema

## Passos para reproduzir
efetuar alguma solicitação de desbloqueio no app do maxpedido (no cenário de exemplo foi check-in fora do raio) e tentar gerar a chave de desbloqueio

## Resultado apresentado
chave de desbloqueio indefinida

## Resultado esperado
é esperado que a chave seja gerada sem falhas

## Descrição
Senhores, está acontecendo uma situação a qual não identifiquei a causa raiz dessa situação:

ao tentar gerar senha de desbloqueio utilizando a versão ponta do app maxpedido:

!image-2024-12-16-17-54-01-172.png!

o codigo que o PWA gera é apresentado como undefinied:

!image-2024-12-16-17-55-22-293.png!

isso é um cenário de falha do app? se sim, é problema no PWA ou APK do maxpedido?

login maxpedido: pacaluz.26

login maxgestao: pacaluz.5549

## Comentarios do Gatekeeper

### 1. 2024-12-17T07:57:53.761-0300 | Filipe do Amaral Padilha

Será enviado para N3.
Ticket em N3 -> https://suporte.maximatech.com.br/browse/MXGESNDV-15659

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
