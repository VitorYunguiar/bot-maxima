# Diagnóstico e Playbooks de Atendimento da Logística

Guia para investigação de problemas nos módulos maxMotorista e maxRoteirizador.

## Guia de diagnóstico

## 1 Visão Geral do Sistema de Logística

Este documento serve como base para analistas de suporte realizarem diagnóstico de problemas reportados por clientes no sistema de logística.
Ele não é um manual de uso da tela, e sim um guia de investigação técnica: quais tabelas consultar, como elas se relacionam, quais campos são obrigatórios, quais parametrizações impactam a visibilidade dos dados e quais perguntas fazer ao cliente antes de abrir um chamado para o time de desenvolvimento.
### 1.1 Módulos
#### 1.1.1 maxMotorista
📊 Dashboards
Visão Tático Operacional
Nível de Serviço Logístico - OTIF
Visão Gerencial
Painel de Monitoramento
Controle de Portaria
### Indicadores de Entregas
Painel de Custos - Tabela Frete
### Produtividade por Motorista
Retornos de Viagem
### Dashboard de Análises de Entrega e do Romaneio
Despesas
📝 Relatórios
Notas Fiscais Pendentes
Notas Fiscais por Situação
Registros de Jornadas
Apuração de Campanha
### Entregas Realizadas
### Entregas Consolidado
### Geolocalização entregas x clientes
Hodômetro
Despesas
### Percentuais de Entrega, Valores e Peso
### Tempo / desempenho motorista
### Motoristas Envolvidos no Período
Ocorrências por carregamento
Análise de TMA por Cliente
Custo Previsto X Realizado
Romaneio
Ocorrências
Ocoren
Canhotos
### Tabela Frete Operacional/ Carregamento e Entrega
Tempos
Tempo no Cliente
### Tempo de Espera do Pedido
Tempo Médio no Cliente
### Tempo Médio em Entrega
### Tempo Médio do Pedido
Tempo Médio Aguardando no Cliente
✍️ Cadastros
Centro de Distribuição
Clientes
Motivo
Devolução
Cancelamento
Furo de Sequência
Reagendamento
Ocorrências
Canhoto
Jornadas
Jornada
Ausência
Registro de Jornada
Horários de Trabalho
Contatos
Visão Painel Gerencial
MaxPag
Dias Úteis
Pontos de Referência
🔍 Consultas
Listagem de Romaneios
Listagem de Carregamentos
Despesas
Tipos de Despesas
Despesas do aplicativo
### Entregas
Hodômetros
### Reentregas
Recebíveis
Cidades
Eventos
Descargas Canceladas
### Log de Sincronização do Motorista
Registro de pontos de parada
### Auditoria de Coordenadas de Entrega
Veículos
Comodatos
✅ Autorizações
### Autorizar Entrega fora do Raio
### 📄 OCOREN
Importar
🗺️ Mapas
### Monitoramento de entregas
### Monitoramento do Motorista
📰 Ocorrências
⚙️ Configurações
Usuários
Perfil de Acesso
Portal
Aplicativo
Administrativo
Logo da Empresa
Geração de coordenadas/Geocode
E-mail
Rastreador
Whatsapp
📦 MaxInsights
#### 1.1.2 principais maxRoteirizador
🗺️ Roteirização
🔍 Consultas
Romaneios
Carregamentos
Painel de Baixa Pgto Frete
Painel de carga automática
Falha Geocode
📊 Dashboard
Visão Tático Operacional
Nível de Serviço Logístico - OTIF
Visão Gerencial
Painel de Monitoramento
Controle de Portaria
### Indicadores de Entregas
Painel de Custos - Tabela Frete
### Produtividade por Motorista
Retornos de Viagem
### Dashboard de Análises de Entrega e do Romaneio
Despesas
Indicadores de uso
### Pedidos prontos para montagem
✍️ Cadastros
Filiais
Centro de Distribuição
Clientes
Ramo de atividade
### Motoristas
Ajudantes
Combustível
Tipo de Veículo
Característica do veículo
Veículos
Rotas
Motivo
Transferência
Tabela Frete
Ponto de Parada
Áreas de Atendimento
Regiões de Atendimento
### Solicitação de Entrega/Coleta
Palavras Chave
Identificação Personalizada
Carga automática
📄 Relatórios
Resumo de montagem
Lucratividade por Romaneio
Custo por Romaneio
Extrato de Custo por Transportadora
Embarque de veículo
### 💻 XML
Importar
### EXCEL
### Cancelar Pedidos
🛠️ Melhorias
✅ Autorizações
📍 Mapas
Visualizar Clientes
⚙️ Configurações
Usuários
Perfil de Acesso
Portal
Aplicativo
Administrativo
Logo da Empresa
Geração de coordenadas/Geocode
E-mail
Rastreador
Whatsapp
Certificados Digitais
📦 MaxInsights
### 1.2 Conceitos de negócio importantes
#### 1.2.1
### Faz a gestão das entregas, ele seria um complemento do roteirizador
Rotina que faz o faturamento do carregamento 1402
Só aparecer os carregamentos depois de faturados
O maxMotorista só controla as notas de mercadorias, não controla nota de transporte.
Dashboard inicial
Resumo da situação dos motoristas: em trânsito, em espera, em entrega.
Informações de entregas do dia, pendentes e possíveis atrasos.
Nível de Serviço Logístico (OTIF) e controle de portaria.
Visões relacionadas a retorno de viagem e desempenho das entregas.
Relatórios
Extração de relatórios em PDF e Excel.
Possibilidade de consultar na tela antes, com filtros.
Diversos relatórios operacionais e gerenciais (a serem detalhados depois).
Cadastros
Cadastro de jornada de trabalho, dias úteis e motivos (devolução, cancelamento, furo de sequência, etc.).
Cadastros que alimentam o aplicativo do motorista e o portal.
O que é configurado aqui impacta diretamente o que o motorista enxerga e registra.
Consultas
Consultas diretas no painel, sem precisar gerar relatório.
Visualização de romaneios, despesas lançadas, entregas, hodômetros, entre outros.
Complementa os relatórios, com foco em consulta rápida dentro do sistema.
Autorizações
Tratativa de solicitações de entrega fora do raio.
Controlado por parametrização do sistema.
### OCOREN
Tela para importação de arquivos OCOREN.
Mapas
Monitoramento de entregas em mapa.
Acompanhamento do motorista em tempo quase real: percurso, entregues, pendentes.
Ocorrências
Gerenciamento das ocorrências registradas pelo motorista.
Pode envolver solicitação de apoio ao supervisor.
Configurações
Configuração de usuários e perfis de acesso.
Parametrizações do portal, aplicativo e área administrativa.
Integração com rastreador de veículo.
Configuração de e-mail para disparo de canhoto (e outros canais, se parametrizados).
#### 1.2.2
Carregamento: é um objeto onde vai ter várias notas, uma organização logística das entregas, e a parte financeira fiscal; é um conjunto de pedidos para poder montar a carga para ser entregue.
Rota: Rota está vinculado a Região do cliente, onde organizo clientes por região física, com isso posso criar uma rota para entrega em regiões específicas. Um conjunto de clientes em um trajeto.
Fluxo: montar o carregamento/roteirizar (pelo roteirizador), faturar (ERP), depois vai para o motorista (pelo maxMotorista).
Perfeito, vou resumir o maxRoteirizador no mesmo estilo enxuto que fizemos pro maxMotorista, separado por menus.
Roteirização
Onde é feita toda a roteirização no mapa.
### Montagem de carga dos pedidos integrados:
Vindo da força de vendas.
Via integração nativa (Winthor) com ERP.
Via outros ERPs integrados.
Via importação do XML da nota fiscal.
Define quais pedidos vão em qual carga/carregamento.
Consultas
Consulta das cargas já montadas.
Visualização dos carregamentos e seus status (faturado, em entrega, etc.).
Painel para baixa de pagamento de frete, quando há frete terceirizado.
Dashboard
Indicadores de uso do roteirizador.
Visão de pedidos prontos para montagem (já integrados).
Indicadores de quantidade de cargas montadas pela Max x montadas fora.
Visões gerenciais e operacionais sobre a roteirização.
Cadastros
Cadastro de centro de distribuição, filiais, ramos de atividade e veículos.
Abriga cadastros gerais do roteirizador.
Também exibe dados que vêm do ERP (quando há integração), permitindo apenas visualização ou edição pontual.
Relatórios
Relatórios de resumo de montagem.
Relatórios de lucratividade por romaneio.
Relatórios de embarque de veículo e outros indicadores financeiros/operacionais ligados à roteirização.
XML / Excel
Importação de XML de notas.
Importação de informações via Excel.
Cancelamento de pedidos via rotina específica.
Mapas
Visualização de clientes em mapa.
Possibilidade de usar mapa de calor para analisar concentração de clientes/pedidos.
Configurações
Parametrização de perfis de acesso e usuários.
Configurações de geração de coordenadas/geocodificação.
Outras parametrizações gerais do módulo (comportamento, integrações, etc.).
## 2 do Analista de Suporte e Escopo deste Documento
2.1. Papel do Analista de Suporte
O analista de suporte é o responsável por investigar, interpretar e orientar os clientes que utilizam os módulos maxMotorista e maxRoteirizador do sistema de logística.
Seu foco não é apenas “resolver tela”, mas entender o processo logístico por trás do problema e identificar se a causa está em:
### uso incorreto da funcionalidade;
parametrização inadequada;
dados faltantes ou inconsistentes;
falha de integração;
erro sistêmico (bug) ou limitação do produto.
As principais atividades do analista de suporte são:
Ler, entender e classificar o chamado do cliente.
Fazer perguntas complementares para obter todas as informações necessárias (datas, filtros, número de romaneio, CNPJ, motorista, filial, etc.).
Utilizar este documento para:
### identificar quais telas e funcionalidades estão envolvidas;
identificar quais tabelas e relações de banco de dados precisam ser analisadas;
selecionar os SELECTs de diagnóstico mais adequados.
Validar se o comportamento relatado está de acordo com:
as regras de negócio do sistema;
as parametrizações do cliente;
os dados disponíveis na base.
Registrar claramente o que foi feito, o que foi encontrado e qual orientação será repassada ao cliente.
Quando necessário, escalar o chamado para times superiores (desenvolvimento, infraestrutura) com todas as evidências já coletadas.
2.2. O que o Analista Faz e o que Não Faz
O analista de suporte FAZ:
Analisa o chamado com foco em processo logístico + funcionalidade.
Consulta logs, tabelas e relatórios internos para confirmar as informações do cliente.
Usa SELECTs de leitura para entendimento de dados (sem alterar registros).
Verifica parametrizações, permissões e filtros configurados.
Explica ao cliente o motivo do comportamento do sistema e orienta sobre o uso correto.
Encaminha para desenvolvimento apenas quando há forte evidência de bug ou necessidade de melhoria.
O analista de suporte NÃO FAZ:
Não altera diretamente dados sensíveis em produção, salvo procedimentos oficiais e autorizados.
Não desenvolve novas funcionalidades ou customizações específicas.
Não assume tarefas do time de infraestrutura (servidor, rede, banco fora do escopo de aplicação).
Não executa scripts de correção sem procedimento aprovado e documentado.
2.3. Escopo deste Documento
Este documento foi criado para ser um guia de diagnóstico técnico para o suporte, com foco em:
Relacionar menus, telas e módulos (maxMotorista e maxRoteirizador) com as tabelas e integrações envolvidas.
Detalhar conceitos de negócio relevantes (romaneio, jornada, entrega, roteirização, frete, etc.).
Fornecer modelos de SELECTs que auxiliem a análise de tickets.
Orientar quais perguntas devem ser feitas ao cliente em cada tipo de situação.
Sugerir fluxos de análise (playbooks) para os problemas mais comuns.
O documento não é:
um manual de treinamento de usuários finais;
um guia completo de operação de toda a logística do cliente;
uma documentação técnica de desenvolvimento (código-fonte, arquitetura interna detalhada).
Ele é voltado especificamente para:
Analistas de suporte internos, que atendem empresas usuárias do sistema;
IA de apoio ao suporte, que utilizará este conteúdo para sugerir caminhos de análise, perguntas e SELECTs.
2.4. Tipos de Problemas e Como Enxergá-los
Para padronizar a análise, todos os tickets devem ser vistos dentro de uma das categorias abaixo (ou combinação delas):
Problema de uso / operação
Ex.: filtro de data incorreto, filial errada selecionada, relatório usado de forma equivocado.
Normalmente se resolve com orientação ao cliente e demonstração da forma correta de uso.
Problema de parametrização
Ex.: status configurado como “não visível”, raio de entrega ajustado de forma muito restrita, permissão de acesso faltando.
Envolve análise em tabelas de parâmetros e telas de configurações.
Problema de dados
Ex.: pedido sem centro de distribuição, endereço incompleto, motivo de ocorrência não cadastrado.
Envolve análise de cadastros, integrações e consistência dos dados gravados nas tabelas.
Problema de integração
Ex.: pedido não chegou para roteirização, XML não importou, falha na integração com ERP.
Envolve tabelas de fila, logs de integração e comparação entre o que está no ERP e o que chegou ao sistema.
Problema sistêmico (bug)
Comportamento divergente da regra de negócio prevista, sem justificativa por uso, parâmetro ou dados.
Após análise cuidadosa, deve ser escalado ao desenvolvimento, com evidências (prints, SELECTs, passos para reproduzir).
2.5. Como Utilizar este Documento no Dia a Dia
Ao receber um chamado, o analista deve:
Identificar o módulo e o menu envolvido
### maxMotorista ou maxRoteirizador?
Dashboard, Relatório, Consulta, Roteirização, Mapa, Configurações, etc.
Localizar a seção correspondente neste documento
Capítulos que tratam de:
Conceito de negócio
### Funcionalidade
Tabelas relacionadas
Playbooks de análise
Aplicar o checklist de perguntas ao cliente
Sempre colher: datas, CNPJ, número de pedido/romaneio/nota, motorista, filial, filtros utilizados.
Executar os SELECTs sugeridos
Usando os modelos deste documento como base.
Adaptando apenas os filtros (por exemplo, :numeroRomaneio, :idCliente, :dataInicial, :dataFinal).
Classificar o tipo de problema (uso, parâmetro, dados, integração, bug)
Com base nos resultados obtidos e nas regras de negócio descritas.
Registrar o diagnóstico e a orientação
Descrever claramente:
O que foi analisado;
O que foi encontrado nas tabelas;
Qual a causa provável do problema;
Qual a orientação dada ao cliente ou qual a necessidade de escalonamento.
2.6. Quando Escalar o Chamado
O analista deve considerar o escalonamento quando:
Todos os checks de uso, parâmetros e dados forem realizados, sem explicação para o comportamento.
O SELECT mostrar dados corretos, mas a tela não refletir essas informações, sem justificativa conhecida.
Houver indício de erro de cálculo, regra de negócio quebrada ou inconsistência entre módulos.
O problema afetar mais de um cliente de forma semelhante (potencial falha geral).
Ao escalar:
Registrar de forma objetiva:
Descrição do problema.
Passos para reproduzir.
Prints de tela relevantes.
SELECTs executados e resultados encontrados.
Conclusão preliminar do suporte (hipótese).
## 3 Funcional e Fluxo de Dados
### 3.1 macro do fluxo:
#### 3.1.1
No maxMotorista, o fluxo começa após o faturamento das entregas no ERP do cliente:
Quando há integração (por exemplo, com o WinThor, rotina 1402, ou outros ERPs), assim que o pedido é faturado ele entra na fila para ser integrado à Máxima.
Existe um job de entregas que roda em janelas de 30 em 30 minutos.
Esse job aciona três procedures, responsáveis por alimentar as tabelas utilizadas pelo maxMotorista:
### Tabela de entregas
Tabela de notas fiscais
### Tabela de itens de nota/entrega
### Após a execução dessas procedures, as entregas passam a ficar:
Disponíveis para visualização no painel gerencial (maxMotorista Web), onde o supervisor acompanha as entregas;
Disponíveis para o aplicativo do motorista, assim que o motorista sincronizar.

