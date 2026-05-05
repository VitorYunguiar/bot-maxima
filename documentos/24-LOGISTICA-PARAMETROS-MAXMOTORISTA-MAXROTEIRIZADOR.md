# Parâmetros de Logística: maxMotorista e maxRoteirizador

Base operacional para configurar parâmetros dos módulos maxMotorista e maxRoteirizador.

## maxMotorista com Extrator

### MaximaTech
### maxMotorista 
c/ Extrator
## 1° ENTRAR NO AMBIENTE NUVEM.
https://gestaonuvem.solucoesmaxima.com.br/Acessar?ReturnUrl=%2F
Ao acessar o site, clicar em CADASTROS e clicar em AMBIENTE NUVEM, selecionar o cliente e posteriormente clicar no ícone do Sysmax.

## 2° DEFINIÇÃO DO LOGO DA EMPRESA E E-MAIL DE XML DOS CLIENTES
https://maxroteirizador.solucoesmaxima.com.br/#/pages/roteirizacao
Então, antes deixa eu ja explicar pra vocês aqui sobre esses ícones aqui na parte superior direita da tela, o primeiro ícone que é um passarinho é o ícone de autorizações, então sempre que o motorista precisar de alguma autorização ele vai cair aqui nesse ícone para quem está fazendo o monitoramento possa autorizar ou não, e o outro ícone que é um sino, é o ícone de notificação, então aqui vão aparecer informações como motorista fez o check-in fora do local do cliente, entrega inferior a tantos minutos, devoluções e mais outras, tá bom?

Para definir o logo da empresa, vocês vão clicar aqui nesse ícone de chave de boca e clicar em Logo da empresa
Tem também essa outra configuração importante no mesmo ícone que é a de e-mail, essa opção ela vai ser utilizada lá quando o motorista chegar lá no cliente e o cliente pedir o XML da nota, aí estando configurado aqui o motorista consegue na hora fazer esse envio pro cliente, ok? Aí vocês podem utilizar a mesma configuração lá da rotina 132 do Winthor ou do DocFiscal, tá?

## 3° DEFINIÇÃO DOS PARÂMETROS APLICATIVO
https://maxmotorista.solucoesmaxima.com.br/#/pages/configuracoes/parametros-aplicativo
Ao acessar o site, clique na engrenagem no canto superior direito da página e depois clique em Aplicativo para acessar os parâmetros do aplicativo do motorista.

O primeiro parâmetro é o Definir quantidade de casas decimais - Aqui eu preciso saber quantas casas decimais vocês utilizam no Winthor de vocês quando vão fazer devolução? Ou vocês não trabalham com números fracionados?

O segundo parâmetro é Ocultar Valores dos Produtos e os itens das notas, vocês querem que o motorista não consiga visualizar os valores de cada produto da nota e os seus itens ou o motorista pode visualizar ali normalmente?
O próximo parâmetro é Exibir Volumes da Nota Fiscal, vocês querem que seja exibido os volumes da nota fiscal ou não?

Esse próximo parâmetro que é Exibir Letras do WMS no Dispositivo e Exibir Letras WMS por Código de Cliente vocês trabalham com WMS no Winthor?

O outro parâmetro é Cadastrar Conferente No Dispositivo, vocês querem que o motorista possa cadastrar o conferente (Não é obrigatório mesmo que ativo) do cliente (Nome e CPF) que está recebendo a mercadoria lá ou não tem necessidade?

Para esse outro parâmetro que é o Habilitar reenvio de XML para contato do ERP, vocês querem permitir que o motorista só possa enviar a nota fiscal para os e-mails cadastrados dentro do Winthor ou vocês querem permitir que o motorista possa digitar um e-mail novo?

Bora pro próximo que é o Aba sequência de entrega, esse parâmetro aqui vocês querem que tenha ali a sequência de entrega ali dentro do aplicativo, aí vai puxar a sequência tanto do Winthor quanto do maxRoteirizador.
Esse próximo parâmetro é Habilitar fila de espera, esse daqui é quando o motorista chega no cliente e o cliente não pode receber a mercadoria nesse momento. Temos a opção do motorista coloca o cliente em fila de espera, faz as outras entregas e depois volta no cliente para fazer a entrega, vocês acham interessante ou não?

