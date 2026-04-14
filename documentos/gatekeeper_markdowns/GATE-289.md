# GATE-289 - Locks no banco local

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Henrique Torres Andrade [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Banco de Dados
- Natureza: Dúvida
- Atualizado em: 2024-11-07T08:57:18.454-0300

## Contexto do Problema

## Passos para reproduzir
>> Verificar print em anexo

## Resultado apresentado
>> Locks no banco do cliente

## Resultado esperado
>> MAXSOLUCOES não causar locks no banco do cliente

## Descrição
>> Cliente informa que está com lock no banco por conta de JOBs da Máxima, porém conforme verificado na rotina 551 aparentemente no momento não existem locks. Orientado pelo Filipe Padilha a subir chamado pra GATE

## Comentarios do Gatekeeper

### 1. 2024-11-07T08:57:18.452-0300 | Filipe do Amaral Padilha

Foi feito contato com o cliente hoje de manhã 07/11/2024 e eu busquei entender com o cliente se no momento estão ocorrendo problemas com o banco de dados, no que diz respeito a LOCKs e também a muitas Sessions ativas com JOBS em execução e ele me informou que no momento não tem nada impactando no ambiente dele.

Ofereci fazer uma análise, mas ele disse que prefere entrar em contato na hora sinalizando caso tenha problemas. Então eu combinei com ele que se ele tiver problemas com o banco, referente ao assunto desse ticket, ele vai me acionar diretamente via Whatasapp para que eu possa investigar.

Obs: De fato estar ocorrendo o problema na hora é necessário porque eu preciso analisar as jobs em execução em tempo real, e também, principalmente se for LOCK. Claro que ele pode também gerar um AWR do banco que guarda esses dados, mas como não temos, ficamos acordados dessa forma.

Obs2: Já alinhei com o cliente sobre o MaxViewer e pedi para ele baixar, para deixar pronto caso precisemos conectar na hora para verificar

--Equanto agurdamos alguma ocorrência desse cliente relacionada a esse assunto, vou encerrar esse do GATE e você pode pausar o N1 como aguardando dados

## Resposta Canonica

Após contato em 07/11/2024, o cliente informou que, naquele momento, não havia impacto no ambiente relacionado a LOCKs nem excesso de sessions ativas com JOBs em execução. Assim, não houve ocorrência ativa para análise em tempo real.

Foi identificado que a investigação desse tipo de caso, especialmente envolvendo LOCK, depende de o problema estar ocorrendo no momento da análise. Embora um AWR do banco pudesse auxiliar na consulta histórica, não há AWR disponível no momento.

Ficou alinhado com o cliente o uso do MaxViewer, que deverá ser deixado preparado para eventual acesso remoto quando houver nova ocorrência. Também foi definido que, ao ocorrer novamente problema no banco relacionado a esse assunto, o cliente deverá acionar diretamente via WhatsApp para que o Gatekeeper realize a investigação em tempo real.

Dessa forma, o encaminhamento é:
- aguardar nova ocorrência para análise;
- cliente acionar via WhatsApp no momento do problema;
- N1 pausar o atendimento como aguardando dados;
- encerrar o chamado do GATE até que haja nova ocorrência.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 405464
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
