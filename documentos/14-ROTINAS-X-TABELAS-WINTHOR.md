# WinThor - Rotinas x Tabelas

**Palavras-chave**: WinThor, rotina, tabela, modulo, consulta operacional, consulta tecnica, PCCLIENT, PCUSUARI, PCPEDC, PCPEDI, PCCARREG, PCFILIAL, PCMOV, PCPREST, PCCOB, PCMETASUP, PCPRODUT, PCCOTA

**Sistema**: WinThor

**Area**: Referencia operacional de rotinas e tabelas

---

## Visao geral

Este documento foi normalizado a partir de uma planilha XLSX para uso no RAG deste ambiente.
Cada rotina virou uma secao independente, com indices reversos por referencia tecnica e por modulo para melhorar recuperacao por embeddings e full-text search.

- Aba utilizada: `Rotinas`
- Registros uteis convertidos: `73`
- Registros sem modulo informado: `5`
- Registros sem tabela informada: `4`
- Registros com observacoes: `2`
- Rotinas repetidas na fonte: `1203, 517`

## Criterios de normalizacao

- Campos vazios foram preservados como `Nao informado na planilha`.
- O texto das tabelas foi mantido como veio na fonte e tambem tokenizado para busca reversa.
- Quando uma rotina aparece mais de uma vez, cada linha foi preservada como um registro proprio.
- Nao houve correcao semantica manual dos dados da planilha; o documento prioriza fidelidade a fonte.

## Indice por rotina

### Rotina 111 - Rotina de faturamento

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`
- Referencia tecnica na planilha: `FUNC_RESUMOFATURAMENTO`
- Tabelas e tokens tecnicos normalizados para busca: `FUNC_RESUMOFATURAMENTO`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `2`

Resumo: a rotina `111` (Rotina de faturamento) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE` e referencia `FUNC_RESUMOFATURAMENTO`.

### Rotina 132 - Parâmetro que define média de desconto.

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCPARAMFILIAL / PCFILIAL`
- Tabelas e tokens tecnicos normalizados para busca: `PCPARAMFILIAL`, `PCFILIAL`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `3`

Resumo: a rotina `132` (Parâmetro que define média de desconto.) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCPARAMFILIAL / PCFILIAL`.

### Rotina 146 - Resumo de Vendas

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`
- Referencia tecnica na planilha: `PCMETASUP`
- Tabelas e tokens tecnicos normalizados para busca: `PCMETASUP`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `4`

Resumo: a rotina `146` (Resumo de Vendas) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE` e referencia `PCMETASUP`.

### Rotina 201 - Precificação de produto

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCTABPR`
- Tabelas e tokens tecnicos normalizados para busca: `PCTABPR`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `5`

Resumo: a rotina `201` (Precificação de produto) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCTABPR`.

### Rotina 203 - Cadastrar Produto

- Modulo WinThor: `ROTINAS CADASTROS BÁSICOS`
- Referencia tecnica na planilha: `PCPRODUT`
- Tabelas e tokens tecnicos normalizados para busca: `PCPRODUT`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `6`

Resumo: a rotina `203` (Cadastrar Produto) esta associada ao modulo `ROTINAS CADASTROS BÁSICOS` e referencia `PCPRODUT`.

### Rotina 238 - Manutenção do cadastro de produtos (colocar múltiplo em filiais e etc.)

- Modulo WinThor: `RELACIONAMENTOS DE PRODUTOS`
- Referencia tecnica na planilha: `PCPRODFILIAL`
- Tabelas e tokens tecnicos normalizados para busca: `PCPRODFILIAL`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `7`

Resumo: a rotina `238` (Manutenção do cadastro de produtos (colocar múltiplo em filiais e etc.)) esta associada ao modulo `RELACIONAMENTOS DE PRODUTOS` e referencia `PCPRODFILIAL`.

### Rotina 283 - Cadastrar cotação de Concorrentes

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `PCCOTA`
- Tabelas e tokens tecnicos normalizados para busca: `PCCOTA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `8`

Resumo: a rotina `283` (Cadastrar cotação de Concorrentes) esta associada ao modulo `ROTINAS DE APOIO` e referencia `PCCOTA`.

### Rotina 285 - Analisar Cotação de Concorrentes

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `PCCONCOR / PCCOTA`
- Tabelas e tokens tecnicos normalizados para busca: `PCCONCOR`, `PCCOTA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `9`

Resumo: a rotina `285` (Analisar Cotação de Concorrentes) esta associada ao modulo `ROTINAS DE APOIO` e referencia `PCCONCOR / PCCOTA`.

### Rotina 292 - Cadastrar embalagem

- Modulo WinThor: `ROTINAS CADASTROS BÁSICOS`
- Referencia tecnica na planilha: `PCEMBALAGEM`
- Tabelas e tokens tecnicos normalizados para busca: `PCEMBALAGEM`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `10`

Resumo: a rotina `292` (Cadastrar embalagem) esta associada ao modulo `ROTINAS CADASTROS BÁSICOS` e referencia `PCEMBALAGEM`.

### Rotina 297 - Produtos Similares

- Modulo WinThor: `RELACIONAMENTOS DE PRODUTOS`
- Referencia tecnica na planilha: `PCPRODSIMIL`
- Tabelas e tokens tecnicos normalizados para busca: `PCPRODSIMIL`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `11`

Resumo: a rotina `297` (Produtos Similares) esta associada ao modulo `RELACIONAMENTOS DE PRODUTOS` e referencia `PCPRODSIMIL`.

### Rotina 301 - Autorizar Preço de Venda

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCAUTORI`
- Tabelas e tokens tecnicos normalizados para busca: `PCAUTORI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `12`

Resumo: a rotina `301` (Autorizar Preço de Venda) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCAUTORI`.

### Rotina 302 - Cadastrar de clientes

- Modulo WinThor: `Cadastrar de clientes`
- Referencia tecnica na planilha: `PCCLIENT`
- Tabelas e tokens tecnicos normalizados para busca: `PCCLIENT`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `13`

Resumo: a rotina `302` (Cadastrar de clientes) esta associada ao modulo `Cadastrar de clientes` e referencia `PCCLIENT`.

### Rotina 303 - Acompanhar Meta x Venda

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencia tecnica na planilha: `PCMETARCA`
- Tabelas e tokens tecnicos normalizados para busca: `PCMETARCA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `14`

Resumo: a rotina `303` (Acompanhar Meta x Venda) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)` e referencia `PCMETARCA`.

### Rotina 304 - cadastro de cotas por RCA

- Modulo WinThor: `Nao informado na planilha`
- Referencia tecnica na planilha: `PCPRODUSUR`
- Tabelas e tokens tecnicos normalizados para busca: `PCPRODUSUR`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `74`

Resumo: a rotina `304` (cadastro de cotas por RCA) esta associada ao modulo `Nao informado na planilha` e referencia `PCPRODUSUR`.

### Rotina 308 - Alterar condição especial do cliente

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCPLPAGCLI`
- Tabelas e tokens tecnicos normalizados para busca: `PCPLPAGCLI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `15`

Resumo: a rotina `308` (Alterar condição especial do cliente) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCPLPAGCLI`.

### Rotina 309 - Cadastrar dias úteis de venda Produto

- Modulo WinThor: `ROTINAS CADASTROS BÁSICOS`
- Referencia tecnica na planilha: `PCDATAS`
- Tabelas e tokens tecnicos normalizados para busca: `PCDATAS`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `16`

Resumo: a rotina `309` (Cadastrar dias úteis de venda Produto) esta associada ao modulo `ROTINAS CADASTROS BÁSICOS` e referencia `PCDATAS`.

### Rotina 311 - Extrato, saldo do RCA

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`
- Referencia tecnica na planilha: `PCLOGRCA.VLCORRENTE / PCLOGRCA.VLCORRENTEANT`
- Tabelas e tokens tecnicos normalizados para busca: `PCLOGRCA.VLCORRENTE`, `PCLOGRCA.VLCORRENTEANT`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `17`

Resumo: a rotina `311` (Extrato, saldo do RCA) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE` e referencia `PCLOGRCA.VLCORRENTE / PCLOGRCA.VLCORRENTEANT`.

### Rotina 313 - Cliente por RCA

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES`
- Referencia tecnica na planilha: `PCUSUARI / PCCLIENT`
- Tabelas e tokens tecnicos normalizados para busca: `PCUSUARI`, `PCCLIENT`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `18`

Resumo: a rotina `313` (Cliente por RCA) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES` e referencia `PCUSUARI / PCCLIENT`.