No maxMotorista Web, o foco principal é o acompanhamento da operação, permitindo ao gestor/supervisor:
### Ver onde o motorista está;
Acompanhar o que já foi entregue, o que está em trânsito e o que está pendente;
Identificar devoluções, check-in fora do raio, retornos de viagem e nível de serviço.

### No aplicativo do motorista, o fluxo é centrado na execução da rota:
Recebimento e início do romaneio
O motorista recebe o romaneio com as entregas vinculadas.
Ao iniciar o romaneio, conforme parametrização, pode ser solicitado o registro do hodômetro do veículo.
### Visão das entregas
O motorista visualiza todas as entregas que precisa realizar, na sequência definida:
Se a carga foi roteirizada pela Máxima → segue a sequência do maxRoteirizador.
Se não foi roteirizada pela Máxima → segue a sequência definida pelo ERP.
Para confirmar se a carga foi roteirizada pela Máxima, basta consultar o maxRoteirizador, na tela de Consulta de Carregamentos.
### Execução da entrega e furo de sequência
O motorista pode seguir a sequência sugerida ou furar a sequência.
Em caso de furo, ele deve informar um motivo de furo de sequência, previamente cadastrado pelo cliente (regra de negócio do cliente).
Check-in e descarga
### Ao chegar no cliente, o motorista:
Inicia o check-in, que pode ser com ou sem foto, conforme parametrização.
Em seguida, inicia a descarga da entrega.
Na tela de descarga são listados os itens da nota daquele cliente:
Pode marcar itens como entregues, devolução parcial ou devolução total;
Pode bipar produtos;
Pode tirar foto da entrega in loco como comprovação.
### Comprovação da entrega
### O motorista pode:
Coletar a assinatura digital do cliente;
Tirar fotos adicionais;
Tirar a foto do canhoto assinado, que funciona como comprovante fiscal da entrega.
Após isso, ele finaliza a entrega e segue para a próxima.
Navegação
Em cada card de entrega, há opção de abrir a navegação (Waze, Google Maps etc.) para ir até o próximo cliente.
Finalização do romaneio e jornada
Ao concluir todas as entregas do dia, o motorista pode finalizar o romaneio.
Se o cliente utiliza jornada de trabalho, o motorista também registra o fim da jornada, encerrando oficialmente o expediente no sistema.
#### 3.1.2
O maxRoteirizador é o módulo responsável pela montagem de carga e roteirização dos pedidos no mapa.
Ao acessar a aba de Roteirização, o usuário visualiza o mapa com as filiais já plotadas e uma área de filtros. Esses filtros podem ser aplicados conforme a regra de negócio do cliente, permitindo filtrar por:
Filiais
Rotas
Praças
Cidades
Regiões
Clientes
### Pedidos
Valores
### Posições do pedido
Todas essas informações são recebidas via integração:
Quando utiliza o Intorn, a rotina padrão utilizada para montagem de carga é a 901.
Quando utiliza outros ERPs, os dados chegam pelas tabelas de integração.
Quando utiliza importação de XML, as informações vêm pela rotina de importação de XML da nota fiscal.
Importante: nenhum pedido é criado diretamente na tela de roteirização. Tudo que aparece nos filtros e no mapa é baseado no que o cliente envia pela integração. Caso algum filtro não funcione como esperado, é provável que o cliente não utilize aquela funcionalidade ou não tenha o envio daquele dado parametrizado/ativado no portal.
A montagem de carga é exclusiva para pedidos liberados e faturados, porém o sistema permite visualizar pedidos pendentes ou bloqueados, para que o usuário possa tratá-los e agilizar a liberação para montagem.
### Após aplicar os filtros, o sistema lista os pedidos no mapa, exibindo:
Um pin para cada cliente;
Uma numeração indicando a quantidade de pedidos daquele cliente.
Assim, o usuário tem uma visão geral de todos os clientes com pedidos disponíveis para montagem de carga.
Existem duas formas principais de montar carga no mapa:
Agrupamento automático, que pode ser feito por:
Cidade
Praça
### RCA
Região
Rota
Transportadora
Área de atendimento
Nesse caso, o sistema agrupa os clientes mostrados no mapa com base no critério selecionado.
Desenho de área no mapa, utilizando formas:
Círculo
Quadrado
Retângulo
Polígono
O usuário desenha a região desejada no mapa e, ao finalizar, é exibido um menu lateral com opções como:
Adicionar nova carga
### Transferir pedidos
Visualizar detalhes do cliente
No canto inferior esquerdo, o sistema apresenta um resumo dos pedidos selecionados, incluindo:
Peso total
Volume
### Quantidade de pedidos
Valor total
Ao escolher adicionar nova carga, o usuário preenche as informações do carregamento, como:
Destino
Veículo
### Motorista
Centro de distribuição
Horários
Perfil de roteirização
Tabela de frete
Outros campos obrigatórios e complementares, conforme a operação do cliente
Após o preenchimento, o usuário grava a carga e o sistema roteiriza automaticamente com base no perfil de roteirização selecionado. Em seguida, é apresentada uma tela com:
### Listagem de pedidos da rota
Caminho sugerido: do centro de distribuição, passando pelos clientes, até o retorno
### Horário de saída do CD, primeira entrega, última entrega e retorno
Custo de frete, percentuais e cálculos relacionados à tabela de frete
Nessa tela, o usuário pode ainda:
### Alterar a sequência de entrega
### Remover pedidos da rota
Reprocessar ou recalcular a rota após ajustes
Criar pontos de parada (ex.: abastecimento)
Criar pontos de passagem (para forçar o trajeto a passar por determinado local)
Ao final do processo de roteirização, a carga fica pronta para salvamento, que pode ser feito de quatro formas:
Salvar carregamento normal
Salva o carregamento como um único registro.
Salvar carregamento com quebra por filial
Separa o carregamento por filial e agrupa em um único romaneio.
Salvar carregamento com quebra por lote
Loteia o veículo, salvando múltiplos carregamentos conforme os lotes configurados, todos amarrados a um único romaneio.
Essa quebra não impacta a visão do motorista ou do cliente.
### Salvar carregamento com quebra de reentrega
Utilizado quando o cliente não possui o ERP Intorn e precisa que o carregamento de reentrega seja diferente do carregamento normal.
Gera dois carregamentos (normal e reentrega), ambos vinculados a um único romaneio.
Essa visão macro resume o ciclo completo dentro do maxRoteirizador: receber pedidos da integração, filtrar, visualizar no mapa, montar cargas, roteirizar e salvar o carregamento conforme a necessidade operacional do cliente.
### 3.2 INTEGRAÇÕES
Perfeito, vou reescrever esse tópico como texto de documentação, organizado e fácil de usar no futuro.

3.2. Principais Integrações
Este tópico descreve, em visão macro, as principais integrações que alimentam o ambiente logístico (maxRoteirizador e maxMotorista) e como elas se relacionam com outros produtos da Máxima e com ERPs de terceiros.

#### 3.2.1 nativa com Intor
A principal integração utilizada hoje é com o Intor, de forma nativa.
Arquitetura geral
Quando o cliente está em ambiente on-premise, o Intor possui um banco de dados local.
Dentro desse banco, o cliente possui um schema específico da Max Soluções, que é o “banco da Máxima” dentro do ambiente Intor.
O Intor grava os dados no seu banco “sistema” e, a partir disso, os dados são replicados para o schema da Máxima, nas tabelas necessárias.
Esses dados são então enviados para o banco em nuvem da Máxima, que é onde ficam as informações de logística e demais produtos.
Ambiente em nuvem (Intor em nuvem)
Quando o cliente utiliza o Intor em nuvem, a lógica é semelhante, porém o banco já está hospedado em ambiente cloud, com o schema da Máxima dentro do próprio banco do Intor.
Extrator
A integração entre o banco do cliente (Intor) e o ambiente nuvem da Máxima é feita por um extrator.
A manutenção desse extrator é responsabilidade do time de desenvolvimento do MaxPedido.
Quando houver tickets relacionados ao extrator:
O suporte logístico deve analisar o sintoma e identificar se se trata de falha de integração/extrator.
Confirmando que é um problema de extrator, o ticket deve ser direcionado para o time de desenvolvimento do MaxPedido, e não para o time de logística.
Localização do extrator e dados de conexão
O extrator fica em um Portainer, dentro do portal da Max Soluções.
É possível consultar os dados de conexão do cliente acessando:
Max Soluções → Extratores → buscar pelo cliente
Nessa tela, estarão informações como:
IP do cliente/servidor
Porta utilizada (por padrão, geralmente 9000 e 9002)
Para acesso:
Portainer: utilizar o IP + porta configurada.
Ringfire (para análise/atualização de banco, quando aplicável): acessar usando o IP + porta do Ringfire + /ringfire.

#### 3.2.2 entre Logística e outros produtos Máxima
Além da integração com ERPs, o módulo de logística se integra com outros produtos da própria Máxima:
### Integração com MaxPedido
O MaxPedido consome dados do módulo de logística (principalmente maxMotorista) para exibir, para o vendedor:
### Situação da entrega;
### Se o motorista já saiu para a rota;
### Se a entrega foi realizada;
Se houve devolução.
Esses dados são consultados diretamente das tabelas de entrega do MaxMotorista.
Integração com TimeHawk
O TimeHawk é um portal de acompanhamento de entregas.
O cliente final pode consultar o andamento das suas notas fiscais por:
Código de rastreio;
### CNPJ;
Ou outros identificadores previstos.
As informações exibidas no TimeHawk são extraídas diretamente dos dados de entrega do MaxMotorista.
Integração com TMS de Armazém
Existe uma integração recente com um produto TMS da própria Máxima, voltado para gestão de armazém e veículos.
Esse TMS troca informações com o módulo de logística para complementar o fluxo de carga, armazenagem e transporte.
Integração com rastreador de veículos
O sistema já possui alguns rastreadores de veículos homologados e mapeados.
Quando o cliente deseja integrar um rastreadores novo/não homologado, é necessário:
Abrir um ticket com o layout de integração desse rastreador;
Esse layout é analisado e encaminhado como demanda de melhoria para o time responsável, para inclusão do novo rastreador.
Integração com Sem Parar
Integração para mapeamento dos gastos de pedágio do motorista.
Permite relacionar os eventos de pedágio com as viagens/cargas realizadas.
Integração com MaxPag
O MaxPag é um serviço de pagamentos (Pix, cartão de crédito, débito).
### O MaxMotorista pode integrar com o MaxPag para:
Disponibilizar links de pagamento para o cliente final;
Permitir, quando parametrizado, a baixa automática do título/recebível após a confirmação do pagamento.
A lógica de exibição do link e baixa automática depende de parametrização no ambiente do cliente.

