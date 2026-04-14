# GATE-136 - PCORCAVENDAI

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXGESN - Banco de Dados
- Natureza: Dúvida
- Atualizado em: 2024-10-07T14:44:49.966-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Boa tarde, cliente abriu uma demanda solicitando  que mudem a procedure do FV para que registre o CODDESCONTO na PCORCAVENDAI, pelo que o cliente me falou, quando o RCA ao fazer um orçamento, clica na opção "Salvar e Enviar Orçamento", o maxPedido grava nessas duas tabelas o orçamento, porém segundo o cliente, o campo CODDESCONTO não está sendo gravado.

Conectei no ambiente do cliente e validei que não existe uma PCORCAVENDACFV ou PCORCAVENDAIFV.

## Comentarios do Gatekeeper

### 1. 2024-10-03T16:49:18.786-0300 | Filipe do Amaral Padilha

Se trata de melhoria alinhado com o P.O Cleyton, por gentileza, verificar com o cliente se ele quer seguir com o processo de melhoria e então encaminhar para N3 como épico.

Fiz atualização do cliente e testei também na versão ponta maxPedido e banco de dados, atualmente o fluxo de gravar seria na PCPEDIFV e depois PCORCAI, porém a gente não grava a informação no bd do cliente e por isso seria melhoria e não apresenta a informação lá que ele deseja.

O cliente gostaria da funcionalidade para:

"Essa informação é útil pra saber se o representante tá usando uma política circular do mês inteiro por exemplo, ou se é uma política especifica, e eu vou usar pra fazer o conta corrente da empresa esses dados."

## Resposta Canonica

Trata-se de uma **melhoria**, alinhada com o **P.O Cleyton**, e não de correção.

No fluxo validado, a informação de desconto **deveria ser gravada primeiro na PCPEDIFV e depois na PCORCAI**. Entretanto, após atualização do cliente e testes realizados também na **versão ponta do maxPedido** e no **banco de dados**, foi confirmado que **essa informação não está sendo gravada no banco de dados do cliente**. Por esse motivo, **o dado desejado não é apresentado atualmente**.

A necessidade relatada pelo cliente é utilizar essa informação para identificar se o representante está aplicando uma **política circular do mês inteiro** ou uma **política específica**, além de apoiar o **controle de conta corrente da empresa** com base nesses dados.

### Conclusão
No cenário atual:
- **não há gravação da informação no banco de dados do cliente**;
- **a informação desejada não é apresentada**;
- o caso deve ser tratado como **melhoria**.

### Próximo passo
Validar com o cliente se deseja seguir com a solicitação de melhoria. Em caso positivo, **encaminhar para o N3 como épico**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 398848
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
