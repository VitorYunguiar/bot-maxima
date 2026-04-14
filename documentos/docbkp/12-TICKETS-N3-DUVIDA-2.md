# Extração de Tickets - MaxPedido (MXPEDDV)

## MXPEDDV-109379

**Contexto**
Erro ao fazer GET no endpoint TABELASTRIBUTACOESERP: "A quantidade de chaves não é compatível. Sua consulta possui 5 chave(s) e o banco de dados tem 7."

**Solução / Diagnóstico**
Para realizar o GET na tabela de tributações, é necessário utilizar o endpoint TabelaTributo. Usando esse endpoint, as informações são retornadas corretamente.

---

## MXPEDDV-109381

**Contexto**
Aplicação não valida corretamente política de desconto comercial, reportando desconto acima do esperado mesmo com política presente.

**Solução / Diagnóstico**
Necessário definir a quantidade mínima/máxima para aplicação da política levando em conta o fator da embalagem.

---

## MXPEDDV-109404

**Contexto**
Ao tentar cancelar um pedido com erro, o MaxPedido retorna: "Não foi encontrado nenhum item para o pedido!"

**Solução / Diagnóstico**
Pedido foi importado de um orçamento antes da versão 4.030.1, onde havia erro na importação de orçamentos, fazendo os pedidos serem salvos sem itens. Para o pedido em questão não há o que fazer; o problema será resolvido para novos pedidos e orçamentos na versão mais recente.

---

## MXPEDDV-109440

**Contexto**
Parâmetro de percentual médio do pedido (15,99%) configurado para permitir salvar pedido com bloqueio no Winthor, mas na APK não está salvando.

**Solução / Diagnóstico**
Para não bloquear na APK, definir um valor no parâmetro PERMAXDESCVENDA_FV (MaxPedido) acima do valor definido na 132 (PERMAXDESCVENDA).

---

## MXPEDDV-109525

**Contexto**
Cliente gostaria de alterar o nome da empresa que aparece na impressão do pedido.

**Solução / Diagnóstico**
O aplicativo tenta buscar o nome do parâmetro "EMPRESA" da tabela MXSPARAMETRO. Quando não encontrado, busca a informação da tabela mxsconfig, coluna empresa.

---

## MXPEDDV-109600

**Contexto**
Títulos pagos no Winthor aparecem como em aberto no banco Nuvem (codoperacao = 2).

**Solução / Diagnóstico**
Está parametrizado para gerar títulos pagos apenas com 90 dias, por isso gerou codoperacao = 2 apenas para deletar o título da APK.

---

## MXPEDDV-109656

**Contexto**
Diferença de preço entre PCPEDC e PCPEDIFVMANIF em pedido pronta entrega. Valor tabela maior que valor venda, gerando desconto após integração. Custo diferente também.

**Solução / Diagnóstico**
O valor correto é gravado na PCPEDCFVMANIF; após integração o valor fica incorreto – necessidade de verificar com a TOTVS. Sobre o custo diferente, o campo CUSTOFINLIQUIDO não é utilizado nos projetos do extrator/atualizador.

---

## MXPEDDV-109658

**Contexto**
Ao compartilhar pedido, o PDF não apresenta o valor de ST dos produtos (antes funcionava na base antiga).

**Solução / Diagnóstico**
Necessário habilitar o parâmetro CON_CALCSTPF para calcular impostos para cliente PF. Também é necessário incluir valor na coluna IVA da tabela MXSTRIBUT.

---

## MXPEDDV-109738

**Contexto**
Pedido AFV 690 emitiu item com 72 unidades ao preço de R$ 1,003, sendo preço de tabela R$ 68,70.

**Solução / Diagnóstico**
O parâmetro ACEITADESCTMKFV está com valor 'S', permitindo descontos acima do valor flexível. Além disso, o produto não possui preço mínimo cadastrado.

---

## MXPEDDV-109751

**Contexto**
Divergência de estoque entre Pedido de Venda e MaxPedido: o MaxPedido não está trazendo valores corretos de movimentações.

**Solução / Diagnóstico**
A contabilização de estoque ocorre de formas diferentes. Para consistência, utilizar apenas um dos fluxos (Pedido de Venda ou MaxPedido), não ambos.

---

## MXPEDDV-109761

**Contexto**
Em determinada embalagem, informar quantidade 1 não altera o valor total; só altera com quantidade muito maior. Cliente precisa colocar 600000 para dar o mesmo valor de uma caixa.

