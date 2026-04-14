# GATE-197 - RCA não cumpriu todo o roteiro e mesmo assim não solicitou desbloqueio

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: N/A
- Atualizado em: 2024-10-17T16:52:50.406-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Importar a base anexada
>>Acessar a tela de clientes
>>Clicar nos 3 pontinhos
>>Ir em roteiro
>>Ir para o roteiro do dia 16/10 e assim irá ver que não consta clientes nesse roteiro do dia 16/10

Então queria entender o que está havendo, se foi por isso que não bloqueou do RCA iniciar a rota no dia seguinte, sem cumprir todo o roteiro, e também ver se não há algo que está faltando configurar

Login: ORCA.lucas
senha: acesso temporário

## Resultado apresentado
O RCA não conclui todo o roteiro planejado para o dia anterior, e o aplicativo não impede o início do roteiro do dia atual.

## Resultado esperado
Quando o RCA não concluir todo o roteiro do dia anterior, o aplicativo deve bloqueá-lo de iniciar o roteiro do dia atual.

## Descrição
O RCA 9231 não cumpriu todo o roteiro do dia anterior 16/10, e o aplicativo não bloqueou solicitando o desbloqueio para o mesmo iniciar as visitas de hoje dia 17/10.

O cliente tem ativo o parâmetro BLOQ_RCA_COM_ROTA_PENDENTE, e com isso quando um vendedor não conclui o roteiro do dia anterior, deve bloquear no outro dia solicitando o desbloqueio.

Mas ocorre que em alguns casos não está ocorrendo isso

Pelo que analisei de fato o vendedor não cumpriu todo seu roteiro do dia 16/10, faltando os clientes 114144 e 115059, que foi colocado no roteiro do dia 16/10  criado no roteirizador de vendedores.

Também notei que no MaxPedido não constou o roteiro do dia 16/10, e gostaria de entender o que ocorreu para não ter o roteiro no MaxPedido, uma vez que o mesmo foi gerado na MXSCOMPROMISSOS, e também o cliente atendeu diversos clientes do roteiro faltando somente os clientes com código 114144 e 115059.

Analisei a tabela MXSAPARELHOSDESBLOQLOG e de fato para esse RCA não teve nenhum desbloqueio.

## Comentarios do Gatekeeper

### 1. 2024-10-17T16:52:50.404-0300 | Filipe do Amaral Padilha

Em outro chamado o dev MXPEDDV-80135, recomendou usar o parâmetro PERMITIR_DELETE_HISTORICOCOMP = S para deletar os históricos junto com os compromissos, porém esse parâmetro não pode ser usado junto com a questão do roteiro pentende porque o aplicativo usa essa informação para validar o roteiro do dia anterior.

Como esse parâmetro está ativo o roteiro do dia 16/10 foi totalmente apagado junto com o histórico dele e por isso mesmo que o RCA não tenha cumprido a rota, nada foi validado no sistema. No caso o dia 16/10 é um dia que se perdeu e não tem como restaurar mais para validar o roteiro, mas agora que eu voltei o parâmetro na nuvem para PERMITIR_DELETE_HISTORICOCOMP = N, o do dia 17, será validado amanhã no dia 18/10, normalmente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 401497
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'não bloqueou o início da rota no dia seguinte, mesmo com clientes não atendidos' não está explicitamente no texto-fonte | 'Esse cenário é incompatível com a validação de bloqueio por roteiro pendente' extrapola o texto-fonte ao falar em bloqueio | 'Não utilizar PERMITIR_DELETE_HISTORICOCOMP = S em conjunto com a regra de bloqueio por roteiro pendente' menciona regra de bloqueio, que não aparece no texto-fonte
