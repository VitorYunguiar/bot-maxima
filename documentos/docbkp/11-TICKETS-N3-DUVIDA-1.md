# Casos Resolvidos — maxPedido

**Sistema:** maxPedido

**Área:** Suporte Técnico / Diagnóstico

## MXPEDDV-106711

**Contexto**

O cliente usa políticas comerciais em alguns produtos, porém ele usa também desconto por plano de pagamento a vista (código 132). Foi feito o cadastro de ambos na MXSDESCONTO, porém não soma os dois descontos.

Foi criada uma política de desconto de 2% (código da política = PLANO) para esse plano, e o produto 206 por exemplo tem 50% de desconto, porém ao tentar colocar as duas condições não valida, apresenta desconto acima do permitido.

Já em um produto em desconto valida a política do a vista como o produto 9295.

É possível o app somar o desconto do produto e mais o do plano quando for o plano a vista cadastrado?

**Solução / Diagnóstico**

O MaxPedido não é possível aplicar desconto sobre desconto. Quando há mais de uma política aplicável, a lógica irá sempre aplicar a de maior desconto.

## MXPEDDV-106712

**Contexto**

Cliente deseja apresentar o Preço Unitário Sem Imposto (IPI) na listagem como já ocorre na tela de negociação.

Atualmente está apresentando um preço unitário sem imposto na aba TABELA que não é o preço praticado.

O que é necessário para que o preço unitário da tela de negociação seja apresentado na listagem da aba TABELA?

**Solução / Diagnóstico**

O parâmetro MOSTRAR_COLUNA_PVENDASEMIMPOSTO_NA_LISTAGEM vai fazer com que use a coluna mxstabpr.pvendasemimposto4, não há cálculos. Se ativar o parâmetro HABILITA_PRECO_FINAL_LISTAGEM, irá calcular o preço na listagem conforme a negociação, porém mostra o preço da embalagem, sem dividir pelo fator da embalagem como na tela da negociação no campo valor unitário.

## MXPEDDV-106713

**Contexto**

Cliente realiza venda apenas por CX e quer que a quantidade na tela de negociação seja pelo QTUNIT da CX. Ao habilitar algumas parametrizações não teve o resultado esperado:

- USAR_QT_UNIT_PROD_EXIBICAO
- EXIBIR_QUANTIDADE_SEM_FATOR_EMBALAGEM
- USAR_QTUNITCX_EXIBICAO

Qual parâmetro necessário para validar o QTUNIT da MXSEMBALAGEM?

**Solução / Diagnóstico**

O atual fluxo utiliza o qtunicx (a quantidade de item que tem na caixa) para obter o preço unitário do produto. Como a embalagem padrão é caixa, a quantidade é a da caixa, não dos itens que estão dentro da caixa. Esses parâmetros citados não alteram o fluxo de exibição da quantidade. O que pode definir uma quantidade é o múltiplo, que permite que quantidades unitárias sejam multiplicadas por um múltiplo configurado, assim todo o fluxo considera as unidades que formam a caixa.

## MXPEDDV-106753

**Contexto**

Cenário onde, mesmo com o parâmetro USAR_MULTIPLO_QTDE e com o múltiplo presente no app, não há registro desse valor no JSON do pedido.

Produto 1 (FORMA REDONDA 20 ALTA) com múltiplo 4, produto 4 (BULE 10) com múltiplo 3.

**Solução / Diagnóstico**

A aplicação envia apenas o campo produto.embalagemSelecionada.multiplo para o backend, e esse campo só é preenchido caso o tipo do produto seja "frios". Caso o cliente queira que o campo seja alimentado para produtos cujo tipo_estoque seja diferente de "frio", uma melhoria deve ser aberta para análise de viabilidade.

## MXPEDDV-106776

**Contexto**

Os pedidos de vários vendedores não sobem para a nuvem para ser feito o GET. Mesmo mudando de rede, fazendo swipe, reiniciando o telefone, não sobem.

**Solução / Diagnóstico**

Verificado que o pedido 416 não foi atualizado pois está vinculado ao pedido 412 e o 412 não recebeu retorno. A crítica não está com o codigopedidonuvem válido. O ERP enviou o JSON com o campo CODIGOPEDIDONUVEM vazio. É necessário orientar o ERP a enviar da forma correta, com o codigopedidonuvem preenchido.

## MXPEDDV-106799

**Contexto**

Os status de pedidos não atualizam. Aparecem com status 4 na tabela de integração de pedido, porém no app não retorna, ou fica na casinha mas está integrado, ou fica com X. No JSON da crítica, o campo POSICAOPEDIDOERP está como "Pendente".

**Solução / Diagnóstico**

O pedido 455 não foi atualizado pois a crítica não está no formato correto. O JSON enviado pelo ERP continha erro de formatação (aspas mal colocadas). É necessário orientar o ERP a enviar o JSON corretamente.

## MXPEDDV-106810

**Contexto**

Demanda referente às permissões de acesso à central de configurações.

**Solução / Diagnóstico**

Foi identificado que o usuário sysmax não possuía vínculo com o ambiente nem as permissões necessárias para acesso à central. O vínculo foi restabelecido e as permissões foram inseridas manualmente na tabela de acessosrotinas. Após o ajuste, o usuário passou a acessar a central normalmente.

## MXPEDDV-106829

**Contexto**

Não subiram para a PCCLIENTFV os dados referentes a roteiro de visitas que os vendedores cadastraram no aplicativo. No JSON os dados estão presentes, mas na tabela os campos estão em branco.

**Solução / Diagnóstico**

Quando o extrator grava as informações de cadastro na PCCLIENTFV e o cadastro possui roteiro, ele faz o insert na PCROTACLI e não nos campos da PCCLIENTFV conforme layout da TOTVS. O cadastro de exemplo não gravou o campo CODCLI porque a integradora não gravou o PCCLIENTFV.CODCLI. Sempre que fizer um cadastro, deve-se verificar a gravação na PCROTACLI.

## MXPEDDV-106853

**Contexto**

Foi realizado a criação do ponto de montagem, algumas fotos não chegaram, mesmo estando no diretório (produto 20179).

**Solução / Diagnóstico**

O ponto de montagem estava correto e a foto do produto estava sendo listada no Docker corretamente. Foi corrigido o endereço do mapeamento das fotos de produto e as fotos foram reprocessadas. O produto citado subiu para a nuvem.

