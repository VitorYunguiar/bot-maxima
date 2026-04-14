# GATE-396 - Alto processamento no banco do cliente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Henrique Torres Andrade [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Banco de Dados
- Natureza: Dúvida
- Atualizado em: 2024-11-27T17:45:18.794-0300

## Contexto do Problema

## Passos para reproduzir
>> Verificado relatório AWR em anexo

## Resultado apresentado
>> Alto processamento no banco do cliente, conforme print em anexo

## Resultado esperado
>> Tabelas do MAXSOLUCOES não causar alto processamento no banco do cliente

## Descrição
>> Segundo o cliente, o banco do cliente "Reposit" está com processamento alto, por conta de vários processos do MAXSOLUCOES
>> Relatório AWR em anexo do chamado

## Comentarios do Gatekeeper

### 1. 2024-11-27T17:36:34.987-0300 | Filipe do Amaral Padilha

Enviado para N3 para resguardar uma análise de um desenvolvedor experiente, porém eu vou deixar a minha análise aqui e já uma possível solução visto que o cliente está bastante exaltado com os problemas que vem enfrentando:

Baseado na análise do AWR deles e também de casos semelhantes em outros clientes, eu sugiro a criação dos INDEX:

Quem precisa criar é o DBA ou alguém com permissão do usuário SYSTEM diretamente no banco do cliente.

CREATE INDEX SOLMAR.PCPEDC_MXS01 ON SOLMAR.PCPEDC(DTCANCEL,CONDVENDA,POSICAO, CODCOB) TABLESPACE TS_DADOS;

CREATE INDEX SOLMAR.PCPREST_MX01 ON SOLMAR.PCPREST (NUMPED) TABLESPACE TS_DADOS;

CREATE INDEX SOLMAR.PCPREST_MX02 ON SOLMAR.PCPREST (CODCOB, DTPAG, NVL (CHEQUETERCEIRO, 'N')) TABLESPACE TS_DADOS;

Coletar estatísticas:

BEGIN
DBMS_STATS.GATHER_TABLE_STATS(ownname => 'SOLMAR',
tabname => 'PCPREST', cascade => true,
estimate_percent => dbms_stats.auto_sample_size);
END;

BEGIN
DBMS_STATS.GATHER_TABLE_STATS(ownname => 'SOLMAR',
tabname => 'PCPEDC', cascade => true,
estimate_percent => dbms_stats.auto_sample_size);
END;

Feito isso ele pode já conferir se os problemas cessaram e aguardar o retorno mais completo do N3

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409132
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Afirmar que a causa provável do alto processamento no banco `Reposit` é a necessidade de criação de índices nas tabelas `SOLMAR.PCPEDC` e `SOLMAR.PCPREST` não está no texto-fonte. O texto apenas sugere a criação dos índices com base na análise do AWR e em casos semelhantes, sem citar o banco `Reposit` nem definir isso como causa provável. | Afirmar que o relato do cliente indica processamento elevado associado a processos do MAXSOLUCOES não está no texto-fonte. O texto-fonte apenas diz que o cliente está bastante exaltado com os problemas que vem enfrentando. | A expressão 'no chamado' não aparece no texto-fonte. | A formulação 'validação definitiva' depende do retorno do N3 extrapola o texto-fonte, que apenas diz para aguardar o retorno mais completo do N3. | Afirmar especificamente 'validar se o alto processamento foi eliminado' extrapola o texto-fonte, que diz para conferir se os problemas cessaram.
