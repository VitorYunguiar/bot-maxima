# Documentos Técnicos - MaxGestão / MaximaTech

**Total de documentos:** 102

**Período:** Diversos tickets e documentações técnicas.

---

## DOC-MXGESNDV-17962.docx

**Ao exportar resultados do menu Orçamento x Venda não é retornado o código e nome do vendedor que realizou pedido ou orçamento.\
TICKET:** MXGESNDV-17962

------------------------------------------------------------------------

**CAUSA:**\
o método responsável pela exportação em CSV que é utilizada na API estava removendo a coluna CODUSUARIO, com isso, a propriedade em tela estava sendo removida;

------------------------------------------------------------------------

**ANÁLISE:**\
Foi realizada a validação do método e o motivo da coluna estar em exclusão e não foi encontrado um outro ponto que seja indispensável o uso da coluna.\
Com isso, foi feita a remoção da propriedade CODUSUARIO na lista de exclusão, normalizando a exportação com a coluna citada.

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
A coluna RCA, propriedade CODUSUARIO será exportada normalmente.

---

## DOC-MXGESNDV-17973.docx

**Relatório Painel de Auditoria - Gerando em Branco.\
TICKET:** MXGESNDV-17973

------------------------------------------------------------------------

**CAUSA:**\
Estava ocorrendo falha no método que faz o cálculo de impressão, devido a alguns rca\'s estarem sem a filial vinculada;

------------------------------------------------------------------------

**ANÁLISE:**\
Foi inserida tratativa no método que faz o vínculo para buscar a filial do filtro, assim, não ocorrerá a falha e inserirá o RCA na filial;

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
N/A

---

## Doc-Back-PWAWeb-MXGESNDV-12359.docx

# 1. Introdução

Este documento descreve as alterações que deverão ser realizadas na tabela **MXUSUARIOS** e a implementação da nova propriedade AceitouPWA no modelo de retorno da aplicação. Essas alterações têm o objetivo de capturar o consentimento do usuário sobre o uso da plataforma **MaxGestão Web PWA**, oferecendo três opções de aceitação, com otimizações de performance e boas práticas de desenvolvimento.

**2. Alterações na Tabela MXUSUARIOS**

**2.1 Estrutura Atualizada da Tabela**

A tabela **MXUSUARIOS** será alterada para incluir a coluna **ACEITOUPWA**, que armazenará o status de aceite do PWA para cada usuário. A nova coluna terá as seguintes especificações:

- **Coluna**: **ACEITOUPWA**
- **Tipo de Dados**: NUMBER(1)
- **Valores**:
  - **1:** Representa a opção **"Aceitou usar o PWA"**. O usuário concordou em usar o MaxGestão Web PWA e terá acesso às funcionalidades que foram migradas para essa plataforma.
  - **2:** Representa a opção **"Não aceitou usar o PWA"**. O usuário optou por não utilizar o MaxGestão Web PWA, então ele verá apenas as funcionalidades disponíveis na versão tradicional do sistema.
  - **3:** Representa a opção **"Default quando usuário ainda não fez a escolha"**.
- **Diagrama DER:**

![Diagrama Descrição gerada automaticamente](media/image2.png){width="6.268055555555556in" height="2.1534722222222222in"}

**2.2 Script SQL para Atualização**

ALTER TABLE MXUSUARIOS
ADD ACEITOUPWA NUMBER(1) DEFAULT 2;

UPDATE MXUSUARIOS
SET ACEITOUPWA = 2
WHERE ACEITOUPWA IS NULL;

**3. Propriedade AceitouPWA e Atualizações de Parâmetros no Endpoint**

**3.1 Definição da Propriedade**

A propriedade **AceitouPWA** será introduzida no modelo de retorno da aplicação, responsável por indicar o status de aceite do usuário em relação ao uso do **MaxGestão Web PWA**. Esta propriedade será populada através de uma query SQL com base no valor presente na coluna **ACEITOUPWA** da tabela **MXUSUARIOS**.

A implementação usará um **enumerador** no código, garantindo uma interpretação eficiente dos valores numéricos armazenados no banco de dados, promovendo legibilidade e facilidade de manutenção.

**Script SQL para Obter se Aceitou PWA**

**3.2 Atualização de Parâmetros no Endpoint:**

- **Análise do Retorno do Endpoint**

Após a análise do retorno do endpoint, foi identificada a necessidade de acrescentar os seguintes parâmetros ao payload de resposta:

**3.3 Estrutura de Retorno do Endpoint**

Exemplo de retorno da propriedade **AceitouPWA** via API:

- **Endpoint**: api/v1/usuario/validarToken?token=token

- **Ajuste de Parâmetros Existentes**

Além dos novos parâmetros, verificou-se que os campos **loginUser** e **nome** já existem no retorno, porém estão sendo retornados como null. Será necessário garantir que essas informações sejam corretamente preenchidas e apresentadas, principalmente para uso no PWA.

A Propriedade **rotina** retornada na estrutura do **Login** deverá retornar o valor da rotina, se o usuário possuir.

Na estrutura rotinaVersao, manter os dados referentes a versão apk.

**Diagrama da Classe:**

![](media/image1.png){width="6.270833333333333in" height="6.222915573053369in"}

**4. Fluxo de Aceite do PWA**

**4.1 Comportamento do Sistema**

- Usuário não escolheu: Se o valor de **ACEITOUPWA** for 3, o sistema solicitará que o usuário faça sua escolha, atualizando o valor de **ACEITOUPWA** de forma definitiva.

**4.2 Validação de Aceite**

Durante a validação do token de usuário, a aplicação verificará o valor de **ACEITOUPWA** na tabela **MXUSUARIOS** e retornará o status correto. Dependendo do valor, a interface exibirá as funcionalidades migradas para o **PWA** ou manterá o acesso à versão tradicional do sistema.

**5. Considerações Técnicas**

**5.1 Enumerador ao Invés de String**

A propriedade **AceitouPWA** será representada como um enumerador, permitindo que o valor numérico armazenado no banco de dados seja interpretado corretamente no código. Para melhorar a consistência, a performance, e facilita a manutenção do código.

**5.2 Uso de NUMBER(1) em ACEITOUPWA**

O uso do tipo **NUMBER(1)** ao invés de **VARCHAR(1)** oferece melhor performance e armazenamento, além de simplificar comparações e operações lógicas no banco de dados.

**5.3 Valor Padrão**

O valor 3 será o padrão na coluna **ACEITOUPWA**, indicando que o usuário ainda não escolheu. O sistema solicitará essa escolha ao usuário, gravando 1 (Aceitou) ou 2(Não Aceitou) de forma definitiva.

---

## Doc-Envio de Lead IG.docx

Botão para envio do lead (pré-cadastro) para o ERP a partir do Mapa de oportunidades > Inteligência Geográfica

**Fluxo:**

- Parametrizar o representante e praça padrão para envio dos dados;
- Parametrização disponível em: Configurações > Parâmetros para envio de Lead a partir da Inteligência Geográfica (IG);

![](media/image1.png){width="6.270833333333333in" height="2.940229658792651in"}

- Caso não esteja parametrizado será exibido o seguinte alerta para o cliente realizar a parametrização

![](media/image2.png){width="6.267716535433071in" height="3.5416666666666665in"}

- Parâmetro do representante padrão: MXCONFIGDATA NOME = 'CODUSUR_PADRAO_CADASTRO_LEAD_IG'
- Parâmetro da praça padrão: MXCONFIGDATA NOME = PRACA_PADRAO_CADASTRO_LEAD_IG
- Caso não possua nenhum das parametrizações é apresentado um alerta para o usuário indicando que ele deve realizar a parametrização para continuar;
- Desta forma, ao clicar no botão "Enviar cadastro" os dados são preenchidos baseados nos dados apresentados e enviados para a integração MXSINTEGRACAOCLIENTE, com status = 0.
- Com isso, o extrator ou integrador do cliente puxará os dados e realizará a integração do cliente.

Os dados no json são preenchidos da seguinte forma:

- StatusCodPrincipalBloqueado = false
- CodigoRede = "0"
- Nome: Razão social, com no máximo 60 caracteres, caso possua mais caracteres são cortados (para evitar erros na integração)
- Fantasia: Nome fantasia, com no máximo 40 caracteres, caso possua mais caracteres são cortados (para evitar erros na integração)
- CNPJ: CNPJ do cliente
- CNAE,
- Praca
  - Codigo: Código padrão definido na tela em configurações
  - CodigoCidade: Código da cidade IBGE que vem do IG, caso não seja encontrada é realizada a busca da mesma baseado no município escolhido
- Observacao: "CLIENTE CADASTRADO A PARTIR DO MAXGESTAO"
- TipoOperacao: "I"
- CodigoRCA: Código do representante padrão definido na tela em configurações
- InscricaoEstadual: "ISENTO"
- DicionarioDeParametros: Parâmetros do cliente

Com isso o botão pode ter algumas descrições que indicam o status do lead (cliente):

- Enviar cadastro: Cliente Não está cadastrado (Não está na MXSINTEGRACAOCLIENTE e MXSCLIENT). Único que fica habilitado;
- Enviado ERP: Está apenas na integração (MXSINTEGRACAOCLIENTE ) (Exemplo, clientes OERP podem demorar a puxar o cliente ou retornar o dado na mxsclient);
- Em análise: Dado está na MXSCLIENT, mas sem data de alteração (DTULTALTER), funcionário de alteração (CODFUNCULTALTER) e codusur (codusur1) igual ao codusur padrão;
- Concluído: Processo completo, quando cliente possui: data de alteração (DTULTALTER), funcionário de alteração (CODFUNCULTALTER) e codusur (codusur1) diferente codusur padrão.

**Detalhes técnicos:**

- Back-end: Controller Lead -> responsável por salvar e obter os status dos leads
  - Endpoint: "enviar" salva o lead
  - Endpoint: "verificar-lead-enviado" verifica o status do lead para a atualização do status no botão de enviar
- Tabelas:
  - MXSINTEGRACAOCLIENTE: onde os dados são salvos e são consumidos pelo extrator/integrador
  - MXSCLIENT: tabela de clientes onde ocorre o retorno após o lead virar o cliente.

---

## Doc-MXGESNDV-17888.docx

**Devoluções zeradas** TICKET: MXGESNDV-17888

> **CAUSA:**
>
> As devoluções consideram se o CODFISCAL da tabela ERP_MXSNFENT está preenchido com algum desses códigos a seguir: 131, 132, 231, 232, 199, 299.

# ANÁLISE:

Durante a análise, foi identificado que a lógica responsável por validar as devoluções considera uma série de regras dentre elas o CODFISCAL da tabela ERP_MXSNFENT.

# REGRA DE NEGÓCIO:

# Esse documento foi feito com o objetivo de mapear a apuração das devoluções para ambos os tipos de clientes da Máxima OERPS e Winthor. Ele contém a lógica atual que o maxGestão utiliza para apurar as devoluções no Painel Geral Indicadores de venda por Emissão e Faturamento:

/*\######################################################################################################################################################################################################################*/

-->>OERPs

-->>Consulta para verificar as devoluções por Data Emissão do pedido

-->>Ela considera todos os supervisores, filiais, RCAs que o usuário possuir acesso nas permissões do maxGestão

-->>Importante se atentar às validações da consulta no WHERE e ao CASE no SELECT

-->>É só jogar a consulta na IDE (Dbeaver ou SQL Developer) apertar no teclado CTRL + A (para selecionar toda a consulta) e consultar

WITH AA AS( SELECT A.DATA FROM MXDIASUTEIS A WHERE DATA BETWEEN TO_DATE(:dtinicio, 'dd/mm/yyyy') AND TO_DATE(:dtfim, 'dd/mm/yyyy') GROUP BY A.DATA
)
, B AS( SELECT DIAUTIL, TO_CHAR(A.DATA,'MM/YYYY') AS DATA FROM MXDIASUTEIS A JOIN AA ON A.DATA = AA.DATA ),
A AS ( SELECT DEVOL.DATA AS DATA, DECODE('S','N',0,SUM(DEVOL.VLDEVOLUCAO - 0 - 0 - DEVOL.VLREPASSE)) VLTOTAL FROM( SELECT TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY') AS DATA, NVL( SUM( CASE WHEN ERP_MXSNFSAID.CONDVENDA IN (6,11) THEN 0 ELSE ( NVL (ERP_MXSMOV.QT, 0) * ( NVL (ERP_MXSMOV.PUNIT, 0) + NVL (ERP_MXSMOV.VLFRETE, 0) + NVL (ERP_MXSMOV.VLOUTRASDESP, 0) + NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) + NVL (ERP_MXSMOV.VLOUTROS, 0) - NVL (ERP_MXSMOV.VLREPASSE, 0))) END ), 0) AS VLDEVOLUCAO, NVL(SUM(NVL (ERP_MXSMOV.QT, 0) * NVL (ERP_MXSMOV.ST, 0)),0) VLST, NVL(SUM(NVL(ERP_MXSMOV.VLIPI, 0) * NVL (ERP_MXSMOV.QT, 0)),0) VLIPI, NVL(ROUND (SUM(ERP_MXSMOV.QT * ERP_MXSMOV.VLREPASSE), 2), 0) VLREPASSE FROM ERP_MXSNFENT, ERP_MXSESTCOM, ERP_MXSTABDEV, MXSCLIENT, MXSEMPR, MXSUSUARI, MXSSUPERV, MXSFORNEC F, ERP_MXSNFSAID, ERP_MXSMOV, MXSPRODUT, ERP_MXSDEVCONSUM, MXSHISTORICOPEDC VENDAS WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT(+) AND ERP_MXSNFENT.CODDEVOL = ERP_MXSTABDEV.CODDEVOL(+) AND MXSCLIENT.CODCLI = ERP_MXSNFENT.CODFORNEC AND ERP_MXSNFENT.NUMTRANSENT = ERP_MXSDEVCONSUM.NUMTRANSENT(+) AND ERP_MXSNFENT.CODMOTORISTADEVOL = MXSEMPR.MATRICULA(+) AND ERP_MXSNFENT.CODUSURDEVOL = MXSUSUARI.CODUSUR AND MXSUSUARI.CODSUPERVISOR = MXSSUPERV.CODSUPERVISOR(+) AND TO_NUMBER(ERP_MXSESTCOM.NUMTRANSENT) = ERP_MXSMOV.NUMTRANSENT AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD(+) AND NVL (TO_CHAR(ERP_MXSMOV.DTCANCEL,'DD-MM-YYYY'), '00-00-0000') = '00-00-0000' AND NVL (ERP_MXSMOV.CODOPER, 'ED') = 'ED' AND TRUNC(ERP_MXSNFENT.DTENT) BETWEEN TO_DATE(:dtinicio, 'dd/mm/yyyy') AND TO_DATE(:dtfim, 'dd/mm/yyyy') AND ERP_MXSNFENT.TIPODESCARGA IN ('6','7','T') AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA' AND ERP_MXSNFENT.CODFISCAL IN ('131','132','231','232','199','299') AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+) AND NVL(ERP_MXSNFSAID.CONDVENDA,0) NOT IN (4, 8, 10, 13, 20, 98, 99) AND MXSUSUARI.CODSUPERVISOR IN (SELECT KEYDADOS AS CODSUPERVISOR FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = :codusuario ) AND ERP_MXSESTCOM.NUMTRANSVENDA = VENDAS.NUMTRANSVENDA(+) AND ERP_MXSNFENT.CODFILIAL IN (SELECT KEYDADOS FROM MXACESSODADOS Z WHERE Z.CODDADOS = '6' AND Z.CODUSUARIO = :codusuario ) AND F.CODFORNEC(+) = ERP_MXSNFENT.CODFORNEC
GROUP BY TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY')
) DEVOL
GROUP BY DEVOL.DATA
)
SELECT 'DEVOL' SERIE, NVL(B.DATA, A.DATA) DATA, B.DIAUTIL DIAUTIL, NVL(A.VLTOTAL,0) VLTOTAL FROM A LEFT JOIN B ON A.DATA = B.DATA GROUP BY NVL(B.DATA, A.DATA), B.DIAUTIL, VLTOTAL, 'DEVOL'