## MXPEDDV-106926

**Contexto**

A equipe do cliente havia alterado o IP do extrator, o que impedia o acesso ao Hangfire. Após ajuste, o acesso ao Portainer e Hangfire foi normalizado. Porém, os dados de dias úteis não são apresentados no gráfico e no resumo de vendas.

**Solução / Diagnóstico**

No cadastro do extrator, o endereço do cliente estava sem "http://". Após adicionar, os gráficos apareceram normalmente.

## MXPEDDV-106951

**Contexto**

Pedido informa que já tem carga montada, mas não tem.

**Solução / Diagnóstico**

O extrator estava online e funcionando normalmente. Ao analisar, o carregamento já havia sido integrado. Caso a falha ocorra novamente, deve-se retornar com a conexão para análise imediata.

## MXPEDDV-106965

**Contexto**

Vendedor não consegue visualizar as fotos dos produtos, mesmo fazendo o procedimento de "baixar fotos". Quando gera um orçamento ou pedido para enviar ao cliente, as fotos são mostradas. Feitos testes com a base do zero, o download das fotos não processa.

**Solução / Diagnóstico**

Não foi possível simular a situação. Ao importar a base, as fotos baixaram normalmente. Caso volte a acontecer, deve-se conectar no aparelho do usuário para validar se há restrições de rede impedindo o download das fotos.

## MXPEDDV-106969

**Contexto**

Diversos pedidos TV14 estão gerando divergência ao gerar a NF pois estão sem a base de ICMS. A TOTVS informou que essa informação vem do FV. Nos JSONs, não estão sendo enviadas informações de ICMS.

**Solução / Diagnóstico**

Para exibir o ICMS é necessário ativar o parâmetro IMPRIME_ICMS_NOTA = 'S'.

## MXPEDDV-106987

**Contexto**

Alguns pedidos ficam com o campo posição vazios na parte de consultas de pedidos na central de configurações. No app o status do pedido aparece, mas na central não.

**Solução / Diagnóstico**

Alguns pedidos não exibem a posição na Central porque não existe registro correspondente na tabela MXSHISTORICOPEDC. O ERP envia o campo NUMPEDERP, e esse valor precisa existir exatamente como NUMPED dentro de MXSHISTORICOPEDC para que a posição seja exibida. Como o ERP ainda não gravou o histórico do pedido, o registro não está presente na tabela.

## MXPEDDV-106988

**Contexto**

O RCA está com problema ao definir horário: na região dele o horário é uma hora a menos. Ele só consegue trabalhar se mantiver a hora do celular errada.

**Solução / Diagnóstico**

Cliente que utiliza sincronização automática também é obrigatório o uso do fuso horário e data automáticos.

## MXPEDDV-107040

**Contexto**

Banco local do cliente não atualiza a versão, mesmo executando as jobs no Hangfire diversas vezes. O extrator fica reiniciando constantemente.

**Solução / Diagnóstico**

**Extrator não subir:** Problema causado por incompatibilidade entre Docker versão 29 e Portainer. Foi instalada a versão 5:27.0.2-1~ubuntu.22.04 do Docker, que possui compatibilidade, e o Portainer subiu normalmente.

**Banco local não atualizava:** Algumas colunas estavam faltando no banco local. Foi passado ao DBA do cliente o documento de grants para execução, permitindo a atualização dos dados.

## MXPEDDV-107044

**Contexto**

Faturamento não chega no ERP. O extrator sofreu shutdown; reiniciando ele volta a funcionar, mas o cenário é recorrente.

**Solução / Diagnóstico**

Não foram identificados logs de erro do extrator de queda ou shutdown no período informado. Caso a falha ocorra novamente, deve-se acionar no momento da falha para análise. Ao abrir o ticket, detalhar a falha junto com prints da análise.

## MXPEDDV-107104

**Contexto**

O cliente usa kit aberto na MXSFORMPROD, com kits cadastrados na filial 10. Quando o cliente é de outra filial (usam MXSTABPRCLI), o kit não abre os produtos. Exemplo: cliente da filial de venda 27, ao selecionar o kit 480070, abre como produto normal; já cliente da filial 10 abre os itens do kit.

**Solução / Diagnóstico**

Esse fluxo não existe no MaxPedido. A rotina 316 do Winthor comporta esse padrão, mas no MaxPedido é necessário uma melhoria para adequar ao ajuste da rotina 316.

## MXPEDDV-107120

**Contexto**

Cliente T-Cloud: solicitado que abrisse as portas 9000, 9001, 9002. Encaminhado para N3 analisar o que pode ser feito da parte da Máxima.

**Solução / Diagnóstico**

Não está sendo possível conectar-se ao banco de dados a partir dos IPs da AWS da Máxima. Necessário verificar com a TOTVS. Após verificação, o extrator subiu normalmente.

## MXPEDDV-107141

**Contexto**

Os pedidos não estão aparecendo para montar romaneio.

**Solução / Diagnóstico**

O mapeamento das imagens estava causando erro no deploy. Foi alterado o endereço das fotos para fazer o deploy.

## MXPEDDV-107183

**Contexto**

O cliente usa desconto por quantidade e embalagens. Ele gostaria que, quando a embalagem passasse da quantidade mínima da campanha, já puxasse o desconto. Exemplo: campanha de 10 a 9999 quantidade com 10% de desconto; na embalagem com 12, queria que já puxasse os 10%. Usam a MXSDESCONTO.

**Solução / Diagnóstico**

Existe a opção do conceito de combo (conforme base de conhecimento) e a opção de criar uma campanha para o código de barras da caixa, onde uma caixa (12 unidades) atende o que 10 unidades atingiria e aplicaria o desconto da política.

## MXPEDDV-107202

**Contexto**

Pagamento realizado no portal e não capturado, porém no Winthor o pedido já foi faturado. O pedido está como faturado e não teve o retorno de pagamento no MaxPag.

**Solução / Diagnóstico**

Foi realizada análise da base de dados local, base de dados nuvem, fluxo no Extrator, fluxo no IntPdv e logs.

## MXPEDDV-107269

**Contexto**

Após diversos procedimentos (forçar parada do app, limpar cache, reiniciar aparelho), o problema persiste. Em outro aparelho entra normalmente.

