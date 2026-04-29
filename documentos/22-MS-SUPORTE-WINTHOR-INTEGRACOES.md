# Suporte Winthor, integracoes e operacao maxPedido

> Documento preparado para ingestao em banco vetorial (RAG).
> Sistema: maxPedido | Winthor | Extrator | OERP | Oracle | Portainer
> Area: Sincronizacao | Desconto | API Winthor | Nova filial | Status 11 | Tributacao

---

## Objetivo

Consolidar procedimentos de suporte para operacao maxPedido/Winthor e integracoes relacionadas: lentidao de sincronizacao, desconto acima do permitido, API Winthor para edicao/cancelamento, cadastro de nova filial, processamento de pedidos/status 11 e tributacao.

---

## 1. Lentidao de sincronizacao

### Quando usar

Use quando o cliente relatar lentidao ou demora na sincronizacao do app.

### Pre-requisitos

- APK deve estar usando server base nova sync.
- Confirmar usuario, aparelho, horario aproximado e periodo da sincronizacao.

### Fontes de analise

| Fonte | Uso |
| --- | --- |
| `MXSCONEXOES` | Verificar registros da conexao/sincronizacao |
| `MXSCONEXOESLOG` | Verificar horarios inicial/final e logs de sincronizacao |
| Grafana | Acompanhar processo por `codusuario` |

URL citada:

```text
https://monitoramento.solucoesmaxima.com.br/d/log-maxpedido-apps-prod/logs-app-producao?orgId=1&from=now-1h&to=now&timezone=browser&var-app=maxpedido%2Fmxp-serverbase-mensagem-novasync&var-search=&refresh=10s
```

### Diagnostico

1. Filtrar o usuario no Grafana.
2. Comparar horario inicial e final em `MXSCONEXOES`/`MXSCONEXOESLOG`.
3. Verificar se os endpoints de sincronizacao foram chamados.
4. Se nao houver logs, a APK provavelmente nao chamou os endpoints.
5. Se houver logs com demora, identificar etapa mais lenta.

---

## 2. Limitar desconto / desconto acima do permitido

### Cenario

Cliente OERP permite desconto acima do limite configurado. Exemplo citado:

- `MXSTABPR.PERDESCMAX = 15%`.
- Politica de desconto tambem limita a 15%.
- Pedido ainda permite desconto maior, como 99%.
- Somente desconto extremo, como 100%, gera alerta.

### Causa provavel

Parametro `ACEITADESCTMKFV` ativo na tabela:

```text
MXSPARAMFILIAL
```

Quando esse parametro esta ativo, a APK pode aceitar desconto acima do definido na politica/campanha.

### Solucao

- Desativar `ACEITADESCTMKFV`.
- Em Winthor, ajustar pela rotina 132.
- Em OERPs, ajustar por update no banco em `MXSPARAMFILIAL`.

### Checklist

1. Confirmar produto e filial.
2. Validar `MXSTABPR.PERDESCMAX`.
3. Validar politica/campanha aplicada.
4. Consultar `MXSPARAMFILIAL.ACEITADESCTMKFV`.
5. Desativar parametro quando a regra desejada for limitar pelo desconto da politica.
6. Reprocessar/sincronizar e testar novo pedido.

---

## 3. API Winthor para edicao/cancelamento de pedidos

### Objetivo

Configurar integracao com Winthor Anywhere para permitir edicao/cancelamento de pedidos.

### Variaveis de ambiente na stack

```text
LINK_API_WINTHOR_CANCELAMENTO
USUARIO_API_WINTHOR_CANCELAMENTO
SENHA_API_WINTHOR_CANCELAMENTO
```

### Regras de preenchimento

| Variavel | Regra |
| --- | --- |
| `LINK_API_WINTHOR_CANCELAMENTO` | IP local/rede do cliente que acessa Winthor Anywhere |
| `USUARIO_API_WINTHOR_CANCELAMENTO` | Login do usuario em caixa alta conforme cadastro Winthor |
| `SENHA_API_WINTHOR_CANCELAMENTO` | Senha em caixa alta e criptografada com `Criptografia Maxima V1.0` |

Observacao de seguranca: nao registrar senhas reais em chamados/documentacao. Para testes manuais no Winthor Anywhere, usar a senha descriptografada diretamente no ambiente do cliente.

### Parametro Maxima

Configurar:

```text
UTLIZA_API_CANCEL_WINTHOR = S
```

Atencao: o parametro aparece como `UTLIZA_API_CANCEL_WINTHOR` sem a letra `I` apos `UTL`. Criar exatamente com esse nome se o ambiente espera essa grafia.

### Permissao RCA

Habilitar na Central de Configuracoes a permissao do RCA para:

- Editar pedidos enviados ao ERP.
- Editar pedidos enviados.
- Cancelar pedidos enviados.
- Solicitar aprovacao para pedidos de troca, quando aplicavel.

