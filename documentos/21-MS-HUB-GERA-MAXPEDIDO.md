# Hub Gera + maxPedido

> Documento preparado para ingestao em banco vetorial (RAG).
> Sistema: Hub Gera | maxPedido | maxGestao | maxPag
> Area: Campanhas | Regras comerciais | Ofertas | Brindes | Portfolio recomendado | Logs Gera

---

## Objetivo

Documentar a integracao entre Hub Gera e maxPedido, incluindo ativacao, sincronizacao, execucao de regras comerciais, ofertas, brindes, portfolio recomendado, parametros, responsabilidade de suporte, status de pedidos, tabelas e logs para diagnostico.

O Hub Gera processa e valida regras comerciais complexas. O maxPedido atua como interface de execucao para o vendedor.

---

## Visao geral

A integracao Hub Gera + maxPedido permite aplicar automaticamente:

- Descontos.
- Brindes.
- Precificacao dinamica.
- Campanhas progressivas.
- Portfolio recomendado.
- Classificacoes comerciais.

Na pratica, regras comerciais sao calculadas pelo Hub Gera, enquanto o vendedor opera o pedido no maxPedido.

---

## Requisitos recomendados do aparelho

| Componente | Especificacao |
| --- | --- |
| Sistema operacional | Android 11 ou superior |
| Processador | Qualcomm Snapdragon serie 700 ou equivalente |
| Memoria RAM | 6 GB |
| Armazenamento livre | 1 GB |

---

## Fluxo de uso no maxPedido

1. Ativar o servico da Gera.
2. Gerar chave de integracao entre Hub Gera e maxPedido.
3. Instalar/usar o aplicativo Gera quando necessario para sincronizacao e execucao das regras.
4. Antes de iniciar o pedido, realizar sincronizacao manual no maxPedido via broadcast com Hub Gera.
5. A sincronizacao traz ofertas, recomendacoes de produtos e classificacoes comerciais.
6. Se o parametro de bloqueio estiver ativo, o pedido so pode ser confeccionado apos sincronizacao concluida.
7. Na aba Tabela, o maxPedido exibe produtos conforme portfolio recomendado pela industria.
8. Na aba Ofertas, o vendedor visualiza campanhas em andamento, nao positivadas e positivadas.
9. O vendedor pode recalcular ofertas.
10. Ao atingir regras de campanha, brindes ficam disponiveis na aba de ofertas.
11. Ao inserir itens e fechar pedido, descontos sao aplicados automaticamente conforme regras atingidas.
12. Ao finalizar, o sistema alerta oportunidades nao aproveitadas e solicita recalcule das ofertas quando aplicavel.
13. Pedido e enviado para processamento no Hub Gera.

---

## Parametros de configuracao

| Parametro | Descricao | Formato esperado |
| --- | --- | --- |
| `HABILITA_SISTEMA_GERA` | Libera a visao e as rotinas Gera no APK | Booleano S/N |
| `CNPJ_SISTEMA_GERA` | CNPJ da filial/contrato Gera validado conforme filial do vendedor | String CNPJ |
| `GUID_DISTRIBUIDOR_GERA` | Identificador unico do distribuidor no Hub Gera | UUID/String |
| `FUNCTION_KEY_GERA` | Chave de acesso do cliente no sistema Gera | String |
| `DISTRIBUIDORES_GERA` | Codigos de fornecedores vinculados a operacao Gera | CSV sem espaco |
| `BLOQUEIA_CONFECCAO_PEDIDO_GERA` | Bloqueia confeccao se a sincronizacao Gera nao foi concluida | Booleano S/N |

Observacao: a documentacao interna cita `BLOQUEIA_CONFECCAO_PEDIDO_GERA` como default `S` e oculto `S`.

---

## Responsabilidade de suporte

### Acionar Suporte Gera

- Hub Gera fora do ar, instavel ou indisponivel.
- Erro de autenticacao ou token.
- Geracao/validacao de tokens.
- Calculo de preco, descontos e brindes.
- Portfolio recomendado/mix ausente ou inconsistente.
- Status de fechamento e autorizacoes comerciais no Hub Gera.

### Acionar Suporte Maxima

- Dados nao atualizam no maxPedido.
- Falha de sincronizacao de pedidos ou informacoes.
- Filtros que nao funcionam.
- Dados inconsistentes na visualizacao.
- Produtos aparecendo indevidamente ou bloqueados sem motivo no maxPedido.
- Problemas de interface/operacao do app apos retorno do Hub Gera.

