# GATE-226 - diveregencia de quantidades de clientes entre banco e aplicaçao

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: ROTVENDN - Carteira de Clientes
- Natureza: N/A
- Atualizado em: 2024-10-24T12:50:13.547-0300

## Contexto do Problema

## Passos para reproduzir
acessar o ambiente do roteirizador do cliente e buscar pelo vendedor MARCONES MENDES DOS SANTOS - CODUSUR 522.
Comparar com os registros que são contados na view de vinculos dos clientes com RCA

## Resultado apresentado
divergência na quantidade de clientes entre banco e sistema

## Resultado esperado
a principio, é esperado que a quantidade seja equivalente entre a consulta realizada e o que o sistema exibe, porém não tenho certeza se há outra regra que restringe as quantidades retornadas por algum motivo.

## Descrição
Senhores, ao analisar o cenário citado estamos observando divergência em quantidade de clientes que não identifiquei qual a regra que está afetando o sistema e gerando essa situação. No roteirizador exibe a quantidade abaixo:

!image-2024-10-24-09-12-35-485.png!

enquanto que na view que trás essa informação, a contagem trás o seguinte valor:

!image-2024-10-24-09-15-55-681.png!

Não identifiquei de onde está sendo observado esse valor de 196 clientes que o sistema trás.

## Comentarios do Gatekeeper

### 1. 2024-10-24T11:52:04.331-0300 | Filipe do Amaral Padilha

O que ocorre é que no Roteirizador tem uma opção na engrenagem em cima na direita de "excluir clientes inativos", então com isso faz uma validação onde remove alguns clientes com DTEXCLUSAO preenchida e bloqueiodefinitivo != 'S' e também sem coordenadas definidas.

Coloquei na imagem Screenshot_1.png

Então para os dados ficarem compatíveis com o número de clientes da carteira e que também é gerado na view (211) ele deve desmarcar essa configuração.

A view é a SELECT COUNT(*) FROM MXSVCLIENTESRCA WHERE CODUSUR IN(522);

Os dados exibidos serão conforme ela.

O SQL que ela faz é:

SELECT "CODUSUR",
"CODCLI",
"DTCADASTRO",
"DTULTCOMP"
FROM (SELECT DISTINCT codusur,
codcli,
dtcadastro,
dtultcomp
FROM (SELECT c.codusur1 codusur,
c.codcli,
c.dtcadastro,
c.dtultcomp
FROM mxsclient c
WHERE NVL(c.codusur1,'0') > '0' AND c.codoperacao != 2
UNION
SELECT c.codusur2 codusur,
c.codcli,
c.dtcadastro,
c.dtultcomp
FROM mxsclient c
WHERE NVL(c.codusur2,'0') > '0' AND c.codoperacao != 2
UNION
SELECT c.codusur3 codusur,
c.codcli,
c.dtcadastro,
c.dtultcomp
FROM mxsclient c
WHERE NVL(c.codusur3,'0') > '0' AND c.codoperacao != 2
UNION
/* CONSULTA PARA ENVIAR OS CONSUMIDORES FINAIS PARA TODOS OS CODUSUR - FILTRAR_CONSUMIDOR_FINAL_GERACAO = N */
SELECT DISTINCT CODUSUR,
C.CODCLI,
C.DTCADASTRO,
C.DTULTCOMP
FROM MXSUSUARIOS M, MXSCLIENT C
WHERE M.STATUS = 'A'
AND M.CODUSUR IS NOT NULL
AND M.CODOPERACAO != 2
AND OBTER_PARAMETRO ('FILTRAR_CONSUMIDOR_FINAL_GERACAO', NULL, 'N') = 'N'
AND C.CODCLI IN ('1', '2', '3')
AND C.CONSUMIDORFINAL = 'S'
UNION
/* CONSULTA PARA ENVIAR OS CONSUMIDORES FINAIS APENAS PARA OS CODUSUR VINCULADOS NA ERP_MXSUSURCLI - FILTRAR_CONSUMIDOR_FINAL_GERACAO = S */
SELECT DISTINCT
E.CODUSUR,
C.CODCLI,
C.DTCADASTRO,
C.DTULTCOMP
FROM MXSCLIENT C
INNER JOIN ERP_MXSUSURCLI E ON E.CODCLI = C.CODCLI AND E.CODOPERACAO != 2
WHERE C.CODOPERACAO != 2
OR (OBTER_PARAMETRO ('FILTRAR_CONSUMIDOR_FINAL_GERACAO', NULL, 'N') = 'S'
AND C.CODCLI IN ('1', '2', '3')
AND C.CONSUMIDORFINAL = 'S'
AND C.CODOPERACAO != 2)))
WHERE codusur = 522

## Resposta Canonica

A divergência é causada pela configuração **"excluir clientes inativos"** no Roteirizador.

Quando essa opção está marcada, o sistema desconsidera clientes que atendem aos seguintes critérios:
- **DTEXCLUSAO preenchida**
- **bloqueiodefinitivo != 'S'**
- **sem coordenadas definidas**

Por isso, a quantidade exibida no sistema pode ficar diferente da contagem retornada pela view. Para o **CODUSUR 522**, o número compatível com a carteira e com a view é **211**.

Consulta utilizada na conferência:

```sql
SELECT COUNT(*) FROM MXSVCLIENTESRCA WHERE CODUSUR IN(522);
```

A exibição dos dados segue a view, mas no Roteirizador a opção citada aplica esse filtro adicional na interface.

**Ação recomendada:** desmarcar a opção **"excluir clientes inativos"** no Roteirizador e validar novamente a quantidade exibida para o **CODUSUR 522**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 402853
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