#### 3.2.3 com clientes e outros ERPs (não Intor)
Para clientes que utilizam outros ERPs ou integrações próprias, o modelo é diferente da integração nativa com Intor:
A integração é passiva do lado da Máxima:
A Máxima fornece um layout de integração, especificando:
Tabelas e estruturas que devem ser alimentadas;
Campos obrigatórios para cada tipo de dado (pedidos, clientes, produtos, etc.).
O próprio cliente (via TI interno ou via ERP) é responsável por:
Enviar os dados à Máxima;
Consumir os dados da Máxima, quando houver retorno previsto.
Responsabilidade
A Máxima não executa o processo de integração nesses casos; apenas:
Disponibiliza o layout;
Recebe os dados nas estruturas padrão;
Disponibiliza as informações para consumo.
Se houver problema na integração, o analista de suporte:
Verifica se os dados estão chegando no formato e tabelas corretas;
Orienta o cliente com base no layout;
Quando for problema no lado do cliente/ERP, a correção deve ser feita pela equipe de TI do cliente.
Layout de integração
O layout com:
Nome das tabelas;
Campos obrigatórios;
Tipos de dados e regras básicas;
Já está disponível neste documento (em seções específicas) e pode ser consultado sempre que:
O cliente tiver dúvidas;
For necessário validar se a integração está enviando algo fora do padrão.

---

## Playbooks de atendimento

## 1 Playbooks de Atendimento (Guias de Diagnóstico)
Este capítulo reúne roteiros práticos de atendimento para os principais tipos de problemas reportados pelos clientes nos módulos maxRoteirizador e maxMotorista.
O objetivo é padronizar a atuação do analista de suporte, evitando “tentativa e erro” e garantindo que todos sigam uma linha de raciocínio consistente, baseada nas integrações, tabelas e parametrizações descritas nos capítulos anteriores.
Cada playbook está estruturado em:
Sintoma – como o problema normalmente é descrito pelo cliente;
Perguntas iniciais para o cliente – o que o analista deve perguntar logo no começo para enquadrar o cenário;
Passos de análise – sequência sugerida de verificações, com referências aos capítulos de integrações, tabelas e parametrizações;
SELECTs recomendados – consultas de banco de dados que ajudam a confirmar se o problema está em dados, integração, parametrização ou uso;
Quando escalar para desenvolvimento – critérios objetivos para decidir quando o caso deixa de ser suporte de primeiro/segundo nível e passa a ser analisado pelo time de produto/DEV.
Na prática, este capítulo funciona como um manual de diagnóstico rápido:
diante de um problema (“registro não aparece”, “pedido não entrou na rota”, “status divergente”), o analista localiza o playbook correspondente e segue os passos sugeridos até identificar a causa raiz ou justificar a necessidade de escalonamento.

### MaxMotorista

#### Status da entrega não atualiza no portal
Sintoma
Cliente diz que o motorista entregou, reagendou ou colocou em fila de espera, mas o status no portal continua antigo.
O que pedir ao cliente
Número da nota.
Número do carregamento.
Nome do motorista.
Horário em que ele executou a ação no app.
Print da tela do app, se possível.
Passo a passo
Confirmar o status atual em MXMP_ENTREGAS.
Verificar o histórico da entrega em MXMP_HISTORICO_ENTREGAS.
Verificar se houve log de mudança em MXMP_LOG_SITUACAO_ENTREGA_NOTA.
Confirmar se o motorista sincronizou.
Se necessário, comparar com a base local MXMD_ENTREGAS, que contém SITUACAO, SITUACAO_ORIG, DATA_CHECKIN, DATA_INICIO_DESCARGA, DATA_TERMINO_DESCARGA e campos de sincronização.
SELECTs
```sql
SELECT *
FROM MXMP_ENTREGAS
WHERE ID = :ID_ENTREGA;
SELECT *
FROM MXMP_HISTORICO_ENTREGAS
WHERE ID_ENTREGA = :ID_ENTREGA
ORDER BY DATA DESC;
SELECT *
FROM MXMP_LOG_SITUACAO_ENTREGA_NOTA
WHERE ID_REGISTRO = :ID_ENTREGA
ORDER BY DATA_E_HORA DESC;
SELECT *
FROM MXMP_CONTROLE_SINC_MOTORISTA
WHERE ID_MOTORISTA = :ID_MOTORISTA
ORDER BY DATA DESC;
```

Como interpretar
Se MXMP_ENTREGAS não mudou e não existe histórico, o app provavelmente não sincronizou.
Se existe histórico mas a tela ainda não reflete, verificar filtros da tela ou atraso de atualização.
Se na base local MXMD_ENTREGAS já existe a ação, mas no portal não, a falha está na sincronização do app para a nuvem. As tabelas locais têm campos próprios de sincronização e status.
Quando escalar
Se a sincronização foi concluída, há dados no app, mas o portal não atualiza.
Se houver erro recorrente em MXMP_FALHA_SINCRONIZACAO.

#### Ocorrência / devolução / reagendamento não aparece no portal
Sintoma
Motorista registrou ocorrência, devolução, descarga cancelada ou reagendamento, mas o suporte não vê no maxMotorista web.
O que pedir ao cliente
Tipo da ocorrência.
Nota / entrega afetada.
Motorista.
Horário da ação.
Motivo escolhido no app.
Passo a passo
Verificar MXMP_OCORRENCIAS.
Verificar MXMP_HISTORICO_OCORRENCIA.
Se for devolução, verificar MXMP_DEVOLUCOES.
Se for cancelamento/reagendamento, verificar MXMP_DESCARGA_CANCELADA e MXMP_DESCARGA_REAGENDADA.
Confirmar se o motivo usado existe e está ativo em MXMP_MOTIVO_OCORRENCIA, MXMP_MOTIVO_REAGENDAMENTO, MXMP_MOTIVO_CANCELAMENTO, MXMP_MOTIVO_FURO_SEQUENCIA.
Se necessário, comparar com as tabelas locais MXMD_OCORRENCIAS, MXMD_HISTORICO_OCORRENCIA, MXMD_DESCARGA_CANCELADA e MXMD_DESCARGA_REAGENDADA. Essas tabelas possuem campos como ENVIADO e SITUACAO_SINCRONIZACAO, que ajudam a saber se o app já tentou sincronizar.
SELECTs
```sql
SELECT *
FROM MXMP_OCORRENCIAS
WHERE ID_REGISTRO = :ID_REGISTRO
ORDER BY DATA_OCORRENCIA DESC;
SELECT *
FROM MXMP_HISTORICO_OCORRENCIA
WHERE ID_OCORRENCIA = :ID_OCORRENCIA
ORDER BY DATA_UTC DESC;
SELECT *
FROM MXMP_DESCARGA_REAGENDADA
WHERE ID_ENTREGA = :ID_ENTREGA;
SELECT *
FROM MXMP_DESCARGA_CANCELADA
WHERE ID_ENTREGA = :ID_ENTREGA;
SELECT *
FROM MXMP_MOTIVO_OCORRENCIA
WHERE ID = :ID_MOTIVO;
```

Como interpretar
Se o motivo não existir ou estiver inadequado, o usuário pode ter conseguido gravar localmente mas a regra de portal não refletir corretamente.
Se na base local existe ocorrência com flag de envio pendente, a falha é de sincronização do app.
A documentação do mapa funcional já indica essas tabelas como núcleo das ocorrências no maxMotorista.
Quando escalar
Se a ocorrência existe na base local e nunca sobe.
Se a ocorrência sobe, mas a tela do portal não reflete mesmo com dados corretos em MXMP_*.

#### Despesa lançada no app não aparece no portal
Sintoma
Motorista lançou abastecimento, pedágio, infração ou outra despesa, mas o portal não mostra.
O que pedir ao cliente
Tipo de despesa.
Valor.
Data/hora.
Motorista.
Carregamento / romaneio.
Passo a passo
Verificar MXMP_DESPESAS.
Se for abastecimento, verificar MXMP_DESPESA_ABASTECIMENTO.
Se for infração, verificar MXMP_DESPESA_INFRACAO.
Confirmar o tipo em MXMP_TIPO_DESPESA.
Confirmar sincronização do motorista.
Se necessário, comparar com MXMD_DESPESAS, que possui VALOR, OBSERVACAO, DATA, ID_USUARIO e SITUACAO_SINCRONIZACAO.
SELECTs
```sql
SELECT *
FROM MXMP_DESPESAS
WHERE ID_USUARIO = :ID_USUARIO
 AND DATA BETWEEN :DT_INI AND :DT_FIM
ORDER BY DATA DESC;
SELECT *
FROM MXMP_DESPESA_ABASTECIMENTO
WHERE ID_DESPESA = :ID_DESPESA;
SELECT *
FROM MXMP_DESPESA_INFRACAO
WHERE ID_DESPESA = :ID_DESPESA;
SELECT *
FROM MXMP_CONTROLE_SINC_MOTORISTA
WHERE ID_MOTORISTA = :ID_MOTORISTA
ORDER BY DATA DESC;
```

Como interpretar
Se existe em MXMD_DESPESAS com sincronização pendente, ainda não subiu do app.
Se existe em MXMP_DESPESAS mas não aparece no portal, revisar filtros por motorista, data, filial e situação.
O mapa funcional do maxMotorista já aponta MXMP_DESPESAS e MXMP_CONTROLE_SINC_MOTORISTA como base dessa análise.
Quando escalar
Se a despesa está em MXMP_DESPESAS e a tela não mostra.
Se há falha recorrente de sincronização do mesmo tipo de despesa.

#### Hodômetro não aparece / não sincroniza
Sintoma
Motorista registrou hodômetro, mas o portal não mostra ou mostra incompleto.
O que pedir ao cliente
Motorista.
Placa.
Data/hora do lançamento.
Se foi início ou fim de jornada/romaneio.
Se foi tirada foto do hodômetro.
Passo a passo
Verificar MXMP_HODOMETROS.
Conferir vínculo com romaneio, usuário e placa.
Verificar se a jornada existe.
Confirmar se o parâmetro de uso de hodômetro está habilitado e se há exigência de foto, placa e captura obrigatória, já que esses parâmetros afetam o comportamento do app. A documentação de parâmetros menciona “Habilitar o uso de hodômetro”, “Exigir foto de hodômetro”, “Exigir placa de veículo”, “Definir quantidade máxima de hodômetros por dia” e “Definir horário de captura obrigatória”.
Se necessário, comparar com MXMD_HODOMETROS, que contém KM, DATA_CADASTRO, PLACA, IMAGEM, SITUACAO_SINCRONIZACAO, TIPO_HODOMETRO e ID_ROMANEIO.
SELECTs
```sql
SELECT *
FROM MXMP_HODOMETROS
WHERE ID_USUARIO = :ID_USUARIO
 AND DATA_CADASTRO BETWEEN :DT_INI AND :DT_FIM
ORDER BY DATA_CADASTRO DESC;
SELECT *
FROM MXMP_LANCAMENTOS_JORNADA
WHERE ID_USUARIO = :ID_USUARIO
 AND INICIO_JORNADA BETWEEN :DT_INI AND :DT_FIM
ORDER BY INICIO_JORNADA DESC;
SELECT *
FROM MXMP_LOG_HODOMETROS_ALTERACAO
WHERE ID_USUARIO_NOVO = :ID_USUARIO
ORDER BY DATA_ALTERACAO DESC;
```

Como interpretar
Se está na base local e não está na MXMP, a falha é de sincronização.
Se está na MXMP, mas sem vínculo correto com placa/romaneio/usuário, o problema pode ser regra de lançamento ou edição posterior.
O próprio mapeamento que você montou já orienta a revisar jornada, sincronização e vínculo do veículo.
Quando escalar
Se há dado válido no app e ele nunca sobe.
Se o registro é alterado/perdido após sincronização.

#### Recebível não aparece ou não baixa no maxMotorista / MaxPag
Sintoma
Recebível não aparece no app ou no portal, ou o pagamento foi feito e a baixa não aconteceu.
O que pedir ao cliente
Número da nota.
Número da transvenda.
Forma de pagamento.
Se o link do MaxPag foi gerado.
Se o pagamento já está confirmado.
Passo a passo
Verificar se o título/recebível existe em MXMP_RECEBIVEIS.
Se usar MaxPag, verificar MXMP_MAXPAG_LINK, MXMP_MAXPAG_MOV e MXMP_LOG_BAIXA_TITULO_SINC.
Confirmar se a solução MaxPag está habilitada no app; a documentação de parâmetros do maxMotorista diz que o uso do MaxPag depende de habilitação específica no aplicativo.
Confirmar sincronização do motorista, porque a visualização do recebível também depende do app sincronizar.
SELECTs
```sql
SELECT *
FROM MXMP_RECEBIVEIS
WHERE NUMTRANSVENDA = :NUMTRANSVENDA;
SELECT *
FROM MXMP_MAXPAG_LINK
WHERE NUMTRANSVENDA = :NUMTRANSVENDA
 OR NUMNOTA = :NUMNOTA;
SELECT *
FROM MXMP_MAXPAG_MOV
WHERE NUMTRANSVENDA = :NUMTRANSVENDA
ORDER BY DATA DESC;
SELECT *
FROM MXMP_LOG_BAIXA_TITULO_SINC
WHERE NUMTRANSVENDA_ACEITO LIKE '%' || :NUMTRANSVENDA || '%'
 OR NUMTRANSVENDA_RECUSADO LIKE '%' || :NUMTRANSVENDA || '%'
ORDER BY DATA DESC;
```