**Solução / Diagnóstico**
Duas opções: 1) Habilitar parâmetro USACADEMBALAGEMPROCFRIOS para negociar embalagem cadastrada na MXSEMBALAGEM. 2) Corrigir MXSPRODUT.PESOPECA para = 1 (atualmente 0,00001 causa falha no cálculo).

---

## MXPEDDV-109793

**Contexto**
Políticas de desconto configuradas para não debitar do saldo de CC do RCA, mas ainda assim estão debitando.

**Solução / Diagnóstico**
Conforme teste, um ambiente movimenta o flex e outro não para a mesma campanha. A movimentação ocorre após integração com o ERP, fora do ambiente Máxima.

---

## MXPEDDV-109812

**Contexto**
Produto disponível na R316 mas no aparelho do RCA fica indisponível para vários clientes.

**Solução / Diagnóstico**
Produto estava com PCEMBALAGEM.EXCLUIDO = 'S', impedindo integração com FV. Alterado para 'N' e produto integrado.

---

## MXPEDDV-109829

**Contexto**
Cliente deseja exibir mensagem impedindo vendedor de fazer pedido se saldo CC for negativo/zerado.

**Solução / Diagnóstico**
Se BASECREDDEBRCA = 'S', o desconto não é debitado; para debitar, alterar para 'N'. Parâmetro CON_TIPOMOVCCRCA = 'FF' movimenta só no faturamento (não bloqueia na venda); alterar para 'VV' para bloquear no momento da venda.

---

## MXPEDDV-109896

**Contexto**
APK com falha na validação de estoque: cálculo (qtestger - qtbloqueada - qtpendente - qtreserv) não diminui o QTPENDENTE.

**Solução / Diagnóstico**
Habilitar o parâmetro BLOQUEIAVENDAESTPENDENTE na MXSPARAMFILIAL.

---

## MXPEDDV-109898

**Contexto**
Cliente deseja controle para parar/reiniciar a integração (extrator), similar ao Pedido de Vendas.

**Solução / Diagnóstico**
Criado um usuário com privilégios de administrador para o cliente no portainer.

---

## MXPEDDV-109916

**Contexto**
Banco local não está sendo atualizado. Cliente executou grants e alterou parâmetro PRIMEIRA_IMPLANTACAO para 'S', mas log apresenta erro.

**Solução / Diagnóstico**
Faltam criar colunas na tabela PCNFSAID: NUMCUPOM (NUMBER(10)) e TIPODOCUMENTO (VARCHAR2(1)). Executar os ALTER TABLE e depois atualizar extrator.

---

## MXPEDDV-110152

**Contexto**
Cliente gostaria que na nota do pronta entrega a embalagem apareça como master (atualmente sai em unidade).

**Solução / Diagnóstico**
O XML da nota é gerado pelo ERP; o MaxPedido só usa esses dados para gerar a nota. Não há regras para tratar embalagens. As embalagens precisam vir direto do XML da TV13.

---

## MXPEDDV-110153

**Contexto**
Pedido teste: produto com preço 2,85, desconto 2% = 2,79, mas chegou no ERP com 2,69, gerando débito indevido.

**Solução / Diagnóstico**
O JSON mostra preço 2,79 na MXSINTEGRACAOPEDIDO, mas 2,69 na MXSHISTORICOPEDI. O preço diferente veio após a integração (não é alteração do backend Máxima).

---

## MXPEDDV-110207

**Contexto**
Pedidos não estão integrando corretamente; desconto não abatido da verba e item cortado.

**Solução / Diagnóstico**
Uma trigger no ambiente do cliente comprometia a integração. Após desabilitar a trigger e reprocessar os pedidos, foram processados pela integradora.

---

## MXPEDDV-110232

**Contexto**
Integração enviando informações para MXSEMBALAGEM, mas nenhuma atualização no banco (requisições com sucesso).

**Solução / Diagnóstico**
A tabela MXSEMBALAGEM tem chave primária (CODAUXILIAR, CODFILIAL). Mesmos valores para produtos diferentes sobrescrevem registros. Para gravar múltiplos registros, enviar valores distintos para cada produto.

---

## MXPEDDV-110234

**Contexto**
Ao compartilhar boleto de pedido pronta entrega, informa "não foi possível encontrar o boleto", mesmo existindo na ERP_MXSPREST e MXSTITULOSABERTOS.

