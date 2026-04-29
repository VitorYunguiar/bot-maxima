# Documento de Suporte - Extrator

> Documento preparado para ingestao em banco vetorial (RAG).
> Sistema: Extrator | Maxima Solucoes | Portainer | Docker | Oracle
> Area: Suporte | Infraestrutura | Rede | DNS | Banco de dados | Integracao

---

## Sobre este documento

Este documento consolida o procedimento de suporte para diagnosticar problemas no Extrator. Ele cobre verificacoes iniciais, analise de logs no Portainer, falhas de rede/DNS, usuario Oracle bloqueado, problema de TNS NAME, falta de GRANTS no banco e locks que impedem a integracao.

Palavras-chave: extrator, Portainer, Docker, auth.solucoesmaxima.com.br, DNS, firewall, curl, nslookup, resolv.conf, daemon.json, Oracle, SQLPlus, ORA-28000, ORA-12514, ORA-12162, ORA-03135, ORA-20001, GRANTS, PCMETAPROD, lock, v$session, v$locked_object, gv$lock, DBA.

Observacao de seguranca: valores de login, senha e variaveis de ambiente devem ser omitidos ou mascarados para evitar ingestao de credenciais pelo RAG.

---

## Verificacoes iniciais

Antes de iniciar qualquer diagnostico do Extrator, confirme:

- Dados do cadastro: verificar se os dados do extrator no ambiente nuvem estao corretos.
- Conexao de internet: verificar se a internet do cliente esta funcionando.
- Versao do ambiente: verificar se o ambiente do cliente esta atualizado.
- Acesso Portainer: verificar se e possivel acessar o Portainer do cliente.

## Analise de logs no Portainer

Acesse o Portainer do cliente e verifique os logs do sistema para identificar erros ou alertas.

Procure padroes como:

- Erros de conexao de rede.
- Problemas de autenticacao.
- Timeouts em requisicoes.
- Erros de permissao, como GRANT ou permissions.
- TNS NAME nao resolvido.
- Sessoes bloqueadas no banco de dados.

### Alertas comuns

Logs do Extrator podem indicar:

- Erro indicando que a URL `auth.solucoesmaxima.com.br` esta bloqueada para acesso do extrator.
- Erro de transporte de rede, com falha de conexao do endereco de transporte TCP.
- Logs de validacao do extrator contendo campos de login e senha; os valores devem ser tratados como sensiveis e nao devem ser copiados para documentacao ou RAG.

---

## 1. Diagnostico de problemas de rede e DNS

Use este diagnostico quando houver erros de conectividade ou falha ao contactar servidores externos.

### Causas comuns

- Bloqueio de rede por firewall.
- Problemas na resolucao de DNS.
- IP nao liberado no cliente.

### Pre-requisito

Conectar ao Linux do cliente para executar os testes.

## 1.1 Teste de liberacao de IP

Objetivo: confirmar se o IP do cliente consegue acessar o servidor de autenticacao.

### Comando

```bash
curl -I http://auth.solucoesmaxima.com.br
```

### Resultado esperado de sucesso

- HTTP 200 ou HTTP 301 com redirecionamento.
- Resposta em ate 5 segundos.

Resultado esperado de sucesso:

```text
HTTP/1.1 301 Moved Permanently
Server: awselb/2.0
Content-Type: text/html
Connection: keep-alive
Location: https://auth.solucoesmaxima.com.br:443/
```

### Possiveis erros

```text
curl: (7) Failed to connect to auth.solucoesmaxima.com.br port 80 after 0 ms: Couldn't connect to server
```

```text
curl: (28) Connection timed out after 10000 milliseconds
```

### Solucao

Verificar se o IP esta liberado no firewall do cliente. Solicitar ao time de infraestrutura do cliente a liberacao do acesso.

## 1.2 Teste de resolucao DNS

Objetivo: confirmar se o DNS consegue resolver o dominio corretamente.

### Comando

```bash
nslookup auth.solucoesmaxima.com.br
```

### Resultado esperado de sucesso

Resultado esperado:

```text
Server:   1.1.1.1
Address:  1.1.1.1#53

Non-authoritative answer:
Name:    auth.solucoesmaxima.com.br
Address: 34.224.161.131
Name:    auth.solucoesmaxima.com.br
Address: 50.17.64.25
Name:    auth.solucoesmaxima.com.br
Address: 52.55.237.29
```

### Possiveis erros

```text
curl: (6) Could not resolve host: auth.solucoesmaxima.com.br
```

```text
;; communications error to 127.0.0.1#53: connection refused
;; no servers could be reached
```

