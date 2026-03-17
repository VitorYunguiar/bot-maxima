# Casos Resolvidos — Gatekeeper maxPedido

**Sistema:** maxPedido

**Área:** Suporte Técnico / Diagnóstico


---

## Caso 1

**Contexto**

O vendedor destak.rca não consegue iniciar um pedido no cliente 6716. Ao tentar, o sistema apresenta uma mensagem de inconsistência de dados. As permissões do vendedor (planos, cobranças, filiais) foram verificadas na Central e estão de acordo com o cadastro do cliente, mas o cliente possui vínculos em diversas tabelas do banco, e é necessário identificar qual deles está causando o alerta.


**Solução / Diagnóstico**

Após análise, foi verificado que o cliente 6716 utiliza a tabela MXSTABPRCLI, que está vinculada às regiões 1 e 3. O cliente também utiliza a MXSPLPAGREGIAO para fazer o vínculo entre plano de pagamento e região. Foi constatado que não havia vínculo na região 1 para o plano de pagamento 2. Após a inserção desse vínculo, foi possível realizar o pedido. A orientação é que o cliente seja instruído a cadastrar o vínculo na MXSPLPAGREGIAO com o plano 2.


---

## Caso 2

**Contexto**

O cliente solicitou alterações no espelho do pedido: 1) Remoção do campo de impostos; 2) Remoção do "Impresso em" e "Válido até". O analista sabe que o item 1 é resolvido pelo parâmetro OCULTAR_IMPOSTOS_PEDIDO_EMAIL, mas não encontrou um parâmetro para o item 2 e acredita que seja algo novo, possivelmente com um parâmetro para remoção.


**Solução / Diagnóstico**

Foi alinhado via Discord que, para ocultar a validade, basta configurar o parâmetro OCULTAR_VALIDADE_PROPOSTA como "S".


---

## Caso 3

**Contexto**

O produto de código 56558 aparece na aba de produtos da base do RCA, mas não é encontrado ao fazer pedidos para os clientes 6611 e 1533 (filial 7). O analista verificou filiais, estoque, tabela de preço e restrições de venda via inspect, mas não encontrou nenhum impedimento.


**Solução / Diagnóstico**

Após análise, foi constatado que na tabela MXSTABPR não havia informação na coluna PVENDA1 para a região 50 (região do cliente) para o produto 56558. Como o cliente utiliza a MXSTABPRCLI, que vincula o cliente às filiais 1, 7 e 50, é necessário que haja preço para todas as regiões correspondentes. Após inserir a informação de preço (PVENDA1) na MXSTABPR via inspect, o produto passou a aparecer normalmente. O cliente deve ser orientado a verificar o preço do produto, seja no Winthor (tabela PCTABPR) ou realizando uma carga de dados.


---

## Caso 4

**Contexto**

O cliente deseja que o preço unitário seja exibido na tela de negociação. Os parâmetros EXIBIR_VALOR_UNITARIO e EXIBE_PRECO_UNIT_LISTAGEM já foram criados, mas a tela continua exibindo apenas o valor total. Foram feitas alterações no banco da APK (alterando PVENDA e QTUNIT), mas o campo não foi alterado.


**Solução / Diagnóstico**

Para exibir o campo "Valor Un:", é necessário: 1. Desativar a permissão "Exibir Valor Total" no cadastro do RCA ou do Perfil de usuários. 2. Configurar o parâmetro EXIBIR_VALOR_UNITARIO = S. 3. O cliente precisa alterar a quantidade unitária do produto (QTUNIT) na rotina 203 do Winthor (PCPRODUT.QTUNIT).


---

## Caso 5

**Contexto**

Um pedido com um produto a R$47 foi cancelado. Após alguns dias, o preço do produto subiu para R$53. Ao duplicar o pedido cancelado com a opção "manter condições comerciais", o novo pedido foi gerado com o preço antigo de R$47. O analista questiona o comportamento.


**Solução / Diagnóstico**

O analista (Carlos Prates) encaminhou o ticket para o desenvolvimento, pois a princípio isso abre uma brecha para enviar um produto com valor anterior que não seja justificado como desconto.


---

## Caso 6

**Contexto**

Ao inserir um produto de campanha, a quantidade inserida no campo sempre retorna para 1, impossibilitando a venda de mais de uma unidade. O problema ocorre na base do zero para o login viacerta.670.


**Solução / Diagnóstico**

O comportamento está correto de acordo com a configuração da campanha feita pelo cliente. A campanha estava configurada para ser "por produto" com uma quantidade mínima de venda obrigatória maior que 1. Isso nunca será verdade, pois a condição é aplicada ao próprio produto. Após alterar a configuração da campanha no inspect (para aplicar a regra a um conjunto de produtos, como uma seção), o funcionamento ficou correto.


---

## Caso 7

**Contexto**

Após parametrizar a exibição da lucratividade, o valor apresentado (aproximadamente 92,98%) não se altera, independentemente do desconto aplicado no produto. O analista questiona qual cálculo está sendo feito.


**Solução / Diagnóstico**

O cálculo da lucratividade é ((PVENDA - CUSTO FINANCEIRO) / PVENDA) * 100. O CUSTO FINANCEIRO é calculado como PVENDA1 * (CODICMTAB / 100). Com o parâmetro DESCONSIDERAR_IMPOSTOS_CALCULO_LUCRATIVIDADE desativado, o cálculo considera a tributação. Se ativado, o cálculo simplifica e busca o custo diretamente da MXSEST.CUSTOFIN. O percentual não mudava porque o custo financeiro se ajustava proporcionalmente ao novo preço com desconto, mantendo a relação.


---

## Caso 8

**Contexto**

Vários produtos da linha Red Bull (ex: 1537) não aparecem no maxPedido para o RCA disdal.2675 no cliente 55731. O analista validou que os produtos têm cadastro, o RCA não tem restrições e tem permissões totais, mas os produtos não são exibidos.


**Solução / Diagnóstico**

Após análise, foi constatado que os produtos não estavam cadastrados nas tabelas de permissão do RCA: MXSUSURDEPSEC (departamento/seção) e MXSUSURFORNEC (fornecedor). Após inserir essas permissões via inspect, os produtos apareceram. O cliente deve ser orientado a fazer esse cadastro (rotina 587 do Winthor) e, se já tiver feito, verificar se os dados estão sendo carregados para a nuvem.


---

## Caso 9

**Contexto**

O cliente deseja que, se qualquer cliente de uma rede (principal ou secundário) estiver bloqueado, seja impedida a realização de pedidos para todos os clientes daquela rede.


**Solução / Diagnóstico**

A solução foi alcançada com a seguinte parametrização no maxPedido: BLOQUEAR_CONFECCAO_PEDIDO_CLIENTE_PRINC_BLOQ = S, ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO = N, PERMITE_ORCAMENTO_CLIENTE_BLOQ = S, ACEITAVENDAAVISTACLIBLOQ = N. Além disso, o parâmetro CON_VERIFICARCLIENTESREDE deve estar como 'S'. O sistema valida o bloqueio através da tabela MXSCLIENTESBLOQUEADOS. Quando um cliente da rede está bloqueado, a validação do parâmetro ACEITAR_DIGITAR_PEDIDO_CLIREDEBLOQUEADO entra em ação, bloqueando a transmissão de pedidos para todos os clientes da mesma rede.


---

## Caso 10

**Contexto**

Um pedido bonificado (TV5) está travado na base do RCA LYNKZ.miguel (numped 256014561) e não é enviado para a nuvem, nem oferece a opção de reenviar.


**Solução / Diagnóstico**

Foi verificado que o fluxo de pedidos bonificados só envia o pedido BNF após o pedido "pai" (original) ser integrado ao ERP. O pedido travado (BNF) foi gerado a partir do pedido 256014560, que ainda não possui NUMPEDERP na MXSINTEGRACAOPEDIDO e não foi encontrado na MXSHISTORICOPEDC. O pedido BNF será enviado automaticamente assim que o pedido original for integrado com sucesso.


---

## Caso 11

**Contexto**

Uma política de preço fixo para o produto 8153 é aplicada corretamente na filial 50, mas não é apresentada quando o RCA tenta vender na filial 07, mesmo com o registro na base.


**Solução / Diagnóstico**

O problema ocorre porque ao trocar a filial de venda de 50 para 7, a "filial de emissão da NF" (filialNF) não é alterada, permanecendo 50. A política de preço fixo é validada com base na filialNF. Para corrigir, deve-se ativar o parâmetro IGUALAR_FILIALNF_AO_ALTERAR_FILIAL = S, que faz a filialNF acompanhar a filial de venda. Recomenda-se também desativar o parâmetro FILIALNF_DEFINE_FILIAL_PEDIDO ou habilitar a permissão "Permitir escolha da filial de emissão da NF" para os RCAs.


---

## Caso 12

**Contexto**

Vendedores não conseguem iniciar pedidos devido a um aviso de roteiros pendentes do dia anterior. A configuração de bloqueio está ativa, mas não há registros pendentes na MXSVISITAS da base do vendedor analisado (mix.272). O cliente tem usado um código de desbloqueio manualmente.


**Solução / Diagnóstico**

A análise mostrou que o RCA MIX.78 (e outros) possui vários clientes com visitas agendadas nos últimos 7 dias (conforme parâmetro DIAS_VERIFICACAO_ROT_PEND) que não foram justificadas. Um script SQL complexo foi executado e confirmou a existência dessas pendências, que estavam causando o bloqueio. A orientação é informar o cliente sobre os registros pendentes ou sugerir a alteração do parâmetro.


---

## Caso 13

**Contexto**

Ao acessar as campanhas de desconto 2930 e 2931, a mensagem "não possui nenhum item disponível" é exibida. O produto 7527, ao ser adicionado, direciona para a campanha 2930, mas ao acessá-la, não há itens. O analista nota que a campanha tem os produtos 227 e 7526, mas o 7527 não está na MXSDESCONTOI.


**Solução / Diagnóstico**

O problema ocorre porque o produto configurado na campanha 2930 é o 7526, que é o produto principal do 7527. O produto 7526 não existe na base do RCA (não está disponível para negociação), causando o conflito. Ao alterar a campanha para o produto correto (7527) via inspect, o funcionamento normalizou. O cliente deve ser orientado a liberar o produto principal para o RCA ou alterar o produto vinculado à campanha.


---

## Caso 14

**Contexto**

O cliente tem uma regra de comissão onde o RCA só ganha comissão se o desconto concedido for menor que 6%. Atualmente, mesmo com descontos maiores, a comissão de 8% continua sendo contabilizada no maxPedido. O analista não encontra onde essa configuração de limite de desconto para comissão é feita.


**Solução / Diagnóstico**

O cliente está utilizando um modelo de comissão progressiva, onde quanto maior o desconto, menor a comissão. Essa configuração é feita na rotina 363 e vai para a tabela MXSCOMISSAOREGIAO. Foi constatado que a tabela MXSCOMISSAOREGIAO na nuvem estava vazia ou com dados incorretos (ex: dtinicio e dtfim nulas, tipovendedor errado). O cliente deve verificar a rotina 363 e salvar novamente para que as informações sejam enviadas corretamente para a nuvem.


---

## Caso 15

**Contexto**

O cliente deseja que pedidos bonificados sejam barrados no maxPedido caso o RCA não tenha saldo de conta corrente suficiente, e não apenas na integradora.


**Solução / Diagnóstico**

Para barrar no maxPedido, os parâmetros corretos são PERMITE_DESCONTAR_BONIF_CC_NEGATIVA = N e IMPEDIR_ABATIMENTO_SEMSALDORCA = S. Se o objetivo for enviar para aprovação, deve-se usar ENVIAR_PEDIDO_SEMSALDO_AUTORIZACAO = S e VALIDAR_CC_APROV_PEDIDO = S.


---

## Caso 16

**Contexto**

Ao tentar usar o plano de pagamento 230 com a cobrança 237, o maxPedido exibe erro informando que o plano não aceita essa cobrança. O analista verificou as tabelas de permissão e não encontrou impedimentos.


**Solução / Diagnóstico**

Após análise, foi constatado que a coluna VENDABK da MXSPLPAG estava nula. Ao alterá-la para 'S' via inspect, a aplicação passou a aceitar a cobrança. O cliente deve ser orientado a enviar a configuração completa do plano de pagamento.


---

## Caso 17

**Contexto**

O produto 99847 não aparece para o vendedor na filial 9 quando o cliente é o 232332 (com planos específicos), mas aparece para o cliente 2000860. Ambos os clientes são da mesma região e usam a mesma tabela de preço, e não há restrições ativas.


**Solução / Diagnóstico**

A análise mostrou que o produto 99847 não estava aparecendo porque as colunas PVENDA e PVENDA1 na MXSTABPR estavam com valor zero para as regiões do cliente (26 e 315). Após corrigir os valores via inspect, o produto passou a ser exibido. O cliente deve ser orientado a enviar as informações de preço corretas.


---

## Caso 18

**Contexto**

O cliente vai começar a usar campanhas de desconto e quer saber quais as alterações no JSON de integração do pedido quando uma campanha é utilizada.


**Solução / Diagnóstico**

Ao comparar dois JSONs (um com campanha e outro sem), a principal diferença é a presença de uma lista chamada PoliticaCampanhaDesconto no JSON do pedido com campanha. Essa lista contém os detalhes de todas as campanhas aplicadas aos itens. No pedido sem campanha, essa lista é exibida vazia.


---

## Caso 19

**Contexto**

O cliente deseja impedir que o RCA salve um pedido com valor acima do limite de crédito do cliente. Os parâmetros BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE, PERMITI_VENDA_AVISTA_SEMLIMITE e outros foram configurados, mas o pedido ainda é salvo e enviado.


**Solução / Diagnóstico**

Para cliente Winthor (caso da PCM), o maxPedido sempre permite salvar o pedido, mas pode bloqueá-lo ou exibir uma mensagem de alerta. Não há configuração atual no maxPedido para impedir o salvamento. O parâmetro BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE controla o envio, não o salvamento. A recomendação é validar com o cliente se no Winthor (316) ele consegue configurar para não salvar o pedido quando o limite é excedido. Se o Winthor bloquear, então pode ser aberta uma demanda de erro para o maxPedido N3.


---

## Caso 20

**Contexto**

O cliente quer substituir a informação de "Código de Fábrica" pela "Marca do produto" na listagem de produtos do aplicativo.


**Solução / Diagnóstico**

Para obter esse comportamento, deve-se desabilitar o parâmetro HABILITAR_VISUALIZACAO_COD_FAB_PROD_TAB = N (para ocultar o código de fábrica) e habilitar o parâmetro LIST_PROD_FIELD_MARCA = S (para exibir o campo da marca).


---

## Caso 21

**Contexto**

Um pedido (NUMPED 3200118) foi rejeitado pela integradora devido a nível de venda, mas o link de pagamento do maxPag foi gerado e ficou como "PRÉ AUTORIZADO". As configurações do extrator foram corrigidas, mas o status do pagamento não se alterou.


**Solução / Diagnóstico**

Após atualizar o ambiente e sincronizar o maxPag, o pedido foi estornado, conforme esperado, já que não foi processado pela integradora.


---

## Caso 22

**Contexto**

Ao tentar abrir ou editar um pedido específico (821977), o aplicativo exibe a mensagem: "O pedido ... foi editado mas seu histórico não está disponível! Sincroniza para obter o histórico", mesmo após sincronização.


**Solução / Diagnóstico**

Após análise e conversa com o desenvolvimento, foi orientado a atualizar o ambiente e a versão da APK do RCA e pedir para que ele sincronize novamente. Se o problema persistir, o ticket deve ser reaberto para encaminhamento ao N3.


---

## Caso 23

**Contexto**

Os vendedores 1160 e 1161 não conseguem iniciar pedido em nenhum cliente. O erro foi anexado. O analista já verificou os planos de pagamento na nuvem e no Winthor e estão iguais.


**Solução / Diagnóstico**

O problema ocorre porque na tabela MXSPLPAG, a coluna codfilial estava com o valor '1'. Como o RCA tem permissão para trabalhar com duas filiais (1 e outra), o código da filial no plano deve ser '99' para que o plano seja válido para todas as filiais. Após ajustar via inspect, o acesso foi normalizado. O cliente deve ser orientado a não vincular planos de pagamento a uma filial específica quando o RCA opera em múltiplas filiais.


---

## Caso 24

**Contexto**

O cliente possui os parâmetros GPS_TRACKING_ENABLED = S e CONFIRMA_ATUALIZACAO_COORDENADA_CLIENTE = S, mas ao finalizar um pedido, a mensagem perguntando se deseja atualizar as coordenadas do cliente não é exibida.


**Solução / Diagnóstico**

A mensagem não era exibida devido à falta da permissão "Solicitar autorização para alterar coordenadas do cliente" no perfil do RCA. Para que a mensagem apareça, é necessário ter essa permissão habilitada, além dos dois parâmetros.


---

## Caso 25

**Contexto**

O analista pergunta qual a parametrização para bloquear que o vendedor envie um pedido bonificado se não tiver saldo de conta corrente, ou que permita inserir produtos bonificados apenas até o limite do saldo.


**Solução / Diagnóstico**

Para obter esse comportamento, o parâmetro PERMITE_DESCONTAR_BONIF_CC_NEGATIVA deve ser configurado como 'N' diretamente no banco nuvem. Após sincronizar, ao tentar inserir um item em uma venda de bonificação que exceda o saldo do RCA, a mensagem "Produto excedeu crédito do RCA" será exibida, impedindo a inserção do item.


---

## Caso 26

**Contexto**

Cliente quer saber quais as alterações no JSON de integração quando um pedido é enviado com desconto escalonado.


**Solução / Diagnóstico**

Ao contrário das campanhas de desconto, o desconto escalonado não adiciona novas estruturas ou listas ao JSON. A diferença está nos valores das variáveis existentes (como o percentual de desconto) que serão alterados para refletir o desconto escalonado aplicado.


---

## Caso 27

**Contexto**

Um pedido aparece como "L" na timeline do aplicativo, mas já foi faturado. Ele existe na MXSINTEGRACAOPEDIDO e na PCPEDCFV (banco local), mas não é encontrado na tabela de histórico (MXSHISTORICOPEDC).


**Solução / Diagnóstico**

Foi realizada uma carga manual na MXSHISTORICOPEDC para incluir o pedido. Após a carga, o histórico do pedido apareceu, mas com status de cancelado. O analista deve verificar com o cliente se a nota fiscal correspondente foi realmente cancelada.


---

## Caso 28

**Contexto**

O alerta de economia de bateria continua aparecendo e impedindo o uso do maxPedido, mesmo com os parâmetros BLOQUEAR_UTLIZACAO_ECONOMIA_BATERIA e BLOQUEAR_UTILIZACAO_BATERIA_OTIMIZADA configurados como 'N'.


**Solução / Diagnóstico**

O alerta é controlado por dois parâmetros: BLOQUEAR_UTLIZACAO_ECONOMIA_BATERIA e GPS_TRACKING_ENABLED. Se qualquer um deles estiver como 'S', o fluxo que exige o modo de economia de bateria será ativado. No caso, o GPS_TRACKING_ENABLED estava como 'S', por isso o alerta persistia.


---

## Caso 29

**Contexto**

Ao duplicar um pedido que contém produtos com desconto e trocar o cliente, os descontos são perdidos, mesmo selecionando a opção "Tentar manter as condições comerciais". Isso é um problema para RCAs que precisam trocar o cliente de um pedido.


**Solução / Diagnóstico**

A mensagem "Tenta manter as condições..." indica que o sistema tentará, mas não garante, pois valida diversas condições do novo cliente (plano de pagamento, região, políticas de desconto automáticas, etc.). No caso analisado, os produtos do pedido original tinham uma política de desconto automática (CODDESCONTO = 23469). Ao duplicar para um novo cliente, essa política foi reaplicada, gerando um novo cálculo de desconto. O comportamento foi demonstrado em vídeo.


---

## Caso 30

**Contexto**

Um cliente reclama que um campo específico (hint de múltiplo) aparece para alguns produtos e para outros não. O analista descobriu que a diferença está na unidade do produto (MXSPRODUT.UNIDADE): aparece para 'UN' e não aparece para 'KG'. Ele quer saber se isso é um erro ou uma melhoria.


**Solução / Diagnóstico**

O hint com a informação de múltiplo só aparece se o produto usar um múltiplo maior que 1 E a unidade da embalagem for 'UN'. Atualmente, o código valida apenas a unidade do tipo 'UN'. Portanto, para produtos com unidade 'KG', o campo não é exibido, o que está de acordo com o funcionamento atual do sistema.


---

## Caso 31

**Contexto**

O produto 451047 não aparece ao fazer um pedido para o cliente 61845, mas aparece normalmente no card de produtos para o mesmo RCA (megadist.gbeck). O analista já limpou restrições, mas o problema persiste em base zero.


**Solução / Diagnóstico**

A análise mostrou que o cliente tem configurado o uso obrigatório de embalagem nas filiais (parâmetro UTILIZAVENDAPOREMBALAGEM). Foi constatado que o produto 451047 não possui embalagem cadastrada. Após cadastrar uma embalagem para o produto via inspect, ele passou a ser exibido normalmente. O cliente deve ser orientado a cadastrar a embalagem para o produto.


---

## Caso 32

**Contexto**

O produto KIT PROMO SH+COND+CP TLL KD NUTRKD 480ML (CÓD: 299) não aparecia no aplicativo. O preço existe na PCTABPR do Winthor, mas não subiu para a MXSTABPR na nuvem. O ambiente foi atualizado, mas a divergência persiste.


**Solução / Diagnóstico**

Foi orientado ao cliente que enviasse o preço do produto 299 novamente. O preço chegou na MXSTABPR, mas foi identificado um erro na pkg_carga_nuvem por falta de permissão (grants). A orientação é que o cliente verifique com a TOTVS a necessidade de rodar os grants para normalizar a package de carga.


---

## Caso 33

**Contexto**

O cliente quer usar vínculos de plano de pagamento por região (MXSPLPAGREGIAO). O analista testou e, ao ativar o parâmetro VINCULO_REGIAO_PLANO, o RCA perde as permissões e não consegue iniciar pedido.


**Solução / Diagnóstico**

O parâmetro VINCULO_REGIAO_PLANO faz o sistema buscar os planos na MXSPLPAGREGIAO. O erro ocorria porque a região do cliente testado (05999, região 44) não estava vinculada a nenhum plano na MXSPLPAGREGIAO, embora o cliente tivesse vínculos na MXSPLPAGCLI. Após inserir a região 44 na MXSPLPAGREGIAO, o pedido foi iniciado normalmente com os planos da região. O select utilizado para a listagem foi fornecido.


---

## Caso 34

**Contexto**

Ao incluir qualquer produto para o cliente 14370 (RCA 19), o aplicativo exibe o erro: "Não foi possível carregar a tributação para esse produto...". Os produtos são incluídos normalmente para outros clientes.


**Solução / Diagnóstico**

O problema ocorre porque o cliente 14370 é do estado do RJ, e a tabela MXSTABTRIB não possui informações de tributação para o RJ, apenas para MG. Ao alterar o estado do cliente para MG via inspect, os produtos foram inseridos normalmente. O cliente deve ser orientado a cadastrar a tributação para o RJ.


---

## Caso 35

**Contexto**

O pedido 2300008379, feito na rotina 316 do Winthor, não aparece na timeline do vendedor jbatista.368. O parâmetro PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO está ativo e o CODUSUR no pedido está correto.


**Solução / Diagnóstico**

Foi constatado que o pedido 2300008379 era do tipo "balcão reserva". O parâmetro ENVIA_PEDIDOS_BALCAO_RESERVA não existia no ambiente (ou seja, estava como 'N'). Após criar o parâmetro como 'S' e realizar uma carga, o pedido passou a aparecer na timeline.


---

## Caso 36

**Contexto**

O cliente quer uma configuração que permita que o RCA confeccione o pedido para um cliente com títulos em atraso, mas que esse pedido fique bloqueado no aparelho e só seja enviado ao ERP após a regularização do cliente.


**Solução / Diagnóstico**

A configuração solicitada (salvar o pedido como bloqueado no aparelho) não é possível. O fluxo existente usa os parâmetros BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE e CON_NUMDIASMAXVENDACLIINADIMPLENTE. Se o objetivo é apenas alertar e deixar o pedido ser salvo, mas sem garantia de integração, a configuração deve ser BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE = S e CON_NUMDIASMAXVENDACLIINADIMPLENTE menor que NUMERO_DIAS_CLIENTE_INADIMPLENTE. Isso exibirá um alerta, salvará o pedido, mas ele poderá ser barrado no ERP.


---

## Caso 37

**Contexto**

Durante a homologação da V3, o cliente observou que, ao alterar o tipo de venda para "entrega futura" (TV7), a V2 exibe produtos normalmente, mas a V3 não exibe nenhum produto.


**Solução / Diagnóstico**

A análise mostrou que a V3, diferentemente da V2, faz uma validação de restrição de venda (MXSRESTRICAOVENDA) na query de listagem de produtos. Foi constatado que existiam registros na MXSRESTRICAOVENDA para o tipo de venda 7, que estavam barrando a exibição dos produtos. Após a remoção dessas restrições, os produtos passaram a ser exibidos normalmente na V3.