### Rotina 317 - Imprimir Pedido

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCPEDC / PCPEDI / PCMOV`
- Tabelas e tokens tecnicos normalizados para busca: `PCPEDC`, `PCPEDI`, `PCMOV`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `19`

Resumo: a rotina `317` (Imprimir Pedido) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCPEDC / PCPEDI / PCMOV`.

### Rotina 318 - Enviar Mensagem para RCA

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `PCMENS`
- Tabelas e tokens tecnicos normalizados para busca: `PCMENS`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `20`

Resumo: a rotina `318` (Enviar Mensagem para RCA) esta associada ao modulo `ROTINAS DE APOIO` e referencia `PCMENS`.

### Rotina 322 - Venda Por Departamento

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencia tecnica na planilha: `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`
- Tabelas e tokens tecnicos normalizados para busca: `PCPEDC`, `PCPEDI`, `PCCLIENT`, `PCUSUARI`, `PCDEPTO`, `PCSEC`, `PCFORNEC`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `21`

Resumo: a rotina `322` (Venda Por Departamento) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)` e referencia `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`.

### Rotina 329 - Cancelamento do Pedido de Vendas

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCNFCANITEM / PCNFCAN`
- Tabelas e tokens tecnicos normalizados para busca: `PCNFCANITEM`, `PCNFCAN`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `22`

Resumo: a rotina `329` (Cancelamento do Pedido de Vendas) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCNFCANITEM / PCNFCAN`.

### Rotina 335 - Consultar Pedido de Venda

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCPEDC / PCPEDI`
- Tabelas e tokens tecnicos normalizados para busca: `PCPEDC`, `PCPEDI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `23`

Resumo: a rotina `335` (Consultar Pedido de Venda) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCPEDC / PCPEDI`.

### Rotina 336 - Alterar Pedido de Vendas

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCVISITA`
- Tabelas e tokens tecnicos normalizados para busca: `PCVISITA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `24`

Resumo: a rotina `336` (Alterar Pedido de Vendas) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCVISITA`.

### Rotina 344 - Consultar Visita

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES (Roteirização)`
- Referencia tecnica na planilha: `Nao informado na planilha`
- Tabelas e tokens tecnicos normalizados para busca: Nao informado na planilha
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `25`

Resumo: a rotina `344` (Consultar Visita) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES (Roteirização)` e referencia `Nao informado na planilha`.

### Rotina 349 - Cadastrar Brindes

- Modulo WinThor: `RELACIONAMENTOS DE PRODUTOS`
- Referencia tecnica na planilha: `PCPROMC / PCPROMI`
- Tabelas e tokens tecnicos normalizados para busca: `PCPROMC`, `PCPROMI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `26`

Resumo: a rotina `349` (Cadastrar Brindes) esta associada ao modulo `RELACIONAMENTOS DE PRODUTOS` e referencia `PCPROMC / PCPROMI`.

### Rotina 353 - Cadastrar Meta Diária por RCA (valor)

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencia tecnica na planilha: `PCMETASUP / PCMETARCA`
- Tabelas e tokens tecnicos normalizados para busca: `PCMETASUP`, `PCMETARCA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `27`

Resumo: a rotina `353` (Cadastrar Meta Diária por RCA (valor)) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)` e referencia `PCMETASUP / PCMETARCA`.

### Rotina 354 - Cadastrar Rota de Visita e Cliente

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES (Roteirização)`
- Referencia tecnica na planilha: `PCROTACLI`
- Tabelas e tokens tecnicos normalizados para busca: `PCROTACLI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `28`

Resumo: a rotina `354` (Cadastrar Rota de Visita e Cliente) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES (Roteirização)` e referencia `PCROTACLI`.

### Rotina 356 - Wizard de conta-corrente de RCA

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`
- Referencia tecnica na planilha: `pc_pkg_controlarsaldorca (PCUSUARI)`
- Tabelas e tokens tecnicos normalizados para busca: `PC_PKG_CONTROLARSALDORCA`, `PCUSUARI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `29`

Resumo: a rotina `356` (Wizard de conta-corrente de RCA) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE` e referencia `pc_pkg_controlarsaldorca (PCUSUARI)`.

### Rotina 357 - Cadastro preço fixo

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCPRECOPROM`
- Tabelas e tokens tecnicos normalizados para busca: `PCPRECOPROM`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `30`

Resumo: a rotina `357` (Cadastro preço fixo) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCPRECOPROM`.

### Rotina 382 - Duplicar pedido de venda

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCPEDC / PCPEDI`
- Tabelas e tokens tecnicos normalizados para busca: `PCPEDC`, `PCPEDI`
- Observacoes: `(ROTINA DESCONTINUADA USAR A 316)`
- Linha original na planilha: `31`

Resumo: a rotina `382` (Duplicar pedido de venda) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCPEDC / PCPEDI`.

### Rotina 385 - Roteiro de visitas (cadastro de rotas)

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES (Roteirização)`
- Referencia tecnica na planilha: `PCROTACLIFIXAC / PCROTACLIFIXAI`
- Tabelas e tokens tecnicos normalizados para busca: `PCROTACLIFIXAC`, `PCROTACLIFIXAI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `32`

Resumo: a rotina `385` (Roteiro de visitas (cadastro de rotas)) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES (Roteirização)` e referencia `PCROTACLIFIXAC / PCROTACLIFIXAI`.

### Rotina 387 - Desconto por quantidade

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCDESCQUANT`
- Tabelas e tokens tecnicos normalizados para busca: `PCDESCQUANT`
- Observacoes: `(ROTINA DESCONTINUADA - USAR A 561)`
- Linha original na planilha: `33`

Resumo: a rotina `387` (Desconto por quantidade) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCDESCQUANT`.

### Rotina 391 - Restrição de venda

- Modulo WinThor: `RELACIONAMENTOS DE PRODUTOS`
- Referencia tecnica na planilha: `PCRESTRICAOVENDA`
- Tabelas e tokens tecnicos normalizados para busca: `PCRESTRICAOVENDA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `34`

Resumo: a rotina `391` (Restrição de venda) esta associada ao modulo `RELACIONAMENTOS DE PRODUTOS` e referencia `PCRESTRICAOVENDA`.

### Rotina 399 - Gerar Meta Mensal (Fornecedor - Sessão - Produto - Cliente)

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencia tecnica na planilha: `PCMETA`
- Tabelas e tokens tecnicos normalizados para busca: `PCMETA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `35`

Resumo: a rotina `399` (Gerar Meta Mensal (Fornecedor - Sessão - Produto - Cliente)) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)` e referencia `PCMETA`.

### Rotina 407 - Rel. Fechamento de Carga

- Modulo WinThor: `PRONTA ENTREGA`
- Referencia tecnica na planilha: `PCPREST / PCCLIENT / PCCOB,/ PCMOVCR`
- Tabelas e tokens tecnicos normalizados para busca: `PCPREST`, `PCCLIENT`, `PCCOB`, `PCMOVCR`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `36`

Resumo: a rotina `407` (Rel. Fechamento de Carga) esta associada ao modulo `PRONTA ENTREGA` e referencia `PCPREST / PCCLIENT / PCCOB,/ PCMOVCR`.

### Rotina 410 - Acertos

- Modulo WinThor: `PRONTA ENTREGA`
- Referencia tecnica na planilha: `PCCARREG / PCVEICUL`
- Tabelas e tokens tecnicos normalizados para busca: `PCCARREG`, `PCVEICUL`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `37`

Resumo: a rotina `410` (Acertos) esta associada ao modulo `PRONTA ENTREGA` e referencia `PCCARREG / PCVEICUL`.

### Rotina 417 - Mapa de Acerto

- Modulo WinThor: `PRONTA ENTREGA`
- Referencia tecnica na planilha: `PCMOV / PCNFSAID / PCPRODUT`
- Tabelas e tokens tecnicos normalizados para busca: `PCMOV`, `PCNFSAID`, `PCPRODUT`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `38`

Resumo: a rotina `417` (Mapa de Acerto) esta associada ao modulo `PRONTA ENTREGA` e referencia `PCMOV / PCNFSAID / PCPRODUT`.

### Rotina 505 - Relacionar fornecedor por RCA