Como interpretar
Se não existe MXMP_MAXPAG_LINK, o link nem foi gerado.
Se existe link, mas não existe movimento, o pagamento não retornou para a Máxima.
Se existe movimento e a baixa não aconteceu, olhar MXMP_LOG_BAIXA_TITULO_SINC.
O catálogo de tabelas mostra MXMP_MAXPAG_LINK, MXMP_MAXPAG_MOV e MXMP_LOG_BAIXA_TITULO_SINC como peças centrais do fluxo financeiro.
Quando escalar
Se o MaxPag confirmou pagamento e a baixa nunca chega.
Se o link foi gerado, o movimento retornou, mas o título continua sem baixa.

#### Motorista não aparece no mapa / monitoramento
Sintoma
Cliente diz que o motorista está trabalhando, mas não aparece no painel de monitoramento ou no mapa.
O que pedir ao cliente
Nome do motorista.
Carregamento atual.
Último horário em que ele abriu o app.
Se o GPS do dispositivo está ativo.
Se a bateria/rede estão ok.
Passo a passo
Verificar se o carregamento está de fato vinculado ao motorista.
Verificar MXMP_LOCALIZACAO_MOTORISTA.
Verificar se há entregas em andamento para ele.
Verificar se o usuário responsável está corretamente vinculado.
Validar sincronização e dados do aparelho em MXMP_APARELHOS, que armazena última sincronização, GPS ligado, status de rede e localização do dispositivo.
Se necessário, olhar MXMD_LOCALIZACAO na base local do app.
SELECTs
```sql
SELECT *
FROM MXMP_LOCALIZACAO_MOTORISTA
WHERE ID_MOTORISTA = :ID_MOTORISTA
ORDER BY DATA DESC;
SELECT *
FROM MXMP_ENTREGAS
WHERE ID_USUARIO = :ID_USUARIO
ORDER BY DATA_GERACAO DESC;
SELECT *
FROM MXMP_APARELHOS
WHERE ID_USUARIO = :ID_USUARIO
ORDER BY DATA_ULTIMA_SINCRONIZACAO DESC;
```

Como interpretar
Se não existe MXMP_LOCALIZACAO_MOTORISTA, o app não está enviando posição.
Se o aparelho mostra GPS desligado/rede ruim, a causa pode ser operacional do dispositivo.
O teu mapa funcional já aponta MXMP_LOCALIZACAO_MOTORISTA, MXMP_ENTREGAS e log de sincronização como base dessa análise.
Quando escalar
Se o aparelho sincroniza normalmente, mas a localização nunca é gravada.
Se há inconsistência entre usuário, motorista e aparelho.

#### Entrega fora do raio / check-in fora do raio
Sintoma
Motorista não consegue iniciar check-in ou precisa de autorização para concluir a entrega porque está fora do raio.
O que pedir ao cliente
Nota / entrega.
Cliente.
Distância aproximada do local.
Se a autorização foi solicitada.
Se o problema aconteceu com um cliente específico ou vários.
Passo a passo
Verificar MXMP_ENTREGAS e coordenadas do cliente/endereço.
Verificar MXMP_LOCALIZACAO_CLIENTE e MXMP_LOCALIZACAO_END_ENTREGA.
Verificar parâmetros de restrição/raio.
Validar no app se o registro local marcou CHECKIN_FORA_RAIO / CHECKOUT_FORA_RAIO. A tabela local MXMD_ENTREGAS possui esses campos.
Conferir parâmetros do app: “Definir raio de distância máxima no check-in”, “Exigir autorização de check-in fora do raio” e “Permitir Realizar Checkin sem Coordenadas”.
SELECTs
```sql
SELECT *
FROM MXMP_ENTREGAS
WHERE ID = :ID_ENTREGA;
SELECT *
FROM MXMP_LOCALIZACAO_CLIENTE
WHERE ID_CLIENTE = :ID_CLIENTE;
SELECT *
FROM MXMP_LOCALIZACAO_END_ENTREGA
WHERE CODCLI = :ID_CLIENTE
 AND ID_ENDERECO_ENTREGA = :ID_ENDERECO;
SELECT *
FROM MXMP_PARAMETROS_RESTRICAO;
```

Como interpretar
Se o cliente/endereço está sem coordenadas, o app pode bloquear ou exigir exceção.
Se o parâmetro de autorização estiver ativo, a autorização é comportamento esperado.
Se o parâmetro de permitir check-in sem coordenadas estiver desativado, isso também explica o bloqueio.
Quando escalar
Se as coordenadas estão corretas, o raio está coerente e ainda assim o cálculo se comporta errado.
Se a autorização é liberada, mas o app continua bloqueando.

#### Jornada não inicia / não finaliza / não aparece nos relatórios
Sintoma
Motorista não consegue bater jornada, ou a jornada não aparece nos relatórios / portal.
O que pedir ao cliente
Motorista.
Data.
Se a jornada é obrigatória nesse ambiente.
Se tentou iniciar refeição/finalizar refeição/fim de jornada.
Se o app pediu GPS.
Passo a passo
Verificar MXMP_JORNADAS e MXMP_HORARIOS_TRABALHO.
Verificar MXMP_LANCAMENTOS_JORNADA.
Verificar MXMP_DESCANSO_JORNADA, MXMP_AUSENCIA e MXMP_LOG_REGISTRO_JORNADA.
Conferir parâmetros do app relacionados a jornada: “Obriga Batida de Horário Refeição” e “Obrigar GPS no registro de Jornada”.
Se necessário, comparar com a base local MXMD_LANCAMENTOS_JORNADA e MXMD_DESCANSO_JORNADA. Essas tabelas têm campos de início/fim e sincronização local.
SELECTs
```sql
SELECT *
FROM MXMP_JORNADAS;
SELECT *
FROM MXMP_HORARIOS_TRABALHO;
SELECT *
FROM MXMP_LANCAMENTOS_JORNADA
WHERE ID_USUARIO = :ID_USUARIO
 AND INICIO_JORNADA BETWEEN :DT_INI AND :DT_FIM
ORDER BY INICIO_JORNADA DESC;
SELECT *
FROM MXMP_LOG_REGISTRO_JORNADA
WHERE ID_USUARIO = :ID_USUARIO
ORDER BY DATA_DA_ALTERACAO DESC;
```

Como interpretar
Se não existe jornada configurada, o problema é de cadastro.
Se existe jornada e o app não deixa bater, revisar parâmetros de GPS e refeição.
Se a jornada está no app local e não sobe, revisar sincronização.
Quando escalar
Se a regra está toda correta e o app continua bloqueando indevidamente.
Se há divergência entre lançamento gravado e horário exibido no portal.

#### Foto / canhoto / assinatura / XML não aparece ou não envia
Sintoma
Cliente informa que a foto de check-in, assinatura, canhoto, foto de entrega ou envio do XML por e-mail não está funcionando.
O que pedir ao cliente
Tipo do problema: foto, assinatura, canhoto ou XML.
Nota.
Motorista.
Se o erro ocorre em todas as entregas ou apenas em algumas.
Se o motorista estava online/Wi-Fi ou rede móvel.
Passo a passo
Verificar em MXMP_NOTAS_FISCAIS os campos de foto, observação de canhoto, motivo e status do canhoto.
Verificar em MXMP_ENTREGAS os campos de foto de check-in, foto de assinatura digital, foto de transbordo e foto de entrega.
Verificar MXMP_FOTOS e MXMP_ARQUIVOS.
Verificar MXMP_CONFIGURACAO_EMAIL e MXMP_CONTROLE_EMAIL_ENTREGA para problemas de envio de XML/canhoto por e-mail.
Conferir os parâmetros do app: “Exigir foto no check-in”, “Exigir foto de assinatura”, “Foto em caso de avaria”, “Exigir foto em caso de devolução”, “Sincronizar fotos somente via WiFi”, “Habilitar reenvio de XML para contato do ERP”, “Habilitar o validador da NF-E” e “Tipo de validação do canhoto da NF-E”.
Se necessário, analisar a base local MXMD_FOTOS, MXMD_NOTAS_FISCAIS e MXMD_ENTREGAS. Essas tabelas guardam blobs, hashes, flags de sincronização e informações de foto/assinatura/canhoto no dispositivo.
SELECTs
```sql
SELECT *
FROM MXMP_NOTAS_FISCAIS
WHERE NUMERO_NOTA = :NUMNOTA
 AND NUMERO_TRANSVENDA = :NUMTRANSVENDA;
SELECT *
FROM MXMP_ENTREGAS
WHERE ID = :ID_ENTREGA;
SELECT *
FROM MXMP_FOTOS
WHERE ID_REGISTRO = :ID_REGISTRO
ORDER BY DATA DESC;
SELECT *
FROM MXMP_CONFIGURACAO_EMAIL;
SELECT *
FROM MXMP_CONTROLE_EMAIL_ENTREGA
WHERE ID_ENTREGA = :ID_ENTREGA;
```

Como interpretar
Se o parâmetro exige foto e o usuário não anexou, o bloqueio pode ser comportamento esperado.
Se a foto existe localmente e não subiu, olhar sincronização/Wi-Fi.
Se o e-mail está configurado incorretamente, o XML não será enviado pelo app. A documentação funcional do maxMotorista cita explicitamente a configuração de e-mail/XML e os parâmetros de fotos e validação de canhoto.
Quando escalar
Se a configuração está correta, a foto está salva, mas nunca sobe.
Se o envio de e-mail falha mesmo com configuração válida.
Se o validador de NF-E rejeita canhotos válidos de forma recorrente.

#### Entrega não aparece no aplicativo do motorista
Sintoma
Cliente informa que o motorista não está enxergando as entregas no app para realizar as baixas, mesmo já tendo feito a roteirização / carregamento.
Exemplos de relatos:
### “Montei o carregamento, faturei, mas não aparece nada no app do motorista.”
### “O motorista X não recebeu as entregas do carregamento Y.”

Perguntas iniciais para o cliente
Qual é o carregamento?
Número do carregamento (NUMCAR) e filial.
### Qual motorista deveria receber essas entregas?
Nome / código do motorista e usuário correspondente no app.
Esse carregamento já foi faturado?
Perguntar explicitamente se as notas já foram emitidas.
### O motorista já fez sincronização recente no app?
Pedir para ele forçar uma sincronização e informar horário.
### As entregas aparecem no portal web (maxMotorista / consultas)?
Se não aparecem nem no web, o problema está antes do app.

1) Validar se o carregamento está corretamente faturado
No ERP:
Tabela ERP_MXSCARREG
Verificar se o NUMCAR informado existe.
Conferir:
quantidade de notas (campo de “numnotas” / “qtd notas”, conforme layout);
se não está cancelado / fechado de forma indevida.
Exemplo:
```sql
SELECT *
```

### FROM ERP_MXSCARREG
### WHERE NUMCAR = :NUMCAR;
Tabela ERP_MXSNFSAID
Verificar se existem notas fiscais vinculadas a esse carregamento (NUMCAR) e se não estão canceladas.
```sql
SELECT *
```

### FROM ERP_MXSNFSAID
### WHERE NUMCAR = :NUMCAR
### AND ESPECIE = 'NF'
### AND (DTCANCEL IS NULL OR DTCANCEL = TO_DATE('01/01/1900','DD/MM/YYYY'));
Se não houver notas para o carregamento, ou estiverem canceladas, não haverá entregas para o motorista.

### 2) Confirmar que as notas do carregamento viraram registros de entrega
Fluxo geral:
ERP_MXSNFSAID + MXSHISTORICOPEDC → MXMP_NOTAS_FISCAIS → MXMP_ENTREGAS
### Tabela MXSHISTORICOPEDC (pedidos / faturamento)
Verificar se os pedidos do carregamento estão lá e se têm horário de faturamento (HORAFAT / MINUTOFAT):
```sql
SELECT NUMPED, NUMCAR, HORAFAT, MINUTOFAT
```

### FROM MXSHISTORICOPEDC
### WHERE NUMCAR = :NUMCAR;
Tabela MXMP_NOTAS_FISCAIS
Verificar se as notas do carregamento foram gravadas aqui:
```sql
SELECT *
```