---

## Caso 38

**Contexto**

Ao iniciar um pedido no cliente 11528, filial 2, e inserir o produto 59544, o maxPedido exibe o alerta de erro ao carregar a tributação. O erro não ocorre no Winthor. O analista já comparou tabelas (MXSCLIENT, MXSTABTRIB, etc.) e fez testes de insert/update sem sucesso.


**Solução / Diagnóstico**

O problema ocorria porque o pedido estava usando a filialNF 1, que não possui tributação cadastrada para aquele produto/cliente. Como o cliente trabalha com filial de venda igual à filialNF no Winthor, era necessário que o maxPedido também fizesse essa igualação. A solução foi habilitar o parâmetro IGUALAR_FILIALNF_AO_ALTERAR_FILIAL. Com isso, a filialNF passou a ser 2 e a tributação foi carregada com sucesso.


---

## Caso 39

**Contexto**

Um RCA que também é supervisor tem seu CODUSUR alterado diretamente na Central de Configurações. Ao tentar voltar para sua própria base no aplicativo (via menu Ferramentas/Supervisor), a lista de usuários aparece em branco.


**Solução / Diagnóstico**

A funcionalidade de troca de usuário no app lista apenas os RCAs vinculados ao supervisor (pelo CODSUPERVISOR) que estão ativos e com licença. Ao alterar o CODUSUR diretamente na Central, o vínculo de supervisão é quebrado, e o app não consegue mais listar os usuários daquela equipe. Para voltar à base original, o usuário precisaria alterar manualmente o código novamente na Central. Não é uma falha, mas sim a forma como a funcionalidade foi projetada.


---

## Caso 40

**Contexto**

Usuários do perfil 700 não conseguem visualizar o campo "REGIÃO" no card de produtos, enquanto usuários do perfil 100 (do qual o 700 foi duplicado) conseguem. As permissões parecem iguais.


**Solução / Diagnóstico**

O problema não está nas permissões do perfil, mas sim nas regiões liberadas para o RCA. O RCA OPCAOATAC.917 (perfil 700) tem clientes nas regiões 16 e 20, mas as permissões de região no portal (tabela MXSREGIAO e MXSACESSOENTIDADES) estão configuradas para outras regiões, que não são as dos seus clientes. O filtro, combinado com o parâmetro FILTRAR_REGIOES_FILIAL, faz com que nenhuma região válida seja encontrada, deixando o campo em branco. A solução é ajustar as permissões do RCA para as regiões corretas (16 e 20).


---

## Caso 41

**Contexto**

Ao duplicar o pedido 4376433 para clientes diferentes, os valores finais do pedido são diferentes, mesmo selecionando a opção de manter o preço e as condições. Isso ocorre mesmo com clientes da mesma região.


**Solução / Diagnóstico**

Foi realizado um teste de duplicação do pedido do cliente 854 para o cliente 17217 na versão mais recente (3.251.6), e o preço foi mantido, conforme demonstrado em vídeo. O problema pode não estar mais ocorrendo na versão mais recente.


---

## Caso 42

**Contexto**

O cliente gerou um boleto personalizado (para remover a hora da data), mas ele não aparece como opção para o RCA na hora de exportar o boleto de um título.


**Solução / Diagnóstico**

Foi esclarecido que o suporte pode orientar o cliente sobre a funcionalidade de boleto customizado, mas a customização em si (como remover a hora) é de responsabilidade do cliente. O boleto padrão não possui parâmetro para remoção da hora; apenas o boleto customizado pode ser alterado dessa forma.


---

## Caso 43

**Contexto**

Na aba "Objetivos" do maxPedido, ao buscar os valores do mês atual, a mensagem "Nenhum dado encontrado" é exibida, mesmo o RCA possuindo vendas faturadas no período.


**Solução / Diagnóstico**

Foi realizada uma tentativa de simular o problema, mas a falha não foi reproduzida. As informações apareceram normalmente. O RCA deve ser orientado a atualizar o aplicativo para a versão mais recente.


---

## Caso 44

**Contexto**

Ao tentar acessar qualquer produto na filial 6, o aplicativo exibe a mensagem: "O PRODUTO SELECIONADO NÃO POSSUI DADOS DA FILIAL DE VENDA".


**Solução / Diagnóstico**

O usuário hortigran.josecarlos não possuía permissão de acesso à filial 6. Após conceder a permissão na Central, o problema foi resolvido.


---

## Caso 45

**Contexto**

Ao iniciar um pedido no cliente 1014627 (que usa vínculos na filial/região 10), a aplicação apresenta "inconsistência nos dados". O vendedor tem permissão na filial 10. O problema é resolvido se o vendedor também tiver permissão na filial 1.


**Solução / Diagnóstico**

O problema ocorre porque o cliente utiliza a MXSTABPRCLI (vinculando-o às filiaisNF 2 e 10). No entanto, a tabela de plano de pagamento por região (MXSPLPAGREGIAO) só possui registros para a região 10, e não para a região 2. Quando o sistema tenta validar os planos, encontra uma inconsistência. A solução é o cliente enviar as informações de plano de pagamento para a região 2 na MXSPLPAGREGIAO para esse cliente.


---

## Caso 46

**Contexto**

O cliente questiona se é possível, em um mesmo pedido normal (TV1), ter o mesmo item sendo vendido uma vez como normal e outra como bonificado, usando o parâmetro PERMITE_ITEM_BNFTV1.


**Solução / Diagnóstico**

O parâmetro PERMITE_ITEM_BNFTV1 apenas ativa um checkbox na negociação para gerar um item bonificado, mas por padrão, o sistema não permite o mesmo item duas vezes. Para conseguir esse comportamento, é necessário ativar o parâmetro CON_USACHAVETRIPLAPCPEDI = S. Com a chave tripla ativa, é possível inserir o mesmo produto múltiplas vezes, diferenciando um como bonificado. É importante alertar o cliente de que a integração dele precisará tratar essa informação, que virá no JSON.


---

## Caso 47

**Contexto**

O cliente usa o parâmetro EMITIR_NOTIFICACAO_EST_COMPLETA e recebe notificações de toda movimentação de estoque (entrada e saída). Ele deseja receber apenas notificações de entrada de produtos.


**Solução / Diagnóstico**

Atualmente, não é possível configurar para receber apenas notificações de entrada. Os parâmetros existentes (EMITIR_NOTIFICACAO_EST_COMPLETA e MXSESTNOTIFICACAO_STATUS) controlam a notificação como um todo (entrada e saída). Não há uma configuração para filtrar o tipo de movimento.


---

## Caso 48

**Contexto**

Ao negociar o produto 91432 na filial 2, a lucratividade apresentada no maxPedido é sempre negativa, independentemente do plano de pagamento. O analista verificou que o custo financeiro e o custo real do produto são iguais, mas o cálculo ainda assim resulta em negativo.


**Solução / Diagnóstico**

O cálculo da lucratividade considera o preço de venda, o custo do produto (da MXSEST) e o custo da comissão (da MXSPRODFILIAL). No caso analisado, o custo do produto é maior que o preço de venda, e a comissão de 2,5% torna o resultado ainda mais negativo. A orientação é que o maxPedido reflete o cálculo do ERP. Se na rotina 316 do Winthor a lucratividade também está negativa (conforme evidenciado), o comportamento do maxPedido está correto.


---

## Caso 49

**Contexto**

Para o cliente 13801, a MXSHISTORICOPEDC mostra apenas um pedido (44027032) de setembro, enquanto a PCPEDC no banco local mostra três pedidos (44027032, 44027175, 44027465).


**Solução / Diagnóstico**

Foi realizada uma carga manual para incluir os pedidos faltantes na MXSHISTORICOPEDC. O RCA deve ser orientado a sincronizar para visualizar o histórico completo.


---

## Caso 50

**Contexto**

Em um pedido com cobrança Cartão de Crédito (maxPag), o crédito disponível do cliente (R$ 241,55) não foi descontado do valor total do pedido (R$ 1997,70) no aplicativo, resultando em um bloqueio de valor total no cartão. No entanto, o crédito foi zerado no Winthor, indicando que foi utilizado.


**Solução / Diagnóstico**

Foi esclarecido que o "Crédito do Cliente" é diferente de "Limite do Cliente". O crédito é um valor a favor do cliente (ex: de devoluções) e é utilizado principalmente em bonificações ou abatimentos em pedidos com itens bonificados (dentro do TV1). Para usar o crédito em uma venda normal com cartão de crédito, o item precisaria ser configurado como bonificado dentro do pedido normal, usando o parâmetro PERMITE_ITEM_BNFTV1. O crédito não é abatido automaticamente em vendas normais a prazo.


---

## Caso 51

**Contexto**

Clientes cadastrados para serem faturados na filial NF 2 estão tendo seus pedidos faturados pela filial NF 1 no Winthor. O JSON do pedido mostra a NF 2 corretamente, mas a integração grava como NF 1.


**Solução / Diagnóstico**

A análise mostrou que o parâmetro IGUALAR_FILIALNF_AO_ALTERAR_FILIAL estava ativo. Esse parâmetro iguala a filial de venda (escolhida pelo RCA no cabeçalho) à filial NF. Como a filial de venda escolhida foi a 1, a filialNF também se tornou 1, sobrescrevendo a informação do cadastro do cliente. A solução é desativar esse parâmetro e, se necessário, liberar a permissão para o RCA escolher a filial NF manualmente.


---

## Caso 52

**Contexto**

Uma restrição por plano de pagamento (código 1) foi criada para o plano 081, incluindo o produto 015227-3. No entanto, ao tentar usar esse plano, o produto 015227-3 não pode ser inserido, enquanto outros produtos da mesma restrição podem. O produto está na lista de restrição.


**Solução / Diagnóstico**

A análise mostrou que os produtos que funcionavam estavam vinculados a múltiplas restrições, enquanto o que apresentava problema estava vinculado a apenas duas. Ao replicar a configuração dos produtos que funcionavam para o produto problemático no portal, a restrição passou a funcionar corretamente. A query que o sistema usa para validar a restrição foi fornecida para referência futura.


---

## Caso 53

**Contexto**

Um título para o cliente 02830801 foi baixado no sistema, mas no aplicativo ele ainda consta como aberto. Na base do vendedor, o título tem valor negativo e não é encontrado na tabela de títulos da nuvem (ERP_MXSPREST).


**Solução / Diagnóstico**

Foi realizada uma correção manual. Após a correção, a situação foi validada em base zero e normalizada. O RCA deve ser orientado a sincronizar para verificar.


---

## Caso 54

**Contexto**

Após enviar uma solicitação de aumento de limite de crédito, ela não é mais exibida no aplicativo, nem mesmo após ser negada. O RCA não tem nenhum retorno sobre o status da solicitação.


**Solução / Diagnóstico**

Foi realizado um teste para simular o problema (solicitar, depois negar no gestão), mas o fluxo ocorreu normalmente no ambiente de teste. O RCA deve ser orientado a atualizar o aplicativo para a versão mais recente e validar novamente.


---

## Caso 55

**Contexto**

O cliente não consegue liberar um pedido na rotina 336 do Winthor. A TOTVS informou que o pedido está travado devido à trigger MAXSOLUCOES.TRG_MXS_PCAUTORC. O ambiente foi atualizado, mas o erro persiste.


**Solução / Diagnóstico**

Foi feita uma conexão no banco local e a trigger foi desabilitada para teste. Após isso, o cliente conseguiu fazer a alteração na 336. A trigger foi reabilitada e recompilada. O cliente foi orientado a reportar se o problema ocorrer novamente.


---

## Caso 56

**Contexto**

Quando um RCA sem saldo de conta corrente aplica um desconto, uma mensagem de alerta é exibida, mas ao clicar em "OK", o desconto é aplicado e o produto é inserido. O analista quer saber como bloquear a aplicação do desconto e quais parâmetros usar.


**Solução / Diagnóstico**

Para bloquear a aplicação do desconto quando o RCA não tem saldo, devem ser configurados os parâmetros: EXIBIR_SALDOCC_DISPONIVEL = S (para exibir o saldo) e DESABILITA_INSERCAO_ITEM_ACIMALIMITECREDITORCA = S (para bloquear a inserção do item). Com isso, a mensagem "Desconto aplicado é maior que o valor disponível na Conta Corrente do RCA" será exibida e o item não será inserido.


---

## Caso 57

**Contexto**

A duplicata 61610 consta como aberta no aplicativo e no banco nuvem, mas já foi baixada no Winthor.


**Solução / Diagnóstico**

Foi realizada uma carga para normalizar os títulos. A situação foi resolvida.


---

## Caso 58

**Contexto**

Uma comissão progressiva foi cadastrada (4% para descontos de 0 a 5%). A configuração existe na base do RCA (MXSCOMISSAOREGIAO), mas não é exibida ao clicar em "Comissões" na tela do produto. O valor total da comissão (4%) aparece na aba totais, sugerindo que o cálculo está vindo de outra fonte.


**Solução / Diagnóstico**

O problema ocorria por um conflito de configuração. A comissão foi configurada para descontos de 0 a 10%, mas o limite máximo de desconto permitido para o produto era de 5%. Isso impedia a exibição da tabela de comissão. Após ajustar a configuração da comissão para um limite de 4% (dentro do permitido), a informação passou a ser exibida corretamente.


---

## Caso 59

**Contexto**

Na versão 3.251.9, ao importar um orçamento que continha produtos com desconto para um pedido, os descontos não eram refletidos no saldo flex (conta corrente) do vendedor na aba "Totais". O mesmo processo na versão 3.239.2 funcionava corretamente.


**Solução / Diagnóstico**

Foi identificado que uma correção anterior (MXPEDDV-78829) alterou o comportamento para respeitar o parâmetro PERMITE_INICIAR_PEDIDO_COMO_ORCAMENTO_NAO_MOV_CC. Quando esse parâmetro está como 'S' (como no caso do cliente), a movimentação de conta corrente é desativada ao importar um orçamento, que é o comportamento esperado e corrigido. O comportamento na versão antiga estava incorreto.


---

## Caso 60

**Contexto**

O valor de vendas exibido no resumo do maxPedido para o RCA 73 (filtrado por departamentos 2 e 160) é de R$ 4.835,31. Uma consulta SQL direta na MXSHISTORICOPEDI para os mesmos filtros resultou em R$ 5.390,91, e um relatório do Winthor do cliente mostrou um valor muito maior (R$ 47.807,91).


**Solução / Diagnóstico**

Foi fornecida a query SQL completa que o backend e o aplicativo utilizam para alimentar o resumo de vendas. A query possui diversos filtros (ex: posicao, condvenda, codoperacao, parâmetros como CRITERIOVENDA e VALIDAR_APURACAO_NF) que não estão sendo considerados nas consultas de comparação do analista. Ao executar a query correta, o valor encontrado coincidiu com o do aplicativo. A orientação é explicar ao cliente que a comparação só é válida se os mesmos critérios de apuração forem usados em ambos os sistemas.


---

## Caso 61

**Contexto**

O cliente solicita que o campo CODDESCONTO seja gravado na tabela PCORCAVENDAI (e PCORCAVENDAC) quando um orçamento é salvo e enviado. Atualmente, segundo o cliente, o campo não é gravado.


**Solução / Diagnóstico**

Foi alinhado com o PO que se trata de uma melhoria. Atualmente, o maxPedido não grava essa informação nas tabelas de orçamento do cliente. O analista deve verificar se o cliente deseja seguir com o processo de abertura de um épico de melhoria.


---

## Caso 62

**Contexto**

O cliente quer ocultar qualquer informação de estoque. Já usa o parâmetro OCULTAR_INFORMACOES_ESTOQUE, mas a mensagem de alerta "Estoque insuficiente. Quantidade acima do disponível" ainda é exibida ao tentar vender mais do que o estoque. Ele quer remover essa mensagem e simplesmente permitir a venda.


**Solução / Diagnóstico**

Não é possível ocultar essa mensagem com a configuração atual. O parâmetro OCULTAR_INFORMACOES_ESTOQUE apenas oculta a quantidade de estoque na mensagem, não a mensagem em si. Como solução paliativa, foi sugerido o uso do parâmetro QUANTIDADE_MAXIMA_ESTOQUE, que permite burlar a validação de estoque, mas isso pode levar a vendas sem estoque real.


---

## Caso 63

**Contexto**

O analista pergunta se é possível ocultar a informação do preço de venda (PVENDA) que é exibida para cada item na tela de mix do cliente.


**Solução / Diagnóstico**

Atualmente, não existe uma opção (parâmetro ou permissão) para ocultar o campo PVENDA na tela de mix do cliente. Seria uma questão de melhoria.


---

## Caso 64

**Contexto**

Um cliente foi cadastrado via maxPedido pelo RCA 93. A integração retornou sucesso (status 4), e o cliente aparece na tabela PCCLIENT do banco local, mas não foi criado na MXSCLIENT do banco nuvem, portanto não aparece para o RCA.


**Solução / Diagnóstico**

A análise mostrou que o cadastro do cliente não foi autorizado no sistema e foi excluído do banco local. Por isso, mesmo com o status de sucesso na integração, o registro não subiu para a nuvem.


---

## Caso 65

**Contexto**

Após atualizar o ambiente, os valores na dashboard inicial (gráfico de vendas) não são apresentados, embora o resumo de vendas mostre vendas faturadas. O analista suspeita de permissões de acesso externo.


**Solução / Diagnóstico**

Para atualizar o gráfico do menu de vendas, é necessário cadastrar a meta mensal do RCA na Rotina 353 do Winthor. A tabela PCMETARCA estava vazia. O gráfico depende da meta mensal estar definida. Além disso, o parâmetro CRITERIOVENDA está como 'F', então só carrega vendas faturadas do mês atual. Como não há vendas faturadas do RCA no mês, a informação não é exibida.


---

## Caso 66

**Contexto**

Cliente excluiu uma campanha de desconto (201179), mas ela continua aparecendo no maxPedido para o RCA. Na base do zero a política não aparece, mas na base do RCA sim. No banco nuvem, a campanha está com código de operação 2 (deletado).


**Solução / Diagnóstico**

O analista ficou no aguardo da resposta do RCA para confirmar se a campanha ainda aparece após uma sincronização, já que em base do zero ela não é mais exibida. Se o problema persistir, deve ser encaminhado para o desenvolvimento como divergência de banco.


---

## Caso 67

**Contexto**

Analista pergunta qual tabela faz o vínculo dos grupos de clientes utilizados no campo `MXSPRECOPROM.CODGRUPOCLI` para políticas de preço fixo.


**Solução / Diagnóstico**

A integração desses grupos e sua relação com as campanhas é feita nas tabelas MXSGRUPOSCAMPANHAC e MXSGRUPOSCAMPANHAI. A relação para validação dos preços fixos é: MXSGRUPOSCAMPANHAC.codgrupo = mxsprecoprom.codgrupocli e MXSGRUPOSCAMPANHAI.coditem = codcli.


---

## Caso 68

**Contexto**

Ao transformar um orçamento em pedido, a margem de lucratividade muda drasticamente. O problema foi testado em várias versões, ocorrendo crash nas mais novas (3.251.8/9) e divergência de valores na versão do cliente (3.251.6).


**Solução / Diagnóstico**

A lucratividade muda porque o maxPedido recalcula os preços com base na informação mais atual na base do RCA. Isso é controlado pelo parâmetro QTDE_DIAS_VALIDAR_ORC_IMPORTACAO. Com valor 0 (padrão), o recálculo sempre ocorre. Uma solução paliativa é configurar este parâmetro para 7 dias. O crash nas versões mais novas foi encaminhado para o N3.


---

## Caso 69

**Contexto**

Cliente deseja que pedidos de brinde (TV5) sejam enviados para integração junto com o pedido principal (TV1), sem precisar aguardar a liberação do TV1 no ERP.


**Solução / Diagnóstico**

O comportamento atual do maxPedido é enviar a bonificação somente após o retorno do NUMPEDERP do pedido pai. Não há configuração para alterar isso, sendo uma possível melhoria. Uma novidade em desenvolvimento (sincronização automática) pode ajudar nesse cenário futuramente.


---

## Caso 70

**Contexto**

Cliente OERPs reporta que o roteiro de visitas não é gerado na tabela MXSCOMPROMISSOS, embora os registros existam na ERP_MXSROTACLI.


**Solução / Diagnóstico**

O problema era na geração dos compromissos no banco nuvem. Foi corrigido com a atualização do ambiente e a execução da job de compromissos. A agenda agora é gerada normalmente.


---

## Caso 71

**Contexto**

Há uma divergência no valor atendido (VLATEND) entre as tabelas MXSHISTORICOPEDC (nuvem) e PCPEDC (local) para o pedido 107005840. O cliente tem diversos registros pendentes para subir.


**Solução / Diagnóstico**

Foi realizada uma carga para normalizar o processo. O valor foi corrigido.


---

## Caso 72

**Contexto**

O maxPedido apresenta preço divergente da rotina 316 para produtos com tributação SUFRAMA quando um desconto é aplicado. Sem desconto, o cálculo funciona corretamente.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 73

**Contexto**

Pedidos já integrados (status 4) não atualizam o status na timeline do RCA, que usa sincronização automática e não pode fazer swipe.


**Solução / Diagnóstico**

O problema ocorria porque o usuário não estava configurado para sincronização automática. O campo USAMSGMAXSYNC na MXSUSUARIOS não estava como 'S'. Após ativar a configuração e reenviar os pedidos, a funcionalidade foi normalizada.


---

## Caso 74

**Contexto**

Cliente possui uma política de desconto da rotina 561 (CREDITASOBREPOLITICA = N, BASECREDDEBRCA = S). Ao aplicar um desconto (acréscimo negativo) após o desconto da política, é gerado saldo de conta corrente indevidamente. O cliente não quer que isso ocorra.


**Solução / Diagnóstico**

O conflito ocorre por conta da coluna ALTERAPTABELA da política, que estava como 'S'. Ao alterá-la para 'N', o desconto da política não movimenta a conta corrente, e o acréscimo também não, conforme desejado. A análise também esclareceu que o teto máximo de acréscimo é definido na MXSCONFIGERP (PERMAXVENDA).


---

## Caso 75

**Contexto**

Campo 'Data Entrega' (DataPrevisaoFaturamento) de um relatório personalizado não é preenchido em alguns pedidos, embora exista no JSON. O problema não é geral, pois funciona em outros pedidos.


**Solução / Diagnóstico**

A análise do código mostrou que o campo no relatório é populado pela coluna DTENTREGA. Não foi possível simular o erro, pois o pedido com problema (925004293) não estava na base do RCA. O analista solicitou a base que contém o pedido com falha para continuar a investigação.


---

## Caso 76

**Contexto**

Há uma divergência nos valores de histórico de compras para o RCA 62 e cliente 216. O valor no banco nuvem e na base do zero é R$ 87.130, mas na base do RCA e em um relatório do cliente os valores são diferentes (R$ 23.495,72 e R$ 107.326,10).


**Solução / Diagnóstico**

A funcionalidade de histórico é alimentada por uma job da Máxima com regras próprias (tabela MXSCLIENTCHARTHISTVENDA). A informação na base do RCA estava incorreta. Foi realizada uma carga da tabela MXSCLIENTCHARTHISTVENDA para corrigir. A orientação é que a comparação com o Winthor não é direta, pois o Winthor apura por data de faturamento, enquanto a funcionalidade do maxPedido tem seu próprio critério.


---

## Caso 77

**Contexto**

Títulos pagos não estão sendo baixados corretamente no aplicativo. Eles constam como pagos no Winthor e na ERP_MXSPREST, mas permanecem na tabela MXSTITULOSABERTOS, indicando falha na job de títulos.


**Solução / Diagnóstico**

Foi realizada uma carga para normalizar os títulos. O RCA deve sincronizar para validar.


---

## Caso 78

**Contexto**

Descontos em um pedido são tratados de forma diferente entre o maxPedido e a rotina 316 do Winthor. No maxPedido, o valor final do produto é R$ 109,42, enquanto no Winthor é R$ 109,50, o que faz a integração barrar o pedido por desconto acima do permitido.


**Solução / Diagnóstico**

O problema é de arredondamento. Para igualar o comportamento, devem ser configurados os parâmetros USAR_NUMCASASDECIMAIS_EXIBICAO_REAL = S e NUMCASASDECIMAIS_EXIBICAO com o mesmo número de casas decimais usado no Winthor (ex: 6).


---

## Caso 79

**Contexto**

Os produtos 19679 e 13751 não são exibidos ao iniciar um pedido na filial 6, embora apareçam no card de produtos. O analista suspeita de restrição de venda, mas o comportamento é inconsistente.


**Solução / Diagnóstico**

O problema não era restrição, mas sim a falta de informações de preço na tabela MXSTABPR para os produtos questionados. As colunas PVENDA, PVENDA1 e PTABELA estavam zeradas. Após inserir os valores via inspect, os produtos passaram a ser exibidos. O cliente deve ser orientado a enviar os preços corretos.


---

## Caso 80

**Contexto**

Ao exportar a pesquisa de produtos com fotos na Central de Configurações, o arquivo Excel é limitado a 2001 registros, embora a pesquisa retorne mais de 6000 produtos.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 81

**Contexto**

Após atualizar para a versão 3.252.1, a seleção de região na aba de produtos desaparece, gerando um erro. O problema não ocorria em versões anteriores.