**Solução / Diagnóstico**

Conectado no aparelho do usuário, ajustadas as permissões de download e rede pelo menu de configurações do Android. Desativados apps que poderiam estar consumindo banda, habilitada a rede móvel. O download da base foi concluído.

## MXPEDDV-107273

**Contexto**

No cliente Zuppani, descontos estão sendo aplicados sobre o preço de tabela apresentado na tela de negociação. Na tela de negociação são apresentados dois valores. Não foi identificado de onde puxa o preço de tabela. Exemplo: produto 009705, região 010112B, cliente 77253601, o PVENDA está 319,02 (igual ao valor total), mas o preço de tabela na tela é 340,71. O desconto é aplicado sobre 340,71.

**Solução / Diagnóstico**

O aplicativo está somando 22% de IPI que está cadastrado para o produto.

## MXPEDDV-107274

**Contexto**

Quando o vendedor faz um pedido TV1 e envia, depois abre o cliente novamente e faz um pedido bonificado, na hora de salvar aparece o TV1 para vincular mesmo que com erro. O correto seria que não aparecesse o TV1 para vincular, visto que ele não foi integrado com sucesso.

**Solução / Diagnóstico**

O comportamento ocorre porque os parâmetros PERMITE_VINCULAR_TV5_COM_TV1_PENDENTE e PERMITE_VINCULAR_TV5_COM_TV1_PENDENTE_ENVIO estão ativados na base. Normalmente, os clientes utilizam apenas o parâmetro PERMITE_VINCULAR_TV1_FATURADO_BNF = 'S', que permite vincular ao TV5 somente pedidos TV1 já faturados.

## MXPEDDV-107325

**Contexto**

Dúvida sobre instalação de cliente. Durante a execução, apareceram mensagens de erro como "tabela ou view não existe", "faltam colunas", "Object reference not set", "ORA-00980", etc. O cliente não executou os grants corretamente.

**Solução / Diagnóstico**

O extrator foi inicializado novamente com o parâmetro PRIMEIRA_IMPLANTAÇÃO = 'S'. Identificado que o usuário MAXSOLUCOES está sem algumas grants necessárias. Enviado arquivo com todas as permissões que precisam ser aplicadas pelo DBA do cliente usando o usuário SYSTEM. Após a execução das grants, deve-se iniciar o extrator novamente.

## MXPEDDV-107326

**Contexto**

Pedidos ficam travados na nuvem. Após reestruturação do banco, sem sucesso. O problema aparece, abre chamado, se resolve sozinho, depois retorna.

**Solução / Diagnóstico**

**Análise APK:** Problema já corrigido no ticket MXPEDDV-105542. O TV5 estava vinculado a um TV1, mas na base existiam dois pedidos (um bloqueado e um já transmitido) com o mesmo número, fazendo a APK entender que o TV1 estava pendente. O erro foi corrigido na versão 4.024.7.

**Análise Backend:** O pedido TV1 foi importado com sucesso e retornou corretamente. Necessária análise da APK para entender por que o pedido não sai do aparelho.

## MXPEDDV-107334

**Contexto**

Produtos 121732 e 121733 não eram apresentados no MaxPedido. Possuem registros na PCTABTRIB, mas não na MXSTABTRIB na nuvem. Foi realizada carga total, mas os registros não chegaram. Outros produtos também estão sem tributação na nuvem (ex.: 2894).

**Solução / Diagnóstico**

A trigger responsável por subir a tributação (MXSTABTRIB) valida os campos REVENDA = 'S', ENVIARFORCAVENDAS = 'S', DTEXCLUSAO = NULL na PCPRODUT. O produto informado estava com REVENDA = 'N' e DTEXCLUSAO preenchido, portanto não foi enviado. É necessário revisar o cadastro do produto no WinThor.

## MXPEDDV-107341

**Contexto**

Cliente estava com problema nas embalagens. Após orientação para configurar o campo UTILIZAVENDAPOREMBALAGEM como 'S' na MXSFILIAL, começou a apresentar erro que impacta os descontos.

**Solução / Diagnóstico**

Com as evidências enviadas, não é possível identificar qual erro o ERP está apresentando. A estrutura enviada para o pedido está correta, mas é necessário que o ERP detalhe o erro encontrado para análise.

## MXPEDDV-107383

**Contexto**

Problemas na transmissão de cadastro de novos clientes. Os clientes não foram transmitidos para o ERP. O suporte do Inovação detectou divergências.

**Solução / Diagnóstico**

O ERP está operando fora do padrão esperado:
- Em retornos de sucesso (status 4), o ERP repete o código do cliente. O correto é retornar o código gerado no próprio ERP.
- Em retornos de erro (status 5), o ERP envia codigo = 0. O código não deve ser informado em caso de erro.
- Na consulta de clientes (GET), devem ser considerados apenas status 0,1,2,9. Status 5 não deve ser utilizado.
- Em novo cadastro, o campo codigo deve ser NULL; em edição, deve vir com o código do cliente.
Necessário alinhar com o integrador responsável.

## MXPEDDV-107395

**Contexto**

Apoio para reinstalação T-Cloud (IAAS). Não foi possível criar tabelas, packages, triggers; o usuário fica sendo bloqueado pela TOTVS.

**Solução / Diagnóstico**

Ajustado o banco de dados do cliente, liberado link do Hangfire pela equipe de tecnologia, ajustado o extrator pelo Jenkins.

## MXPEDDV-107410

**Contexto**

O extrator do cliente está oscilando (online/offline). Verificados logs, atualizado ambiente e Hangfire, mas a oscilação persiste.

**Solução / Diagnóstico**

O usuário MAXSOLUCOES no banco do cliente estava bloqueado. O DBA do cliente realizou o desbloqueio, e o extrator iniciou corretamente.

## MXPEDDV-107424

**Contexto**

Cliente utiliza metas do tipo 'P' (por peso). Gostaria de entender como funciona o vínculo entre produtos e o peso previsto, pois no app não mostra o peso previsto dos produtos.

**Solução / Diagnóstico**

A meta já está sendo calculada e há valores de previsão. Há muitos produtos, e muitos deles o vendedor não gerou dados. Se filtrar apenas os produtos que possuem valor (631, 728, 626, 664, 201, 636...), eles ficam visíveis na tela de objetivos.

## MXPEDDV-107482