### FROM MXMP_NOTAS_FISCAIS NF
### JOIN ERP_MXSNFSAID S
### ON NF.NUMERO_NOTA = S.NUMNOTA
### AND NF.NUMERO_TRANSVENDA = S.NUMTRANSVENDA
### WHERE S.NUMCAR = :NUMCAR;
### Tabela MXMP_ENTREGAS
Essa tabela é a base que manda as entregas para o app do motorista.
Verificar se existem registros para o carregamento:
```sql
SELECT *
```

### FROM MXMP_ENTREGAS
### WHERE ID_CARREGAMENTO = :NUMCAR;
Situações possíveis:
Não existe registro em MXMP_NOTAS_FISCAIS → problema na criação das notas de logística.
Existe em MXMP_NOTAS_FISCAIS, mas não em MXMP_ENTREGAS → problema na criação das entregas.
Existe em MXMP_ENTREGAS → seguir para passos de sincronização e vinculação de motorista.

### 3) Verificar se a job de entregas já rodou (30 minutos)
A criação de entregas é feita por procedures chamadas por um job que roda a cada 30 minutos:
### CRIAR_MXMP_NOTAS_FISCAIS
### CRIAR_MXMP_ENTREGAS
### CRIAR_MXMP_ENDERECO_ENTREGAS
Passos:
### Verificar na MXSHISTORICOPEDC o horário de faturamento do pedido:
```sql
SELECT NUMPED, NUMCAR, HORAFAT, MINUTOFAT, DTFAT
```

### FROM MXSHISTORICOPEDC
### WHERE NUMCAR = :NUMCAR;
Comparar com o horário atual:
Se ainda não se passaram 30 minutos desde o faturamento, orientar o cliente a aguardar o próximo ciclo da job.
Se já se passaram mais de 30 minutos e não há registros em MXMP_NOTAS_FISCAIS / MXMP_ENTREGAS, provavelmente a job ou as procedures estão com problema.
Em ambiente controlado (com cuidado e seguindo padrão da empresa), o DBA/analista avançado pode rodar manualmente as procedures:
### BEGIN
### CRIAR_MXMP_NOTAS_FISCAIS;
### COMMIT;
### END;
/

### BEGIN
### CRIAR_MXMP_ENTREGAS;
### COMMIT;
### END;
/

### BEGIN
### CRIAR_MXMP_ENDERECO_ENTREGAS;
### COMMIT;
### END;
/
Se ao rodar as procedures der erro na tela → registrar mensagem de erro e envolver o DBA da Máxima / time técnico.
Se rodar sem erro, mas ainda não criar entregas → provavelmente falta campo/parametrização ou há alguma condição de filtro não atendida.

### 4) Validar motorista vinculado ao carregamento
Outro caso comum: o carregamento foi vinculado a outro motorista (ou a um motorista inexistente/inativo).
### Na ERP_MXSCARREG, verificar o campo CODMOTORISTA:
```sql
SELECT NUMCAR, CODMOTORISTA
```

### FROM ERP_MXSCARREG
### WHERE NUMCAR = :NUMCAR;
Com o CODMOTORISTA, conferir na tabela de usuários/motoristas da logística, por exemplo:
```sql
SELECT *
```

### FROM MXMP_USUARIOS
### WHERE ID_MOTORISTA = :CODMOTORISTA;
(Ajustar o nome da coluna de acordo com o layout real: pode ser COD_MOTORISTA, ID_MOTORISTA, etc.)
Situações:
Não existe usuário para esse CODMOTORISTA → o carregamento foi amarrado a um motorista inexistente.
O usuário/motorista está inativo → o app não vai receber as entregas.
Nesses casos, o cliente deve corrigir o motorista no carregamento (conforme fluxo funcional) e, se necessário, reprocessar entregas.

### 5) Verificar sincronização com o aplicativo do motorista
### Se MXMP_ENTREGAS já tem os registros:
Verificar o campo de data/horário de sincronização na própria tabela (por exemplo, um campo do tipo DT_SINCRONIZACAO ou similar).
```sql
SELECT *
```

### FROM MXMP_ENTREGAS
### WHERE ID_CARREGAMENTO = :NUMCAR;
Se o campo de sincronização estiver preenchido:
Significa que o motorista já sincronizou e os dados foram enviados para o app.
Se mesmo assim não aparece no app:
### extrair/inspecionar o banco local do aplicativo (SQLite) do motorista;
conferir se o registro está chegando no mobile ou se está havendo erro local.
Se o campo de sincronização estiver vazio:
O motorista ainda não sincronizou as entregas.
Orientar o cliente a fazer:
logout/login no app,
forçar sincronização,
confirmar se a data/hora da sincronização mudou.

6) Verificar parâmetro de “Envio das notas fiscais para processamento” (dias)
Existe um parâmetro na área administrativa relacionado ao prazo em dias para envio das notas fiscais para processamento de entregas.
Esse parâmetro define que as entregas só serão geradas se a data do pedido/nota for superior à quantidade de dias configurada.
Passos:
Verificar o valor parametrizado (no menu administrativo / tabela de parâmetros específica – documentar nesse capítulo o nome da tabela/coluna quando você tiver).
### Comparar a data do pedido/nota com esse parâmetro:
Se a data do pedido/nota não atende ainda o prazo mínimo, as entregas não serão geradas.
Ajustar o parâmetro ou aguardar o período correto, conforme a regra de negócio do cliente.

SELECTs recomendados (resumo)
Carregamento no ERP
```sql
SELECT *
```

### FROM ERP_MXSCARREG
### WHERE NUMCAR = :NUMCAR;
Notas do carregamento
```sql
SELECT *
```

### FROM ERP_MXSNFSAID
### WHERE NUMCAR = :NUMCAR
### AND ESPECIE = 'NF'
### AND (DTCANCEL IS NULL OR DTCANCEL = TO_DATE('01/01/1900','DD/MM/YYYY'));
### Pedidos e horário de faturamento
```sql
SELECT NUMPED, NUMCAR, HORAFAT, MINUTOFAT, DTFAT
```

### FROM MXSHISTORICOPEDC
### WHERE NUMCAR = :NUMCAR;
Notas de logística
```sql
SELECT *
```

### FROM MXMP_NOTAS_FISCAIS NF
### JOIN ERP_MXSNFSAID S
### ON NF.NUMERO_NOTA = S.NUMNOTA
### AND NF.NUMERO_TRANSVENDA = S.NUMTRANSVENDA
### WHERE S.NUMCAR = :NUMCAR;
### Entregas geradas para o carregamento
```sql
SELECT *
```

### FROM MXMP_ENTREGAS
### WHERE ID_CARREGAMENTO = :NUMCAR;
### Motorista do carregamento e vínculo com usuário
```sql
SELECT NUMCAR, CODMOTORISTA
```

### FROM ERP_MXSCARREG
### WHERE NUMCAR = :NUMCAR;

```sql
SELECT *
```

### FROM MXMP_USUARIOS
### WHERE ID_MOTORISTA = :CODMOTORISTA;
(Ajustar nomes de campos conforme o seu esquema real.)

Quando escalar para desenvolvimento / DBA
Escale para time técnico / DBA / desenvolvimento quando:
O carregamento está correto em ERP_MXSCARREG e as notas existem em ERP_MXSNFSAID;
### Os pedidos constam em MXSHISTORICOPEDC com horário de faturamento válido;
Já se passaram mais de 30 minutos do faturamento;
Você já rodou (ou confirmou a execução) das procedures:
### CRIAR_MXMP_NOTAS_FISCAIS
### CRIAR_MXMP_ENTREGAS
CRIAR_MXMP_ENDERECO_ENTREGAS
e mesmo assim não há registros coerentes em MXMP_NOTAS_FISCAIS / MXMP_ENTREGAS;
Ou ao rodar as procedures, ocorre erro não trivial;
Ou as entregas existem em MXMP_ENTREGAS, há registro de sincronização, mas no app ainda não aparece mesmo após limpar base/sincronizar.
Nesses casos:
Registrar todas as informações (carregamento, motorista, notas, horários, prints, SELECTs executados);
Direcionar o ticket ao time técnico responsável, anexando mensagens de erro das procedures (quando houver) e resultados das consultas.

Conferindo o que as procedures deveriam criar
1) Diagnóstico da CRIAR_MXMP_NOTAS_FISCAIS
(notas que deveriam estar em MXMP_NOTAS_FISCAIS e não estão)
Esse SELECT replica a lógica principal da CRIAR_MXMP_NOTAS_FISCAIS e mostra quais notas atendem às regras, mas ainda não estão em MXMP_NOTAS_FISCAIS.
Com isso, o analista consegue ver se está faltando alguma informação vinda do ERP.
### SELECT
s.NUMCAR,
s.NUMNOTA,
s.NUMTRANSVENDA,
s.CODCLI,
s.DTSAIDA,
ped.NUMPED,
ped.CODENDENTCLI,
car.DATAMON,
car.DTSAIDA,
### car.CODMOTORISTA,
nf.NUMERO_NOTA AS NF_LOGISTICA,
nf.NUMERO_TRANSVENDA AS TRANSV_LOGISTICA
FROM ERP_MXSNFSAID s
INNER JOIN MXSHISTORICOPEDC ped
ON s.NUMPED = ped.NUMPED
### INNER JOIN (
```sql
SELECT A.NUMCAR, A.DTFECHA, A.DT_CANCEL, A.DATAMON, A.DTSAIDA, A.CODMOTORISTA
```

### FROM ERP_MXSCARREG A
### WHERE A.DTSAIDA >= GET_DATA_INICIO_SISTEMA
AND NVL(A.DT_CANCEL, TO_DATE('01/01/1900','DD/MM/YYYY')) = TO_DATE('01/01/1900','DD/MM/YYYY')
AND NVL(A.DTFECHA , TO_DATE('01/01/1900','DD/MM/YYYY')) = TO_DATE('01/01/1900','DD/MM/YYYY')
### AND NVL(A.CODMOTORISTA, '0') <> '0'
) car
ON s.NUMCAR = car.NUMCAR
LEFT JOIN MXMP_NOTAS_FISCAIS nf
ON nf.NUMERO_NOTA = s.NUMNOTA
AND nf.NUMERO_TRANSVENDA = s.NUMTRANSVENDA
WHERE s.ESPECIE = 'NF'
AND s.DTSAIDA >= GET_DATA_INICIO_SISTEMA
AND NVL(s.DTCANCEL, TO_DATE('01/01/1900','DD/MM/YYYY')) = TO_DATE('01/01/1900','DD/MM/YYYY')
AND nf.NUMERO_NOTA IS NULL
AND nf.NUMERO_TRANSVENDA IS NULL
- opcional: focar em um carregamento específico
- AND s.NUMCAR = :NUMCAR
ORDER BY s.NUMCAR, s.NUMNOTA;
Como interpretar:
Se esse SELECT traz linhas, significa que existem notas no ERP (ERP_MXSNFSAID + MXSHISTORICOPEDC + ERP_MXSCARREG) que atendem à regra da procedure, mas ainda não foram gravadas em MXMP_NOTAS_FISCAIS.
Verificar:
se CODCLI, NUMPED, NUMCAR estão corretos;
### se DTSAIDA, CODMOTORISTA, DATAMON fazem sentido;
se existe algum padrão de notas “sobrando” (ex.: sempre de uma filial específica, sempre com determinado tipo de condição de venda).
Se o SELECT não retorna nada, em tese não há notas pendentes para entrar em MXMP_NOTAS_FISCAIS segundo a regra da procedure.

### 2) Diagnóstico da CRIAR_MXMP_ENTREGAS
### (notas que já estão em MXMP_NOTAS_FISCAIS mas ainda não geraram entregas)
Esse SELECT replica a parte principal da CRIAR_MXMP_ENTREGAS, focando nas notas que:
já existem em MXMP_NOTAS_FISCAIS
### ainda não têm ID_ENTREGA
estão amarradas a um carregamento (NUMCAR)
e traz ainda informações de localização (cliente / endereço de entrega).
### SELECT
s.NUMCAR AS ID_CARREGAMENTO,
s.NUMNOTA,
s.NUMTRANSVENDA,
s.CODCLI AS ID_CLIENTE,
### DECODE(ped.CODENDENTCLI, 0, NULL, ped.CODENDENTCLI) AS ID_ENDERECO_ENTREGA,
nf.ID AS ID_REGISTRO_NOTA_LOG,
### nf.ID_ENTREGA,
### ent.ID AS ID_ENTREGA_EXISTENTE,
locCli.LATITUDE AS LAT_CLI,
locCli.LONGITUDE AS LON_CLI,
locEnd.LATITUDE AS LAT_END,
locEnd.LONGITUDE AS LON_END
FROM MXMP_NOTAS_FISCAIS nf
JOIN ERP_MXSNFSAID s
ON nf.NUMERO_NOTA = s.NUMNOTA
AND nf.NUMERO_TRANSVENDA = s.NUMTRANSVENDA
JOIN MXSHISTORICOPEDC ped
ON s.NUMPED = ped.NUMPED
### LEFT JOIN MXMP_ENTREGAS ent
### ON ent.ID = nf.ID_ENTREGA
LEFT JOIN MXMP_LOCALIZACAO_CLIENTE locCli
ON locCli.ID_CLIENTE = s.CODCLI
### LEFT JOIN MXMP_LOCALIZACAO_END_ENTREGA locEnd
ON locEnd.CODCLI = s.CODCLI
AND locEnd.ID_ENDERECO_ENTREGA = DECODE(ped.CODENDENTCLI, 0, NULL, ped.CODENDENTCLI)
### WHERE nf.ID_ENTREGA IS NULL
AND s.NUMCAR IS NOT NULL
AND s.ESPECIE = 'NF'
AND s.DTSAIDA >= GET_DATA_INICIO_SISTEMA
- opcional: focar em um carregamento específico
- AND s.NUMCAR = :NUMCAR
ORDER BY s.NUMCAR, s.NUMNOTA;
Como interpretar:
Linhas retornadas = notas que já foram para MXMP_NOTAS_FISCAIS, mas ainda não ganharam ID_ENTREGA.
Campos importantes:
ID_ENDERECO_ENTREGA → se estiver estranho ou inconsistente, pode travar a criação de entrega.
LAT_CLI / LON_CLI e LAT_END / LON_END →
se tudo NULL, pode indicar problema de geolocalização (sem registro em MXMP_LOCALIZACAO_CLIENTE / MXMP_LOCALIZACAO_END_ENTREGA).
Se nada aparecer aqui, significa que em teoria todas as notas com esse padrão já têm ID_ENTREGA ou nem se encaixam na regra da procedure.

