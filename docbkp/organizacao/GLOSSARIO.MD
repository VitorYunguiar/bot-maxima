### Bloquear RCA de fazer bonificação sem saldo de C/C

<aside>
💡

CON_USACREDRCA = S
CON_BONIFICALTDEBCREDRCA = S
IMPEDIR_ABATIMENTO_SEMSALDORCA = S
PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N

</aside>

### Brindes

```jsx
MXSBRINDEEXRESTRICOES
MXSBRINDEEX
MXSBRINDEEXVALIDACOES
MXSBRINDEEXPREMIO
```

### Venda Broker

```jsx
MXPED-57813
```

### Conta Corrente / CC / Flex

<aside>
💡 EXIBIR_SALDOCC_DISPONIVEL = S
CON_USACREDRCA = S
CON_TIPOMOVCCRCA = VV
MXSUSUARI.USADEBCREDRCA = S

DEBITO NA VENDA, CREDITO NO ACERTO (VA)
DEBITO NA VENDA, CREDITO NO FATURAMENTO (VF)
DEBITO/CREDITO NA VENDA (VV)
DEBITO/CREDITO NO FATURAMENTO (FF)

</aside>

---

### Bloquear RCA de fazer bonificação sem saldo de C/C

<aside>
💡

CON_USACREDRCA = S
CON_BONIFICALTDEBCREDRCA = S
IMPEDIR_ABATIMENTO_SEMSALDORCA = S
PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N

</aside>

### Desconto Máximo / Desconto Produto / Limite de Desconto

<aside>
💡 Verificar MXSTABPR.PERDESCMAX
Verificar MXSCLIENTREGIAO.PERDESCMAX
Verificar Políticas de desconto do item

</aside>

### Verificar se o Serviço de Agendamento do Oracle está rodando

```jsx
SELECT sid, serial#, username, program, module
FROM v$session
WHERE program LIKE 'CJQ%'
   OR program LIKE 'J0%';
```

### Meta Gráfico

<aside>
💡 Rotinas: 399 / 3305
Tabelas: ERP_MXSMETARCA, PCMETARCA, PCMETA

Obs: Não necessariamente as informações precisam descer para nuvem, se tratando da rotina 3305, basta apenas que a meta esteja na tabela PCMETA
Obs2: Possivelmente existe chance de não informar a meta caso a flag de dias úteis não esteja marcada

</aside>

### Histórico de Pedidos

<aside>
💡 Parâmetro FILTRAR_HISTCOMPRAS_RCA = N: O mesmo realiza ou não o filtro onde será apresentado o histórico de compras somente do rca quem vendeu ou de todos os representantes.

Parâmetro FILTRAR_DADOS_RCA = N: Mostrar apenas pedidos que foram realizados pelo RCA atual (Se configurado como N traz de todos os RCAs que fizeram pedido no cliente).

Parâmetro FILTRAR_DADOS_CONSULTA_POSITIVACAO_RCA = N: Quando este parâmetro estiver verdadeiro (S), irá trazer a positivação dos clientes somente dos pedidos que o RCA fez no modulo Consultas > Positivação de clientes.

Parâmetro FILTRAR_DADOS_TITULOS_RCA = S: S - Só mostra os títulos do RCA que está logado / N - Mostra os títulos de todos os RCAs.

Parâmetro GERAR_DADOS_MIX_CLIENTES_DIAS = 90: Gera mix das vendas realizadas nos clientes dos últimos 90 dias.

Parâmetro CATALOGO_PEDIDOS_DIAS_SYNC = 90: Mostra o histórico de vendas dos últimos 90 dias.

</aside>

### Relatório Espelho do Pedido

<aside>
💡 EXIBIR_CAMPOS_ESPELHO_POR_EMBALAGEM = S: Em conjunto com o parâmetro EXIBIR_PRECO_UNIT_EMB cria um campo chamado VL. UNIT EMB. que mostra o valor total da embalagem, não o valor unitário dos produtos da embalagem.

</aside>

### Imprimir Boleto no maxPedido

<aside>
💡 EXIBE_LINHA_DIGITAVEL = S: Irá aparecer a linha de boleto na tela de título e ao clicar, gera o arquivo PDF do boleto.

</aside>

### Previsão de Faturamento

<aside>
💡 Parametrização:

OBRIGAR_PREVISAO_FATURAMENTO = N
PRAZO_VALIDADE_PREVISAOFATURAMENTO = 30
PREVISAO_FATURAMENTO_DIA_MAIS_UM = S
CONSIDERAR_DATA_ATUAL_PREV_FAT = N

</aside>

### Combos de Desconto

<aside>
💡

Configuração Geral: https://basedeconhecimento.maximatech.com.br/display/BMX/Como+configurar+Combo+de+Descontos

MIQ https://basedeconhecimento.maximatech.com.br/display/BMX/Como+cadastrar+Campanha+MIQ

SQP https://basedeconhecimento.maximatech.com.br/display/BMX/Como+cadastrar+Campanha+SQP

MQT https://basedeconhecimento.maximatech.com.br/display/BMX/Como+Cadastrar+Campanha+de+Desconto+MQT

FPU https://basedeconhecimento.maximatech.com.br/display/BMX/Como+cadastrar+Campanha+FPU

FPV https://basedeconhecimento.maximatech.com.br/display/BMX/Como+cadastrar+Campanha+FPU

</aside>

### Tabelas de permissões inspect

MXSACESSODADOS → Acesso as permissões da central: cobrançcas/planos de pagamento/filial de venda, etc..

MXSACESSOENTIDADES → Acesso da aba “acessos” das permissões da central de configurações