### Solucao

Configurar DNS conforme os metodos abaixo.

## 1.3 Configuracao de DNS no /etc/resolv.conf

Use este metodo para resolver problemas de DNS em todo o sistema.

### Passos

1. Verificar a configuracao atual:

```bash
cat /etc/resolv.conf
```

2. Realizar backup:

```bash
cp /etc/resolv.conf /etc/resolv.conf.backup
```

3. Editar o arquivo:

```bash
cat > /etc/resolv.conf << 'EOF'
nameserver 8.8.8.8
nameserver 8.8.4.4
options ndots:0 timeout:2 attempts:1
EOF
```

4. Tornar o arquivo imutavel para nao perder a configuracao ao reiniciar:

```bash
chattr +i /etc/resolv.conf
```

5. Para editar novamente, se necessario:

```bash
chattr -i /etc/resolv.conf
```

## 1.4 Configuracao de DNS no Docker

Use este metodo quando o DHCP do cliente entrega um DNS que precisa ser sobrescrito ou quando o problema e especifico do Docker.

### Passos

1. Realizar backup:

```bash
cp /etc/docker/daemon.json /etc/docker/daemon.json.backup
```

2. Editar o arquivo via `cat`:

```bash
cat > /etc/docker/daemon.json << 'EOF'
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}
EOF
```

Opcionalmente, editar via `nano`:

```bash
nano /etc/docker/daemon.json
```

Adicionar:

```json
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}
```

3. Reiniciar Docker:

```bash
systemctl restart docker
```

ou:

```bash
service docker restart
```

Importante: sempre reinicie o extrator apos alterar configuracoes do Docker.

### Falha de deploy por DNS

Uma falha ao fazer deploy de uma stack do Extrator pode indicar erro ao baixar imagem do Docker Registry por problema temporario de resolucao de nome:

```text
failed to deploy a stack
MXS-Extrator-aclsantos Pulling
MXS-Extrator-aclsantos Error
Error response from daemon:
Get "https://registry-1.docker.io/v2/": dial tcp: lookup registry-1.docker.io:
Temporary failure in name resolution
```

Falhas de deploy/pull no Portainer podem ser causadas por DNS incorreto.

---

## 2. Diagnostico de usuario bloqueado

Use este diagnostico quando houver erros de autenticacao ou acesso negado ao banco de dados.

### Sintomas

- Erro `ORA-28000: the account is locked`.
- Falha na autenticacao mesmo com credenciais corretas.

### Diagnostico

1. Verificar na stack qual usuario e senha estao sendo utilizados.
2. Contactar o DBA do cliente para verificar o status do usuario.
3. Solicitar ao DBA que desbloqueie o usuario, se necessario.
4. Testar o acesso ao banco local do cliente com as credenciais.

### Exemplo de erro Oracle

Um erro comum em cliente Oracle/SQL pode aparecer com:

- User/schema: `MAXSOLUCOES`.
- Host: `192.168.1.200`.
- Port: `1521`.
- Service Name: `WINT`.
- Erro exibido: `ORA-28000: the account is locked`.

Nao ingerir nem reproduzir senhas em documentacao ou base vetorial.

---

## 3. Diagnostico de problema de TNS NAME

Use este diagnostico quando houver erros como `TNS:could not resolve the connect identifier` ou similar.

### Causa

O TNS Name nao esta configurado corretamente ou nao existe no banco.

### Passos para diagnostico

1. Pegar o TNS name com o cliente e conferir se as informacoes estao iguais ao cadastro do extrator.
2. Acessar o banco local do cliente e verificar os servicos disponiveis.

### SQL para verificar servicos Oracle

```sql
-- Lista todos os servicos registrados no banco
SELECT name FROM v$services;

-- Mostra o parametro service_names configurado
SELECT value FROM v$parameter WHERE name = 'service_names';
```

A consulta `SELECT value FROM v$parameter WHERE name = 'service_names';` pode retornar um valor como `BDMAXIMA`. Esse resultado confirma qual e o ServiceName correto.

3. Tentar conectar no banco com as informacoes coletadas.
4. Se conectar normalmente no banco, mas o extrator nao conseguir, testar a comunicacao via Linux instalando o SQLPlus.

### Instalacao do SQLPlus no Linux