- Modulo WinThor: `RELACIONAMENTOS DE PRODUTOS`
- Referencia tecnica na planilha: `PCUSURFORNEC`
- Tabelas e tokens tecnicos normalizados para busca: `PCUSURFORNEC`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `39`

Resumo: a rotina `505` (Relacionar fornecedor por RCA) esta associada ao modulo `RELACIONAMENTOS DE PRODUTOS` e referencia `PCUSURFORNEC`.

### Rotina 514 - Cadastro do tipo de tributação (acréscimo na tabela de pessoa física)

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCTRIBUTPARTILHA`
- Tabelas e tokens tecnicos normalizados para busca: `PCTRIBUTPARTILHA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `40`

Resumo: a rotina `514` (Cadastro do tipo de tributação (acréscimo na tabela de pessoa física)) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCTRIBUTPARTILHA`.

### Rotina 516 - Cadastrar Supervisor

- Modulo WinThor: `ROTINAS CADASTROS BÁSICOS`
- Referencia tecnica na planilha: `PCSUPERV`
- Tabelas e tokens tecnicos normalizados para busca: `PCSUPERV`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `41`

Resumo: a rotina `516` (Cadastrar Supervisor) esta associada ao modulo `ROTINAS CADASTROS BÁSICOS` e referencia `PCSUPERV`.

### Rotina 517 - Cadastrar RCA

- Modulo WinThor: `ROTINAS CADASTROS BÁSICOS`
- Referencia tecnica na planilha: `PCUSUARI`
- Tabelas e tokens tecnicos normalizados para busca: `PCUSUARI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `42`

Resumo: a rotina `517` (Cadastrar RCA) esta associada ao modulo `ROTINAS CADASTROS BÁSICOS` e referencia `PCUSUARI`.

### Rotina 517 - Cadastro RCA (Percentual Acréscimo/Desconto)

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCUSUARI`
- Tabelas e tokens tecnicos normalizados para busca: `PCUSUARI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `43`

Resumo: a rotina `517` (Cadastro RCA (Percentual Acréscimo/Desconto)) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCUSUARI`.

### Rotina 522 - Cadastrar tipo de cobrança

- Modulo WinThor: `ROTINAS CADASTROS BÁSICOS`
- Referencia tecnica na planilha: `PCCOB`
- Tabelas e tokens tecnicos normalizados para busca: `PCCOB`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `44`

Resumo: a rotina `522` (Cadastrar tipo de cobrança) esta associada ao modulo `ROTINAS CADASTROS BÁSICOS` e referencia `PCCOB`.

### Rotina 523 - Cadastrar plano de pagamento

- Modulo WinThor: `ROTINAS CADASTROS BÁSICOS`
- Referencia tecnica na planilha: `PCPLPAG`
- Tabelas e tokens tecnicos normalizados para busca: `PCPLPAG`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `45`

Resumo: a rotina `523` (Cadastrar plano de pagamento) esta associada ao modulo `ROTINAS CADASTROS BÁSICOS` e referencia `PCPLPAG`.

### Rotina 528 - Cadastro de novos destinatários p/ envio de mensagem

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `PCEMPR`
- Tabelas e tokens tecnicos normalizados para busca: `PCEMPR`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `46`

Resumo: a rotina `528` (Cadastro de novos destinatários p/ envio de mensagem) esta associada ao modulo `ROTINAS DE APOIO` e referencia `PCEMPR`.

### Rotina 530 - Permissões de acessos para cada usuário (usuário 8888)

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `Nao informado na planilha`
- Tabelas e tokens tecnicos normalizados para busca: Nao informado na planilha
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `47`

Resumo: a rotina `530` (Permissões de acessos para cada usuário (usuário 8888)) esta associada ao modulo `ROTINAS DE APOIO` e referencia `Nao informado na planilha`.

### Rotina 535 - Cadastrar Filiais

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `PCFILIAL`
- Tabelas e tokens tecnicos normalizados para busca: `PCFILIAL`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `48`

Resumo: a rotina `535` (Cadastrar Filiais) esta associada ao modulo `ROTINAS DE APOIO` e referencia `PCFILIAL`.

### Rotina 561 - Cadastrar política de Desconto

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCDESCONTO`
- Tabelas e tokens tecnicos normalizados para busca: `PCDESCONTO`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `49`

Resumo: a rotina `561` (Cadastrar política de Desconto) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCDESCONTO`.

### Rotina 574 - Cadastrar tributação nos produtos

- Modulo WinThor: `RELACIONAMENTOS DE PRODUTOS`
- Referencia tecnica na planilha: `PCTRIBUT`
- Tabelas e tokens tecnicos normalizados para busca: `PCTRIBUT`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `50`

Resumo: a rotina `574` (Cadastrar tributação nos produtos) esta associada ao modulo `RELACIONAMENTOS DE PRODUTOS` e referencia `PCTRIBUT`.

### Rotina 577 - Cadastrar Cidades e código IBGE

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES`
- Referencia tecnica na planilha: `PCMOTNAOCOMPRA`
- Tabelas e tokens tecnicos normalizados para busca: `PCMOTNAOCOMPRA`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `51`

Resumo: a rotina `577` (Cadastrar Cidades e código IBGE) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES` e referencia `PCMOTNAOCOMPRA`.

### Rotina 578 - Cadastrar Motivo de Não Compra

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES (Roteirização)`
- Referencia tecnica na planilha: `Nao informado na planilha`
- Tabelas e tokens tecnicos normalizados para busca: Nao informado na planilha
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `52`

Resumo: a rotina `578` (Cadastrar Motivo de Não Compra) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES (Roteirização)` e referencia `Nao informado na planilha`.

### Rotina 586 - Relacionamento Cliente X RCA

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES`
- Referencia tecnica na planilha: `PCUSURCLI`
- Tabelas e tokens tecnicos normalizados para busca: `PCUSURCLI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `53`

Resumo: a rotina `586` (Relacionamento Cliente X RCA) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES` e referencia `PCUSURCLI`.

### Rotina 587 - Cadastrar Relacionamento de rca departamento e seção

- Modulo WinThor: `RELACIONAMENTOS DE PRODUTOS`
- Referencia tecnica na planilha: `PCUSURDEPSEC`
- Tabelas e tokens tecnicos normalizados para busca: `PCUSURDEPSEC`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `54`

Resumo: a rotina `587` (Cadastrar Relacionamento de rca departamento e seção) esta associada ao modulo `RELACIONAMENTOS DE PRODUTOS` e referencia `PCUSURDEPSEC`.

### Rotina 901 - Montar carga

- Modulo WinThor: `Nao informado na planilha`
- Referencia tecnica na planilha: `PCCARREG`
- Tabelas e tokens tecnicos normalizados para busca: `PCCARREG`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `55`

Resumo: a rotina `901` (Montar carga) esta associada ao modulo `Nao informado na planilha` e referencia `PCCARREG`.

### Rotina 904 - Cancelamento de carga

- Modulo WinThor: `Nao informado na planilha`
- Referencia tecnica na planilha: `PCCARREG`
- Tabelas e tokens tecnicos normalizados para busca: `PCCARREG`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `56`

Resumo: a rotina `904` (Cancelamento de carga) esta associada ao modulo `Nao informado na planilha` e referencia `PCCARREG`.

### Rotina 905 - Transferência de NFs do carregamento

- Modulo WinThor: `Nao informado na planilha`
- Referencia tecnica na planilha: `PCNFSAID`
- Tabelas e tokens tecnicos normalizados para busca: `PCNFSAID`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `57`

Resumo: a rotina `905` (Transferência de NFs do carregamento) esta associada ao modulo `Nao informado na planilha` e referencia `PCNFSAID`.

### Rotina 1203 - Extrato do cliente

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCPREST`
- Tabelas e tokens tecnicos normalizados para busca: `PCPREST`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `58`

Resumo: a rotina `1203` (Extrato do cliente) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCPREST`.

### Rotina 1203 - Tipo de cobrança, venda, plano padrão

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES`
- Referencia tecnica na planilha: `PCCOBCLI`
- Tabelas e tokens tecnicos normalizados para busca: `PCCOBCLI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `59`