3) Conferindo se existem entregas duplicadas para o mesmo cliente/carregamento/endereço
Esse SELECT ajuda a ver se o bloqueio da procedure pode ser por já existir entrega:
### SELECT
e.ID,
e.ID_CLIENTE,
e.ID_CARREGAMENTO,
e.ID_ENDERECO_ENT_PED,
### COUNT(*) OVER(
PARTITION BY e.ID_CLIENTE, e.ID_CARREGAMENTO, e.ID_ENDERECO_ENT_PED
### ) AS QTD_ENTREGAS_PARA_MESMO_ALVO
### FROM MXMP_ENTREGAS e
WHERE e.ID_CARREGAMENTO = :NUMCAR
### ORDER BY QTD_ENTREGAS_PARA_MESMO_ALVO DESC, e.ID;
Se QTD_ENTREGAS_PARA_MESMO_ALVO > 1, já tem mais de uma entrega para a mesma combinação de cliente + carregamento + endereço, o que interfere diretamente na lógica QTD_ENTREGAS_EXISTENTES da procedure.

### MaxRoteirizador

#### Pedido não aparece na tela de roteirização
Sintoma
Cliente informa que o pedido existe no ERP, mas não aparece no mapa / grade da roteirização. A documentação do mapa funcional indica que a seleção de pedidos para montagem de carga parte principalmente de MXSHISTORICOPEDC e MXSHISTORICOPEDI, combinadas com status e dados de apoio do ERP.
O que pedir ao cliente
Número do pedido.
Filial.
Se o pedido já foi faturado ou se o cliente trabalha com faturamento por pedido.
Cidade, praça, rota, região e cliente usados no filtro.
Se o pedido veio do ERP ou por XML.
Passo a passo
Confirmar se o pedido existe em MXSHISTORICOPEDC e os itens em MXSHISTORICOPEDI.
Verificar se o pedido já não está vinculado a um carregamento / romaneio.
Validar os filtros de rota, praça, região, cidade e filial, porque esses filtros dependem do correto preenchimento do ERP e dos vínculos auxiliares.
Validar parâmetros que interferem diretamente na elegibilidade do pedido, especialmente:
### Utilizar faturamento por pedido;
### Trabalhar com montagem de pedidos balcão reserva;
Validar campos do WMS (WinThor);
### Validar campo TipoEntrega do Item do Pedido;
Utilizar rota vinculada a praça.
SELECTs
```sql
SELECT *
```

### FROM MXSHISTORICOPEDC
### WHERE NUMPED = :NUMPED;
```sql
SELECT *
```

### FROM MXSHISTORICOPEDI
### WHERE NUMPED = :NUMPED;
```sql
SELECT *
```

### FROM ERP_MXSMOV
### WHERE NUMPED = :NUMPED;
```sql
SELECT *
```

### FROM MXMP_BASE_CARREGAMENTO
### WHERE ID_CARREGAMENTO IN (
```sql
SELECT NUMCAR
```

### FROM MXSHISTORICOPEDC
### WHERE NUMPED = :NUMPED
);
Como interpretar
Se o pedido não existir em MXSHISTORICOPEDC, o problema está antes da roteirização.
Se o pedido existe e continua fora da tela, normalmente o próximo suspeito é filtro/regra de negócio ou parâmetro funcional. A própria documentação dos parâmetros aponta que o comportamento da tela muda conforme faturamento por pedido, WMS, praça/rota e tipo de entrega.
Quando escalar
Se o pedido existe, não está vinculado, atende à regra do cliente e mesmo assim não aparece.
Se houver indício de erro de regra na própria tela de roteirização.

#### Não consigo salvar a pré-carga / carga
Sintoma
Usuário consegue selecionar pedidos, mas não consegue salvar a carga ou pré-carga.
O que pedir ao cliente
Número do carregamento, se já foi gerado.
Se foi informado veículo e motorista.
Se usa frota própria, transportadora ou ambos.
Print da mensagem exibida na tela.
Passo a passo
Confirmar se existe tentativa gravada em MXMP_BASE_CARREGAMENTO ou MXMP_ROTEIRIZACAO.
Verificar se motorista e veículo existem e estão disponíveis.
Validar parâmetros:
Permitir Salvar Pré Carga Sem Veículo;
### Salvar Pré Carga Sem Motorista;
Prioriza os veículos de terceiros na busca de veículos para montagem de carga;
Trabalhar com transportadora.
Se o bloqueio mencionar valor mínimo, revisar:
Validar valor mínimo por Rota;
Validar valor mínimo por Praça.
SELECTs
```sql
SELECT *
```

### FROM MXMP_BASE_CARREGAMENTO
### WHERE ID_CARREGAMENTO = :ID_CARREGAMENTO;
```sql
SELECT *
```

### FROM MXMP_ROTEIRIZACAO
### WHERE ID_CARREGAMENTO = :ID_CARREGAMENTO;
```sql
SELECT *
```

### FROM ERP_MXSVEICUL
### WHERE CODVEICULO = :ID_VEICULO;
```sql
SELECT *
```

### FROM MXSUSUARI
### WHERE CODUSUR = :ID_MOTORISTA;
Como interpretar
Se a carga não existe nem em MXMP_BASE_CARREGAMENTO, o bloqueio ocorreu antes do salvamento.
Se existir carga base sem motorista/veículo, o comportamento pode ser coerente com os parâmetros da pré-carga.
Se o problema for com transporte de terceiros, os parâmetros de priorização também influenciam a busca de veículo.
Quando escalar
Se todos os cadastros e parâmetros estão corretos e a tela continua bloqueando sem justificativa clara.

#### Carregamento não aparece em Consultas > Carregamentos
Sintoma
Usuário salvou a carga, mas ela não aparece na consulta de carregamentos.
O que pedir ao cliente
Número do carregamento.
Filial.
Data de montagem.
Se o carregamento foi cancelado ou fechado.
Se foi salvo com quebra por filial/lote/reentrega.
Passo a passo
Verificar se o carregamento existe no ERP (MXSCARREG) e/ou na base de logística (MXMP_BASE_CARREGAMENTO, MXMP_ROMANEIO). O mapa funcional do maxRoteirizador liga essa consulta a MXSCARREG, MXSHISTORICOPEDC, MXSHISTORICOPEDI, MXMP_ROMANEIO e MXMP_ROTA_ROMANEIO.
Verificar filtros de filial e período.
Validar se o carregamento não foi cancelado, fechado ou convertido para outro romaneio.
Se houver divergência, analisar histórico/log do carregamento.
SELECTs
```sql
SELECT *
```

### FROM MXSCARREG
### WHERE NUMCAR = :NUMCAR;
```sql
SELECT *
```

### FROM MXMP_BASE_CARREGAMENTO
### WHERE ID_CARREGAMENTO = :NUMCAR;
```sql
SELECT *
```

### FROM MXMP_ROMANEIO
### WHERE ID_CARREGAMENTO = :NUMCAR;
```sql
SELECT *
```

### FROM MXMP_HISTORICO_CARREGAMENTO
### WHERE ID_CARREGAMENTO = :NUMCAR
### ORDER BY DATA DESC;
Como interpretar
Se existe no ERP mas não na MXMP, o salvamento/logística não consolidou.
Se existe na MXMP, mas a consulta não mostra, geralmente é filtro de período/filial/situação.
Se houver histórico de cancelamento ou mudança de romaneio, isso explica “sumiço” da consulta.
Quando escalar
Se o dado está gravado corretamente, mas a tela não retorna o carregamento.

#### Romaneio não aparece ou aparece incompleto
Sintoma
Cliente diz que o romaneio não aparece na consulta ou aparece sem todos os pedidos / notas esperados.
O que pedir ao cliente
Número do romaneio ou carregamento.
Pedido(s) esperados.
Filial.
Data da montagem.
Se houve quebra por filial, lote ou reentrega.
Passo a passo
Verificar MXMP_ROMANEIO e MXMP_ROTA_ROMANEIO.
Confirmar se os pedidos/itens existem em MXSHISTORICOPEDC e MXSHISTORICOPEDI.
Confirmar se as notas estão em MXSNFSAID.
Se houver divergência, analisar custos e estrutura do romaneio.
SELECTs
```sql
SELECT *
```

### FROM MXMP_ROMANEIO
### WHERE ID = :ID_ROMANEIO
### OR ID_CARREGAMENTO = :NUMCAR;
```sql
SELECT *
```

### FROM MXMP_ROTA_ROMANEIO
### WHERE ID_ROMANEIO = :ID_ROMANEIO;
```sql
SELECT *
```

### FROM MXSHISTORICOPEDC
### WHERE NUMCAR = :NUMCAR;
```sql
SELECT *
```

### FROM MXSHISTORICOPEDI
### WHERE NUMPED IN (
```sql
SELECT NUMPED
```

### FROM MXSHISTORICOPEDC
### WHERE NUMCAR = :NUMCAR
);
```sql
SELECT *
```

### FROM MXSNFSAID
### WHERE NUMCAR = :NUMCAR;
Como interpretar
Se os pedidos não estão em MXSHISTORICOPEDC/PEDI, o problema é de origem.
Se os pedidos existem, mas o romaneio não os reflete, a falha está na montagem/consolidação.
A própria documentação do mapa funcional ressalta que MXSHISTORICOPEDC/MXSHISTORICOPEDI são a base para saber quais pedidos e itens compõem o romaneio.
Quando escalar
Se os pedidos e notas estão corretos, mas a composição do romaneio está errada sem explicação funcional.

#### Falha Geocode / cliente não aparece corretamente no mapa
Sintoma
Cliente não aparece no mapa, aparece sem localização, ou entra em Falha Geocode.
O que pedir ao cliente
Código do cliente.
Endereço completo.
Se usa endereço padrão ou endereço de entrega.
Se o problema acontece com um cliente ou vários.
Passo a passo
Verificar MXSCLIENT e MXSCLIENTENDENT.
Verificar MXMP_LOCALIZACAO_CLIENTE e MXMP_LOCALIZACAO_END_ENTREGA.
Verificar MXMP_FALHA_GEOCODE, MXMP_FILA_GEOCODE e MXMP_LOG_ERROS.
Confirmar se o serviço de geocodificação está ativo.
Validar o parâmetro relacionado a atualização das coordenadas do cliente. A documentação do maxRoteirizador mostra que “Atualizar as coordenadas do cliente ao realizar o check in” influencia cenários em que o endereço varia ou é fixo.
SELECTs
```sql
SELECT *
```

### FROM MXSCLIENT
### WHERE CODCLI = :CODCLI;
```sql
SELECT *
```

### FROM MXSCLIENTENDENT
### WHERE CODCLI = :CODCLI;
```sql
SELECT *
```

### FROM MXMP_LOCALIZACAO_CLIENTE
### WHERE ID_CLIENTE = :CODCLI;
```sql
SELECT *
```

### FROM MXMP_LOCALIZACAO_END_ENTREGA
### WHERE CODCLI = :CODCLI;
```sql
SELECT *
```

### FROM MXMP_FALHA_GEOCODE
### WHERE ID_CLIENTE = :CODCLI
### ORDER BY DATA DESC;
```sql
SELECT *
```

### FROM MXMP_FILA_GEOCODE
### WHERE ID_CLIENTE = :CODCLI
### ORDER BY DATA_CADASTRO DESC;
Como interpretar
Se o cadastro de endereço estiver incompleto, o problema é de dado.
Se o cadastro está certo, mas não existe MXMP_LOCALIZACAO_*, o geocode não processou.
Se existe MXMP_FALHA_GEOCODE, olhar a fila/log para entender o motivo da falha. O mapa funcional já indica exatamente essa cadeia de análise.
Quando escalar
Se o endereço está correto, o serviço de geocodificação está ativo e a fila continua falhando sem motivo claro.