**Solução / Diagnóstico**
Parâmetro ENVIA_PEDIDOS_BALCAORESERVA estava 'N' e o pedido é do tipo Balcão Reserva. Parametrização alterada e informações reenviadas.

---

## MXPEDDV-110248

**Contexto**
Erro de versão do protocolo CIFS no ponto de montagem do extrator (mensagem CIFS: VFS: cifs_mount failed w/return code = -95).

**Solução / Diagnóstico**
Servidor Linux do cliente estava sem acesso à internet. Após ajuste da infraestrutura e liberação de acesso, extrator iniciado corretamente.

---

## MXPEDDV-110303

**Contexto**
No MaxPedido só aparece filial 14 para venda, mesmo com outras filiais habilitadas. Na 316 é possível selecionar filial 1,2,11 e NF na 14.

**Solução / Diagnóstico**
Cliente vinculado à filial 14 via rotina 3314 do Winthor (só há registro na pctabprcli para essa filial). MaxPedido carrega apenas filiais desse vínculo. Em alinhamento com P.O. para levantar configurações da 316 e replicar no MaxPedido.

---

## MXPEDDV-110312

**Contexto**
Ao encerrar horário de almoço da jornada, vendedor não consegue iniciar novo período.

**Solução / Diagnóstico**
Comportamento correto: usuário precisa respeitar o horário estabelecido na jornada.

---

## MXPEDDV-110329

**Contexto**
Precificação da tabela 912 traz valor incorreto no app (região 48 correta).

**Solução / Diagnóstico**
MXSTABPR.VLST = 0 para região 912, então impostos calculados diretamente sobre pvenda1. Necessário que VLST venha com algum valor para remover impostos do preço tabelado antes de calcular impostos de venda.

---

## MXPEDDV-110339

**Contexto**
View MXSVCLIENTSRCA traz 248 clientes, mas script correto traz 191.

**Solução / Diagnóstico**
Quantidade a mais deve-se à categorização de clientes feita pelo Gestão da Máxima (tabela mxmp_carteirizacao do banco Nuvem).

---

## MXPEDDV-110389

**Contexto**
Cliente quer alterar nomenclatura da coluna UN/UND nas notas/relatórios do MaxPedido.

**Solução / Diagnóstico**
- Espelho do pedido / relatório compartilhado: possível personalizar relatório.
- Nota fiscal Danfe: possível personalizar.
- Nota fiscal da impressora térmica: layout padrão, não alterável.

---

## MXPEDDV-110457

**Contexto**
Pedidos gerados pelo RCA aparecem sem nome do cliente (só código).

**Solução / Diagnóstico**
Não há vínculo de cliente para o usuário. Necessário cadastrar vínculos no Winthor.

---

## MXPEDDV-110478

**Contexto**
Em alguns clientes na filial 2 não carrega tributação dos itens; na 316 funciona.

**Solução / Diagnóstico**
Parâmetro IGUALAR_FILIALNF_AO_ALTERAR_FILIAL habilitado, carregando mesma tributação da filial.

---

## MXPEDDV-110499

**Contexto**
Tributação errada no app (antiga, sem ST), mesmo com tributação atualizada.

**Solução / Diagnóstico**
Cliente utiliza tributação por região. Conforme MXSTABPR para região '1.:.1.:.1.:.A', produto '1.:.1.:.00000260' deve usar CODST '1.:.1.:.MT.:.2.:.08111000.:.01'. O app carrega o ST cadastrado.

---

## MXPEDDV-110570

**Contexto**
Erros de conexão e IPs ao reinstalar cliente Barrigão.

**Solução / Diagnóstico**
Linux do cliente não conectava à internet. Configurado rede para DHCP via netplan, instalado docker, portainer e extrator. Extrator online.

---

## MXPEDDV-110573

**Contexto**
Portainer acessível via IP interno mas não via IP público. Integração funciona, mas gerir e central não mostram informações do extrator.

**Solução / Diagnóstico**
Porta 9000 estava fechada no ambiente do cliente. Após liberação, acesso normalizado.

---

## MXPEDDV-110649

**Contexto**
Divergência de preço em produtos com precificação por embalagem: R$ 135,82 na tabela, mas na negociação fica R$ 135,72.