Resumo: a rotina `1203` (Tipo de cobrança, venda, plano padrão) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES` e referencia `PCCOBCLI`.

### Rotina 1213 - Títulos

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `PCPREST / PCCLIENT / PCCOB / PCFILIAL`
- Tabelas e tokens tecnicos normalizados para busca: `PCPREST`, `PCCLIENT`, `PCCOB`, `PCFILIAL`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `60`

Resumo: a rotina `1213` (Títulos) esta associada ao modulo `ROTINAS DE APOIO` e referencia `PCPREST / PCCLIENT / PCCOB / PCFILIAL`.

### Rotina 1332 - Devolução pronta entrega (manifesto)

- Modulo WinThor: `PRONTA ENTREGA`
- Referencia tecnica na planilha: `PCTABDEV / PCNFBASE / PCMOV / PCNFENT`
- Tabelas e tokens tecnicos normalizados para busca: `PCTABDEV`, `PCNFBASE`, `PCMOV`, `PCNFENT`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `61`

Resumo: a rotina `1332` (Devolução pronta entrega (manifesto)) esta associada ao modulo `PRONTA ENTREGA` e referencia `PCTABDEV / PCNFBASE / PCMOV / PCNFENT`.

### Rotina 1402 - Gerar Faturamento

- Modulo WinThor: `PRONTA ENTREGA`
- Referencia tecnica na planilha: `PCCARREG`
- Tabelas e tokens tecnicos normalizados para busca: `PCCARREG`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `62`

Resumo: a rotina `1402` (Gerar Faturamento) esta associada ao modulo `PRONTA ENTREGA` e referencia `PCCARREG`.

### Rotina 2014 - Cadastrar embalagem (auto-serviço)

- Modulo WinThor: `ROTINAS CADASTROS BÁSICOS`
- Referencia tecnica na planilha: `PCEMBALAGEM`
- Tabelas e tokens tecnicos normalizados para busca: `PCEMBALAGEM`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `63`

Resumo: a rotina `2014` (Cadastrar embalagem (auto-serviço)) esta associada ao modulo `ROTINAS CADASTROS BÁSICOS` e referencia `PCEMBALAGEM`.

### Rotina 2316 - Digitar Pedido de Venda (medicamentos)

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `Nao informado na planilha`
- Tabelas e tokens tecnicos normalizados para busca: Nao informado na planilha
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `64`

Resumo: a rotina `2316` (Digitar Pedido de Venda (medicamentos)) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `Nao informado na planilha`.

### Rotina 2323 - Cadastrar Promoção (Módulo Medicamentos)

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCPROMOCAOMED`
- Tabelas e tokens tecnicos normalizados para busca: `PCPROMOCAOMED`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `65`

Resumo: a rotina `2323` (Cadastrar Promoção (Módulo Medicamentos)) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCPROMOCAOMED`.

### Rotina 2500 - INTEGRADORA, APURARCAMPANHASBRINDES

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES , PROCEDURES , TRIGGERS, VIEWS`
- Tabelas e tokens tecnicos normalizados para busca: `PCRETORNOIMPORTARVENDAS`, `PACKAGES`, `FUNCOES`, `PROCEDURES`, `TRIGGERS`, `VIEWS`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `66`

Resumo: a rotina `2500` (INTEGRADORA, APURARCAMPANHASBRINDES) esta associada ao modulo `ROTINAS DE APOIO` e referencia `PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES , PROCEDURES , TRIGGERS, VIEWS`.

### Rotina 3305 - Cadastrar Meta Mensal

- Modulo WinThor: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencia tecnica na planilha: `PCMETA / PCMETAC`
- Tabelas e tokens tecnicos normalizados para busca: `PCMETA`, `PCMETAC`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `67`

Resumo: a rotina `3305` (Cadastrar Meta Mensal) esta associada ao modulo `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)` e referencia `PCMETA / PCMETAC`.

### Rotina 3306 - Cadastrar campanha de desconto para Força de Vendas * (Com exceção Restrição por plano de pagamento)

- Modulo WinThor: `CONFECÇÃO DE PEDIDOS`
- Referencia tecnica na planilha: `PCDESCONTOC / PCDESCONTOI / PCDESCONTORESTRICAO`
- Tabelas e tokens tecnicos normalizados para busca: `PCDESCONTOC`, `PCDESCONTOI`, `PCDESCONTORESTRICAO`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `68`

Resumo: a rotina `3306` (Cadastrar campanha de desconto para Força de Vendas * (Com exceção Restrição por plano de pagamento)) esta associada ao modulo `CONFECÇÃO DE PEDIDOS` e referencia `PCDESCONTOC / PCDESCONTOI / PCDESCONTORESTRICAO`.

### Rotina 3307 - Cadastrar Cesta básica

- Modulo WinThor: `RELACIONAMENTOS DE PRODUTOS`
- Referencia tecnica na planilha: `PCFORMPROD`
- Tabelas e tokens tecnicos normalizados para busca: `PCFORMPROD`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `69`

Resumo: a rotina `3307` (Cadastrar Cesta básica) esta associada ao modulo `RELACIONAMENTOS DE PRODUTOS` e referencia `PCFORMPROD`.

### Rotina 3314 - Cadastrar Tab. De Preço Utilizada Pelo Cli

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES`
- Referencia tecnica na planilha: `PCTABPRCLI`
- Tabelas e tokens tecnicos normalizados para busca: `PCTABPRCLI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `70`

Resumo: a rotina `3314` (Cadastrar Tab. De Preço Utilizada Pelo Cli) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES` e referencia `PCTABPRCLI`.

### Rotina 3315 - Cadastro de RCA por Cliente

- Modulo WinThor: `RELACIONAMENTOS DE CLIENTES`
- Referencia tecnica na planilha: `PCUSURCLI`
- Tabelas e tokens tecnicos normalizados para busca: `PCUSURCLI`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `71`

Resumo: a rotina `3315` (Cadastro de RCA por Cliente) esta associada ao modulo `RELACIONAMENTOS DE CLIENTES` e referencia `PCUSURCLI`.

### Rotina 3320 - Cadastro de brinde Express

- Modulo WinThor: `Nao informado na planilha`
- Referencia tecnica na planilha: `PCBRINDEEX`
- Tabelas e tokens tecnicos normalizados para busca: `PCBRINDEEX`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `72`

Resumo: a rotina `3320` (Cadastro de brinde Express) esta associada ao modulo `Nao informado na planilha` e referencia `PCBRINDEEX`.

### Rotina 3329 - Cadastro de tipos de Bonificações

- Modulo WinThor: `ROTINAS DE APOIO`
- Referencia tecnica na planilha: `PCTIPOBONIFIC`
- Tabelas e tokens tecnicos normalizados para busca: `PCTIPOBONIFIC`
- Observacoes: `Nao informado na planilha`
- Linha original na planilha: `73`

Resumo: a rotina `3329` (Cadastro de tipos de Bonificações) esta associada ao modulo `ROTINAS DE APOIO` e referencia `PCTIPOBONIFIC`.

## Indice reverso por referencia tecnica

### Referencia tecnica FUNCOES

- Rotinas relacionadas: `2500 - INTEGRADORA, APURARCAMPANHASBRINDES`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES , PROCEDURES , TRIGGERS, VIEWS`

Resumo: a referencia tecnica `FUNCOES` aparece nas rotinas 2500.

### Referencia tecnica FUNC_RESUMOFATURAMENTO

- Rotinas relacionadas: `111 - Rotina de faturamento`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`
- Referencias originais da planilha: `FUNC_RESUMOFATURAMENTO`

Resumo: a referencia tecnica `FUNC_RESUMOFATURAMENTO` aparece nas rotinas 111.

### Referencia tecnica PACKAGES

- Rotinas relacionadas: `2500 - INTEGRADORA, APURARCAMPANHASBRINDES`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES , PROCEDURES , TRIGGERS, VIEWS`

Resumo: a referencia tecnica `PACKAGES` aparece nas rotinas 2500.

### Referencia tecnica PCAUTORI