Esse próximo parâmetro Exibir contato do Vendedor, do Supervisor e do Cliente, lá dentro do Winthor já tem essas informações cadastradas, vocês querem que seja exibido pro motorista?

O outro parâmetro é Definir raio de distância máxima no check-in, esse funciona assim, vamos colocar que o motorista foi lá fazer a entrega e ele tá no cliente mas quando ele vai fazer o check-in ele não está na localização exata cadastrada, aí esse parâmetro serve para notificar vocês, qual a distância máxima que o motorista pode fazer checkin fora do endereço exato cadastrado? (checkin é obrigatório)

O próximo é Exigir autorização de check-in fora do raio, esse campo quando habilitado, se o motorista estiver fora desse raio de distância máxima no check-in ele vai precisar de autorização, que cai no ícone ali do passarinho, querem que ative?

O próximo parâmetro é Permitir a visualização do romaneio no Aplicativo, querem permitir?
O próximo parâmetro é Tela de entrega do Aplicativo, temos 3 opções aqui, esse parâmetro é mais para mostrar qual vai ser a primeira aba que vai aparecer pro motorista na tela de entrega.
O próximo parâmetro é Habilitar Reagendamento da entrega via aplicativo, vocês querem permitir que o motorista possa informar que será feito um reagendamento de entregas ou não? Vamos supor que o cliente fala que não pode receber hoje, só pode receber em outro dia, aí o motorista vai informar no aplicativo a nova data. (Ele consegue concluir o carregamento, aí vocês conseguem pegar aquele pedido reagendado que foi reagendado para passar para um outro carregamento.)
O outro parâmetro que é o Habilitar Solicitação de Devolução, esse é um parâmetro que é somente informativo, ele serve mais para adiantar o processo de devolução, querem ativar?
O outro parâmetro é o Habilitar botão de reentrega no aplicativo, essa opção funciona assim, vamos colocar que o motorista não consegue entregar aquela mercadoria a tempo. Então ele vai informar no aplicativo.
(Opção seria pegar os pedidos não entregues e colocar no outro dia em outro carregamento. Feito no WinThor, na rotina 905).

O próximo é o Raio para furo de cerca, ele serve basicamente para definir um raio de distância máxima que ele pode exceder da rota que foi estabelecida.
Aí na aba alertas tem esse parâmetro que se estiver habilitado o gestor do portal vai receber notificação quando essa cerca for ultrapassada
O próximo é o Habilitar Leitura por código de entrega, la no aplicativo ele abre um leitor para fazer a bipagem.O outro é o Habilitar Leitura por volume WMS, la no aplicativo ele abre um leitor para ver os códigos dos volumes do WMS.
O próximo é o Obrigar Bipagem, vocês querem que seja obrigatório pro motorista ter que bipar ou não precisa?
O seguinte é o Obrigar Batida de Horário Refeição, como funciona o horário de almoço do motorista aí de vocês? Vocês fazem esse controle interno ou querem fazer pelo aplicativo da Máxima?
O outro é o Visualizar Notas Fiscais de Acompanhamento (CONDVENDA 4), esse do condvenda4 vai gerar e exibir entregas no qual o tipo da venda foi uma venda tipo 4 - simples fatura.
O outro é o Habilitar utilização do maxPag, pelo que eu vi aqui vocês não contrataram a solução a parte do maxPag, né, não sei se explicaram para vocês mas o maxPag é uma ferramenta a parte que permite ao motorista lá no ato de recebimento da entrega ele gera um link para pagamento da conta se for cartão de crédito, débito ou pix.
O próximo é o Habilitar o validador da NF-E, esse parâmetro se complementa com o debaixo, mas vocês querem que a aplicação valide a qualidade do canhoto, para ver se a imagem está boa, se é um canhoto mesmo ou não.
O próximo é o Tipo de validação do canhoto da NF-E, (se tiver marcado o de cima), vocês querem que ele valide o canhoto pelo NF-E, isso é, ele vai ver a disposição das informações e vai validar se aquilo é uma nota fiscal mesmo, ou querem validar pelo número da nota?
O outro é o Obrigar GPS no registro de Jornada, vocês vão utilizar o registro de jornada?
O outro é o Permitir Realizar Checkin sem Coordenadas, esse parâmetro é mais utilizado quando vocês podem ter clientes que às vezes no Winthor vai estar cadastrado errado o endereço ou desatualizado, aí vocês podem ativar para que o motorista consiga realizar o checkin sem validar as coordenadas.
O outro é o Obrigar justificativa furo de sequência entrega, vocês querem que o motorista precise ficar justificando toda vez que ele furar uma sequência do roteirizador ou não veem necessidade?