**Contexto**

Faixas cadastradas por fornecedor e por supervisor no maxGestão não estão sendo validadas pelo maxPedido. Exemplo: faixa de lucratividade inferior a 26% deveria gerar autorização, mas o pedido é salvo normalmente.

**Solução / Diagnóstico**

Ambas as situações se trataram de permissões no Admin.

## MXPEDDV-107491

**Contexto**

Ambiente com API de cancelamento configurada, mas o cancelamento não funciona. O usuário da WTA acessa normalmente pelo IP informado.

**Solução / Diagnóstico**

O erro já havia sido corrigido em versão superior. Orientado a atualizar o Extrator do cliente.

## MXPEDDV-107511

**Contexto**

Mesmo permitindo usar acréscimo ou desconto, o app não respeita o percentual informado pelo RCA nem o acréscimo automático da condição de pagamento.

**Solução / Diagnóstico**

Habilitar o parâmetro CON_UTILIZAPERCFINPRECOPROM na MXSPARAMFILIAL. Só assim será possível aplicar a taxa do plano de pagamento sobre o preço fixo.

## MXPEDDV-107532

**Contexto**

Os RCAs não estão conseguindo incluir itens no pedido. Aparecem erros. Na edição de pedidos, alguns conseguem cancelar, outros apresentam erros.

**Solução / Diagnóstico**

Atualizada a stack do Portainer para apontar para o IP do novo host.

## MXPEDDV-107576

**Contexto**

A APK está gravando no JSON das justificativas os campos dataAbertura e dataFechamento com um intervalo fixo de 10 minutos, independentemente do horário real da ação. Mesmo após atualização do ambiente e versão, o comportamento persiste.

**Solução / Diagnóstico**

Favor ativar o parâmetro UTILIZA_HORA_APARELHO_JUSTIFICATIVA_VISITA.

## MXPEDDV-107580

**Contexto**

Dúvida sobre a integração do maxPromotor com o maxPedido: qual tabela do banco nuvem armazena as rupturas do maxPromotor? O maxPedido consulta diretamente dela?

**Solução / Diagnóstico**

A APK busca as informações via endpoint, não por banco de dados.

## MXPEDDV-107582

**Contexto**

No mesmo cliente, filial e região, ao pesquisar o produto 002676, o valor na listagem é R$ 32,00, VLTOTAL na negociação R$ 32,00, preço de tabela R$ 33,60. Já o produto 000627: listagem R$ 3,58, VLTOTAL R$ 34,62, preço de tabela R$ 34,62. Não foi identificado o motivo da diferença.

**Solução / Diagnóstico**

O produto 000627 está calculando ST (1,04). Composição: R$ 33,58 (preço base) + R$ 1,04 (ST) = R$ 34,62. A tributação 501001B_RED possui IVA 44,39, alíquota 1=20, alíquota 2=7, redução de base 35%. O produto 002676 usa tributação 0103SST0 que não possui IVA, portanto não calcula ST.

## MXPEDDV-107601

**Contexto**

Ao tentar criar o Portainer, ocorre erro (imagem em anexo).

**Solução / Diagnóstico**

Feito o downgrade do Docker para a versão 28.5.2 e reinstalado o Portainer.

## MXPEDDV-107612

**Contexto**

Pedido do RCA 80017 não sai da nuvem. O pedido 882422653 está somente na APK. Atualização de versão não resolveu.

**Solução / Diagnóstico**

O pedido TV5 não sobe para a nuvem porque o pedido TV1 vinculado a ele teve sua solicitação de limite de crédito rejeitada.

## MXPEDDV-107625

**Contexto**

Problemas nas ações de cancelamento e edição de pedidos. Testes de usuário, link, porta e acesso ao WTA estão corretos, mas o cancelamento não funciona.

**Solução / Diagnóstico**

Há um bloqueio de comunicação de rede entre as duas máquinas. Os logs mostram timeout em todas as tentativas de comunicação com a API de cancelamento, e o ping não responde. Necessário que a infra do cliente resolva o bloqueio.

## MXPEDDV-107628

**Contexto**

Extrator não está subindo após reinstalação.

**Solução / Diagnóstico**

O extrator do cliente está online sem erros. No Gerir Suporte não aparece porque existem dois extratores online. Necessário fechar o extrator antigo (na Mais Dados) que não é mais utilizado.

## MXPEDDV-107640

**Contexto**

Erro de cálculo do produto 3301. O MaxPedido calcula R$ 7,25 + ST = 7,90, mas o ERP (Proton) calcula R$ 7,25 + ST = 8,83. O produto tem redução de base de cálculo.

**Solução / Diagnóstico**

A tributação 070DF40 tem redução de 65% da base de ST. O app aplica a redução apenas sobre a AliqICMS1, mas o cliente informou que a redução deve ser aplicada nas duas alíquotas. Para compatibilidade, deve-se enviar as alíquotas já com a redução aplicada: aliqicms1 = 7, aliqicms2 = 7, percbaseredst = 0.

## MXPEDDV-107653

**Contexto**

Quando o cliente habilita o parâmetro CANCELA_PEDIDO_AUTORIZACAO, pedidos com alteração não são enviados para autorização. O pedido enviado anteriormente fica no ERP como liberado e no MaxPedido aparece alerta de histórico não disponível.

**Solução / Diagnóstico**

Ao ativar o parâmetro CANCELA_PEDIDO_AUTORIZACAO, é necessário reiniciar o extrator. Após ativação e reinicialização, o fluxo funcionou corretamente.

## MXPEDDV-107673

**Contexto**

Ao tentar configurar o Ponto de Montagem, retornou erro. Não foi possível buscar as fotos.

**Solução / Diagnóstico**

Foi feita a configuração do mapeamento de fotos, criada job no crontab, configurado o compose, processada a job. As fotos foram publicadas e acessadas via link do S3.

## MXPEDDV-107698

**Contexto**

O pedido bonificado 888 não subiu para a nuvem. Eles fazem vínculo de TV1 com TV5. Provavelmente algo no 887, mas o 887 está no ERP.

**Solução / Diagnóstico**

O pedido TV1 estava aguardando autorização. Possivelmente o cliente estava enviando o retorno da autorização sem o codPedidoNuvem. Assim que atualizou, o TV5 subiu normalmente.

## MXPEDDV-107713