- Rotinas relacionadas: `301 - Autorizar Preço de Venda`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCAUTORI`

Resumo: a referencia tecnica `PCAUTORI` aparece nas rotinas 301.

### Referencia tecnica PCBRINDEEX

- Rotinas relacionadas: `3320 - Cadastro de brinde Express`
- Modulos relacionados: `Nao informado na planilha`
- Referencias originais da planilha: `PCBRINDEEX`

Resumo: a referencia tecnica `PCBRINDEEX` aparece nas rotinas 3320.

### Referencia tecnica PCCARREG

- Rotinas relacionadas: `410 - Acertos`; `901 - Montar carga`; `904 - Cancelamento de carga`; `1402 - Gerar Faturamento`
- Modulos relacionados: `Nao informado na planilha`, `PRONTA ENTREGA`
- Referencias originais da planilha: `PCCARREG`, `PCCARREG / PCVEICUL`

Resumo: a referencia tecnica `PCCARREG` aparece nas rotinas 410, 901, 904, 1402.

### Referencia tecnica PCCLIENT

- Rotinas relacionadas: `302 - Cadastrar de clientes`; `313 - Cliente por RCA`; `322 - Venda Por Departamento`; `407 - Rel. Fechamento de Carga`; `1213 - Títulos`
- Modulos relacionados: `Cadastrar de clientes`, `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`, `PRONTA ENTREGA`, `RELACIONAMENTOS DE CLIENTES`, `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCCLIENT`, `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`, `PCPREST / PCCLIENT / PCCOB / PCFILIAL`, `PCPREST / PCCLIENT / PCCOB,/ PCMOVCR`, `PCUSUARI / PCCLIENT`

Resumo: a referencia tecnica `PCCLIENT` aparece nas rotinas 302, 313, 322, 407, 1213.

### Referencia tecnica PCCOB

- Rotinas relacionadas: `407 - Rel. Fechamento de Carga`; `522 - Cadastrar tipo de cobrança`; `1213 - Títulos`
- Modulos relacionados: `PRONTA ENTREGA`, `ROTINAS CADASTROS BÁSICOS`, `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCCOB`, `PCPREST / PCCLIENT / PCCOB / PCFILIAL`, `PCPREST / PCCLIENT / PCCOB,/ PCMOVCR`

Resumo: a referencia tecnica `PCCOB` aparece nas rotinas 407, 522, 1213.

### Referencia tecnica PCCOBCLI

- Rotinas relacionadas: `1203 - Tipo de cobrança, venda, plano padrão`
- Modulos relacionados: `RELACIONAMENTOS DE CLIENTES`
- Referencias originais da planilha: `PCCOBCLI`

Resumo: a referencia tecnica `PCCOBCLI` aparece nas rotinas 1203.

### Referencia tecnica PCCONCOR

- Rotinas relacionadas: `285 - Analisar Cotação de Concorrentes`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCCONCOR / PCCOTA`

Resumo: a referencia tecnica `PCCONCOR` aparece nas rotinas 285.

### Referencia tecnica PCCOTA

- Rotinas relacionadas: `283 - Cadastrar cotação de Concorrentes`; `285 - Analisar Cotação de Concorrentes`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCCONCOR / PCCOTA`, `PCCOTA`

Resumo: a referencia tecnica `PCCOTA` aparece nas rotinas 283, 285.

### Referencia tecnica PCDATAS

- Rotinas relacionadas: `309 - Cadastrar dias úteis de venda Produto`
- Modulos relacionados: `ROTINAS CADASTROS BÁSICOS`
- Referencias originais da planilha: `PCDATAS`

Resumo: a referencia tecnica `PCDATAS` aparece nas rotinas 309.

### Referencia tecnica PCDEPTO

- Rotinas relacionadas: `322 - Venda Por Departamento`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`

Resumo: a referencia tecnica `PCDEPTO` aparece nas rotinas 322.

### Referencia tecnica PCDESCONTO

- Rotinas relacionadas: `561 - Cadastrar política de Desconto`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCDESCONTO`

Resumo: a referencia tecnica `PCDESCONTO` aparece nas rotinas 561.

### Referencia tecnica PCDESCONTOC

- Rotinas relacionadas: `3306 - Cadastrar campanha de desconto para Força de Vendas * (Com exceção Restrição por plano de pagamento)`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCDESCONTOC / PCDESCONTOI / PCDESCONTORESTRICAO`

Resumo: a referencia tecnica `PCDESCONTOC` aparece nas rotinas 3306.

### Referencia tecnica PCDESCONTOI

- Rotinas relacionadas: `3306 - Cadastrar campanha de desconto para Força de Vendas * (Com exceção Restrição por plano de pagamento)`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCDESCONTOC / PCDESCONTOI / PCDESCONTORESTRICAO`

Resumo: a referencia tecnica `PCDESCONTOI` aparece nas rotinas 3306.

### Referencia tecnica PCDESCONTORESTRICAO

- Rotinas relacionadas: `3306 - Cadastrar campanha de desconto para Força de Vendas * (Com exceção Restrição por plano de pagamento)`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCDESCONTOC / PCDESCONTOI / PCDESCONTORESTRICAO`

Resumo: a referencia tecnica `PCDESCONTORESTRICAO` aparece nas rotinas 3306.

### Referencia tecnica PCDESCQUANT

- Rotinas relacionadas: `387 - Desconto por quantidade`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCDESCQUANT`

Resumo: a referencia tecnica `PCDESCQUANT` aparece nas rotinas 387.

### Referencia tecnica PCEMBALAGEM

- Rotinas relacionadas: `292 - Cadastrar embalagem`; `2014 - Cadastrar embalagem (auto-serviço)`
- Modulos relacionados: `ROTINAS CADASTROS BÁSICOS`
- Referencias originais da planilha: `PCEMBALAGEM`

Resumo: a referencia tecnica `PCEMBALAGEM` aparece nas rotinas 292, 2014.

### Referencia tecnica PCEMPR

- Rotinas relacionadas: `528 - Cadastro de novos destinatários p/ envio de mensagem`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCEMPR`

Resumo: a referencia tecnica `PCEMPR` aparece nas rotinas 528.

### Referencia tecnica PCFILIAL

- Rotinas relacionadas: `132 - Parâmetro que define média de desconto.`; `535 - Cadastrar Filiais`; `1213 - Títulos`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`, `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCFILIAL`, `PCPARAMFILIAL / PCFILIAL`, `PCPREST / PCCLIENT / PCCOB / PCFILIAL`

Resumo: a referencia tecnica `PCFILIAL` aparece nas rotinas 132, 535, 1213.

### Referencia tecnica PCFORMPROD

- Rotinas relacionadas: `3307 - Cadastrar Cesta básica`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCFORMPROD`

Resumo: a referencia tecnica `PCFORMPROD` aparece nas rotinas 3307.

### Referencia tecnica PCFORNEC

- Rotinas relacionadas: `322 - Venda Por Departamento`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`

Resumo: a referencia tecnica `PCFORNEC` aparece nas rotinas 322.

### Referencia tecnica PCLOGRCA.VLCORRENTE

- Rotinas relacionadas: `311 - Extrato, saldo do RCA`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`
- Referencias originais da planilha: `PCLOGRCA.VLCORRENTE / PCLOGRCA.VLCORRENTEANT`

Resumo: a referencia tecnica `PCLOGRCA.VLCORRENTE` aparece nas rotinas 311.

### Referencia tecnica PCLOGRCA.VLCORRENTEANT

- Rotinas relacionadas: `311 - Extrato, saldo do RCA`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`
- Referencias originais da planilha: `PCLOGRCA.VLCORRENTE / PCLOGRCA.VLCORRENTEANT`

Resumo: a referencia tecnica `PCLOGRCA.VLCORRENTEANT` aparece nas rotinas 311.

### Referencia tecnica PCMENS

- Rotinas relacionadas: `318 - Enviar Mensagem para RCA`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCMENS`

Resumo: a referencia tecnica `PCMENS` aparece nas rotinas 318.

### Referencia tecnica PCMETA

- Rotinas relacionadas: `399 - Gerar Meta Mensal (Fornecedor - Sessão - Produto - Cliente)`; `3305 - Cadastrar Meta Mensal`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCMETA`, `PCMETA / PCMETAC`

Resumo: a referencia tecnica `PCMETA` aparece nas rotinas 399, 3305.

### Referencia tecnica PCMETAC

- Rotinas relacionadas: `3305 - Cadastrar Meta Mensal`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCMETA / PCMETAC`

Resumo: a referencia tecnica `PCMETAC` aparece nas rotinas 3305.

### Referencia tecnica PCMETARCA

- Rotinas relacionadas: `303 - Acompanhar Meta x Venda`; `353 - Cadastrar Meta Diária por RCA (valor)`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCMETARCA`, `PCMETASUP / PCMETARCA`

Resumo: a referencia tecnica `PCMETARCA` aparece nas rotinas 303, 353.

### Referencia tecnica PCMETASUP

- Rotinas relacionadas: `146 - Resumo de Vendas`; `353 - Cadastrar Meta Diária por RCA (valor)`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`, `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCMETASUP`, `PCMETASUP / PCMETARCA`