**Solução / Diagnóstico**

O ticket foi encaminhado para o N3, pois se trata de um erro que será corrigido em uma nova versão.


---

## Caso 82

**Contexto**

Nenhum produto é exibido na base do RCA após sincronização, embora na base do zero os produtos apareçam normalmente.


**Solução / Diagnóstico**

Foi realizada uma carga, pois foi identificado que na base do RCA havia produtos com colunas de preço sem informação. O RCA deve sincronizar para que os produtos passem a ser exibidos.


---

## Caso 83

**Contexto**

Ao clicar em 'Atualizar menu', o sistema exibe o erro: 'Não foi possível atualizar o resumo de vendas'.


**Solução / Diagnóstico**

O erro ocorria por dois motivos: 1) Falta de cadastro das datas na Rotina 309 do Winthor (tabela PCDATAS). 2) O link do cliente T-Cloud no cadastro do extrator estava como 'http' em vez de 'https'. A correção exige que o cliente cadastre as datas na 309 e, após a correção do link, os usuários precisam relogar no maxSoluções.


---

## Caso 84

**Contexto**

O produto 801797 não aparece devido à divergência nas tabelas de embalagem (MXSEMBALAGEM) e produto por filial (MXSPRODFILIAL) entre o banco local e a nuvem.


**Solução / Diagnóstico**

Foi realizada uma carga nas tabelas questionadas. A informação agora consta no banco nuvem. O RCA deve sincronizar para visualizar o produto.


---

## Caso 85

**Contexto**

Ao tentar abrir um produto no maxPedido, é exibida a mensagem de erro de tributação. O erro não ocorre na rotina 316. Alterar a CODFILIALNF do cliente na MXSCLIENT para 1 resolve, mas o cliente deveria funcionar com a CODFILIALNF 3, que tem registros na MXSTABTRIB.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento, pois não foi possível fazer o debug no momento devido a problemas de acesso.


---

## Caso 86

**Contexto**

A legenda de 'produto em promoção' continua sendo exibida para um produto, mesmo após a política de desconto/preço fixo ter vencido ou sido removida da base da APK.


**Solução / Diagnóstico**

Foi alinhado na daily sobre os procedimentos e a situação foi resolvida em conjunto com o cliente.


---

## Caso 87

**Contexto**

O produto 2266 não é apresentado na aba 'Tabela'. O departamento do produto (1200) não existe no banco nuvem, embora exista no Winthor (PCDEPTO).


**Solução / Diagnóstico**

A análise mostrou que o departamento 1200 está classificado como 'IM' (imobilizado) no sistema de origem, o que impede sua integração com o força de vendas. Para que seja enviado, a classificação deve ser 'RT' (revenda de terceiros).


---

## Caso 88

**Contexto**

Analista pergunta se existe uma forma de a APK deletar orçamentos antigos automaticamente após um período (ex: 30 dias).


**Solução / Diagnóstico**

Atualmente, não existe um fluxo de exclusão automática de orçamentos. Há o parâmetro BLK_CONN_QTDEORCPENDENTE, que limita a quantidade de orçamentos salvos, mas não os exclui automaticamente por tempo. Quando o limite é atingido, o RCA precisa escolher quais orçamentos deletar manualmente.


---

## Caso 89

**Contexto**

O cliente configurou parâmetros para permitir que apenas a filial 5 possa iniciar orçamentos em clientes bloqueados (PERMITE_ORCAR_CLIENT_BLOQ e PERMITE_ORCAMENTO_CLIENTE_BLOQ = S para filial 5). No entanto, o RCA da filial 5 ainda não consegue iniciar o orçamento.


**Solução / Diagnóstico**

Após análise, foi constatado que os parâmetros PERMITE_ORCAMENTO_CLIENTE_BLOQ e PERMITE_ORCAR_CLIENT_BLOQ não aceitam configuração por filial, apenas por usuário ou geral. O teste com a configuração por usuário funcionou conforme esperado.


---

## Caso 90

**Contexto**

Após uma atualização para corrigir um problema de timeline, os pedidos do cliente (que usa sincronização automática) pararam de atualizar o status.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 91

**Contexto**

Ao importar uma planilha com cerca de 7 mil clientes para uma campanha de brinde na Central, o sistema informa que 1.4 mil não puderam ser importados, mas os que supostamente foram importados também não aparecem na tela.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 92

**Contexto**

O produto 1055 não aparece na base de nenhum vendedor, mas aparece na base do zero.


**Solução / Diagnóstico**

Foi realizada uma carga na tabela MXSPRODFILIAL, onde foi identificado que a informação sobre o produto não havia subido para a nuvem.


---

## Caso 93

**Contexto**

Os registros dos RCAs 2543 e 2544 não foram encontrados na tabela MXSUSUARIOS na nuvem, indicando falha na replicação.


**Solução / Diagnóstico**

O replicador do cliente estava parado desde 21/09/2024. Foi reativado, e os dados agora constam na nuvem. A causa raiz para a parada será investigada pelo N3.


---

## Caso 94

**Contexto**

Há uma grande divergência entre os títulos pagos e a previsão de comissão no relatório do Winthor (rotina 1248) e os valores exibidos na consulta de títulos do maxPedido para o RCA 214. A soma na tabela MXSTITULOSABERTOS se aproxima do valor do maxPedido.


**Solução / Diagnóstico**

A análise mostrou que a comparação com a rotina 1248 não é válida, pois ela é um relatório de comissão com critérios diferentes. O maxPedido consulta títulos por data de vencimento/pagamento, enquanto a 1248 usa data de baixa, e há diferenças entre valor do título e valor pago (juros/multa). A quantidade de títulos no maxPedido reflete a ERP_MXSPREST, que vem do ERP. A divergência é inerente aos diferentes critérios de apuração.


---

## Caso 95

**Contexto**

Cliente precisa obrigar o RCA a seguir a sequência de visitas do roteiro do dia, não permitindo pular clientes. As configurações testadas (permissão 'Obrigar sequenciamento de visitas' e parâmetro OBRIGAR_ATENDIMENTO_PARA_CHECKOUT) não funcionaram.


**Solução / Diagnóstico**

Para obrigar o sequenciamento, são necessárias as permissões na Central: 'Bloquear venda de clientes fora da rota = V' e 'Obrigar sequenciamento de visitas = V', além do parâmetro UTILIZA_CHECKIN_CHECKOUT = S. Com isso, o RCA será forçado a seguir a sequência da rota. Para atender clientes fora da rota, precisará gerar uma visita avulsa.


---

## Caso 96

**Contexto**

Uma solicitação de aumento de limite de crédito feita por um RCA não aparece no maxGestão nem na tabela MXSINTEGRACAOLIMCREDCLI, embora as permissões do supervisor e os parâmetros estejam configurados.


**Solução / Diagnóstico**

Após nova validação na versão mais recente do maxPedido, o fluxo funcionou normalmente. É provável que alguma configuração tenha sido ajustada pelo cliente durante o período de análise. O RCA deve ser orientado a atualizar o aplicativo.


---

## Caso 97

**Contexto**

Uma política de desconto cadastrada na Central para o cliente 37200 (produto 22164) não é listada no aplicativo, embora o preço do produto seja alterado, indicando que o desconto está sendo aplicado de alguma forma.


**Solução / Diagnóstico**

O problema era um erro de cadastro. A política foi configurada para a praça 26, mas o cliente em questão (37200) está vinculado à praça 1. Após ajustar a política para a praça 1, ela passou a ser exibida corretamente.


---

## Caso 98

**Contexto**

Analista pergunta se os parâmetros VERIFICAR_QTD_MAX_ITENS_PEDIDO e VERIFICAR_QTD_MAX_ITENS_PEDIDO_NRO funcionam por usuário.


**Solução / Diagnóstico**

Sim, ambos os parâmetros validam por usuário e também de forma geral.


---

## Caso 99

**Contexto**

O campo de código de fábrica aparece cortado na metade na listagem de produtos para um RCA com um celular Galaxy A01, embora apareça completo em outros aparelhos.


**Solução / Diagnóstico**

Foi alinhado com o PO que se trata de uma limitação de layout em telas pequenas. Uma solução de contorno é desabilitar a exibição do estoque contábil com o parâmetro EXIBIR_ESTOQUE_CONTABIL = N, liberando espaço na tela. Se o cliente precisar dessa informação, seria necessário abrir uma melhoria.


---

## Caso 100

**Contexto**

Após alterar o horário de execução do replicador, o cliente começou a enfrentar locks no banco de dados local, atribuídos ao replicador.


**Solução / Diagnóstico**

O horário foi revertido para as 18h. A causa do lock pode não estar diretamente relacionada ao replicador. Foi identificado e corrigido um erro de aumento de campo nas tabelas MXSUSUARIOS e MXSCOMPROMISSOS. O cliente deve reportar se o lock voltar a ocorrer para investigação em tempo real.


---

## Caso 101

**Contexto**

No relatório 8022 (Apuração de campanhas), o filtro 'CAMPANHA' não carrega os dados cadastrados no Winthor. O IIS e o portal admin estão configurados corretamente.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 102

**Contexto**

As faixas de comissão enviadas pelo cliente na tabela MXSFAIXACOMISSAOUSUR não são exibidas para o vendedor ao consultar a comissão do produto.


**Solução / Diagnóstico**

Para que o fluxo da tabela MXSFAIXACOMISSAOUSUR funcione, é necessário habilitar o parâmetro HABILITA_FAIXA_COMISSAO = S. Após ativá-lo, as comissões passaram a ser apresentadas.


---

## Caso 103

**Contexto**

Alterações nos vínculos de clientes com usuários (campos CODUSUR), feitas diretamente no banco ou na rotina 302, não estão subindo para o banco nuvem, mesmo após atualização do ambiente. Exemplo: cliente 9642.


**Solução / Diagnóstico**

Foi realizada uma carga para normalizar as informações. A orientação para o cliente é que alterações feitas diretamente via banco de dados não disparam as triggers de integração. Para que a alteração seja refletida na nuvem, é necessário que uma coluna de data de atualização (como DTULTALTER) seja modificada, o que normalmente ocorre ao salvar pela rotina. Se a alteração for via banco, o cliente deve forçar essa atualização de data para que o extrator capture a mudança.


---

## Caso 104

**Contexto**

Ao tentar cadastrar um novo cliente via APK, o campo e-mail é preenchido automaticamente pela busca de CNPJ, mas o sistema acusa erro e não permite salvar.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 105

**Contexto**

Após uma carga de dados para a filial 12, a filial aparece na base do vendedor e os produtos são exibidos, mas a filial 12 não fica disponível para seleção no cabeçalho do pedido.


**Solução / Diagnóstico**

O problema ocorre porque o cliente utiliza a tabela MXSTABPRCLI para vincular clientes a filiais de venda. Como a filial 12 não tinha vínculo nessa tabela para os clientes testados, ela não aparecia no spinner. Após inserir o vínculo na MXSTABPRCLI, a filial passou a ser exibida.


---

## Caso 106

**Contexto**

Mesmo com o RCA cumprindo todo o roteiro do dia anterior (15/10), o sistema bloqueou o início do roteiro no dia seguinte (16/10), exigindo desbloqueio. Este é um problema recorrente, já tratado no desenvolvimento (MXPEDDV-80135).


**Solução / Diagnóstico**

O problema foi causado por registros na MXSHISTORICOCOMPROMISSOS que foram deletados (codoperacao=2) na nuvem, mas a deleção não chegou à base do RCA via sincronismo. Uma carga foi feita para reenviar os registros de compromissos deletados. Agora, ao sincronizar, a base do RCA será normalizada. Além disso, o parâmetro PERMITIR_DELETE_HISTORICOCOMP foi desativado ( = N), pois seu uso interfere na validação de rota pendente.


---

## Caso 107

**Contexto**

O produto 11 apresenta divergência de preço entre a MXSTABPR (nuvem) e a PCTABPR (local). O cliente afirma que o problema é recorrente.


**Solução / Diagnóstico**

Foi realizada uma carga na MXSTABPR para normalizar o preço do produto 11.


---

## Caso 108

**Contexto**

O produto 17477 não aparece na base dos vendedores, embora apareça na base do zero.


**Solução / Diagnóstico**

Foi realizada uma carga interna, pois foi identificado que a tabela MXSTABPR na base do RCA não continha a informação de preço para o produto, impedindo sua exibição.


---

## Caso 109

**Contexto**

O extrator do cliente (OERPs) está em loop, reiniciando constantemente, e o hangfire fica offline. Já foi reinstalado, mas o problema persiste.


**Solução / Diagnóstico**

A causa do loop era a expiração da senha do banco de dados. O cliente foi orientado a contatar o DBA para atualizar a senha.


---

## Caso 110

**Contexto**

Após uma carga de filial nova (filial 12), o vínculo do cliente 14380 com a nova filial, cadastrado na PCTABPRCLI (rotina 3314), não subiu para a MXSTABPRCLI na nuvem.


**Solução / Diagnóstico**

Foi realizada uma carga para normalizar e igualar as informações do banco local com o nuvem. O vínculo com a filial 12 foi criado na nuvem.


---

## Caso 111

**Contexto**

As informações de última compra (data e quantidade vendida por mês) não são exibidas na aba 'Tabela' do pedido. O analista descobriu que a tabela MXSQTDEPRODVENDA não está sendo alimentada, embora o cliente não use o fluxo de mix, mas deseja ver essas informações.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento, pois se trata de uma falha na alimentação automática da tabela MXSQTDEPRODVENDA.


---

## Caso 112

**Contexto**

Ticket duplicado (clonado) do GATE-191.


**Solução / Diagnóstico**

Ticket clonado errado.


---

## Caso 113

**Contexto**

Há uma divergência nos títulos para o cliente 13169. Duplicatas como 327748 e 327763 estão associadas a numtransvenda incorretos no banco nuvem, causando a exibição de títulos pagos como em aberto.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 114

**Contexto**

O RCA 9231 não cumpriu todo o roteiro do dia 16/10, mas o aplicativo não bloqueou seu acesso no dia 17/10, como deveria, dado o parâmetro BLOQ_RCA_COM_ROTA_PENDENTE estar ativo. O analista notou que o roteiro do dia 16/10 não aparecia no app, embora existisse na MXSCOMPROMISSOS.


**Solução / Diagnóstico**

O problema foi causado pelo parâmetro PERMITIR_DELETE_HISTORICOCOMP = S. Com ele ativo, os compromissos e seus históricos são apagados. Como o roteiro do dia 16/10 foi apagado, o sistema não tinha referência para validar as pendências. O parâmetro foi desativado ( = N) para que a validação funcione corretamente nos dias seguintes.


---

## Caso 115

**Contexto**

Ao duplicar um pedido, o valor final fica diferente do original devido a uma mudança na porcentagem de desconto em alguns produtos. Em versões mais novas, ocorre um erro 'Infinity or NaN'.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 116

**Contexto**

O gráfico de metas não é gerado para o RCA 2444, mesmo com as metas cadastradas no banco nuvem.


**Solução / Diagnóstico**

A análise mostrou que o cálculo da meta no backend resultava em um valor negativo (R$ -0,3) após considerar as vendas e os dias úteis. Como o gráfico não exibe valores negativos ou zerados, ele não era gerado.


---

## Caso 117

**Contexto**

A meta de visitas criada na central não aparece no aplicativo. Ao acessar a aba de visitas, é exibida a mensagem 'ERRO AO CARREGAR INFO DE VISITAS'.


**Solução / Diagnóstico**

A funcionalidade de consulta de visitas no MaxPedido foi desenvolvida para mostrar dados de acordo com o Painel de Auditoria do MaxGestão. No cenário atual do cliente, não há informações de visitas (clientes visitados dentro do roteiro) para serem exibidas.


---

## Caso 118

**Contexto**

Ao cadastrar um cliente com um CEP específico (77063174), o maxPedido não reconhece o endereço e exibe erro, embora o CEP seja válido e retorne dados na consulta direta ao ViaCEP. O problema ocorre apenas com alguns CEPs.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 119

**Contexto**

Cliente opera com faixas de lucratividade (ex: até 15% salva, acima de 15,01% envia para autorização). Devido ao arredondamento com 6 casas decimais no maxPedido, valores como 15,000001% são tratados como acima de 15%, impedindo o salvamento. O analista questiona se há um parâmetro para arredondar para cima.


**Solução / Diagnóstico**

Atualmente, não existe um parâmetro que realize o arredondamento para cima conforme solicitado. O analista foi orientado a abrir um ticket de desenvolvimento diretamente, caso deseje essa melhoria.


---

## Caso 120

**Contexto**

Vários produtos vendidos para o cliente 135838 em outubro não geraram registros na tabela MXSPRODUTPOS (positivação de produtos). Apenas 4 registros, com status de deletado, existem.


**Solução / Diagnóstico**

O problema ocorre porque o cliente tem o parâmetro VALIDAR_APURACAO_NF = S e a integração não está enviando corretamente os dados das notas fiscais (ERP_MXSNFSAID) e movimentações (ERP_MXSMOV) vinculadas aos pedidos. Para resolver, o cliente pode desligar o parâmetro (VALIDAR_APURACAO_NF = N) para que a apuração considere apenas a MXSHISTORICOPEDC, ou corrigir o envio dos dados de nota fiscal.


---

## Caso 121

**Contexto**

Após uma carga nas tabelas de plano de pagamento (MXSCOBPLPAG, MXSPLPAG) para corrigir um erro, a correção funcionou ao sincronizar uma vez, mas ao refazer a carga e pedir nova sincronização, o RCA voltou a apresentar o erro de 'plano de pagamento não encontrado'.


**Solução / Diagnóstico**

Foi realizada uma carga interna em todas as tabelas envolvidas no processo de plano de pagamento (MXSCLIENT, MSXPLPAG, MXSCOB, MXSFILIAL, MXSPLPAGCLI, MXSCOBPLPAG). Aguarda-se o retorno do RCA para confirmar a correção.


---

## Caso 122

**Contexto**

O cliente gostaria que, ao marcar o checkbox 'Unidade Master' na tela de negociação, a quantidade fosse automaticamente preenchida com a quantidade da embalagem master (ex: 26). Atualmente, o campo permanece com 1, e o RCA só descobre a quantidade correta após uma mensagem de erro.


**Solução / Diagnóstico**

Atualmente, não existe uma forma automática para esse comportamento. A funcionalidade atual apenas valida se a quantidade informada é múltipla da quantidade da caixa master ao tentar inserir. O solicitado seria uma melhoria.


---

## Caso 123

**Contexto**

Uma campanha de desconto progressivo (ex: comprar no mínimo 12 unidades de uma família) não está validando quando a quantidade mínima é maior que 1. Funciona com quantidade 1, mas não com 12.


**Solução / Diagnóstico**

O campo 'Quantidade Mínima da Família' na configuração da campania se refere ao número de itens DIFERENTES dentro daquela família que precisam ser comprados. Se a família tem apenas um produto, a quantidade mínima deve ser 1. Para exigir 12 unidades do mesmo produto, a configuração correta é na 'Quantidade Mínima do Item', e não na quantidade da família.


---

## Caso 124

**Contexto**

Cliente utiliza um WMS de terceiros e precisa integrar os dados de validade ao maxPedido. Foi criada uma view no banco local, mas os dados não estão sendo integrados. Foi orientado a customizar a view PCVIEWVALIDADEWMS e ativar o parâmetro CUSTOMIZAR_VIEWWMS.


**Solução / Diagnóstico**

Foi realizada a configuração de customização da view no banco local. O fluxo agora é: a view personalizada alimenta a PCVIEWVALIDADEWMS, a job WMS é executada e popula a MXSVALIDADEWMS na nuvem. Os dados já estão no banco nuvem, bastando o RCA sincronizar.


---

## Caso 125

**Contexto**

Ao duplicar um pedido, o sistema não permite que o RCA altere a filial do novo pedido, mesmo mantendo o mesmo cliente.


**Solução / Diagnóstico**

Conforme demonstrado em vídeo, só é possível alterar a filial ao duplicar um pedido se todos os itens forem removidos primeiro. Isso ocorre porque filiais diferentes podem ter estoques, regras de tributação e preços diferentes, o que impossibilitaria a manutenção dos itens originais.


---

## Caso 126

**Contexto**

Para alguns clientes (ex: 9999), as filiais 2 e 3 não aparecem para seleção no cabeçalho do pedido, embora apareçam para outros clientes. O RCA tem todas as filiais liberadas.


**Solução / Diagnóstico**

A análise mostrou que o cliente 9999 tinha vínculo apenas com a filial 1 na tabela MXSTABPRCLI. Após deletar esse vínculo ou adicionar as filiais 2 e 3 na mesma tabela, as opções passaram a ser exibidas.


---

## Caso 127

**Contexto**

O cliente utiliza os parâmetros FORCAR_ATUALIZACAO_CADASTRO_CLIENTE e DIAS_ATUALIZACAO_CADASTRO_CLIENTE. Após um RCA atualizar os dados de um cliente e fazer um pedido, ao iniciar um novo pedido para o mesmo cliente, a aplicação solicita a atualização novamente.


**Solução / Diagnóstico**

A solicitação de atualização ocorre se o período desde a última atualização for maior que o configurado ou se o campo MXSCLIENT.DTULTALTER estiver nulo. No cliente testado (00729702), a DTULTALTER estava preenchida e dentro do prazo, e o fluxo funcionou normalmente. Se o problema persistir para outros clientes, é necessário um vídeo mostrando o fluxo e evidências de que a DTULTALTER não foi atualizada após a alteração.


---

## Caso 128

**Contexto**

Aparente duplicação de títulos na consulta do app para o mesmo cliente. A análise mostrou que a mesma duplicata (ex: 000074) está associada a dois números de transação diferentes (numtransvenda). Um deles é de um pedido de auto-serviço, que o cliente não integra ao maxPedido, mas o título foi gerado no ERP.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 129

**Contexto**

Ao duplicar um pedido e tentar alterar o plano de pagamento para E08, mantendo o preço informado, o maxPedido exibe uma mensagem de erro confusa sobre desconto máximo, mesmo o desconto aplicado (17,10%) sendo menor que o máximo informado (17,99%).


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 130

**Contexto**

Pedidos (1570981101, 1570981103) constam como faturados na PCPEDC (banco local), mas na MXSHISTORICOPEDC (nuvem) estão com posição 'M' (montado?) e o status não atualiza no app, mesmo em versão ponta.


**Solução / Diagnóstico**

A análise mostrou que os pedidos foram para filiais diferentes no ERP (30 e 7) do que as originalmente enviadas (32). Como a filial 32 não estava configurada na PCMXSINTEGRACAOPEDIDO para integração com o força de vendas, o status não retornou. O analista adicionou a filial 32 na configuração, mas é necessário confirmar com o cliente se essa filial deve ser usada no força de vendas.


---

## Caso 131

**Contexto**

A APK está permitindo que um pedido de bonificação (TV5) seja vinculado a um pedido do mês 7 que já foi faturado.


**Solução / Diagnóstico**

Existe o parâmetro PERMITE_VINCULAR_TV1_FATURADO_BNF que controla esse comportamento. Para que não seja possível vincular a pedidos faturados, ele deve estar configurado como 'N'.


---

## Caso 132

**Contexto**

Alguns produtos, como o 506153, não aparecem no maxPedido para o RCA 110, indicando uma divergência entre a base do RCA e a base do zero.


**Solução / Diagnóstico**

Foi realizada uma carga interna em todas as tabelas do fluxo do produto que estavam com informações faltantes na base do RCA. O RCA deve sincronizar para que os produtos passem a ser exibidos.


---

## Caso 133

**Contexto**

Cliente utiliza vínculos na PCTABPRCLI, vinculando clientes apenas à filial 1. No entanto, existem pedidos antigos feitos pela filial 3 que o RCA não consegue visualizar no histórico, recebendo uma mensagem de erro. O objetivo é apenas consultar o histórico, não fazer novos pedidos pela filial 3.


**Solução / Diagnóstico**

Atualmente, o aplicativo exige que a filial do pedido consultado esteja liberada para o RCA e presente na MXSFILIAL na base do aparelho para conseguir montar a consulta. Como a filial 3 não é liberada (não está na MXSFILIAL da base), a consulta falha. Permitir a consulta sem a filial liberada seria uma melhoria.


---

## Caso 134

**Contexto**

No relatório 'Visitas Previstas x Realizadas' do maxGestão, apenas um representante aparece no filtro, enquanto deveriam aparecer mais. A funcionalidade funcionava até a semana passada.


**Solução / Diagnóstico**

O problema foi causado por uma série de filtros na consulta. Para que um RCA apareça, ele precisa: 1) Estar vinculado a um supervisor que tenha COD_CADRCA preenchido na rotina 516. 2) O RCA deve ter uma licença do maxPedido ativa (status 'A' na MXSUSUARIOS) e estar vinculado a uma filial. O cliente precisa ajustar os cadastros dos supervisores e RCAs para que mais representantes sejam listados.


---

## Caso 135

**Contexto**

O cliente 18325 tem limite de crédito disponível, mas ao tentar fazer um pedido com o plano de pagamento '5 - 28 dias', o sistema impede de salvar, alegando que o limite foi excedido. O problema só ocorre com este plano.


**Solução / Diagnóstico**