**Solução / Diagnóstico**
Preço da embalagem 135,82 dividido por 36 unidades = 3,772777777. Arredondado para 2 casas = 3,77. Recomendado alterar configuração para 6 casas decimais.

---

## MXPEDDV-110673

**Contexto**
Cadastro de cliente com crítica "cód cliente já existente" gravou apenas na PCCLIENTFV com importado=3, e reenvio não integra.

**Solução / Diagnóstico**
Análise do fluxo de integração e da package IMPORTARCADASTROS da TOTVS. Testes de novos cadastros realizados (ID_CLIENTE 201,202,203,221 na MXSINTEGRACAOCLIENTE).

---

## MXPEDDV-110722

**Contexto**
Extrator cai recorrentemente; reiniciar resolve momentaneamente, mas volta a ficar offline.

**Solução / Diagnóstico**
Banco de dados do cliente não aceitava conexões externas e havia bloqueio de IPs da Máxima. Cliente ajustou configuração e liberou IPs.

---

## MXPEDDV-110773

**Contexto**
Na versão nova, quantidade de estoque aparece em unidades em ambas as telas (listagem e venda), antes convertia para caixa/múltiplo na tela de venda.

**Solução / Diagnóstico**
Remete ao ticket MXPEDDV-110821.

---

## MXPEDDV-110795

**Contexto**
Fluxo de retorno de estoque para pedidos pronta entrega com MaxPag: em caso de link expirado ou estornado, estoque não retorna.

**Solução / Diagnóstico**
Não há tratativa para esses cenários. Foram abertos os tickets MXPEDDV-111024 e MXPEDDV-111005 para correção.

---

## MXPEDDV-110837

**Contexto**
Movimentação duplicada de conta corrente do RCA e movimentação gerada pelo codusuario = 0 (Ambiente Nuvem).

**Solução / Diagnóstico**
Testes mostraram: quando campanha debita, valor 64,60; quando não debita, valor 76,00. Movimentação correta nos pedidos ID_PEDIDO = 6449 e 6437.

---

## MXPEDDV-110848

**Contexto**
Pedidos sumiram de um carregamento (tinha 10, ficou 6). Trigger adicionada para logs.

**Solução / Diagnóstico**
Logs mostraram que os pedidos nunca foram vinculados ao carregamento mencionado. Necessário verificar procedimento de logística.

---

## MXPEDDV-110913

**Contexto**
Aparelho não sincroniza, fica minutos tentando.

**Solução / Diagnóstico**
Necessário disponibilizar mais espaço de armazenamento (logs do Grafana mostraram base gerada normalmente).

---

## MXPEDDV-110917

**Contexto**
Nenhum produto aparece na base do cliente, mesmo após marcar filial para não vender por embalagem e alterar UTILIZAVENDAPOREMBALAGEM para 'N'.

**Solução / Diagnóstico**
Faltava permissão de fornecedores no portal de configurações.

---

## MXPEDDV-110938

**Contexto**
Forma de pagamento não aparece para dois clientes no palm (apenas para uma vendedora).

**Solução / Diagnóstico**
MaxPedido V4 não permite iniciar pedido quando cliente não possui plano de pagamento vinculado (MXSCLIENT.CODPLPAG). Necessário cadastrar. O comportamento da V3 (permitir sem plano) é um erro.

---

## MXPEDDV-110957

**Contexto**
Cliente possui regra: na filial 14, itens de bicicleta não podem ser faturados pela Filial NF 14 (apenas moto). Na 316 funciona.

**Solução / Diagnóstico**
MaxPedido não possui fluxo que vincule filial NF ao departamento de produtos. Cliente não apresentou evidências técnicas de como funciona no Winthor.

---

## MXPEDDV-110968

**Contexto**
Ao abrir cliente, erro "Nenhuma modalidade de cobrança pode ser carregada". Tipo cobrança BOL, prazo médio 0.0.

**Solução / Diagnóstico**
Faltam dados nas tabelas MXSCOBRANCAFILIAL e MXSCOBPLPAG. Precisam ser alimentadas.

---

## MXPEDDV-110979

**Contexto**
Combos de desconto (SQP) debitando indevidamente, mesmo com NAODEBITCCRCA='S'.

**Solução / Diagnóstico**
Campanhas configuradas corretamente; MaxPedido não movimentou flex. O pedido foi realizado em 26/01 e a política que movimenta flex foi alterada em 28/01. Duplicando o pedido, não ocorre movimentação. Ocorrência devida à mudança de regras após digitação.