Resumo: a referencia tecnica `PCMETASUP` aparece nas rotinas 146, 353.

### Referencia tecnica PCMOTNAOCOMPRA

- Rotinas relacionadas: `577 - Cadastrar Cidades e código IBGE`
- Modulos relacionados: `RELACIONAMENTOS DE CLIENTES`
- Referencias originais da planilha: `PCMOTNAOCOMPRA`

Resumo: a referencia tecnica `PCMOTNAOCOMPRA` aparece nas rotinas 577.

### Referencia tecnica PCMOV

- Rotinas relacionadas: `317 - Imprimir Pedido`; `417 - Mapa de Acerto`; `1332 - Devolução pronta entrega (manifesto)`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`, `PRONTA ENTREGA`
- Referencias originais da planilha: `PCMOV / PCNFSAID / PCPRODUT`, `PCPEDC / PCPEDI / PCMOV`, `PCTABDEV / PCNFBASE / PCMOV / PCNFENT`

Resumo: a referencia tecnica `PCMOV` aparece nas rotinas 317, 417, 1332.

### Referencia tecnica PCMOVCR

- Rotinas relacionadas: `407 - Rel. Fechamento de Carga`
- Modulos relacionados: `PRONTA ENTREGA`
- Referencias originais da planilha: `PCPREST / PCCLIENT / PCCOB,/ PCMOVCR`

Resumo: a referencia tecnica `PCMOVCR` aparece nas rotinas 407.

### Referencia tecnica PCNFBASE

- Rotinas relacionadas: `1332 - Devolução pronta entrega (manifesto)`
- Modulos relacionados: `PRONTA ENTREGA`
- Referencias originais da planilha: `PCTABDEV / PCNFBASE / PCMOV / PCNFENT`

Resumo: a referencia tecnica `PCNFBASE` aparece nas rotinas 1332.

### Referencia tecnica PCNFCAN

- Rotinas relacionadas: `329 - Cancelamento do Pedido de Vendas`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCNFCANITEM / PCNFCAN`

Resumo: a referencia tecnica `PCNFCAN` aparece nas rotinas 329.

### Referencia tecnica PCNFCANITEM

- Rotinas relacionadas: `329 - Cancelamento do Pedido de Vendas`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCNFCANITEM / PCNFCAN`

Resumo: a referencia tecnica `PCNFCANITEM` aparece nas rotinas 329.

### Referencia tecnica PCNFENT

- Rotinas relacionadas: `1332 - Devolução pronta entrega (manifesto)`
- Modulos relacionados: `PRONTA ENTREGA`
- Referencias originais da planilha: `PCTABDEV / PCNFBASE / PCMOV / PCNFENT`

Resumo: a referencia tecnica `PCNFENT` aparece nas rotinas 1332.

### Referencia tecnica PCNFSAID

- Rotinas relacionadas: `417 - Mapa de Acerto`; `905 - Transferência de NFs do carregamento`
- Modulos relacionados: `Nao informado na planilha`, `PRONTA ENTREGA`
- Referencias originais da planilha: `PCMOV / PCNFSAID / PCPRODUT`, `PCNFSAID`

Resumo: a referencia tecnica `PCNFSAID` aparece nas rotinas 417, 905.

### Referencia tecnica PCPARAMFILIAL

- Rotinas relacionadas: `132 - Parâmetro que define média de desconto.`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCPARAMFILIAL / PCFILIAL`

Resumo: a referencia tecnica `PCPARAMFILIAL` aparece nas rotinas 132.

### Referencia tecnica PCPEDC

- Rotinas relacionadas: `317 - Imprimir Pedido`; `322 - Venda Por Departamento`; `335 - Consultar Pedido de Venda`; `382 - Duplicar pedido de venda`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`, `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCPEDC / PCPEDI`, `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`, `PCPEDC / PCPEDI / PCMOV`

Resumo: a referencia tecnica `PCPEDC` aparece nas rotinas 317, 322, 335, 382.

### Referencia tecnica PCPEDI

- Rotinas relacionadas: `317 - Imprimir Pedido`; `322 - Venda Por Departamento`; `335 - Consultar Pedido de Venda`; `382 - Duplicar pedido de venda`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`, `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCPEDC / PCPEDI`, `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`, `PCPEDC / PCPEDI / PCMOV`

Resumo: a referencia tecnica `PCPEDI` aparece nas rotinas 317, 322, 335, 382.

### Referencia tecnica PCPLPAG

- Rotinas relacionadas: `523 - Cadastrar plano de pagamento`
- Modulos relacionados: `ROTINAS CADASTROS BÁSICOS`
- Referencias originais da planilha: `PCPLPAG`

Resumo: a referencia tecnica `PCPLPAG` aparece nas rotinas 523.

### Referencia tecnica PCPLPAGCLI

- Rotinas relacionadas: `308 - Alterar condição especial do cliente`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCPLPAGCLI`

Resumo: a referencia tecnica `PCPLPAGCLI` aparece nas rotinas 308.

### Referencia tecnica PCPRECOPROM

- Rotinas relacionadas: `357 - Cadastro preço fixo`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCPRECOPROM`

Resumo: a referencia tecnica `PCPRECOPROM` aparece nas rotinas 357.

### Referencia tecnica PCPREST

- Rotinas relacionadas: `407 - Rel. Fechamento de Carga`; `1203 - Extrato do cliente`; `1213 - Títulos`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`, `PRONTA ENTREGA`, `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCPREST`, `PCPREST / PCCLIENT / PCCOB / PCFILIAL`, `PCPREST / PCCLIENT / PCCOB,/ PCMOVCR`

Resumo: a referencia tecnica `PCPREST` aparece nas rotinas 407, 1203, 1213.

### Referencia tecnica PCPRODFILIAL

- Rotinas relacionadas: `238 - Manutenção do cadastro de produtos (colocar múltiplo em filiais e etc.)`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCPRODFILIAL`

Resumo: a referencia tecnica `PCPRODFILIAL` aparece nas rotinas 238.

### Referencia tecnica PCPRODSIMIL

- Rotinas relacionadas: `297 - Produtos Similares`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCPRODSIMIL`

Resumo: a referencia tecnica `PCPRODSIMIL` aparece nas rotinas 297.

### Referencia tecnica PCPRODUSUR

- Rotinas relacionadas: `304 - cadastro de cotas por RCA`
- Modulos relacionados: `Nao informado na planilha`
- Referencias originais da planilha: `PCPRODUSUR`

Resumo: a referencia tecnica `PCPRODUSUR` aparece nas rotinas 304.

### Referencia tecnica PCPRODUT

- Rotinas relacionadas: `203 - Cadastrar Produto`; `417 - Mapa de Acerto`
- Modulos relacionados: `PRONTA ENTREGA`, `ROTINAS CADASTROS BÁSICOS`
- Referencias originais da planilha: `PCMOV / PCNFSAID / PCPRODUT`, `PCPRODUT`

Resumo: a referencia tecnica `PCPRODUT` aparece nas rotinas 203, 417.

### Referencia tecnica PCPROMC

- Rotinas relacionadas: `349 - Cadastrar Brindes`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCPROMC / PCPROMI`

Resumo: a referencia tecnica `PCPROMC` aparece nas rotinas 349.

### Referencia tecnica PCPROMI

- Rotinas relacionadas: `349 - Cadastrar Brindes`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCPROMC / PCPROMI`

Resumo: a referencia tecnica `PCPROMI` aparece nas rotinas 349.

### Referencia tecnica PCPROMOCAOMED

- Rotinas relacionadas: `2323 - Cadastrar Promoção (Módulo Medicamentos)`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCPROMOCAOMED`

Resumo: a referencia tecnica `PCPROMOCAOMED` aparece nas rotinas 2323.

### Referencia tecnica PCRESTRICAOVENDA

- Rotinas relacionadas: `391 - Restrição de venda`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCRESTRICAOVENDA`

Resumo: a referencia tecnica `PCRESTRICAOVENDA` aparece nas rotinas 391.

### Referencia tecnica PCRETORNOIMPORTARVENDAS

- Rotinas relacionadas: `2500 - INTEGRADORA, APURARCAMPANHASBRINDES`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES , PROCEDURES , TRIGGERS, VIEWS`

