# Registros de ferias incorretos - CONTROLE_MXSUSUARIOS

> Documento preparado para ingestao em banco vetorial (RAG).
> Fonte original: `C:\Users\vitor\Downloads\MXPEDDV-102590 - Registros de férias incorretos (CONTROLE_MXSUSUARIOS).pdf`
> Ticket: MXPEDDV-102590
> Data de extracao: 2026-04-29
> Sistema: maxGestao | maxPedido | Central de Configuracoes
> Area: Usuarios | Ferias | Controle de acesso | Normalizacao de dados

---

## Sobre este documento

Este documento descreve o cenario de registros incorretos de ferias na tabela `CONTROLE_MXSUSUARIOS`, gerados por fluxo antigo via trigger, e o impacto disso no maxGestao e maxPedido.

Palavras-chave: ferias, usuario bloqueado, usuario inativo, maxGestao, maxPedido, CONTROLE_MXSUSUARIOS, DATA_DESBLOQUEIO, DATA_PROCESSAMENTO, TK_SYNC_FV_MXSUSUARIOS, Central de Configuracoes, cadastro de ferias, RCA.

---

## Causa

A causa foi a insercao automatica de ferias via trigger `TK_SYNC_FV_MXSUSUARIOS` quando o usuario era inativado ou ativado no portal.

O fluxo antigo criava registros de ferias na tabela `CONTROLE_MXSUSUARIOS` apenas com a data de inicio (`DATA`) quando o usuario era inativado. Quando o usuario era ativado novamente, o registro deveria receber a data fim em `DATA_DESBLOQUEIO`.

Como a trigger foi descontinuada, alguns bancos ficaram com registros antigos sem data fim. O maxGestao interpreta registro sem `DATA_DESBLOQUEIO` como ferias ainda vigentes e deixa de exibir dados do usuario.

---

## Analise

O fluxo na trigger de usuarios `TK_SYNC_FV_MXSUSUARIOS` controlava ativacao e inativacao dos usuarios, permitindo identificar quando o usuario estava de ferias.

Fluxo antigo:

1. Usuario era inativado no portal.
2. A trigger inseria registro em `CONTROLE_MXSUSUARIOS`.
3. O registro era criado somente com a data de inicio (`DATA`).
4. Quando o usuario era ativado novamente, a trigger atualizava a data fim (`DATA_DESBLOQUEIO`).

Problema deixado pela descontinuacao:

1. A funcionalidade passou a ser feita pela Central de Configuracoes.
2. Registros antigos permaneceram sem `DATA_DESBLOQUEIO`.
3. O maxGestao passou a considerar o usuario ainda em ferias.
4. Os dados do usuario deixavam de aparecer.

---

## Script de normalizacao

Use este script para corrigir registros de ferias antigos sem data fim, preenchendo `DATA_DESBLOQUEIO` com `DATA_PROCESSAMENTO`.

Substitua `[#USUARIOMAXIMA#]` pelo schema correto do cliente.

```sql
DECLARE
  VCOUNT NUMBER;
BEGIN
  /*
    CORRECAO PARA O CENARIO EM QUE O REGISTRO DE FERIAS
    (CONTROLE_MXSUSUARIOS) FOI INSERIDO VIA TRIGGER QUE FOI DESCONTINUADA.

    CENARIO:
    - USUARIO ERA INATIVADO NO PORTAL;
    - A TRIGGER INSERIA O REGISTRO DE FERIAS SEM DATA FIM (DATA_DESBLOQUEIO);
    - QUANDO O USUARIO ERA ATIVADO NOVAMENTE, ERA ATUALIZADO O REGISTRO COM A DATA FIM;
    - ESSA FUNCIONALIDADE FOI DESCONTINUADA;
    - AGORA O CONTROLE E REALIZADO VIA CENTRAL DE CONFIGURACOES;
    - FICARAM REGISTROS INCORRETOS EM ALGUNS BANCOS.
  */

  SELECT COUNT(*)
    INTO VCOUNT
    FROM [#USUARIOMAXIMA#].CONTROLE_MXSUSUARIOS
   WHERE DATA_DESBLOQUEIO IS NULL
   ORDER BY DATA_PROCESSAMENTO DESC;

  IF VCOUNT > 0 THEN
    UPDATE [#USUARIOMAXIMA#].CONTROLE_MXSUSUARIOS
       SET DATA_DESBLOQUEIO = DATA_PROCESSAMENTO
     WHERE DATA_DESBLOQUEIO IS NULL;

    COMMIT;
  END IF;

EXCEPTION
  WHEN OTHERS THEN
    NULL;
END;
/
```

Observacao tecnica: o `ORDER BY` em `SELECT COUNT(*)` foi preservado conforme o PDF. Se houver erro no banco do cliente, validar o script com o DBA antes de executar.

---

## Novo fluxo de cadastro de ferias

O fluxo de cadastro de ferias foi migrado para a Central de Configuracoes. O usuario pode cadastrar as ferias manualmente conforme necessario, permitindo controle correto do periodo.

Caminho:

```text
Central de Configuracoes > Cadastros > Ferias
```

Fluxo antigo:

- Ferias eram cadastradas automaticamente pela trigger ao ativar ou inativar o usuario no portal.

Fluxo novo:

- A trigger foi descontinuada.
- O processo agora e realizado pela Central de Configuracoes.

---

## Regra de negocio - maxGestao

O maxGestao:

- Nao exibe dados do usuario caso ele esteja de ferias no periodo.
- Usa a tabela `CONTROLE_MXSUSUARIOS`.
- Se o registro de ferias nao possui data fim (`DATA_DESBLOQUEIO`), considera que o usuario ainda esta de ferias.
- Esse cenario de ferias sem data fim nao deve mais ocorrer a partir do cadastro pela Central.

---

## Regra de negocio - maxPedido

O maxPedido:

- Permite apenas um cadastro de ferias dentro do periodo para um vendedor.
- Possui validacao no maxPedido APK para barrar acesso ao maxPedido caso o RCA esteja de ferias.
- Permite cadastro de ferias retroativo.

---

## Evidencia visual do PDF

Os prints mostram:

- Um bloco de script SQL/PLSQL para normalizacao de `CONTROLE_MXSUSUARIOS`.
- A tela da Central de Configuracoes no menu `Cadastros > Ferias`, listando registros de ferias.

