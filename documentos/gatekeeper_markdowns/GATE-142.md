# GATE-142 - Dashboard inicial sem valores

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Pedro Henrique Rodrigues Moura
- ERP do cliente: Winthor
- Assunto: MXPED - Resumo de Vendas
- Natureza: Dúvida
- Atualizado em: 2024-10-04T10:00:12.077-0300

## Contexto do Problema

## Passos para reproduzir
- Login: caete.145

>> Acessar MaxPedido;
>> "Atualizar Menu";

## Resultado apresentado
>> Dados atualizados;
>> Porém não carrega nenhum valor;

>> No resumo de vendas apresenta vendas faturadas.

## Resultado esperado
>> Que carregue os valores visto que todos os acessos externos estão liberados.

## Descrição
- Após atualizar o ambiente nuvem e local do cliente, os valores na dashboard inicial não apresenta nada.

## Comentarios do Gatekeeper

### 1. 2024-10-04T09:53:45.402-0300 | Filipe do Amaral Padilha

Para atualizar o gráfico do menu de vendas, na Rotina 353 eles precisariam cadastrar a meta do RCA 145 mensal, porque eles não cadastraram ainda, a tabela PCMETARCA está vazia.

Uma dica boa também para entender o funcionamento do gráfico do Menu inicial: Ele depende de a meta mensal estar definida, essa meta mensal fica na aba de Objetivos > Venda dentro do maxPedido, se o campo "Meta:" estiver assim R$0,00 então significa que não foi cadastrada a meta mensal.

Então por isso que mesmo com acesso na 9002, não atualiza o menu deles com os resultados. Pelo o que analisei, seria somente isso, as PCDIASUTEIS e PCDATAS deles já estão corretas.

Após cadastrarem a meta de venda mensal do RCA na 353 é só atualizar o menu e validar a mesma aba dentro de objetivos que os dados serão apresentados.

--------

Já sobre as outras informações da tela inicial (Pedidos e Objetivos)

-> nada é apresentado porque o parâmetro CRITERIOVENDA está definido como "F" então só vai carregar a venda faturada do mês atual e como nenhum pedido foi faturado ainda desse RCA nesse Mês, nenhuma informação é apresentada.

## Resposta Canonica

**Causa identificada**

A ausência de valores na dashboard inicial do MaxPedido ocorre por dois fatores combinados:

1. **A meta mensal do RCA 145 não foi cadastrada**  
   A tabela **PCMETARCA** está vazia, e o gráfico do menu inicial depende dessa meta para ser atualizado.

2. **O parâmetro `CRITERIOVENDA` está definido como `"F"`**  
   Nessa configuração, a tela inicial considera **apenas venda faturada do mês atual**. Como **não há pedido faturado para o RCA 145 neste mês**, não são exibidas informações em **Pedidos** e **Objetivos**.

**Validações realizadas**

- A tabela **PCMETARCA** está vazia.
- Na **Rotina 353**, ainda não foi cadastrada a meta mensal do **RCA 145**.
- No MaxPedido, a meta mensal é refletida na aba **Objetivos > Venda**.
- Se o campo **“Meta:”** aparecer como **R$0,00**, isso confirma que a meta mensal não foi cadastrada.
- Mesmo com acesso liberado na **9002**, o menu não atualiza os resultados sem a meta mensal cadastrada.
- As tabelas **PCDIASUTEIS** e **PCDATAS** já estão corretas.
- `CRITERIOVENDA = "F"` limita a exibição à venda faturada do mês atual.

**Ação recomendada**

- Cadastrar a **meta de venda mensal do RCA 145** na **Rotina 353**.
- Validar no MaxPedido, em **Objetivos > Venda**, se o campo **“Meta:”** deixa de aparecer como **R$0,00**.
- Após o cadastro, executar **Atualizar Menu**.
- Validar novamente a aba **Objetivos > Venda** para confirmar a exibição dos dados.

**Responsável pela ação**

- **Cliente / usuário responsável** pelo cadastro da meta mensal do **RCA 145** na **Rotina 353**.

**Próximo passo**

Cadastrar a meta mensal do RCA 145 na Rotina 353, atualizar o menu e validar na aba **Objetivos > Venda** se os dados passam a ser exibidos.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 398945
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
