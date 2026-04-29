# Rastro - maxPedido, maxTracking e maxGestao

> Documento preparado para ingestao em banco vetorial (RAG).
> Sistema: maxPedido | maxTracking | maxGestao | API de Rastros | Winthor
> Area: Rastreio | Check-in/check-out | Auditoria | KM trabalhado | KM total

---

## Objetivo

Orientar a analise de divergencias de rastreamento entre maxPedido, maxTracking, API de Rastros, banco nuvem e maxGestao. O foco e diagnosticar se o dado foi capturado no aparelho, enviado pelo maxTracking, consolidado pela API de Rastros e apresentado corretamente no maxGestao.

Use este documento quando o cliente relatar:

- Check-in, check-out, pedido ou justificativa de nao venda que nao aparece no maxGestao.
- Divergencia entre rastro apresentado no app, API de Rastros e painel de auditoria.
- KM trabalhado ou KM total zerado, inconsistente ou fora da margem aceitavel.
- Acompanhamento de RCA/representante sem informacoes no periodo esperado.

---

## Pre-requisitos no aparelho

Para que o maxPedido gere rastros confiaveis:

- GPS deve permanecer ligado.
- Otimizacao de bateria para o aplicativo deve estar desativada.
- O vendedor deve permitir localizacao conforme orientacao do sistema operacional.
- Em fluxos com check-in/check-out forcado, o RCA deve operar dentro das regras de raio/cerca eletronica configuradas.

Se GPS ou bateria estiverem incorretos, o app pode impedir o inicio do pedido ou gerar rastro com baixa precisao.

---

## Eventos que geram rastro

O maxPedido pode gerar informacoes de visita/rastro quando o vendedor:

- Realiza check-in.
- Realiza check-out.
- Faz pedido.
- Salva e bloqueia um pedido.
- Registra justificativa de nao venda.

Quanto mais restrito for o fluxo, como check-in/check-out forcado e cerca eletronica, maior tende a ser a precisao do atendimento registrado.

---

## Fontes de dados para diagnostico

Para investigar divergencias, colete e compare estas fontes:

| Fonte | Uso |
| --- | --- |
| Base do maxPedido | Confirma eventos gerados no app |
| Base do maxTracking | Confirma eventos capturados e enviados para API |
| API de Rastros | Confirma consolidacao consumida por maxPedido/maxGestao |
| Banco nuvem | Permite confronto com pedidos, visitas e integracoes |
| Painel de auditoria do maxGestao | Mostra como o dado chegou para consulta operacional |

Quando o caso for enviado para desenvolvimento, a base do maxPedido e a base do maxTracking ajudam a reproduzir e confrontar o fluxo completo.

---

## Analise no maxTracking

O maxTracking pode ser aberto no DBeaver como base SQLite apos transferir/descompactar o arquivo do aparelho.

Consultas uteis:

```sql
SELECT *
FROM MXS_EVENTS E
WHERE DATA_HORA_EVENTO BETWEEN '2023-11-21T00:00:00' AND '2023-11-21T23:59:59';
```

```sql
SELECT *
FROM MXS_EVENTS E
WHERE DATA_HORA_EVENTO BETWEEN '2023-11-21T00:00:00' AND '2023-11-21T23:59:59'
  AND CODCLI IN (...);
```

```sql
SELECT *
FROM MXS_RASTREAMENTOS
WHERE ID = :ID;
```

```sql
SELECT *
FROM MXS_RASTREAMENTOS
ORDER BY DATA_HORA_ENVIO_ACEITO ASC;
```

No maxTracking, a coluna de envio indica se a informacao foi enviada para a API de Rastros. Se o evento existe no maxTracking, mas nao foi enviado, a investigacao deve focar no processo de envio/sincronizacao do maxTracking.

---

## Analise na API de Rastros

A API de Rastros consolida dados consumidos por maxPedido e maxGestao.

Procedimento recomendado:

1. Obter token de autorizacao pela Central ou maxGestao.
2. Autorizar a requisicao no Swagger/API.
3. Informar codigo do cliente Maxima.
4. Informar codigo do produto Maxima quando aplicavel.
5. Filtrar por usuario, codusur, cliente e periodo.
6. Usar data inicial no inicio do dia e data final em `23:59:59`.
7. Executar a consulta e validar retorno HTTP 200.
8. Baixar o JSON quando houver muitos eventos e pesquisar por cliente/RCA.

Endpoint citado para distancia/rastro:

```text
https://maxrastro-prod-solucoesmaxima.com.br/swagger/index.html
GET /api/v1.1/distancia/rastro
```

O maxGestao espelha o resultado da API de Rastros. Para KM total e KM trabalhado, a apresentacao divide o valor retornado por mil.