```bash
cd /tmp

wget https://download.oracle.com/otn_software/linux/instantclient/2114000
wget https://download.oracle.com/otn_software/linux/instantclient/2114000

apt-get install -y unzip libaio1

mkdir -p /opt/oracle

unzip instantclient-basic-linux.x64-21.14.0.0.0dbru.zip -d /opt/oracle
unzip instantclient-sqlplus-linux.x64-21.14.0.0.0dbru.zip -d /opt/oracle

export ORACLE_HOME=/opt/oracle/instantclient_21_14
export LD_LIBRARY_PATH=$ORACLE_HOME
export PATH=$ORACLE_HOME:$PATH
```

Observacao: validar o URL exato do Instant Client antes de executar em ambiente real.

### Testar conexao pelo Linux

Formato:

```bash
sqlplus USUARIO/SENHA@IPDOBANCOLOCAL:1521/SERVICENAME
```

Exemplo:

```bash
sqlplus system/linuxlive@192.168.1.200:1521/WINT
```

### Resultado se conectar com sucesso

Se conectar com sucesso via SQLPlus, o DBA precisa atuar e disponibilizar o acesso ao extrator, configurando o TNS name corretamente.

### Resultado se falhar

Solicitar ao DBA para revisar a configuracao do TNS name e permissoes.

Erros comuns:

```text
ORA-12514: TNS:listener does not currently know of service requested in connect descriptor
```

```text
ORA-12162: TNS:net service name is incorrectly specified
```

```text
ORA-03135: connection lost contact
Process ID: 0
Session ID: 0 Serial number: 0
```

---

## 4. Diagnostico de falta de GRANTS no banco

Use este diagnostico quando aparecerem erros no log relacionados a permissao no banco.

### Sintomas

Exemplos de sintomas:

```text
ORA-20001: Falta permissao INSERT na tabela PCMETAPROD
ORA-20001: Falta permissao UPDATE na tabela PCMETAPROD
ORA-20001: Falta permissao DELETE na tabela PCMETAPROD
```

### Solucao

1. Acessar o script de GRANTS no link:

```text
https://docs.google.com/document/d/1Mcll7erhPBk1yO2PWRo6plS66Ow8iS6QhsNqc5KSHsI/edit?tab=t.0
```

2. Alterar o `SCHEMA WINTHOR` para o schema local do cliente.
3. Executar o script no banco como usuario `SYSTEM`, ou solicitar ao DBA para executar.
4. Testar novamente o extrator apos a execucao.

---

## 5. Diagnostico: extrator executa mas nao integra por lock no banco

Use este diagnostico quando os logs aparecem normais, mas o extrator nao consegue integrar os dados.

### Causa comum

Existem sessoes bloqueadas ou em lock no banco, impedindo o fluxo.

## 5.1 Identificar locks - VerificarSessions.sql

O script `VerificarSessions.sql` verifica todas as sessoes e locks.

Observacao: algumas linhas longas de SQL podem variar por ambiente. Validar o bloco antes de executar.

```sql
SELECT DISTINCT
  SES.PROGRAM EXECUTAVEL,
  OBJ.OBJECT_NAME TABELA,
  TO_CHAR(TRUNC(SES.LAST_CALL_ET / 60 / 60), 'FM999900') || ':' ||
  TO_CHAR(TRUNC(((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET /
  TO_CHAR(TRUNC(((((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET
  TRUNC(((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET / 60 / 60)
  SES.LAST_CALL_ET TEMPO_EM_SEGUNDOS,
  SES.STATUS,
  DECODE(LOC.LOCKED_MODE,
    1, 'NO LOCK',
    2, 'ROW SHARE',
    3, 'ROW EXCLUSIVE',
    4, 'SHARE',
    5, 'SHARE ROW EXCL',
    6, 'EXCLUSIVE',
    NULL) LOCKED_MODE,
  'alter system kill session ''' || SID || ',' || SERIAL# || ''' immediate;' COMANDO_KILL,
  SES.SID SID,
  SES.SERIAL# SERIAL#,
  SQL.SQL_TEXT TEXTO_SQL,
  SES.MACHINE MAQUINA,
  SES.USERNAME USUARIO_ORACLE,
  SES.OSUSER USUARIOS_SO
FROM
  V$SESSION SES,
  V$LOCKED_OBJECT LOC,
  DBA_OBJECTS OBJ,
  V$SQL SQL
WHERE
  SES.SID = LOC.SESSION_ID
  AND LOC.OBJECT_ID = OBJ.OBJECT_ID
  AND SES.SQL_ADDRESS = SQL.ADDRESS(+)
ORDER BY SES.LAST_CALL_ET DESC;
```

## 5.2 Identificar objetos bloqueados - VerificarObjetosLock.sql

O script `VerificarObjetosLock.sql` verifica objetos bloqueados.