**Contexto**

Validação de valores de comissão ou vendas com o cliente. Consultas diretas nas views de integração retornam valores divergentes.

**Solução / Diagnóstico**

Será necessário agendar uma reunião com o cliente para apresentar o funcionamento do cálculo e esclarecer todos os pontos. O cliente está sem disponibilidade no momento.

## MXPEDDV-107818

**Contexto**

Lentidão para carregar o card de resumo e pedido na central (cliente EBD).

**Solução / Diagnóstico**

A lentidão foi causada na tela de detalhes de pedido do dashboard, que usava a coluna DTINCLUSAO sem índice. Com a grande quantidade de dados, ficou lento. Foi criado um índice para liberar a consulta. Será criada tarefa interna para analisar possíveis melhorias na consulta.

## MXPEDDV-107849

**Contexto**

Alguns produtos estão com mensagem de erro de tributação.

**Solução / Diagnóstico**

Cadastrada a fórmula PVENDA_ST_IPI_FECP_PAUTA_RED_SEM_FUNCEP na API de fórmulas.

## MXPEDDV-107877

**Contexto**

Produto não processa preço solicitado.

**Solução / Diagnóstico**

O comportamento é causado pelo parâmetro CALCULA_PRECO_NEGOCIACAO_MUDAR_FOCO, que faz com que o sistema só calcule o preço após mudança de foco do campo. Na base ele está = S. Basta alterar para N que o preço será calculado na digitação.

## MXPEDDV-107987

**Contexto**

Ao fazer um pedido, apresenta problema na imagem em anexo. Verificadas filiais e configurações no maxPag/central, aparentemente tudo correto.

**Solução / Diagnóstico**

Análise das configurações do cliente e das tabelas do banco nuvem presentes no fluxo informado.

## MXPEDDV-108075

**Contexto**

Ao subir o extrator, ele não finaliza. Ao pará-lo, ficam vários objetos inválidos no Winthor. Necessário normalizar o ambiente.

**Solução / Diagnóstico**

Executados os grants como system, atualizado o banco local, normalizados os objetos no banco de dados.

## MXPEDDV-108078

**Contexto**

Cliente gostaria de remover os usuários dos motoristas que aparecem na central de configurações.

**Solução / Diagnóstico**

Mesmo após deletar os RCAs, ao acessar a central eles são inseridos novamente. É necessário abrir um ticket de melhoria para alteração desse fluxo. Já alinhado com o PO.

## MXPEDDV-108098

**Contexto**

Os descontos informados na digitação dos pedidos não estão sendo destacados quando chegam no ERP. Alguns pedidos de determinados vendedores destacam.

No JSON, o campo valorTabela está como 0. O produto tem preço de tabela 19,5 e foi vendido a 15,8, mas o desconto não é calculado.

**Solução / Diagnóstico**

A propriedade DTOProduto.PrecoTabela não é alimentada. Favor considerar as propriedades PercDescontoInformadoTela, PrecoVendaInformado e PrecoTabelaInformado.

## MXPEDDV-108105

**Contexto**

Configurado pronta entrega, habilitado parâmetro UTILIZA_PRONTA_ENTREGA, vinculada carga na central, feita carga de dados, mas na consulta do MaxPedido não exibe o carregamento (exemplo NUMCAR 22218).

**Solução / Diagnóstico**

O carregamento em questão tem condvenda = 1 na PCNFSAID. Para gerar dados de pronta entrega, são consideradas notas de saída com condvenda igual a 13.

## MXPEDDV-108162

**Contexto**

Remover usuários dos motoristas da central de configurações. Apenas o RCA "máxima" é vendedor, os demais são motoristas.

**Solução / Diagnóstico**

Não é possível remover os usuários da central. Toda vez que é acessado, os usuários são recriados. Necessário ticket de melhoria para alterar esse fluxo no menu único.

## MXPEDDV-108167

**Contexto**

No endpoint 5.16 NotasSaidaCapas, os dados não estavam chegando ao banco nuvem. Alguns campos obrigatórios não estavam sendo enviados pelo integrador. O cliente questiona por que a API retorna "SUCESSO" mesmo quando faltam dados obrigatórios.

**Solução / Diagnóstico**

Não é possível alterar os retornos da API. Outros clientes utilizam da mesma forma. O layout de integração está disponível na biblioteca. A API retorna vários tipos de erro (HTTP 400, 500, 401 etc.). Caso o layout esteja desatualizado, deve-se falar com o supervisor para atualização.

## MXPEDDV-108178

**Contexto**

Durante a criação do extrator do cliente, ao acessar a URL, ocorre erro "Whitelabel Error Page" e "Unauthorized". O acesso usando IP interno funciona, indicando problema de permissão de acesso externo. A equipe de TI informou que o cliente possui portas externas específicas (20374-20378) que devem ser usadas.

**Solução / Diagnóstico**

Ao usar o ambiente do cliente, é necessário criar o Portainer e configurar a stack apontando para as portas corretas liberadas. Verificou-se que o usuário MAXSOLUCOES não existia no banco do cliente. O DBA precisa executar os grants para criar o usuário e liberar os acessos.

## MXPEDDV-108236

**Contexto**

Comportamento divergente: ao iniciar um pedido "do zero" ou importar um orçamento, o campo de tabela de preço fica editável. Ao duplicar um orçamento, o campo fica barrado para alteração. O cliente relata que antes os RCAs conseguiam alterar.

**Solução / Diagnóstico**

Não é possível alterar a tabela de preço com produtos inseridos no pedido.

## MXPEDDV-108305

**Contexto**

Na grid da tabela de pagamentos do MaxPag, as colunas codigoCliente e Nota Fiscal não aparecem com valores. Esses campos são essenciais para relatórios.

**Solução / Diagnóstico**

**MaxPag:** Não há erro por parte do MaxPag. O problema está na integração do MaxPedido com o MaxPag: ao gerar o link, o campo dadosExtras não é preenchido com os valores desejados.

**MaxPedido:** As informações de NumNotaFiscal e NumCarregamento ainda não estão disponíveis no momento da geração do link, pois serão geradas apenas após o pagamento ser confirmado e o pedido faturado. Foi alinhado com o PO como melhoria.

## MXPEDDV-108314

**Contexto**

Erro ao criar ponto de montagem.

**Solução / Diagnóstico**