---

## Relacao com RPMXSVISITAFV e Winthor

A tabela `RPMXSVISITAFV` pode conter informacoes de visita que integram com Winthor/rotina 344. Ela e uma forma diferente de consolidacao e nao necessariamente depende da API de Rastros.

Para analise de maxGestao, a referencia principal continua sendo a estrutura da API de Rastros. A `RPMXSVISITAFV` ajuda a confrontar se algum evento foi integrado ao Winthor, mas nao substitui a validacao do fluxo maxTracking -> API de Rastros -> maxGestao.

---

## Analise no painel de auditoria do maxGestao

O painel de auditoria permite validar:

- Primeiro e ultimo cliente do RCA.
- Atendimentos processados.
- Versao do aplicativo utilizada.
- Se o GPS estava ativo.
- Data/hora de inicio e fim.
- Pedido salvo/bloqueado.
- Informacoes consolidadas do objeto retornado pela API.

Retencao:

- Os dados consolidados ficam disponiveis por tempo limitado, citado no treinamento como cerca de 90 dias.
- Para acompanhamento recorrente, orientar cliente a gerar relatorios mensalmente ou, no maximo, a cada dois meses.
- Dados muito antigos podem ter sido limpos do MongoDB/API e nao voltar para consulta.

Quando houver informacao avermelhada ou inconsistente no painel, pode indicar que o rastro nao subiu do maxPedido para a API/MongoDB ou que ocorreu falso positivo/inconsistencia na consolidacao.

---

## KM total e KM trabalhado

Conceitos:

| Campo | Descricao |
| --- | --- |
| KM total | Todo o percurso capturado a partir do inicio da captura no aparelho/GPS |
| KM trabalhado | Percurso entre um check-out e o proximo check-in; considera atendimentos |
| Acuracia | Precisao do ponto de localizacao em relacao ao valor real |

Pontos importantes:

- Acuracia alta prejudica calculos e pode gerar divergencias.
- Quando a acuracia passa da margem aceitavel, o KM trabalhado pode ficar maior que o KM total.
- Use 100 metros como margem operacional para avaliar acuracia.
- Se o KM esta zerado, verificar se houve check-in, latitude/longitude, GPS e parametros de rastro.

---

## Parametro de KM inicial/final do roteirizador

Alguns clientes cadastram ponto inicial e ponto final no roteirizador. Essa informacao pode ser somada ao KM trabalhado.

Tabela citada:

```text
MXMP_ROTEIRIZACAO_DIA_SEMANA
```

Coluna citada:

```text
TOTAL_KM_DIA
```

Efeito pratico:

- Se o cliente cadastra 10 km da casa ate o primeiro cliente, esses 10 km podem ser somados ao KM trabalhado.
- Quando esse parametro estiver habilitado, a comparacao entre KM da API e KM apresentado no maxGestao deve considerar essa soma.
- Se estiver desabilitado, o KM trabalhado vem diretamente da API de Rastros.

---

## Ordem recomendada de diagnostico

1. Confirmar periodo, RCA, cliente e tipo de evento questionado.
2. Validar se GPS e bateria estavam corretamente configurados no aparelho.
3. Consultar base do maxPedido para confirmar se o evento foi gerado.
4. Consultar base do maxTracking para confirmar captura e envio.
5. Consultar API de Rastros para confirmar consolidacao.
6. Consultar painel de auditoria do maxGestao.
7. Se houver pedido, confrontar com historico/integracao de pedido no banco nuvem.
8. Para KM, validar acuracia, retorno da API e possivel configuracao de ponto inicial/final.

---

## Perguntas frequentes

### O check-in pode existir em RPMXSVISITAFV mesmo sem aparecer na API de Rastros

Sim. A `RPMXSVISITAFV` pode receber dados por um caminho diferente e integrar com Winthor/rotina 344. Para maxGestao, porem, a validacao principal e a API de Rastros.

### E obrigatorio coletar a base maxTracking

Para diagnostico completo, sim. Ela permite saber se o app capturou o evento e se o maxTracking tentou enviar para a API.

### O painel de auditoria mostra check-in, check-out e pedido separados

O painel consolida inicio/fim do atendimento. Para eventos detalhados, consultar mapa, API de Rastros ou relatorio customizado.

### Por que um rastro antigo nao aparece mais

Dados antigos podem ter sido limpos pela retencao do MongoDB/API. Por isso, relatorios de acompanhamento devem ser gerados periodicamente.

### Quem atua em problemas da API de Rastros

A API de Rastros envolve tecnologia/API, enquanto tracking e captura no app envolvem maxPedido/APK. Casos de KM trabalhado e divergencia de rastro devem ser triados conforme a origem do problema.