---

## Perguntas frequentes

### As validacoes de campanha sao atualizadas automaticamente no maxPedido

As validacoes dependem da sincronizacao e do recalcule das ofertas. Se a regra mudou no Hub Gera, valide se a sincronizacao foi concluida e se o vendedor recalculou as ofertas.

### O maxPedido processa brindes para o ERP

Nao. Os brindes conquistados sao apresentados no maxPedido, mas o processamento e realizado pelo Hub Gera.

### O que acontece se o vendedor aplica desconto manual junto com desconto Gera

O Hub Gera define se a campanha permite desconto manual adicional. Quando permitido, o proprio Hub Gera audita valores repassados entre industria e distribuidor.

### E possivel misturar produtos Gera e produtos padrao no mesmo pedido

Sim, dependendo da regra de portfolio/mix retornada pelo Hub Gera e da configuracao do contrato. A aba Tabela pode filtrar produtos conforme o portfolio recomendado.

### maxPedido + Gera integra com maxGestao e maxPag

Sim. O fluxo pode envolver maxGestao e maxPag conforme a regra de autorizacao/pagamento do pedido.

---

## Status e criticas de pedidos Gera

| Mensagem/status | Diagnostico |
| --- | --- |
| Aguardando processamento no HubGera | Fluxo normal de fila de processamento |
| Pedido fechado, aguardando aprovacao no HubGera | Regras de negocio validadas; aguardando liberacao comercial |
| Pedido aprovado, aguardando retorno da autorizacao do HubGera | Transicao interna para autorizacao final |
| Pedido pronto para integracao | Pedido pode seguir para ERP via nuvem |
| Pedido com erro de integracao Gera | Pode liberar botao de reprocessamento ao segurar o pedido |
| Erro por item de portfolio invalido | Problema de regra/portfolio Gera; consultar Suporte Gera |
| Erro tecnico, timeout ou status 500 | Validar log, JSON de retorno e possibilidade de reprocessamento |

Quando houver erro, a rotina recomendada e consultar `MXSLOGSGERA`, localizar o JSON e buscar pelo codigo auxiliar/EAN do produto quando a falha envolver item de portfolio.

---

## Diagnostico por logs

Tabela principal:

```text
MXSLOGSGERA
```

Campos citados:

| Campo | Descricao |
| --- | --- |
| `IDLOG` | Identificador do log |
| `TIPOLOG` | Broadcast executado ou tipo de retorno recebido |
| `IDENTIFICADOR` | `NUMPED` ou `IDPEDIDO`, dependendo do broadcast; pode ser nulo em sincronizacao |
| `RETORNO` | Envio do broadcast ou retorno do Hub Gera |
| `DTRETORNO` | Data/hora do envio ou recebimento do retorno |

Use a tabela para:

- Confirmar se a sincronizacao ocorreu.
- Validar retorno do Hub Gera.
- Identificar erros de produto, portfolio, promocao ou autorizacao.
- Auditar regras aplicadas ao pedido.

---

## Estrutura de tabelas Gera

### Cadastro e vinculos

| Tabela | Finalidade |
| --- | --- |
| `MXSINDUSTRIAGERA` | Cadastro das industrias e CNPJs |
| `MXSCLIENTEGERA` | Vinculo de documentos de clientes a industria |
| `MXSCLASSIFICACAOCOMERCIALGERA` | Classificacao comercial por industria/cliente |
| `MXSSEGMENTOSGERA` | Segmentos/faixas e hashtags de classificacao |

### Produtos, portfolio e campanhas

| Tabela | Finalidade |
| --- | --- |
| `MXSPRODRECOMENDADOGERA` | Portfolio recomendado, cotas e precos sugeridos |
| `MXSPROMOCOESGERA` | Promocoes/campanhas recebidas do Hub Gera |
| `MXSREQUISITOSGERA` | Requisitos para conquista de promocao |
| `MXSPREMIOSGERA` | Premios, brindes e descontos |
| `MXSFAMILIAGERA` | Familias ou classificacoes de produtos |
| `MXSPRODFAMILIAGERA` | Relacao entre familia/classificacao e EAN |

---

## Campos tecnicos relevantes

### `MXSPRODRECOMENDADOGERA`