---

## MXPEDDV-110997

**Contexto**
Pedido editado gerou crítica, mas na APK não apareceu (tabela mxscriticapedido não consta).

**Solução / Diagnóstico**
Após importar base e acessar pedido, as críticas carregaram ao fazer swipe na tela. Problema relacionado a erro de login com API de cancelamento da TOTVS, já sanado.

---

## MXPEDDV-111001

**Contexto**
Cálculo de multa e juros para títulos em atraso incorreto (multa correta, juros diário muito inferior).

**Solução / Diagnóstico**
O fluxo utiliza MXSCOB.TXJUROS dividido por 100. O ERP deve enviar o valor já multiplicado por 100 (ex: 33 em vez de 0,33) para que o cálculo fique correto.

---

## MXPEDDV-111033

**Contexto**
Campanha 48041: cálculo de preço correto apenas para os 5 primeiros produtos; demais ficam em carregamento infinito.

**Solução / Diagnóstico**
Cliente usando scroll do mouse no Android. O Android não notifica a rolagem, então o carregamento lazy não é iniciado.

---

## MXPEDDV-111154

**Contexto**
Pedidos não estão sendo enviados.

**Solução / Diagnóstico**
Possível bloqueio de IP na rede. Liberar os IPs da Máxima: 3.81.180.2, 34.236.34.79, 3.81.180.245, 200.225.244.33, 177.43.92.98, 18.215.65.25.

---

## MXPEDDV-111176

**Contexto**
Processador.dll gerando volume muito alto de requisições, causando sobrecarga no banco.

**Solução / Diagnóstico**
SQL que abre muitas sessões e delete na PCMXSINTEGRACAO. Correção na versão mais nova do extrator e banco. Necessário atualizar banco nuvem, local e extrator.

---

## MXPEDDV-111210

**Contexto**
Pedido 698201483 teve produtos cortados; campanha 257643 continha os produtos.

**Solução / Diagnóstico**
Pedido enviado para aprovação em 30/01, aprovado em 31/01. Campanha foi inativada em 31/01, poucos minutos antes do pedido chegar no WinThor.

---

## MXPEDDV-111219

**Contexto**
Campanhas de desconto desapareceram da tabela MXSDESCONTO (não ficaram como codoperacao=2).

**Solução / Diagnóstico**
Rotina de limpeza remove registros com DTFIM há mais de 15 dias e ENVIANV='N'. Cliente alterou manualmente DTFIM para data anterior, causando exclusão.

---

## MXPEDDV-111220

**Contexto**
ERP precisa identificar no JSON: campanhas cashback, desconto por volume e descontos manuais.

**Solução / Diagnóstico**
- Cashback: campo MXSDESCONTO.CREDITASOBREPOLITICA.
- Desconto por volume: campos QTINI/QTFIM; produto inserido via campanha envia propriedade `politicaCampanhaDesconto`.
- Desconto manual: propriedade `PercDescontoInformadoTela` presente, sem `politicaCampanhaDesconto`.

---

## MXPEDDV-111250

**Contexto**
Estoque pronta entrega exibido incorretamente.

**Solução / Diagnóstico**
Cliente vinculando NF TV13 a novo carregamento, mas TV13 anterior já foi consumido. Procedimento correto: emitir nova TV13 ou fechar carregamento e ajustar mercadoria no Winthor.

---

## MXPEDDV-111265

**Contexto**
RCA não consegue cancelar pedido com link de pagamento expirado, mesmo com PERMITE_APAGAR_PEDIDOS ativo.

**Solução / Diagnóstico**
Necessário habilitar permissão na central para exclusão de pedidos enviados. Após apagar do dispositivo, estoque do pronta entrega voltou.

---

## MXPEDDV-111289

**Contexto**
Pedidos com desconto acima de 5% (permitido) estão sendo rejeitados na versão 4.031.4, mas na V3 funcionam.

**Solução / Diagnóstico**
Testes na versão 4.032.3 gravaram pedidos com sucesso no ERP.

---

## MXPEDDV-111294

**Contexto**
Erro ao configurar ponto de montagem no Linux.

**Solução / Diagnóstico**
Repositórios do Linux não estavam sendo acessados. Adicionados novos repositórios no arquivo sources.list e configuradas as fotos.

---

## MXPEDDV-111334