Resumo: a referencia tecnica `PCRETORNOIMPORTARVENDAS` aparece nas rotinas 2500.

### Referencia tecnica PCROTACLI

- Rotinas relacionadas: `354 - Cadastrar Rota de Visita e Cliente`
- Modulos relacionados: `RELACIONAMENTOS DE CLIENTES (Roteirização)`
- Referencias originais da planilha: `PCROTACLI`

Resumo: a referencia tecnica `PCROTACLI` aparece nas rotinas 354.

### Referencia tecnica PCROTACLIFIXAC

- Rotinas relacionadas: `385 - Roteiro de visitas (cadastro de rotas)`
- Modulos relacionados: `RELACIONAMENTOS DE CLIENTES (Roteirização)`
- Referencias originais da planilha: `PCROTACLIFIXAC / PCROTACLIFIXAI`

Resumo: a referencia tecnica `PCROTACLIFIXAC` aparece nas rotinas 385.

### Referencia tecnica PCROTACLIFIXAI

- Rotinas relacionadas: `385 - Roteiro de visitas (cadastro de rotas)`
- Modulos relacionados: `RELACIONAMENTOS DE CLIENTES (Roteirização)`
- Referencias originais da planilha: `PCROTACLIFIXAC / PCROTACLIFIXAI`

Resumo: a referencia tecnica `PCROTACLIFIXAI` aparece nas rotinas 385.

### Referencia tecnica PCSEC

- Rotinas relacionadas: `322 - Venda Por Departamento`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`
- Referencias originais da planilha: `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`

Resumo: a referencia tecnica `PCSEC` aparece nas rotinas 322.

### Referencia tecnica PCSUPERV

- Rotinas relacionadas: `516 - Cadastrar Supervisor`
- Modulos relacionados: `ROTINAS CADASTROS BÁSICOS`
- Referencias originais da planilha: `PCSUPERV`

Resumo: a referencia tecnica `PCSUPERV` aparece nas rotinas 516.

### Referencia tecnica PCTABDEV

- Rotinas relacionadas: `1332 - Devolução pronta entrega (manifesto)`
- Modulos relacionados: `PRONTA ENTREGA`
- Referencias originais da planilha: `PCTABDEV / PCNFBASE / PCMOV / PCNFENT`

Resumo: a referencia tecnica `PCTABDEV` aparece nas rotinas 1332.

### Referencia tecnica PCTABPR

- Rotinas relacionadas: `201 - Precificação de produto`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCTABPR`

Resumo: a referencia tecnica `PCTABPR` aparece nas rotinas 201.

### Referencia tecnica PCTABPRCLI

- Rotinas relacionadas: `3314 - Cadastrar Tab. De Preço Utilizada Pelo Cli`
- Modulos relacionados: `RELACIONAMENTOS DE CLIENTES`
- Referencias originais da planilha: `PCTABPRCLI`

Resumo: a referencia tecnica `PCTABPRCLI` aparece nas rotinas 3314.

### Referencia tecnica PCTIPOBONIFIC

- Rotinas relacionadas: `3329 - Cadastro de tipos de Bonificações`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCTIPOBONIFIC`

Resumo: a referencia tecnica `PCTIPOBONIFIC` aparece nas rotinas 3329.

### Referencia tecnica PCTRIBUT

- Rotinas relacionadas: `574 - Cadastrar tributação nos produtos`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCTRIBUT`

Resumo: a referencia tecnica `PCTRIBUT` aparece nas rotinas 574.

### Referencia tecnica PCTRIBUTPARTILHA

- Rotinas relacionadas: `514 - Cadastro do tipo de tributação (acréscimo na tabela de pessoa física)`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCTRIBUTPARTILHA`

Resumo: a referencia tecnica `PCTRIBUTPARTILHA` aparece nas rotinas 514.

### Referencia tecnica PCUSUARI

- Rotinas relacionadas: `313 - Cliente por RCA`; `322 - Venda Por Departamento`; `356 - Wizard de conta-corrente de RCA`; `517 - Cadastrar RCA`; `517 - Cadastro RCA (Percentual Acréscimo/Desconto)`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`, `INFORMAÇÕES DE VENDA DO REPRESENTANTE`, `INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)`, `RELACIONAMENTOS DE CLIENTES`, `ROTINAS CADASTROS BÁSICOS`
- Referencias originais da planilha: `PCPEDC / PCPEDI / PCCLIENT / PCUSUARI / PCDEPTO / PCSEC / PCFORNEC ...`, `PCUSUARI`, `PCUSUARI / PCCLIENT`, `pc_pkg_controlarsaldorca (PCUSUARI)`

Resumo: a referencia tecnica `PCUSUARI` aparece nas rotinas 313, 322, 356, 517, 517.

### Referencia tecnica PCUSURCLI

- Rotinas relacionadas: `586 - Relacionamento Cliente X RCA`; `3315 - Cadastro de RCA por Cliente`
- Modulos relacionados: `RELACIONAMENTOS DE CLIENTES`
- Referencias originais da planilha: `PCUSURCLI`

Resumo: a referencia tecnica `PCUSURCLI` aparece nas rotinas 586, 3315.

### Referencia tecnica PCUSURDEPSEC

- Rotinas relacionadas: `587 - Cadastrar Relacionamento de rca departamento e seção`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCUSURDEPSEC`

Resumo: a referencia tecnica `PCUSURDEPSEC` aparece nas rotinas 587.

### Referencia tecnica PCUSURFORNEC

- Rotinas relacionadas: `505 - Relacionar fornecedor por RCA`
- Modulos relacionados: `RELACIONAMENTOS DE PRODUTOS`
- Referencias originais da planilha: `PCUSURFORNEC`

Resumo: a referencia tecnica `PCUSURFORNEC` aparece nas rotinas 505.

### Referencia tecnica PCVEICUL

- Rotinas relacionadas: `410 - Acertos`
- Modulos relacionados: `PRONTA ENTREGA`
- Referencias originais da planilha: `PCCARREG / PCVEICUL`

Resumo: a referencia tecnica `PCVEICUL` aparece nas rotinas 410.

### Referencia tecnica PCVISITA

- Rotinas relacionadas: `336 - Alterar Pedido de Vendas`
- Modulos relacionados: `CONFECÇÃO DE PEDIDOS`
- Referencias originais da planilha: `PCVISITA`

Resumo: a referencia tecnica `PCVISITA` aparece nas rotinas 336.

### Referencia tecnica PC_PKG_CONTROLARSALDORCA

- Rotinas relacionadas: `356 - Wizard de conta-corrente de RCA`
- Modulos relacionados: `INFORMAÇÕES DE VENDA DO REPRESENTANTE`
- Referencias originais da planilha: `pc_pkg_controlarsaldorca (PCUSUARI)`

Resumo: a referencia tecnica `PC_PKG_CONTROLARSALDORCA` aparece nas rotinas 356.

### Referencia tecnica PROCEDURES

- Rotinas relacionadas: `2500 - INTEGRADORA, APURARCAMPANHASBRINDES`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES , PROCEDURES , TRIGGERS, VIEWS`

Resumo: a referencia tecnica `PROCEDURES` aparece nas rotinas 2500.

### Referencia tecnica TRIGGERS