Vamos para a aba de FOTOS:
Querem tomar uma água, alongar as pernas ou podemos seguir direto?
O primeiro é o Exigir foto no check-in, esse parâmetro obriga o motorista anexar foto ao realizar o check-in de uma entrega. Pode ser habilitado como OPCIONAL: Tira foto do estabelecimento.
O próximo é o Exigir foto de assinatura, esse daqui tira a foto da NF assinada. Só finaliza a entrega depois de anexar a foto.
Esse próximo parâmetro que é o Foto em caso de avaria, Tirar foto do produto avariado. (estragado, amassado, rasgado, com defeito)
Esse próximo parâmetro é o Exigir foto de dinheiro, se no ato da venda for definido que o pagamento será no ato da entrega.
Esse próximo parâmetro que é o Exigir foto de hodômetro, quando o motorista vai iniciar a entrega, antes de sair ele informa o hodômetro, e quando retorna ele informa novamente. Ativando esse parâmetro, é obrigatório colocar a foto.
Esse próximo parâmetro que é o Exigir foto de cheque, querem que seja obrigatório uma foto do cheque?
Esse outro parâmetro que é o Exigir foto em caso de devolução, caso o motorista realize ali o processo de devolução querem que seja obrigatória uma foto do produto?
Esse outro parâmetro que é o Sincronizar fotos somente via WiFi, se não ativado usa os dados do motorista.
Esse outro parâmetro que é o Exigir Foto da Assinatura do Recebedor da Entrega essa daqui é só se vocês achar interessante porque já tem a foto da assinatura do canhoto, então essa daqui seria uma segunda foto a mais.
Esse outro parâmetro que é o Habilitar foto única para Assinatura Canhoto, essa opção quando habilitada ela permite ao motorista tirar uma única imagem de todas as notas fiscais sem precisar de que ele bata de nota a nota, vocês querem a comprovação de todas as notas fiscais ou basta uma nota?

Vamos para a aba de ALERTAS:
Esses alertas são os que vão chegar ali para vocês no sinos, tá bom?
Exibir notificação de tempo máximo de entrega: Qual é o tempo máximo da entrega? No Roteirizador a gente definiu um tempo médio, mas qual seria o tolerável?
Exibir notificação de tempo máximo de espera: Qual é o tempo tolerável de espera até vocês serem notificado
Exibir notificação de tempo máximo de deslocamento: Olha, se estiver habilitado vocês vão ter que definir qual o tempo máximo que o motorista leva para deslocar de um cliente para o outro cliente.
Configura o intervalo de tempo para receber notificações: Qual tempo quero ser notificado as notificações acima.
Exibir notificação de furo de sequência de entregas: quando o motorista furar a sequência gera notificação ao motorista.
Exibir notificação de devolução: Exibe notificação, caso o motorista efetue alguma devolução parcial ou total.
Exibir notificação de fila de espera: Exibe notificação, caso o motorista coloque uma entrega em fila de espera.
Exibir notificação de bateria do dispositivo: Exibe notificação, caso a bateria do dispositivo esteja próximo do fim.
Alerta de excesso de velocidade: Exibe notificação que o motorista passou o limite de velocidade, caso o parâmetro valor padrão de velocidade limite tenha sido configurado.

Vamos para a aba de OUTROS:

Esse primeiro parâmetro que é o Definir intervalos de sincronização automática, é o tempo de sincronização entre o aplicativo e o portal, o motorista pode sincronizar manualmente também caso necessário, tá?

Esse próximo parâmetro que é o Definir se as entregas realizadas serão mantidas no aplicativo após a sincronização automática, as entregas já realizadas continuam aparecendo ao motorista. Pode acontecer de às vezes os motoristas querer consultar alguma entrega já concluída.

Esse próximo parâmetro que é o Definir período de bloqueio de sincronização, vocês querem bloquear que o processo de sincronização automática aconteça?
O próximo parâmetro é relacionado ao hodômetro e é o Definir quantidade máxima de hodômetros por dia, vocês querem que o motorista registre o hodômetros quantas vezes por dia? No início e no fim? Ou mais?
O próximo parâmetro é o Definir horário de captura obrigatória de hodômetro, os motoristas todos saem no mesmo horário? Se eles saírem, vocês colocam aqui o horário, se não, deixa em branco.
O próximo parâmetro é o Exigir placa de veículo, quando o motorista registrar o hodômetro ele já vai obrigar o motorista a colocar a placa, mas essa informação já vai automática tá?
O próximo parâmetro é o Habilitar o uso de Hodômetro, é só para deixar obrigatório o uso do hodômetro.
Esses próximos parâmetros de RECEBIMENTO basta ler a legenda:

O único diferencial é o Exibir a opções do recebimento, esse parâmetro aqui é para exibir a opção de recebimento no apk, quando ela está ativada, vai aparecer uma opção ao finalizar a entrega do motorista, perguntando se ele quer efetuar o recebimento (pagamento) do cliente ou quer deixar o recebimento como pendente.
O único diferencial é o Ocultar Títulos com Cobrança por Boleto, Esse parâmetro aí basicamente vai ocultar a listagem dos recebíveis no qual a cobrança é boleto (em alguns casos não faz sentido chegar cobrando que o cliente pague um boleto entregando dinheiro pro motorista).

---

## maxRoteirizador

### MaximaTech
### maxRoteirizador
## 1° ENTRAR NO AMBIENTE NUVEM.
https://gestaonuvem.solucoesmaxima.com.br/Acessar?ReturnUrl=%2F
Ao acessar o site, clicar em CADASTROS e clicar em AMBIENTE NUVEM, selecionar o cliente e posteriormente clicar no ícone do Sysmax.

## 2° DEFINIÇÃO DO LOGO DA EMPRESA
https://maxroteirizador.solucoesmaxima.com.br/#/pages/roteirizacao
Ao acessar o site, clicar na chave de boca e clicar em logo da empresa.

## 3° DEFINIÇÃO DOS PARÂMETROS.
https://maxroteirizador.solucoesmaxima.com.br/#/pages/roteirizacao
Ao acessar o site, clique na engrenagem no canto superior direito da página e depois clique em Portal para acessar os parâmetros.