O erro ocorria devido à interação do parâmetro BLOQ_ENVIO_PEDIDO_ACIMA_LIMITE = S com o campo VALIDALIMITECREDITO da tabela MXSCOB (que estava como null, interpretado como 'S'). Como o parâmetro BLOQ_SALVAR_PEDIDO_ACIMA_LIMITE_CLI_APK estava como 'N', o sistema tentava validar o limite, mas a configuração estava inconsistente. Após alterar BLOQ_SALVAR_PEDIDO_ACIMA_LIMITE_CLI_APK para 'S', o cálculo de limite passou a funcionar corretamente para o plano.


---

## Caso 136

**Contexto**

Cadastros de clientes feitos pelo aplicativo estão duplicando na rotina 302 do Winthor. O cliente usa o parâmetro HABILITA_PED_CLI_NAO_SINC. O analista questiona se o parâmetro está causando a duplicação.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento para uma segunda opinião.


---

## Caso 137

**Contexto**

As metas mensais cadastradas pela rotina 3305 não estão sendo apresentadas no aplicativo para nenhum RCA.


**Solução / Diagnóstico**

A solução foi habilitar os parâmetros UTILIZAR_META_TRANSMITIDA_EM_TIPO_ZERO = S e DEFINE_META_GRAFICO = 0. Após essa configuração, as metas passaram a ser exibidas.


---

## Caso 138

**Contexto**

Na filial 50, o desconto de 3% do plano de pagamento 79 não está sendo aplicado a um produto com preço fixo, embora funcione na filial 7. O valor na rotina 316 é R$ 1,87 (preço fixo R$ 1,93 - 3%), mas no maxPedido o valor fica em R$ 1,93.


**Solução / Diagnóstico**

O problema ocorre porque não existe uma política de preço fixo cadastrada para a filial 50 para o produto 44103, apenas para a filial 7. Após inserir uma política para a filial 50 via teste, o desconto passou a ser aplicado. O cliente deve verificar se os dados na PCPRECOPROM para a filial 50 estão sendo enviados corretamente para a nuvem.


---

## Caso 139

**Contexto**

Há uma divergência de valores entre o maxPedido e o maxPag para o pedido 801278. No maxPedido o valor é R$ 1.073,00, enquanto no maxPag, no JSON e na MXSINTEGRACAOPEDIDO o valor é R$ 1.219,32. O pedido não gerou NUMPEDERP.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 140

**Contexto**

O plano de pagamento 2 (PLPAG 2) está com o campo PERTCFIM divergente entre o banco local (-3%) e o banco nuvem (0%).


**Solução / Diagnóstico**

O ambiente foi normalizado com uma carga, igualando as informações.


---

## Caso 141

**Contexto**

Problema recorrente no cliente Muffato: pedidos bonificados (TV5) demoram muito para serem enviados para a nuvem após o pedido principal (TV1) ser processado pelo ERP, mesmo com sincronização automática. O pedido principal já tem histórico, mas a bonificação fica presa na APK.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 142

**Contexto**

Cliente reporta novamente que um RCA cumpriu todo o roteiro do dia anterior, mas o sistema bloqueou o acesso no dia seguinte. Desta vez, o roteirizador apontava 12 clientes para o dia 23/10, mas a MXSCOMPROMISSOS mostrava 15, causando a divergência.


**Solução / Diagnóstico**

O problema provavelmente será tratado como erro ou melhoria. A análise inicial indica que o cliente alterou a rota do RCA no dia 23/10 enquanto ela ainda estava vigente, e o sistema não tem um mecanismo para apagar o histórico dos compromissos de forma compatível com as remoções feitas. Foi encaminhado para desenvolvimento.


---

## Caso 143

**Contexto**

O produto 92656 não aparece para o RCA 956, embora apareça para outros e as tabelas principais pareçam ok.


**Solução / Diagnóstico**

O produto não aparece em alguns casos devido à região de precificação. O RCA tem acesso a várias regiões, mas o produto só está precificado em algumas delas (2, 12, 6, 8, 10, 11, 1). Se o cliente tentar vender para um cliente de uma região sem preço, ou consultar o card de produtos em uma região sem preço, o produto não será exibido. A solução é precificar o produto nas regiões desejadas.


---

## Caso 144

**Contexto**

Durante a migração da V2 para a V3, uma campanha de preço fixo cadastrada na Central para o produto 14377 (valor 24.49) não é apresentada na V3, mas funciona na V2.


**Solução / Diagnóstico**

Foi identificado que a query da V3 não trata informações de 'numregiao' nulas em políticas de preço fixo, ao contrário da V2. O ticket foi encaminhado para o N3 como erro, para alinhamento com o P.O., pois o cliente está em processo de migração.


---

## Caso 145

**Contexto**

O campo 'Observação de entrega' (OBSENTREGA) na MXSHISTORICOPEDC não está sendo exibido no aplicativo para o pedido 135751, mesmo após atualizações de versão e ambiente.


**Solução / Diagnóstico**

O problema era a configuração do parâmetro TAMANHO_OBS_ENT1, que estava com valor zero (padrão). Após configurá-lo para 600 caracteres, o campo passou a ser exibido corretamente.


---

## Caso 146

**Contexto**

Um relatório personalizado, cuja alteração foi combinada com um antigo desenvolvedor, ficou incompleto. O cliente solicita que o combinado seja cumprido: os valores de total produtos e IPI estão iguais, e deveriam ser diferentes (o valor do IPI deveria ser deduzido do total de produtos). Outras correções (endereço de entrega, formato da data) também foram solicitadas.


**Solução / Diagnóstico**

O analista foi orientado a entrar em contato diretamente com a supervisora do desenvolvimento backend para verificar a possibilidade de outro desenvolvedor assumir a tarefa pendente.


---

## Caso 147

**Contexto**

O produto 10742 possui apenas uma embalagem ativa para o força de vendas, mas na APK são apresentadas duas embalagens com a mesma descrição.


**Solução / Diagnóstico**

Foi realizada uma carga para igualar as informações entre o banco local e a nuvem, corrigindo a duplicidade.


---

## Caso 148

**Contexto**

Alguns produtos, como o 59, possuem uma imagem cadastrada, mas ao acessá-la, o que se vê é uma imagem padrão de 'indisponível' (fundo branco com os dizeres). Isso dificulta a identificação de quais produtos realmente têm problemas de imagem.


**Solução / Diagnóstico**

A análise mostrou que o próprio cliente fez o upload de uma imagem com os dizeres 'não disponível'. Não se trata de uma imagem padrão da Máxima. Portanto, não há como o sistema diferenciar automaticamente uma imagem real de uma imagem de 'placeholder' enviada pelo cliente. A única forma de saber se um produto não tem foto é quando não há registro na MXSPRODUTOSFOTOS.


---

## Caso 149

**Contexto**

A seleção múltipla de produtos está calculando a quantidade final de forma incorreta. Por exemplo, ao selecionar 2 caixas de um produto que tem 24 unidades por caixa, o resultado na aba de itens é 48, e não 2 caixas. O analista suspeita de uma multiplicação indevida pelo QTUNIT.


**Solução / Diagnóstico**

O comportamento observado está correto de acordo com a configuração do produto. Se 1 unidade no sistema equivale a 24 itens (caixa), ao selecionar 2, a quantidade inserida no pedido será de 48 itens. Isso se aplica tanto à seleção múltipla quanto à simples. O sistema está refletindo a configuração de unidade do produto.


---

## Caso 150

**Contexto**

O produto 46120023 não aparece na base dos RCAs 277, 324 e 372, embora apareça na base do zero.


**Solução / Diagnóstico**

A análise mostrou que não havia informação na tabela MXSPRODFILIAL nas bases desses RCAs para o produto 46120023. Foi realizada uma carga e os RCAs devem sincronizar para que o produto apareça.


---

## Caso 151

**Contexto**

A sincronização automática foi liberada para o cliente, mas o status dos pedidos não está atualizando, mesmo com o campo USAMSGMAXSYNC = S e os pedidos já constando como liberados na nuvem.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento para aplicação de uma solução.


---

## Caso 152

**Contexto**

Na base do RCA, o preço de alguns produtos está sendo exibido como o valor da embalagem, e não o valor unitário. Na base do zero, o valor estava correto. O problema persistiu mesmo após apagar a base.


**Solução / Diagnóstico**

O problema era devido ao campo QTUNIT da tabela MXSEMBALAGEM, que estava com valor 12 na base do RCA, enquanto deveria ser 1 para a exibição correta do valor unitário. Foi identificada uma divergência entre banco local e nuvem, e uma carga foi realizada para normalizar.


---

## Caso 153

**Contexto**

As informações de endereço (comercial e de entrega) de um cliente (119619) estão trocadas no aplicativo em comparação com a rotina 302 do Winthor. O cliente não concordou com a devolutiva anterior de que o erro estava no banco de dados local.


**Solução / Diagnóstico**

Após reanálise, foi confirmado que o banco nuvem reflete exatamente os dados do banco local. A divergência é entre a rotina 302 e a tabela PCCLIENT no banco local. O ticket foi encaminhado para o desenvolvimento para investigar a causa da informação trocada.


---

## Caso 154

**Contexto**

Títulos de 2022 para o cliente 4861 estão em aberto na ERP_MXSPREST (nuvem), mas não existem mais na PCPREST (local). O problema ocorre com outros clientes também.


**Solução / Diagnóstico**

Foi realizada uma carga nas filiais liberadas do cliente para igualar o banco local e a nuvem. O RCA deve sincronizar para que os títulos sejam corrigidos.


---

## Caso 155

**Contexto**

Mesmo com os parâmetros de bloqueio de rota pendente configurados (JUSTIFICAR_ROTEIRO_ANTERIOR=S, DIAS_VERIFICACAO_ROTEIRO_PENDENTE=1, etc.), a aplicação permite iniciar um pedido para um cliente do roteiro atual, mesmo havendo clientes sem justificativa no roteiro do dia anterior.


**Solução / Diagnóstico**

Faltava o parâmetro BLOQ_RCA_COM_ROTA_PENDENTE, que é o responsável por efetivamente bloquear a confecção de pedidos caso existam rotas pendentes dentro do período configurado. Após habilitá-lo, o bloqueio passou a funcionar.


---

## Caso 156

**Contexto**

Cliente utiliza preço fixo (MXSPRECOPROM) e planos de pagamento com desconto (PERTXFIM). Ele gostaria que o sistema aplicasse ambos os descontos (MXSPRECOPROM + PERTXFIM), mas atualmente só aplica o preço fixo e o IPI.


**Solução / Diagnóstico**

Atualmente, não existe configuração no sistema para somar automaticamente o desconto do plano de pagamento (PERTXFIM) a uma política de preço fixo. Testes com os campos ACEITADESCPRECOFIXO e validaracrescdescprecofixo não produziram o resultado esperado. O solicitado seria uma melhoria.


---

## Caso 157

**Contexto**

Pedidos cancelados no ERP (ex: 5100121233) não têm seu status atualizado no maxPedido, permanecendo como liberado.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento.


---

## Caso 158

**Contexto**

Informações de carregamento de pedidos feitos como 'balcão reserva' não estão sendo exibidas nos 'Dados do ERP' no aplicativo, embora existam na MXSHISTORICOPEDC. Testes na versão ponta não resolveram.


**Solução / Diagnóstico**

O problema ocorria porque o parâmetro ENVIA_PEDIDOS_BALCAO_RESERVA não estava cadastrado. Como a origem do pedido é 'R' (balcão reserva), esse parâmetro é necessário para que o histórico seja enviado corretamente. Foi cadastrado e o cliente deve fazer um novo pedido para testar.


---

## Caso 159

**Contexto**

Ao tentar usar a campanha de desconto 7709, que contém o item 164889, o sistema retorna erro informando que o item não possui tributação. A tributação existe na PCTABTRIB (Winthor), mas não na MXSTABTRIB (nuvem). O cliente já tentou reenviar a tributação, sem sucesso.


**Solução / Diagnóstico**

Foi identificado que havia um objeto inválido no banco. Após realizar o processo de liberação de permissão em algumas tabelas, o registro de tributação para o item 164889 subiu para a nuvem normalmente.


---

## Caso 160

**Contexto**

Um RCA específico (843) do perfil 700 está tendo seu pedido com cobrança de cartão de crédito rejeitado, com a mensagem de que não tem permissão para gerar link de pagamento. Outros RCAs do mesmo perfil não têm esse problema. O analista já removeu o plano PIX que estava indo no JSON incorretamente, mas o erro persiste.


**Solução / Diagnóstico**

A diferença entre os perfis 700 e 100 são as cobranças liberadas. O perfil 700 tem a cobrança de cartão de crédito liberada, o que automaticamente aciona o fluxo do maxPag. Para um RCA não usar o maxPag, a cobrança de cartão de crédito não deve ser liberada para ele, ou pode-se usar o parâmetro PERMITIR_VENDA_CARTAO_CREDITO por usuário para controlar quem pode usar essa forma de pagamento.


---

## Caso 161

**Contexto**

Há múltiplos problemas com uma cesta de natal (produto 251425): preço na listagem difere do preço na negociação, ao selecionar 'à vista' o preço muda para 79,58, e há mensagens de erro sobre preço mínimo e custo inválido. O analista não entende o funcionamento de cestas.


**Solução / Diagnóstico**

Para dar continuidade à análise, foi solicitada a origem de preço da rotina 316 para o produto, a fim de comparar com as informações recebidas pelo maxPedido e identificar possíveis divergências.


---

## Caso 162

**Contexto**

Para o cliente 13485, ao iniciar um pedido de bonificação, o item 183 carrega um múltiplo de 12 unidades. O mesmo não ocorre para o cliente 3558. O campo VALIDARMULTIPLOVENDA na MXSCLIENT está como 'N' para ambos.


**Solução / Diagnóstico**

O comportamento é controlado pelo campo ACEITAVENDAFRACAO na tabela MXSCLIENT. O cliente 13485 estava com este campo como 'S', permitindo a venda por múltiplos. Ao alterá-lo para 'N', o item passou a ser inserido com quantidade 1, igual ao cliente 3558.


---

## Caso 163

**Contexto**

O analista questiona de onde vem o valor de IPI de alguns produtos, pois na MXSTABPR o campo VLIPI está 0 em todas as regiões, mas ao consultar o produto no aplicativo, na aba imposto, é exibido o valor de 17,05.


**Solução / Diagnóstico**

O valor do IPI vem da tabela MXSPRODUT. Foi verificado que o cálculo é: 3,25 (percentual) / 100 = 0,325 x 524,63 = 17,05.


---

## Caso 164

**Contexto**

Os títulos não são apresentados corretamente na consulta do aplicativo. No cliente 5911, a MXSTITULOSABERTOS mostra dois títulos, mas o app exibe apenas um. A situação ocorre em outros cenários.


**Solução / Diagnóstico**

Foi analisado que o fluxo de títulos está de acordo com as informações enviadas. Para o RCA dalmo.sergio, aparece apenas um título para o cliente 5911 porque os outros títulos estão pagos (DTPAG preenchido) ou pertencem a outros RCAs. Para exibir títulos pagos, é necessário ativar o parâmetro EXIBIRTITULOSPAGOS = S.


---

## Caso 165

**Contexto**

Ao gerar um boleto, o código de barras apresenta problemas de leitura em aplicativos de bancos. O cliente testou em diferentes apps e a leitura não acontece.


**Solução / Diagnóstico**

Foi testado o documento anexado e a leitura do código de barras ocorreu com sucesso nos aplicativos Flash e Banco Itaú. O problema pode estar relacionado a boletos muito antigos, cuja linha digitável pode estar com defeito gerado no ERP. A informação de linha digitável vem do campo LINHADIG da PCPREST, que é integrada para a nuvem. Portanto, não é um problema do maxPedido.


---

## Caso 166

**Contexto**

O banco do cliente 'Reposit' está com alto processamento devido a vários processos do MAXSOLUCOES. Relatório AWR em anexo.


**Solução / Diagnóstico**

Baseado na análise do AWR, foram sugeridas a criação de índices e coleta de estatísticas para melhorar a performance. As instruções foram passadas para o cliente executar via DBA.


---

## Caso 167

**Contexto**

Na tabela ERP_MXSPREST, títulos abertos referentes ao período 30/05 a 09/06 divergem do banco local: banco nuvem tem 667 títulos, local apenas 16.


**Solução / Diagnóstico**

Foi realizada a carga e normalização das informações na tabela ERP_MXSPREST para o período indicado.


---

## Caso 168

**Contexto**

Há divergência de registros entre PCTABPR e MXSTABPR. Na MXSTABPR, preços zerados para alguns produtos, enquanto na PCTABPR há valores. Isso causa falta de exibição do produto no app.


**Solução / Diagnóstico**

O cliente manualmente na rotina 201 regravou o registro do preço, normalizando a divergência. As informações subiram para a nuvem.


---

## Caso 169

**Contexto**

O cliente envia as tabelas ERP_MXSNFSAID e ERP_MXSMOV para gerar dados na MXSQTDEPRODVENDA, mas a tabela não é gerada. Uma condição é que o campo ERP_MXSMOV.CODUSUR seja igual a ERP_MXSNFSAID.CODUSUR, mas mesmo com envio correto, a tabela não é gerada.


**Solução / Diagnóstico**

Foi alinhado com o desenvolvimento que, para OERPs, a integração deve enviar o codusur na ERP_MXSMOV. No caso de Winthor, o processo alimenta automaticamente. Portanto, o cliente deve ser orientado a enviar essa informação.


---

## Caso 170

**Contexto**

O preço de uma cesta no maxPedido está divergente da rotina 316. Na MXSPRECOCESTAI consta o preço correto, mas no app é exibido outro valor.


**Solução / Diagnóstico**

Foi identificado que existem dois preços para o mesmo CODPRODACAB, com diferentes CODPRECOCESTA. O aplicativo sempre pega o menor preço. Para corrigir, deve-se deletar o preço errado ou enviar codoperacao=2 para o registro incorreto e sincronizar.


---

## Caso 171

**Contexto**

Os status dos pedidos não atualizam para os RCAs e ficam divergentes do banco nuvem. Pedido consta como 'L' na MXSHISTORICOPEDC, mas não atualiza na base do RCA. Cliente usa sync automática.


**Solução / Diagnóstico**

O problema foi corrigido (questão de assinatura), mas a publicação oficial ainda não foi feita. Foi realizado o reenvio dos dados do pedido para o RCA receber a assinatura e atualizar o status. A correção definitiva será lançada posteriormente.


---

## Caso 172

**Contexto**

Preço de cesta no maxPedido divergente da rotina 316. Na tabela PCPRECOCESTAI e MXSPRECOCESTAI os valores estão corretos, mas no app é apresentado valor divergente (55,98 vs 53,98).


**Solução / Diagnóstico**

Existem dois códigos de preço cesta para o produto, e o app prioriza o menor valor. Se houver apenas um registro, o valor fica correto. Pode-se marcar codoperacao=2 no registro errado e sincronizar.


---

## Caso 173

**Contexto**

Divergência entre PCPREST e ERP_MXSPREST: na PCPREST, DTPAG e VPAGO estão preenchidos (pago), mas na ERP_MXSPREST e MXSTITULOSABERTOS não (pendente).


**Solução / Diagnóstico**

Foi realizada a carga conforme solicitado, normalizando a divergência.


---

## Caso 174

**Contexto**

Produto não aparece mesmo tendo precificação, estoque, acesso a fornecedor, departamento e seção, e sem restrições de venda. O produto consta na base do RCA, mas não é exibido.


**Solução / Diagnóstico**

O produto é FL (fora de linha) e o parâmetro OCULTAR_PROD_FORA_LINHA estava como 'S'. Alterando o parâmetro ou a observação do pedido, o produto passa a ser exibido.


---

## Caso 175

**Contexto**

Os dados do resumo de vendas da filial 6 não são apresentados na aba de departamento (zerado).


**Solução / Diagnóstico**

Foi realizada análise e, na última versão, o resumo de vendas está gerando valores normalmente. Pode ter sido algo pontual no momento do teste.


---

## Caso 176

**Contexto**

Pedidos bonificados gerados automaticamente não são apresentados no histórico de pedidos. O pedido 3380001429 consta na MXSHISTORICOPEDC do vendedor, mas não aparece no app.


**Solução / Diagnóstico**

Foi feita simulação e o pedido bonificado é apresentado corretamente. Como o pedido existe na MXSHISTORICOPEDC, ao sincronizar o RCA, ele será puxado.


---

## Caso 177

**Contexto**

Extrator Tcloud offline e banco Winthor inacessível.


**Solução / Diagnóstico**

Houve uma instabilidade na nuvem da TOTVs, que foi normalizada. Os logs da integração mostram que já está funcionando. Se voltar a ocorrer, o cliente deve procurar a TOTVs.


---

## Caso 178

**Contexto**

Clientes não aparecem na base do RCA (LDN.34). Em base zero aparecem, mas na base do RCA não.


**Solução / Diagnóstico**

Foi realizada carga interna e os clientes foram normalizados. Solicitar ao RCA que sincronize e, se ainda não aparecer, verificar filtros no celular.


---

## Caso 179

**Contexto**

Algumas fotos de produtos não são processadas na job de fotos do ponto de montagem da NORDIL. Os caminhos são válidos no Linux, mas a job não gera registro na MXSPRODUTOSFOTOS.


**Solução / Diagnóstico**

Existia um problema com imagens em status 'notfound'. Foi alterado o diretório na stack do portainer para um inválido, forçando a remoção das fotos no S3 e banco nuvem. Depois, retornou-se ao diretório original e a job foi disparada novamente, subindo todas as fotos corretamente. Para produtos com erro de extensão (.jpeg vs .JPG), é necessário ajustar o cadastro.


---

## Caso 180

**Contexto**

Ao consultar produtos na aba 'Produtos', a APK não retorna registros na versão ponta, mas na versão 3.257.0 funciona. Na aba tabela os produtos são exibidos normalmente.


**Solução / Diagnóstico**

Já existe um ticket no desenvolvimento sobre o assunto (MXPEDDV-85633). Orientar o cliente a não usar a versão ponta até a correção ser publicada.


---

## Caso 181

**Contexto**

Pedido de R$16.000 (numped 19471392) foi pago via PIX, mas não chegou ao ERP. O motivo original era data de previsão de faturamento incompatível. Após tentar reenviar, o pedido entrou em loop no maxPag gerando novo link.


**Solução / Diagnóstico**

Foi ajustado manualmente: setado status do pedido para 0, permitindo o envio ao ERP. O pedido foi integrado e gerou críticas de corte. O corte será estornado automaticamente quando o pedido for faturado. O parâmetro PRAZO_VALIDADE_PEDIDO foi ajustado para 30 dias (deve ser retornado para 7 após resolução).


---

## Caso 182

**Contexto**

Não há permissão na central de configurações para reenviar pedido bloqueado. O cliente quer remover essa permissão dos RCAs.


**Solução / Diagnóstico**

Atualmente não existe permissão ou parâmetro exclusivo para reenvio de pedidos. A ação de reenviar está vinculada à edição do pedido. Caso o cliente queira uma funcionalidade específica, seria necessário uma melhoria.


---

## Caso 183

**Contexto**

Ao justificar visita em cliente fora de rota, mesmo salvando a justificativa, o sistema não autoriza o check out.


**Solução / Diagnóstico**

É necessário configurar o parâmetro UTILIZA_HORA_APARELHO_JUSTIFICATIVA_VISITA.


---

## Caso 184

**Contexto**

Produto não aparece para o RCA, embora haja preço na MXSTABPR para as filiais que o RCA tem acesso, estoque e permissões corretas.


**Solução / Diagnóstico**

O cliente 522931 utiliza MXSTABPRCLI, com regiões diferentes por filial NF. Na filial 2, não há preço para a região 10 para o produto, por isso não aparece. Na filial 5 funciona normalmente.


---

## Caso 185

**Contexto**

Produto 1505.0 não pode ser inserido em pedido na filial 1, retornando erro de tributação. Outros produtos funcionam. Testes em base zero com cliente 10106.


**Solução / Diagnóstico**

O produto estava sem CODST na MXSTABPR. Após incluir o código de tributação, passou a funcionar.


---

## Caso 186

**Contexto**

Planos de pagamento para o cliente 10201: na PCPLPAGCLI existem 4 registros, mas na MXSPLPAGCLI apenas 2, causando falta de planos no app.


**Solução / Diagnóstico**

Provavelmente, na carga de filial, a opção 'Clientes' não foi habilitada, impedindo a descida dos vínculos. Foi realizada carga de dados para normalizar a MXSPLPAGCLI. Além disso, foi fornecido um script para corrigir objetos inválidos no banco do cliente.


---

## Caso 187

**Contexto**

Após queda de energia, o menu do maxPedido parou de atualizar. A porta 9002 está acessível, mas a atualização falha.


**Solução / Diagnóstico**

Embora a porta estivesse aberta para teste local, a comunicação entre o servidor da Máxima (AWS) e o cliente estava bloqueada. O acesso internacional à porta 9002 estava inacessível, impedindo a atualização do menu. O cliente precisa liberar o acesso externo.


---

## Caso 188

**Contexto**

Produtos similares exibidos no APK são diferentes dos cadastrados na MXSPRODSIMIL (cliente GBM).