O Linux estava sem o pacote cifs instalado, impossibilitando a montagem do compartilhamento. Após instalar o pacote, o diretório foi montado normalmente.

## MXPEDDV-108316

**Contexto**

Preço do produto diverge da tela de negociação do MaxPedido comparado ao Winthor (172,33 vs 172,40), causando corte ao importar o pedido.

**Solução / Diagnóstico**

Somando os preços fixos dos produtos dentro da cesta, multiplicado pela quantidade, dá 169,84 (preço da cesta com ST). Somando 2,49 (valor do FECP que a 316 calcula) = 172,33, que é o valor da APK. Necessário verificar se o preço apresentado na 316 está realmente correto.

## MXPEDDV-108325

**Contexto**

Cliente deseja retirar a obrigatoriedade da justificativa de não venda para produtos em pré-pedido. Na aba de parâmetros da central aparecem apenas 9 parâmetros, mas na MXSPARAMETRO há 587. O parâmetro INFORMAR_MOTIVONAOVENDA_PREPEDIDO existe mas não aparece.

**Solução / Diagnóstico**

O cliente estava com o tipo "INDUSTRIA" habilitado. Foi desabilitado e o ambiente ajustado para não iniciar com Industria = true no token da central. Com a alteração, o SQL carregado foi o do cliente (não indústria).

## MXPEDDV-108338

**Contexto**

Ao realizar um pedido que gera brinde e tentar cancelar, ocorrem dois erros: 1) a aplicação manda cancelar apenas o pedido principal, o brinde não é cancelado; 2) o pedido principal não é cancelado de fato, apenas a legenda muda no app.

**Solução / Diagnóstico**

Foram habilitados os parâmetros CANCELA_PEDIDO_AUTORIZACAO e PERMITE_CANCELAR_PED_BRINDE, e reiniciado o extrator. O fluxo passou a cancelar os dois pedidos corretamente.

## MXPEDDV-108356

**Contexto**

Sugestão de venda valida se o cliente teve 3 vendas de um produto dentro do prazo determinado pelo parâmetro CATALOGO_PEDIDOS_DIAS_SYNC. Se a venda do produto passar do prazo, a sugestão não lista. Cliente com 3 vendas dentro do prazo lista; sem 3 vendas dentro do prazo não lista.

**Solução / Diagnóstico**

A sugestão de venda é montada de acordo com as 3 últimas vendas com base no histórico de pedidos presente na base do vendedor. O parâmetro CATALOGO_PEDIDOS_DIAS_SYNC está definido como 120 dias, portanto só desce para o aparelho o histórico dos últimos 120 dias.

## MXPEDDV-108359

**Contexto**

As filiais parametrizadas para descer para a Máxima (1,2,3) não estão descendo. Foram realizadas diversas ações (reiniciar extrator, atualizar banco, rodar atualizador, carga total, etc.) sem sucesso. Na carga total aparecem outras filiais.

**Solução / Diagnóstico**

A porta no cadastro do extrator estava incorreta. Foi alterada para a porta configurada na stack do cliente, e os dados passaram a aparecer corretamente.

## MXPEDDV-108365

**Contexto**

Cliente Winthor, extrator operando, mas pedidos não estão sendo processados.

**Solução / Diagnóstico**

Os pedidos não integram devido a timeout na requisição para obter os pedidos. O extrator consegue se comunicar com a API, mas a taxa de download na máquina do extrator está lenta, demorando mais de 5 minutos para baixar o JSON, enquanto o timeout é de 3 minutos. Verificar com o provedor de internet do cliente a lentidão.

## MXPEDDV-108384

**Contexto**

Problema recorrente de tributação. Na demanda anterior, foi tratado via N3 com cadastro de fórmula na API. O mesmo comportamento voltou a ocorrer em outros cenários com fórmulas diferentes.

**Solução / Diagnóstico**

Atualmente não é possível identificar quais fórmulas foram criadas pelo cliente em seu ambiente para realizar o cadastro. O cadastro é feito sob demanda. Favor solicitar ao cliente todas as fórmulas personalizadas criadas e enviar para cadastro.

## MXPEDDV-108498

**Contexto**

Representante faz a justificativa das visitas pelo aplicativo, mas não aparece na central de soluções. A última justificativa que aparece é de 03/10.

**Solução / Diagnóstico**

Foi identificado que o Portainer e o Extrator não estão instalados. Por isso, ao chamar o método de salvar visita, a informação não é gravada corretamente. O implantador foi orientado a subir o Portainer e a stack do Extrator conforme o manual.

## MXPEDDV-108522

**Contexto**

RCA fez um pedido com 140 itens, mas ao enviar percebeu que tinha apenas 24 itens, mantendo o valor total. O pedido foi salvo e bloqueado, depois alterado. O relatório do pedido retorna um valor anormal.

**Solução / Diagnóstico**

Necessária a base de dados para continuidade da análise. A base anexada não continha o pedido de exemplo. O valor total vem do JSON em root.valorTotal. Necessário o JSON da APK para análise.

## MXPEDDV-108523

**Contexto**

Política de desconto escalonado cadastrada, mas a legenda não aparece e o desconto não é aplicado.

**Solução / Diagnóstico**

Existe restrição de exclusividade para pedido Telemarketing. Necessário remover essa restrição para que o desconto seja aplicado.

## MXPEDDV-108549

**Contexto**

Cliente teve erro no link do MaxPag, resultando em pedidos duplicados. Os pedidos com erro ficaram presos na base, consumindo estoque, e não é possível cancelar.

**Solução / Diagnóstico**

Pedidos com erro de link de pagamento presos na base do RCA, sem opção de cancelamento ou deleção. Orientado a ativar o parâmetro PERMITE_APAGAR_PEDIDOS na central de forma temporária para que o RCA sincronize e faça a exclusão.

## MXPEDDV-108560

**Contexto**

O job que atualiza as imagens não está funcionando. As imagens são upadas no site mas não aparecem automaticamente para o RCA. O processo de baixa automática de fotos na APK (uma vez por dia) não está acontecendo.

**Solução / Diagnóstico**

Fluxo de download de fotos: ao acessar a tela inicial pela primeira vez, o app agenda o download automático para 24 horas depois. Após a primeira execução, ocorre uma vez por dia. O fluxo foi simulado e validado com sucesso. O download manual também funciona.

