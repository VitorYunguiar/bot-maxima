# GATE-183 - Replicador causando lock de banco

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Extrator
- Natureza: Dúvida
- Atualizado em: 2024-10-15T16:02:31.725-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
Ocorrendo locks no banco devido ao replicador.

## Resultado esperado
Não ocorrer locks no banco.

## Descrição
Cliente informou que após alterar o horario de execução do replicador de 18h para 16h ocorreram locks no banco local devido ao replicador.

Imagens em anexo

## Comentarios do Gatekeeper

### 1. 2024-10-15T16:02:31.724-0300 | Filipe do Amaral Padilha

Voltamos a hora para disparo do Replicador para as 18h, porém não sei se só isso iria resolver o lock que está ocorrendo, porque o lock pode ser devido a outro motivo.

O lock para a gente saber o motivo precisa estar ocorrendo na hora, então eu recomendo que o cliente deixe o lock e nos acionar caso ocorra novamente. Se ele identificar o motivo, também é válido para a gente entender o que causa, porque o DBA também pode investigar locks no banco de dados local.

Já sobre os logs que ele mandou a gente fez a correção no banco de dados na coluna CODUSUARIO das tabelas MXSUSUARIOS e MXSCOMPROMISSOS porque teve um aumento desse campo em uma alteração recente na nuvem.

Também foi feita a carga dos dados que não haviam gravado corretamente dos compromissos devido ao erro.

O Replicador não usa o processador.dll que está acusando no lock por isso acredito que as coisas não tenham relação.

## Resposta Canonica

**Análise canônica**

Não foi possível confirmar que o lock no banco local seja causado pelo Replicador. O motivo do lock **não foi identificado**, e a análise aponta que ele **pode estar sendo causado por outro fator**.

Foi validado que:
- o horário de disparo do Replicador foi **revertido para 18h**;
- o **Replicador não utiliza o `processador.dll`** que está sendo apontado no lock;
- houve uma **correção no banco de dados** na coluna **`CODUSUARIO`** das tabelas **`MXSUSUARIOS`** e **`MXSCOMPROMISSOS`**;
- essa correção foi necessária após um **aumento do campo `CODUSUARIO`** em alteração recente na nuvem;
- também foi realizada a **carga dos compromissos** que não haviam sido gravados corretamente em função desse erro.

**Limitações da análise**
- O motivo do lock só pode ser identificado **no momento em que ele estiver ocorrendo**.
- Não há evidência de que apenas retornar o horário do Replicador para **18h** elimine o problema.
- Não há relação confirmada entre o Replicador e o **`processador.dll`** citado no lock.

**Próximo passo recomendado**
Manter o ambiente até que o lock ocorra novamente e **acionar a equipe no momento da ocorrência** para investigação. Em paralelo, o **DBA** pode analisar os locks no banco de dados local. Caso o cliente identifique algum padrão ou causa, deve informar à equipe de suporte.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 400971
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