Observacao: algumas linhas longas de SQL podem variar por ambiente. Validar o bloco antes de executar.

```sql
SELECT
  DECODE(L.BLOCK, 0, 'Em espera', 'Bloqueando ->') USER_STATUS,
  L.BLOCK,
  CHR(39) || S.SID || ',' || S.SERIAL# || CHR(39) SID_SERIAL,
  (SELECT INSTANCE_NAME FROM GV$INSTANCE WHERE INST_ID = L.INST_ID) CONN_,
  S.SID,
  S.PROGRAM,
  S.SCHEMANAME,
  S.OSUSER,
  S.MACHINE,
  DECODE(L.TYPE,
    'RT', 'Redo Log Buffer',
    'TD', 'Dictionary',
    'TM', 'DML',
    'TS', 'Temp Segments',
    'TX', 'Transaction',
    'UL', 'User',
    'RW', 'Row Wait',
    L.TYPE) LOCK_TYPE,
  DECODE(L.LMODE,
    0, 'None',
    1, 'Null',
    2, 'Row Share',
    3, 'Row Excl.',
    4, 'Share',
    5, 'S/Row Excl.',
    6, 'Exclusive',
    LTRIM(TO_CHAR(LMODE, '990'))) LOCK_MODE,
  CTIME,
  OBJECT_NAME,
  TO_CHAR(TRUNC(S.LAST_CALL_ET / 60 / 60), 'FM999900') || ':' ||
  TO_CHAR(TRUNC(((S.LAST_CALL_ET / 60 / 60) - TRUNC(S.LAST_CALL_ET / 60 /
  TO_CHAR(TRUNC(((((S.LAST_CALL_ET / 60 / 60) - TRUNC(S.LAST_CALL_ET / 60
  TRUNC(((S.LAST_CALL_ET / 60 / 60) - TRUNC(S.LAST_CALL_ET / 60 / 60)) *
  S.LAST_CALL_ET TEMPO_EM_SEGUNDOS,
  L.TYPE,
  L.LMODE
FROM
  GV$LOCK L
  JOIN GV$SESSION S ON (L.INST_ID = S.INST_ID AND L.SID = S.SID)
  JOIN GV$LOCKED_OBJECT O ON (O.INST_ID = S.INST_ID AND S.SID = O.SESSION_ID)
  JOIN DBA_OBJECTS D ON (D.OBJECT_ID = O.OBJECT_ID)
WHERE
  (L.ID1, L.ID2, L.TYPE) IN (SELECT ID1, ID2, TYPE FROM GV$LOCK WHERE REQUEST > 0)
ORDER BY TEMPO_EM_SEGUNDOS DESC;
```

### Acoes recomendadas para locks

1. Executar ambos os scripts para ter uma visao completa das sessoes e locks.
2. Identificar qual sessao ou objeto esta travando o processamento.
3. Solicitar ao DBA ou cliente para matar as sessoes problematicas usando o comando gerado.
4. Reiniciar o extrator apos liberar os locks.
5. Monitorar se o problema persiste.

---

## Resumo de diagnostico

| Problema | Causa provavel | Acao inicial |
| --- | --- | --- |
| Conexao recusada | Firewall ou IP nao liberado | Executar `curl` para validar |
| DNS nao resolvido | Configuracao DNS errada | Reconfigurar `/etc/resolv.conf` ou Docker DNS |
| Autenticacao falha | Usuario bloqueado | Contactar DBA para desbloquear |
| TNS NAME nao resolvido | TNS nao configurado | Executar scripts SQL para validar |
| Permissao negada | GRANTS insuficientes | Executar script de GRANTS |
| Nao integra com logs normais | Lock no banco | Executar scripts de verificacao de locks |

---

## Guia rapido de decisao

Se o log cita `auth.solucoesmaxima.com.br`, erro de rede, timeout, `Could not resolve host`, `Temporary failure in name resolution` ou `no servers could be reached`, priorize o diagnostico de rede e DNS.

Se o log cita `ORA-28000`, verifique usuario Oracle bloqueado e acione o DBA para desbloqueio.

Se o log cita `TNS`, `connect identifier`, `ORA-12514`, `ORA-12162` ou `ORA-03135`, valide TNS name, ServiceName, conectividade via SQLPlus e permissoes com o DBA.

Se o log cita `ORA-20001` e falta de permissao `INSERT`, `UPDATE` ou `DELETE` em tabela, execute o fluxo de GRANTS.

Se os logs parecem normais, mas o extrator nao integra dados, investigue locks no banco usando os scripts de sessao e objetos bloqueados.