/*\######################################################################################################################################################################################################################*/

-->>OERPs

-->>Consulta para verificar as devoluções por Data de faturamento do pedido

-->>Ela considera todos os supervisores, filiais, RCAs que o usuário possuir acesso nas permissões do maxGestão

-->>Importante se atentar às validações da consulta no WHERE e ao CASE no SELECT

-->>É só jogar a consulta na IDE (Dbeaver ou SQL Developer) apertar no teclado CTRL + A (para selecionar toda a consulta) e consultar

WITH DEVOL_RESUMO_FATURAMENTO AS ( SELECT ERP_MXSNFENT.DTENT AS DTENT, ERP_MXSNFENT.CODFILIAL, ROUND ( ( NVL (ERP_MXSMOV.QT, 0) * DECODE ( ERP_MXSNFSAID.CONDVENDA, 5, 0, 6, 0, 11, 0, 12, 0, DECODE (ERP_MXSMOV.CODOPER, 'SB', 0, NVL (ERP_MXSMOV.ST, 0)))), 2) VLST, DECODE (NVL (ERP_MXSNFSAID.CONDVENDA, 0), 5, 0, 6, 0, 11, 0, (NVL (ERP_MXSMOV.VLIPI, 0) * NVL (ERP_MXSMOV.QT, 0))) VLIPI, CASE WHEN SUBSTR (ERP_MXSMOV.ROTINACAD, 7, 5) = '1361' THEN NVL (ERP_MXSMOV.QT, 0) * NVL (ERP_MXSMOV.PUNITCONT, 0) ELSE ( NVL (ERP_MXSMOV.QT, 0) * ( CASE WHEN ERP_MXSNFSAID.CONDVENDA = 6 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 11 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 1 THEN CASE WHEN NVL (ERP_MXSMOVCOMPLE.BONIFIC, 'N') = 'N' THEN ( CASE WHEN ERP_MXSMOV.PUNIT = 0 THEN ERP_MXSMOV.PUNITCONT WHEN ERP_MXSMOV.PUNIT IS NULL THEN ERP_MXSMOV.PUNITCONT ELSE ERP_MXSMOV.PUNIT END + NVL (ERP_MXSMOV.VLFRETE, 0) + NVL (ERP_MXSMOV.VLOUTRASDESP, 0) + NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) + NVL (ERP_MXSMOV.VLOUTROS, 0)) ELSE 0 END ELSE CASE WHEN ERP_MXSMOV.PUNIT = 0 THEN ERP_MXSMOV.PUNITCONT WHEN ERP_MXSMOV.PUNIT IS NULL THEN ERP_MXSMOV.PUNITCONT ELSE ERP_MXSMOV.PUNIT END + NVL (ERP_MXSMOV.VLFRETE, 0) + NVL (ERP_MXSMOV.VLOUTRASDESP, 0) + NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) + NVL (ERP_MXSMOV.VLOUTROS, 0) END - CASE WHEN ERP_MXSNFSAID.CONDVENDA = 6 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 11 THEN 0 ELSE NVL (ERP_MXSMOV.VLREPASSE, 0) END - CASE WHEN ERP_MXSNFSAID.CONDVENDA = 6 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 11 THEN 0 ELSE NVL (ERP_MXSMOV.ST, 0) END)) + ROUND ( ( NVL (ERP_MXSMOV.QT, 0) * CASE WHEN ERP_MXSNFSAID.CONDVENDA = 6 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 11 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 12 THEN 0 ELSE CASE WHEN ERP_MXSMOV.CODOPER = 'SB' THEN 0 ELSE NVL (ERP_MXSMOV.ST, 0) END END), 2) END AS VLDEVOLUCAO, CASE WHEN NVL (ERP_MXSNFSAID.CONDVENDA, 0) = 6 THEN 0 WHEN NVL (ERP_MXSNFSAID.CONDVENDA, 0) = 11 THEN 0 ELSE NVL (ROUND (ERP_MXSMOV.QT * ERP_MXSMOV.VLREPASSE, 2), 0) END AS VLREPASSE, ERP_MXSNFENT.CODFORNEC AS CODCLI, COALESCE (MXSHISTORICOPEDC.CODSUPERVISOR, MXSUSUARI.CODSUPERVISOR) AS CODSUPERVISOR, NVL (ERP_MXSNFSAID.CONDVENDA, 0) AS CONDVENDA, ERP_MXSNFENT.CODUSURDEVOL AS CODUSUR, 0 AS VLBONIFIC, MXSFORNEC.CODFORNEC FROM ERP_MXSNFENT, ERP_MXSESTCOM, ERP_MXSNFSAID, ERP_MXSMOV, MXSPRODUT, MXSCLIENT, MXSFORNEC, MXSPRACA, ERP_MXSTABDEV, MXSUSUARI, MXSHISTORICOPEDC, MXSFORNEC FORNECPRINC, ERP_MXSMOVCOMPLE WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT AND MXSCLIENT.CODPRACA = MXSPRACA.CODPRACA(+) AND ERP_MXSESTCOM.NUMTRANSENT = ERP_MXSMOV.NUMTRANSENT AND MXSFORNEC.CODFORNEC(+) = MXSPRODUT.CODFORNEC AND ERP_MXSNFSAID.NUMPED = MXSHISTORICOPEDC.NUMPED(+) AND MXSFORNEC.CODFORNECPRINC = FORNECPRINC.CODFORNEC(+) AND ERP_MXSNFENT.CODDEVOL = ERP_MXSTABDEV.CODDEVOL(+) AND ERP_MXSNFENT.CODUSURDEVOL = MXSUSUARI.CODUSUR(+) AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+) AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD AND ERP_MXSNFENT.CODFORNEC = MXSCLIENT.CODCLI AND NVL (ERP_MXSESTCOM.NUMTRANSVENDA, 0) <> 0 AND NVL (ERP_MXSNFENT.TIPODESCARGA, 'X') IN ('6', '7', 'T', 'X') AND NVL (ERP_MXSNFENT.CODFISCAL, 0) IN (131, 132, 231, 232, 199, 299) AND NVL (TO_CHAR (ERP_MXSMOV.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000' AND NVL (ERP_MXSMOV.CODOPER, 'ED') = 'ED' AND ( NVL (ERP_MXSNFENT.ESPECIE, 'X') <> 'OE' OR ( NVL (ERP_MXSNFENT.ESPECIE, 'X') = 'OE' AND NVL (ERP_MXSNFSAID.VENDAASSISTIDA, 'N') = 'S' AND ERP_MXSNFSAID.CONDVENDA = 7)) AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA' AND ERP_MXSMOV.NUMTRANSITEM = ERP_MXSMOVCOMPLE.NUMTRANSITEM(+) AND NVL(ERP_MXSMOV.CODOPERACAO,0) != 2 AND NVL(ERP_MXSNFENT.CODOPERACAO,0) != 2 AND NVL(MXSHISTORICOPEDC.CODOPERACAO,0) != 2 AND NVL(ERP_MXSNFSAID.CODOPERACAO,0) != 2 AND NVL(MXSPRODUT.CODOPERACAO,0) != 2 AND NVL (ERP_MXSNFENT.TIPOMOVGARANTIA, -1) = -1 AND TRUNC(ERP_MXSNFENT.DTENT) BETWEEN TRUNC(TO_DATE(:dtinicio, 'dd/mm/yyyy')) AND TRUNC(TO_DATE(:dtfim, 'dd/mm/yyyy')) AND ERP_MXSNFSAID.CONDVENDA NOT IN (4,8,10,13,20,98,99))

SELECT SUM(DEVOL.VLDEVOLUCAO - 0 - 0 - DEVOL.VLREPASSE) VLDEVOLUCAO FROM DEVOL_RESUMO_FATURAMENTO DEVOL , MXSSUPERV, MXSUSUARI, MXSCLIENT WHERE MXSSUPERV.CODSUPERVISOR = DEVOL.CODSUPERVISOR AND TRUNC(DEVOL.DTENT) BETWEEN TRUNC(TO_DATE(:dtinicio, 'dd/mm/yyyy')) AND TRUNC(TO_DATE(:dtfim, 'dd/mm/yyyy')) AND MXSUSUARI.CODUSUR = DEVOL.CODUSUR AND MXSCLIENT.CODCLI = DEVOL.CODCLI

/*\######################################################################################################################################################################################################################*/

-->>WINTHOR

-->>Consulta para verificar as devoluções por Data de emissão do pedido -->>Ela considera todos os supervisores, filiais, RCAs que o usuário possuir acesso nas permissões do maxGestão

-->>Importante se atentar às validações da consulta no WHERE e ao CASE no SELECT

-->>É só jogar a consulta na IDE (Dbeaver ou SQL Developer) apertar no teclado CTRL + A (para selecionar toda a consulta) e consultar

WITH AA AS( SELECT A.DATA FROM ERP_MXSDATAS A WHERE DATA BETWEEN TO_DATE(:dtinicio, 'dd/mm/yyyy') AND TO_DATE(:dtfim, 'dd/mm/yyyy') GROUP BY A.DATA
)
, B AS( SELECT DIAUTIL, TO_CHAR(A.DATA,'MM/YYYY') AS DATA FROM ERP_MXSDATAS A JOIN AA ON A.DATA = AA.DATA ),
A AS ( SELECT DEVOL.DATA AS DATA, DECODE('S','N',0,SUM(DEVOL.VLDEVOLUCAO - 0 - 0 - DEVOL.VLREPASSE)) VLTOTAL FROM( SELECT TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY') AS DATA, NVL( SUM( CASE WHEN ERP_MXSNFSAID.CONDVENDA IN (6,11) THEN 0 ELSE ( NVL (ERP_MXSMOV.QT, 0) * ( NVL (ERP_MXSMOV.PUNIT, 0) + NVL (ERP_MXSMOV.VLFRETE, 0) + NVL (ERP_MXSMOV.VLOUTRASDESP, 0) + NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) + NVL (ERP_MXSMOV.VLOUTROS, 0) - NVL (ERP_MXSMOV.VLREPASSE, 0))) END ), 0) AS VLDEVOLUCAO, NVL(SUM(NVL (ERP_MXSMOV.QT, 0) * NVL (ERP_MXSMOV.ST, 0)),0) VLST, NVL(SUM(NVL(ERP_MXSMOV.VLIPI, 0) * NVL (ERP_MXSMOV.QT, 0)),0) VLIPI, NVL(ROUND (SUM(ERP_MXSMOV.QT * ERP_MXSMOV.VLREPASSE), 2), 0) VLREPASSE FROM ERP_MXSNFENT, ERP_MXSESTCOM, ERP_MXSTABDEV, MXSCLIENT, MXSEMPR, MXSUSUARI, MXSSUPERV, MXSFORNEC F, ERP_MXSNFSAID, ERP_MXSMOV, MXSPRODUT, ERP_MXSDEVCONSUM, MXSHISTORICOPEDC VENDAS WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT(+) AND ERP_MXSNFENT.CODDEVOL = ERP_MXSTABDEV.CODDEVOL(+) AND MXSCLIENT.CODCLI = ERP_MXSNFENT.CODFORNEC AND ERP_MXSNFENT.NUMTRANSENT = ERP_MXSDEVCONSUM.NUMTRANSENT(+) AND ERP_MXSNFENT.CODMOTORISTADEVOL = MXSEMPR.MATRICULA(+) AND ERP_MXSNFENT.CODUSURDEVOL = MXSUSUARI.CODUSUR AND MXSUSUARI.CODSUPERVISOR = MXSSUPERV.CODSUPERVISOR(+) AND TO_NUMBER(ERP_MXSESTCOM.NUMTRANSENT) = ERP_MXSMOV.NUMTRANSENT AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD(+) AND NVL (TO_CHAR(ERP_MXSMOV.DTCANCEL,'DD-MM-YYYY'), '00-00-0000') = '00-00-0000' AND NVL (ERP_MXSMOV.CODOPER, 'ED') = 'ED' AND TRUNC(ERP_MXSNFENT.DTENT) BETWEEN TO_DATE(:dtinicio, 'dd/mm/yyyy') AND TO_DATE(:dtfim, 'dd/mm/yyyy') AND ERP_MXSNFENT.TIPODESCARGA IN ('6','7','T') AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA' AND ERP_MXSNFENT.CODFISCAL IN ('131','132','231','232','199','299') AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+) AND NVL(ERP_MXSNFSAID.CONDVENDA,0) NOT IN (4, 8, 10, 13, 20, 98, 99) AND MXSUSUARI.CODSUPERVISOR IN (SELECT KEYDADOS AS CODSUPERVISOR FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = :codusuario ) AND ERP_MXSESTCOM.NUMTRANSVENDA = VENDAS.NUMTRANSVENDA(+) AND ERP_MXSNFENT.CODFILIAL IN (SELECT KEYDADOS FROM MXACESSODADOS Z WHERE Z.CODDADOS = '6' AND Z.CODUSUARIO = :codusuario ) AND F.CODFORNEC(+) = ERP_MXSNFENT.CODFORNEC
GROUP BY TO_CHAR(ERP_MXSNFENT.DTENT,'MM/YYYY')
) DEVOL
GROUP BY DEVOL.DATA
)
SELECT 'DEVOL' SERIE, NVL(B.DATA, A.DATA) DATA, B.DIAUTIL DIAUTIL, NVL(A.VLTOTAL,0) VLTOTAL FROM A LEFT JOIN B ON A.DATA = B.DATA GROUP BY NVL(B.DATA, A.DATA), B.DIAUTIL, VLTOTAL, 'DEVOL'

