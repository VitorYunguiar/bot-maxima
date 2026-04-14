# GATE-537 - funcionalidade para gerar destaques em clientes especificos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2024-12-20T14:36:43.471-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Senhores, ao analisar a demanda citada onde o cliente diz o seguinte:
"preciso que alguns clientes aparecem com algum destaque de ou cores diferentes... pois são clientes schatech e precisar ter uma atenção maior para venda". Não consegui identificar um formato de configuração que hoje atenda o cliente. O mesmo testou a viabilidade de utilizar cores por classe de venda(com base no campo VIP da MXSCLIENT), porém o cliente já utiliza essas classes internamente no winthor para a sua regra de negócios para indicar diferenças de faturamento.

Existe algum outro formato em que o cliente consiga gerar esse destaque de forma que ele possa escolher os clientes com base em seu próprio critério? Em anexo segue audio curto do cliente explicando sua necessidade.

## Comentarios do Gatekeeper

### 1. 2024-12-20T14:36:43.470-0300 | Filipe do Amaral Padilha

Qualquer outra forma que ele quiser diferente disso que cito abaixo, poderia ser considerado para avaliação como Melhoria do sistema.

Sobre sinalização que eu encontrei no maxPedido, atualmente teríamos:

Por Classe de Venda e coloração: Seria possível mudar a coloração do cliente por classe de venda que é a informação que a gente integra na CLASSEVENDA da MXSCLIENT, algo que o cliente preenche na 302. Informação sai na listagem de clientes.

Por definição de cliente "VIP": Tem um campo que integramos também dos clientes que é o campo "VIP" da MXSCLIENT, porém diferente dos outros, esse campo para o RCA visualizar no app, teria que apertar para "Ver informações cadastrais" antes ou depois que já tivesse iniciado o pedido.

Por 'Cliente Sinalizado': É um parâmetro por DEFAULT é false SINALIZA_CLIENTES e trabalha em conjunto com QT_DIAS_SINALIZAR_CLIENTE = 60 que é uma informação validada através da MXSCLIENT no campo DTULCOMP. Quando ultrapassa o número de dias do QT_DIAS_SINALIZAR_CLIENTE, gera uma legenda que é um ícone amarelinho na listagem de clientes chamada "cliente sinalizado", você consegue conferir apertando nos "três pontinhos" na listagem. A informação sai na listagem de clientes.

Por Faixa de Sortimento: Não são todos os cliente Winthor, que tem a opção de cadastrar o cliente por Faixa de Sortimento. No Winthor em específico eu não sei como ele faria para configurar a integração e cadastro desse campo, porém eu sei que a Nordil tem isso na Rotina 302 deles. O cliente teria que ver dois pontos com a TOTVs, sendo 1° se existe a possibilidade de habilitar e 2° se habilitado, se ele pode cadastrar quantos números quiser ou é restrito à seis faixas (1,2,3,4,5,6). A informação sai na listagem de clientes com cor roxa.

Outra possibilidade, se ele curtir a ideia da faixa de sortimento, poderia também entrar em contato com a CS ou através de melhoria solicitar acesso a API da Máxima para integrar diretamente via API no endpoint de clientes no campo faixasortimento. Afinal, por exemplo, Laredo é cliente Winthor mas tem acesso para integrar na API o pré-pedido.

## Resposta Canonica

Atualmente, não foi identificado no sistema um formato de configuração que atenda exatamente à necessidade de destacar clientes com base em critério próprio, além das opções já existentes.

As alternativas hoje identificadas são:

- **Classe de Venda com coloração**: utiliza a informação integrada na `CLASSEVENDA` da `MXSCLIENT`, preenchida na rotina 302, e a informação é exibida na listagem de clientes.
- **Cliente VIP**: usa o campo `VIP` da `MXSCLIENT`, porém essa informação **não aparece diretamente na listagem**; para o RCA visualizar no app, é necessário acessar **"Ver informações cadastrais"** antes ou depois de iniciar o pedido.
- **Cliente Sinalizado**: exibe uma legenda com **ícone amarelo** na listagem de clientes quando o número de dias configurado é ultrapassado, com validação pelo campo `DTULCOMP` da `MXSCLIENT`. Parâmetros envolvidos:
  - `SINALIZA_CLIENTES = false` por padrão
  - `QT_DIAS_SINALIZAR_CLIENTE = 60`
- **Faixa de Sortimento**: a informação pode ser exibida na listagem de clientes com **cor roxa**. Porém, nem todos os clientes Winthor possuem essa opção, e não foi informado como configurar a integração e o cadastro desse campo no Winthor. Há indicação de que a Nordil possui essa configuração na rotina 302.

Limitações identificadas:
- Qualquer forma diferente das opções acima depende de **avaliação como melhoria do sistema**.
- O uso de **Faixa de Sortimento** depende de validação com a **TOTVS**, inclusive para confirmar:
  - se é possível habilitar o recurso no Winthor;
  - se o cadastro permite quantos números forem necessários ou se há restrição a **seis faixas**.

Encaminhamento recomendado:
1. Validar com o cliente se alguma das opções existentes atende parcialmente a necessidade.
2. Caso nenhuma atenda, encaminhar para **avaliação como melhoria**.
3. Em paralelo, verificar com a **TOTVS** a viabilidade de habilitar e cadastrar **Faixa de Sortimento**.
4. Se necessário, acionar a **CS** ou solicitar via melhoria acesso à API da Máxima para integração do campo `faixasortimento` no endpoint de clientes.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 413454
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