### Validacao final

1. Testar login no Winthor Anywhere com IP, usuario e senha.
2. Confirmar que o usuario possui permissao no Winthor.
3. Configurar variaveis na stack.
4. Configurar parametro `UTLIZA_API_CANCEL_WINTHOR`.
5. Habilitar permissao do RCA.
6. Executar cancelamento em pedido de teste.

---

## 4. Cadastro de nova filial

### Objetivo

Parametrizar corretamente filial, origem e escopo de dados para evitar:

- Processamento desnecessario.
- Lentidao na integracao.
- Excesso de geracao de base.
- Lentidao em relatorios.
- Sincronizacao de dados que o cliente nao utiliza.

Quanto menor e mais coerente o volume de dados, melhor a performance da nuvem e do aplicativo.

### Parametrizacao principal

Tabela local:

```text
PCMXSCONFIGURACOES
```

Parametros citados:

| Parametro | Uso |
| --- | --- |
| `CODFILIAL_IMPORTACAO` | Filiais usadas pela nuvem/app para a maior parte das informacoes |
| `CODFILIAL_PREST` | Filiais especificas para titulos/prestacoes |

Regra:

- Para titulos, se `CODFILIAL_PREST` existir, ele e usado.
- Se `CODFILIAL_PREST` nao existir, o fluxo assume `CODFILIAL_IMPORTACAO`.
- `CODFILIAL_PREST` existe para customizar titulos sem precisar ampliar toda a carga de importacao.

### Triggers

Triggers sao usadas para integracao em tempo real:

- Alteracao no banco dispara informacao.
- Validacoes ocorrem no momento do disparo.
- Se a filial ainda nao estava parametrizada quando o dado mudou, o dado pode nao ser reenviado automaticamente depois.
- Trigger invalida pode impedir insert/update/delete na tabela e causar erro operacional.

### Jobs

Jobs sao usadas quando a integracao precisa consolidar ou reduzir volume:

- Podem consultar varias tabelas.
- Consolidam dados antes de enviar para nuvem.
- Evitam geracao desnecessaria.
- Disparam de tempo em tempo.
- Perdem imediatismo, mas ganham performance.

### Pontos de atencao

- `PCPREST` pode subir via trigger, mesmo quando outras tabelas da filial nao sobem.
- Se `PCPREST` sobe sem nota/tabela relacionada, podem existir lacunas de visualizacao.
- Para nova filial, avaliar se basta ajustar parametro ou se precisa carga total/script para tabelas ja existentes.
- Em alguns casos, incluir filial depois exige processo de carga para dados antigos.

---

## 5. Processamento de pedidos / Status 11

### Fluxo Outros ERPs

1. Pedido/orcamento e gravado na nuvem em `MXSINTEGRACAOPEDIDO`.
2. Integracao do cliente faz GET na API.
3. API retorna informacoes para o ERP.
4. Ao enviar para o cliente, status muda para enviado ao ERP.
5. ERP retorna critica.
6. A nuvem guarda passivamente o retorno do cliente.

Nesse modelo, muitos problemas dependem da integracao do proprio cliente.

### Fluxo Winthor

1. Extrator faz GET na API PDV.
2. Extrator busca informacoes do pedido.
3. Extrator replica nas tabelas `PCPEDCFV` e `PCPEDIFV`.
4. Ao gravar nessas tabelas, pedido fica em status 11.
5. Scheduler/job Oracle chama a integradora.
6. Integradora processa o pedido no Winthor.
7. Logs ficam registrados, como em `PCLOGINTEGRADORA`.
8. Ao finalizar, a integradora atualiza status/importado e mensagem de critica.
9. Job coleta a critica e devolve para nuvem/aplicativo.

### O que significa status 11

Status 11 indica que o pedido foi gravado nas tabelas FV do Winthor e esta aguardando processamento pela integradora/scheduler.

Se o pedido fica parado em status 11, investigar:

- Scheduler/job Oracle parado.
- Job desabilitado.
- Parametro `job_queue_processes` insuficiente/zerado.
- Objeto invalido no banco.
- Erro em `PCLOGINTEGRADORA`.
- Erro em `PCMXSLOGERROS`.
- Integrador Winthor travado ou com lock.

### Tabelas e objetos para diagnostico

```text
MXSINTEGRACAOPEDIDO
PCPEDCFV
PCPEDIFV
PCLOGINTEGRADORA
PCMXSLOGERROS
USER_SCHEDULER_JOBS
ALL_SCHEDULER_JOBS
DBA_SCHEDULER_JOBS
V$PARAMETER
```

Consulta para objetos invalidos:

```sql
SELECT OWNER, OBJECT_NAME, OBJECT_TYPE, STATUS
FROM ALL_OBJECTS
WHERE STATUS = 'INVALID';
```

### Status citados