**Solução / Diagnóstico**

Teste realizado na última versão mostra a listagem de acordo com o esperado. As análises do ticket anterior se aplicam.


---

## Caso 189

**Contexto**

Na aba 'Movimentação' do pedido, algumas informações (data de montagem, faturamento, conferente) não são exibidas, enquanto data de digitação aparece.


**Solução / Diagnóstico**

As informações vêm da MXSHISTORICOPEDC. O script que carrega a movimentação foi fornecido em anexo.


---

## Caso 190

**Contexto**

É possível configurar o sistema para que, ao ultrapassar a quantidade de pedidos fora de rota (QTD_MAX_PED_FORA_ROTA), seja solicitada senha de autorização?


**Solução / Diagnóstico**

Atualmente não existe ligação entre o parâmetro QTD_MAX_PED_FORA_ROTA e a permissão de autorização. Seria uma melhoria a ser desenvolvida.


---

## Caso 191

**Contexto**

Plano de pagamento 045, com valor mínimo de pedido R$300, não bloqueou pedido de R$60.


**Solução / Diagnóstico**

O parâmetro BLOQUEAR_PEDIDO_ABAIXO_MIN_PLANO_PAGAMENTO não estava ativo. Após ativá-lo, a validação passou a funcionar.


---

## Caso 192

**Contexto**

Status de pedidos não atualizam pela sincronização automática. Pedidos com posição F na MXSHISTORICOPEDC permanecem como L na base do RCA.


**Solução / Diagnóstico**

Foi feito procedimento para normalizar os status dos pedidos. O RCA deve validar.


---

## Caso 193

**Contexto**

Resumo de vendas não atualiza para alguns RCAs (14565, 16024, 98229), mesmo com portas 9000/9002 liberadas. Para outros RCAs funciona.


**Solução / Diagnóstico**

Existe um bloqueio de acesso internacional. O Hangfire do cliente não está acessível de fora do Brasil, o que impede a atualização do resumo de vendas, pois a requisição passa por servidores nos EUA. A liberação deve ser feita pelo cliente.


---

## Caso 194

**Contexto**

Quantidade de clientes positivados no app é 15, mas na MXSHISTORICOPEDC há 61 registros. A MXSCLIENTPOS também tem 15.


**Solução / Diagnóstico**

Foi feita carga para normalizar as informações. Agora a quantidade apresentada deve condizer com os registros da MXSCLIENTPOS.


---

## Caso 195

**Contexto**

Cadastro de cliente (CPF 738.627.703-20) pelo aplicativo não integra com Winthor, retornando crítica de código cliente já existente. O código nuvem 182 já existe na MXSCLIENT.


**Solução / Diagnóstico**

A crítica veio da integradora (status 14). Mesmo deletando registros na PCPEDCFV, a crítica antiga persiste. O cliente deve enviar o cadastro novamente. O ambiente da Máxima está ok, pois outros cadastros no mesmo período foram bem-sucedidos.


---

## Caso 196

**Contexto**

Ao iniciar pedido para o cliente 2922, mensagem de inconsistência: nenhum plano de pagamento carregado. Verificações nas tabelas de vínculo não apontam causa.


**Solução / Diagnóstico**

O cliente 2922 tem plano 15 e cobrança 2 (Dinheiro) cadastrados. Na tabela MXSCOBPLPAG, a cobrança 2 só pode ser usada com o plano 11. Portanto, deve-se alterar o plano do cliente para 11, ou usar cobrança 4 (Boleto) com plano 15.


---

## Caso 197

**Contexto**

Valores de frete cadastrados na MXSCLIENT (VLFRETE=45, VLMAXCOBFRETE=800) não são aplicados no pedido. O frete permanece 0.


**Solução / Diagnóstico**

Para que o frete seja aplicado, é necessário que o parâmetro FORCAR_UTILIZACAO_FRETE_CLIENTE esteja 'N', o campo mxsclient.fretedespacho = 'C', e na filial mxsfilial.tipofreteauto = 'C'. Além disso, para o campo de valor do frete ficar visível, o parâmetro CON_INCLUIDESPRODAPENF deve ser 'S'.


---

## Caso 198

**Contexto**

Registros da PCTABPRCLI para a filial 11 não desceram para a nuvem; apenas um registro consta na MXSTABPRCLI, enquanto há vários no banco local.


**Solução / Diagnóstico**

Havia objetos inválidos na carga nuvem. Após resolver e recompilar, as informações foram integralizadas normalmente.


---

## Caso 199

**Contexto**

Na MXSHISTORICOPEDI do pedido 517261, PTABELA e PVENDA são iguais, mas na ERP_MXSLOGRCA foi adicionado valor de 220 (2,20 por unidade do produto 176), alterando a conta corrente indevidamente.


**Solução / Diagnóstico**

O sistema utiliza o parâmetro USAR_CCRCA_MAXIMA e a movimentação é baseada nas informações do pedido. No JSON, o campo 'PrecoVendaInformado' era 13,80, mas o histórico registrou 16,00. Isso ocorreu porque havia uma política de desconto automática (13,75% sobre R$16,00) que resultou em R$13,80, gerando movimentação de conta corrente. Se não deveria haver movimentação, o ERP deveria ter enviado o preço de venda correto no histórico.


---

## Caso 200

**Contexto**

Após migrar da V2 para V3, ao tentar inserir o produto 12111.0 no cliente 201864, ocorre erro de tributação. O produto 4281.0 funciona.


**Solução / Diagnóstico**

O cliente utiliza processo de filial retira. Para iniciar pedido com filial 1, é necessário ter liberação no portal. Foi constatado que o RCA não tinha permissão para a filial 1. Após liberar, o produto passou a ser inserido normalmente.


---

## Caso 201

**Contexto**

Permissão de acesso a cobrança já foi marcada na central, mas na base do RCA não atualiza, impedindo iniciar pedido. Em base zero funciona.


**Solução / Diagnóstico**

Foi constatado que a RCA não conseguiu sincronizar a cobrança 'BK' na tabela MXSCOB. Foi feita uma normalização de dados; ao sincronizar, a informação será recebida. Recomenda-se atualizar a versão, pois há correção que reenvia informações com falha de download.


---

## Caso 202

**Contexto**

No pedido 183006815, o percentual de juros do plano de pagamento 22 deveria ser 3% (PERTX), mas o aplicativo aplicou 6,7%. Cliente insistiu que o problema é o frete.


**Solução / Diagnóstico**

Não foi identificada divergência. O pedido foi aceito pela integradora e está com status Liberado. Sugere-se validar na rotina 316 se há diferença no valor praticado. Sem evidências claras, não há ação da Máxima.


---

## Caso 203

**Contexto**

Fornecedor 701 e seus produtos não são exibidos na APK. Ao vincular o produto a outro fornecedor (695), ele aparece. RCA tem acesso a todos os fornecedores.


**Solução / Diagnóstico**

O problema já havia sido resolvido pelo cliente, que fez os vínculos corretamente.


---

## Caso 204

**Contexto**

API de cancelamento do cliente Tcloud não funciona, mesmo com todas as informações corretas. Pedido é cancelado no app mas permanece com posição L na MXSHISTORICOPEDC.


**Solução / Diagnóstico**

O problema era a configuração do IP no extrator. Foi necessário colocar o IP sem a porta, pois o acesso só funciona assim. Após ajuste e reinicialização, o cancelamento passou a funcionar. Parâmetros ajustados: UTLIZA_API_CANCEL_WINTHOR = S (para todos), e PERMITE_CANCELAR_PEDIDO_ERP deixado em geral NULL.


---

## Caso 205

**Contexto**

Alerta de preço mínimo só aparece quando o preço é zero. Inserindo valores abaixo do mínimo (3,00), o produto é inserido sem alerta. Parâmetros VALIDAR_PRECO_MINIMO_201 e CON_VALIDAPRECOMINIMO estão 'S'.


**Solução / Diagnóstico**

O parâmetro ACEITADESCTMKFV na MXSPARAMFILIAL estava ativado, permitindo descontos acima do máximo permitido. Desativando-o, a validação de preço mínimo passou a funcionar.


---

## Caso 206

**Contexto**

Pedidos de origem telemarketing (ORIGEMPED = T) não são enviados para a MXSHISTORICOPEDC, mesmo com ENVIA_PEDIDOS_TELEMARKETING habilitado na PCMXSCONFIGURACOES e ambiente atualizado.


**Solução / Diagnóstico**

A ativação do parâmetro só afeta pedidos futuros. Para pedidos retroativos, é necessária carga. Foi realizada carga da PCPEDC e PCPEDI referente às filiais 1 e 3 do mês passado e atual.


---

## Caso 207

**Contexto**

Cliente deseja que clientes bloqueados possam fazer pedidos à vista. Testes com parametrização não funcionam. O sistema permite pedidos com boleto, quando deveria bloquear.


**Solução / Diagnóstico**

Atualmente, com o parâmetro BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE ativo, não há forma de permitir apenas venda à vista; é uma melhoria em andamento (MXPEDDV-82146). Como contorno, pode-se desativar o parâmetro, permitindo vendas à vista. A exibição de várias cobranças ocorre porque os campos de nível de venda estão iguais para todas.


---

## Caso 208

**Contexto**

Título duplicata 186134 está pago no banco local, mas na nuvem DTPAG e VPAGO estão vazios, aparecendo como devido.


**Solução / Diagnóstico**

A duplicata foi marcada com codoperacao=2 na MXSTITULOSABERTOS e será removida na próxima execução da job. Foi feita carga interna; o RCA deve sincronizar.


---

## Caso 209

**Contexto**

Pedidos estão sumindo do menu de pedidos para alguns RCAs, aparecendo apenas no histórico. Exemplo: pedido 3802108600.


**Solução / Diagnóstico**

Na base anexada, o pedido aparece normalmente. Pode ser algum filtro no aparelho. Sugere-se fazer backup, limpar dados do app, importar base novamente. Se persistir, reabrir com vídeo.


---

## Caso 210

**Contexto**

Produto 96777 não aparece no maxPedido. Não existe na MXSTABPR, mas existe na PCTABPR.


**Solução / Diagnóstico**

Havia objetos inválidos e falta de grants. Após normalização, a informação subiu para a MXSTABPR. O RCA deve sincronizar.


---

## Caso 211

**Contexto**

Pedidos de clientes (ex.: 5523) estão sendo gerados na filial 1, mas deveriam ser apenas na filial em que são negociados. O app disponibiliza ambas as filiais.


**Solução / Diagnóstico**

Para restringir, pode-se usar a Rotina 3314 (PCTABPRCLI) para vincular cliente a uma filial/região específica, ou a Rotina 391 (PCRESTRICAOVENDA) para cadastrar restrição por cliente e filial. Ambas funcionam no maxPedido.


---

## Caso 212

**Contexto**

Campos 'Posição financeira', 'Contatos', 'Referências comerciais' não desabilitam na central de configurações, mesmo tentando ocultá-los.


**Solução / Diagnóstico**

Atualmente não é possível ocultar essas abas; são padrão do sistema. Para ocultá-las, seria necessária uma melhoria.


---

## Caso 213

**Contexto**

Valores do resumo de vendas não batem com o ERP para o vendedor Cláudio (RCA 7348) no mês de dezembro. Análise mostra divergência nas tabelas.


**Solução / Diagnóstico**

O cálculo do resumo de vendas utiliza informações dos endpoints MXSHISTORICOPEDC, MXSHISTORICOPEDI, etc. A divergência pode ocorrer por diversos fatores (dedução de devoluções, impostos, data de apuração). A Máxima forneceu os dados em Excel para comparação. A correção deve ser feita na integração do ERP, enviando os dados corretos.


---

## Caso 214

**Contexto**

Duplicata 669805 foi baixada no Winthor, mas no banco nuvem ainda consta pendente (DTPAG e VPAGO vazios).


**Solução / Diagnóstico**

Foi realizada normalização dos registros. A duplicata foi marcada com codoperacao=2 e será removida na próxima job. O problema ocorreu devido a falha 'ORA-06508' no passado, que impedia a subida dos dados. Após correção, foi feita a carga retroativa.


---

## Caso 215

**Contexto**

Conta corrente do vendedor não apresenta dados. Parâmetros verificados, tabela ERP_MXSLOGRCA vazia.


**Solução / Diagnóstico**

As informações subiram normalmente para a base da APK. A conta corrente aparece zerada porque o cálculo é feito com base em movimentações. O SQL que calcula a diferença foi fornecido.


---

## Caso 216

**Contexto**

Pedidos abaixo de R$200 não são salvos devido a mensagem de valor mínimo, mas a cobrança BKBB está configurada com valor mínimo R$100. No app, ainda aparece R$200.


**Solução / Diagnóstico**

O valor de R$200 está vindo do parâmetro CON_VLMINVENDABK da MXSPARAMFILIAL, que tem prioridade sobre os valores individuais da cobrança. Alterando esse parâmetro, a validação passa a usar o valor correto.


---

## Caso 217

**Contexto**

Para clientes da 'Rede Mais', o RCA está negociando produtos com preço diferente do que aparece na base do zero. Duas políticas comerciais não estão refletidas na base do RCA.


**Solução / Diagnóstico**

Foi realizada carga interna nas tabelas do fluxo. O RCA deve sincronizar para receber as atualizações.


---

## Caso 218

**Contexto**

Pedidos do RCA (3201016992, 3201016993, 3201016994) não aparecem no app, embora constem na MXSINTEGRACAOPEDIDO. RCA não tem permissão para deletar.


**Solução / Diagnóstico**

Os pedidos não estão na tabela MXSPEDIDO, portanto não aparecem na timeline. Possíveis causas: exclusão manual, importação de base antiga, limpeza de dados. Recomenda-se ativar o parâmetro 'PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO' para restaurá-los a partir do histórico. Se o cliente discordar, solicitar vídeo comprovando exclusão automática.


---

## Caso 219

**Contexto**

Em orçamentos, é possível aplicar qualquer desconto (até 100%), sem bloqueio. Em pedidos, o desconto é limitado ao PERDESCMAX da MXSTABPR.


**Solução / Diagnóstico**

O orçamento utiliza o parâmetro CON_PERMAXDESCVENDA da MXSPARAMFILIAL (rotina 132). Alterando esse parâmetro, é possível limitar o desconto também em orçamentos. No entanto, mesmo que o orçamento permita, ao enviar o pedido a validação será feita.


---

## Caso 220

**Contexto**

Faixas de comissão cadastradas na MXSCOMISSAOPLPAG não são exibidas para o plano de pagamento 2, mas são exibidas para o plano 4, no mesmo cenário.


**Solução / Diagnóstico**

Faltavam informações na MXSCOMISSAOPLPAG. Após ajuste, as faixas passaram a ser exibidas normalmente.


---

## Caso 221

**Contexto**

Valores exibidos no maxGestão para vendas transmitidas divergem da rotina 146 do Winthor. Exemplo: maxGestão mostra R$201.231,48, rotina 146 mostra R$198.689,30.


**Solução / Diagnóstico**

A rotina 146 considera o valor da capa (VLATEND) da PCPEDC, enquanto o maxGestão soma os itens (QT*PVENDA) da PCPEDI. Essa diferença é esperada e ocorre quando há divergência entre capa e itens. Para venda faturada (rotina 111), os dados devem bater. Se o cliente desejar comportamento diferente, seria uma melhoria.


---

## Caso 222

**Contexto**

Ao fazer pedido com o item 29825, a integradora rejeita pois o CODAUXILIAR 10061 não existe na PCEMBALAGEM, apenas na MXSEMBALAGEM. Divergência entre as tabelas.


**Solução / Diagnóstico**

Foi feita normalização do produto e da filial 2. Foram adicionados logs na trigger de embalagens para rastrear futuras divergências. Os logs serão mantidos por tempo limitado. O RCA deve sincronizar e, se o item estiver com embalagem errada no pedido, removê-lo e reinseri-lo.


---

## Caso 223

**Contexto**

RCAs estão conseguindo enviar pedidos com valor abaixo da restrição de R$300. Exemplo: pedido 64220005. Em base do zero, o sistema bloqueia.


**Solução / Diagnóstico**

Análise dos JSONs mostrou que o número da região no pedido era 0, provavelmente devido a algum problema no momento da criação. Quando a região não é capturada, a restrição não é aplicada. Se o problema se repetir, é necessário capturar a base no momento da ocorrência para depuração.


---

## Caso 224

**Contexto**

O cliente reporta que um vendedor específico tem 71 dias sem visitar um cliente, mesmo tendo feito um pedido recentemente. O analista verificou que a informação de dias sem visita não atualiza.


**Solução / Diagnóstico**

A informação que atualiza o campo de dias sem visita é a coluna dtultcomp da tabela MXSCLIENT, que estava desatualizada. Foi feita a atualização manual dessa informação e orientado o RCA a sincronizar o aplicativo para refletir a mudança.


---

## Caso 225

**Contexto**

O cliente deseja ocultar a aba de títulos pendentes no cadastro do cliente no MaxPedido. O analista quer saber se é possível.


**Solução / Diagnóstico**

Sim, é possível ocultar a aba de títulos pendentes utilizando o parâmetro CLIENTE_EXIBIR_TITULOS. Deve-se configurá-lo como 'Não' na central de configurações. Após alterar, o RCA precisa sincronizar o MaxPedido para que a aba seja ocultada.


---

## Caso 226

**Contexto**

Uma indenização (NUMINDENIZACAO 80254) foi criada no MaxPedido, retornou crítica de sucesso, mas não aparece nas tabelas do Winthor (PCINDC, PCINDCFV, PCINDIFV). O analista encontrou o registro apenas na MXSINTEGRACAOINDENIZACAO.


**Solução / Diagnóstico**

O problema ocorre porque o numindenizacao gerado pelo MaxPedido (baseado no PROXNUMPEDFORCA) é convertido para codindeniz no Winthor. Esse código já existia previamente no banco (PCINDCFV), impedindo a gravação. A causa é um conflito de numeração, que deve ser resolvido no cadastro da Rotina 517, garantindo que o PROXNUMPEDFORCA não gere números já utilizados.


---

## Caso 227

**Contexto**

O pedido 528221828 foi pago via MaxPag e processado no ERP, mas no portal MaxPag ainda consta como 'Pré-Aprovado'. O analista quer entender por que o status não atualizou.


**Solução / Diagnóstico**

O fluxo do MaxPag funciona com pré-autorização no momento do pagamento. A autorização final só ocorre após o faturamento completo do pedido. Se o pedido ainda está com status 'Liberado' (não faturado), pode sofrer cortes, então o status permanece como pré-aprovado até a conclusão do faturamento. Não é um erro, é o comportamento esperado.


---

## Caso 228

**Contexto**

O resumo de vendas não atualiza para dezembro de 2024, exibindo 'Sem dados', embora o Hangfire esteja funcionando. O analista verificou que as metas existem nas tabelas ERP_MXSMETA e ERP_MXSMETARCA.


**Solução / Diagnóstico**

A falta de dados na tabela ERP_MXSDATAS para o mês de dezembro de 2024 impedia a atualização do resumo de vendas. É necessário que o cliente cadastre as datas na rotina apropriada para que os dados sejam carregados.


---

## Caso 229

**Contexto**

Ao tentar inserir itens no cliente 18748, todos os produtos retornam erro de tributação, mesmo após verificação das tabelas de tributação. O analista não encontrou inconsistências aparentes.


**Solução / Diagnóstico**

As informações de tributação no banco nuvem foram atualizadas recentemente. O RCA deve sincronizar o aplicativo para receber as atualizações e resolver o erro de tributação.


---

## Caso 230

**Contexto**

O status de pedidos não atualiza automaticamente para múltiplos usuários, mesmo após correções anteriores. O pedido já está faturado no banco, mas permanece com status de envio no RCA.


**Solução / Diagnóstico**

Foi feito o reenvio dos dados dos pedidos para o RCA de forma paliativa para que ele receba as informações corretas. O problema foi encaminhado para investigação mais aprofundada, mas a solução imediata foi o reenvio manual dos dados.


---

## Caso 231

**Contexto**

O produto 29476.0 não aparece para o RCA 132 em qualquer cliente, embora exista na base e tenha todas as permissões necessárias. O analista suspeita de algum bloqueio.


**Solução / Diagnóstico**

O produto estava com estoque deletado (codoperacao = 2) na tabela MXSEST, o que impedia sua exibição. Após uma validação com estoque inserido, o produto apareceu normalmente. O cliente deve verificar a situação do estoque no ERP.


---

## Caso 232

**Contexto**

O plano de pagamento 3, liberado para o vendedor na central de configurações, não é exibido para o cliente 850, mas aparece para o cliente 894. O analista verificou as tabelas de vínculo e não encontrou inconsistências.


**Solução / Diagnóstico**

O comportamento está correto. O cliente 850 tem como plano padrão o 28, com prazo médio de 5 dias, então apenas planos com prazo menor ou igual a 5 são exibidos. Já o cliente 894 tem plano padrão 16 (prazo 21 dias), exibindo planos com prazo até 21 dias. A exibição segue a regra de prazos baseada no plano padrão do cliente.


---

## Caso 233

**Contexto**

O produto 001934-7 recebe um acréscimo de 10 centavos ao alterar o plano de pagamento, enquanto outros produtos não. O analista espera que o preço permaneça em 5,09.


**Solução / Diagnóstico**

A divergência de 1% (10 centavos) era causada pelo campo fatorpreco na tabela mxsembalagem para esse produto. Ao excluir ou zerar esse fator, o preço se iguala aos demais produtos. O cliente deve ajustar a embalagem do produto no ERP.


---

## Caso 234

**Contexto**

Diversos produtos com histórico de venda nos últimos 3 meses não aparecem na sugestão de venda para o cliente 8701. O analista questiona o que pode estar gerando essa situação.


**Solução / Diagnóstico**

A sugestão de venda considera as últimas 3 vendas de um produto no último mês. Se o produto não teve pelo menos 3 vendas nesse período, ele não entra na sugestão. No caso do produto 3310, houve apenas 2 vendas, justificando sua ausência.


---

## Caso 235

**Contexto**

Em pedidos salvos e bloqueados, a autorização de preço (rotina 301) não é carregada, mesmo após sincronização. O RCA precisa duplicar o pedido para que a autorização apareça. O analista questiona se esse é o comportamento correto.


**Solução / Diagnóstico**

Esse comportamento é considerado um erro. O esperado é que a autorização seja carregada mesmo em pedidos salvos e bloqueados após sincronização. O ticket foi encaminhado para análise do time de desenvolvimento (N3) por se tratar de uma falha.


---

## Caso 236

**Contexto**

Os produtos similares exibidos no MaxPedido para o produto 9259 são diferentes dos cadastrados na MXSPRODSIMIL. O analista testou parâmetros e não conseguiu igualar.


**Solução / Diagnóstico**

O produto similar é baseado na MXSPRODSIMIL, mas passa por validações adicionais: o produto deve existir na MXSPRODUT e ter preço na MXSTABPR para as regiões do cliente. No exemplo, os produtos 3047 (inexistente) e 1736 (sem preço para a região) não aparecem, explicando a divergência.


---

## Caso 237

**Contexto**

Pedidos estão sendo enviados duplicados para a MXSINTEGRACAOPEDIDO, enquanto na base do RCA consta apenas um. O problema ocorre esporadicamente e já havia acontecido em versões anteriores.


**Solução / Diagnóstico**

O problema foi identificado como duplicação de requisições no backend. O ticket foi encaminhado para N3 para investigação, pois pode ser um bug no aplicativo que envia requisições duplicadas para salvar os pedidos.


---

## Caso 238

**Contexto**

O produto 1505.0 não pode ser inserido em pedidos na filial 1 devido a erro de tributação. Outros produtos funcionam normalmente. O analista realizou diversos selects e não encontrou problemas.


**Solução / Diagnóstico**

O produto não possuía código de situação tributária (codst) preenchido na MXSTABPR. Após o preenchimento, o erro de tributação foi resolvido. O cliente deve verificar o cadastro de tributação do produto no ERP.


---

## Caso 239

**Contexto**

Poucos planos de pagamento aparecem para o cliente 10201. Na PCPLPAGCLI existem 4 registros, mas na MXSPLPAGCLI apenas 2. O analista suspeita de divergência de dados.


**Solução / Diagnóstico**

A divergência ocorreu porque, durante a carga inicial, a opção 'Clientes' não foi habilitada, impedindo que os vínculos da PCPLPAGCLI fossem para a nuvem. Foi realizada uma carga de dados para normalizar a MXSPLPAGCLI. Além disso, foram identificados objetos inválidos no banco, que devem ser corrigidos com um script específico fornecido.


---

## Caso 240

**Contexto**

Após uma queda de energia, o menu do MaxPedido parou de atualizar. As portas 9002 estão acessíveis, mas a atualização falha.


**Solução / Diagnóstico**

O problema foi identificado como inacessibilidade da porta de comunicação do servidor do cliente a partir da infraestrutura da Máxima (AWS). O fluxo de atualização de menu faz uma chamada do servidor da Máxima para o cliente, e a porta estava bloqueada. O cliente deve verificar as configurações de firewall para liberar o acesso externo.


---

## Caso 241

**Contexto**