- Rotinas relacionadas: `2500 - INTEGRADORA, APURARCAMPANHASBRINDES`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES , PROCEDURES , TRIGGERS, VIEWS`

Resumo: a referencia tecnica `TRIGGERS` aparece nas rotinas 2500.

### Referencia tecnica VIEWS

- Rotinas relacionadas: `2500 - INTEGRADORA, APURARCAMPANHASBRINDES`
- Modulos relacionados: `ROTINAS DE APOIO`
- Referencias originais da planilha: `PCRETORNOIMPORTARVENDAS, PACKAGES, FUNCOES , PROCEDURES , TRIGGERS, VIEWS`

Resumo: a referencia tecnica `VIEWS` aparece nas rotinas 2500.

## Indice por modulo

### Modulo Cadastrar de clientes

- Rotinas do modulo: `302 - Cadastrar de clientes`
- Principais tabelas do modulo: `PCCLIENT`
- Total de rotinas mapeadas neste modulo: `1`

### Modulo CONFECÇÃO DE PEDIDOS

- Rotinas do modulo: `132 - Parâmetro que define média de desconto.`; `201 - Precificação de produto`; `301 - Autorizar Preço de Venda`; `308 - Alterar condição especial do cliente`; `317 - Imprimir Pedido`; `329 - Cancelamento do Pedido de Vendas`; `335 - Consultar Pedido de Venda`; `336 - Alterar Pedido de Vendas`; `357 - Cadastro preço fixo`; `382 - Duplicar pedido de venda`; `387 - Desconto por quantidade`; `514 - Cadastro do tipo de tributação (acréscimo na tabela de pessoa física)`; `517 - Cadastro RCA (Percentual Acréscimo/Desconto)`; `561 - Cadastrar política de Desconto`; `1203 - Extrato do cliente`; `2316 - Digitar Pedido de Venda (medicamentos)`; `2323 - Cadastrar Promoção (Módulo Medicamentos)`; `3306 - Cadastrar campanha de desconto para Força de Vendas * (Com exceção Restrição por plano de pagamento)`
- Principais tabelas do modulo: `PCAUTORI`, `PCDESCONTO`, `PCDESCONTOC`, `PCDESCONTOI`, `PCDESCONTORESTRICAO`, `PCDESCQUANT`, `PCFILIAL`, `PCMOV`, `PCNFCAN`, `PCNFCANITEM`, `PCPARAMFILIAL`, `PCPEDC`, `PCPEDI`, `PCPLPAGCLI`, `PCPRECOPROM`, `PCPREST`, `PCPROMOCAOMED`, `PCTABPR`, `PCTRIBUTPARTILHA`, `PCUSUARI`, `PCVISITA`
- Total de rotinas mapeadas neste modulo: `18`

### Modulo INFORMAÇÕES DE VENDA DO REPRESENTANTE

- Rotinas do modulo: `111 - Rotina de faturamento`; `146 - Resumo de Vendas`; `311 - Extrato, saldo do RCA`; `356 - Wizard de conta-corrente de RCA`
- Principais tabelas do modulo: `FUNC_RESUMOFATURAMENTO`, `PCLOGRCA.VLCORRENTE`, `PCLOGRCA.VLCORRENTEANT`, `PCMETASUP`, `PCUSUARI`, `PC_PKG_CONTROLARSALDORCA`
- Total de rotinas mapeadas neste modulo: `4`

### Modulo INFORMAÇÕES DE VENDA DO REPRESENTANTE (Metas)

- Rotinas do modulo: `303 - Acompanhar Meta x Venda`; `322 - Venda Por Departamento`; `353 - Cadastrar Meta Diária por RCA (valor)`; `399 - Gerar Meta Mensal (Fornecedor - Sessão - Produto - Cliente)`; `3305 - Cadastrar Meta Mensal`
- Principais tabelas do modulo: `PCCLIENT`, `PCDEPTO`, `PCFORNEC`, `PCMETA`, `PCMETAC`, `PCMETARCA`, `PCMETASUP`, `PCPEDC`, `PCPEDI`, `PCSEC`, `PCUSUARI`
- Total de rotinas mapeadas neste modulo: `5`

### Modulo Nao informado na planilha

- Rotinas do modulo: `304 - cadastro de cotas por RCA`; `901 - Montar carga`; `904 - Cancelamento de carga`; `905 - Transferência de NFs do carregamento`; `3320 - Cadastro de brinde Express`
- Principais tabelas do modulo: `PCBRINDEEX`, `PCCARREG`, `PCNFSAID`, `PCPRODUSUR`
- Total de rotinas mapeadas neste modulo: `5`

### Modulo PRONTA ENTREGA

- Rotinas do modulo: `407 - Rel. Fechamento de Carga`; `410 - Acertos`; `417 - Mapa de Acerto`; `1332 - Devolução pronta entrega (manifesto)`; `1402 - Gerar Faturamento`
- Principais tabelas do modulo: `PCCARREG`, `PCCLIENT`, `PCCOB`, `PCMOV`, `PCMOVCR`, `PCNFBASE`, `PCNFENT`, `PCNFSAID`, `PCPREST`, `PCPRODUT`, `PCTABDEV`, `PCVEICUL`
- Total de rotinas mapeadas neste modulo: `5`

### Modulo RELACIONAMENTOS DE CLIENTES

- Rotinas do modulo: `313 - Cliente por RCA`; `577 - Cadastrar Cidades e código IBGE`; `586 - Relacionamento Cliente X RCA`; `1203 - Tipo de cobrança, venda, plano padrão`; `3314 - Cadastrar Tab. De Preço Utilizada Pelo Cli`; `3315 - Cadastro de RCA por Cliente`
- Principais tabelas do modulo: `PCCLIENT`, `PCCOBCLI`, `PCMOTNAOCOMPRA`, `PCTABPRCLI`, `PCUSUARI`, `PCUSURCLI`
- Total de rotinas mapeadas neste modulo: `6`

### Modulo RELACIONAMENTOS DE CLIENTES (Roteirização)

- Rotinas do modulo: `344 - Consultar Visita`; `354 - Cadastrar Rota de Visita e Cliente`; `385 - Roteiro de visitas (cadastro de rotas)`; `578 - Cadastrar Motivo de Não Compra`
- Principais tabelas do modulo: `PCROTACLI`, `PCROTACLIFIXAC`, `PCROTACLIFIXAI`
- Total de rotinas mapeadas neste modulo: `4`

### Modulo RELACIONAMENTOS DE PRODUTOS

- Rotinas do modulo: `238 - Manutenção do cadastro de produtos (colocar múltiplo em filiais e etc.)`; `297 - Produtos Similares`; `349 - Cadastrar Brindes`; `391 - Restrição de venda`; `505 - Relacionar fornecedor por RCA`; `574 - Cadastrar tributação nos produtos`; `587 - Cadastrar Relacionamento de rca departamento e seção`; `3307 - Cadastrar Cesta básica`
- Principais tabelas do modulo: `PCFORMPROD`, `PCPRODFILIAL`, `PCPRODSIMIL`, `PCPROMC`, `PCPROMI`, `PCRESTRICAOVENDA`, `PCTRIBUT`, `PCUSURDEPSEC`, `PCUSURFORNEC`
- Total de rotinas mapeadas neste modulo: `8`

### Modulo ROTINAS CADASTROS BÁSICOS

- Rotinas do modulo: `203 - Cadastrar Produto`; `292 - Cadastrar embalagem`; `309 - Cadastrar dias úteis de venda Produto`; `516 - Cadastrar Supervisor`; `517 - Cadastrar RCA`; `522 - Cadastrar tipo de cobrança`; `523 - Cadastrar plano de pagamento`; `2014 - Cadastrar embalagem (auto-serviço)`
- Principais tabelas do modulo: `PCCOB`, `PCDATAS`, `PCEMBALAGEM`, `PCPLPAG`, `PCPRODUT`, `PCSUPERV`, `PCUSUARI`
- Total de rotinas mapeadas neste modulo: `8`

### Modulo ROTINAS DE APOIO

- Rotinas do modulo: `283 - Cadastrar cotação de Concorrentes`; `285 - Analisar Cotação de Concorrentes`; `318 - Enviar Mensagem para RCA`; `528 - Cadastro de novos destinatários p/ envio de mensagem`; `530 - Permissões de acessos para cada usuário (usuário 8888)`; `535 - Cadastrar Filiais`; `1213 - Títulos`; `2500 - INTEGRADORA, APURARCAMPANHASBRINDES`; `3329 - Cadastro de tipos de Bonificações`
- Principais tabelas do modulo: `FUNCOES`, `PACKAGES`, `PCCLIENT`, `PCCOB`, `PCCONCOR`, `PCCOTA`, `PCEMPR`, `PCFILIAL`, `PCMENS`, `PCPREST`, `PCRETORNOIMPORTARVENDAS`, `PCTIPOBONIFIC`, `PROCEDURES`, `TRIGGERS`, `VIEWS`
- Total de rotinas mapeadas neste modulo: `9`

## Pontos de atencao da fonte

- Rotinas sem modulo informado: `304 - cadastro de cotas por RCA`; `901 - Montar carga`; `904 - Cancelamento de carga`; `905 - Transferência de NFs do carregamento`; `3320 - Cadastro de brinde Express`
- Rotinas sem tabela informada: `344 - Consultar Visita`; `530 - Permissões de acessos para cada usuário (usuário 8888)`; `578 - Cadastrar Motivo de Não Compra`; `2316 - Digitar Pedido de Venda (medicamentos)`

## Fonte

Documento gerado automaticamente a partir da planilha XLSX original.