## MXPEDDV-108561

**Contexto**

Ao compartilhar foto do produto, as informações marcadas nas configurações não são apresentadas corretamente. Na V3 funcionava.

**Solução / Diagnóstico**

O MaxPedido está enviando os detalhes do produto junto com as fotos. Se compartilhado por e-mail ou Telegram, os detalhes aparecem. No WhatsApp, o aplicativo rejeita o EXTRA_TEXT da imagem. É um bloqueio do próprio WhatsApp.

## MXPEDDV-108563

**Contexto**

Na versão mais recente do app (4.028.1 e 4.028.2), a tabela de preço da filial não carrega. Em versão mais antiga (4.011.2) funciona.

**Solução / Diagnóstico**

Os parâmetros USATABPRECOFILIAL e VALIDA_FILIAL_MXSCLIENTREGIAO estão habilitados, exigindo vínculo entre Cliente x Região e Filial x Região. Como não há vínculo Cliente x Região, as tabelas de preço não são carregadas. Necessário criar esse vínculo ou desabilitar VALIDA_FILIAL_MXSCLIENTREGIAO.

## MXPEDDV-108645

**Contexto**

Ao copiar o espelho de um pedido original, a cópia não respeita o parâmetro EXIBIR_CAMPOS_ESPELHO_POR_EMBALAGEM. O original apresenta quantidade em caixa, a cópia apresenta quantidade em unidade com embalagem caixa, gerando inconsistência.

**Solução / Diagnóstico**

Foi realizada análise do fluxo de geração de relatórios, do espelho do pedido, simulação no ambiente do cliente, análise do projeto de geração de relatório e dos dados necessários.

## MXPEDDV-108747

**Contexto**

Campanha promocional configurada na rotina 3306 para utilização por família de produtos. Ao acessar a campanha no Força de Vendas, a mensagem "Nenhum produto da campanha pode ser carregado" é exibida.

**Solução / Diagnóstico**

As embalagens dos produtos filhos estavam marcadas para não enviar ao força de vendas. O cliente ajustou e normalizou.

## MXPEDDV-108770

**Contexto**

Pedidos foram faturados e a integração enviou a atualização, mas no maxGestão não aceita a atualização. O pedido 2113683 está com erros.

**Solução / Diagnóstico**

O integrador está enviando a posição como "P" (PENDENTE). O pedido chegou com status PENDENTE e foi gravado assim. Mesmo com o envio de dados de NF no endpoint NotasSaidasCapas, é obrigatória a atualização da posição também no endpoint HistoricoPedidosCapas. Necessário validar a integração do cliente.

## MXPEDDV-108785

**Contexto**

Após atualização no Winthor, os pedidos estão integrando mas não estão sendo processados automaticamente. Pedido exemplo: 18274399.

**Solução / Diagnóstico**

Estavam ocorrendo erros na chamada para a integradora, provavelmente devido a objetos inválidos ou falta de grants. O usuário maxSolucoes não tinha acesso. Após a TOTVS executar as grants e validar a integradora, o problema foi corrigido.

## MXPEDDV-108806

**Contexto**

O extrator parou com erro aparentemente relacionado ao diretório das fotos.

**Solução / Diagnóstico**

Ajustado o diretório de imagens no compose do Portainer. Ajustado o novo diretório "imagens_data_segalas" no script de montagem de arquivos e validada sua execução.

## MXPEDDV-108832

**Contexto**

Ao buscar o produto 2019, o sistema lista corretamente com estoque 121. Ao selecionar, o estoque é exibido como zerado na negociação. Ao retornar para a tabela, o estoque também fica zerado. Existe cadastro na MXSFILIALRETIRA (filial retira 2 vinculada à filial venda 4). O RCA não tem permissão para a filial 2. Mesmo após excluir o registro, o sistema continua validando a filial 2.

**Solução / Diagnóstico**

Está configurado para usar filial retira, com DEFINE_FILIAL_RETIRA_PADRAO = 2, mas o usuário não tem permissão para essa filial. Também está configurado que a filial retira da filial 4 é a própria filial 4. Há conflito de parametrizações. O ajuste deve ser: não usar filial retira, ou definir DEFINE_FILIAL_RETIRA_PADRAO = 0 (pegará a filial retira relacionada à filial 4), ou dar permissão ao usuário para a filial 2.

## MXPEDDV-108880

**Contexto**

Pedido foi editado e reenviado ao ERP. Durante a edição, o pedido original foi cancelado automaticamente e gerado um novo. Após isso, o pedido deixou de aparecer no Palm do vendedor. A crítica de integração apresentou erro de API de cancelamento, mas o ERP enviou o histórico do novo pedido e o cancelamento do original. O pedido consta na base com status 8 (Pendente de Autorização), mas não há registros de avanço para autorização.

**Solução / Diagnóstico**

Quando um pedido é editado pela API do Winthor, o pedido é cancelado e gerado um novo mantendo a mesma numeração do RCA. No cenário, a API do Winthor gerou o cancelamento e retornou uma crítica interna de erro, interrompendo o fluxo no MaxPedido, mas o Winthor gerou o novo pedido e o histórico. O erro não foi replicado no desenvolvimento. Para o cliente, foi enviado um comando SQL via sincronização para atualizar o pedido na base do usuário.

## MXPEDDV-108893

**Contexto**

Ao editar qualquer cliente, o aplicativo sempre solicita informar a "UF", mesmo que a informação já esteja no cadastro.

**Solução / Diagnóstico**

A aba que não carrega o Estado é a de Endereço Comercial. A coluna estcom da tabela mxsclient está NULL, ou seja, o cadastro já vem do cliente com o campo Estado do Endereço Comercial vazio.

## MXPEDDV-108931

**Contexto**

Ao tentar configurar o relatório da 800, o portal não lista os relatórios para serem liberados.

**Solução / Diagnóstico**

Configurado o gerador800 no IIS, configurado appsettings.json, reiniciado o IIS. Os relatórios passaram a funcionar normalmente.

## MXPEDDV-108940

**Contexto**

Em consultas > venda pronta entrega, os itens 130 e 141 aparecem mais de uma vez, mesmo tendo a mesma embalagem.

**Solução / Diagnóstico**

Falha corrigida na versão 4.030.1 pelo ticket MXPEDDV-108947.