#### Pedido não aparece em “Pedidos prontos para montagem”
Sintoma
Usuário vê o pedido no ERP, mas o painel “Pedidos prontos para montagem” não lista o item.
O que pedir ao cliente
Número do pedido.
Filial.
Situação do pedido.
Se o pedido já foi vinculado a alguma carga.
Se o cliente usa WMS, rota vinculada a praça ou faturamento por pedido.
Passo a passo
Verificar MXSHISTORICOPEDC e MXSHISTORICOPEDI.
Verificar se o pedido já está em MXMP_BASE_CARREGAMENTO.
Revisar MXSROTAEXP, MXSPRACA e MXSFILIAL.
Verificar o parâmetro Utilizar faturamento por pedido, porque ele altera quando o pedido entra no fluxo. A própria documentação destaca esse ponto e menciona que, quando o cliente trabalha com faturamento por pedido, isso muda o comportamento do processo.
SELECTs
```sql
SELECT *
```

### FROM MXSHISTORICOPEDC
### WHERE NUMPED = :NUMPED;
```sql
SELECT *
```

### FROM MXSHISTORICOPEDI
### WHERE NUMPED = :NUMPED;
```sql
SELECT *
```

### FROM MXMP_BASE_CARREGAMENTO
### WHERE ID_CARREGAMENTO IN (
```sql
SELECT NUMCAR
```

### FROM MXSHISTORICOPEDC
### WHERE NUMPED = :NUMPED
);
```sql
SELECT *
```

### FROM MXSROTAEXP
### WHERE CODROTA = :CODROTA;
Como interpretar
Se já estiver em MXMP_BASE_CARREGAMENTO, o pedido não está mais “pronto”; ele já foi aproveitado.
Se o pedido existe mas está sem rota/praça/filial coerente, o painel pode não trazê-lo.
O próprio documento do mapa funcional aponta MXSHISTORICOPEDC, MXSHISTORICOPEDI e MXMP_BASE_CARREGAMENTO como base dessa tela.
Quando escalar
Se o pedido atende a todas as regras e continua fora do indicador.

#### XML importado não gera nota/pedido na roteirização
Sintoma
Cliente importou XML, mas a nota/pedido não aparece para roteirização.
O que pedir ao cliente
Número da nota.
Chave do XML, se houver.
Data da importação.
Se o ambiente está parametrizado para trabalhar com XML.
Passo a passo
Confirmar o parâmetro Trabalhar com importação de XML. A documentação diz claramente que esse fluxo só deve ser ativado quando o cliente quer usar XML além do ERP.
Verificar MXSDOCELETRONICO e MXSNFSAID.
Verificar MXMP_DADOS_ENTREGA_NOTA.
Verificar MXMP_FILA_VERI_SEFAZ, MXMP_CAD_SEFAZ e MXMP_LOG_ERROS.
SELECTs
```sql
SELECT *
```

### FROM MXSDOCELETRONICO
### WHERE CHAVEACESSO = :CHAVE
### OR NUMNOTA = :NUMNOTA;
```sql
SELECT *
```

### FROM MXSNFSAID
### WHERE NUMNOTA = :NUMNOTA;
```sql
SELECT *
```

### FROM MXMP_DADOS_ENTREGA_NOTA
### WHERE NUMERO_NOTA = :NUMNOTA;
```sql
SELECT *
```

### FROM MXMP_FILA_VERI_SEFAZ
### WHERE ID_NOTA = :ID_NOTA
### ORDER BY DATA DESC;
```sql
SELECT *
```

### FROM MXMP_LOG_ERROS
### ORDER BY DATA DESC;
Como interpretar
Se o XML não gerou MXSNFSAID, a falha está antes da logística.
Se gerou MXSNFSAID mas não gerou dados em MXMP_DADOS_ENTREGA_NOTA, o problema está no processamento da nota para logística.
Se a fila da SEFAZ apontar erro, o bloqueio pode ser fiscal/validação.
Quando escalar
Se o parâmetro XML está ativo, a nota entrou, mas o fluxo para na validação/integração sem causa clara.

#### Custo / lucratividade por romaneio divergente
Sintoma
Cliente diz que o relatório de custo ou lucratividade por romaneio não bate com a expectativa.
O que pedir ao cliente
Romaneio.
Carregamento.
Filial.
Tabela de frete usada.
Se trabalha com frete terceirizado.
Passo a passo
Verificar MXMP_CUSTO_ROMANEIO, MXMP_CUSTO_ROMANEIO_FRETE e MXMP_CUSTO_ROMANEIO_TERCEIRIZADO.
Verificar MXMP_TABELA_FRETE, MXMP_CIDADE_TABELA_FRETE, MXMP_CUSTO_CIDADE_FRETE, MXMP_CUSTO_FAIXA_FRETE.
Revisar se o parâmetro Trabalhar com custo de montagem do carregamento está em linha com a regra do cliente.
Se houver frete terceirizado, revisar o aceite e históricos de frete.
SELECTs
```sql
SELECT *
```

### FROM MXMP_CUSTO_ROMANEIO
### WHERE ID_ROMANEIO = :ID_ROMANEIO;
```sql
SELECT *
```

### FROM MXMP_CUSTO_ROMANEIO_FRETE
### WHERE ID_ROMANEIO = :ID_ROMANEIO;
```sql
SELECT *
```

### FROM MXMP_CUSTO_ROMANEIO_TERCEIRIZADO
### WHERE ID_ROMANEIO = :ID_ROMANEIO;
```sql
SELECT *
```

### FROM MXMP_TABELA_FRETE
### WHERE ID = :ID_TABELA_FRETE;
```sql
SELECT *
```

### FROM MXMP_HIST_ACEITE_FRETE
### WHERE ID_ROMANEIO = :ID_ROMANEIO
### ORDER BY DATA DESC;
Como interpretar
Se o romaneio não tem custo, o relatório naturalmente ficará zerado ou incompleto.
Se a tabela de frete não bate com a rota/cidade/faixa, o cálculo diverge.
O mapa funcional do maxRoteirizador liga exatamente esses relatórios às tabelas de custo e tabela de frete.
Quando escalar
Se os custos e a tabela de frete estão corretos, mas o cálculo final apresentado pelo sistema continua divergente.

#### Extrator / integração aparece offline ou sem atualizar
Sintoma
No dashboard de indicadores de uso, o extrator aparece offline ou o cliente diz que os dados não estão chegando.
O que pedir ao cliente
Nome do ambiente.
Horário em que o problema começou.
Se mais alguma integração falhou no mesmo período.
Print do dashboard de indicadores de uso.
Passo a passo
Verificar a tela de indicadores de uso, que o teu mapa funcional relaciona diretamente com MXMP_POSICAO_TATICO_OPERACIONAL e com o acompanhamento do extrator/servidor.
Confirmar se os dados de ERP recentes continuam sendo gravados.
Se for WinThor, lembrar que o parâmetro Bloquear Alterações de Carregamento em Sincronização existe justamente para reduzir conflito de sincronização.
Se o extrator estiver offline, seguir o playbook de infraestrutura/extrator do cliente.
SELECTs
```sql
SELECT *
```

### FROM MXMP_POSICAO_TATICO_OPERACIONAL
### ORDER BY DATA DESC;
```sql
SELECT *
```

### FROM MXSHISTORICOPEDC
### WHERE DTMOV >= SYSDATE - 1
### ORDER BY DTMOV DESC;
```sql
SELECT *
```

### FROM MXMP_LOG_ERROS
### ORDER BY DATA DESC;
Como interpretar
Se o ERP continua recebendo pedidos/notas, mas a posição do extrator não atualiza, a falha pode estar no extrator/serviço.
Se nada recente entra no ERP logístico, pode ser uma quebra mais ampla de integração.
O mapa funcional já registra que a tela de indicadores de uso serve para acompanhar banco, servidor e extrator.
Quando escalar
Se a infraestrutura do extrator precisar de restart/análise técnica.
Se houver erro recorrente de integração sem causa funcional.

#### Usuário não vê tela, filtro, cliente, veículo ou função no maxRoteirizador
Sintoma
Usuário não consegue ver funcionalidade, filtro, cadastro, mapa ou consulta que outro usuário vê.
O que pedir ao cliente
Usuário.
Perfil.
Filial.
Tela específica que não aparece.
Se outro usuário do mesmo cliente enxerga.
Passo a passo
Verificar MXMP_USUARIOS, MXMP_PERFIL_ACESSO, MXMP_USUARIO_PERFIL_ACESSO, MXMP_PERMISSOES_*.
Verificar vínculo de filial e rota em MXMP_USUARIOS_FILIAIS e MXMP_USUARIOS_ROTAS.
Se o problema for veículo, revisar vínculo de filial do veículo, porque a documentação do mapa funcional do maxRoteirizador cita explicitamente que veículo pode não aparecer por falta de vínculo de filial ou campos obrigatórios.
Se o problema for cliente/mapa, revisar cliente, endereço, cidade e vínculos auxiliares.
SELECTs
```sql
SELECT *
```

### FROM MXMP_USUARIOS
### WHERE LOGIN = :LOGIN;
```sql
SELECT *
```

### FROM MXMP_USUARIO_PERFIL_ACESSO
### WHERE ID_USUARIO = :ID_USUARIO;
```sql
SELECT *
```

### FROM MXMP_USUARIOS_FILIAIS
### WHERE ID_USUARIO = :ID_USUARIO;
```sql
SELECT *
```

### FROM MXMP_USUARIOS_ROTAS
### WHERE ID_USUARIO = :ID_USUARIO;
```sql
SELECT *
```

### FROM MXMP_PERMISSOES_USUARIO
### WHERE ID_USUARIO = :ID_USUARIO;
Como interpretar
Se o usuário não está vinculado à filial ou rota correta, isso explica diferença de visualização.
Se o perfil não possui permissão, o comportamento é esperado.
O próprio teu mapeamento de configurações e cadastros do maxRoteirizador já aponta essas tabelas como base da análise de acesso e visibilidade.
Quando escalar
Se a permissão está correta e a tela continua invisível apenas para um usuário específico.
Se houver suspeita de bug no controle de acesso.

Esses 10 playbooks cobrem o núcleo mais comum do maxRoteirizador: roteirização, pré-carga, carregamentos, romaneios, geocode, pedidos prontos para montagem, XML, custos, extrator e permissões. Eles estão alinhados com o teu mapa funcional e com os parâmetros funcionais do produto.
No próximo passo eu posso fazer uma destas duas coisas:
transformar esses 10 playbooks em seções numeradas prontas para colar no capítulo, tipo 5.1, 5.2, 5.3;
ou gerar mais 10 playbooks complementares do maxRoteirizador, focando em WMS, tabela de frete, janela de entrega, agendamento, transbordo, crossdocking, quebra por filial, quebra por lote e reprocessamento da rota.

#### Integração travada por bloqueio no banco do cliente (WinThor)

Sintoma
O cliente informa que:
“A Máxima não está trabalhando direito / não está atualizando”,
mas ao olhar o ERP WinThor, tudo parece “normal” no uso diário,
ainda assim, os dados não estão sendo processados/inseridos como esperado (rotinas da Máxima que dependem de gravação/leitura no banco do WinThor ficam travadas).
Na prática, o problema costuma ser:
Sessões / rotinas do WinThor bloqueando tabelas, impedindo que os processos da Máxima consigam gravar ou ler no banco do cliente.

Perguntas iniciais para o cliente
O ambiente é WinThor local ou WinThor PCloud?
Isso define onde você vai conectar no banco.
O problema é geral ou em algum processo específico?
Ex.: só integração de pedidos, só baixas, só notas.
Usuários do WinThor relatam lentidão ou travamento?
Ajuda a confirmar que o problema é de banco/sessão.
Desde quando perceberam que a Máxima não está “andando”?
Útil para cruzar com sessões mais antigas/bloqueadas.
TI/ERP fez alguma atualização ou rotina pesada recente?
Jobs, scripts, relatórios ou processos em lote costumam gerar locks.

Passos de análise
Referências:
– Cap. 3: Arquitetura Funcional / Fluxo de Dados (WinThor ↔ Máxima)
– Cap. 5: Integrações e Entrada de Dados
– Cap. 7: Infraestrutura e parametrizações de integração

1) Conectar no banco do WinThor do cliente
Se WinThor for local (on-premise):
Conectar via MDesk ao banco do cliente, usando a conexão do schema da Máxima (ou outro usuário com permissão de leitura nas views de sessão/lock).
Se for WinThor PCloud:
Acessar o banco do cliente pelo workspace do PCloud, conectando-se ao banco Oracle correspondente ao ambiente WinThor.
Essa etapa é técnica (normalmente N2 / DBA), porque envolve acesso direto ao banco do WinThor.

2) Verificar se há bloqueios (locks) no banco do WinThor
Rodar a consulta abaixo para ver quem está bloqueando quem:
```sql
SELECT DECODE (L.BLOCK, 0, 'Em espera', 'Bloqueando ->') USER_STATUS,
```

