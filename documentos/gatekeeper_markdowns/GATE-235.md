# GATE-235 - Relatorio Venda por Equipe e Análise de Vendas x Rotina 146

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatórios - Dados Divergentes do ERP
- Natureza: N/A
- Atualizado em: 2024-10-29T11:50:47.349-0300

## Contexto do Problema

## Passos para reproduzir
Replicar busca com os mesmos filtros das imagens.

## Resultado apresentado
Valores divergentes

## Resultado esperado
Valores iguais.

## Descrição
Valores apresentados no relatório "Venda por Equipe e Análise de Vendas" do portal administrativo estão divergentes dos valores apresentados na rotina 146.

Imagens em anexo.

## Comentarios do Gatekeeper

### 1. 2024-10-29T11:50:47.348-0300 | Filipe do Amaral Padilha

Por padrão a Rotina 146 desconsidera o valor das bonificações e na hora de filtrar no relatório de Venda por Equipe e Análise de Venda eu reparei que não foi habilitado esse filtro.

Ele fica localizado na opção de "Deduzir" Selecionar tipo dedução antes de gerar os dados.

Com essa dedução (Bonificações) habilitada, os valores da 146 com o do relatório devem estar batendo.

!image-2024-10-29-11-51-00-172.png!

Obs: Tentei solicitar conexão para o cliente para eu verificar na 146 deles e garantir a taça, porém o cliente não me respondeu;

## Resposta Canonica

A divergência ocorre porque a Rotina 146 desconsidera por padrão o valor das bonificações, enquanto no relatório **Venda por Equipe e Análise de Vendas** a dedução correspondente não estava habilitada.

Pela análise textual das evidências, a comparação foi feita com regras diferentes entre as duas visões:
- na **Rotina 146**, as bonificações já são desconsideradas por padrão;
- no relatório, a opção **Deduzir** não estava configurada com o tipo **Bonificações**.

Com a dedução de **Bonificações** habilitada no relatório, os valores do relatório e da Rotina 146 devem ficar alinhados.

### Ação recomendada
- No relatório **Venda por Equipe e Análise de Vendas**, habilitar a opção **Deduzir**.
- Selecionar o tipo de dedução **Bonificações** antes de gerar os dados.
- Validar a comparação com a **Rotina 146** do cliente.

### Limitação da análise
Não foi possível confirmar diretamente a configuração da **Rotina 146** no ambiente do cliente, pois houve tentativa de solicitar conexão, mas não houve retorno. Portanto, o próximo passo é aguardar o retorno do cliente para validar a rotina e, em paralelo, orientar o ajuste do filtro de dedução no relatório.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 403628
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