| Campo | Uso |
| --- | --- |
| `INDUSTRIA_ID` | Industria no Gera Promo |
| `EAN` | EAN do produto |
| `PORTFOLIOCODE` | Codigo do portfolio |
| `QTADQUIRIDA` | Quantidade da cota ja adquirida pelo PDV |
| `QTLIBERADA` | Quantidade da cota ainda disponivel |
| `QTCOTA` | Cota total recomendada |
| `PRECOSUGERIDO` | Preco ideal/recomendado |
| `PRECOMINIMO` | Menor preco sugerido |
| `PRECOMAXIMO` | Maior preco sugerido |
| `PRECOCUSTO` | Preco de custo |

### `MXSPROMOCOESGERA`

| Campo | Uso |
| --- | --- |
| `CODE` | Codigo da promocao na industria |
| `NAME` | Nome da promocao |
| `DESCRIPTION` | Descricao da promocao |
| `REQUIREMENTSMINIMUM` | Requisitos minimos para conquista |
| `REQUIREMENTSTOTAL` | Requisitos totais configurados |
| `DISCOUNTLIMIT` | Valor maximo sobre o qual desconto aplica |
| `DISCOUNTLIMITMINIMUM` | Valor minimo para desconto |

### `MXSREQUISITOSGERA`

| Campo | Uso |
| --- | --- |
| `IDREQUISITO` | Identificador do requisito |
| `CODEPROMOTION` | Codigo da promocao |
| `RANGE` | Faixa de valores quando aplicavel |
| `VALUE` | Quantidade ou valor requerido |
| `VALUETYPE` | `Different Items`, `Items` ou `$` |
| `TARGETTYPE` | `ProductLine`, `ProductClassification`, `Product` ou `AnyProduct` |
| `TARGETCODE` | Codigo do alvo do requisito |
| `TARGETNAME` | Nome do alvo |
| `LOGICOPERATOR` | Operador `And` ou `Or` |

### `MXSPREMIOSGERA`

| Campo | Uso |
| --- | --- |
| `IDPREMIO` | Identificador do premio |
| `CODEPROMOTION` | Codigo da promocao |
| `RANGE` | Faixa de valor quando aplicavel |
| `VALUE` | Valor do premio |
| `VALUETYPE` | `Items`, `%`, `$` ou `To$` |
| `TARGETTYPE` | Alvo do premio: produto, familia, requisito ou qualquer produto |
| `TARGETCODE` | Codigo do produto/familia alvo |
| `TARGETNAME` | Nome do produto/familia alvo |
| `LOGICOPERATOR` | Operador entre premios |

---

## Regras de negocio internas

- O sistema deve validar `CNPJ_SISTEMA_GERA` conforme filial logada pelo vendedor.
- `GUID_DISTRIBUIDOR_GERA` e chave mestre; sem GUID valido, as requisicoes ao Hub Gera nao devem prosseguir.
- A aba Tabela deve filtrar produtos com base no portfolio/mix retornado pela Gera.
- Regras Gera podem bloquear ou sobrepor regras locais dependendo do contrato.
- Em falha de comunicacao, timeout ou status 500, manter registro para auditoria e permitir diagnostico/reprocessamento quando aplicavel.
- Monitoramento deve usar `MXSLOGSGERA` para confirmar broadcast, retorno, erro e JSON recebido.

---

## Checklist de diagnostico

1. Confirmar se `HABILITA_SISTEMA_GERA` esta ativo para o cliente/filial.
2. Validar `CNPJ_SISTEMA_GERA`, `GUID_DISTRIBUIDOR_GERA` e `FUNCTION_KEY_GERA`.
3. Confirmar fornecedores em `DISTRIBUIDORES_GERA`.
4. Verificar se o app Gera/maxPedido sincronizou com sucesso.
5. Validar se `BLOQUEIA_CONFECCAO_PEDIDO_GERA` esta impedindo pedido sem sincronizacao.
6. Consultar `MXSLOGSGERA` pelo pedido, broadcast ou retorno.
7. Para produto ausente, validar `MXSPRODRECOMENDADOGERA` e portfolio.
8. Para campanha/desconto/brinde, validar `MXSPROMOCOESGERA`, `MXSREQUISITOSGERA` e `MXSPREMIOSGERA`.
9. Para classificacao comercial, validar `MXSCLASSIFICACAOCOMERCIALGERA` e `MXSSEGMENTOSGERA`.
10. Se erro for calculo/regra do Hub, acionar Suporte Gera.
11. Se erro for sincronizacao/visualizacao no app, acionar Suporte Maxima.