/*\######################################################################################################################################################################################################################*/

-->>WINTHOR

-->>Consulta para verificar as devoluções por Data de faturamento do pedido

-->>Ela considera todos os supervisores, filiais, RCAs que o usuário possuir acesso nas permissões do maxGestão

-->>Importante se atentar às validações da consulta no WHERE e ao CASE no SELECT

-->>É só jogar a consulta na IDE (Dbeaver ou SQL Developer) apertar no teclado CTRL + A (para selecionar toda a consulta) e consultar

WITH DEVOL_RESUMO_FATURAMENTO AS ( SELECT ERP_MXSNFENT.DTENT AS DTENT, ERP_MXSNFENT.CODFILIAL, ROUND ( ( NVL (ERP_MXSMOV.QT, 0) * DECODE ( ERP_MXSNFSAID.CONDVENDA, 5, 0, 6, 0, 11, 0, 12, 0, DECODE (ERP_MXSMOV.CODOPER, 'SB', 0, NVL (ERP_MXSMOV.ST, 0)))), 2) VLST, DECODE (NVL (ERP_MXSNFSAID.CONDVENDA, 0), 5, 0, 6, 0, 11, 0, (NVL (ERP_MXSMOV.VLIPI, 0) * NVL (ERP_MXSMOV.QT, 0))) VLIPI, CASE WHEN SUBSTR (ERP_MXSMOV.ROTINACAD, 7, 5) = '1361' THEN NVL (ERP_MXSMOV.QT, 0) * NVL (ERP_MXSMOV.PUNITCONT, 0) ELSE ( NVL (ERP_MXSMOV.QT, 0) * ( CASE WHEN ERP_MXSNFSAID.CONDVENDA = 6 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 11 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 1 THEN CASE WHEN NVL (ERP_MXSMOVCOMPLE.BONIFIC, 'N') = 'N' THEN ( CASE WHEN ERP_MXSMOV.PUNIT = 0 THEN ERP_MXSMOV.PUNITCONT WHEN ERP_MXSMOV.PUNIT IS NULL THEN ERP_MXSMOV.PUNITCONT ELSE ERP_MXSMOV.PUNIT END + NVL (ERP_MXSMOV.VLFRETE, 0) + NVL (ERP_MXSMOV.VLOUTRASDESP, 0) + NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) + NVL (ERP_MXSMOV.VLOUTROS, 0)) ELSE 0 END ELSE CASE WHEN ERP_MXSMOV.PUNIT = 0 THEN ERP_MXSMOV.PUNITCONT WHEN ERP_MXSMOV.PUNIT IS NULL THEN ERP_MXSMOV.PUNITCONT ELSE ERP_MXSMOV.PUNIT END + NVL (ERP_MXSMOV.VLFRETE, 0) + NVL (ERP_MXSMOV.VLOUTRASDESP, 0) + NVL (ERP_MXSMOV.VLFRETE_RATEIO, 0) + NVL (ERP_MXSMOV.VLOUTROS, 0) END - CASE WHEN ERP_MXSNFSAID.CONDVENDA = 6 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 11 THEN 0 ELSE NVL (ERP_MXSMOV.VLREPASSE, 0) END - CASE WHEN ERP_MXSNFSAID.CONDVENDA = 6 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 11 THEN 0 ELSE NVL (ERP_MXSMOV.ST, 0) END)) + ROUND ( ( NVL (ERP_MXSMOV.QT, 0) * CASE WHEN ERP_MXSNFSAID.CONDVENDA = 6 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 11 THEN 0 WHEN ERP_MXSNFSAID.CONDVENDA = 12 THEN 0 ELSE CASE WHEN ERP_MXSMOV.CODOPER = 'SB' THEN 0 ELSE NVL (ERP_MXSMOV.ST, 0) END END), 2) END AS VLDEVOLUCAO, CASE WHEN NVL (ERP_MXSNFSAID.CONDVENDA, 0) = 6 THEN 0 WHEN NVL (ERP_MXSNFSAID.CONDVENDA, 0) = 11 THEN 0 ELSE NVL (ROUND (ERP_MXSMOV.QT * ERP_MXSMOV.VLREPASSE, 2), 0) END AS VLREPASSE, ERP_MXSNFENT.CODFORNEC AS CODCLI, COALESCE (MXSHISTORICOPEDC.CODSUPERVISOR, MXSUSUARI.CODSUPERVISOR) AS CODSUPERVISOR, NVL (ERP_MXSNFSAID.CONDVENDA, 0) AS CONDVENDA, ERP_MXSNFENT.CODUSURDEVOL AS CODUSUR, 0 AS VLBONIFIC, MXSFORNEC.CODFORNEC FROM ERP_MXSNFENT, ERP_MXSESTCOM, ERP_MXSNFSAID, ERP_MXSMOV, MXSPRODUT, MXSCLIENT, MXSFORNEC, MXSPRACA, ERP_MXSTABDEV, MXSUSUARI, MXSHISTORICOPEDC, MXSFORNEC FORNECPRINC, ERP_MXSMOVCOMPLE WHERE ERP_MXSNFENT.NUMTRANSENT = ERP_MXSESTCOM.NUMTRANSENT AND MXSCLIENT.CODPRACA = MXSPRACA.CODPRACA(+) AND ERP_MXSESTCOM.NUMTRANSENT = ERP_MXSMOV.NUMTRANSENT AND MXSFORNEC.CODFORNEC(+) = MXSPRODUT.CODFORNEC AND ERP_MXSNFSAID.NUMPED = MXSHISTORICOPEDC.NUMPED(+) AND MXSFORNEC.CODFORNECPRINC = FORNECPRINC.CODFORNEC(+) AND ERP_MXSNFENT.CODDEVOL = ERP_MXSTABDEV.CODDEVOL(+) AND ERP_MXSNFENT.CODUSURDEVOL = MXSUSUARI.CODUSUR(+) AND ERP_MXSESTCOM.NUMTRANSVENDA = ERP_MXSNFSAID.NUMTRANSVENDA(+) AND ERP_MXSMOV.CODPROD = MXSPRODUT.CODPROD AND ERP_MXSNFENT.CODFORNEC = MXSCLIENT.CODCLI AND NVL (ERP_MXSESTCOM.NUMTRANSVENDA, 0) <> 0 AND NVL (ERP_MXSNFENT.TIPODESCARGA, 'X') IN ('6', '7', 'T', 'X') AND NVL (ERP_MXSNFENT.CODFISCAL, 0) IN (131, 132, 231, 232, 199, 299) AND NVL (TO_CHAR (ERP_MXSMOV.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000' AND NVL (ERP_MXSMOV.CODOPER, 'ED') = 'ED' AND ( NVL (ERP_MXSNFENT.ESPECIE, 'X') <> 'OE' OR ( NVL (ERP_MXSNFENT.ESPECIE, 'X') = 'OE' AND NVL (ERP_MXSNFSAID.VENDAASSISTIDA, 'N') = 'S' AND ERP_MXSNFSAID.CONDVENDA = 7)) AND NVL (ERP_MXSNFENT.OBS, 'X') <> 'NF CANCELADA' AND ERP_MXSMOV.NUMTRANSITEM = ERP_MXSMOVCOMPLE.NUMTRANSITEM(+) AND NVL(ERP_MXSMOV.CODOPERACAO,0) != 2 AND NVL(ERP_MXSNFENT.CODOPERACAO,0) != 2 AND NVL(MXSHISTORICOPEDC.CODOPERACAO,0) != 2 AND NVL(ERP_MXSNFSAID.CODOPERACAO,0) != 2 AND NVL(MXSPRODUT.CODOPERACAO,0) != 2 AND NVL (ERP_MXSNFENT.TIPOMOVGARANTIA, -1) = -1 AND TRUNC(ERP_MXSNFENT.DTENT) BETWEEN TRUNC(TO_DATE('01/03/2025', 'dd/mm/yyyy')) AND TRUNC(TO_DATE('31/03/2025', 'dd/mm/yyyy')) AND ERP_MXSNFSAID.CONDVENDA NOT IN (4,8,10,13,20,98,99))

> SELECT SUM(DEVOL.VLDEVOLUCAO - 0 - 0 - DEVOL.VLREPASSE) VLDEVOLUCAO FROM DEVOL_RESUMO_FATURAMENTO DEVOL , MXSSUPERV, MXSUSUARI, MXSCLIENT WHERE MXSSUPERV.CODSUPERVISOR = DEVOL.CODSUPERVISOR AND TRUNC(DEVOL.DTENT) BETWEEN TRUNC(TO_DATE('01/03/2025', 'dd/mm/yyyy')) AND TRUNC(TO_DATE('31/03/2025', 'dd/mm/yyyy')) AND MXSUSUARI.CODUSUR = DEVOL.CODUSUR AND MXSCLIENT.CODCLI = DEVOL.CODCLI

---

## Doc-MXGESNDV-17889.docx

**Devoluções zeradas** TICKET: MXGESNDV-17889

> **CAUSA:**
>
> Falta de padronização do comportamento dos filtros no PWA Mobile.

# ANÁLISE:

> Os filtros no maxGestão PWA Mobile não possuíam padronização de funcionamento quanto aos valores que carregam por default e também sobre as informações que carregavam após pressionar os botões limpar todos os campos ou limpar os valores das datas em específico.

# REGRA DE NEGÓCIO:

# Realizada padronização do comportamento dos filtros do PWA Mobile. Agora todos os filtros iniciam no primeiro dia do mês na data inicial e o dia atual na data final. Caso limpe os filtros eles seguem a mesma regra.

---

## Doc-MXGESNDV-17890.docx

**Devoluções zeradas** TICKET: MXGESNDV-17890

> **CAUSA:**
>
> Intermitência na comunicação do Extrator do maxPedido causa a falha de conclusão do processo de transferência de Saldo de Conta Corrente realizado através do maxGestão porque nós chamamos a API do maxPedido para realizar o processo.

# ANÁLISE:

> Durante a análise foram identificados logs de intermitência na comunicação do Extrator com o banco de dados Winthor e também observado que o atualizador automático da versão do Extrator estava desligado.

# REGRA DE NEGÓCIO:

O maxGestão faz a requisição de transferência de Conta Corrente para a API do maxPedido corretamente e a API do maxPedido utiliza o Extrator para realizar a operação no banco de dados do Winthor. Durante a análise foram identificados logs de intermitência na comunicação do Extrator com o banco de dados Winthor e também observado que o atualizador automático da versão do Extrator estava desligado.\
\
Foi feita a reativação do Atualizador Automático e reiniciado o Extrator do cliente. Feito isso observamos que a versão foi atualizada corretamente e a conectividade do Extrator voltou ao seu funcionamento ideal. Com o Extrator funcionamento corretamente a transferência de Saldo de Conta Corrente voltou a funcionar.

É importante que o Extrator do maxPedido esteja com o funcionamento ideal, estável e com os acessos à porta 9002 liberados em relação às nossas máquinas da AWS.

---

## Doc-MXGESNDV-17896.docx

**Devoluções zeradas** TICKET: MXGESNDV-17896

> **CAUSA:**
>
> Problemas de compatibilidade de informação entre maxGestão e maxMotorista.

# ANÁLISE:

> Durante a análise foi identificado que somente o campo "Em Espera" está compatível com o maxMotorista no filtro de Monitoramento "Clicar em Dashboard - Painel de Monitoramento\
> Filtrar a data desejada\
> Observar o campo Em espera (ao lado de um ícone de um boneco roxo com reloginho)"
>
> Qualquer alteração nas regras do Gestão teria de ser considerada a partir de agora uma melhoria porque precisamos definir um melhor escopo de integração com o maxMotorista.

# REGRA DE NEGÓCIO:

> Atualmente o maxGestão tem uma regra própria para definir os status de Entregas que são exibidos no Painel Geral. Recentemente foram realizados alguns ajustes, mas é importante deixar claro que comparações com outros sistemas da Máxima ou terceiros não são válidas.\
> \
> Todas as informações geradas abaixo são consideradas de consultas realizadas no banco de dados Nuvem da Máxima:\
> \
> Quantidade "Em Entrega": Essa informação busca entregas com a situação 'CK' (CHECKIN) que já estão com a data de início da descarga iniciada, ou seja, que já iniciou a descarga e ainda não finalizou. Considera a data de Checkin da entrega conforme os filtros realizados no Painel Geral.\
> \
> Quantidade "Em Espera": Essa informação busca entregas com a situação 'EP' (ESPERA) que ainda estão com a data de início da descarga zeradas, ou seja, que não iniciou ainda a descarga e considera a data de saída do carregamento conforme os filtros realizados no Painel Geral.\
> \
> Quantidade "Em Trânsito": Essa informação busca entregas com a situação 'PD' (PENDENTE) que já estão com o romaneio em situação "INICIADO" e considera a data de início do romaneio conforme os filtros realizados no Painel Geral.
>
> C:\MaximaSistemas\maxgestao\MaximaSistemas.Data.Context\SQL\DashBoards\ResumoVendas\Nuvem\ObtenhaDashBoardIndicadoresVenda_v6.sql

WITH /\*+ INDICADORES EMISSAO \*/ TOTALPEDIDOAUTORIZADO AS (
SELECT COUNT(*) AS QTDPEDIDOAUTORIZADO
FROM MXSINTEGRACAOPEDIDO VENDAS
{TABELAMXSCLIENT}
WHERE TRUNC(VENDAS.DATA) BETWEEN :DATAINICIAL AND :DATAFINAL
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '5' AND KEYDADOS = VENDAS.CODSUPERVISOR)
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)
AND CODUSUARIOAUTORIZOU IS NOT NULL
AND STATUS NOT IN ({STATUSPEDIDO})
{PARAM_EQUIPE} {FILIAL} {REPRESENTANTE} {TIPOVENDA} {CLIENTE}
),
TOTALPEDIDOS AS (
SELECT
SUM(CASE VENDAS.STATUS WHEN 0 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS SALVONANUVEM,
SUM(CASE VENDAS.STATUS WHEN 1 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS ENVIADOPARAAPI,
SUM(CASE VENDAS.STATUS WHEN 2 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS ENVIADOAOERP,
SUM(CASE VENDAS.STATUS WHEN 3 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS EMPROCESSAMENTOPELOERP,
SUM(CASE VENDAS.STATUS WHEN 4 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS PROCESSADOCOMSUCESSO,
SUM(CASE VENDAS.STATUS WHEN 5 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS FALHATOTAL,
SUM(CASE VENDAS.STATUS WHEN 6 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS BLOQUEADOPARAENVIO,
SUM(CASE VENDAS.STATUS WHEN 7 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS PEDIDOCANCELADO,
SUM(CASE VENDAS.STATUS WHEN 8 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS AGUARDANDOAUTORIZACAO,
SUM(CASE VENDAS.STATUS WHEN 10 THEN COUNT(VENDAS.STATUS) ELSE 0 END) AS PEDIDONEGADO,
0 AS QTDPEDIDOREALIZADO
FROM MXSINTEGRACAOPEDIDO VENDAS
WHERE TRUNC(VENDAS.DATA) BETWEEN :DATAINICIAL AND :DATAFINAL
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '5' AND KEYDADOS = VENDAS.CODSUPERVISOR)
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)
{FILIAL} {REPRESENTANTE} {FILTROEQUIPE} {TIPOVENDA} {CLIENTE}
GROUP BY VENDAS.STATUS
),
TOTPESOTAB AS (
SELECT SUM(TOTPESO) TOTPESO, SUM(TOTVOLUME) TOTVOLUME
FROM MXSHISTORICOPEDC VENDAS
LEFT JOIN (
SELECT DISTINCT NUMPEDERP, CODSUPERVISOR
FROM MXSINTEGRACAOPEDIDO
WHERE TRUNC(DATA) BETWEEN :DATAINICIAL AND :DATAFINAL
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '5' AND MXSINTEGRACAOPEDIDO.CODSUPERVISOR = KEYDADOS)
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND MXSINTEGRACAOPEDIDO.CODFILIAL = KEYDADOS)
AND CODSUPERVISOR IS NOT NULL
) MXSI ON MXSI.NUMPEDERP = VENDAS.NUMPED
WHERE TRUNC(VENDAS.DATA) BETWEEN :DATAINICIAL AND :DATAFINAL
AND VENDAS.POSICAO <> 'C'
AND VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)
AND EXISTS(SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = :CODUSUARIO AND KEYDADOS = VENDAS.CODSUPERVISOR
UNION ALL
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = :CODUSUARIO AND KEYDADOS = MXSI.CODSUPERVISOR AND VENDAS.CODSUPERVISOR IS NULL)
AND VENDAS.CODOPERACAO <> 2
{FILIAL} {REPRESENTANTE} {EQUIPE} {TIPOVENDA} {CLIENTE} {PEDIDO}
),
TOTALCARGAS AS (
SELECT
SUM(QTDEMENTREGA) AS QTEMENTREGA,
SUM(QTEMESPERA) AS QTEMESPERA,
SUM(QTEMTRANSITO) AS QTEMTRANSITO,
SUM(QTSEMCARGA) AS QTSEMCARGA
FROM (
SELECT COUNT(DISTINCT CAR.CODMOTORISTA) AS QTDEMENTREGA, 0 AS QTEMESPERA, 0 AS QTEMTRANSITO, 0 AS QTSEMCARGA
FROM MXMP_ENTREGAS E
INNER JOIN ERP_MXSCARREG CAR ON CAR.NUMCAR = E.ID_CARREGAMENTO AND CAR.NUMCAR NOT IN ( '-1', '0' )
LEFT JOIN ERP_MXSVEICUL MXSVEICUL ON MXSVEICUL.CODVEICULO = CAR.CODVEICULO
INNER JOIN MXSEMPR MOT ON MOT.MATRICULA = CAR.CODMOTORISTA
WHERE TRUNC(E.DATA_CHECKIN) BETWEEN :DATAINICIAL AND :DATAFINAL
AND NVL(TO_CHAR(E.DATA_INICIO_DESCARGA, 'DD-MM-YYYY'), '00-00-0000') != '00-00-0000'
AND NVL(TO_CHAR(E.DATA_TERMINO_DESCARGA, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND E.SITUACAO = 'CK'
AND EXISTS (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND KEYDADOS = MOT.CODFILIAL)
UNION ALL
SELECT 0 AS QTEMENTREGA, COUNT(DISTINCT CAR.CODMOTORISTA) AS QTEMESPERA, 0 AS QTEMTRANSITO, 0 AS QTSEMCARGA
FROM MXMP_ENTREGAS E
INNER JOIN ERP_MXSCARREG CAR ON CAR.NUMCAR = E.ID_CARREGAMENTO AND CAR.NUMCAR NOT IN ( '-1', '0' )
LEFT JOIN ERP_MXSVEICUL MXSVEICUL ON MXSVEICUL.CODVEICULO = CAR.CODVEICULO
INNER JOIN MXSEMPR MOT ON MOT.MATRICULA = CAR.CODMOTORISTA
WHERE TRUNC(CAR.DTSAIDA) BETWEEN :DATAINICIAL AND :DATAFINAL
AND NVL(TO_CHAR(E.DATA_INICIO_DESCARGA, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND E.SITUACAO = 'EP'
AND EXISTS (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND KEYDADOS = MOT.CODFILIAL)
UNION ALL
SELECT 0 AS QTEMENTREGA, 0 AS QTEMESPERA, COUNT(DISTINCT U.ID) AS QTEMTRANSITO, 0 AS QTSEMCARGA
FROM MXMP_USUARIOS U
INNER JOIN ERP_MXSCARREG CAR ON CAR.CODMOTORISTA = U.ID_MOTORISTA AND CAR.NUMCAR NOT IN ( '-1', '0' )
LEFT JOIN ERP_MXSVEICUL MXSVEICUL ON MXSVEICUL.CODVEICULO = CAR.CODVEICULO
INNER JOIN MXSEMPR MOT ON MOT.MATRICULA = CAR.CODMOTORISTA
INNER JOIN MXMP_ENTREGAS E ON E.ID_CARREGAMENTO = CAR.NUMCAR
INNER JOIN MXMP_ROMANEIO ROM ON ROM.ID = CAR.ID_ROMANEIO
WHERE U.ID_MOTORISTA IS NOT NULL
AND U.TIPO = 'M'
AND U.EXCLUIDO = 'N'
AND TRUNC(ROM.DT_INICIO) BETWEEN :DATAINICIAL AND :DATAFINAL
AND E.SITUACAO = 'PD'
AND ROM.SITUACAO = 'INICIADO'
AND EXISTS (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND KEYDADOS = MOT.CODFILIAL)
UNION ALL
SELECT 0 AS QTEMENTREGA, 0 AS QTEMESPERA, 0 AS QTEMTRANSITO, COUNT(DISTINCT U.ID) AS QTSEMCARGA
FROM MXMP_USUARIOS U
INNER JOIN MXSEMPR MOT ON MOT.MATRICULA = U.ID_MOTORISTA
LEFT JOIN ERP_MXSCARREG CAR ON CAR.CODMOTORISTA = U.ID_MOTORISTA AND CAR.NUMCAR NOT IN ( '-1', '0' ) AND NVL(TO_CHAR(CAR.DTFECHA, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
LEFT JOIN ERP_MXSVEICUL MXSVEICUL ON MXSVEICUL.CODVEICULO = CAR.CODVEICULO
WHERE U.ID_MOTORISTA IS NOT NULL
AND U.TIPO = 'M'
AND U.EXCLUIDO = 'N'
AND CAR.CODMOTORISTA IS NULL
AND EXISTS (SELECT KEYDADOS FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND KEYDADOS = MOT.CODFILIAL)
)
)
SELECT
TABPEDIDO.*,
TA.QTDPEDIDOAUTORIZADO AS PEDIDOAUTORIZADO,
TC.QTEMENTREGA,
TC.QTEMESPERA,
TC.QTEMTRANSITO,
TC.QTSEMCARGA
FROM (
SELECT
SUM(SALVONANUVEM) AS SALVONANUVEM,
SUM(ENVIADOPARAAPI) AS ENVIADOPARAAPI,
SUM(ENVIADOAOERP) AS ENVIADOAOERP,
SUM(EMPROCESSAMENTOPELOERP) AS EMPROCESSAMENTOPELOERP,
SUM(PROCESSADOCOMSUCESSO) AS PROCESSADOCOMSUCESSO,
SUM(FALHATOTAL) AS FALHATOTAL,
SUM(BLOQUEADOPARAENVIO) AS BLOQUEADOPARAENVIO,
SUM(PEDIDOCANCELADO) AS PEDIDOCANCELADO,
SUM(AGUARDANDOAUTORIZACAO) AS AGUARDANDOAUTORIZACAO,
SUM(PEDIDONEGADO) AS PEDIDONEGADO,
SUM(VALORTOTAL) AS VALORTOTAL,
SUM(QTDPEDIDOREALIZADO) AS QTDPEDIDOREALIZADO,
SUM(QTDITENS) AS QTDITENS,
SUM(ROUND(TOTVOLUME, 2)) AS TOTVOLUME,
SUM(ROUND((TOTPESO / 1000), 2)) AS TOTPESO
FROM (
SELECT
0 AS SALVONANUVEM, 0 AS ENVIADOPARAAPI, 0 AS ENVIADOAOERP, 0 AS EMPROCESSAMENTOPELOERP,
0 AS PROCESSADOCOMSUCESSO, 0 AS FALHATOTAL, 0 AS BLOQUEADOPARAENVIO, 0 AS PEDIDOCANCELADO,
0 AS AGUARDANDOAUTORIZACAO, 0 AS PEDIDONEGADO,
COUNT(DISTINCT(VENDAS.NUMPED)) AS QTDPEDIDOREALIZADO,
SUM(NVL(DECODE(VENDAS.CONDVENDA, 6, 0, 11, 0, 12, 0, ROUND((ITEMPED.QT * ITEMPED.PVENDA), 2) - {ST} - {IPI}), 0)) - {BONIFIC} AS VALORTOTAL,
SUM({TIPOVENDADECODEITENS}) AS QTDITENS,
MAX((SELECT TOTPESO FROM TOTPESOTAB)) AS TOTPESO,
MAX((SELECT TOTVOLUME FROM TOTPESOTAB)) AS TOTVOLUME
FROM MXSHISTORICOPEDC VENDAS
{TABELAMXSCLIENT}
INNER JOIN MXSHISTORICOPEDI ITEMPED ON VENDAS.NUMPED = ITEMPED.NUMPED
{TABELADEVOLQUERYINDICADORES}
{TABELAMXSCLIENT}
INNER JOIN MXSUSUARI US ON VENDAS.CODUSUR = US.CODUSUR
LEFT JOIN (
SELECT DISTINCT NUMPEDERP, CODSUPERVISOR, CODUSUR
FROM MXSINTEGRACAOPEDIDO
WHERE CODSUPERVISOR IS NOT NULL
AND TRUNC(DATA) BETWEEN :DATAINICIAL AND :DATAFINAL
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '5' AND MXSINTEGRACAOPEDIDO.CODSUPERVISOR = KEYDADOS)
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND MXSINTEGRACAOPEDIDO.CODFILIAL = KEYDADOS)
AND CODSUPERVISOR IS NOT NULL
) MXSI ON MXSI.NUMPEDERP = VENDAS.NUMPED AND MXSI.CODUSUR = VENDAS.CODUSUR
WHERE VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'
AND TRUNC(VENDAS.DATA) BETWEEN :DATAINICIAL AND :DATAFINAL
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = :CODUSUARIO AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)
AND EXISTS(SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = :CODUSUARIO AND KEYDADOS = VENDAS.CODSUPERVISOR
UNION ALL
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = :CODUSUARIO AND KEYDADOS = MXSI.CODSUPERVISOR AND VENDAS.CODSUPERVISOR IS NULL)
AND VENDAS.CODOPERACAO <> 2
AND ITEMPED.CODOPERACAO <> 2
AND VENDAS.POSICAO <> 'C'
AND NVL(ITEMPED.POSICAO, 'L') <> 'C'
{FILIAL} {REPRESENTANTE} {EQUIPE} {TIPOVENDA} {CLIENTE} {PEDIDO} {RESTRICAODEVOLQUERYINDICADORES}
UNION
SELECT T.*, 0 AS VALORTOTAL, 0 AS QTITENS, 0 AS TOTPESO, 0 AS TOTVOLUME FROM TOTALPEDIDOS T
)
HAVING SUM(SALVONANUVEM) IS NOT NULL
) TABPEDIDO
LEFT JOIN TOTALPEDIDOAUTORIZADO TA ON 1 = 1
LEFT JOIN TOTALCARGAS TC ON 1 = 1

---

## Doc-MXGESNDV-17930.docx

KM TRABALHADOS e KM TOTAL Zerados TICKET: MXGESNDV-17930

> **CAUSA:**
>
> No Relatório de Auditoria os campos KM TRABALHADOS e KM TOTAL estão zerados.

# ANÁLISE:

> O resultado de Km Trabalhado e Total estão zerados devido a configuração atual que está sendo utilizada no maxGestão.
>
> Configurações do Sistema
>
> >> Configurações Gerais
>
> opção >> Utilizar ponto inicial/ponto final do Roteirizador.
>
> >> Painel de Auditoria
>
> opção >> Utiliza Validação Mesmo Rastro Para Eventos
>
> Vamos explicar melhor abaixo o que ocorre:
>
> Quando o a opção de "Utilizar ponto inicial/ponto final do Roteirizador" está marcada, então é feito um recálculo do Km Trabalhado que considera a soma do Km previsto para o dia no roteirizador + o Km Trabalhado de fato pelo RCA, (Km que foi apurado pelo maxPedido).
>
> Quando a opção "Utiliza Validação Mesmo Rastro Para Eventos" está ativa, a gente verifica a diferença entre os Kms: Caso a soma do Km previsto para o dia no roteirizador + o Km Trabalhado seja maior que o Km Total apurado pelo maxPedido, que é o Km real rodado pelo RCA no dia, então automaticamente zeramos todos os dados de km Trabalhado e Total para evitar uma possível inconsistência na lógica dessas informações.
>
> Possíveis soluções:
>
> Nós entendemos que o cliente quer ver os Km trabalhados e totais dos RCAs então nós recomendamos a desativação de ambas configurações:
>
> Configurações do Sistema
>
> >> Configurações Gerais
>
> opção >> Utilizar ponto inicial/ponto final do Roteirizador.
>
> >> Painel de Auditoria
>
> opção >> Utiliza Validação Mesmo Rastro Para Eventos
>
> Quando elas estão desativadas então o fluxo citado referente aos recálculos e demais validações não ocorre e somente o valor real capturado pelo maxPedido é apresentado.
>
> Caso somente a opção >> Utiliza Validação Mesmo Rastro Para Eventos for desabilitada então o Km Trabalhado será exibido maior que o Km Total devido a questão de somar ao Km Previsto do Roteirizador que explicamos.

# REGRA DE NEGÓCIO:

# Atualmente quando habilitada a opção de utilizar ponto inicial e final do Roteirizador no Km Trabalhado do maxGestão, a gente usa o Km Previsto do Roteirizador para aquele RCA e dia da semana e soma isso ao Km Trabalhado que foi gerado pelo maxPedido então pode ocorrer do Km Rodado (Total) ficar menor que o Km Trabalhado.

---

## Doc-MXGESNDV-17951.docx

Detalhamento media de itens por faturamento - Indicadores de Vendas TICKET: MXGESNDV-17951

> **CAUSA:**
>
> A query apresenta alto consumo de recursos do banco de dados e onera a API com requisições desnecessárias no front-end

# ANÁLISE:

# A consulta de media de itens por faturamento nos indicadores de vendas está gerando alguns alertas de desempenho referente a alto consumo e lentidão na execução.

# 

# REGRA DE NEGÓCIO:

# Foi ajustada a query do /\* PRODUTOPEDIDO_MEDIA_ITENS_DESCRICAO_FATURAMENTO \*/ e agora a regra está centralizada com a do /\* PRODUTOPEDIDO_MEDIA_ITENS_FATURAMENTO \*/, os dados na maioria das vezes batem se você somar a média agrupada por item e comparar com a média total.

# Os dados somente não [irão]{.underline} bater se você somar a média dos itens para comparar com a média total devido a questões e arredondamento das casas decimais. Porém se você por exemplo, aumenta o número de casas decimais e soma para comparar os valores ficam corretos. Foi removida a regra que considerava itens da ERP_MXSNFENT por data de entrada da nota e baseadas no CODUSURDEVOL. Esses valores por data de Emissão do painel geral devem bater com a rotina 146 e por data de Faturamento devem bater/se aproximar com a Rotina 111.

---

## Doc-MXGESNDV-18594.docx

LENTIDÃO NO PROCESSO DE TRANSFERÊNCIA DE SALDO DE CONTA CORRENTE Winthor TICKET: MXGESNDV-18594

> **CAUSA:**
>
> Havíamos adicionado uma tela de carregamento que obrigava o usuário a aguardar 30 segundos o processo de consolidação dos dados da transferência de saldo de conta corrente no banco de dados.

# ANÁLISE:

Apresentávamos uma mensagem de "Processando Transferência" para aguardar a consolidação dos dados no banco nuvem. Nesse processo fazíamos o usuário aguardar 30 segundos o que pode ter gerado o relato de lentidão que o cliente vem sentido.

# REGRA DE NEGÓCIO:

Antes: apresentávamos uma mensagem de "Processando Transferência" para aguardar a consolidação dos dados no banco nuvem. Nesse processo fazíamos o usuário aguardar 30 segundos o que pode ter gerado o relato de lentidão que o cliente vem sentido.\
\
Agora: A tela de "Processando Transferência" foi removida. Ela não será mais exibida nem no Gestão de Conta Corrente e nem na Autorização de pedidos quando for necessário autorizar o pedido.\
Agora a gente fez tratativas no código para caso o saldo ainda não tenha sido consolidado no banco nuvem, mesmo assim a gente vai calcular só a nível de front-end, o saldo transferido + o saldo Atual do RCA caso ocorra transferência de saldo. Também será atualizado o Saldo Após aprovação do pedido + saldo transferido.

No maxGestão PWA, existe um processo diferente que aguarda a transferência de saldo de conta corrente e sempre retorna corretamente a informação do saldo do RCA após a transferência.

---

## Doc-MXGESNDV-17995.docx

Registros de 2 eventos no painel de auditoria TICKET: MXGESNDV-17995

> **CAUSA:**
>
> Registros de 2 eventos no painel de auditoria causados por eventos gerados pelo maxPedido sem o mesmo código de vinculação.

# ANÁLISE:

> O maxGestão atualmente faz o agrupamento "Checkin + ação" ou "Checkout + ação" ou "Checkin + ação + Checkout" ou "Checkin + Checkout" somente se o código de vinculação destes for o mesmo na informação do rastro que é gerado pelo maxPedido e gravado na API de rastros:
> https://maxrastro-prod.solucoesmaxima.com.br/swagger/index.html
>
> Se as justificativas de não venda vieram sem código de vinculação compatível com o Checkin + Checkout, dados são apresentados de forma separada. Então o Gestão corretamente mostra o Checkin + Checkout e separadamente a Justificativa de Não venda.
>
> Para que a informação fique unificada no maxGestão os rastros que a gente consulta na API de rastros devem estar assim:
>
> --Aqui eu reduzi o número de informações para ficar mais visível e entendível
>
> [
>
> {
>
> "eventType": "CHECKIN",
>
> },
>
> "checkinCheckout": {
>
> "codigoVinculacao": 1748284550641
>
> },
>
> },
>
> {
>
> "eventType": "JUSTIFICATIVANAOVENDA",
>
> },
>
> "justificativaNaoVenda": {
>
> "codigoVinculacao": 1748284550641
>
> },
>
> },
>
> {
>
> "eventType": "CHECKOUT",
>
> "checkinCheckout": {
>
> "codigoVinculacao": 1748284550641
>
> },
>
> }
>
> ]
>
> No dia 22/05/2025 a gente recebeu assim:
>
> [
>
> {
>
> "eventType": "CHECKIN",
>
> },
>
> "checkinCheckout": {
>
> "codigoVinculacao": 1747917846557
>
> },
>
> },
>
> {
>
> "eventType": "JUSTIFICATIVANAOVENDA",
>
> "justificativaNaoVenda": {
>
> "codigoVinculacao": -1
>
> },
>
> },
>
> {
>
> "eventType": "CHECKOUT"
>
> "checkinCheckout": {
>
> "codigoVinculacao": 1747917846557
>
> }
>
> }
>
> E por este motivo os dados foram apresentados de forma separada.
>
> Conclusão: Não se trata de um problema no maxGestão, os dados ficariam unificados nesse cenário, se o maxPedido tivesse gerado eles corretamente para a gente.
>
> Recomendação: Atualizar a versão do maxPedido para a mais recente. Os dados retroativos não podem mais ser alterados. Se o problema persistir então deve ser solicitada uma análise na equipe do maxPedido referente a geração de rastros nas versões mais recentes

# REGRA DE NEGÓCIO:

# O maxGestão atualmente faz o agrupamento "Checkin + ação" ou "Checkout + ação" ou "Checkin + ação + Checkout" ou "Checkin + Checkout" somente se o código de vinculação destes for o mesmo na informação do rastro que é gerado pelo maxPedido e gravado na API de rastros: [[https://maxrastro-prod.solucoesmaxima.com.br/swagger/index.html]{.underline}](https://maxrastro-prod.solucoesmaxima.com.br/swagger/index.html)

> Se as justificativas de não venda vierem sem código de vinculação compatível com o Checkin + Checkout, dados são apresentados de forma separada. Então o Gestão corretamente mostra o Checkin + Checkout e separadamente a Justificativa de Não venda, pedido ou orçamento.

---

## DOC-MXGESNDV-18061.docx

**calculo incorreto no totalizador\
TICKET:** MXGESNDV-18061

------------------------------------------------------------------------

**CAUSA:**\
A API do maxGestão estava calculando a propriedade PercClienteNaoPositivado baseado na coluna Visitados e como ele não visitou nenhum cliente no período, com isso, não entrava no cálculo e ficava zerado;

------------------------------------------------------------------------

**ANÁLISE:**\
A propriedade foi retirada do IF de checagem de visitados > 0 e foi inserida na checagem de agendados > 0, pois o cálculo é: (1 - (Positivados - Agendados) * 100), por exemplo (1 - (5 - 10) * 100);

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
Agora não será preciso ter visita para a propriedade ser calculada, apenas agendados, conforme regra do totalizador;

---

## Doc-MXGESNDV-18071.docx

**Usuário gerente não é apresentado na transferência de CC** TICKET: MXGESNDV-18071

> **CAUSA:**
>
> Na transferência de SaldoCC da autorização de Pedidos não eram validadas as permissões de acesso do usuário logado.

# ANÁLISE:

# Durante a análise foram identificados vários pontos a serem corrigidos referentes a transferência de conta corrente realizada na tela de autorização de pedidos. Dentre eles foi identificada a necessidade de validar as permissões de transferência de conta corrente do usuário logado. Foi incluído o tipoUsuario RepresentanteOrigem para que o destino da Conta Corrente seja carregado corretamente e o processo de transferência possa ocorrer sem falhas. Além disso foi ajustado o processo de fechamento durante a autorização de pedidos para sempre recarregar os dados após a transferência corretamente.

# REGRA DE NEGÓCIO:

# Para o processo de transferência de saldo de conta corrente através da autorização de pedidos, agora o maxGestão web (Angular) valida as permissões de acesso para transferência de saldo do usuário logado. As validações são as mesmas na aba Gestão de Conta Corrente. A correção é justamente nesse ponto, porque na aba de Gestão a operação já era possível por meio do usuário logado, porém por dentro da transferência de saldo na autorização de pedidos, antes não era possível. Deve validar as permissões de transferência de Conta Corrente do usuário logado e caso tenha as permissões, exibir corretamente a listagem de usuários disponíveis na (ORIGEM) da transferência de conta corrente, sendo comparável ao mesmo processo na hora de buscar os usuários de origem no Gestão de Conta Corrente. Para o maxGestão PWA Desktop e Mobile essa correção ainda não foi implementada.

# Comportamento novo: se o usuário abrir o detalhamento do pedido e clicar em aprovar, pendente ou rejeitar, e logo em seguida em cancelar, a listagem de pedidos será atualizada porque o usuário pode ter feito transferência de saldo e se ela não for atualizada dá problema no carregamento dos dados do pedido. Mesmo que ele não tenha feito transferência vamos atualizar a listagem de pedidos, antes o sistema não atualizava essa listagem.

Comportamento novo: Serão realizadas até 5 tentativas de busca do saldo atualizado de conta corrente do RCA, se após as 5 tentativas não encontrar o saldo novo, o antigo será exibido.

---

## DOC-MXGESNDV-18083.docx

**Coluna ticket médio aparece zerada porém com valor de totalizador\
TICKET:** MXGESNDV-18083

------------------------------------------------------------------------

**CAUSA:**\
A propriedade TicketMedio estava com o cálculo errado, pois só eram calculados valores se o Positivados fosse maior que zero, acontece que em alguns cenários os positivados são fora da agenda;

------------------------------------------------------------------------

**ANÁLISE:**\
Foi alterado o cálculo para somar as duas propriedades e se o resultado for maior que zero, será feito o cálculo de ticket médio;

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
Agora o ticket médio será calculado com a soma dos positivados fora e positivados dentro da agenda;

---

## DOC-MXGESNDV-18233.docx

**Erro relatório Analítico de Vendas com divergência de valores\
TICKET:** MXGESNDV-18233

------------------------------------------------------------------------

**CAUSA:**\
Erro relatório Analítico de Vendas com divergência de valores entre ERP e Painel Geral

------------------------------------------------------------------------

**ANÁLISE:**\
O relatório Analítico de Vendas estava retornando todos os pedidos, inclusive os cancelados;

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
Para normalizar com os valores do painel e do winthor, foi adicionada uma cláusula onde só serão retornados pedidos diferentes de 'C' (Cancelados), AND MXSHISTORICOPEDC.POSICAO != 'C';

---

## DOC-MXGESNDV-18312.docx

**Troca no filtro Filial não reflete nos outros\
TICKET:** MXGESNDV-18312

------------------------------------------------------------------------

**CAUSA:**\
O método responsável pela troca, não estava atualizando os demais, apenas o gerente e o coordenador;

------------------------------------------------------------------------

**ANÁLISE:**\
Foi inserida tratativa no método que faz a troca para desmarcar o supervisor e o rca, ao trocar a filia.

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
N/A

---

## DOC-MXGESNDV-18497.docx

**Mensagem de validação do valor da CC do vendedor na aprovação do pedido;\
TICKET:** MXGESNDV-18497

------------------------------------------------------------------------

**CAUSA:**\
Quando o pedido tinha AutorizacaoSaldoccNegativo = true, os valores dos itens sem necessidade de autorização estavam sendo somados ao valorSaldoCC, causando duplicidade e divergência nos valores apresentados e debitados.

------------------------------------------------------------------------

**ANÁLISE:**\
No backend, o cálculo foi ajustado com o método CalculaValoresSaldosContaCorrente(), que considera corretamente os itens com e sem autorização. Também foram revisadas as mensagens de validação. No frontend (PWA), a mensagem e a variável exibida foram corrigidas

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
No fluxo hoje, quando o pedido AutorizacaoSaldoccNegativo = true não é apresentada nenhuma mensagem de conta corrente negativa, o usuário reclama que não aparece mensagem, mas não foi possível simular com os pedidos que foram repassados.

Com isso foram feitos alguns pedidos direto no FECP e o fluxo foi o mesmo no PWA e no Web.

O comportamento validado é que, quando o pedido tem AutorizacaoSaldoccNegativo = true a API não faz validação de Conta corrente faltante, pois, ela pode ficar negativa. Se essa propriedade estiver como false, o fluxo segue e impede a aprovação do pedido, independentemente se for PWA ou Web normal.

---

## Doc-MXGESNDV-18551.docx

Divergência entre maxGestão filtro por data de Emissão e Rotina 146 do Winthor TICKET: MXGESNDV-18551

> **CAUSA:**
>
> Dentro do banco do Winthor do cliente, existe uma divergência entre as tabelas PCPEDC e PCPEDI no que se refere à soma dos históricos das vendas. As querys apresentadas podem ser passadas para o DBA, ou TI responsável realizarem a compreensão da situação. Como existe uma divergência nas próprias tabelas locais, ao realizar a comparação com o maxGestão, os dados não serão compatíveis.\
> \
> Para os dados serem compatíveis entre Rotina 146 e maxGestão, conforme explicamos anteriormente deve existir também uma compatibilidade entre as somas das tabelas PCPEDC e PCPEDI, caso contrário o resultado será este, o cliente terá uma visão das vendas da Rotina 146 e terá outra visão no maxGestão e isso não necessariamente é algo ruim, simplesmente os sistemas apuram essas informações de formas distintas.\
> \
> Friso também que qualquer alteração no comportamento das apurações nos sistemas da Máxima, no que se refere a regra de negócios, deverá ser tratado como melhoria.

# ANÁLISE:

A primeira questão que precisamos considerar para realizar essa análise é que o maxGestão não é obrigado a coincidir com a Rotina 146, porque o filtro de data por emissão de pedido do painel geral não foi programado usando a mesma lógica de apuração dos dados que a Rotina 146 do Winthor. Existem sim outros filtros e relatórios do maxGestão que coincidem com o Winthor, mas não é o caso desse filtro em específico.\
\
O que acontece é que a Rotina 146 do Winthor faz a soma dos valores atendidos por histórico das capas dos pedidos, em termos técnicos, seria a soma SUM(VLATEND) da tabela PCPEDC do Winthor. Enquanto o maxGestão faz a soma através dos históricos dos itens nos pedidos, que em termos técnicos seria SUM(QT * PVENDA) da MXSHISTORICOPEDI (Tabela que vem integrada da PCPEDI).\
\
Existem cenários em que o maxGestão usando filtro de data por emissão de pedido vai coincidir com a Rotina 146, isso acontece somente quando no banco de dados do Winthor (Banco local) a soma SUM(VLATEND) da tabela PCPEDC é a mesma da SUM(QT * PVENDA) da PCPEDI.\
\
Dito isso, vamos entender o cenário:\
\
1° Devemos conceder todas as permissões de acesso disponíveis no maxGestão para o usuário utilizado, por exemplo, o Sysmax\
\
2° Devemos verificar as filiais utilizadas para consultar na Rotina 146: CODFILIAL(1,2,3,7,8,9,14,16,25,26,27,28,29,30,31,32,33,34)\
\
3° Devemos verificar na tabela PCMXSCONFIGURACOES se o parâmetro CODFILIAL_IMPORTACAO possui essas filiais integrando na Máxima:\
Adicionada Filial 32 CODFILIAL_IMPORTACAO - 2025-04-25 16:10:55,\
CODFILIAL_IMPORTACAO: (1,2,3,7,8,9,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34)\
\
4° Agora vamos realizar a soma no banco local Winthor, utilizando o mesmo SQL utilizado no Gestão e comparando a soma das CAPAS e a soma dos históricos dos itens:\
\
Histórico de CAPAS:\
Resultado -> R$4938352.52\
SQL:\
SELECT\
SUM(NVL(VENDAS.VLATEND, 0)) AS VALORTOTAL\
FROM\
PCPEDC VENDAS\
INNER JOIN PCUSUARI US ON\
VENDAS.CODUSUR = US.CODUSUR\
WHERE\
VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)\
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'\
AND TRUNC(VENDAS.DATA) BETWEEN TO_DATE('01/06/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss') AND TO_DATE('17/06/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')\
AND VENDAS.POSICAO <> 'C'\
AND VENDAS.CODFILIAL IN(1, 2, 3, 7, 8, 9, 14, 16, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34);\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
Histórico de Itens:\
Resultado -> R$4956453.28\
SQL:\
SELECT\
SUM(NVL(DECODE(VENDAS.CONDVENDA, 6, 0, 11, 0, 12, 0, ROUND((ITEMPED.QT * ITEMPED.PVENDA), 2) - 0 - 0), 0)) - 0 AS VALORTOTAL,\
SUM(DECODE(VENDAS.CONDVENDA, 6, 0, 1)) AS QTDITENS\
FROM\
PCPEDC VENDAS\
INNER JOIN PCPEDI ITEMPED ON\
VENDAS.NUMPED = ITEMPED.NUMPED\
INNER JOIN PCUSUARI US ON\
VENDAS.CODUSUR = US.CODUSUR\
WHERE\
VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)\
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'\
AND TRUNC(VENDAS.DATA) BETWEEN TO_DATE('01/06/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss') AND TO_DATE('17/06/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')\
AND VENDAS.POSICAO <> 'C'\
AND NVL(ITEMPED.POSICAO, 'L') <> 'C'\
AND VENDAS.CODFILIAL IN(1, 2, 3, 7, 8, 9, 14, 16, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34)\
\
Conclusão:\
\
Dentro do banco do Winthor do cliente, existe uma divergência entre as tabelas PCPEDC e PCPEDI no que se refere à soma dos históricos das vendas. As querys apresentadas podem ser passadas para o DBA, ou TI responsável realizarem a compreensão da situação. Como existe uma divergência nas próprias tabelas locais, ao realizar a comparação com o maxGestão, os dados não serão compatíveis.\
\
Para os dados serem compatíveis entre Rotina 146 e maxGestão, conforme explicamos anteriormente deve existir também uma compatibilidade entre as somas das tabelas PCPEDC e PCPEDI, caso contrário o resultado será este, o cliente terá uma visão das vendas da Rotina 146 e terá outra visão no maxGestão e isso não necessariamente é algo ruim, simplesmente os sistemas apuram essas informações de formas distintas.\
\
Friso também que qualquer alteração no comportamento das apurações nos sistemas da Máxima, no que se refere a regra de negócios, deverá ser tratado como melhoria.\
\
Observação: Se executado esses scripts no banco nuvem:\
\
Por exemplo o SQL:\
SELECT\
COUNT(VENDAS.NUMPED),\
SUM(NVL(DECODE(VENDAS.CONDVENDA, 6, 0, 11, 0, 12, 0, ROUND((ITEMPED.QT * ITEMPED.PVENDA), 2) - 0 - 0), 0)) - 0 AS VALORTOTAL,\
SUM(DECODE(VENDAS.CONDVENDA,6,0,1)) AS QTDITENS\
FROM MXSHISTORICOPEDC VENDAS\
INNER JOIN MXSHISTORICOPEDI ITEMPED ON VENDAS.NUMPED = ITEMPED.NUMPED\
INNER JOIN MXSUSUARI US ON VENDAS.CODUSUR = US.CODUSUR\
LEFT JOIN (\
SELECT DISTINCT NUMPEDERP, CODSUPERVISOR, CODUSUR\
FROM MXSINTEGRACAOPEDIDO\
WHERE CODSUPERVISOR IS NOT NULL\
AND TRUNC(DATA) BETWEEN TO_DATE('01/06/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss') AND TO_DATE('17/06/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')\
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '74005' AND CODDADOS = '5' AND MXSINTEGRACAOPEDIDO.CODSUPERVISOR = KEYDADOS)\
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '74005' AND CODDADOS = '6' AND MXSINTEGRACAOPEDIDO.CODFILIAL = KEYDADOS)\
AND CODSUPERVISOR IS NOT NULL\
) MXSI ON MXSI.NUMPEDERP = VENDAS.NUMPED AND MXSI.CODUSUR = VENDAS.CODUSUR\
WHERE VENDAS.CONDVENDA NOT IN (4, 8, 10, 13, 20, 98, 99)\
AND NVL(TO_CHAR(VENDAS.DTCANCEL, 'DD-MM-YYYY'), '00-00-0000') = '00-00-0000'\
AND TRUNC(VENDAS.DATA) BETWEEN TO_DATE('01/06/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss') AND TO_DATE('20/06/2025 00:00:00', 'dd/mm/yyyy hh24:mi:ss')\
AND EXISTS (SELECT 1 FROM MXACESSODADOS WHERE CODUSUARIO = '74005' AND CODDADOS = '6' AND KEYDADOS = VENDAS.CODFILIAL)\
AND EXISTS(SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '74005' AND KEYDADOS = VENDAS.CODSUPERVISOR\
UNION ALL\
SELECT KEYDADOS FROM MXACESSODADOS WHERE CODDADOS = '5' AND CODUSUARIO = '74005' AND KEYDADOS = MXSI.CODSUPERVISOR AND VENDAS.CODSUPERVISOR IS NULL)\
AND VENDAS.CODOPERACAO <> 2\
AND ITEMPED.CODOPERACAO <> 2\
AND VENDAS.POSICAO <> 'C'\
AND NVL(ITEMPED.POSICAO, 'L') <> 'C';\
\
Vai retornar sempre 1 pedido a menos, porque lá na Rotina 146 eles filtraram a Filial 33 e a PCMXSCONFIGURACOES não está configurada para integrar a CODFILIAL_IMPORTACAO 33.\
Teria que entender com eles se eles querem integrar essa filial com a Máxima também e realizar o processo de carga de filial nova.

# REGRA DE NEGÓCIO:

# De modo geral é difícil encontrar um caso onde os dados do maxGestão por data de emissão de pedidos batem com a Rotina 146 devido a vários fatores como divergência no banco de dados local, origem de pedidos distintas, dados não integrados na nuvem. Um dos motivos primordiais é que o maxGestão apura somando os históricos dos itens enquanto o Winthor apura somando os históricos das capas dos pedidos.

---

## DOC-MXGESNDV-18555.docx

Avaliar KMs rodados na roteirização dos vendedores TICKET: MXGESNDV-18555

> **CAUSA:**
>
> O resultado de Km Trabalhado e Total estão elevados devido a configuração atual que está sendo utilizada no maxGestão e o dado sobre km que são gerados pelo maxPedido.

# ANÁLISE:

> Análise maxGestão:
>
> O resultado de Km Trabalhado e Total estão elevados devido a configuração atual que está sendo utilizada no maxGestão e o dado sobre km que são gerados pelo maxPedido.
>
> Configurações do Sistema
>
> >> Configurações Gerais
>
> opção >> Utilizar ponto inicial/ponto final do Roteirizador.
>
> >> Painel de Auditoria
>
> opção >> Considerar LATITUDE/LONGITUDE do Roteirizador
>
> Vamos explicar melhor abaixo o que ocorre:
>
> Quando o a opção de "Utilizar ponto inicial/ponto final do Roteirizador" está marcada, então é feito um recálculo do Km Trabalhado que considera a soma do Km previsto para o dia no roteirizador + o Km Trabalhado de fato pelo RCA, (Km que foi apurado pelo maxPedido).
>
> Possíveis soluções:
>
> Nós entendemos que o cliente quer ver os Km trabalhados e totais dos RCAs então nós recomendamos a desativação de ambas configurações:
>
> Configurações do Sistema
>
> >> Configurações Gerais
>
> opção >> Utilizar ponto inicial/ponto final do Roteirizador.
>
> >> Painel de Auditoria
>
> opção >> Considerar LATITUDE/LONGITUDE do Roteirizador
>
> ----------------------------------------------------------------
>
> Validação realizada:
>
> Link utilizado da API de rastros: https://maxrastro-prod.solucoesmaxima.com.br/swagger/index.html
>
> Utilizei para analisar como exemplo o RCA 115571 - Tiago Ribeiro
>
> Código Cliente Máxima:
>
> Data inicio: 01/06/2025
>
> Data final: 17/06/2025
>
> Do dia 2025-06-02 14:14:55.000 até 2025-06-10 06:20:49.000
>
> Por exemplo, ele ainda estava usando a versão 3.261.2 --Isso pode explicar porque alguns rastros estão com problemas, mas seria necessário analisar dia por dia para entender se há algum rastro gerado com inconsistência.
>
> No maxGestão estamos apenas mostrando o rastro que veio do endpoint /api​/v1.1​/distancia​/rastro​/cache
>
> Então quando os parâmetros citados forem desativados, no Mês observamos que o RCA segundo dados do maxPedido andou cerca de 700km, se esses dados são considerados ainda assim, inconsistentes pelo cliente, então é necessária uma verificação dos rastros capturados pelo maxPedido e armazenados nas bases maxTracking.
>
> [
>
> {
>
> "codigoProdutoMaxima": "1",
>
> "codigoClienteMaxima": "2951",
>
> "codigoUsuario": "115571",
>
> "codigoUsur": "19",
>
> "codigoSupervisor": "2",
>
> "dataHoraCaptura": "2025-06-01T11:01:36Z",
>
> "distancias": [
>
> {
>
> "tipo": "RASTRO",
>
> "valor": 722030.2435100001,
>
> "totalAcuracia": 284061
>
> },
>
> {
>
> "tipo": "TRABALHADO",
>
> "valor": 766062.0199709601,
>
> "totalAcuracia": 196726
>
> }
>
> ]
>
> }
>
> ]

# REGRA DE NEGÓCIO:

> O maxGestão apenas consulta o valor na API de rastros e apresenta na tela do Painel de Auditoria.

---

## Doc-MXGESNDV-18945.docx

Pedidos bloqueados não gera ícone no painel de auditoria

Ticket: MXGESNDV-18945

![Group 1, Objeto agrupado](/media/image.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

> **CAUSA:**
>
> Pedidos bloqueados não eram considerados de forma independente da MXSHISTORICOPEDC e também não eram atualizados corretamente quando transmitidos.

![Group 8, Objeto agrupado](/media/image2.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

# **ANÁLISE:**

> Pedidos bloqueados não eram considerados de forma independente da MXSHISTORICOPEDC e também não eram atualizados corretamente quando transmitidos.

![Group 15, Objeto agrupado](/media/image3.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

# **REGRA DE NEGÓCIO:**

> Antes o painel de auditoria buscava o pedido bloqueado na tabela de histórico de pedidos e esse era um comportamento incorreto.\
> \
> Agora o painel busca pedidos bloqueados que estiverem compatíveis entre o rastro PEDIDOBLOQUEADO e o pedido na MXSINTEGRACAOPEDIDO com status igual a 6.\
> \
> Com a alteração surgiu uma situação onde calculava o valor de venda em andamento em pedidos com qualquer status. Foi alterado para calcular venda em andamento somente em pedidos bloqueados com status 6 na integração de pedidos.\
> \
> Antes pedidos bloqueados e pedidos com a mesma numeração em eventos avulsos não eram atualizados corretamente, porque o pedido bloqueado continuava sendo exibido mesmo tendo um pedido já positivado no histórico de pedidos.\
> \
> Agora foi ajustado para atualizar o pedido bloqueado devidamente no painel de auditoria caso ele tenha um pedido correspondente no histórico de pedidos. Com isso, se um pedido bloqueado já foi processado e possui um rastro de um "pedido" compatível, então ele deixará de ser exibido como bloqueado e passará a ser exibido como pedido positivado.\
> \
> Se o pedido for cancelado com status 7 ou posição C deixará de ser exibido com a legenda. Se o pedido estiver com status 0 ou 1 que significa que ainda está em processamento, então não será exibido.

---

## Doc-MXGESNDV-18947.docx

Positivação apresentada indevidamente

Ticket: MXGESNDV-18947

> **CAUSA:**
>
> No detalhamento de atendimentos havia um pedido avulso com rastro em dois dias distintos e nós mostrávamos a data do evento mais antigo

# ANÁLISE:

# Foi ajustada a ordenação dos eventos avulsos para seguir a ordem do mais recente, então se existir um rastro mais antigo ele será desconsiderado e mostraremos o mais recente, assim ficando condizente com a informação de positivados por data. Foram ajustadas as consultas que buscam os dados consolidados para agrupar a positivação por data conforme regra já vigente no Painel original

# **REGRA DE NEGÓCIO:**

# O comportamento do painel de auditoria original é que as positivações são agrupadas por data. Isso significa que, se duas positivações no mesmo cliente foram feitas no mesmo dia, somente 1 será contabilizada. E se duas positivações forem feitas no mesmo cliente em dois dias ou mais distintos, então serão contabilizadas as positivações correspondentes ao número de dias pesquisados, nesse caso 2 positivações.

# O comportamento do Painel Original foi mantido e agora aplicado também ao Painel Consolidado.

# Antes nós motrávamos os eventos avulsos ordenados pela data do evento mais recente, o que causava o problema com a data do pedido. Agora nós mostraremos a data do evento mais recente, assim ficando condizente com o número de positivados que é agrupado por data.

---

## Doc-MXGESNDV-18616.docx

**Falha em geração de relatorio 800 em um determinado tipo TICKET:** MXGESNDV-18616

> **CAUSA:**

# O problema com a geração do Relatório 8091 está relacionado ao gerador que a Máxima utiliza para executar os SQLs no banco de dados Oracle. Esse gerador é em Delphi e no momento não é viável realizar uma correção nesse gerador.

# Em específico quando o bind das datas e o tipo 'T' eram selecionados, ocorria o erro

# Log erro de execução da consulta no Oracle: "ORA-01843: not a valid month", o relatório quebrava e não era gerado.

# ANÁLISE:

# Para resolver essa situação foi necessária uma alteração no SQL local do relatório 8091. A alteração a princípio não causa impactos nos resultados porque foram sugeridas somente alterações na formatação dos parâmetros de datas dentro da query. Também validamos que está gerando agora com sucesso no Winthor e no maxGestão ambos os filtros por tipo F e tipo T. Sugestão para ajuste da query do relatório 8091: Adicionar nos parâmetros de data TO_DATE(:DTI, 'DD/MM/YYYY'), remover o CAST da data e remover o EXTRACT no final do relatório: Ficaria assim: AND PCPEDC.DATA BETWEEN TO_DATE(:DTI, 'DD/MM/YYYY') AND TO_DATE(:DTF, 'DD/MM/YYYY') ... AND PCMOV.DTMOV BETWEEN TO_DATE(:DTI, 'DD/MM/YYYY') AND TO_DATE(:DTF, 'DD/MM/YYYY') ... AND PCNFSAID.DTSAIDA BETWEEN TO_DATE(:DTI, 'DD/MM/YYYY') AND TO_DATE(:DTF, 'DD/MM/YYYY') ... AND PCNFENT.DTENT BETWEEN TO_DATE(:DTI, 'DD/MM/YYYY') AND TO_DATE(:DTF, 'DD/MM/YYYY') ... SELECT :TIPO TIPO, FILIAL FILIAL, TO_DATE(:DTI, 'DD/MM/YYYY') DTINCIAL, TO_DATE(:DTF, 'DD/MM/YYYY') DTFINAL, EXTRACT(MONTH FROM TO_DATE(:DTI, 'DDMMYYYY')) MES, EXTRACT(YEAR FROM TO_DATE(:DTI, 'DDMMYYYY')) ANO, APURACAO.CODSUPERVISOR, APURACAO.SUPERV, APURACAO.CODFORNEC, APURACAO.FORNECEDOR, SUM(QTVENDA) QTDVENDA, SUM(VLVENDA) VLVENDA, SUM(VLDEVOLUCAO) VLDEVOLUCAO, SUM(TOTPESO) PESO, SUM(QTCLIPOS) COBERTURA, SUM(VOLUME) VOLUME, SUM(MIXVENDA) MIXVENDA FROM ( -- ... seus selects ... ) APURACAO GROUP BY :TIPO, APURACAO.CODSUPERVISOR, APURACAO.SUPERV, APURACAO.CODFORNEC, APURACAO.FORNECEDOR, --:DTI, --:DTF, FILIAL, --EXTRACT(MONTH FROM TO_DATE(:DTI, 'DDMMYYYY')), --EXTRACT(YEAR FROM TO_DATE(:DTI, 'DDMMYYYY')) ORDER BY APURACAO.CODSUPERVISOR, VLVENDA DESC

# Em alguns casos se faz necessário evitar funções do Oracle por causa da compatibilidade com o programa do Gerador que utilizamos.

# Foi necessário também ajustar o sql do relatório diretamente no SFTP da GD7 porque ao salvar no Winthor, não estava tendo comunicação com o SFTP internamente deles.

# REGRA DE NEGÓCIO:

# Deve ser gerado o relatório da 800 através do maxGestão utilizando o Gerador, porém em alguns casos alterações no gerador são inviáveis tecnicamente e pode ser necessário ter de realizar alterações nas querys.

---

## Doc-MXGESNDV-18721.docx

Lentidão e timeout em extração de relatorio 800 (TCLOUD GD7)

Ticket: MXGESNDV-18721

> **CAUSA:**
>
> O cliente migrou o gerador800 para ambiente local mesmo sendo tcloud; Para esse fluxo funcionar é necessário ajustar a validação que a API realiza para clientes tcloud.

# ANÁLISE:

# Foi alterada a configuração do relatórios 800 para um ambiente local do cliente mesmo ele sendo T-Cloud porque o processo de realizar a comunicação com o SFTP e o banco T-Cloud da TOTVs para geração dos relatórios é muito lento. Isso ocasiona problemas de geração nos relatórios e também uma demora maior no processo de gerar.

# **REGRA DE NEGÓCIO:**

# Criado o parâmetro TCLOUD_GERADOR800_LOCAL, se estiver 'S' a comunicação não será feita via SFTP, será utilizado o fluxo padrão para buscar os dados em ambiente local. Se estiver 'N' a comunicação será realizada via SFTP e utilizando o ambiente cloud da TOTVs, sendo necessário realizar a configuração no appsettings. Para utilizar o parâmetro é necessário também solicitar ao dev maxGestão ou maxPedido o arquivo que contém a alteração mais recente no gerador-800. Além disso é necessário criar o parâmetro no banco do Winthor na tabela PCMXSCONFIGURACOES.

---

## DOC-MXGESNDV-18778.docx

**Filtro Equipe - Vendas por cliente vs Nível de Produto\
TICKET:** MXGESNDV-18778

------------------------------------------------------------------------

**CAUSA:**\
A página estava utilizando o método obtenha-supervisores-auditoria, que retorna supervisores baseados num filtro de filial, porém, a tela não tem um filtro de filial.

------------------------------------------------------------------------

**ANÁLISE:**\
Foi alterado para o método ObtenhaSupervisores, que retorna default todos supervisores, sem esperar o filtro de filial;

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
N/A

---

## Doc-MXGESNDV-18807.docx

Horário negativo - Painel de Auditoria visão RCA

Ticket: MXGESNDV-18807

> **CAUSA:**
>
> Identificado que o problema ocorre quando os objetos possuem múltiplos checkins, checkouts e pedidos com mesmo código de vinculação, nesse contexto, anteriormente passava numa função local que tratava o conceito de "multiplos eventos" e no processo de entrar nessa função, adicionava um pedido que não foi encontrado na nuvem e com isso, ficava com a HoraFim zerada.

# ANÁLISE:

> A nova correção resolve esse problema porque o conceito de "multiplos eventos" foi reescrito. Agora todos os eventos múltiplos são separados em grupos de 3 e existe uma proteção maior para evitar que a horaInicio e horaFim fiquem zerados.
>
> Antes o método realizava a ordenação somente pela hora do evento então poderia acontecer de dois Checkins serem processados e depois um pedido, com isso, a função múltiplos eventos inseria um registro com a horaFim faltando o que causava a hora de atendimento negativa apresentada.

# **REGRA DE NEGÓCIO:**

> Obs: A regra de negócios foi mudada para trazer justificativas com Checkin realizado no dia anterior. Isso permite que a gente traga a informação na lista de clientes atendidos e com ela presente, conseguimos mostrar a ordem prevista que estava faltando.
>
> Também corrigimos para mostrar a hora final da visita caso a hora inicial esteja zerada, como nesse caso, o Checkin foi feito no dia anterior, então a data inicial fica zerada. Então ao utilizar a data final da visita, a gente mantém a correta ordenação dos horários dos atendimentos em relação a ordem realizada da visita.
>
> Obs2: Se a hora inicial da visita e final estiverem zeradas devido a alguma inconsistência do rastro gerado, então a informação será apresentada porém com a ordem realizada em branco. Isso foi mantido propositalmente para a gente enteder os casos onde o maxPedido gera o rastro de forma muito inconsistente.
>
> Obs3: Agora a hora que é utilizada para definir a sequência realizada é a mesma hora apresentada cliente por cliente no detalhamento dos atendimentos. Assim corrige o problema onde clientes atendidos ficam com a hora divergente da sequência realizada.
>
> Obs4: Agora a gente exibe e trata cada atendimento separadamente, mesmo que o maxpedido gere, por exemplo, 3 checkins e 3 checkouts com a mesma hora de inicio e fim, a gente exibe os 3 de forma separada. O que diferencia um do outro é a ação tomada pelo RCA, então se teve pedido ou justificativa será exibido também.

---

## DOC-MXGESNDV-18827.docx

**Falha ao transferir valor\
TICKET:** MXGESNDV-18827

------------------------------------------------------------------------

**CAUSA:**\
Foi verificado que a checagem do usuário Geral ao obter a conta corrente estava levando em consideração o CODUSUARIO da pesquisa, que nesse caso estava com o CODUSUR nulo na tabela MXSUSUARIOS;.

------------------------------------------------------------------------

**ANÁLISE:**\
Foi ajustado o SQL para checar existe o CODUSUR existe na tabela como um todo e não só do CODUSUARIO, assim, o fluxo fica correto e segue a checagem de permissão

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
N/A

---

## Doc-MXGESNDV-18860.docx

Erro ao tentar carregar todos os clientes

Ticket: MXGESNDV-18860

![Group 1, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

> **CAUSA:**
>
> O limite para passar códigos de clientes através do método GET era ultrapassado e a requisição não batia na API. O filtro de clientes não considerava os Supervisores e RCAs selecionados.

![Group 8, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

# **ANÁLISE:**

> Fix: Foi corrigido um bug na conversão de string para inteiro causado por caracteres especiais na frente dos "dois pontos" -> "The input string '...(131)' was not in a correct format."
>
> Fix: Foi corrigido um bug na conversão de string para inteiro causado por uma vírgula na frente dos "dois pontos" -> "The input string ',42' was not in a correct format."
>
> Fix: Foi corrigido a validação do filtro "Tipo" que é obrigatório, mas quando estava vazio não mostrava mensagem ao usuário forçando o preenchimento do filtro
>
> Fix: Foi corrigido o problema com a passagem dos dados para o backend, onde o GET com URL não suportava o número de clientes no filtro.
>
> Fix: Foi ajustado para o filtro de clientes ficar disponível somente quando o de equipes for selecionado.
>
> Fix: Foi corrigido o carregamento da página, anteriormente todos os filtros carregavam, realizando consultas desnecessárias no banco de dados para trazer todos os dados nos filtros. Sendo que a de Obter Clientes carregava duas vezes devido o carregamento do filtro de supervisores e de RCAs.
>
> Feat: Foi melhorado o carregamento da página, agora a aba abre mais rápido porque os filtros carregam conforme a necessidade.
>
> Feat: Foi desenvolvido um endpoint só para carregar os dados vazios ao iniciar os filtros.
>
> Feat: Foi criado o endpoint POST para suportar a quantidade de dados selecionados nos filtros, principalmente de clientes que possui muitos dados.
>
> Feat: Foi ajustado no backend para quebrar de 1000 em 1000 os dados recebidos do filtro de clientes para que seja possível consultar no banco Oracle e retornar tudo para o frontend.
>
> Feat: Foram alteradas as consultas dos filtros usando REGEX e também a consulta do relatório principal para ficar mais performático no banco de dados, principalmente considerando que agora várias consultas são executadas quando o filtro de clientes é muito grande.
>
> Feat: A consulta de clientes foi adaptada para buscar os dados conforme os filtros de Supervisores e/ou RCAs selecionados.

![Group 15, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

# **REGRA DE NEGÓCIO:**

> Agora o filtro de clientes só é habilitado quando pelo menos 1 supervisor é selecionado. O filtro de clientes foi adaptado para buscar os dados conforme os filtros de Supervisores e/ou RCAs selecionados.

---

## Doc-MXGESNDV-18913.docx

> **Painel de Auditoria sem Informações**

MXGESNDV-18913

> **CAUSA:**
>
> Ao consultar períodos maiores informações eram descartadas por não serem da mesma data da visita planejada.

# ANÁLISE:

> Existia um filtro que descartava informações caso a data do rastro do evento não fosse a mesma da data de visita planejada para o cliente

# **REGRA DE NEGÓCIO:**

> Antigamente o código comparava as datas do rastro com a da visita planejada para o cliente do RCA, então quando filtrava por exemplo dia 24 e 25, registros eram descartados porque a visita era do dia 24 e os pedidos do dia 25.\
> \
> Agora, ajustamos para considerar todos os rastros e selecionar específicos não repetidos por data, codcli e tipo do evento. Não mais usando como critério a questão de o evento ter sido realizado no mesmo dia da agenda do cliente.

---

## Doc-MXGESNDV-18915.docx

Painel de Auditoria sem Informações

Ticket: MXGESNDV-18915

> **CAUSA:**
>
> O maxGestão padrão atualmente traz dados referentes aos atendimentos registrados através de rastros gerados do maxPedido dos últimos 45 dias.

# ANÁLISE:

# Depois dos 45 dias, não é possível mais recuperar os rastros anteriores devido ao volume de informações e o custo que isso pode ter em banco de dados não relacional em nuvem. Por esse motivo, os períodos citados não trazem mais dados e será possível verificar somente atendimentos realizados a partir dos últimos dois meses, dependendo do dia. 

# **REGRA DE NEGÓCIO:**

> O maxGestão padrão atualmente traz dados referentes aos atendimentos registrados através de rastros gerados do maxPedido dos últimos 45 dias. Para alterar esse comportamento seria necessário solicitar um ticket de Melhoria.

---

## Doc-MXGESNDV-19160.docx

\[INTERNO\] Melhorar o README do Portal Executivo Cloud

TICKET: MXGESNDV-19160

> **CAUSA:**
>
> O Portal executivo cloud não possuía um Readme explicando o projeto e como executar localmente

# ANÁLISE:

> O README será feito direto pelo gitlab com o editor e visuazação do gitlab e os arquivos foram ajustados com as respectivas versões 4.5.1 e 12.0, o nome foi corrigido para Criptografia45

# REGRAS DE NEGÓCIO:

\# 🚀 Portal Executivo

Sistema web para consulta de Relatórios, desenvolvido em ASP.NET WebForms, com integração Oracle e frontend dinâmico em Ajax.

Este projeto é mantido pela Maximatech e centraliza funcionalidades de consulta de dados, emissão de relatórios e menus dinâmicos.

---

## 📦 Clonando o Projeto

git clone --single-branch --branch feature/GestaoNuvem https://gitlab.maximatech.com.br/gestor/portalexecutivo.git

---

## 🛠️ Configuração Inicial

1. **\*\*Abra o Visual Studio 2022\*\***
   - Selecione a solução `PortalExecutivo.sln`.

2. **\*\*Configuração do Oracle Client\*\***
   - Edite o arquivo `web.config` do Portal Executivo:
   ```xml
   <add key="OraclePath" value="Caminho onde você instalou o Client Oracle" />
   ```
   - Exemplo: `C:\oracle\product\12.2.0\client_1`

3. **\*\*Configuração dos Pacotes NuGet\*\***
   - Certifique-se de que o Visual Studio está apontando para as fontes corretas:
     - `nuget.org`
     - `https://nexus.maximatech.com.br/repository/nuget-hosted/`
   - No Visual Studio, acesse:
     **__Tools > NuGet Package Manager > Package Sources__**

4. **\*\*Baixar e Instalar .NET 4.5.1 \*\***
   - https://dotnet.microsoft.com/pt-br/download/dotnet-framework/net451

5. **\*\*Restaurar, Limpar e Buildar\*\***
   - Execute:
     - **__Build > Clean Solution__**
     - **__Build > Rebuild Solution__**

---

## ⚙️ Executando o Projeto

1. **\*\*Inicie o Portal Executivo\*\***
   - Execute o projeto no IIS Express ou IIS local.

2. **\*\*Acesso com Credencial de Cliente\*\***
   - Para autenticar como cliente, obtenha o token de produção.
   - Acesse:
   ```
   http://localhost:4952/PortalExecutivo/?PWE=<TOKEN_DO_CLIENTE>
   ```
   - Substitua `<TOKEN_DO_CLIENTE>` pelo token real.

---

## 🧩 Principais Funcionalidades

- **\*\*🔒 Autenticação e Controle de Sessão\*\***
- **\*\*📋 Menus Dinâmicos por Permissão\*\***
- **\*\*🏢 Informações de Empresa e Usuário\*\***
- **\*\*🔎 Pesquisa Global com Ajax\*\***
- **\*\*⚠️ Redirecionamento Inteligente para Erros\*\***
- **\*\*🗂️ Integração Oracle para dados e permissões\*\***
- **\*\*📈 Exibição de Versão do Sistema\*\***

---

## 🖥️ Frontend

- **\*\*Ajax Dinâmico\*\*** para pesquisa e navegação.
- **\*\*Layout responsivo\*\*** via MasterPage.
- **\*\*Recursos multilíngue\*\*** via arquivos de recursos globais.

---

## 📝 Observações

- O projeto depende do Oracle Client instalado localmente.
- O token de cliente é obtido via ambiente de produção.
- Para dúvidas sobre permissões, consulte o administrador do sistema.

---

## 📚 Referências

- [Documentação Oficial ASP.NET](https://docs.microsoft.com/pt-br/aspnet/web-forms/)
- [NuGet](https://www.nuget.org/)
- [Maximatech Nexus](https://nexus.maximatech.com.br/)

---

## 🏷️ Licença

Este projeto é privado e de uso exclusivo da Maximatech.

---

## Doc-MXGESNDV-19161.docx

Oscilação na busca do relatorio em painel de auditoria

TICKET: MXGESNDV-19161

> **CAUSA:**
>
> Em situações de rastros com mesmo código de vinculação e múltiplos eventos de PEDIDO ou JUSTIFICATIVA a aplicação quebrava por não conseguir agrupar os eventos

# ANÁLISE:

# Foi realizada tratativa para em caso de múltiplos eventos com 1 grupo, pegar o CHECKIN e CHECKOUT e replicar para todos os eventos PEDIDO ou JUSTIFICATIVA assim tornando possível montar o objeto corretamente. Foi adicionado um log na AWS para o método ObtenhaDistanciaClientePorRastroCache. Foi feita tratativa com try-catch para não quebrar o fluxo de montagem dos objetos dos clientes. Em termos menos técnicos: O RCA através do maxPedido pode fazer 1 checkin 2 justificativas e 1 checkout. E nesse cenário, o Painel de Auditoria não estava programado para lidar com o cenário e montar corretamente as visitas considerando o início do Checkin e fim do Checkout separando por ação feita.

# REGRAS DE NEGÓCIO:

Antes o Painel de Auditoria mostrava os múltiplos eventos considerando só a hora de início e final (PEDIDO, JUSTIFICATIVA).

Depois foi refatorado para agrupar sempre de 3 em 3 eventos quando tivesse código de vinculação compatível com CHECKIN e CHECKOUT e nessa alteração, foi excluído o conceito de "múltiplos eventos". Mesmo tentando agrupar de 3 em 3, ele consegue agrupar de 2 em 2 para casos de eventos faltando por terem sido feitos em outro dia e o fluxo segue normalmente.

Agora foi readaptado o conceito de múltiplos eventos para eles serem exibidos no Painel de Auditoria considerando a hora de início do Checkin e final do Checkout. Então por exemplo, se o usuário realizar 1 Checkin, 1 pedido, 2 justificativas e 1 checkout; o sistema irá agrupar 3 vezes esses eventos para mostrar na tela de forma separada e os horários de inicio e fim de atendimento irão se repetir, pois esses eventos foram feitos dentro da mesma margem de tempo.

---

## DOC-MXGESNDV-18982.docx

**VENDA PREVISTA NÃO APARECE\
TICKET:** MXGESNDV-18982

------------------------------------------------------------------------

**CAUSA:**\
No SQL responsável por retornar os registros de venda prevista estava considerando um NVL como prioridade na tabela ERP_MXSMETA, acontece que o supervisor 125 não estava nulo na tabela, apenas com valor 0, com isso, ele retornava zerado e não era consultado na tabela ERP_MXSMETARCA, onde estão os registros;

------------------------------------------------------------------------

**ANÁLISE:**\
Foi alterado a ordem, será repassado primeiro no NVL (função para tratar nulo do oracle) a tabela ERP_MXSMETARCA, se estiver nulo, irá buscar da ERP_MXSMETA;

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
N/A

---

## DOC-MXGESNDV-19022.docx

**Problemas painel de auditoria\
TICKET:** MXGESNDV-19022

------------------------------------------------------------------------

**CAUSA:**\
Existe um fluxo onde o usuário é alterado para troca de CODUSUR, troca de informações que inserem a DTDESBLOQUEIO nula. Com a melhoria para desconsiderar o status, alguns desses registros estavam retornando como férias, já que apenas as datas são validas;

------------------------------------------------------------------------

**ANÁLISE:**\
Foi alterado a ordem, será repassado primeiro no NVL (função para tratar nulo do oracle) a tabela ERP_MXSMETARCA, se estiver nulo, irá buscar da ERP_MXSMETA;

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
N/A

---

## Doc-MXGESNDV-19036.docx

Supervisor conseguindo liberar pedido abaixo de margem permitida

Ticket: MXGESNDV-19036

![Group 1, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

> **CAUSA:**
>
> Ocorria um arredondamento no cálculo da margem de lucratividade do pedido diminuindo a precisão do cálculo
>
> ![Group 8, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

# **ANÁLISE:**

> Ocorria um arredondamento no cálculo da margem de lucratividade do pedido diminuindo a precisão do cálculo

![Group 15, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

# **REGRA DE NEGÓCIO:**

> A margem de lucratividade do pedido deve ser compatível com a do maxPedido.

A margem está sendo calculada pela API, foi realizado um pequeno ajuste no arredondamento. Porém se o maxPedido criar formas diferentes de calcular essa margem de lucratividade, pode ser necessário pegar a margem que eles já calculam e gravam na MXSINTEGRACAOPEDIDO ao invés de calcular na API.

---

## DOC-MXGESNDV-19066.docx

**VISITAS PREVISTAS VS REALIZADAS WEB não retorna resultados\
TICKET:** MXGESNDV-19066

------------------------------------------------------------------------

**CAUSA:**\
O problema ocorre devido repassar apenas as datas como filtro, pelo fato do método usar o painel de auditoria como referência é necessário um codsupervisor para fazer a validação;

------------------------------------------------------------------------

**ANÁLISE:**\
Como o codsupervisor é obrigatório, foi inserido um método auxiliar para buscar o codsupervisor do filtro, quando não existir serão retornados todos os supervisores dos representantes válidos, quando existir somente a filial no filtro, serão repassadas as filiais para a busca dos supervisores.

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
Quando o filtro de supervisores for vazio, será feito o preenchimento dos supervisores conforme é feito por rca.

---

## DOC-MXGESNDV-19068.docx

**Indicadores divergindo do ranking de fornecedores\
TICKET:** MXGESNDV-19068

**CAUSA:**\
Foi identificado que a query que preenche o Ranking de Fornecedores estava sem a condição que restringe os condvendas, conforme já é o comportamento padrão dos outros rankings e indicadores;

------------------------------------------------------------------------

**ANÁLISE:**\
Foi inserida a condição conforme já praticado nos outros cards, agora o ranking irá desconsiderar os condvendas: 4, 8, 10, 13, 20, 98 e 99;

------------------------------------------------------------------------

**REGRA DE NEGÓCIO:**\
N/A

---

## Doc-MXGESNDV-19098.docx

**Erro ao abrir o detalhamento**

TICKET: MXGESNDV-19098

> **CAUSA:**
>
> Não está abrindo o detalhamento retornando uma tela em branco onde o usuário fica preso.

# ANÁLISE:

> O método distanciaClienteRastro que busca os dados na API de rastros sofria uma Exception de timeout com origem externa, assim o processamento do detalhamento era interrompido e retornava vazio para o Front.

# REGRA DE NEGÓCIO:

> Foi inserida uma tratativa no front para não quebrar o layout e permitir o usuário continuar navegando no sistema e foi alterada a API para preservar o fluxo e as informações já processadas. Caso sofra timeout no distanciaClienteRastro somente o KM do detalhamento dos atendimentos por cliente do RCA ficará zerado.

---

## Doc-MXGESNDV-19128.docx

**Metas Categoria max gestão app**

TICKET: MXGESNDV-19128

> **CAUSA:**
>
> Meta de Categoria não é apresentada em VendasPrevistasXRealizadas.

# ANÁLISE:

> As consultas não estavam buscando as metas por categoria e ao remover algum filtro selecionado e buscar os dados novamente ocorria uma exceção.

# REGRA DE NEGÓCIO:

> O acompanhamento de Vendas Previstas x Realizadas mostrará as metas cadastradas na ERP_MXSMETA com o TIPOMETA = 'A'. Para OERPs é necessário realizar a integração ou o cadastro da Meta via Central e para clientes Winthor nós integramos da PCMETA.

---

## Doc-MXGESNDV-19138.docx

**informativo aparecendo indevidamente** Ticket: MXGESNDV-19138

> **CAUSA:**

Se você inicializa a variável diretamente na declaração da classe, pode acontecer do Angular tentar acessar a variável antes do ciclo de vida correto, causando comportamentos inesperados ou valores indefinidos.

# ANÁLISE:

Dentro do ngOnInit, você garante que o valor de localStorage e de EnumModuloGestao já está disponível e inicializado corretamente quando o Angular renderiza o template.

Sempre que precisar de valores do localStorage ou de variáveis que dependem do ambiente já carregado, inicialize no ngOnInit.

Isso garante que o template enxergue o valor correto e as condições do *ngIf funcionem como esperado.

# **REGRA DE NEGÓCIO:**

Caso o cliente seja Starter a opção em Painel Geral e DashBoard de verificar pedidos faturados deve ser desabilitada e a mensagem de recurso pró deve ser apresentada.

---

## Doc-MXGESNDV-19287.docx

ERRO RELATÓRIO - VISITAS PREVISTAS VS REALIZADAS

**zeradas** TICKET: MXGESNDV-19287

> **CAUSA:**
>
> Ocorria uma exceção por transação em aberto durante consulta dos dados via API.

# ANÁLISE:

> Foi identificado que era executada a abertura de transaction e depois não era commitada. Além disso colocar transações nesse ponto do código se tornou uma complicação porque ele executa transações em paralelo de consulta e também de inserção duas vezes.
>
> Como o método de Inserir já utiliza ExecuteNonQuery, então não é necessário declarar começo de transação e nem commitar, pois essa funcionalidade já autocommita nesse caso e se ocorrer uma falha, somente a execução do registro em questão fica com erro.

# REGRA DE NEGÓCIO:

---

## Doc-MXGESNDV-19310.docx

**Erro na venda prevista vs realizada** TICKET: MXGESNDV-19310

> **CAUSA:**
>
> O relatório não era gerado devido a um erro que ocorria no backend especificamente para os filtros que são utilizados nesse relatório.

# ANÁLISE:

> A verificação de filtro nulo e sem itens selecionados estava incompleta causando exceções de lista nula na API. A abordagem usando Any é mais eficiente para validação de listas e também foi adicionado uma verificação de nulo no objeto das deduções para reforçar. Ajustada a verificação de nulo do filtro Deduções utilizando Any em conjunto com IsNullOrWhiteSpace do .NET.

# REGRA DE NEGÓCIO:

---

## Doc-MXGESNDV-19320.docx

**Mapas com KMs zerados** TICKET: MXGESNDV-19320

> **CAUSA:**
>
> Os Kms ficavam zerados porque a api de rastros não suportava a passagem dos códigos dos supervisores com zeros na frente e devido a utilização do método MontarKMsRcaRefatorado que não considerava os parâmetros utilizaValidacaoMesmoRastroParaEventos e habilitaPontoInicialPontoFinal.

# ANÁLISE:

> A consulta na API de rastros foi ajustada para passar na url somente os RCAs como é feito no PainelDeAuditoria e o método de calcular os Kms foi alterado para o MontarKMsRca que considera os parâmetros.

# REGRA DE NEGÓCIO:

# O comportamento da apuração dos Kms em Mapas foi ajustado para ficar compatível com o do Painel de Auditoria, agora os parâmetros do sistema para utilizar coordenadas dos Roteirizador e mesmo rastro para eventos também são validados em Mapas

---

## Doc-MXGESNDV-19370.docx

**Inativação de usuarios** Ticket: MXGESNDV-19370

![Group 1, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

> **CAUSA:**
>
> Atualmente a inativação e ativação de usuários é um conceito ligado às licenças dos nossos sistemas.
>
> ![Group 8, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

# **ANÁLISE:**

![Group 15, Objeto agrupado](media/image1.png){width="5.927083333333333in" height="5.2083333333333336e-2in"}

# **REGRA DE NEGÓCIO:**

Atualmente a inativação e ativação de usuários é um conceito ligado às licenças dos nossos sistemas, o status do usuário Ativo ou Inativo depende de como o procedimento é realizado:

Como inativar o usuário no maxGestão?

1° Se ele estiver inativo e inutilizável é necessário ativar novamente e colocar como utilizável.

2° Liberar qualquer licença para o usuário (no caso vamos usar do maxGestão mesmo).

3° O usuário tendo a licença liberada, você vai inativar o usuário. Se for usuário Administ