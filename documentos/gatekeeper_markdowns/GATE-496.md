# GATE-496 - reprocessamento de registros de rastro

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - MaxTrack
- Natureza: Dúvida
- Atualizado em: 2024-12-13T09:34:12.282-0300

## Contexto do Problema

## Passos para reproduzir
conforme descrição

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Senhores, ao analisarmos o cenário da demanda citada, observei que a RCA estava usando a versão 3.248.2, versão essa que é anterior a versão 3.258.3 que contém correções implementadas em calculo de KM total, onde é possível constatar que as inconsistências que o cliente relata abaixo, possam ser geradas devido a essa versão:

"Possui um erro no registro de KM do setor 54, em que a mesma realizou toda a rota planejada e possui apenas 1,72 no registro de KM total segue prints e base de dados em anexo"

Nesse cenário, a atualização da versão corrige essas inconsistências de valores anteriores de KM que o cliente relata, ou para se obter os dados retroativos demanda de um reprocessamento no back-end para ser regularizados os registros de KM? em anexo segue base maxtracking

!image-2024-12-12-17-46-16-837.png!

!image-2024-12-12-17-46-34-551.png!

## Comentarios do Gatekeeper

### 1. 2024-12-13T08:35:27.822-0300 | Filipe do Amaral Padilha

Realizei a análise do dia 19/11/2024 referente ao trajeto rastreado através do maxPedido da RCA 30784:

A análise revelou que os dados apresentados do Km total e Trabalhado estão bastante consistentes.

Em anexo eu disponibilizei um vídeo explicando a análise realizada e também imagens chave com as informações.

O fato é que a RCA não se deslocou nesse dia mais que duas ruas, ela ficou andando apenas no entorno do mesmo lugar. Todas as evidências comprovam que a RCA teve um rastreamento consistente no maxPedido e que ela não foi aos clientes que constam como roteirizados.

Nesse sentido, o cliente precisa entender que o km total calculado está consistente e que a RCA não deslocou para gerar uma kilometragem maior do que a apresentada no sistema. Sendo assim, não será necessário reprocessamento de dados, e nem seria possível, porque o próprio rastreamento foi consistente e mostra que foram rastreados os 1,72km total.

## Resposta Canonica

Após análise do dia **19/11/2024** para a **RCA 30784**, com base no rastreamento de origem **maxPedido**, foi verificado que a quilometragem apresentada está **consistente** com o trajeto efetivamente realizado.

Foi identificado que a RCA **não se deslocou além de duas ruas**, permanecendo no entorno do mesmo local, e **não foi aos clientes que constavam como roteirizados**. Nesse contexto, o total rastreado de **1,72 km** está aderente ao comportamento registrado no dia analisado. Os dados de **Km total** e **Km trabalhado** também se mostraram consistentes na análise textual realizada sobre o rastreamento.

Dessa forma, a situação **não caracteriza necessidade de reprocessamento**, pois o próprio rastreamento está consistente com a kilometragem calculada.

**Conclusão**
- **Data analisada:** 19/11/2024  
- **RCA:** 30784  
- **Origem do rastreamento:** maxPedido  
- **Km total rastreado:** 1,72 km  

**Orientação**
Informar ao cliente que a kilometragem apresentada no sistema está consistente com o rastreamento realizado e que **não será necessário reprocessamento de dados**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 412055
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
