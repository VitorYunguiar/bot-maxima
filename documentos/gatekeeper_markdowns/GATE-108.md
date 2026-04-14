# GATE-108 - Rastros não constam no MaxGestao

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Geolocalização
- Natureza: N/A
- Atualizado em: 2024-09-30T13:25:39.328-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o MaxGestão
>>Ir no painel de auditoria
>>Nos filtros: Filial: 3, Supervisor: Todos, Representante: 63809 - 5002.DOUGLAS MEDEIROS CUNHA, Data: 26/09/2024 a 26/09/2024
>>Pesquisar
>>E assim retorna os dados mais não traz o km total e nem trabalhado e fica constando que o RCA está com GPS desativado

Essa mesma consulta foi realizada na sexta, mais não trouxe nenhum dado do dia 26/09

>>Acessar o gestão
>>Ir em geolocalização
>>Filtrar: Pelo RCA 63809 - 5002.DOUGLAS MEDEIROS CUNHA, Data: 26/09/2023 a 26/09/2024
>>Pesquisar
>>E assim o RCA aparece em vermelho no mapa, clicar nele e ir na opção ver cliente
>>Ao ser direcionado, clicar para ver o trajeto executado
>>Filtrar pelo dia 26/09/2024
>>E assim retorna uma mensagem informando que não possui trajeto executado

Login: disjoirs.5002.douglas
senha: Dm@123456

## Resultado apresentado
Rastro demorando para subir ao gestão, e quando sobe fica informando que o RCA está com GPS desativado e sem km total e trabalhado

## Resultado esperado
Que conste os dados corretos no gestão

## Descrição
Foi verificado que no MaxGestão não sobe os rastros do vendedor em tempo real, o que acontece na sexta dia 27/09 consultamos os dados de quinta (26/09) e não havia subido a informação ainda, mais hoje dia 30/09 já consta, mais não tem km total e nem trabalhado. Outro ponto é que sempre fica falando que o RCA está com GPS desativado mesmo estando ativo
E quando tenta ver o trajeto executado do RCA no Mapa do gestão fala que não tem.

Nesse ponto foi identificado que os dados estão demorando aparecer no gestão. E gostaria de entender se é algo do gestão ou do MaxPedido

## Comentarios do Gatekeeper

### 1. 2024-09-30T13:25:39.326-0300 | Filipe do Amaral Padilha

Terá de ser encaminhado para N3 porque acredito que o problema seja o Km Trabalhado que não foi calculado corretamente, e com isso não mostra a informação nem no Painel de Auditoria do maxGestão e nem o trajeto executado em mapas.

--Gatekeeper envia para N3 nesse caso

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 397867
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificação realizada com base nos fatos apurados" não está explicitamente no texto-fonte. | A seção "Evidências analisadas" implica que houve análise formal de evidências, o que não consta no texto-fonte. | "O comportamento relatado está associado a falha no cálculo do Km Trabalhado" extrapola "acredito que o problema seja", que expressa hipótese, não confirmação. | "o que impacta a exibição das informações" apresenta relação causal como fato confirmado, enquanto no texto-fonte isso é uma crença/hipótese. | "para análise e tratativa" não consta no texto-fonte.
