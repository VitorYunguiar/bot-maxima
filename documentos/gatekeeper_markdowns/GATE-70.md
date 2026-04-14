# GATE-70 - Não apresenta opção para atualizar as coordenadas do cliente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor Cloud
- Assunto: MXPED - Cliente - Geolocalização
- Natureza: Dúvida
- Atualizado em: 2024-09-17T13:59:45.734-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Iniciar um pedido em qualquer cliente
>>Salvar e enviar o pedido
>>E assim irá ver que não aparece a mensagem para atualizar as coordenadas do cliente

Login: jfrios.ti
Senha: dsa321

## Resultado apresentado
Não apresenta a mensagem para atualizar as coordenadas do cliente ao salvar e enviar um pedido

## Resultado esperado
Que apresente a mensagem para atualizar as coordenadas do cliente ao salvar e enviar o pedido

## Descrição
O cliente já tem ativo os parâmetros GPS_TRACKING_ENABLED  = S e CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE = S e quando finaliza um pedido, não apresenta a mensagem se deseja ou não atualizar as coordenadas do cliente.

Schema: JFRIOS_582_PRODUCAO
Service name: maxsolucoes-xios.cm35ayc6yrqh.us-east-1.rds.amazonaws.com

## Comentarios do Gatekeeper

### 1. 2024-09-17T11:44:21.211-0300 | Filipe do Amaral Padilha

Validei na versão 3.249.2, mas na versão do cliente vai funcionar também.

A mensagem não estava sendo apresentada devido a falta da permissão "Solicitar autorização para alterar coordenadas do cliente", nesse fluxo de validação do parâmetro CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE, é validada se essa permissão está ativa, assim como o GPS_TRACK_ENABLED que foi citado.

Essa permissão não vai literalmente solicitar uma autorização, essa mensagem não está muito coerente com o que a funcionalidade faz junto com o parâmetro "CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE", mas no final ela só é necessário mesmo para mostrar ou não a mensagem nesse fluxo.

Essa permissão também é válida para atualizar coordenadas do cliente através do botão "Atualizar Coordenadas" que aparece quando você preciona o dedo no cliente antes de abrir um pedido, por exemplo. Ai nesse caso em específico ele pede autorização.

Conclusão, para apresentar a amensagem de "Atualizar" ou "Não atualizar", é necessário ter a permissão e os dois parâmetros habilitados.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 395074
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma que a mensagem 'Atualizar' ou 'Não atualizar' é apresentada 'ao salvar e enviar o pedido'. O texto-fonte não menciona 'salvar e enviar o pedido', apenas diz que a mensagem é apresentada nesse fluxo e conclui que depende da permissão e dos dois parâmetros habilitados. | A resposta recomenda como 'Próximo passo' validar o comportamento após ativar a permissão, confirmando a exibição da mensagem ao salvar e enviar o pedido. Essa parte é recomendação/inferência e inclui novamente o contexto específico de 'salvar e enviar o pedido', que não está no texto-fonte.
