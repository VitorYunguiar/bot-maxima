# GATE-579 - Ajuda com Crítica da Integradora ao Enviar Pedido TV8

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido - Crítica
- Natureza: Dúvida
- Atualizado em: 2025-01-06T11:57:52.951-0300

## Contexto do Problema

## Passos para reproduzir
>>790.LDF
>Iniciar pedido no cliente 1 - CONSUMIDOR FINAL
>Tipo de venda entrega futura
>Filial 51
>Marcar a bolinha de "venda assistida"
>Plan. Pg 20
>Cobrança Visa Débito

>Adicionar qualquer produto no pedido
>Quando aparecer o pop up da venda assistida, selecionar RI - Entrega Imediata
>Salvar e enviar o pedido
>Observar a crítica

## Resultado apresentado
Quando o pedido é processado a integradora retorna a crítica:

Pedido TV8 gerado : 286472 na posicao : L
-6502-ORA-06502: PL/SQL: erro: buffer de string
de caracteres pequeno demais numerico ou de
valor-ORA-06512: em "LDF.INTEGRADORA_COMPLE",
line 2890
ORA-06512: em "LDF.INTEGRADORA", line 27821

## Resultado esperado
Entender o que está causando isso e se podemos resolver daqui sem acionar a TOTVS.

## Descrição
Bom dia, Carlos/Filipe,

Preciso de auxílio para identificar a causa da crítica apresentada pela integradora ao enviarmos um pedido TV8 (Venda Assistida).

Realizei a atualização completa do ambiente antes de testar, mas obtive o mesmo resultado observado pelo cliente. A integradora retorna uma mensagem referente ao "buffer de string de caracteres", indicando que ele é "pequeno demais, numérico ou de valor".

## Comentarios do Gatekeeper

### 1. 2025-01-06T11:57:52.950-0300 | Filipe do Amaral Padilha

Realizei a conexão com o banco do cliente para realizar a verificação do problema e abaixou vou estar colocando os detalhes:

Inicialmente, gostaria de esclarecer que o problema não é causado pela Máxima e a resolução também não será feita por nossas equipes.

O problema ocorre na package "INTEGRADORA_COMPLE" que é do SCHEMA principal da "LDF" do banco do ERP (WINTHOR). Segundo os dados que rastreamos, na hora de processar o pedido na PCPEDCFV, essa pkg utiliza a variável VSCODFILIAL que está definida como VARCHAR2(1); onde justamente está sendo acusado o erro que foi retornado na própria crítica da Integradora do Winthor. linha 2890.

Isso ocorre porque o pedido foi enviado na Filial (51), ou seja, se a variável só aceita VARCHAR2(1), vai estourar o campo e dar problema na hora de processar a informação.

Em anexo eu disponibilizei prints seguindo a orientação do próprio banco do Winthor para localizar o problema na PKG do banco.

Então conforme evidências e expliquei inicialmente, nós não prestamos consultoria e nem manutenção em recursos do Banco do Winthor que não são nossos. No caso a "LDF.INTEGRADORA_COMPLE" não é uma funcionalidade desenvolvida pela Máxima e portanto não prestamos a manutenção nela.

O cliente deve validar o criador dessa PKG, não sabemos se é da TOTVS ou se é algo interno e solicitar a manutenção ao criador.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 414939
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que o valor excedente gerou especificamente um "erro de buffer de string" não aparece no texto-fonte. O texto apenas diz que "vai estourar o campo e dar problema" e que esse é o erro retornado na crítica da Integradora do Winthor. | A formulação "em conformidade com a própria crítica apresentada" não está explicitamente no texto-fonte, embora haja menção de que o erro foi retornado na própria crítica da Integradora do Winthor.
