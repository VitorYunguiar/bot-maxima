# GATE-806 - Trajeto Planejado Não Exibido no Mapa

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral - Mapa Vendedores
- Natureza: Dúvida
- Atualizado em: 2025-02-17T09:04:55.703-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar maxGestão
>> Ir em Geolocalização, mapas, ir em filtro, busca por qualquer RCA, clicar RCA, ver clientes, Clica em "Trajeto Planejado" e "Trajeto Executado"
(Fiz o teste no RCA 13, peguei dos clientes dele e analisei no banco de dados 16667,10675)

## Resultado apresentado
Ao clicar em Trajo Planejo o sistema informa que Não Possui trajeto Planejado.

## Resultado esperado
Que aparece o trajeto planejado

## Descrição
O cliente está reclamando que o MaxGestão deixou de exibir o trajeto planejado no mapa.

Antes, a funcionalidade funcionava mesmo quando havia informações incorretas nos cadastros dos clientes, exibindo-os em locais errados, mas ainda assim apareciam no trajeto. Agora, nada é exibido, e foi informado que isso ocorre por falta de latitude e longitude nos cadastros.

O cliente destaca que:

- Antes, só precisavam ajustar as coordenadas quando um cliente aparecia no lugar errado no mapa.

- Atualmente, seria inviável preencher manualmente esses dados para mais de 16 mil clientes.

- A funcionalidade já funcionava sem essa exigência antes.
-----------------------------------------------------------------------------------------------------
- Verifiquei alguns clientes na MXSCLIENT onde foi visto que a latitude e a longitude estão como NULL.

- Verifiquei MXLOCALIZACAOCLIENTE e lá aparece a latitude e a longitude, também foi visto que mxscompromissos também tem informações.

- ERP_MXSROTACLI também tem rota cadastrada

## Comentarios do Gatekeeper

### 1. 2025-02-17T08:17:43.269-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 para obtermos a opinião do desenvolvimento sobre o assunto

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
