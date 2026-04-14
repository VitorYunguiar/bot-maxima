# Base de Conhecimento – Utilitários, Instalação e Scripts

## Sumário

2. [Instalação e Reinstalação de Extratores](#2-instalação-e-reinstalação-de-extratores)
   - 2.1 [Solicitação de Dados ao Cliente](#21-solicitação-de-dados-ao-cliente)
   - 2.2 [Passo a Passo da Instalação](#22-passo-a-passo-da-instalação)
       - 2.2.1 [Acesso via SSH e Validação de Ambiente](#221-acesso-via-ssh-e-validação-de-ambiente)
       - 2.2.2 [Remoção de Snaps e Docker Antigo](#222-remoção-de-snaps-e-docker-antigo)
       - 2.2.3 [Instalação/Atualização do Docker](#223-instalaçãoatualização-do-docker)
       - 2.2.4 [Preparação do Ambiente](#224-preparação-do-ambiente)
       - 2.2.5 [Instalação do Portainer](#225-instalação-do-portainer)
   - 2.3 [Configuração do Compose](#23-configuração-do-compose)
   - 2.4 [Liberação de Portas e IPs](#24-liberação-de-portas-e-ips)

3. [Scripts e Consultas SQL Úteis](#3-scripts-e-consultas-sql-úteis)
   - 3.1 [Metas](#31-metas)
   - 3.2 [Verificação Antes de Executar DECLARE](#32-verificação-antes-de-executar-declare)
   - 3.3 [Estoque de Produtos](#33-estoque-de-produtos)
   - 3.4 [Configuração do Processador de Fotos](#34-configuração-do-processador-de-fotos)
   - 3.5 [Descobrir Código do RCA](#35-descobrir-código-do-rca)
   - 3.6 [Produto Não Aparece – Forçar Envio](#36-produto-não-aparece--forçar-envio)
   - 3.7 [Produto Não Aparece – Tabelas Winthor e Nuvem](#37-produto-não-aparece--tabelas-winthor-e-nuvem)
   - 3.8 [Reprocessar Tabelas](#38-reprocessar-tabelas)
   - 3.9 [Reprocessar MXSTABPR](#39-reprocessar-mxstabpr)
   - 3.10 [Verificar se Usa Integradora Padrão](#310-verificar-se-usa-integradora-padrão)
   - 3.11 [Horário do Banco](#311-horário-do-banco)
   - 3.12 [Verificar Preços Divergentes](#312-verificar-preços-divergentes)
   - 3.13 [Sessões Ativas no Banco](#313-sessões-ativas-no-banco)
   - 3.14 [Verificar Locks](#314-verificar-locks)
   - 3.15 [Validação de Envio de Endpoints Obrigatórios](#315-validação-de-envio-de-endpoints-obrigatórios)
   - 3.16 [Acompanhamento de Carga](#316-acompanhamento-de-carga)
   - 3.17 [Usuários que Realizaram Pedidos nos Últimos 15 Dias](#317-usuários-que-realizaram-pedidos-nos-últimos-15-dias)
   - 3.18 [Pedido Não Aparece – Checklist Nuvem](#318-pedido-não-aparece--checklist-nuvem)
   - 3.19 [Cancelar Pedido no Sankhya](#319-cancelar-pedido-no-sankhya)
   - 3.20 [Consultas de Metas](#320-consultas-de-metas)
   - 3.21 [Cálculo de Valor de Pedidos](#321-cálculo-de-valor-de-pedidos)
   - 3.22 [Carga de MXSHISTORICOPEDC e MXSHISTORICOPEDI](#322-carga-de-mxshistoricopedc-e-mxshistoricopedi)
   - 3.23 [Jobs do Oracle](#323-jobs-do-oracle)
   - 3.24 [Apuração de Carga (Winthor)](#324-apuração-de-carga-winthor)
   - 3.25 [Saber se Cliente foi Excluído da Carteira do RCA](#325-saber-se-cliente-foi-excluído-da-carteira-do-rca)
   - 3.26 [Usuários Ativos e Inativos](#326-usuários-ativos-e-inativos)
   - 3.27 [Relatórios de Vendas por RCA](#327-relatórios-de-vendas-por-rca)
   - 3.28 [Menu Objetivo – Totais](#328-menu-objetivo--totais)
   - 3.29 [Parâmetros de Check-in/Check-out](#329-parâmetros-de-check-incheck-out)
   - 3.30 [Carga Manual de Dados por Tabela](#330-carga-manual-de-dados-por-tabela)
   - 3.31 [Cálculo do Campo ValorST](#331-cálculo-do-campo-valorst)

4. [Configurações Diversas](#4-configurações-diversas)
   - 4.1 [Preço Mínimo de Pedido por Plano de Pagamento](#41-preço-mínimo-de-pedido-por-plano-de-pagamento)
   - 4.2 [Conta Corrente de RCA](#42-conta-corrente-de-rca)
   - 4.3 [Cadastro de Metas no Winthor](#43-cadastro-de-metas-no-winthor)
   - 4.4 [Habilitar MaxGestão](#44-habilitar-maxgestão)
   - 4.5 [Importação de Filial](#45-importação-de-filial)

## 2. Instalação e Reinstalação de Extratores

### 2.1 Solicitação de Dados ao Cliente

Os mesmos dados listados na seção 1.2 são necessários para a instalação/reinstalação.

### 2.2 Passo a Passo da Instalação

#### 2.2.1 Acesso via SSH e Validação de Ambiente

1. Acessar a máquina Linux via Putty (ou outro cliente SSH) utilizando o IP e porta fornecidos.
2. Solicitar ao cliente a liberação das portas necessárias (ver seção 2.4).
3. Após o login, executar `sudo su` para tornar-se root.
4. Validar o ambiente com o comando:
   ```bash
   sudo curl -sL http://go.maximasist.com.br/validador/start.sh | bash
   ```

#### 2.2.2 Remoção de Snaps e Docker Antigo

Caso necessário, remover snaps e versões antigas do Docker:

```bash
# Verificar snaps instalados
snap list

# Remover snaps
snap remove snapd ; sudo apt purge snapd -y ; sudo apt-mark hold snapd ; sudo apt autoremove -y

# Verificar se há múltiplos containers (indicando mais de um cliente)
docker ps -a

# Desinstalar o Docker completamente
sudo apt-get purge -y docker* ; sudo apt-get autoremove -y --purge docker* ; sudo rm -rf /var/lib/docker /etc/docker ; sudo rm /etc/apparmor.d/docker ; sudo groupdel docker ; sudo rm -rf /var/run/docker.sock
```

#### 2.2.3 Instalação/Atualização do Docker

```bash
# Atualizar pacotes e instalar dependências
sudo apt update
sudo apt-get remove docker docker-engine docker.io containerd runc -y
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

Alternativamente, usar o script oficial do Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
docker version   # Verificar instalação
```

#### 2.2.4 Preparação do Ambiente

Baixar e executar o script de preparação:

```bash
wget -q https://maxsolucoes-versoes.s3.amazonaws.com/extrator/v2/install/ambiente.sh
chmod +x ambiente.sh
sh ambiente.sh
```

#### 2.2.5 Instalação do Portainer

```bash
docker run -d -p 9000:9000 --name MXS_Portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce --admin-password '$2y$05$Xb5IB53HjCQqfD/7k9F2d.thkVspomm/2udcI6/dg8Q6nKJ9ZOZda' --logo "https://maxsolucoes-versoes.s3.amazonaws.com/extrator/v1/logo/logo-maxima.png"
```

Verificar se o container está ativo:

```bash
docker ps -a
```

### 2.3 Configuração do Compose

Modelo de arquivo `docker-compose.yml` para o extrator:

```yaml
version: '3'
 
services:
    MXS-Extrator-parente:
        privileged: true
        image: dockermaxima/extrator:3.1.2.503
        healthcheck:
            test: ["CMD-SHELL", "/bin/healthcheck.sh"]
            interval: 1m30s
            timeout: 10s
            retries: 5
        environment:
            USUARIO_EXTRATOR_NUVEM: PARENTE.parenteferragensprod
            SENHA_EXTRATOR_NUVEM: 6CJLhkDzQHzSyQn0kwqpwXzavaxDjYMnlciyIJOJlxHN+JOEH2s5NmQoyfxYcQa8
            USUARIO_SYSTEM_WINTHOR: SYSTEM
            SENHA_SYSTEM_WINTHOR: 4Z/ceyCgNRhVVguiZ1OIfg==
            TZ: America/Sao_Paulo
            #DIRETORIO_FOTOS_WINTHOR: \\...       
        container_name: MXS-Extrator-parente
        restart: always
        network_mode: bridge
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock
            - /app/maxima/MXS_Extrator/imagens_data_parente:/mnt/maxima/produtos_fotos
            - /app/maxima/MXS_Extrator/extrator_prd_data_parente/Conf:/app/maxima_extrator/extrator_prd/Conf
            - /app/maxima/MXS_Extrator/extrator_prd_data_parente/LOGS:/app/maxima_extrator/extrator_prd/LOGS
            - /app/maxima/MXS_Extrator/extrator_prd_data_parente/id:/app/maxima
        tty: true
        ports:
            - 9002:81/tcp
```

### 2.4 Liberação de Portas e IPs

**Portas a liberar no firewall (TCP):**
- 9000, 9001, 9002, 9003, 10050, 10051, 8000, 9443, 22 (SSH)

**IPs da AWS (nuvem Máxima):**
- 3.81.180.245
- 3.81.180.2
- 34.236.34.79

**IPs da Máxima (outros serviços):**
- 207.191.170.250
- 200.225.244.33
- 177.43.92.98

**URLs e portas para teste de conectividade:**
- `https://intext-hmg.solucoesmaxima.com.br:81/api/v1/`
- `https://intpdv-hmg.solucoesmaxima.com.br:81/api/v1/`
- `https://appsv.solucoesmaxima.com.br:8081/`
- `https://intext-tst-cache.solucoesmaxima.com.br:81/api/v1`
- `https://intext-03.solucoesmaxima.com.br:81/api/v1/`
- `https://intpdv-unificado.solucoesmaxima.com.br:81/api/v1/`
- `https://intext-02.solucoesmaxima.com.br:81/api/v1/`
- `https://intext-04.solucoesmaxima.com.br:81/api/v1/`

---

## 3. Scripts e Consultas SQL Úteis

### 3.1 Metas

```sql
DEFINE_META_GRAFICO = 0 
UTILIZAR_META_TRANSMITIDA_EM_TIPO_ZERO = 'S' 
CRITERIO_VENDA_GRAFICO = "L", "F" ou "T" 
-- Caso seja usada qualquer letra diferente, desde que não seja nulo ou vazio, valor transmitido será utilizado como default, em caso de nulo ou vazio, fluxo antigo será executado

-- Caso DEFINE_META_GRAFICO ou UTILIZAR_META_TRANSMITIDA_EM_TIPO_ZERO não siga o padrão acima, será utilizado o valor atingido do mix
```

### 3.2 Verificação Antes de Executar DECLARE

```sql
SELECT COUNT (*) FROM TABELA; -- SE MAIS DE 30K REGISTROS, FAZER DECLARE COM WHERE
```

### 3.3 Estoque de Produtos

```sql
SELECT QTESTGER - QTRESERV - QTBLOQUEADA FROM MXSEST WHERE CODFILIAL = ? AND CODPROD = ?
```

### 3.4 Configuração do Processador de Fotos

Arquivo de configuração XML para processador de fotos (exemplo):

```xml
<?xml version="1.0" encoding="utf-8"?> 
<configuration> 
    <startup> 
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.7.2" /> 
    </startup> 
    <appSettings> 
        <add key="OraclePath" value="C:\MaximaSistemas\Oracle\instantclient_11_1_X86" /> 
        <add key="Operacao" value="0" /> 
        <add key="Aplicacao" value="0" /> 
        <add key="DirPath" value="C:\Fotos" /> 
    </appSettings> 
    <connectionStrings> 
        <add name="OracleConnectionString" connectionString="User ID=MXSPEDIDOVENDA; Password=urxi2638; Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=7.216.54.198)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=WINT)))" providerName="System.Data.OracleClient" /> 
    </connectionStrings> 
</configuration>
```

### 3.5 Descobrir Código do RCA

```sql
select * from mxsusuarios where codusur = <codigo_erp>;
edit mxsaparelhosusuarios where codusuario = <codusuario>;
select * from mxsaparelhosconnlog where codusuario = <codusuario> order by 11 desc;
```

### 3.6 Produto Não Aparece – Forçar Envio

```sql
DECLARE 
BEGIN 
    FOR REGISTRO IN (SELECT * FROM MXSPRODUT WHERE CODPROD IN (<lista>)) LOOP 
        SYNC.PRC_MXSPRODUT (0, REGISTRO, REGISTRO); 
        COMMIT; 
    END LOOP; 
END;
```

### 3.7 Produto Não Aparece – Tabelas Winthor e Nuvem

**Tabelas Winthor:**

```sql
select qtunit, codprod, dtexclusao, revenda, ENVIARFORCAVENDAS, codfornec, codepto, codsec from pcprodut where codprod in (XX); 
select codprod, revenda, ENVIARFORCAVENDAS, codfilial from pcprodfilial where codprod in (XX); 
select qtunit, enviafv, codfilial, e.* from pcembalagem e where codprod in (XX);
select codfornec, revenda from pcfornec where codfornec in (YY); 
select * from pcdepto where codepto in (ZZ); 
select * from pcsecao where codsec in (TT);
select * from pctabpr where codprod in (XX);
```

**Tabelas na nuvem (MXS):**

```sql
select c.qtunit, c.* from mxsprodut c where codprod in (XX);
select * from mxsprodfilial where codprod in (XX); 
select c.qtunit, c.* from mxsembalagem c where codprod in (XX); 
select * from mxsfornec where codfornec in (YY); 
select * from mxsdepto where codepto in (ZZ);
select * from mxssecao where codsec in (TT); 
select * from mxstabpr where codprod in (XX); 
select * from sync_mxsprodut where codprod in (XX) order by dtatualiz desc;
select * from sync_mxsprodfilial where codprod in (XX) order by dtatualiz desc;
select * from sync_mxsembalagem where codprod in (XX) order by dtatualiz desc; 
select * from sync_mxsfornec where codfornec in (YY) order by dtatualiz desc;
select * from sync_mxsdepto where codepto in (ZZ) order by dtatualiz desc;
select * from sync_mxssecao where codsec in (TT) order by dtatualiz desc;
select * from sync_mxstabpr where codprod in (XX) order by dtatualiz desc;
```

### 3.8 Reprocessar Tabelas

```sql
DECLARE
BEGIN 
    FOR REGISTRO IN (SELECT * FROM MXSCODCLI) LOOP 
        SYNC.PRC_MXSPRODUT (0, REGISTRO, REGISTRO); 
        COMMIT; 
    END LOOP; 
END;
```

### 3.9 Reprocessar MXSTABPR

```sql
BEGIN 
    FOR REGISTRO IN (SELECT * FROM MXSTABPR WHERE CODPROD IN 
        ( 
            SELECT DISTINCT(CODPROD) FROM PCTABPR WHERE DTULTALTPVENDA > SYSDATE - 15 
        )) LOOP
        SYNC.PRC_MXSTABPR(0, REGISTRO, REGISTRO); 
        COMMIT;
    END LOOP; 
END;
```

### 3.10 Verificar se Usa Integradora Padrão

```sql
select * from mxsconfigdata where nome like '%USAR_INTEGRADORA_PADRAO%';
```

### 3.11 Horário do Banco

```sql
select sysdate from dual;
```

### 3.12 Verificar Preços Divergentes

```sql
select * from pcpedifv where numpedrca = 00000;
select * from pctabpr where codprod = 00000;
select * from pcpedcfv where numpedrca = 00000;
```

### 3.13 Sessões Ativas no Banco

```sql
SELECT DISTINCT SES.PROGRAM EXECUTAVEL,
    TO_CHAR(TRUNC(SES.LAST_CALL_ET / 60 / 60), 'FM999900') || ':' ||
    TO_CHAR(TRUNC(((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60), 'FM00') || ':' ||
    TO_CHAR(TRUNC(((((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60) -
        TRUNC(((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60)) * 60), 'FM00') TEMPO,
    SES.LAST_CALL_ET TEMPO_EM_SEGUNDOS,
    SES.STATUS,
    'alter system kill session ''' || SID || ',' || SERIAL# || ''' immediate;' COMANDO_V2,
    SES.SID SID,
    SES.SERIAL# SERIAL#,
    SQL.SQL_TEXT TEXTO_SQL,
    SES.MACHINE MAQUINA,
    SES.USERNAME USUARIO_ORACLE,
    SES.OSUSER USUARIOS_SO
  FROM GV$SESSION       SES,
       GV$SQL           SQL
 WHERE SES.SQL_ADDRESS = SQL.ADDRESS(+)
 AND UPPER(SES.USERNAME) LIKE '%MAXSOLUCOES%'
 ORDER BY SES.LAST_CALL_ET DESC;
```

### 3.14 Verificar Locks

```sql
SELECT DISTINCT SES.PROGRAM EXECUTAVEL,
    TO_CHAR(TRUNC(SES.LAST_CALL_ET / 60 / 60), 'FM999900') || ':' ||
    TO_CHAR(TRUNC(((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60), 'FM00') || ':' ||
    TO_CHAR(TRUNC(((((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60) -
        TRUNC(((SES.LAST_CALL_ET / 60 / 60) - TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60)) * 60), 'FM00') TEMPO,
    SES.LAST_CALL_ET TEMPO_EM_SEGUNDOS,
    SES.STATUS,
    'alter system kill session ''' || SID || ',' || SERIAL# || ''' immediate;' COMANDO_V2,
    SES.SID SID,
    SES.SERIAL# SERIAL#,
    SQL.SQL_TEXT TEXTO_SQL,
    SES.MACHINE MAQUINA,
    SES.USERNAME USUARIO_ORACLE,
    SES.OSUSER USUARIOS_SO
  FROM GV$SESSION       SES,
       GV$SQL           SQL
 WHERE SES.SQL_ADDRESS = SQL.ADDRESS(+)
 AND UPPER(SES.USERNAME) LIKE '%MAXSOLUCOES%'
 ORDER BY SES.LAST_CALL_ET DESC;
```

### 3.15 Validação de Envio de Endpoints Obrigatórios

```sql
SELECT 
    -- MXSATIVI
    (SELECT COUNT(*) FROM MXSATIVI WHERE CODOPERACAO <> 2) AS qtd_mxsativi,
    CASE WHEN (SELECT COUNT(*) FROM MXSATIVI WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsativi_tem_registros,

    -- MXSCIDADE
    (SELECT COUNT(*) FROM MXSCIDADE WHERE CODOPERACAO <> 2) AS qtd_mxscidade,
    CASE WHEN (SELECT COUNT(*) FROM MXSCIDADE WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxscidade_tem_registros,

    -- MXSPRODFILIAL
    (SELECT COUNT(*) FROM MXSPRODFILIAL WHERE CODOPERACAO <> 2) AS qtd_mxsprodfilial,
    CASE WHEN (SELECT COUNT(*) FROM MXSPRODFILIAL WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsprodfilial_tem_registros,

    -- MXSREGIAO
    (SELECT COUNT(*) FROM MXSREGIAO WHERE CODOPERACAO <> 2) AS qtd_mxsregiao,
    CASE WHEN (SELECT COUNT(*) FROM MXSREGIAO WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsregiao_tem_registros,

    -- MXSSECAO
    (SELECT COUNT(*) FROM MXSSECAO WHERE CODOPERACAO <> 2) AS qtd_mxssecao,
    CASE WHEN (SELECT COUNT(*) FROM MXSSECAO WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxssecao_tem_registros,

    -- MXSCLIENT
    (SELECT COUNT(*) FROM MXSCLIENT WHERE CODOPERACAO <> 2) AS qtd_mxsclient,
    CASE WHEN (SELECT COUNT(*) FROM MXSCLIENT WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsclient_tem_registros,

    -- MXSCLIENTECREDDISP
    (SELECT COUNT(*) FROM MXSCLIENTECREDDISP WHERE CODOPERACAO <> 2) AS qtd_mxsclientcreddisp,
    CASE WHEN (SELECT COUNT(*) FROM MXSCLIENTECREDDISP WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsclientcreddisp_tem_registros,

    -- MXSCOB
    (SELECT COUNT(*) FROM MXSCOB WHERE CODOPERACAO <> 2) AS qtd_mxscob,
    CASE WHEN (SELECT COUNT(*) FROM MXSCOB WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxscob_tem_registros,
    
    -- MXSPLPAG
    (SELECT COUNT(*) FROM MXSPLPAG WHERE CODOPERACAO <> 2) AS qtd_mxsplpag,
    CASE WHEN (SELECT COUNT(*) FROM MXSPLPAG WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsplpag_tem_registros,

    -- MXSPRACA
    (SELECT COUNT(*) FROM MXSPRACA WHERE CODOPERACAO <> 2) AS qtd_mxspraca,
    CASE WHEN (SELECT COUNT(*) FROM MXSPRACA WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxspraca_tem_registros,
    
    -- MXSDEPTO
    (SELECT COUNT(*) FROM MXSDEPTO WHERE CODOPERACAO <> 2) AS qtd_mxsdepto,
    CASE WHEN (SELECT COUNT(*) FROM MXSDEPTO WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsdepto_tem_registros,
    
    -- ERP_MXSESTADO
    (SELECT COUNT(*) FROM ERP_MXSESTADO WHERE CODOPERACAO <> 2) AS qtd_erp_mxsestado,
    CASE WHEN (SELECT COUNT(*) FROM ERP_MXSESTADO WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS erp_mxsestado_tem_registros,
    
    -- MXSFILIAL
    (SELECT COUNT(*) FROM MXSFILIAL WHERE CODOPERACAO <> 2) AS qtd_MXSFILIAL,
    CASE WHEN (SELECT COUNT(*) FROM MXSFILIAL WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS erp_MXSFILIAL_tem_registros,
    
    -- MXSPRODUT
    (SELECT COUNT(*) FROM MXSPRODUT WHERE CODOPERACAO <> 2) AS qtd_mxsprodut,
    CASE WHEN (SELECT COUNT(*) FROM MXSPRODUT WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsprodut_tem_registros,
    
    -- MXSTABPR
    (SELECT COUNT(*) FROM MXSTABPR WHERE CODOPERACAO <> 2) AS qtd_MXSTABPR,
    CASE WHEN (SELECT COUNT(*) FROM MXSTABPR WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS MXSTABPR_tem_registros,
    
    -- MXSEST
    (SELECT COUNT(*) FROM MXSEST WHERE CODOPERACAO <> 2) AS qtd_mxsest,
    CASE WHEN (SELECT COUNT(*) FROM MXSEST WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS mxsest_tem_registros,
    
    -- MXSTRIBUT
    (SELECT COUNT(*) FROM MXSTRIBUT WHERE CODOPERACAO <> 2) AS qtd_MXSTRIBUT,
    CASE WHEN (SELECT COUNT(*) FROM MXSTRIBUT WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS MXSTRIBUT_tem_registros,
    
    -- MXSUSUARI
    (SELECT COUNT(*) FROM MXSUSUARI WHERE CODOPERACAO <> 2) AS qtd_MXSUSUARI,
    CASE WHEN (SELECT COUNT(*) FROM MXSUSUARI WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS MXSUSUARI_tem_registros,
    
    -- MXSFORNEC
    (SELECT COUNT(*) FROM MXSFORNEC WHERE CODOPERACAO <> 2) AS qtd_MXSFORNEC,
    CASE WHEN (SELECT COUNT(*) FROM MXSFORNEC WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS MXSFORNEC_tem_registros,
    
    -- ERP_MXSGERENTE
    (SELECT COUNT(*) FROM ERP_MXSGERENTE WHERE CODOPERACAO <> 2) AS qtd_ERP_MXSGERENTE,
    CASE WHEN (SELECT COUNT(*) FROM ERP_MXSGERENTE WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS ERP_MXSGERENTE_tem_registros,
    
    -- MXSHISTORICOPEDC
    (SELECT COUNT(*) FROM MXSHISTORICOPEDC WHERE CODOPERACAO <> 2) AS qtd_MXSHISTORICOPEDC,
    CASE WHEN (SELECT COUNT(*) FROM MXSHISTORICOPEDC WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS MXSHISTORICOPEDC_tem_registros,
    
    -- MXSHISTORICOPEDI
    (SELECT COUNT(*) FROM MXSHISTORICOPEDI WHERE CODOPERACAO <> 2) AS qtd_MXSHISTORICOPEDI,
    CASE WHEN (SELECT COUNT(*) FROM MXSHISTORICOPEDI WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS MXSHISTORICOPEDI_tem_registros,
    
    -- MXSHISTORICOPEDCORTE
    (SELECT COUNT(*) FROM MXSHISTORICOPEDCORTE WHERE CODOPERACAO <> 2) AS qtd_MXSHISTORICOPEDCORTE,
    CASE WHEN (SELECT COUNT(*) FROM MXSHISTORICOPEDCORTE WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS MXSHISTORICOPEDCORTE_tem_registros,
    
    -- ERP_MXSTABDEV
    (SELECT COUNT(*) FROM ERP_MXSTABDEV WHERE CODOPERACAO <> 2) AS qtd_ERP_MXSTABDEV,
    CASE WHEN (SELECT COUNT(*) FROM ERP_MXSTABDEV WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS ERP_MXSTABDEV_tem_registros,
    
    -- ERP_MXSNFENT
    (SELECT COUNT(*) FROM ERP_MXSNFENT WHERE CODOPERACAO <> 2) AS qtd_ERP_MXSNFENT,
    CASE WHEN (SELECT COUNT(*) FROM ERP_MXSNFENT WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS ERP_MXSNFENT_tem_registros,
  
    -- ERP_MXSESTCOM
    (SELECT COUNT(*) FROM ERP_MXSESTCOM WHERE CODOPERACAO <> 2) AS qtd_ERP_MXSESTCOM,
    CASE WHEN (SELECT COUNT(*) FROM ERP_MXSESTCOM WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS ERP_MXSESTCOM_tem_registros,
    
    -- ERP_MXSMOV
    (SELECT COUNT(*) FROM ERP_MXSMOV WHERE CODOPERACAO <> 2) AS qtd_ERP_MXSMOV,
    CASE WHEN (SELECT COUNT(*) FROM ERP_MXSMOV WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS ERP_MXSMOV_tem_registros,
    
    -- ERP_MXSPREST
    (SELECT COUNT(*) FROM ERP_MXSPREST WHERE CODOPERACAO <> 2) AS qtd_ERP_MXSPREST,
    CASE WHEN (SELECT COUNT(*) FROM ERP_MXSPREST WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS ERP_MXSPREST_tem_registros,
    
    -- MXSSUPERV
    (SELECT COUNT(*) FROM MXSSUPERV WHERE CODOPERACAO <> 2) AS qtd_MXSSUPERV,
    CASE WHEN (SELECT COUNT(*) FROM MXSSUPERV WHERE CODOPERACAO <> 2) > 0 THEN 'SIM' ELSE 'NÃO' END AS MXSSUPERV_tem_registros
    
FROM dual;
```

### 3.16 Acompanhamento de Carga

```sql
SELECT COUNT(1), TABELA FROM MAXSOLUCOES.PCMXSINTEGRACAO WHERE STATUS = -1 GROUP BY TABELA ORDER BY COUNT(1) DESC;
```

### 3.17 Usuários que Realizaram Pedidos nos Últimos 15 Dias

```sql
SELECT DISTINCT(CODUSUARIO), MAX(DTINICIOCONEXAO) FROM MXSAPARELHOSCONNLOG WHERE TRUNC(DTINICIOCONEXAO) >= TRUNC(SYSDATE)-15 GROUP BY CODUSUARIO ORDER BY 2 DESC;

-- Versão com detalhes dos usuários
SELECT DISTINCT(IP.CODUSUARIO) COD_USR_MAXIMA, US.NOME NOME_USR, US.LOGIN LOGIN_USR, MAX(IP.NUMPED) ULT_PEDIDO_TRANSMITIDO, MAX(IP.DATA) DT_ULT_PEDIDO_TRANSMITIDO 
FROM MXSINTEGRACAOPEDIDO IP
JOIN MXSUSUARIOS US ON IP.CODUSUARIO = US.CODUSUARIO
WHERE IP.CODUSUARIO IN (SELECT DISTINCT(CODUSUARIO) FROM MXSAPARELHOSCONNLOG WHERE TRUNC(DTINICIOCONEXAO) >= TRUNC(SYSDATE)-15)
AND IP.DATA >= TRUNC(SYSDATE)-15
GROUP BY IP.CODUSUARIO, US.NOME, US.LOGIN
ORDER BY 2 DESC;
```

### 3.18 Pedido Não Aparece – Checklist Nuvem

```sql
select codprod, dtexclusao, revenda, ENVIARFORCAVENDAS, codfornec, codepto, codsec, codcategoria, codsubcategoria 
from mxsprodut where CODPROD IN(XX) and codoperacao !=2;

select codprod, proibidavenda, ENVIARFORCAVENDAS, codfilial 
from mxsprodfilial where codprod in (XX) and codoperacao !=2;

select codfilial, e.* from mxsembalagem e where codprod in (XX) and codoperacao !=2;

select codfornec, revenda from mxsfornec where codfornec in (YY) and codoperacao !=2;

select * from mxsdepto where codepto in (ZZ) and codoperacao !=2;

select * from mxssecao where codsec in (TT) and codoperacao !=2;

select * from mxstabpr where codprod in (XX) and codoperacao !=2;

select * from mxstabprcli where codcli in (cc) and codoperacao !=2;

select * from mxsest where codprod in (XX) and codoperacao !=2;

select a.codfilial, a.codprod, (a.qtestger) - (a.qtbloqueada) - (a.qtpendente) - (a.qtreserv) 
from mxsest a where codprod in (XX);
```

### 3.19 Cancelar Pedido no Sankhya

```sql
UPDATE ERP_MXSPREST SET DTPAG = TRUNC(SYSDATE) WHERE NUMTRANSVENDA = 'NUMTRANSVENDA';
UPDATE MXSTITULOSABERTOS SET DTPAG = TRUNC(SYSDATE) WHERE NUMTRANSVENDA = 'NUMTRANSVENDA'; 
COMMIT;

UPDATE MXSTITULOSABERTOS SET CODOPERACAO=2 WHERE NUMTRANSVENDA = numerotransvenda; 
COMMIT;

SELECT * FROM MXSINTEGRACAOPEDIDO WHERE NUMPEDERP = numeropedido;
SELECT * FROM ERP_MXSPREST where dtpag is null and codcli = codigocliente;
SELECT * FROM ERP_MXSNFSAID WHERE NUMNOTA = numeronota;
SELECT * FROM ERP_MXSPREST WHERE NUMTRANSVENDA = numerotransvenda;
```

### 3.20 Consultas de Metas

```sql
SELECT * FROM ERP_MXSMETARCA WHERE CODUSUR = 273 ORDER BY DATA DESC;

SELECT * FROM MXSDIASUTEIS ORDER BY DATA DESC;

SELECT * FROM ERP_MXSDATAS WHERE DATA >= TRUNC (SYSDATE,'MM');

SELECT * FROM MXSUSUARIOS WHERE LOGIN = 'vermelho.italo';
```

### 3.21 Cálculo de Valor de Pedidos

```sql
-- Soma de vltotal na MXSHISTORICOPEDC
SELECT sum(vltotal) FROM mxshistoricopedc 
WHERE data BETWEEN to_date('01/02/2023','dd/mm/yyyy') AND to_date('23/02/2023','dd/mm/yyyy') 
and codusur = 16 and codoperacao != 2;

-- Soma de (pvenda * qt) na MXSHISTORICOPEDI, considerando apenas pedidos faturados
SELECT sum(pvenda*qt) FROM mxshistoricopedi 
WHERE numped in ( 
    SELECT numped FROM mxshistoricopedc 
    WHERE data BETWEEN to_date('01/02/2023','dd/mm/yyyy') AND to_date('23/02/2023','dd/mm/yyyy') 
    and codusur = 16 and codoperacao != 2 and posicao = 'F' 
) and codoperacao != 2 and posicao != 'C';
```

### 3.22 Carga de MXSHISTORICOPEDC e MXSHISTORICOPEDI

```sql
SELECT * FROM mxshistoricopedc
WHERE CODUSUR = 6 AND CODOPERACAO != 2 
AND TRUNC(data) BETWEEN to_date('01/07/2023', 'dd/mm/yyyy') AND to_date('20/11/2023', 'dd/mm/yyyy');

SELECT * FROM mxshistoricopedi 
WHERE numped IN (
    SELECT NUMPED FROM mxshistoricopedc 
    WHERE CODUSUR = 6 AND CODOPERACAO != 2 
    AND TRUNC(data) BETWEEN to_date('01/07/2023', 'dd/mm/yyyy') AND to_date('20/11/2023', 'dd/mm/yyyy')
) AND CODOPERACAO != 2;
```

### 3.23 Jobs do Oracle

```sql
-- Verificar parâmetro de jobs
select * from v$parameter where name like '%job_queue%';

-- Contar jobs agendadas
select count(1) from all_scheduler_jobs where STATE = 'SCHEDULED';
select count(1) from all_scheduler_jobs where ENABLED = 'TRUE';

-- Script para criar job da Máxima (exemplo)
BEGIN
    SYS.DBMS_SCHEDULER.CREATE_JOB
    (
        job_name        => 'MAXSOLUCOES.INTEGRADORA_PC'
        ,repeat_interval => 'FREQ=SECONDLY;INTERVAL=15'
        ,end_date        => NULL
        ,job_class       => 'DEFAULT_JOB_CLASS'
        ,job_type        => 'STORED_PROCEDURE'
        ,job_action      => 'MAXSOLUCOES.BUSCA_PEDIDOS_PENDENTES'
        ,comments        => NULL
    );
    SYS.DBMS_SCHEDULER.ENABLE(name => 'MAXSOLUCOES.INTEGRADORA_PC');
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

-- Acompanhar subida de pedidos na integradora
select importado, count(1) from pcpedcfv 
where dtinclusao >= trunc(sysdate) - 5 and dadosped is not null
group by importado;
```

### 3.24 Apuração de Carga (Winthor)

```sql
SELECT * FROM PCMXSCONFIGURACOES; 
EDIT PCMXSCONFIGURACOES; 

SET VERIFY OFF
SET SERVEROUTPUT ON
ACCEPT PCODFILIAL PROMPT 'DIGITE O CODIGO DA FILIAL'
DECLARE

 vFilial VARCHAR2(20) := '&PCODFILIAL';
 vTotal VARCHAR (2000);
 
 SQL_CLIENT           VARCHAR2(2000);
 RESULT_CLIENT        NUMBER;
 
 SQL_EMBALAGEM        VARCHAR2 (2000);
 RESULT_EMBALAGEM     NUMBER;
 
 SQL_PRODFILIAL       VARCHAR2(2000);
 RESULT_PRODFILIAL    NUMBER;
 
 SQL_EST              VARCHAR2 (2000);
 RESULT_EST           NUMBER;
 
 SQL_TABTRIB          VARCHAR2(2000);
 RESULT_TABTRIB       NUMBER;
 
 SQL_TABPRCLI         VARCHAR2 (2000);
 RESULT_TABPRCLI      NUMBER;
 
 SQL_PREST            VARCHAR2 (2000);
 RESULT_PREST         NUMBER;

BEGIN

 SQL_CLIENT :=    'SELECT  COUNT(*)
                   FROM  PCCLIENT
                   WHERE   DTEXCLUSAO IS NULL';
 EXECUTE IMMEDIATE SQL_CLIENT INTO RESULT_CLIENT;
 
 SQL_EMBALAGEM := 'SELECT COUNT(*)
                   FROM   PCEMBALAGEM
                   WHERE  NVL (ENVIAFV, ''S'') = ''S''
                     AND NVL (EXCLUIDO, ''N'') = ''N''   
                     AND (DTINATIVO IS NULL OR DTINATIVO > TRUNC (SYSDATE))   
                     AND CODFILIAL IN (' || vFilial || ')';
 EXECUTE IMMEDIATE SQL_EMBALAGEM INTO RESULT_EMBALAGEM;
 
 SQL_PRODFILIAL := 'SELECT   COUNT(*)
                    FROM   PCPRODFILIAL 
                    WHERE   NVL (ENVIARFORCAVENDAS, ''S'') = ''S''
                      AND CODFILIAL IN (' || vFilial || ')';
 EXECUTE IMMEDIATE SQL_PRODFILIAL INTO RESULT_PRODFILIAL;
 
 SQL_EST :=       'SELECT  COUNT(*)
                   FROM   PCEST, PCPRODUT
                   WHERE  PCEST.CODPROD = PCPRODUT.CODPROD
                     AND PCEST.CODFILIAL != ''99''
                     AND NVL (PCPRODUT.OBS, ''XX'') NOT IN (''PV'')
                     AND NVL (PCPRODUT.REVENDA, ''S'') = ''S''
                     AND PCPRODUT.DTEXCLUSAO IS NULL
                     AND NVL (PCPRODUT.ENVIARFORCAVENDAS, ''S'') = ''S''
                     AND PCEST.CODFILIAL IN (' || vFilial || ')';
 EXECUTE IMMEDIATE SQL_EST INTO RESULT_EST;
 
 SQL_TABTRIB :=   'SELECT  COUNT(*)
                   FROM   PCTABTRIB
                   WHERE   CODFILIALNF IN (' || vFilial || ')';
 EXECUTE IMMEDIATE SQL_TABTRIB INTO RESULT_TABTRIB;
 
 SQL_TABPRCLI :=  'SELECT  COUNT(*)
                   FROM   PCTABPRCLI
                   WHERE CODFILIALNF IN (' || vFilial || ')';
 EXECUTE IMMEDIATE SQL_TABPRCLI INTO RESULT_TABPRCLI;
 
 SQL_PREST :=     'SELECT  COUNT(*)
                   FROM   PCPREST
                   WHERE   (DTPAG IS NULL)
                   AND CODFILIAL IN (' || vFilial || ')';
 EXECUTE IMMEDIATE SQL_PREST INTO RESULT_PREST;
 
 vTotal := RESULT_CLIENT + RESULT_EMBALAGEM + RESULT_PRODFILIAL + RESULT_TABTRIB + RESULT_TABPRCLI + RESULT_EST + RESULT_PREST; 
     
 DBMS_OUTPUT.PUT_LINE ('PCCLIENT:' || ' ' || RESULT_CLIENT || ' ' || 'REGISTROS');
 DBMS_OUTPUT.PUT_LINE ('PCEMBALAGEM:' || ' ' || RESULT_EMBALAGEM || ' ' || 'REGISTROS');
 DBMS_OUTPUT.PUT_LINE ('PCPRODFILIAL:' || ' ' || RESULT_PRODFILIAL || ' ' || 'REGISTROS');
 DBMS_OUTPUT.PUT_LINE ('PCEST:' || ' ' || RESULT_EST || ' ' || 'REGISTROS');
 DBMS_OUTPUT.PUT_LINE ('PCTABTRIB:' || ' ' || RESULT_TABTRIB || ' ' || 'REGISTROS');
 DBMS_OUTPUT.PUT_LINE ('PCTABPRCLI:' || ' ' || RESULT_TABPRCLI || ' ' || 'REGISTROS');
 DBMS_OUTPUT.PUT_LINE ('PCPREST:' || ' ' || RESULT_PREST || ' ' || 'REGISTROS');
 DBMS_OUTPUT.PUT_LINE ('TOTAL GERAL:' || ' ' || vTotal || ' ' || 'REGISTROS');
END;
/
```

### 3.25 Saber se Cliente foi Excluído da Carteira do RCA

```sql
SELECT CODUSUR1, CODUSUR2, CODUSUR3, CODCLI, CLIENTE FROM MXSCLIENT WHERE CODCLI IN (6380,78,8823,2209,8440,146);

SELECT * FROM MXSUSUARIOS WHERE CODUSUR = 11;

select * from erp_mxsusurcli WHERE CODCLI IN (6380,78,8823,2209,8440,146);
```

### 3.26 Usuários Ativos e Inativos

```sql
SELECT codusur, nome, login, status FROM MXSUSUARIOS order by STATUS asc;

-- Detalhes com última conexão
SELECT DISTINCT(APL.CODUSUARIO) AS CODUSUARIO_MAXIMA, USR.LOGIN, USR.NOME, USR.STATUS, USR.CODUSUR AS CODUSUARIO_ERP, 
       MAX(APL.APPVERSION) VERSAO_APP, MAX(DTINICIOCONEXAO) DTULTCONEXAO 
FROM MXSAPARELHOSCONNLOG APL 
JOIN MXSUSUARIOS USR ON APL.CODUSUARIO = USR.CODUSUARIO
GROUP BY APL.CODUSUARIO, USR.LOGIN, USR.NOME, USR.CODUSUR, USR.STATUS
ORDER BY NOME;
```

### 3.27 Relatórios de Vendas por RCA

```sql
SELECT 
CODUSUR, CODCLI, NUMPED, VLTOTAL, VLTABELA, VLATEND, CODFILIAL,
CODFILIALNF, POSICAO AS POSICAO_ERP, CODPLPAG, CODCOB, DTFAT AS DATA_FATURAMENTO,
DTABERTURAPEDPALM AS DATA_ABERTURA_PALM , OBS1 , OBS2, OBSENTREGA1, OBSENTREGA2, OBSENTREGA3, 
NUMTRANSVENDA, CODPRACA, CODSUPERVISOR,
DTFECHAMENTOPEDPALM AS DATA_FECHAMENTO_PALM, DTENTREGA AS DATA_ENTREGA, NUMITENS, NUMREGIAO
FROM MXSHISTORICOPEDC 
WHERE DATA BETWEEN '01/11/2022' AND '30/11/2022' AND codusur = 150;
```

### 3.28 Menu Objetivo – Totais

```sql
SELECT COUNT (*), SUM (VLATEND) 
FROM MXSHISTORICOPEDC 
WHERE DATA >= TRUNC (SYSDATE, 'MM') AND CODUSUR = 302 AND POSICAO != 'C' AND CODOPERACAO != 2;

SELECT COUNT (*), SUM (QT * PVENDA) 
FROM MXSHISTORICOPEDI 
WHERE DATA >= TRUNC (SYSDATE, 'MM') AND POSICAO != 'C' AND CODOPERACAO != 2;
```

### 3.29 Parâmetros de Check-in/Check-out

```sql
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%OBRIGAR_ATENDIMENTO_PARA_CHECKOUT%';
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%PERMITIR_PEDIDO_SEM_CHECKIN%';
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%UTILIZA_CHECKIN_CHECKOUT %';
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%QTD_MAX_PED_FORA_ROTA%';
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%VALIDAR_CHECKIN_SEQ_VISITA_AVULSA %';
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%OBRIGAR_ATENDIMENTO_PARA_CHECKOUT %';
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%LIMITE_RAIO_CHECK_IN_OUT %';
SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%GPS_IS_REQUIRED_CONFEC_PEDIDO %';
```

**Observações sobre check-in/check-out:**
- `OBRIGAR_ATENDIMENTO_PARA_CHECKOUT` = 'S' obriga um atendimento (pedido ou justificativa) antes do checkout.
- `PERMITIR_PEDIDO_SEM_CHECKIN` = 'N' não permite pedidos sem check-in.
- `UTILIZA_CHECKIN_CHECKOUT` = 'S' habilita a funcionalidade.
- `QTD_MAX_PED_FORA_ROTA` = 0 (se maior que 0, permite essa quantidade de pedidos fora de rota sem check-in).
- `VALIDAR_CHECKIN_SEQ_VISITA_AVULSA` = 'S' não obriga check-in em visita avulsa.
- `LIMITE_RAIO_CHECK_IN_OUT` define o raio (em metros) para permitir check-in/out.
- `GPS_IS_REQUIRED_CONFEC_PEDIDO` = 'S' obriga GPS ligado para iniciar pedido.

### 3.30 Carga Manual de Dados por Tabela

```sql
DECLARE
BEGIN
    UPDATE MXSCLIENT
    SET ATUALIZID = TO_NUMBER(TO_CHAR(sysdate, 'RRRRMMDDHH24MISS')),
        DTATUALIZ = sysdate
    WHERE CODOPERACAO != 2;
    COMMIT;
END;
/
```

### 3.31 Cálculo do Campo ValorST

Fórmula utilizada:

```
Preço Inicial: 46,5
Acréscimo do plano: 2% (Plano de pagamento A vista)
Preço com acréscimo do plano: 46,5 + 2% = 45,57

|Variáveis para calcular o ST|
PREÇO VENDA = 45,57
IVA = 50%
ALIQ01 = 20,5% 
ALIQ02 = 20,5%
 
BASE ST = PRECO VENDA + IVA => 45,57 + 50% = 68,355

|Calculando ST|
ST = (BASE ST * (ALIQ01/100)) - (PREÇO VENDA * (ALIQ02/100))
ST = (68,355 * 0,205) - (45,57 * 0,205)
ST = 14,012775 - 9,34185
ST = 4,670925
```

Esses valores são obtidos do endpoint MXSTRIBUT (tributações).

---

## 4. Configurações Diversas

### 4.1 Preço Mínimo de Pedido por Plano de Pagamento

- Para utilizar o plano de pagamento com preço mínimo, é necessário que o campo `MXPLPAG.VLMINPEDIDO` esteja preenchido.
- Habilitar o parâmetro: `BLOQUEAR_PEDIDO_ABAIXO_MIN_PLANO_PAGAMENTO`.

### 4.2 Conta Corrente de RCA

Para utilizar a conta corrente por RCA, habilitar as seguintes parametrizações:

1. **CON_USACREDRCA** – Usar crédito de RCA (S/N).
2. **CON_TIPOMOVCCRCA** – Define quando ocorre a movimentação:
   - `VF` – movimentação no faturamento.
   - `VV` – movimentação na transmissão do pedido.
3. **CON_BONIFICALTDEBCREDRCA** – Debita valor de produtos bonificados da conta corrente do RCA (S/N).

### 4.3 Cadastro de Metas no Winthor

A ordem correta para cadastro de metas:

1. **Cadastrar dias úteis** na rotina 309 (grava na tabela PCDATAS). Existe também a rotina 589, que grava na PCDIASUTEIS.
2. **Cadastrar a meta** em uma das rotinas:
   - **353** – Meta diária por RCA (valor) – grava na PCMETARCA, refletida na `erp_mxsmetarca`.
   - **3305** – Meta mensal – grava na PCMETA, refletida na `ERP_MXSMETA`.
   - **399** – Metas por Depto/Sec/Prod/Fornec – grava na PCMETA, refletida na `ERP_MXSMETA`.
   - **368** – Meta de cliente por RCA – grava na PCAUXCLI, refletida na `MXSCLIENTMETAS`.
3. O envio de metas ao PDV é feito via job `JOB_RCA_METAS`, executada a cada 24h.

**Parâmetros em MXSCONFIGDATA (valores recomendados):**
- `DESCONSIDERAR_METAS_ZERADAS = N`
- `META_DEP` (meta por departamento, tipometa D)
- `META_FOR` (meta por fornecedor, tipometa F)
- `META_FRP` (meta por fornecedor principal, tipometa B)
- `META_GERAL_CLIPOS`
- `META_GERAL_MIX`
- `META_GERAL_QTPROD`
- `META_GERAL_VLVENDA`
- `META_SEC` (meta por seção, tipometa S)
- `META_PROD` (meta por produto, tipometa P)

### 4.4 Habilitar MaxGestão

No banco local (Winthor), executar os updates abaixo:

```sql
UPDATE PCMXSCONFIGURACOES SET VALOR = 'S' WHERE NOME = 'UTILIZA_GESTAO_LOGISTICA'; 
UPDATE PCMXSCONFIGURACOES SET VALOR = 'S' WHERE NOME = 'ENVIA_PEDIDOS_CALL_CENTER'; 
UPDATE PCMXSCONFIGURACOES SET VALOR = 'S' WHERE NOME = 'ENVIA_PEDIDOS_TELEMARKETING'; 
UPDATE PCMXSCONFIGURACOES SET VALOR = 'S' WHERE NOME = 'ENVIA_PEDIDOS_BALCAO';
```

### 4.5 Adicionar uma Filial

Parâmetros necessários para alterar e adicionar novas filiais:

- `CODFILIAL_IMPORTACAO`
- `CODFILIAL_PREST`

---