### L.BLOCK,
### CHR (39) || S.SID || ',' || S.SERIAL# || CHR (39) SID_SERIAL,
### (SELECT INSTANCE_NAME FROM GV$INSTANCE WHERE INST_ID = L.INST_ID) CONN_INSTANCE,
### S.SID,
### S.PROGRAM,
### S.SCHEMANAME,
### S.OSUSER,
### S.MACHINE,
### DECODE (L.TYPE,
'RT', 'Redo Log Buffer',
'TD', 'Dictionary',
### 'TM', 'DML',
'TS', 'Temp Segments',
'TX', 'Transaction',
'UL', 'User',
'RW', 'Row Wait',
### L.TYPE) LOCK_TYPE,
### DECODE (L.LMODE,
0, 'None',
1, 'Null',
2, 'Row Share',
3, 'Row Excl.',
4, 'Share',
5, 'S/Row Excl.',
6, 'Exclusive',
### LTRIM (TO_CHAR (LMODE, '990'))) LOCK_MODE,
### CTIME,
### OBJECT_NAME,
### TO_CHAR(TRUNC(S.LAST_CALL_ET / 60 / 60), 'FM999900') || ':' ||
TO_CHAR(TRUNC(((S.LAST_CALL_ET / 60 / 60) - TRUNC(S.LAST_CALL_ET / 60 / 60)) * 60), 'FM00') || ':' ||
TO_CHAR(TRUNC(((((S.LAST_CALL_ET / 60 / 60) - TRUNC(S.LAST_CALL_ET / 60 / 60)) * 60) - TRUNC(((S.LAST_CALL_ET / 60 / 60) - TRUNC(S.LAST_CALL_ET / 60 / 60)) * 60))*60), 'FM00') TEMPO,
### S.LAST_CALL_ET TEMPO_EM_SEGUNDOS,
### L.TYPE,
### L.LMODE
### FROM GV$LOCK L
### JOIN GV$SESSION S
### ON (L.INST_ID = S.INST_ID
### AND L.SID = S.SID)
### JOIN GV$LOCKED_OBJECT O
### ON (O.INST_ID = S.INST_ID
### AND S.SID = O.SESSION_ID)
### JOIN DBA_OBJECTS D
### ON (D.OBJECT_ID = O.OBJECT_ID)
### WHERE (L.ID1, L.ID2, L.TYPE) IN (
```sql
SELECT ID1, ID2, TYPE
```

### FROM GV$LOCK
### WHERE REQUEST > 0)
### ORDER BY 13 DESC;
Como interpretar em linguagem de suporte:
Essa consulta mostra os objetos (tabelas) que estão sendo bloqueados e por qual sessão/programa.
Se aparecer linha com:
### USER_STATUS = 'Bloqueando ->':
essa sessão está bloqueando outras.
PROGRAM indicando algum executável do WinThor (rotina específica, processo em lote, etc.):
provavelmente é uma rotina do WinThor segurando lock nas tabelas que a Máxima precisa acessar.
Se o PROGRAM mostrar algo como PROCESSADOR.DLL (ou similar) e USER_STATUS estiver “Em espera”:
significa que o lado da Máxima está em espera porque o WinThor está segurando algum recurso.
Nessa visão, você já consegue:
ver qual rotina / executável do WinThor está causando bloqueio;
identificar qual objeto (tabela) está travado.
A partir daí, normalmente:
o analista de suporte da Máxima orienta o cliente a envolver TI / suporte WinThor para analisar a rotina que está prendendo o lock.

3) Verificar sessões “penduradas” há muito tempo
Rodar a outra consulta, focada em tempo de sessão e comando para kill:
```sql
SELECT DISTINCT SES.PROGRAM EXECUTAVEL,
```

### OBJ.OBJECT_NAME TABELA,
### TO_CHAR(TRUNC(SES.LAST_CALL_ET / 60 / 60),
### 'FM999900') || ':' ||
### TO_CHAR(TRUNC(((SES.LAST_CALL_ET / 60 / 60) -
### TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60),
### 'FM00') || ':' ||
### TO_CHAR(TRUNC(((((SES.LAST_CALL_ET / 60 / 60) -
### TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60) -
### TRUNC(((SES.LAST_CALL_ET / 60 / 60) -
### TRUNC(SES.LAST_CALL_ET / 60 / 60)) * 60))*60),
### 'FM00') TEMPO,
### SES.LAST_CALL_ET TEMPO_EM_SEGUNDOS,
### SES.STATUS,
### DECODE(LOC.LOCKED_MODE,
### 1, 'NO LOCK',
### 2, 'ROW SHARE',
### 3, 'ROW EXCLUSIVE',
### 4, 'SHARE',
### 5, 'SHARE ROW EXCL',
### 6, 'EXCLUSIVE',
### NULL) LOCKED_MODE,
'alter system kill session ''' || SID || ',' || SERIAL# ||
''' immediate;' COMANDO_DESCONEXAO,
### SES.SID SID,
### SES.SERIAL# SERIAL#,
### SQL.SQL_TEXT TEXTO_SQL,
### SES.MACHINE MAQUINA,
### SES.USERNAME USUARIO_ORACLE,
### SES.OSUSER USUARIOS_SO
### FROM V$SESSION SES,
### V$LOCKED_OBJECT LOC,
### DBA_OBJECTS OBJ,
### V$SQL SQL
### WHERE SES.SID = LOC.SESSION_ID
### AND LOC.OBJECT_ID = OBJ.OBJECT_ID
### AND SES.SQL_ADDRESS = SQL.ADDRESS(+)
### ORDER BY SES.LAST_CALL_ET DESC;
Como interpretar:
EXECUTAVEL (PROGRAM) → qual programa está com sessão aberta (rotina do WinThor, ferramenta, etc.).
TABELA → qual objeto está sendo afetado.
TEMPO / TEMPO_EM_SEGUNDOS → há quanto tempo essa sessão está ativa.
LOCKED_MODE → tipo de lock (EXCLUSIVE geralmente é o mais crítico).
COMANDO_DESCONEXAO → comando ALTER SYSTEM KILL SESSION pronto (para o DBA usar com cuidado).
Uso prático:
Se você encontrar sessões do WinThor com muitas horas (ou dias) em TEMPO e status ativo, segurando lock em tabelas relevantes para a Máxima:
isso explica por que as rotinas da Máxima ficam “paradas” ou em “espera”;
é recomendável orientar o cliente a envolver o DBA/infra do WinThor para encerrar essas sessões ou ajustar as rotinas.
Importante: o kill de sessão deve ser responsabilidade do DBA do cliente / time de infra. O suporte da Máxima não deve sair matando sessão em ambiente de produção do cliente sem alinhamento.

### 4) Verificar status da integração no portal Máxima
Além do banco do WinThor, vale conferir:
No MaxMotorista / MaxRoteirizador, na tela principal (normalmente na parte superior, centro da tela), existe um indicador de status da integração (online / offline).
### Se o status estiver offline:
verificar o extrator do cliente (serviço que conversa entre WinThor e Máxima);
analisar se o extrator está:
parado,
com erro de conexão,
ou travado por conta desses locks no banco.
Em muitos casos:
o extrator tenta acessar o WinThor,
encontra uma tabela bloqueada,
e fica “pendurado”, o que reflete como integração offline ou travada.

Quando escalar e para quem
Para o TI / DBA do cliente (WinThor):
Escalar quando:
as consultas de lock mostram sessões do WinThor com muito tempo de execução,
segurando lock em objetos críticos,
e isso está impedindo as rotinas da Máxima de inserir/atualizar dados.
Orientar:
a revisar as rotinas/processos do WinThor que geram esses locks;
avaliar necessidade de kill de sessão ou ajuste de processos.
Para o time técnico / DBA da Máxima:
Escalar quando:
você já verificou que o problema não é lock no WinThor (consultas limpas);
### extrator está rodando, status de integração ok;
mas mesmo assim:
os dados não chegam na Máxima,
e não há erro ou log claro no extrator.
Nessa hora, enviar:
horário aproximado do problema;
### prints do status de integração;
evidências que os locks no WinThor não são o problema (resultado das consultas limpas);
logs do extrator (quando aplicável).

### MaxPag

#### Baixa automática do MaxPag não está acontecendo Sintoma

Cliente informa que os pagamentos realizados via MaxPag (Pix, cartão etc.) não estão baixando automaticamente no ERP / financeiro.
Exemplos de relatos:
“O cliente pagou pelo link do MaxPag, mas o título não baixou automático.”
“Consigo ver o pagamento no MaxPag, mas não aparece baixa no sistema.”

Perguntas iniciais para o cliente
Qual é o título / documento?
Número do título, nota, pedido ou outro identificador que ajude a localizar o registro.
O pagamento foi confirmado no MaxPag?
Cliente consegue ver o pagamento como pago no portal do MaxPag?
A baixa automática já funcionou em algum momento nesse ambiente?
É um problema novo ou algo que nunca funcionou?
Houve alguma alteração recente de configuração?
Atualização de versão, mudança de servidor, troca de base ou reconfiguração do MaxPag.

1) Verificar se o parâmetro do job do MaxPag está ativo
Rodar:
```sql
SELECT *
```

### FROM MXSPARAMETRO
### WHERE TITULO = 'ATIVAR_JOBMAXPAG_EXTRATOR';
Se não retornar linha nenhuma:
→ É obrigatório incluir o parâmetro. Rodar o INSERT abaixo:
```sql
INSERT INTO MXSPARAMETRO
```

### (CODPARAMETRO, TITULO, NOME, VALOR, DESCRICAO,
### TIPODADO, CODCATEGORIAPARAMETRO, TIPOPARAMETRO, OCULTO, TABELACOMBOBOX, CODOPERACAO)
### VALUES
### (MXSPARAMETRO_SEQ.NEXTVAL,
### 'ATIVAR_JOBMAXPAG_EXTRATOR',
### 'ATIVAR_JOBMAXPAG_EXTRATOR',
### 'S',
'',
3,
1,
### 'G',
### 'N',
### NULL,
0);
Se o registro existir, mas o campo VALOR ≠ 'S':
→ Atualizar para ‘S’, pois o job de baixa automática depende disso.
(Esse passo garante que o job de integração da baixa automática do MaxPag esteja habilitado.)

2) Validar se o cadastro/configuração do MaxPag foi feito corretamente
Depois de garantir o parâmetro:
Confirmar, junto com o cliente, se o cadastro e configuração do MaxPag foram feitos conforme a base de conhecimento oficial.
Orientar o analista a consultar o documento de referência, onde está o passo a passo de configuração (credenciais, callbacks, vínculos, etc.):
https://basedeconhecimento.maximatech.com.br/pages/viewpage.action?pageId=113871186
Se alguma etapa de cadastro (token, credenciais, ambiente, callback, etc.) estiver incorreta, a baixa automática pode não ser disparada.

3) Acompanhar se as baixas estão chegando na MXSBAIXATITULOS
Com o parâmetro ativo e a configuração correta:
Verificar a tabela de controle de baixas:
```sql
SELECT *
```

### FROM MXSBAIXATITULOS
### ORDER BY DATA_TRANSFERENCIA DESC;
Pontos importantes:
Cada baixa recebida do MaxPag deve gerar um registro em MXSBAIXATITULOS.
Acompanhar principalmente:
### STATUS
## 4 → integrado com sucesso
## 0 → pendente para integração
outros valores (ex.: 5) → erro ou situação específica (por exemplo: título já estava baixado no ERP quando tentou integrar)
Interpretação rápida:
Não existe registro para o título
A baixa não está nem chegando na MXSBAIXATITULOS.
Pode ser problema de comunicação/integração entre MaxPag e o job do extrator.
### Existe registro, mas STATUS = 0
O lançamento chegou na logística/integração, mas não foi aplicado no ERP.
Pode ser erro de layout, problema no extrator, título já inexistente ou bloqueio no lado do ERP.
### STATUS = 4, mas cliente diz que não baixou
Verificar se a baixa realmente entrou no financeiro do ERP; pode ser divergência de ambiente/base ou de visualização.

4) Rodar atualizador / atualizar extrator do cliente (quando aplicável)
Se não está registrando na MXSBAIXATITULOS mesmo com parâmetro ativo:
Rodar o atualizador / rotina de atualização do extrator do cliente.
Garantir que o serviço/job responsável pela comunicação com MaxPag está em execução.
Após atualizar:
Repetir o teste de pagamento (se possível em ambiente de homologação) e monitorar novamente a MXSBAIXATITULOS.

Quando escalar para desenvolvimento
### Escalar para o time de desenvolvimento do MaxPedido / MaxPag quando:
Parâmetro ATIVAR_JOBMAXPAG_EXTRATOR está corretamente configurado (VALOR = 'S'),
Configuração do MaxPag foi validada conforme a base de conhecimento (token, credenciais, callbacks, etc.),
O extrator/atualizador do cliente está atualizado e em execução,
Mesmo assim:
Nenhum registro é gerado em MXSBAIXATITULOS para pagamentos confirmados no MaxPag; ou
Os registros aparecem em MXSBAIXATITULOS com STATUS = 0 e não evoluem, apesar de o título no ERP estar correto.
Nesses casos, abrir um ticket para o time de desenvolvimento responsável pelo MaxPedido / MaxPag, anexando:
prints da configuração,
exemplos de pagamentos,
SELECTs executados (MXSPARAMETRO e MXSBAIXATITULOS),
horário aproximado em que o pagamento foi realizado.

### TaEmRota
