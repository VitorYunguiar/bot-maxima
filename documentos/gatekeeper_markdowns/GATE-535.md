# GATE-535 - Lucratividade divergente da 146

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatórios - Dados Divergentes do ERP
- Natureza: Dúvida
- Atualizado em: 2024-12-20T10:05:19.081-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar o maxGestão;
>> Relatórios;
>> Relatório Venda por Equipe e Análise de Vendas;
>> Inserir filtros do print em anexo;
>> Comprar com os valores anexados da rotina 146 do Winthor.

## Resultado apresentado
Valor da %Luc divergente entre o maxGestão e a 146;

## Resultado esperado
Valores iguais.

## Descrição
Porcentagem da lucratividade do relatório do maxGestão está divergente da 146.

Validado no banco local do cliente que os valores da PCHISTORICPEDC e PEDI estão exatamente iguais ao banco nuvem.

Executados os selects em anexo no banco local e no banco nuvem e os dois retornaram exatamente os mesmos valores.

Busca no maxGestão feita com e sem debitar bonificação, porem o valor segue divergente.

## Comentarios do Gatekeeper

### 1. 2024-12-20T09:46:46.481-0300 | Filipe do Amaral Padilha

O script que a gente executa no portal executivo, para o relatório "Venda por Equipe e Análise de Vendas" por padrão faz a dedução das despesas em cima do valor de venda.

Para ficar compatível com a 146, atualmente é necessário sempre marcar a opção "Desconsiderar valor despesas" diretamente na Rotina dentro do Winthor.

Outra ponderação: No maxGestão é necessário deduzir as Bonificações porque a 146 faz isso por padrão.

Com isso você verá que a lucratividade passa a bater entre maxGestão e Rotina 146 e o valor de venda também.

Porém, mesmo fazendo esse procedimento, eu reparei que fica errado a lucratividade de uma das equipes de supervisores. E devido a isso, eu vou encaminhar a demanda para N3.

Eu também vou questioná-los sobre essa questão do "Desconsiderar valor despesas", que atualmente, na 146 é parametrizável a dedução, porém no nosso relatório sempre deduz e não tem como alternar isso no maxGestão.

## Resposta Canonica

**Causa identificada**

A divergência ocorre porque o relatório **“Venda por Equipe e Análise de Vendas”** no **maxGestão/portal executivo** deduz **por padrão** as despesas sobre o valor de venda. Já na **Rotina 146**, para ficar compatível com esse comportamento, é necessário marcar a opção **“Desconsiderar valor despesas”**.  
Além disso, no **maxGestão** também é necessário **deduzir as bonificações**, pois a **Rotina 146** faz isso por padrão.

**Análise**

- O comportamento padrão do relatório no maxGestão é deduzir despesas sobre o valor de venda.
- Na Rotina 146, a dedução de despesas é parametrizável pela opção **“Desconsiderar valor despesas”**.
- Quando:
  - a opção **“Desconsiderar valor despesas”** é marcada na Rotina 146; e
  - no maxGestão é feita a **dedução das bonificações**;
  
  a **lucratividade** e o **valor de venda** passam a bater entre o maxGestão e a Rotina 146.

**Limitação identificada**

Mesmo com esse procedimento, foi constatado que **a lucratividade de uma das equipes de supervisores permanece incorreta**.

**Ação recomendada**

1. Marcar sempre a opção **“Desconsiderar valor despesas”** na **Rotina 146** do Winthor.
2. No **maxGestão**, realizar a **dedução das bonificações**.
3. **Encaminhar a demanda para o N3**, pois permanece divergência na lucratividade de uma das equipes.
4. Solicitar ao **N3** avaliação sobre a diferença de comportamento da opção **“Desconsiderar valor despesas”** entre a **Rotina 146** e o **maxGestão**.

**Responsável pelo próximo passo**

- **N3**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 413385
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