O cliente quer que as informações de movimentação do pedido (data de montagem, faturamento, etc.) no MaxPedido correspondam às da rotina 335 do Winthor. O analista precisa saber de onde vêm essas informações.


**Solução / Diagnóstico**

As informações da aba 'Movimentação' do pedido são provenientes da tabela MXSHISTORICOPEDC. O script de consulta utilizado pelo MaxPedido foi fornecido em anexo para referência.


---

## Caso 242

**Contexto**

O cliente deseja que, ao ultrapassar a quantidade de pedidos fora de rota definida pelo parâmetro QTD_MAX_PED_FORA_ROTA, o sistema solicite uma senha de autorização para desbloqueio. O analista testou e o bloqueio ocorre sem autorização.


**Solução / Diagnóstico**

Atualmente, o parâmetro QTD_MAX_PED_FORA_ROTA e a permissão 'Solicitar autorização para atender cliente fora de rota' são fluxos independentes. Não há ligação entre eles no código. Para que a autorização seja solicitada ao atingir o limite, seria necessária uma melhoria no sistema. Portanto, o comportamento observado está correto para a versão atual.


---

## Caso 243

**Contexto**

O plano de pagamento 045 possui valor mínimo de pedido de R$300, mas o sistema permitiu a criação de um pedido de R$60. O analista verificou que o campo VLMINPARCELA não existe na MXSPLPAG.


**Solução / Diagnóstico**

A validação do valor mínimo do plano de pagamento depende do parâmetro BLOQUEAR_PEDIDO_ABAIXO_MIN_PLANO_PAGAMENTO, que não estava ativo. Após ativá-lo, o sistema passou a bloquear pedidos abaixo do mínimo. O cliente deve habilitar esse parâmetro na configuração.


---

## Caso 244

**Contexto**

O resumo de vendas não atualiza para alguns RCAs, embora as portas 9000 e 9002 estejam liberadas e funcione para outros. O analista suspeita de bloqueio.


**Solução / Diagnóstico**

Foi identificado um bloqueio de acesso internacional. O servidor da Máxima (AWS) está nos EUA, e ao tentar acessar o hangfire do cliente a partir desse ambiente, ocorre timeout, indicando um firewall que bloqueia conexões internacionais. O problema é de infraestrutura do cliente e deve ser resolvido por ele.


---

## Caso 245

**Contexto**

O filtro de comissão diferenciada no MaxPedido não está funcionando como o cliente espera. Ele quer saber como configurá-lo e se ele funciona.


**Solução / Diagnóstico**

O filtro de comissão diferenciada funciona no MaxPedido através dos parâmetros OPERADOR_COMISSAO_DIFERENCIADA e PERCENTUAL_COMISSAO_DIFERENCIADA. O operador define a condição (>, <, >=, etc.) e o percentual o valor de comparação. O sistema compara com as comissões cadastradas na MXSPRODUT (PCOMREP1, PCOMINT1, PCOMEXT1). Quando ativado, o filtro exibe apenas os produtos que atendem à condição.


---

## Caso 246

**Contexto**

O resumo de vendas não atualiza para os usuários 14565, 16024 e 98229, embora as portas estejam liberadas. O analista suspeita de bloqueio.


**Solução / Diagnóstico**

Assim como no GATE-559, o problema é um bloqueio de acesso internacional. O hangfire do cliente não é acessível a partir dos servidores da Máxima (AWS). A solução é o cliente liberar o acesso em seu firewall para conexões originadas fora do país.


---

## Caso 247

**Contexto**

O campo de desconto no boleto gerado pelo MaxPedido está em branco, mesmo com informações na tabela. O analista quer saber por que.


**Solução / Diagnóstico**

O problema foi identificado como uma falta de mapeamento da variável de desconto no relatório personalizado. O ticket foi encaminhado para N3 para correção.


---

## Caso 248

**Contexto**

A quantidade de clientes positivados mostrada no MaxPedido (15) é diferente da encontrada na MXSHISTORICOPEDC (61). O analista suspeita de divergência.


**Solução / Diagnóstico**

Foi realizada uma carga de dados para normalizar as informações da MXSCLIENTPOS. Após a carga, a quantidade apresentada no aplicativo deve se igualar à do banco nuvem. O RCA precisa sincronizar para ver a atualização.


---

## Caso 249

**Contexto**

Um cadastro de cliente (CPF 738.627.703-20) feito pelo aplicativo não integra com o Winthor, retornando crítica de código de cliente já existente. O analista verificou que o código 182 já existe na MXSCLIENT.


**Solução / Diagnóstico**

A crítica de código já existente foi retornada pela integradora do cliente, não pela Máxima. O registro no banco da Máxima estava correto. A solução é o cliente reenviar o cadastro, pois o erro era pontual na integração. Outros cadastros no mesmo período foram bem-sucedidos.


---

## Caso 250

**Contexto**

Ao tentar iniciar um pedido para o cliente 2922, o sistema informa inconsistência nos dados e que nenhum plano de pagamento pôde ser carregado. O analista verificou as tabelas de plano e cobrança, mas não encontrou a causa.


**Solução / Diagnóstico**

O problema ocorre devido ao vínculo restritivo na tabela MXSCOBPLPAG. O cliente 2922 tem como padrão o plano 15 e cobrança 2, mas a cobrança 2 (Dinheiro) só pode ser usada com o plano 11 (à vista). Para resolver, o cliente deve alterar o plano padrão do cliente para 11 ou selecionar uma cobrança compatível (ex: boleto) no momento do pedido.


---

## Caso 251

**Contexto**

A API de cancelamento de pedidos não funciona para o cliente T-Cloud, mesmo com as informações de IP, usuário e senha corretas. O analista testou com e sem porta.


**Solução / Diagnóstico**

O problema era a configuração do IP no extrator do cliente. Foi necessário utilizar o IP sem a porta (http://201.157.197.15/) porque, no ambiente do cliente, a porta do WTA não está liberada para acesso externo. Após ajuste e reinicialização do extrator, a API de cancelamento passou a funcionar.


---

## Caso 252

**Contexto**

O sistema não está bloqueando descontos abaixo do preço mínimo, a menos que o preço seja zero. Os parâmetros VALIDAR_PRECO_MINIMO_201 e CON_VALIDAPRECOMINIMO estão como 'S', e o preço mínimo está definido como 3,0.


**Solução / Diagnóstico**

O parâmetro ACEITADESCTMKFV da MXSPARAMFILIAL estava ativado, permitindo descontos acima do máximo permitido. Ao desativá-lo, o sistema passou a respeitar o preço mínimo. Esse parâmetro vem da rotina 132 do Winthor e deve ser ajustado pelo cliente conforme sua necessidade.


---

## Caso 253

**Contexto**

Pedidos de origem telemarketing (ORIGEMPED = T) não estão sendo enviados para a MXSHISTORICOPEDC, mesmo após habilitar o parâmetro ENVIA_PEDIDOS_TELEMARKETING. O analista fez ambiente atualizado, mas pedidos antigos não subiram.


**Solução / Diagnóstico**

A ativação do parâmetro ENVIA_PEDIDOS_TELEMARKETING só faz com que novos pedidos sejam enviados. Para os pedidos retroativos, é necessária uma carga manual. Foi realizada a carga da PCPEDC e PCPEDI referente aos meses passados e atual para que os dados sejam integrados à nuvem.


---

## Caso 254

**Contexto**

O cliente quer que clientes bloqueados por inadimplência possam fazer pedidos à vista, mas o sistema permite pedidos com outras cobranças. Ela afirma que isso funcionava antes. O analista verificou os parâmetros e encontrou uma melhoria em aberto.


**Solução / Diagnóstico**

Atualmente, não existe uma forma de restringir pedidos de clientes inadimplentes apenas a pagamentos à vista utilizando o parâmetro BLOQUEIA_PEDIDO_CLIENTE_INADIMPLENTE. O comportamento esperado é que, com esse parâmetro ativo, o pedido seja bloqueado independentemente da cobrança. A funcionalidade desejada é uma melhoria (MXPEDDV-82146). Como alternativa, o cliente pode desativar o parâmetro, permitindo que clientes inadimplentes façam pedidos à vista, mas isso liberará todas as cobranças.


---

## Caso 255

**Contexto**

Um título (duplicata 186134) aparece como em aberto no MaxPedido, mas está pago no Winthor. O analista verificou que na nuvem os campos DTPAG e VPAGO estão vazios.


**Solução / Diagnóstico**

Foi realizada uma normalização do registro, setando codoperacao = 2 na MXSTITULOSABERTOS, o que indica que o título foi baixado e deve ser removido do MaxPedido. A job de atualização de títulos rodará em breve, e após sincronizar, o título deixará de aparecer para o RCA.


---

## Caso 256

**Contexto**

O pedido 3802108600 não aparece na timeline de pedidos do RCA, embora exista na base de dados e não tenha sido deletado. O analista suspeita de um bug.


**Solução / Diagnóstico**

O pedido aparece normalmente ao importar a base fornecida em outro aparelho. A causa provável no dispositivo do RCA pode ser um filtro ativo ou alguma inconsistência local. Recomenda-se fazer backup da base, limpar os dados do app, importar uma base nova e depois restaurar a base original. Se o problema persistir, o RCA deve ser orientado a gravar um vídeo do ocorrido para análise.


---

## Caso 257

**Contexto**

O produto 96777 não aparece no MaxPedido. Ele existe na PCTABPR do Winthor, mas não na MXSTABPR da nuvem. O analista suspeita de necessidade de carga.


**Solução / Diagnóstico**

Foram identificados objetos inválidos e falta de grants no banco local. Após a normalização e carga, o produto foi integrado à MXSTABPR. O RCA deve sincronizar para que o produto apareça no aplicativo.


---

## Caso 258

**Contexto**

O cliente deseja restringir que determinados clientes façam pedidos em uma filial específica (ex: cliente 5523 não deve usar a filial 1). O analista quer saber como configurar isso.


**Solução / Diagnóstico**

Existem duas formas no Winthor que são integradas ao MaxPedido: 1) Rotina 3314 (PCTABPRCLI), que vincula o cliente a uma filial e região de preço específicas. 2) Rotina 391 (PCRESTRICAOVENDA), que permite cadastrar restrições por cliente e filial. Ambas devem funcionar no MaxPedido para restringir a seleção de filial no momento do pedido.


---

## Caso 259

**Contexto**

O resumo de vendas do vendedor Claudio não bate com o valor do ERP para dezembro. O analista verificou as tabelas de histórico e os valores não conferem.


**Solução / Diagnóstico**

O cálculo do resumo de vendas da Máxima utiliza os dados enviados pelo ERP nos endpoints MXSHISTORICOPEDC e MXSHISTORICOPEDI. A divergência pode ocorrer por vários motivos (deduções, impostos, data de apuração). A análise detalhada mostra que o cálculo da Máxima é consistente. Para resolver, o integrador do cliente deve comparar os dados enviados com os do ERP e corrigir o que estiver sendo enviado incorretamente. Foi fornecido o script de apuração da venda faturada para auxiliar na comparação.


---

## Caso 260

**Contexto**

Uma duplicata (669805) está baixada no Winthor, mas permanece pendente no banco nuvem. O analista verificou que na ERP_MXSPREST ainda consta como pendente.


**Solução / Diagnóstico**

Foi realizada a normalização do registro, setando codoperacao = 2, o que garante que o título seja dado como baixo no MaxPedido. O problema ocorreu devido a uma falha na job de integração no passado. A job de atualização de títulos rodará em breve, e o título sumirá do aplicativo após sincronização.


---

## Caso 261

**Contexto**

Ao tentar realizar pedidos com o item 29825, a integradora rejeita, informando que o CODAUXILIAR 10061 não existe na PCEMBALAGEM. Esse código existe apenas na MXSEMBALAGEM da nuvem.


**Solução / Diagnóstico**

Foi feita a normalização do produto 29825 e adicionados logs na trigger de embalagens para monitorar futuras divergências. A embalagem errada foi excluída. O RCA deve sincronizar, remover o item do pedido (se a embalagem ainda estiver errada) e reinseri-lo antes de transmitir. A causa exata não foi identificada, mas os logs ajudarão em ocorrências futuras.


---

## Caso 262

**Contexto**

Alguns RCAs estão conseguindo enviar pedidos com valores abaixo do limite de R$300 definido em uma restrição. O analista não conseguiu reproduzir o problema em base zero.


**Solução / Diagnóstico**

A análise dos JSONs dos pedidos mostrou que, nos casos problemáticos, o campo 'região' estava com valor 0. Isso provavelmente fez com que a restrição (que é por região) não fosse aplicada. A causa raiz não foi identificada, mas orienta-se que, se o problema voltar a ocorrer, o RCA envie a base imediatamente para que seja possível depurar.


---

## Caso 263

**Contexto**

Os descontos não estão sendo aplicados aos itens no pedido, mesmo após cadastro das políticas. O analista verificou que na versão 561 os descontos funcionam.


**Solução / Diagnóstico**

Foi realizado um procedimento para sincronizar os descontos na base do RCA. Após a sincronização, o problema deve ser resolvido. O RCA deve ser orientado a sincronizar e validar.


---

## Caso 264

**Contexto**

Pedidos estão sendo gravados na PCPEDC, mas não aparecem na MXSHISTORICOPEDC. Exemplo: pedido 119219089. O analista suspeita de problema na integração.


**Solução / Diagnóstico**

O pedido já foi integrado automaticamente com posição 'F'. Provavelmente, o problema ocorreu porque o cliente estava em uma versão de banco anterior à alteração na TRIGGER que envia os registros para a MXSHISTORICOPEDC. Após a atualização do banco local, os registros integraram normalmente. O ambiente está funcional.


---

## Caso 265

**Contexto**

A data de vencimento dos produtos não aparece no aplicativo na opção 'dados adicionais'. O cliente abriu chamado na TOTVS informando que a consulta deveria ser na PCLOTE, não na PCPRODUT.


**Solução / Diagnóstico**

A informação de data de vencimento nos dados adicionais vem da MXSPRODUT.dtvenc. Para exibir informações da MXSLOTE (lotes), é necessário cadastrar o parâmetro LISTAR_INFO_LOTES, que habilita a opção 'Listar lotes' no menu '+infos' do produto. O cliente deve cadastrar esse parâmetro e os RCAs sincronizarem para utilizar a funcionalidade.


---

## Caso 266

**Contexto**

Pedidos do tipo balcão reserva não aparecem no histórico de pedidos (aba Consultas), mas aparecem na timeline. O analista quer saber se é erro.


**Solução / Diagnóstico**

O problema era que os parâmetros de balcão reserva estavam configurados como 'Não'. Após alterá-los para 'Sim', os pedidos passaram a ser exibidos no histórico de pedidos. O analista deve orientar o cliente a ajustar os parâmetros.


---

## Caso 267

**Contexto**

O cliente deseja entender o fluxo de comissão no MaxPedido, incluindo endpoints e tabelas envolvidas. O analista abriu o ticket para análise.


**Solução / Diagnóstico**

Foi fornecida uma explicação detalhada sobre o funcionamento da comissão no MaxPedido, incluindo: permissões necessárias, parâmetros (HABILITA_FAIXA_COMISSAO), endpoints para faixa de comissão (MXSFAIXACOMISSAOUSUR), comissão por produto (MXSPRODFILIAL.PCOMREP1, etc.), e comissão por RCA (MXSCOMISSAOUSUR). Também foram esclarecidos os pontos sobre o resumo de vendas e a origem dos dados (MXSHISTORICOPEDC ou ERP_MXSNFSAID).


---

## Caso 268

**Contexto**

Um pedido foi confeccionado fora de rota/raio sem solicitar autorização de desbloqueio, mesmo com as permissões de bloqueio ativas. O analista questiona o que permitiu isso.


**Solução / Diagnóstico**

Quando não existe rota cadastrada para o cliente, o sistema não solicita autorização para pedido fora de rota nem validação de raio. Isso não é um erro, mas uma característica do fluxo. Para validar check-in fora do raio, seria necessário usar o parâmetro GPS_EDGE_BLOCK (cerca eletrônica), mas isso não é aconselhável para vendedores autônomos por questões jurídicas.


---

## Caso 269

**Contexto**

Duas políticas de desconto foram excluídas no ERP, mas ainda aparecem no MaxPedido. O analista testou em base zero e elas não aparecem, indicando divergência.


**Solução / Diagnóstico**

Foi realizado o processo de carga interna para sincronizar as exclusões. O RCA deve ser orientado a sincronizar o aplicativo para que as políticas excluídas deixem de ser exibidas.


---

## Caso 270

**Contexto**

O cliente questiona por que todos os clientes estão mostrando o plano de pagamento de 7 dias no cabeçalho do pedido, em vez do plano vinculado a cada cliente. O analista já havia explicado o comportamento, mas o cliente insiste.


**Solução / Diagnóstico**

Quando o cliente não usa as tabelas MXSCOBPLPAG e MXSPLPAGCLI, o sistema carrega o plano do cadastro do cliente (MXSCLIENT). Se esse plano estiver inativo ou o RCA não tiver acesso, o sistema carrega o primeiro plano ativo disponível. No caso do cliente 4076, o plano padrão 133 não existe na base do RCA, então o sistema carrega a cobrança 'O748' e ordena os planos que o RCA possui acesso. Isso explica a exibição do plano de 7 dias para todos.


---

## Caso 271

**Contexto**

Pedidos com origem telemarketing não estão sendo enviados para as tabelas MXSHISTORICOPEDC e MXSHISTORICOPEDI. O analista já ativou o parâmetro ENVIA_PEDIDOS_TELEMARKETING e precisa de carga retroativa.


**Solução / Diagnóstico**

Foi realizada a carga dos dados retroativos para incluir os pedidos de telemarketing nas tabelas de histórico. Após a carga, os dados foram conferidos no banco nuvem.


---

## Caso 272

**Contexto**

O produto 701 apresenta o valor unitário dividido (ex: valor 84,99, valor UN 44,50). O analista quer entender o motivo.


**Solução / Diagnóstico**

Isso ocorre porque o produto tem QTUNIT = 2 na MXSPRODUT, e a permissão 'Exibir valor total' está desabilitada. Para exibir o valor cheio, o cliente pode habilitar essa permissão na central de configurações ou alterar o produto para QTUNIT = 1 na rotina 201.


---

## Caso 273

**Contexto**

O produto 1580 não aparece no MaxPedido. Ele existe na MXSPRODFILIAL, mas não na MXSPRODUT. O analista já fez carga, mas não subiu.


**Solução / Diagnóstico**

O produto não subia porque estava com o campo revenda = 'N' no cadastro. Após o cliente alterar para 'S', o produto foi integrado normalmente à nuvem e passou a aparecer.


---

## Caso 274

**Contexto**

O relatório de metas não é gerado para alguns RCAs, embora a meta conste no banco nuvem e os dias úteis estejam cadastrados. O analista suspeita de erro.


**Solução / Diagnóstico**

O gráfico de metas no menu inicial só é gerado para metas cadastradas na rotina 3304. Metas cadastradas na rotina 3304 não aparecem no gráfico, apenas na aba 'fornecedor' do resumo de vendas. O comportamento está de acordo com o esperado.


---

## Caso 275

**Contexto**

O status de pedidos não atualiza na sincronização automática, mesmo com os pedidos já integrados no ERP. O analista verificou que o pedido 5696 foi integrado, mas o status não reflete.


**Solução / Diagnóstico**

O problema estava relacionado à integração do ERP, que não estava enviando as informações no formato correto (ex: numPedidoERP com '0' na frente, tamanho do campo, falta de dados no MXSHISTORICOPEDC). Foram reforçadas as orientações para o integrador sobre os requisitos. O fluxo do maxSync estava desligado, o que também contribuiu.


---

## Caso 276

**Contexto**

A campanha 42 está incluindo o produto 4244, que não deveria fazer parte dela. O analista verificou as tabelas e não encontrou o produto vinculado.


**Solução / Diagnóstico**

O problema ocorre porque a campanha existe na MXSDESCONTOC, mas não possui itens na MXSDESCONTI. Se no banco local a PCDESCONTOI também estiver vazia, a campanha não funcionará nem na 316. O cliente deve verificar se os itens foram excluídos no ERP e recadastrá-los, se necessário.


---

## Caso 277

**Contexto**

O campo 'PrecoTabelaSemImpostos' no JSON do pedido está sendo enviado com valor multiplicado (4968) na versão 3.268.3, enquanto na versão 3.244.4 era 34,5. O analista suspeita de erro.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento para investigar a possível mudança de comportamento entre versões.


---

## Caso 278

**Contexto**

Ao trocar o plano de pagamento para 'CREDITO A VISTA', o aplicativo alega desconto máximo excedido, mesmo sem descontos nos produtos. O analista investiga a fonte do desconto indesejado.


**Solução / Diagnóstico**

O plano 185, para o qual o RCA estava tentando mudar, possui um desconto de 2% configurado (campo PERTXFIM). Como o desconto máximo permitido era 0, o sistema bloqueava a alteração. O erro não era nos produtos, mas no próprio plano de pagamento. O cliente deve ajustar o desconto máximo ou o percentual do plano.


---

## Caso 279

**Contexto**

Todos os produtos apresentam erro de tributação ao tentar fazer pedidos. O cliente precisa de prioridade, pois o vendedor está a 200km da sede.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento para análise prioritária.


---

## Caso 280

**Contexto**

A conta corrente do vendedor Arthur apresenta valores como se houvesse acréscimos aplicados ao Flex, mas o cliente afirma que não utiliza Flex. O analista verificou que só há um pedido no período.


**Solução / Diagnóstico**

O pedido em questão veio diretamente do ERP (ORIGEMPED = 'B') e não passou pela nuvem, mas a PKG da Máxima movimenta conta corrente para qualquer pedido que chegue via histórico. Para evitar isso, foi desativado o parâmetro USAR_PEDIDOS_ERP_CALCULO_CC, que agora impede a movimentação de conta corrente para pedidos originados diretamente no ERP.


---

## Caso 281

**Contexto**

O cliente quer que a meta diária seja apresentada no resumo de vendas, mas atualmente só aparece a meta mensal de 35000.


**Solução / Diagnóstico**

O sistema estava priorizando a tabela ERP_MXSMETA em vez da ERP_MXSMETARCA. Para que a meta diária (da ERP_MXSMETARCA) seja exibida, é necessário ativar o parâmetro FORCAR_MIX_PCMETARCA = 'S' na PCMXSCONFIGURACOES.


---

## Caso 282

**Contexto**

Os registros na MXSPRODUTPOS estão sendo gerados com CODOPERACAO = 2 (deletados), mesmo para registros recentes. O cliente quer entender por que o histórico de compra do produto não é mantido.


**Solução / Diagnóstico**

A JOB_PRODUTO_POSITIVACAO gera registros com CODOPERACAO = 2 quando o cliente envia informações de delete nas notas fiscais ou pedidos (MXSHISTORICOPEDI ou ERP_MXSNFSAID). Se o cliente está vendo deleções, é porque o ERP está enviando essas operações de exclusão.


---

## Caso 283

**Contexto**

O relatório 8018 no maxGestão não lista as filiais no filtro, embora a listagem funcione no Winthor. O analista suspeita de erro.


**Solução / Diagnóstico**

Ticket encaminhado para o desenvolvimento do maxGestão para correção.


---

## Caso 284

**Contexto**

O campo PrecoOriginal no JSON está sendo enviado com o valor total da embalagem (PTABELA * fator), em vez do preço de tabela unitário. O analista testou com diferentes configurações e o problema persiste.


**Solução / Diagnóstico**

Foi confirmado que o sistema está calculando o PrecoOriginal como (PrecoOriginal * fator da embalagem). O ticket foi encaminhado para o desenvolvimento para avaliar se há um parâmetro que possa alterar esse comportamento ou se é necessário ajuste.


---

## Caso 285

**Contexto**

Pedidos do tipo balcão reserva não são enviados para a MXSHISTORICOPEDC, mesmo com o parâmetro ENVIA_PEDIDOS_BALCAO_RESERVA ativo. O analista precisa de carga.


**Solução / Diagnóstico**

Foi ativado o parâmetro ENVIA_PEDIDOS_BALCAO_RESERVA e realizada a carga dos pedidos referentes ao mês atual. O RCA deve sincronizar para que os pedidos apareçam no histórico.


---

## Caso 286

**Contexto**

Uma vendedora (RCA 5) só vê os títulos dela, mas precisa ver os títulos de outros RCAs (81 e 85) que compartilham a mesma base de clientes. Os parâmetros FILTRAR_DADOS_TITULOS_RCA e FILTRAR_TITULOS_RCA já foram ativados, mas o problema persiste. O analista acredita que seja necessário uma carga de dados.


**Solução / Diagnóstico**

A análise mostrou que os clientes citados (1744, 458, 15715) não estavam na carteira da RCA usada como exemplo (norteali.renata). Na nuvem, apenas o cliente 1744 existe e está vinculado ao RCA 279. A configuração para permitir que um RCA veja títulos de outros já está correta. Se o cliente quiser que a RCA veja os títulos dos outros, é necessário que os clientes estejam na carteira dela ou que ela tenha a permissão adequada. O exemplo fornecido não representa o problema relatado, portanto é necessário que o cliente forneça um exemplo válido para análise.


---

## Caso 287

**Contexto**