## MXPEDDV-108985

**Contexto**

Cliente alega não conseguir realizar um DELETE no endpoint ClientesRegioes. Tentativa de alterar o link, retorna 503 ServiceTemporarilyUnavailable.

**Solução / Diagnóstico**

Orientado o cliente a utilizar o link correto (https://intext-oerp.solucoesmaxima.com.br:81/api/v1/ClientesRegioes/Todos). Após modificar, o DELETE funcionou corretamente.

## MXPEDDV-108986

**Contexto**

Cliente informa consumo excessivo de bateria ao utilizar o MaxPedido.

**Solução / Diagnóstico**

De acordo com os logs, o rastro estava sendo coletado com frequência de 5 em 5 segundos (parâmetro GPS_TRACKING_INTERVAL). Foi alterado para 30 segundos, reduzindo o consumo de bateria.

## MXPEDDV-109001

**Contexto**

Ao configurar o relatório da 800 e testar no aplicativo, retorna mensagem "Não foi encontrado nenhum diretório válido para buscar os relatórios".

**Solução / Diagnóstico**

Configurado o caminho do relatório no appsettings.json com o caminho completo, sem mapeamento. Testada a geração do relatório 8072 (com layout). O relatório 8181 não tem layout, gerando páginas em branco tanto no Winthor quanto no gerador800.

## MXPEDDV-109083

**Contexto**

Não foi possível subir a base no aparelho do representante após várias tentativas.

**Solução / Diagnóstico**

Apoio apenas orientando onde validar. Toda tratativa foi realizada pelo próprio suporte.

## MXPEDDV-109098

**Contexto**

Cliente reclama que as informações de previsões de recebimento não são apresentadas corretamente no MaxPedido.

**Solução / Diagnóstico**

O parâmetro GERAR_DADOS_EST_PENDENTE estava NULL e configurado por usuário. Por ser um parâmetro do backend que ativa a job, ele não funciona por usuário. Ao ativá-lo, é necessário esperar a job rodar para gerar os dados na tabela mxsestpend.

## MXPEDDV-109101

**Contexto**

Aplicativo crashando na versão 4.028.3 e também na versão ponta 4.029.1. Stack trace aponta NullPointerException em ActCampanhasProdutos e ForegroundServiceStartNotAllowedException.

**Solução / Diagnóstico**

Solicitado que o cliente relogasse no MaxSoluções. Após fazer isso, o erro não ocorreu mais.

## MXPEDDV-109113

**Contexto**

Pedido de pronta entrega teve erro em uma nota e não faturou. No painel, o pedido estava cancelado, mas no aplicativo o item não voltou ao estoque e não aparecia opção de cancelamento. Produto 39730. Pedido consta no histórico como cancelado, mas não houve retorno das quantidades de estoque. Não há registro do pedido nas tabelas PCPEDCFV, PCPEDC, PCNFCAN.

**Solução / Diagnóstico**

O pedido não possui registro na PCPEDC, mas está faturado na PCNFSAID e com dados na PCPEDCFVMANIF. Por algum motivo, não foi gravado na PCPEDC, fazendo o processo ficar em loop. Necessário verificar com a TOTVS o motivo.

## MXPEDDV-109129

**Contexto**

Cliente mudou o regime contábil para Lucro Real. No Winthor, os pedidos são emitidos com cálculo correto. No pronta entrega, os pedidos saem com regime tributário incorreto (impostos zerados). Os campos de impostos na PCPEDCFVMANIF e PCPEDIFVMANIF estão zerados.

**Solução / Diagnóstico**

Para visualizar as informações de ICMS, é necessário ativar o parâmetro IMPRIME_ICMS_NOTA = 'S'.

## MXPEDDV-109155

**Contexto**

A aplicação não atualizou pedidos na timeline. Pedido foi editado no app, gerou histórico e crítica corretos, mas a APK não mostra a atualização mesmo após sincronizar. A base do app não atualizou o pedido na MXSPEDIDO.

**Solução / Diagnóstico**

Ao editar um pedido pelo Winthor, desce para a APK apenas o registro na MXSHISTORICOPEDC, sem alterar a MXSPEDIDO. É necessário habilitar o parâmetro PESQUISAR_PEDIDO_APARELHO_COM_HISTORICO para que os pedidos do histórico sejam apresentados.

## MXPEDDV-109220

**Contexto**

Pedidos com itens de cesta básica (tipo CS), mesmo aplicando acréscimo, não movimentam o saldo de conta corrente do RCA. Itens que não são do tipo CS movimentam normalmente.

**Solução / Diagnóstico**

O conta corrente do vendedor está movimentando corretamente ao dar acréscimo de 10% sobre o item 160967. Necessário verificar por que a integradora não movimentou o conta corrente.

## MXPEDDV-109232

**Contexto**

Vendedor não consegue salvar orçamentos após atualizar o app. Cliente T-Cloud.

**Solução / Diagnóstico**

Na última versão já há correção, mas é necessário limpar a base, pois a correção só se aplica a novos casos, não é possível ajuste retroativo.

## MXPEDDV-109242

**Contexto**

Cliente OERPs relata que pedidos não estão atualizando na timeline. Pedido consta com status "P" no banco nuvem, mas não atualiza no MaxPedido.

**Solução / Diagnóstico**

A timeline não atualiza porque na crítica enviada pelo ERP, o numpederp está vindo como decimal (ex.: 44444.0). É necessário corrigir o ERP para enviar o valor correto (ex.: 44444) nos campos numPedido, codigoPedidoNuvem e numPedidoERP. O problema começou a ocorrer a partir de 22/12, indicando alteração no ERP.

## MXPEDDV-109264

**Contexto**

Problema em alguns clientes (2759 e 2730) onde não é possível incluir produtos no pedido; o sistema apresenta mensagem de erro ao carregar tributação. No Winthor, a tributação está OK. Os clientes estão com o campo ESTENT = NULL na MXSCLIENT. Carga total não atualizou.

**Solução / Diagnóstico**

Na tabela PCMXSCONFIGURACOES, o parâmetro INVERTER_END_CLIENTE está 'S', fazendo com que ao gravar na MXSCLIENT inverta as colunas ESTCOM e ESTENT. Por isso ESTENT está NULL. A solução é desativar o parâmetro ou preencher o endereço comercial dos clientes no Winthor.