### ESSES PARÂMETROS SE APLICAM A CLIENTES WINTHOR.
O primeiro parâmetro é o Tempo médio de entrega - Esse parâmetro quer dizer que é o tempo médio de todas as entregas, ou seja, ele vai calcular o tempo que ele fez check in no cliente até o momento em que ele finaliza a descarga, esse parâmetro influencia diretamente no processo de realizar a pré-carga. Você gostaria que eu ativasse?
O segundo parâmetro é Trabalhar com custo de montagem do carregamento, caso eu habilite ele vai mostrar no rodapé da tela de montagem um resumo com os custos do carregamento. Vocês gostariam que eu ativasse? (Os custos são o de combustível, motorista e despesas de viagem).
O próximo parâmetro é Listar Veículos Leves, vocês utilizam veículo pequeno para entrega? Se não = deixar desativado.
Se sim = ativar.
Esse próximo parâmetro que é Utilizar faturamento por pedido eu preciso saber se você fatura por carregamento ou por pedido 
Se faturar por pedido = Sim
Se faturar por carregamento = Desativado
(IMPORTANTE: O pedido só aparece pro motorista no aplicativo quando o pedido estiver faturado).
O outro parâmetro é Trabalhar com montagem de pedidos balcão reserva, vocês trabalham com pedido de balcão reserva?
(Pedidos de balcão reserva é quando o cliente compra, pede pro vendedor separar para que depois façam a entrega para ele).
Para esse outro parâmetro que é o Utilizar rota vinculada a praça, vocês utilizam o conceito de praça? (Conceito de praça: A praça está dentro da rota, que está dentro da região, então dentro da região tem várias rotas, e dentro das rotas tem várias praças).
Se sim = ativar.
Se não = desativar.
Bora pro próximo que é o Perfil de Roteirização, nesse daqui nós temos 3 perfis de roteirização:
Velocidade: Prioriza as vias onde a velocidade máxima seja maior.
Distância: Menor distância final percorrida.
Proximidade: Prioriza a distância de um cliente para o outro, mostrar o exemplo que está na pasta imagem.
Esse próximo parâmetro Período entrega, esse parâmetro define a quantidade máxima de dias que o caminhão vai ficar em viagem. (Cliente trabalha com data de retorno?)
Esse próximo parâmetro Validar complementos no reprocessamento de roteirização, ele é um complemento do parâmetro acima, que basicamente vai verificar se aquela quantidade de entregas é possível ser completada dentro da quantidade de dias definida no campo acima ou não, se não for possível, ele bloqueia a montagem da carga.
Se quiser que bloqueie = ativar.
Se não quiser = desativado.
O outro parâmetro é Trabalhar com importação de XML, eu preciso saber se vocês vão utilizar apenas pedidos do ERP ou vão querer realizar importação de XML?
Se for utilizar XML = ativar.
Se não = desativar.