**Contexto**
Ao efetuar venda com Boleto, mensagem "Usuario sem permissão para o plano de pagamento ou plano de pagamento inexistente". Pedido salva mas não sai do app.

**Solução / Diagnóstico**
Tabela mxsplpag com USAMULTIFILIAL='S' mas sem registros em mxsplpagfilial. Cliente precisa alterar para 'N' ou enviar registros.

---

## MXPEDDV-111399

**Contexto**
Erro de tributação em itens que já têm tributação (no Winthor funciona).

**Solução / Diagnóstico**
Na versão mais recente (4.032.4) não foi possível reproduzir o problema.

---

## MXPEDDV-111401

**Contexto**
Extrator T-CLOUD entrando em loop ao tentar criar colunas que a TOTVS já cria.

**Solução / Diagnóstico**
Extrator não tinha permissão para criar colunas, cada erro deixava o processo lento e o healthcheck reiniciava. Removido o script de criação de colunas do banco do cliente; extrator subiu normalmente.

---

## MXPEDDV-111402

**Contexto**
Como é calculado o campo valorST no JSON do pedido?

**Solução / Diagnóstico**
Exemplo com produto 183.0: Preço inicial 46,5, acréscimo 2% = 45,57. IVA 50% → Base ST = 68,355. Alíquota 20,5%: ST = (68,355*0,205) - (45,57*0,205) = 4,670925.

---

## MXPEDDV-111493

**Contexto**
Portainer/extrator não fica com docker online.

**Solução / Diagnóstico**
Cliente reiniciou máquina Linux, outro dispositivo assumiu o IP. Docker versão 29 incompatível; removido e instalada versão 24, stack recriada.

---

## MXPEDDV-111503

**Contexto**
Parâmetro INICIA_QTDE_UM coloca quantidade 1, mas para produtos com múltiplo (ex: caixa de 6kg) o ERP corta o item.

**Solução / Diagnóstico**
INICIA_QTDE_UM só coloca 1 no campo, não valida múltiplo. Para não ser rejeitado, ativar INICIAR_NEGOCIACAO_QTDE_MULTIPLO_APENAS_UNIDADE e USAR_MULTIPLO_QTDE.

---

## MXPEDDV-111504

**Contexto**
Erro ao importar produtos via CSV para pré-pedido.

**Solução / Diagnóstico**
Documentada a numeração das colunas para importação correta.

---

## MXPEDDV-111529

**Contexto**
Lock no ambiente Top Birra.

**Solução / Diagnóstico**
Lock devido ao WinthorAnywhere fazendo for update na pcest. Parâmetro INTEG_CONTROLE_MAX alterado para 5 para evitar concorrência.

---

## MXPEDDV-111611

**Contexto**
Fluxo de desconto por quantidade não funciona em clientes OERPs (funciona em WinThor).

**Solução / Diagnóstico**
Habilitar parâmetro CON_USADESCPORQUANT na MXSPARAMFILIAL.

---

## MXPEDDV-111627

**Contexto**
Preço unitário não aparece na tela de negociação (campo mostra valor total).

**Solução / Diagnóstico**
Ativar parâmetro USAR_QT_UNIT_PROD_EXIBICAO para dividir o preço pela quantidade unitária.

---

## MXPEDDV-111628

**Contexto**
Pedidos apresentam erro de integração mas não aparecem na mxsintegracaopedidom nem na central.

**Solução / Diagnóstico**
Análise da crítica do pedido, base local, banco nuvem e configurações do ambiente. Fluxo evidenciado.

---

## MXPEDDV-111704

**Contexto**
Erro ao exportar banco (base do zero funciona, base do vendedor não).

**Solução / Diagnóstico**
Aparelho do usuário sem espaço em disco.

---

## MXPEDDV-111732

**Contexto**
Cliente 7261 transferido para base do RCA 78: nenhum produto aparece na aba TABELA para esse cliente (outros clientes funcionam). Na base do zero aparece.

**Solução / Diagnóstico**
Gerada carga nas tabelas de prodfilial que pode interferir quando usuário é transferido de filial. Solicitar usuário sincronizar.

---

## MXPEDDV-111737

**Contexto**
Ao duplicar espelho de pedido, o campo VL UNIT IPI some no espelho cópia.

**Solução / Diagnóstico**
Quando existe relatório personalizado (MXSGRRELATORIO.LAYOUT='S'), a APK usa esse relatório. O layout padrão da central é diferente do gerado internamente. Necessário ajustar o relatório personalizado.

