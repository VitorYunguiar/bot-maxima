# GATE-575 - Permissão não sobe via sincronização

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Cobrança
- Natureza: Dúvida
- Atualizado em: 2025-01-06T10:03:44.783-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxPedido;
>> Importar base do RCA;
>> Iniciar pedido para cliente 2401

## Resultado apresentado
Pedido não inicia devido a falta de permissão de acesso a cobrança

## Resultado esperado
Permissão recebida via sincronização.

## Descrição
Permissão ja foi marcada e o pedido está iniciando normalmente na base do zero, porem na base do RCA não atualizam mesmo sincronizando e não é possivel iniciar o pedido.

Login: neoclean.neoclean22

## Comentarios do Gatekeeper

### 1. 2025-01-06T10:03:44.780-0300 | Filipe do Amaral Padilha

Foram verificados os registros da base da RCA, que geram o problema de iniciar o pedido no cliente 2401.

*Não passar ao cliente:*
Durante a análise eu constatei o seguinte:

Na verdade a RCA tem acesso a permissão da cobrança BK. O acesso se dá na tabela da apk:
SELECT * FROM mxsacessodados

O que causa o problema é que a RCA não conseguiu sincronizar com sucesso a cobrança 'BK' na tabela MXSCOB.

Eu validei os registros de logs que tínhamos disponíveis, porém o dado é de 2024-11-19 12:18:03.000
SELECT * FROM MXSCOB WHERE CODCOB IN('BK');

Então não tem mais informações que levariam a descobrir se ocorreu algum erro de base do maxPEdido, pode ter sido erro de coluna no maxPedido, pode ter sido falha de sincronização, etc.

Pode passar para a cliente:
Pra resolver eu fiz uma normalização de dados, então quando a RCA sincronizar ela vai receber essa informação da cobrança e vai resolver a situação.

Recomendo você atualizar a versão dela e ambiente porque saiu uma correção que, quando ocorre erro de sincronismo, o nosso backend reenvia a informação que falhou no processo de download.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414893
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que a cobrança BK 'não estava corretamente refletida na MXSCOB na base analisada' não está explicitamente dita no texto-fonte; o texto apenas afirma que a RCA não conseguiu sincronizar com sucesso a cobrança BK na tabela MXSCOB. | O campo 'Login: neoclean.neoclean22' não aparece no texto-fonte. | A instrução 'Aplicar a correção' não está suportada como ação específica; o texto-fonte apenas recomenda atualizar a versão e o ambiente porque já saiu uma correção.