| Origem | Status | Significado |
| --- | --- | --- |
| `PCPEDCFV` | 1 | Aguardando processamento |
| `PCPEDCFV` | 2 | Integradora processou |
| `PCPEDCFV` | 3 | Erro; verificar observacao/critica |
| `PCPEDCFV` | 4 | Em processamento pela integradora |
| `MXSINTEGRACAOPEDIDO` | 0 | Pedido gravado na nuvem |
| `MXSINTEGRACAOPEDIDO` | 5 | Objeto com erro de processamento |
| `MXSINTEGRACAOPEDIDO` | 6 | Bloqueado na nuvem |
| `MXSINTEGRACAOPEDIDO` | 8 | Aguardando autorizacao de supervisor/maxGestao |
| Fluxo Winthor | 11 | Gravado em tabelas FV e aguardando integradora |

### Procedimento para status 11 parado

1. Verificar se o pedido esta em `PCPEDCFV` e `PCPEDIFV`.
2. Confirmar status nas tabelas FV.
3. Validar se scheduler/job Oracle esta habilitado e executando.
4. Conferir `job_queue_processes`.
5. Consultar logs da integradora.
6. Consultar `PCMXSLOGERROS`.
7. Verificar objetos invalidos.
8. Se job esta ativa, mas pedido nao processa, acionar DBA/cliente para avaliar integradora Winthor.

---

## 6. Tributacao

### Visao geral

Tributacao e uma das areas mais sensiveis do sistema, principalmente em outros ERPs. A Maxima depende dos dados fiscais enviados pelo ERP/cliente, e divergencias devem ser analisadas com apoio de evidencia fiscal.

### Modelos de tributacao

Winthor e outros ERPs podem trabalhar com:

- Tributacao por regiao.
- Tributacao por estado.

No Winthor, a parametrizacao pode ser verificada na rotina 132.

Em outros ERPs, verificar parametro:

```text
CON_USATRIBUTACAOPORUF
```

Tabela:

```text
MXSPARAMETROFILIAL
```

### Tributacao por regiao

Quando o cliente trabalha por regiao:

- A tributacao e vinculada por codigo ST.
- No Winthor, o codigo ST fica na tabela de preco `PCTABPR`.
- Na Maxima, consultar `MXSTABPR`.
- O codigo ST vincula aliquotas e regras fiscais.

### Tributacao por estado

Quando o cliente trabalha por estado:

- A consulta deixa de depender apenas do codigo ST na tabela de preco.
- Devem ser avaliadas tabelas de tributacao por UF/estado.
- Tabelas citadas: `MXSTABTRIBE` e `MXSTABETRIBE`.

### Filial NF

Quando o cliente usa filial NF:

- A tributacao deve considerar a filial emissora da nota.
- Deve trabalhar com tributacao por estado.
- A regra envolve filial NF, UF destino, produto e codigo ST.
- A configuracao pode estar relacionada a rotina 574 no Winthor.

### Como tratar divergencia fiscal

Para outros ERPs, o suporte geralmente nao tem acesso ao ERP nem conhecimento completo da regra fiscal do cliente. Quando houver divergencia:

1. Solicitar planilha do contador demonstrando o calculo esperado.
2. Solicitar origem de venda/tela com valores usados.
3. Validar se o cliente usa tributacao por estado ou regiao.
4. Conferir parametros e tabelas enviadas pela integracao.
5. Comparar aliquotas, base de calculo, reducao, DIFAL, substituicao, suframa e arredondamento.
6. Encaminhar para desenvolvimento apenas com evidencias completas.

### Tabelas e parametros

```text
PCTABPR
MXSTABPR
MXSTABTRIBE
MXSTABETRIBE
MXSPARAMETROFILIAL
CON_USATRIBUTACAOPORUF
```

### Observacoes importantes

- O calculo do imposto tende a seguir a mesma formula geral, mas entidades e arredondamentos variam por ERP.
- Em alguns ERPs, como cenarios citados de Sanquia/SAP, regras de casas decimais e origem dos dados podem afetar o resultado.
- Quando o cliente usa tributacao fonte automatica ERP, validar se o parametro e do lado Maxima e como o ERP enviou as entidades fiscais.

---

## Checklist geral de suporte

1. Identificar modulo: sincronizacao, desconto, API Winthor, nova filial, status 11 ou tributacao.
2. Coletar cliente, filial, RCA, pedido/produto e horario.
3. Validar parametros envolvidos.
4. Consultar tabelas locais/nuvem relacionadas.
5. Confirmar se o problema e Maxima, Winthor, OERP, DBA ou regra fiscal do cliente.
6. Para casos fiscais, exigir memoria de calculo/planilha do contador.
7. Para status 11, validar scheduler/integrador antes de alterar status manualmente.
8. Para nova filial, avaliar carga total/script quando dados antigos precisam subir.