O próximo é Fechar o carregamento por quantidade de dias, esse campo é para definir uma data para fechar o carregamento (caso WINTHOR = deixar em branco; caso outros ERP = perguntar se ele vai enviar o campo DTFECHA pra gente na integração; caso XML = definir uma quantidade
Se for WINTHOR = deixar em branco.
Se for outro ERP = perguntar se ele vai enviar o campo DTFECHA pra gente na integração, se não, definir uma data.
Se for XML = definir uma data.

O próximo parâmetro é Validar campos do WMS (Winthor), vocês utilizam Winthor? Se sim, vocês utilizam a rotina WMS do Winthor?
Se não = desativado.
Se sim = habilitar.
O próximo parâmetro é Validar campos da rotina 902 (Emitir Mapa) do Winthor, vocês utilizam Winthor? Se sim, caso eu ative esse parâmetro, lá no mapa de separação vocês vão ver que o campo DATAMON que é data de montagem estará sem hora e o campo COFUNCFAT que é o código do funcionário que faturou virá como null. (SERVE PARA OCULTAR AS INFORMAÇÕES).
Se não = desativado.
Se sim = habilitar.
O próximo parâmetro é Definir padrão da data saída do carregamento, esse parâmetro ativo basicamente quer saber se você fatura e sai no mesmo dia ou se você fatura e sai no dia seguinte, ele é só para deixar o campo de saída já preenchido, ou com a data do mesmo dia ou com a data seguinte.
Se faturar e sair no outro dia = desativado.
Se faturar e sair no mesmo dia = habilitar.
O outro parâmetro que é o Atualizar as coordenadas do cliente ao realizar o check in, (ler o parâmetro e depois perguntar para ele) você varia muito seu endereço de entrega ou é sempre fixo?
Se variar muito o endereço de entrega = desativado.
Se for sempre fixo = habilitar.
O outro parâmetro que é o Prioriza os veículos de terceiros na busca de veículos para montagem de carga, você trabalha com transportadora ou com veículo próprio? Você quer priorizar os seus veículos ou você quer priorizar os veículos dos terceiros?
Se não trabalhar = desativado.
Se trabalhar com transportadora = habilitar.
Os outros dois parâmetros que são o Permitir Salvar Pré Carga Sem Veículo e o Salvar Pré Carga Sem Motorista, você quer que possa ser feito a pré carga sem motorista e sem veículo? Lembrando que ele só vai permitir salvar a carga se tiver veículo e motorista, mesmo que seja genérico, precisa ter algum.
Se não = desativado.
Se sim = habilitar.
Os outros dois parâmetros que são o Desativar Cadastro de Motorista e o Desativar Cadastro de Veículos, esses dois parâmetros eu preciso saber se no ERP de vocês, vocês já cadastram Motorista e Veículo? 
Se não cadastraram = desativado.
Se já cadastraram = habilitar.
Os outros dois parâmetros que são o Validar valor mínimo por Rota e o Validar valor mínimo por Praça, esses dois parâmetros vão significar a mesma coisa, vocês querem que o sistema bloqueie para caso não atinja o valor mínimo na Rota ou na Praça ou querem apenas saber se atingiu ou não o valor mínimo?
Se não quiserem que bloqueie = desativado.
Se quiserem que realize o bloqueio = habilitar.
Esse próximo parâmetro que é o Trabalhar com Transportadora, vocês trabalham com transportadora? 
Se não = desativado.
Se sim = habilitar.Esse próximo parâmetro que é o Raio de Entrega com Janela, vocês tem clientes com Janela de Entrega? Se sim, esse parâmetro basicamente quer saber, quando o roteirizador for fazer o encaixe daquele cliente que possui janela de entrega, caso ele mude de posição para ser encaixado, qual a distância de clientes que posso mudar de posição junto com ele?
Esse próximo parâmetro que é o Bloquear Alterações de Carregamento em Sincronização, esse parâmetro, vocês trabalham com Winthor? Só explicando, esse parâmetro é para evitar problemas de sincronização, ás vezes você tá fazendo um processo e o Winthor está realizando um processo de sincronizar ao mesmo tempo, então ativando, a gente evita perder dados.
Se não = desativado.
Se sim = habilitar.
Esse próximo parâmetro que é o Habilitar a remoção/adição de pedidos de carregamento, esse parâmetro ativo permite que vocês REMOVAM E EDITEM apenas os PEDIDOS dos carregamentos salvos, não é possível excluir um carregamento.
Se for Winthor e/ou SE não quiser permitir= desativado.
Se quiser permitir habilitar a edição e remoção = habilitar.
Esse outro parâmetro que é o Validar parâmetro WMS conforme WINTHOR, vocês utilizam Winthor e WMS?
Se não = desativado.
Se sim = habilitar.
Esse outro parâmetro que é o Validar campo TipoEntrega do Item do Pedido, você usa o módulo 41 do Winthor? Esse parâmetro serve para quem trabalha com Home Center (Materiais de Construção) no Winthor.
Se não trabalhar com o módulo 41 = desativado.
Se o cliente trabalhar com o módulo 41 = habilitar.
Esse outro parâmetro que é o Considerar o valor total ao consultar pedido na tela de roteirização, serve para saber se você quer que seja mostrado o valor atendido ou o valor total no relatório?
Se quiser que seja o valor atendido = desativado.
Se quiser que seja o valor total = habilitar.
Esse outro parâmetro que é o Tornar obrigatório período final de entrega da roteirização, você quer que seja obrigatório ter um período final de entrega na tela de edição de CARGA para roteirização?
Se não = desativado.
Se sim = habilitar.
Esse outro parâmetro que é o Permitir a quebra de carregamento por filial, você fatura como uma filial ou utiliza duas filiais separadas? No mesmo pedido tem pedidos dos dois CNPJ faturados?
Se utilizar uma = desativado.
Se utilizar duas filiais = habilitar.
Esse outro parâmetro que é o Obrigar vínculo o pedido bonificado no carregamento, você trabalha com venda normal e venda bonificada?
Se não = desativado.
Se o cliente trabalhar com duas notas fiscais, uma para o produto e outra para o bonificado = habilitar.
Esse outro parâmetro que é o Exibir apenas entregas de cliente pai, AINDA NÃO FOI EXPLICADO.
Cadastro de praça = 572.
Cadastro de rota = 520.
