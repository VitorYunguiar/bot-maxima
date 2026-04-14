# GATE-447 - PCTABPRCLI e MXSTABPRCLI divergentes

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Tabela de Preços
- Natureza: Dúvida
- Atualizado em: 2024-12-04T16:50:23.579-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar a base do RCA em anexo
>>Iniciar pesido para o cliente 2619 e incluir um produto (2641 de exemplo)

## Resultado apresentado
>>O valor que aparece pertence a região 1 e não a 2 que está cadastrada na PCTABPRCLI

## Resultado esperado
>>A PCTABPRCLI e a MXSTABPRCLI devem estar iguais
>>O valor que aparece para o cliente deve ser correspondente a região cadastrada na 3314 (PCTABPRCLI )

## Descrição
>>Cliente diz que ao cadastrar na rotina 3314 o maxPedido ainda não está validando a região cadastrada

>>Verifiquei que o cliente 2619 de exemplo possui registro na PCTABPRCLI, mas não na MXSTABPRCLI

>>Segundo o cliente são vários casos.

## Comentarios do Gatekeeper

### 1. 2024-12-04T16:43:19.846-0300 | Filipe do Amaral Padilha

A nossa trigger da PCTABPRCLI só sobe dados se a filial de importação configurada do registro estiver configurada na tabela PCMXSCONFIGURACOES.

Como o registro é da filial 3, e na PCMXSCONFIGURACOES o CODFILIAL_IMPORTACAO = 3 não estava configurado, o registro não subiu.

Então para resolver eu configurei a filial 3 na CODFILIAL_IMPORTACAO da PCMXSCONFIGURACOES no banco local do cliente.

Depois fiz a carga de filial nova, no caso filial 3.

Enviei o ticket para a TECH só porque me solicitaram para formalizar

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410374
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "por isso, o registro não foi enviado para a MXSTABPRCLI" — o texto-fonte diz apenas que "o registro não subiu", sem explicitar que o destino era a tabela MXSTABPRCLI. | "A divergência entre PCTABPRCLI e MXSTABPRCLI não está na validação da região em si" — o texto-fonte não menciona validação de região nem divergência entre essas tabelas. | "Ação recomendada" — o texto-fonte relata ações já realizadas (configurar a filial 3 e fazer a carga), não apresenta isso como recomendação. | "Próximo passo - Formalizar o atendimento com envio do ticket para a TECH" — o texto-fonte diz que o ticket já foi enviado para a TECH, não que isso seja um próximo passo.
