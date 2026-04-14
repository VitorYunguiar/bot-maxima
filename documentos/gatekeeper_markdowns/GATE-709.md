# GATE-709 - RCA Gledson consta separado do supervisor 17 no relatório de auditoria

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel de Auditoria - Dados Incorretos
- Natureza: Dúvida
- Atualizado em: 2025-01-29T11:19:11.813-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar maxGestão
>> Ir no painel de auditoria
>> Realizar pesquisa para todos os usuários e supervisores, dias 27/01
>> Ir na opçao de imprimir, verificar relatorio
>> Verificar RCA Gledson, se esta abaixo do supervisor 17

## Resultado apresentado
>> No relatorio mostra RCA Gledson seperado, como se não fosse vinculado ao supervisor 17

## Resultado esperado
>> Que no relatorio mostre que o RCA Gledson esta vinculado ao supervisor 17

## Descrição
Ao analisar o RCA Gledson, identificamos um problema na hierarquia do usuário. Quando selecionamos a opção de imprimir, o sistema mostra que o usuário não está vinculado ao supervisor 17. Em vez disso, ele aparece separado, como se não fizesse parte da equipe desse supervisor.

## Comentarios do Gatekeeper

### 1. 2025-01-29T11:19:11.812-0300 | Filipe do Amaral Padilha

A funcionalidade que gera o relatório agrupado por supervisor, também agrupa por filial, porque o Supervisor é voinculado a filial 2.

O RCA 510 que não aparece agrupado na equipe do Supervisor 17, é exibido dessa forma porque no cadastro do RCA na Rotina 517, ele não está vinculado à mesma filial do Supervisor dele, que é a filial 2.

Para resolver, caso eles desejem que o RCA seja agrupado no relatório, eles precisam configurar o RCA vinculando ele à filial 2. Caso contrário ele será exibido desagrupado da equipe.

Se quiserem alterar esse comportamento do maxGestão, eu sugiro abrir uma demanda de melhoria.

SELECT * FROM MXSUSUARI WHERE CODUSUR IN(487, 510, 543,545);

SELECT * FROM MXSUSUARIOS WHERE CODUSUARIO IN(107360, 74412, 85595);

SELECT * FROM MXSSUPERV WHERE CODSUPERVISOR = 17;

## Resposta Canonica

Identificamos que o comportamento apresentado no relatório está aderente à regra atual do maxGestão.

O relatório agrupado por supervisor também considera a filial no agrupamento. Nesse caso, o Supervisor 17 está vinculado à filial 2, porém o RCA 510, conforme cadastro na Rotina 517, não está vinculado à mesma filial. Por isso, ele não é exibido dentro da equipe do Supervisor 17 no relatório impresso e aparece de forma separada.

### Conclusão
A causa do comportamento é divergência de filial entre o Supervisor 17 e o RCA 510.

### Ação recomendada
- Vincular o RCA 510 à filial 2 para que ele seja agrupado corretamente no relatório.
- Caso desejem alterar essa lógica do maxGestão, será necessário abrir uma demanda de melhoria.

### Consultas utilizadas
```sql
SELECT * FROM MXSUSUARI WHERE CODUSUR IN(487, 510, 543,545);

SELECT * FROM MXSUSUARIOS WHERE CODUSUARIO IN(107360, 74412, 85595);

SELECT * FROM MXSSUPERV WHERE CODSUPERVISOR = 17;
```

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 419891
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