---

## MXPEDDV-111756

**Contexto**
Erro ao alterar cadastro de cliente na rotina 302: erro nas tabelas.

**Solução / Diagnóstico**
Consulta de triggers no banco local: nenhuma trigger para o schema MXSPORTALCLIENTE foi retornada, confirmando que já foi removida.

---

## MXPEDDV-111793

**Contexto**
Cliente precisa ver planos por ordem decrescente de prazos (ex: 07, 07/14, 14 dias).

**Solução / Diagnóstico**
Listagem da cobrança tem ordenação padrão pelo código. Não há forma de ordenar por descrição.

---

## MXPEDDV-111808

**Contexto**
Relatório do MaxPedido apresenta apenas valor total de descontos somados, sem segregação por campanha progressiva. Necessário apurar descontos individuais.

**Solução / Diagnóstico**
Análise do fluxo de apuração de campanhas, estrutura do banco e debug durante geração de relatório.

---

## MXPEDDV-111830

**Contexto**
É possível editar pedido quando aguardando pagamento no MaxPag?

**Solução / Diagnóstico**
Não. Pedidos aguardando autorização do MaxPag não podem ser editados.

---

## MXPEDDV-111858

**Contexto**
Divergência de valores entre relatório do Winthor (rotina 1249) e app (objetivo e tela de pedidos).

**Solução / Diagnóstico**
Para conferência do Resumo de Vendas, usar como base a Rotina 111 (faturamento). Os valores conferem.

---

## MXPEDDV-111893

**Contexto**
Solicitação de análise de riscos ao habilitar parâmetro de 6 meses de histórico.

**Solução / Diagnóstico**
Análise realizada; query executada manualmente sem travamento. Pode parametrizar QTD_MESES_PRODVENDA para 6 meses.

---

## MXPEDDV-111916

**Contexto**
Possibilidade de criar desconto que libere desconto em outro item (ex: comprar caipira, ganhar desconto em extrinha).

**Solução / Diagnóstico**
Campanha do tipo FPU pode atender.

---

## MXPEDDV-111946

**Contexto**
Registros da tabela MXSCLIENTECREDDISP estão sendo deletados sozinhos após integração.

**Solução / Diagnóstico**
Parâmetro GERAR_CLIENTECREDDISP_OERP='S' faz o sistema calcular automaticamente crédito disponível (limite - títulos abertos - histórico). Para o ERP enviar os dados, alterar parâmetro para 'N'.

---

## MXPEDDV-111985

**Contexto**
Tela de inteligência de negócios > cadastros gerais > configurações da máxima fica só carregando.

**Solução / Diagnóstico**
Faltava registro na MXSCONFIGERP. Após inserir, tela carregou normalmente.

---

## MXPEDDV-112008

**Contexto**
Pedidos não chegam ao Winthor após religar servidores (falta de energia).

**Solução / Diagnóstico**
Link intpdv-unificado.solucoesmaxima.com.br estava indisponível. Equipe reiniciou o serviço.

---

## MXPEDDV-112012

**Contexto**
Problema na integração de pedidos com SAP (cliente Destro).

**Solução / Diagnóstico**
Mesmo link indisponível; reiniciado serviço.

---

## MXPEDDV-112013

**Contexto**
Extrator não executa serviço (conexão com banco local ok).

**Solução / Diagnóstico**
Container do extrator estava em faixa de IP diferente do banco. Alterado compose para atribuir IP na faixa 172.19.0.0/16.

---

## MXPEDDV-112045

**Contexto**
Erro ao salvar nova mensagem circular.

**Solução / Diagnóstico**
Após atualização, erro corrigido.

---

## MXPEDDV-112139

**Contexto**
Campo Percentual de IPI disponível nos JSONs dos pedidos, mas não disponível no gerador de relatórios.

**Solução / Diagnóstico**
Melhoria: propriedades de IPI e ST precisam ser adicionadas no Stimulsoft e lançadas no atualizador.

---

## MXPEDDV-112157

**Contexto**
Espelho do pedido mostra valor errado (relatório padrão correto, mas duplicado fica errado).

**Solução / Diagnóstico**
Winthor gerou valor total = 4.528,30 e valor atendido = 4.642,55 (incorreto). Para o relatório, configurar para puxar valor atendido em vez de valor total. Necessário alinhamento com TOTVS.