A posição (status) dos pedidos não atualiza na timeline de múltiplos RCAs, mesmo com a sincronização automática.


**Solução / Diagnóstico**

Foi realizada uma carga de dados retroativos para atualizar a timeline dos pedidos. Essa solução paliativa foi aplicada porque já existe uma correção definitiva na versão 4 do sistema. Os RCAs que utilizam a sincronização automática devem atualizar para a versão de ponta da V4 para que os status passem a ser atualizados automaticamente.


---

## Caso 288

**Contexto**

Há uma divergência de comportamento entre a base do zero e a base de um RCA: produtos não aparecem para o vendedor mesmo após sincronizar. O problema ocorre com vários vendedores do cliente.


**Solução / Diagnóstico**

Foi realizada uma carga de dados para as filiais 235, 251, 261, 271, que estavam com problemas na base do RCA. Essa ação imediata resolveu o problema de exibição de produtos. A causa raiz ainda será investigada pelo desenvolvimento, pois suspeita-se que o cliente esteja alterando as filiais dos RCAs com frequência, o que pode causar erros de sincronização.


---

## Caso 289

**Contexto**

Ao tentar iniciar um pedido para o cliente 5107, o sistema retorna uma mensagem informando que nenhum plano de pagamento pode ser carregado. O analista verificou que o cliente possui a cobrança DEP e plano 18, e mesmo alterando via inspect, o problema persiste. Outro cliente com a mesma configuração funciona normalmente.


**Solução / Diagnóstico**

O problema ocorre por dois motivos: 1) O cliente 5107 não possui uma filial vinculada ao seu cadastro na MXSCLIENT (campo CODFILIALNF), ao contrário do cliente que funciona. 2) O RCA utilizado no teste não tem permissão de acesso à cobrança DEP na MXSACESSODADOS. A solução é vincular uma filial ao cliente e/ou liberar a permissão de acesso à cobrança para o RCA, ou deletar o vínculo da cobrança DEP com o plano 18 na tabela MXSCOBPLPAG, já que a cobrança DEP não é do tipo boleto e o plano 18 é a prazo, gerando um conflito.


---

## Caso 290

**Contexto**

O produto 15294 apresenta uma previsão de recebimento no MaxPedido, mas o analista verificou que não há previsões cadastradas na tabela MXSESTPEND para este produto. O problema foi verificado em base do zero.


**Solução / Diagnóstico**

A previsão de recebimento é gerada por uma job que consulta as tabelas PCPEDIDO (compra) e PCMOVPREENT (entrada). As informações estavam presentes na nuvem, por isso o produto aparecia com previsão. Foi realizado um procedimento no banco nuvem para corrigir a informação do produto de exemplo. O RCA deve sincronizar para receber a atualização. Além disso, é importante manter o ambiente do cliente atualizado, pois versões desatualizadas podem impactar a job.


---

## Caso 291

**Contexto**

O relatório 8020 apresenta erro ao ser gerado no maxPedido, embora funcione no Winthor. A variável CODPROD no SQL do relatório já foi corrigida, mas o erro persiste. O cliente é T-Cloud, impossibilitando o acesso aos logs.


**Solução / Diagnóstico**

O analista foi orientado a encaminhar o ticket para o desenvolvimento (N3) conforme alinhado via Discord, pois não foi possível resolver no nível de suporte.


---

## Caso 292

**Contexto**

Ao pesquisar um produto pelos últimos 4 dígitos do código de barras (1059), o aplicativo retorna múltiplos produtos, e não apenas o produto correspondente (846182). O comportamento ocorre tanto na V3 quanto na V4.


**Solução / Diagnóstico**

O comportamento está de acordo com o esperado. A opção de pesquisa 'Pesq. qualquer parte do campo' realiza uma busca com o operador LIKE, retornando todos os registros que contenham a string pesquisada. No teste realizado, a busca por '1059' retornou apenas um produto, indicando que o funcionamento está correto. Se o cliente deseja uma busca exata, deve utilizar a opção de pesquisa por código de barras completo.


---

## Caso 293

**Contexto**

Durante a sincronização, uma mensagem de conclusão aparece no início, e ao clicar em OK, o sistema entra em loop, reiniciando a sincronização. A mensagem só some se o usuário clicar fora da caixa. O problema persiste mesmo na versão ponta.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento (N3) para investigação, pois se trata de um comportamento inadequado da interface de sincronização.


---

## Caso 294

**Contexto**

Acréscimos estão sendo enviados do ERP para a conta corrente do RCA sem que o vendedor tenha movimentado a conta (Flex). O analista forneceu exemplos de pedidos (518354, 518362).


**Solução / Diagnóstico**

Após análise, constatou-se que a Máxima não atende ao cenário onde o ERP recalcula acréscimos (como de boleto) após o faturamento. A movimentação da conta corrente é feita com base nos dados enviados no momento da transmissão do pedido (ERP_MXSLOGRCA). Se o ERP altera o preço depois, isso não é refletido no cálculo da Máxima, gerando a divergência. O caso foi escalado para o desenvolvimento para avaliação de uma possível melhoria.


---

## Caso 295

**Contexto**

Cliente solicita a limpeza dos objetos não utilizados do schema do Pedido de Vendas em seu banco local. Foi alinhado com o gatekeeper que o schema poderia ser dropado.


**Solução / Diagnóstico**

Foi realizado o drop dos schemas do Pedido de Vendas que não são mais utilizados pelo cliente. A ação foi concluída com sucesso.


---

## Caso 296

**Contexto**

Uma política de desconto automática (10959), vinculada à região 1, é aplicada corretamente quando a filial 1 é selecionada, mas deixa de ser aplicada ao alterar para a filial 12, embora ambas as filiais estejam vinculadas à mesma região 1 via MXSTABPRCLI. O parâmetro IGUALAR_FILIALNF_AO_ALTERAR_FILIAL está como 'S' e o fluxo funciona na 316.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento (N3) para investigar por que a política não está sendo aplicada na filial 12, já que as configurações parecem estar corretas.


---

## Caso 297

**Contexto**

O cliente utiliza uma view personalizada do WMS (SR_VALIDADE) que alimenta a tabela MXSVALIDADEWMS no MaxPedido. Em uma demanda anterior, foi necessário realizar carga manual. Agora, o problema de importação recorrente voltou a ocorrer: dados da view não estão sendo importados para a nuvem.


**Solução / Diagnóstico**

Foi refeita a customização da view personalizada e os dados foram importados com sucesso para a nuvem. O RCA deve sincronizar o aplicativo para receber as informações de validade.


---

## Caso 298

**Contexto**

Cadastros de clientes realizados pelo aplicativo não estão gravando campos de endereço (comercial e cobrança) na tabela PCCLIENTFV do Winthor, embora os dados constem no JSON da MXSINTEGRACAOCLIENTE.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento (N3) para investigar por que os campos de endereço não estão sendo persistidos no banco do Winthor.


---

## Caso 299

**Contexto**

Para o produto 4557, a tributação não é carregada quando a FILIALNF 2 é selecionada, embora exista vínculo na MXSTABPRCLI e tributação na MXSTABTRIB para ambas as filiais (1 e 2). Na filial 1 funciona. O banco nuvem está de acordo com o local e o fluxo funciona na 316.


**Solução / Diagnóstico**

O problema era que o RCA não possuía permissão de acesso ao estoque da filial 2. Após liberar a permissão na Central de Configurações, a tributação passou a funcionar normalmente para a filial 2.


---

## Caso 300

**Contexto**

Os dados de conta corrente não são exibidos na versão 4 do aplicativo, mesmo com os parâmetros DEFINE_CC_MENU e outros ativos.


**Solução / Diagnóstico**

O usuário em questão (Mariel) tinha a permissão 'Ocultar conta corrente' marcada em seu cadastro. Após desmarcar essa permissão e sincronizar, os dados da conta corrente passaram a ser exibidos normalmente na V4.


---

## Caso 301

**Contexto**

Vários produtos não aparecem na base do RCA (ex: 5320), mas aparecem na base do zero. O analista já realizou carga em diversas tabelas, mas o problema persiste.


**Solução / Diagnóstico**

Foi realizada uma normalização de dados para o RCA. O problema foi causado por um erro de sincronização devido ao uso de múltiplos aparelhos com o mesmo usuário. O backend já possui uma correção para tratar esses erros, mas, para o caso específico, a normalização manual foi necessária. Após a carga, o RCA deve sincronizar para receber os dados corretos.


---

## Caso 302

**Contexto**

O gráfico 'Clientes positivados' permanece zerado no aplicativo, mesmo com pedidos na base do RCA e registros nas tabelas de dias úteis (MXSDIASUTEIS, ERP_MXSDATAS).


**Solução / Diagnóstico**

Na versão 4 do MaxPedido, o gráfico de clientes positivados considera apenas pedidos FATURADOS (que possuem nota fiscal). Como os pedidos do RCA em questão não estão faturados, o gráfico permanece zerado. Esse é o comportamento esperado para a V4. Já o gráfico de vendas não mostra valores abaixo de 1% da meta, por isso também pode aparecer zerado.


---

## Caso 303

**Contexto**

Ao tentar duplicar um pedido faturado (posição F), o aplicativo retorna uma mensagem de erro informando que não foi possível iniciar o processo. Pedidos com outras posições são duplicados normalmente.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento (N3), pois o comportamento de não permitir a duplicação de pedidos faturados pode não ser o esperado.


---

## Caso 304

**Contexto**

Ao tentar visualizar o histórico de um pedido na base do RCA, o aplicativo solicita que seja feita uma sincronização, mesmo com o histórico presente na base. O pedido é do dia 30/01 e já foram feitas várias sincronizações.


**Solução / Diagnóstico**

Foi habilitado o parâmetro VALIDAR_HORARIO_IMPORTACAO_PEDIDO para tentar resolver o problema. O RCA deve sincronizar e validar. Se o problema persistir, o ticket deve ser encaminhado para o desenvolvimento com a informação de que o parâmetro já foi ativado.


---

## Caso 305

**Contexto**

Os gráficos de valores vendidos no mês não são gerados na versão 4 do MaxPedido, embora o resumo de vendas apresente os valores corretamente.


**Solução / Diagnóstico**

O problema era a falta de dias úteis cadastrados na central de configurações para o mês atual. Após o cadastro dos dias úteis, os gráficos passaram a ser gerados normalmente.


---

## Caso 306

**Contexto**

Uma política de preço fixo (252487) não está sendo aplicada no MaxPedido para o item 2237, nas condições especificadas (cliente 8161, cobrança 001, plano 26). O fluxo funciona na rotina 316 do Winthor.


**Solução / Diagnóstico**

O problema era um acréscimo configurado no imposto para pessoa física (campo PERACRESCISMOPF da MXSTRIBUT). Esse acréscimo estava alterando o valor final, fazendo com que o preço fixo não fosse aplicado como esperado. O cliente deve verificar essa configuração no banco local.


---

## Caso 307

**Contexto**

Os itens do carregamento de pronta entrega 152743 não aparecem para o RCA. Embora haja registros na ERP_MXSMOV e PCMOV, a tabela ERP_MXSCARREG não possui registros para esse carregamento, o que pode ser a causa da divergência.


**Solução / Diagnóstico**

Foi realizada uma carga manual de vários registros da tabela PCCARREG para o banco nuvem, incluindo o carregamento 152743. O RCA deve sincronizar o aplicativo para que os itens sejam exibidos. O problema pode ter ocorrido por alguma falha na trigger que impede a descida automática dos dados.


---

## Caso 308

**Contexto**

Ao tentar inserir o item 3614 em um pedido, ocorre um erro. O problema acontece com todos os usuários. Na rotina 316 do Winthor, a inserção funciona normalmente.


**Solução / Diagnóstico**

O problema ocorria na versão 3.230.0 que o cliente estava utilizando. Testes na versão 4.000.8 mostraram que o item é inserido com sucesso, indicando que houve uma correção em versões posteriores. Recomenda-se que o cliente atualize para a versão 4 ou, se preferir manter-se na V3, para a última versão disponível (3.269.2).


---

## Caso 309

**Contexto**

O aplicativo está apresentando consumo de bateria excessivo (82,1%) em segundo plano, mesmo sem uso ativo. Os parâmetros de tracking estão configurados dentro da normalidade.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento (N3) para investigar possíveis causas para o alto consumo de bateria, que foge do esperado para as configurações de tracking utilizadas.


---

## Caso 310

**Contexto**

Após a troca do IP na stack do extrator (de 192.168.0.9:8180 para 192.168.9.25:8180), a API de cancelamento de pedidos continua não funcionando, retornando crítica de 'API CANCELADA INVALIDA'. O acesso ao WTA pelo IP local funciona.


**Solução / Diagnóstico**

O problema era a falta de uma barra ('/') no final da URL na variável de ambiente da stack do extrator. A correção foi aplicar a URL correta: 'http://192.168.0.25:8180/'. Após o ajuste e novo deploy da stack, a API de cancelamento passou a funcionar.


---

## Caso 311

**Contexto**

O vendedor (mix.302) recebe um alerta de roteiro pendente do dia anterior ao tentar iniciar um pedido, mesmo tendo justificado/atendido todos os clientes do roteiro anterior. O problema foi testado na versão 4.000.8.


**Solução / Diagnóstico**

O bloqueio por roteiro pendente é controlado pelo parâmetro BLOQ_RCA_COM_ROTA_PENDENTE e pela quantidade de dias definida em DIAS_VERIFICACAO_ROTEIRO_PENDENTE. Se o alerta ainda aparece mesmo após justificar, é porque o script de verificação ainda encontra compromissos pendentes. Isso pode ocorrer se a justificativa não foi corretamente registrada ou sincronizada. Como a base do RCA não foi anexada, não foi possível aprofundar a análise, mas a orientação é sobre o funcionamento do parâmetro.


---

## Caso 312

**Contexto**

O cliente relata que processos da Máxima estariam causando locks no banco local e travando o Winthor. O analista verificou que os processos da Máxima estão funcionando, mas ficam presos na fila devido a locks causados por outras aplicações.


**Solução / Diagnóstico**

O problema não é causado pela Máxima, mas o desenvolvimento identificou a necessidade de melhorar o script que apura os limites de crédito dos clientes para evitar que ele seja impactado por locks de terceiros. O ticket foi encaminhado para N3 para essa melhoria.


---

## Caso 313

**Contexto**

Uma política de preço fixo (252487) não está sendo aplicada no MaxPedido (mesmo contexto do GATE-757). O analista reabriu o ticket para o mesmo problema.


**Solução / Diagnóstico**

O ticket foi encaminhado para o desenvolvimento (N3), pois a análise anterior indicou que a causa (acréscimo no imposto) foi resolvida, mas o problema persistiu.


---

## Caso 314

**Contexto**

As solicitações de limite de crédito do RCA 2 não estão chegando no maxGestão para aprovação. As solicitações ficam presas na APK. O RCA 2 é supervisor.


**Solução / Diagnóstico**

Foi realizado um rebuild da sequence da tabela MXSINTEGRACAOLIMCREDCLI para evitar que o problema volte a acontecer. Além disso, observou-se que o cadastro do supervisor 2 não possui os vínculos corretos, o que pode impactar o fluxo. Recomenda-se que o cliente preencha o usuário RCA no cadastro do supervisor.


---

## Caso 315

**Contexto**

Ao importar uma planilha para editar o mix ideal na central de configurações, o sistema retorna erro informando que alguns itens não foram importados. No entanto, é possível adicionar esses mesmos itens manualmente.


**Solução / Diagnóstico**

A importação falha porque a planilha contém códigos auxiliares de embalagem que não existem na base de dados da filial selecionada. A inserção manual funciona porque, ao selecionar o produto, o sistema carrega as embalagens corretas e ativas daquela filial. A solução é garantir que os códigos auxiliares na planilha correspondam exatamente aos cadastrados na filial.


---

## Caso 316

**Contexto**

Há uma divergência de preço para o produto 21697 na região 3: o preço no banco local (PCTABPR) é R$ 11,39, enquanto no banco nuvem (MXSTABPR) é R$ 10,99. Atualizações de ambiente e reinicialização do extrator não resolveram.


**Solução / Diagnóstico**

Foi realizada uma normalização dos dados, atualizando a MXSTABPR com o valor correto do banco local.


---

## Caso 317

**Contexto**

Roteiro pendente do dia anterior (19/02) está sendo exibido incorretamente para o RCA mix.120, com mais de 100 compromissos, embora ele tivesse apenas 10 clientes roteirizados naquele dia. O problema afeta o fluxo de justificativa de roteiro, impedindo novas vendas.


**Solução / Diagnóstico**

Foi identificado que a tabela MXSHISTORICOCOMPROMISSOS continha registros incorretos e duplicados devido a problemas em versões antigas do banco de dados. Foi realizada uma normalização de todos os registros de histórico de compromissos desde 03/01/2025 até a data atual. Os RCAs devem sincronizar para receber os compromissos corretos. O problema deve ser monitorado, mas a expectativa é que não ocorra novamente devido às correções no backend.


---

## Caso 318

**Contexto**

Há divergência de registros de títulos entre a tabela PCPREST (banco local) e a ERP_MXSPREST (banco nuvem), causando a exibição de títulos inadequados no aplicativo.


**Solução / Diagnóstico**

Foi realizada a normalização dos dados, igualando o banco nuvem ao banco local. O RCA deve sincronizar para que os títulos sejam atualizados no aplicativo.


---

## Caso 319

**Contexto**

O cliente utiliza uma view personalizada do WMS e há divergência nas validades dos produtos entre o banco local e o banco nuvem (MXSVALIDADEWMS). É necessária uma carga para normalizar.


**Solução / Diagnóstico**

O fluxo foi revisado e recriado, e os dados do produto de exemplo (127772) foram validados como corretos. A explicação sobre o funcionamento do fluxo (TABELA_WMS -> VIEW_CUSTOMIZADA -> PCMXSVALIDADEWMS -> JOB -> MXSVALIDADEWMS) foi fornecida. Qualquer alteração nas quantidades dispara a trigger e atualiza a nuvem automaticamente.


---

## Caso 320

**Contexto**

Há divergência de registros de políticas de preço fixo entre a PCPRECOPROM (banco local) e a MXSPRECOPROM (banco nuvem). Isso impede que a política seja aplicada no pedido.


**Solução / Diagnóstico**

Foi identificado um erro na trigger TRG_MXS_PCPRECOPROM em 19/02/2025, que impedia a subida dos registros. Foi realizada uma carga para normalizar os dados, e a trigger foi verificada e está funcionando normalmente. Recomenda-se atualizar o ambiente do cliente para a versão mais recente do banco.


---

## Caso 321

**Contexto**

Pedidos estão aparecendo duplicados na timeline, um com status 'Liberado' e outro com 'Faturado', embora no banco exista apenas um pedido.


**Solução / Diagnóstico**

Foi identificado um erro em uma versão do atualizador que transformou a coluna numtransvenda em chave primária no SQLite, causando duplicidade. Foi enviado um comando para dropar e recriar a tabela MXSHISTORICOPEDC na base do RCA com os atributos corretos. O RCA deve sincronizar para resolver.


---

## Caso 322

**Contexto**

Vendedores estão conseguindo bater o ponto fora do horário de tolerância configurado na central. O problema ocorre com o horário de saída da jornada, que deveria ser validado.


**Solução / Diagnóstico**

Atualmente, a funcionalidade de jornada de trabalho no MaxPedido só valida a tolerância no horário de saída da última jornada do dia. Os demais horários (entrada, saída para almoço, etc.) não possuem validação de tolerância. Para que essa validação seja aplicada a todos os horários, é necessário abrir uma solicitação de melhoria.


---

## Caso 323

**Contexto**

O valor exibido na tela inicial (venda transmitida) está divergente do valor apresentado no resumo de vendas e na rotina 1464 do Winthor. O analista testou o parâmetro CRITERIO_VENDA_CARD_PEDIDO sem sucesso.


**Solução / Diagnóstico**

A diferença ocorre porque a tela inicial do MaxPedido está configurada para exibir a 'venda transmitida', enquanto a rotina 1464 do Winthor exibe a 'venda faturada'. Valores transmitidos e faturados nem sempre são iguais, pois nem tudo que é transmitido é faturado imediatamente. Para uma análise mais precisa, recomenda-se comparar dia a dia. O comportamento está de acordo com as configurações do cliente.


---

## Caso 324

**Contexto**

Mesmo com os parâmetros HABILITA_PED_CLI_NAO_SINC e HABILITA_PED_CLI_RECEM_CADASTRADO ativos e o campo CODFUNCULTALTER preenchido, os cadastros temporários de clientes não são removidos do aplicativo após a integração, resultando em clientes duplicados.


**Solução / Diagnóstico**

Foi aplicada uma solução paliativa para o RCA específico (codusuario 106237), enviando um comando para deletar os clientes temporários de sua base. O problema foi encaminhado para N3 para investigação da causa raiz, pois o comportamento esperado é que esses clientes sumam automaticamente.


---

## Caso 325

**Contexto**

Ao tentar liberar uma versão do MaxPedido para um RCA pela rotina 304 da central de configurações, o sistema retorna o erro 'Não foi possível Salvar! O usuário de código: 54361 possui duas versões do Gestão Mobile!', mesmo o RCA não tendo versão liberada. A liberação pela rotina 402 funciona, mas o erro persiste na 304.


**Solução / Diagnóstico**

Em uma simulação realizada, o erro não foi reproduzido. Se o problema persistir, o analista deve abrir um novo ticket com um vídeo demonstrando o passo a passo para que o desenvolvimento possa debugar.


---

## Caso 326

**Contexto**

Duplicidade de pedidos na timeline (mesmo contexto dos GATE-820 e 838). O cliente necessita da carga com o script corretivo.


**Solução / Diagnóstico**

Foi enviado o comando para dropar e recriar a tabela MXSHISTORICOPEDC na base do RCA. O RCA deve sincronizar para que a duplicidade seja resolvida.


---

## Caso 327

**Contexto**

Um supervisor não consegue voltar para sua própria base no maxPedido após trocar para a base de um RCA. O analista identificou que o código ERP do supervisor (346) não retorna no aplicativo, embora apareça na Central de Configurações.


**Solução / Diagnóstico**

A análise mostrou que, para usar a funcionalidade de troca de base, é necessário marcar a flag 'é vendedor' no cadastro do supervisor na central de configurações. Assim, o nome do supervisor aparecerá na lista para que ele possa retornar à sua própria base.


---

## Caso 328

**Contexto**

O cliente questiona por que na rotina 3330 a filial retira do cabeçalho é 2, enquanto a filial retira do produto é 5. O analista verificou que a tabela PCPEDCFV alimenta esse campo e quer saber se é esperado que os valores sejam iguais.


**Solução / Diagnóstico**

O comportamento está de acordo com o esperado. O pedido foi feito com filial de venda 2 e retirada da filial 5 (configurada no fluxo de filial retira). O campo filial retira do cabeçalho mostra a filial de venda, enquanto a do produto mostra a filial de retirada, que pode ser diferente conforme a regra de negócio do cliente.


---

## Caso 329

**Contexto**

Um pedido de balcão reserva não gerava nota e boleto. O analista verificou que não havia dados na MXSHISTORICOPEDC e, mesmo após carga interna, o problema persistia.


**Solução / Diagnóstico**

O pedido era do tipo balcão reserva e estava configurado para não passar histórico. O parâmetro que controla isso foi alterado para 'S' (permitir histórico de pedidos balcão reserva). Após essa alteração, o RCA deve sincronizar para que o histórico seja carregado.


---

## Caso 330

**Contexto**

Clientes de um RCA não aparecem no maxPedido, mesmo após transferência de carteira na rotina 328 e carga interna. O analista verificou que a tabela PCCLIENT tem registros, mas eles não sobem para a nuvem.


**Solução / Diagnóstico**

A coluna DTEXCLUSAO da tabela PCCLIENT deve estar nula para que os clientes sejam enviados para a nuvem. Foi constatado que alguns clientes tinham essa coluna preenchida. Após ajuste (colocando null) e carga, os clientes passaram a aparecer. O cliente deve ser orientado a verificar se alguma rotina está preenchendo essa coluna e, se necessário, mantê-la nula.


---

## Caso 331

**Contexto**

O cliente tem regiões vinculadas ao cliente pela MXSCLIENTREGIAO, mas ao inserir novas regiões, as anteriores são removidas. Além disso, algumas regiões aparecem mesmo sem vínculo. O analista quer entender o comportamento.


**Solução / Diagnóstico**

O parâmetro VALIDA_FILIAL_MXSCLIENTREGIAO estava habilitado, fazendo com que o maxPedido priorize regiões cadastradas na MXSFILIALREGIAO. As regiões 70000 e 70004 aparecem porque não estão na MXSFILIALREGIAO, e com o parâmetro desabilitado todas as regiões são consideradas. A solução depende da necessidade do cliente: manter o parâmetro habilitado e cadastrar as regiões desejadas na MXSFILIALREGIAO, ou desabilitá-lo para que todas as regiões sejam exibidas.


---

## Caso 332

**Contexto**

Um pedido com erro de envio ficou na posição 'pendente do ERP' na timeline, embora não tenha sido enviado. O analista quer saber por que isso ocorre e como ajustar a base do vendedor.


**Solução / Diagnóstico**

