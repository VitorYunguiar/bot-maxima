# GATE-329 - Produto não aparece

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Adriel Gonçalves Peixoto
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2024-11-13T15:28:44.142-0300

## Contexto do Problema

## Passos para reproduzir
rafalim.057

Acessar aba de produtos, ou em qualquer cliente
Pesquisar o produto 3324

## Resultado apresentado
Foi realizado a verificação no banco de dados nuvem e local e identificado que possui divergência entre as tabelas MXSTABPR, na qual no banco local possui dados para e no banco nuvem não.
O produto aparece na rotina 316 normalmente
Na APK não

## Resultado esperado
Produto aparecer na APK

## Descrição
Alguns produtos não aparecem, cliente deu como exemplo o produto 3324

## Comentarios do Gatekeeper

### 1. 2024-11-13T15:27:58.295-0300 | Filipe do Amaral Padilha

O problema do cliente são os registros da tabela MXSTABPR que estão com divergência da PCTABPR conforme foi inforamdo.

Isso é causado porque a nossa PGK_CARGA_NUVEM está inválida no ambiente do cliente. Então a nossa TRIGGER tenta executar os comandos para integração, porém como a PKG está inválida, não consegue exeuctar o comando para intergar os registros.

Para a PKG deixar de estar inválida, é necessário o cliente executar os grants do arquivo em anexo "SCRIPT_TCLOUD_MAXIMA" com um usuário com privilégios, como o SYSTEM, por exemplo no banco de dados do Winthor dele. Dentro desse arquivo tem a GRANT para o MAXSOLUCOES ta tabela PCTRIBUTEXCECAO onde está sendo reportado o problema. --Essa parte de executar os GRANTs eu já pedi para ele, porém é bom reforçar no retorno do ticket no Jira.

Depois que ele executar os GRANTs solicitados, pode ser necessário ainda a gente conectar e recompilar a nossa PKG.

Porém para evitar que a gente reconecte ele pode também executar a parte, depois de rodar os grants esse comando:

ALTER PACKAGE PKG_CARGA_NUVEM COMPILE BODY; COMMIT;

Feito isso, pode ser validado comparando ambas tabelas:

SELECT * FROM MXSTABPR WHERE CODPROD IN(3324);

SELECT * FROM PCTABPR WHERE CODPROD IN(3324);

Depois de integrado o cliente sincroniza o maxPedido e os produtos devem ser apresentados.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 406781
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Esse cenário explica o produto 3324 aparecer na rotina 316 e não aparecer na APK." | "Na análise, foi confirmado:" | "indício de problema de `GRANT` para o usuário `MAXSOLUCOES` na tabela `PCTRIBUTEXCECAO`."