O pedido 1419017549 foi editado, gerando um novo número (1419017653), e sofreu crítica da integradora, o que impediu a atualização do status. Na base do RCA, o pedido original não gerou numpederp e ficou com status 0. A orientação é que, se o RCA excluir o pedido, não haverá impacto, pois a informação de pendente é falsa. Caso o cliente não aceite, pode ser encaminhado para desenvolvimento, mas a chance de correção é a mesma do gatekeeper, pois geraria informação falsa no app.


---

## Caso 333

**Contexto**

O cliente deseja que não seja possível vincular uma bonificação a um pedido de filial diferente. Ativou o parâmetro FILTRAR_FILIAL_BONIFICACAO, mas ele não funciona.


**Solução / Diagnóstico**

O parâmetro FILTRAR_FILIAL_BONIFICACAO não existe no código do maxPedido. Trata-se de uma melhoria já registrada (MXPEDDV-94741). Portanto, o parâmetro não tem efeito, e a funcionalidade desejada não está disponível.


---

## Caso 334

**Contexto**

Para o cliente 14951, a política de desconto 657146 (13%) não é aplicada, apenas a 645376 (9,68%). Para o cliente 3397, ambas são aplicadas. O analista quer entender o motivo.


**Solução / Diagnóstico**

A política 657146 possui a coluna CODGRUPOREST = 21, que valida as tabelas mxsgruposcampanhai e mxsgruposcampanhac. O cliente 14951 não está vinculado a esse grupo na mxsgruposcampanhai, por isso a política não é válida para ele. Após inserir o cliente nessa tabela, a política passou a ser aplicada. O cliente deve verificar no ERP o cadastro do vínculo do cliente ao grupo.


---

## Caso 335

**Contexto**

Um RCA não consegue iniciar pedido devido à mensagem de inconsistência de dados por falta de permissão a plano de pagamento/cobrança, embora todas as permissões estejam dadas.


**Solução / Diagnóstico**

O cliente utiliza o fluxo da MXSPLPAGFILIAL e só há informações para a filial 3, enquanto o RCA está configurado nas filiais 1 e 3. A solução é remover a permissão da filial 1 ou enviar as informações da filial 1 para a MXSPLPAGFILIAL, igual à filial 3.


---

## Caso 336

**Contexto**

Um RCA não vê algumas faixas de comissão na negociação, embora elas existam na mxscomissaousur. O analista questiona a regra de exibição.


**Solução / Diagnóstico**

O que impacta a exibição é o percentual máximo de desconto do produto (PERDESCMAX na MXSTABPR). O maxPedido apresenta apenas as comissões que estão dentro do limite máximo de desconto. No caso, o produto tem PERDESCMAX = 4%, então só aparecem faixas até 4%. Para não exibir a faixa de 3%, o cliente precisaria alterar o percentual de desconto final da comissão ou o percentual máximo de desconto do produto.


---

## Caso 337

**Contexto**

Os itens de um pedido cancelado não aparecem no histórico de pedidos, embora haja registros na MXSHISTORICOPEDI e os produtos tenham o mesmo CODAUXILIAR na MXSPRODUT.


**Solução / Diagnóstico**

A MXSHISTORICOPEDC (capa) está com posição 'C' (cancelado), enquanto a MXSHISTORICOPEDI (itens) está com posição 'P' (pendente). Para que os itens apareçam, a posição nos itens deve ser igual à da capa. Como o cliente é OERPS, ele deve enviar corretamente a posição 'C' na MXSHISTORICOPEDI para os itens cancelados.


---

## Caso 338

**Contexto**

O cliente quer que ao entrar no aplicativo seja exigida a jornada de trabalho, mas atualmente só bloqueia ao iniciar um pedido. O analista verificou que as permissões de bloquear pedido fora da rota e solicitar autorização estão marcadas, mas o sistema entra em visita avulsa.


**Solução / Diagnóstico**

O fluxo atual funciona assim: se o cliente usa roteiro e o RCA não tem rota no dia, ao tentar fazer um pedido é considerada venda avulsa, e o cliente é incluído no roteiro. Mesmo com autorização, o processo é de venda avulsa. Essa alteração foi feita no ano passado e é o comportamento esperado. Caso o cliente não concorde, deve solicitar melhoria.


---

## Caso 339

**Contexto**

O limite de crédito disponível no maxPedido (R$ 961,03) diverge da rotina 1203 do Winthor (R$ 175,68). O analista identificou que o cliente tem títulos com cobrança CAR e quer entender a causa.


**Solução / Diagnóstico**

A divergência ocorre porque os títulos com cobrança CAR não são somados na tabela MXSCLIENTECREDDISP devido ao parâmetro CON_VERIFICALIMCREDCODCOBD da rotina 132 estar configurado como 'N'. Com isso, o backend filtra PCPREST.CODCOB NOT IN ('D', 'DH', 'CAR'). Portanto, esses títulos não são considerados no limite. A solução é alterar a configuração na rotina 132 ou orientar que esse tipo de cobrança não será somado.


---

## Caso 340

**Contexto**

Na versão 4.011.3, a lucratividade não aparece na aba de itens, enquanto na versão 3.270.4 aparecia. O analista quer saber o motivo.


**Solução / Diagnóstico**

Na versão 4, é necessário cadastrar a informação na central de configurações para exibir a lucratividade. Após realizar o cadastro, a informação passou a ser exibida normalmente.


---

## Caso 341

**Contexto**

O ícone de promoção continua aparecendo para um produto mesmo após o fim da promoção. O analista tentou carga em várias tabelas sem sucesso.


**Solução / Diagnóstico**

A base do RCA tinha registros na MXSPRODUTMSK que não existiam mais no banco nuvem. Foi executado um comando para dropar as tabelas na base dos RCAs e recriá-las, forçando a sincronização dos novos dados. Após sincronizar, a legenda de promoção deixou de aparecer.


---

## Caso 342

**Contexto**

O parâmetro DEFINE_FILIAL_RETIRA_PADRAO está configurado como 5, mas o pedido sempre inicia na filial 2. O cliente quer que a filial retira padrão seja 5.


**Solução / Diagnóstico**

O parâmetro DEFINE_FILIAL_RETIRA_PADRAO define a filial retira padrão. Foi verificado que, ao baixar a base do zero, a filial 5 aparece normalmente. Portanto, o problema pode estar na base do RCA. Após validação, a filial 5 passou a ser exibida.


---

## Caso 343

**Contexto**

O resumo de vendas apresenta valores divergentes: venda transmitida R$ 240.194,22, venda faturada R$ 241.379,90 e valor vendido no mês R$ 257.727,58. O analista quer entender a causa.


**Solução / Diagnóstico**

A divergência ocorre devido a um conflito entre as tabelas MXSHISTORICOPEDC e MXSHISTORICOPEDI na coluna POSICAO. Enquanto a capa está faturada, alguns itens ainda estão como pendentes. Isso gera diferença nos valores. O cliente, por ser OERPS, deve enviar as informações corretamente, com a posição dos itens igual à da capa.


---

## Caso 344

**Contexto**

O cliente quer saber se é possível mencionar um cliente normal em um orçamento feito para o consumidor final. O analista não encontrou campo para isso.


**Solução / Diagnóstico**

Para preencher informações do consumidor final, o parâmetro VALIDA_CPF_CNPJ_CONS_FINAL deve estar como 'S'. Isso abre uma janela para preencher os dados, mas funciona apenas em pedido normal, não em orçamento. Em orçamento, essa funcionalidade não está disponível; seria uma melhoria.


---

## Caso 345

**Contexto**

Um RCA não consegue consultar produtos na filial 2 porque nenhum item é retornado. O analista verificou que não há produtos vinculados à filial 2 no banco nuvem, mas o cliente informou que estão cadastrados no ERP.


**Solução / Diagnóstico**

Faltava configurar a filial no parâmetro CODFILIAL_IMPORTACAO da tabela pcmxsconfiguracoes no banco local. Após configurar e fazer a carga, os produtos da filial 2 passaram a subir para a nuvem e aparecer no maxPedido.


---

## Caso 346

**Contexto**

Ao tentar cancelar um pedido, o sistema apresenta erro informando falha na API do Winthor. O analista verificou que a senha do usuário PCADMIN está correta.


**Solução / Diagnóstico**

O problema é recorrente e já foi tratado em outro ticket (GATE-705). Provavelmente é uma questão de configuração, já que em outros clientes funciona. O analista deve verificar as configurações da API no cliente e, se necessário, encaminhar para desenvolvimento com mais detalhes.


---

## Caso 347

**Contexto**

Ao selecionar uma filial de retirada com estoque, o sistema impede a inclusão do item, informando falta de estoque. O analista testou com parâmetro TOTALIZA_ESTOQUE_LISTAGEM_PRODUTO desabilitado, mas o problema persiste.


**Solução / Diagnóstico**

Para que o sistema valide o estoque da filial retira, é necessário ativar o parâmetro UTILIZAFILIALRETIRAFILIALESTOQUE como 'S'. Após essa configuração, o estoque da filial retira passou a ser considerado corretamente.


---

## Caso 348

**Contexto**

O cliente habilitou o parâmetro HABILITA_MAPA_OPORTUNIDADE, mas a aba para preenchimento de CNAEs não aparece no perfil do vendedor na central de configurações.


**Solução / Diagnóstico**

Ao acessar o perfil em configurações, a aba de mapa de oportunidades estava sendo exibida normalmente. Portanto, o problema já foi resolvido ou era um erro momentâneo. O cliente deve verificar novamente.


---

## Caso 349

**Contexto**

Um pedido não foi enviado para o maxPag, ficando apenas no ERP. O analista quer saber por que alguns pedidos vão para o maxPag e outros não, mesmo com o mesmo plano de pagamento e cobrança.


**Solução / Diagnóstico**

Após testes, foi constatado que o processo do maxPag não está sendo acionado corretamente. Como não foi possível identificar a causa rapidamente, o ticket deve ser encaminhado para desenvolvimento para análise mais aprofundada, com os exemplos de pedidos que apresentaram o problema.


---

## Caso 350

**Contexto**

O cliente tem dúvidas sobre o funcionamento da conta corrente: se é estornada ao cancelar um pedido e se ocorre devolução parcial em caso de estorno de itens.


**Solução / Diagnóstico**

Sim, a conta corrente é estornada quando um pedido é cancelado (posição 'C' na MXSHISTORICOPEDC). Em caso de estorno parcial (apenas alguns itens), a MXSHISTORICOPEDC fica com posição 'F' e os itens estornados ficam com posição 'C'. O saldo só é devolvido se houve movimentação na conta corrente referente àqueles produtos. Deve-se verificar na tabela erp_mxslog se há registros de retorno de saldo.


---

## Caso 351

**Contexto**

O cliente não consegue visualizar o produto 30341 e suas embalagens. O analista rodou scripts e não encontrou pendências.


**Solução / Diagnóstico**

O produto não aparece porque não há estoque para a filial 4. Como não há estoque, ele não é exibido na listagem de produtos.


---

## Caso 352

**Contexto**

Pedidos realizados com pagamento TINO não são enviados ao ERP, ficando com a crítica 'Link maxPayment gerado com sucesso'.


**Solução / Diagnóstico**

Não há erro. O link gerado ainda não foi pago. O pedido só desce para o ERP quando a mensageria da API do cartão notificar a reversa do limite. O fluxo correto é: o link precisa ser pago, a API da TINO notifica o MaxSoluções, que então envia o pedido para o ERP.


---

## Caso 353

**Contexto**

Ao iniciar qualquer pedido, o sistema apresenta mensagem de inconsistência por falta de permissão a plano de pagamento/cobrança, mesmo com todas as permissões concedidas.


**Solução / Diagnóstico**

O cliente usa o fluxo da MXSPLPAGFILIAL e só há informações para a filial 3, mas o RCA está configurado nas filiais 1 e 3. A solução é remover a permissão da filial 1 ou enviar as informações da filial 1 para a MXSPLPAGFILIAL, igual à filial 3.


---

## Caso 354

**Contexto**

Ao alterar o tipo de venda para bonificação, o sistema mostra mensagem de que nenhuma cobrança pode ser carregada, embora as cobranças e planos estejam vinculados.


**Solução / Diagnóstico**

A configuração estava errada: o parâmetro VALIDAR_TIPOVENDA_BONIFICACAO estava como 'S' e a cobrança usada era numérica, quando deveria ser BNF, BNFT etc. Além disso, não havia vínculo na MXSCOBPLPAG para bonificação. O cliente deve enviar as informações corretamente, com códigos de cobrança adequados (BNF, BNFT) e vincular os planos.


---

## Caso 355

**Contexto**

O produto 14929 não exibe a opção de solicitação de preço quando se aplica um desconto, embora em outros produtos funcione. O analista testou e o sistema informa que o preço está abaixo do mínimo permitido na rotina 201.


**Solução / Diagnóstico**

O preço mínimo na tabela MXSTABPR está configurado como 0% (PERDESCMAX), o que faz com que qualquer desconto ultrapasse o limite. No entanto, a autorização de preço deveria ser solicitada até o preço mínimo de venda (PRECOMINIMOVENDA = 2,86). Ao testar com um cliente sem restrições, a autorização foi solicitada. Fatores como títulos em aberto podem impedir a autorização. O cliente deve verificar a origem de preço na 316 e garantir que não haja impedimentos.


---

## Caso 356

**Contexto**

O produto 3777, com estoque de 405 unidades, apresentou erro de falta de estoque ao ser inserido em pedido. O analista não conseguiu simular o erro.


**Solução / Diagnóstico**

A crítica veio da integradora, não do maxPedido. No aplicativo, o estoque é exibido corretamente. O cliente deve verificar com a TOTVS por que a integradora está barrando o produto mesmo com estoque disponível.


---

## Caso 357

**Contexto**

O cliente quer que a quantidade mínima do produto 5718 seja 0,8, mas o maxPedido fixa em 1,0 mesmo após alterar QTUNIT na MXSEMBALAGEM e MXSPRODUT.


**Solução / Diagnóstico**

Por padrão, a quantidade mínima sempre é 1. Para trabalhar com frações, o usuário deve fazer o fracionamento manualmente. O sistema não altera automaticamente a quantidade mínima para valores fracionados.


---

## Caso 358

**Contexto**

O cliente não consegue fazer uma venda normal e adicionar um item bonificado. Mesmo ativando os parâmetros PERMITE_CANCELAR_PED_BRINDE e EXIBIR_BNF_NA_VENDA, o campo para item bonificado não aparece.


**Solução / Diagnóstico**

Os parâmetros estavam configurados nas tabelas erradas. O parâmetro PERMITEITEMBNFTV1 é da MXSPARAMFILIAL, enquanto PERMITE_ITEM_BNFTV1 é da MXSPARAMETRO. Após cadastrar os parâmetros nas tabelas corretas, a funcionalidade passou a funcionar.


---

## Caso 359

**Contexto**

Produto sendo integrado com valor divergente: na nuvem consta R$ 8,99, mas no ERP chega R$ 71,92. O analista quer saber o que ocorreu.


**Solução / Diagnóstico**

O JSON do pedido na MXSINTEGRACAOPEDIDO mostra o valor correto de 8,99 multiplicado pela quantidade (72), totalizando 647,28. O campo precoOriginal está 8,99. Portanto, o aplicativo gerou o valor correto. A divergência ocorre na integração do ERP, que ao pegar o JSON pode ter interpretado errado. O cliente deve verificar com o suporte do ERP.


---

## Caso 360

**Contexto**

O cliente deseja a criação da view de lotes de validade da WMS. O analista pediu ajuda.


**Solução / Diagnóstico**

Foi criada a view do wms que faz a integração com wms terceiro com a nuvem da Máxima.


---

## Caso 361

**Contexto**

Um RCA tem roteiro de visitas sem justificar, mas não consegue justificar o cliente. O analista não entende o fluxo.


**Solução / Diagnóstico**

A mensagem de cliente não justificado no roteiro anterior ocorre quando o RCA deixou de justificar alguma visita planejada nos dias configurados no parâmetro DIAS_VERIFICACAO_ROTEIRO_PENDENTE. Para justificar, é necessário acessar o cliente no roteiro e realizar a justificativa. O fluxo está detalhado em tickets como GATE-251, GATE-1364 e GATE-1460.


---

## Caso 362

**Contexto**

Um pedido foi autorizado no maxGestão, mas o RCA recebeu retorno de que o produto foi cortado por preço mínimo. O analista verificou que o preço mínimo na MXSTABPR é nulo e que no JSON a solicitação de autorização está como false.


**Solução / Diagnóstico**

No primeiro pedido, a autorização foi concedida para todos os produtos. No segundo, o produto específico não foi autorizado no maxGestão devido à lucratividade abaixo do esperado, e por isso não gerou registro na PCAUTORI, resultando no corte. O comportamento do sistema está correto.


---

## Caso 363

**Contexto**

Os itens do pedido 74793 não aparecem no histórico, embora constem na pcpedi. O analista verificou que na MXSHISTORICOPEDI os itens estão com posição cancelado, mas no banco local estão faturados.


**Solução / Diagnóstico**

Há divergência entre o banco local e a nuvem. A capa do pedido está faturada, mas os itens estão cancelados na nuvem. Para resolver, o cliente deve atualizar o ambiente e fazer uma carga de pedidos para sincronizar os dados corretamente. Após isso, os itens devem aparecer.


---

## Caso 364

**Contexto**

Ao compartilhar um espelho de pedido, o sistema apresenta alerta de falta de permissão à filial, mesmo com permissões liberadas. O analista testou em versões posteriores e não encontrou correção.


**Solução / Diagnóstico**

A coluna CODFILIAL na tabela MXSHISTORICOPEDC estava nula para o pedido em questão. Essa coluna é obrigatória para o compartilhamento. Como o cliente é OERPS, ele deve enviar a informação da filial corretamente. Após preencher, o compartilhamento deve funcionar.


---

## Caso 365

**Contexto**

Códigos de clientes cadastrados pelo aplicativo estão gerando números fictícios que já pertencem a outros clientes da base. O analista identificou que o parâmetro HABILITA_PED_CLI_NAO_SINC está ativo.


**Solução / Diagnóstico**

Esse problema foi corrigido no ticket MXPEDDV-92377. A falha ocorria porque, mesmo após receber a crítica de sucesso do cadastro, o cliente temporário continuava sendo exibido devido a um filtro incorreto na consulta. A correção foi aplicada para que o cliente temporário não apareça após o retorno do ERP.


---

## Caso 366

**Contexto**

Produtos novos (códigos 4022.0, 4023.0, 4024.0) não aparecem no maxPedido, embora estejam ativos para venda pelo Proton.


**Solução / Diagnóstico**

Os produtos estavam com CODOPERACAO = 2 na tabela MXSEST, o que significa que foram deletados no banco nuvem. Por isso, não são enviados para a base do RCA. O cliente deve reenviar o estoque desses produtos com CODOPERACAO = 1 para que voltem a aparecer.


---

## Caso 367

**Contexto**

Um RCA vinculado a duas campanhas de desconto escalonado (códigos 105 e 801) não vê as campanhas no aplicativo, embora elas estejam no banco nuvem e na base local.


**Solução / Diagnóstico**

As campanhas possuem restrições de exclusividade em vários campos (regiões, supervisores, clientes, etc.). Para que sejam exibidas, todas as restrições devem ser atendidas pelo RCA. No caso, as configurações de exclusividade impediam a exibição. O cliente deve revisar as restrições ou criar campanhas sem exclusividade generalizada.


---

## Caso 368

**Contexto**

Um pedido cancelado (nº 74793) não aparece na MXSQTDEPRODVENDA, embora haja histórico de vendas. O analista quer entender a divergência.


**Solução / Diagnóstico**

O pedido foi cancelado, por isso não é contabilizado na tabela MXSQTDEPRODVENDA, que agrega apenas pedidos efetivados. A ausência está correta, pois o pedido cancelado não deve influenciar nas quantidades vendidas.


---

## Caso 369

**Contexto**

O saldo da conta corrente de alguns RCAs ficou negativo, mesmo com parâmetros que deveriam impedir. O analista desabilitou o parâmetro USAR_CCRCA_MAXIMA como paliativo.


**Solução / Diagnóstico**

Para que o sistema impeza descontos com saldo negativo, é necessário ativar os parâmetros corretos: IMPEDIR_ABATIMENTO_SEMSALDORCA e ABATIMENTODEBITARCCRCA. Além disso, a tabela mxssaldoccrca deve estar preenchida. O cliente deve configurar adequadamente esses parâmetros para bloquear a ação quando não houver saldo.


---

## Caso 370

**Contexto**

Ao imprimir um boleto, aparece uma numeração abaixo do código de barras que não corresponde à linha digitável. O cliente quer remover ou igualar.


**Solução / Diagnóstico**

O layout do boleto é customizável. O código de barras pode ser removido ou ajustado clicando duas vezes sobre ele no editor de layout. O cliente deve fazer a customização conforme desejar.


---

## Caso 371

**Contexto**

O limite de crédito disponível no maxPedido difere do Winthor (R$ -1.036,64 vs R$ 1.000). O analista identificou um título de cobrança PIX de R$ 996 que está sendo considerado na nuvem, mas não no Winthor.


**Solução / Diagnóstico**

O título de cobrança PIX está em aberto na PCPREST (DTPAG e VPAGO nulos), por isso é contabilizado na MXSCLIENTECREDDISP. Na rotina 1203 do Winthor, esse título não aparece, indicando que a lógica de cálculo pode ser diferente. O cliente deve verificar como a 1203 está calculando o limite e, se houver diferença, pode solicitar uma melhoria para alinhar as regras.


---

## Caso 372

**Contexto**

O RCA 914 não tem acesso a fornecedores PEPSICO quando acessa a base de um RCA exclusivo, embora tenha as mesmas permissões. O analista suspeita de erro no fluxo de supervisor.


**Solução / Diagnóstico**

O fluxo de acesso da PEPSICO é específico e pode ter particularidades. Devido à complexidade, o ticket foi encaminhado para desenvolvimento para análise mais aprofundada e correção.


---

## Caso 373

**Contexto**

O produto 34469 não aparece na negociação, embora esteja na base do RCA. O analista verificou que o fornecedor não é exibido nos filtros.


**Solução / Diagnóstico**

O cliente utiliza a tabela MXSUSURFORNEC para controle de acesso a fornecedores. O fornecedor 2826, vinculado ao produto, não estava cadastrado nessa tabela para o RCA. Após incluir, o produto passou a ser exibido.


---

## Caso 374

**Contexto**

O produto 1532 não aparece na base do RCA, mas aparece na base do zero. O analista atualizou o ambiente, mas o problema persiste.


**Solução / Diagnóstico**

Foi constatado que não havia dados do produto na base do RCA. Foi realizada uma carga interna para normalizar. O RCA deve sincronizar e validar. Se ainda assim não aparecer, uma nova base deve ser fornecida para análise.


---

## Caso 375

**Contexto**

O cliente quer que orçamentos com mais de 3 dias não possam ser importados para pedido. Configurou o parâmetro CON_PRAZOVALIDADEORCAMENTO, mas não funciona.


**Solução / Diagnóstico**

O parâmetro CON_PRAZOVALIDADEORCAMENTO é válido e deve ser respeitado para novos orçamentos após a configuração. Para testar, é necessário configurar e depois criar orçamentos. O comportamento esperado é que, após o prazo, a importação seja bloqueada. Se ainda assim não funcionar, pode ser um erro, mas a princípio a configuração está correta.


---

## Caso 376

**Contexto**

O campo 'preço de venda sem impostos' aparece no Winthor, mas não no maxPedido. O analista quer saber se há parametrização para exibi-lo.


**Solução / Diagnóstico**

Esse campo não existe no layout atual do maxPedido. Seria uma melhoria a ser implementada caso o cliente deseje.


---

## Caso 377

**Contexto**

Ao tentar alterar a filial retira de um produto, apenas a filial 2 é exibida, quando deveriam ser 2 e 3. Ocorre em base do zero.


**Solução / Diagnóstico**

Faltava o parâmetro UTILIZAFILIALRETIRAFILIALESTOQUE = 'S'. Após ativá-lo, as filiais retira 2 e 3 passaram a ser exibidas corretamente. A filial 6 não aparece porque não foi configurada como retirada para si mesma.


---

## Caso 378

**Contexto**

Ao duplicar um orçamento, o sistema exibe a mensagem 'Campanha excedeu valor máximo de descontos no período'. O analista quer entender o motivo.


**Solução / Diagnóstico**

A campanha tem um limite de desconto máximo por período. O valor já utilizado somado ao desconto do pedido atual ultrapassa esse limite. Por isso a campanha não é aplicada. Ao duplicar um pedido, nem sempre é possível manter as mesmas condições comerciais se o limite já foi atingido.


---

## Caso 379

**Contexto**

Um RCA não apresenta produtos para o cliente 9330, embora haja precificação na região 10 e acesso à região. O analista suspeita de problema na tabela de preço por região.


**Solução / Diagnóstico**

Os dados da tabela mxsregiao estavam divergentes dos da sync_d_mxsregiao, com regiões removidas incorretamente. O cliente deve reenviar os dados de mxspraca, mxsregiao e mxscliente para gerar novamente os registros na integração. Após isso, os produtos devem aparecer.


---
