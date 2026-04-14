# GATE-565 - Layout de impressão, drivers não funcionam

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: João Pedro Faria Cabral [X]
- ERP do cliente: Sankhya
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Erro
- Atualizado em: 2025-01-02T10:25:14.224-0300

## Contexto do Problema

## Passos para reproduzir
"não está trazendo informações de pedidos"

Ao solicitar para trocar o driver o cliente informou que testou em todos e nenhum imprimiu corretamente

O cliente utilizava a impressora " A7 ", e mudou para a "Leopardo XR" que tem suas especificaçoes citadas na sessão de DESCRIÇÃO, deste chamado.

## Resultado apresentado
Alguns dados não são exibidos em tickets impressos recentemente, como a sessão de DADOS DOS PRODUTOS (anexos)

## Resultado esperado
Identificar o problema

## Descrição
Impressora Portátil Térmica Leopardo XR.

ESPECIFICAÇÕES IMPRESSÃO.
Método de impressão: Térmica Direta
Tipo de Mídia: Papel térmico, Papel térmico personalizado com Blackma
Largura do papel: 80 mm
Largura de impressão: 72 mm
Resolução: 8 pontos/mm (203 dpi)
Pontos/Linha: 576 pontos
Velocidade de impressão: Até 90 mm/seg
Linguagem de Programação: ESC/POS
Códigos de Barras: UPC-A, EAN13, EAN8, CODE 39, ITF, CODABAR, CODE39, CODE128 E QRCODE
Vida Ú_l Cabeça de Impressão: 50 KM

ESPECIFICAÇÕES FÍSICAS.
Grau de Proteção: IP42 sem capa
Resistência: Queda 1,20 metros / Opcional: Capa com resistência até 1,50 metros
Dimensão Externa: 125 X 100 X 50 mm
Peso: 360 gramas (com bateria)
Diâmetro da Bobina: Até 50 mm
Interface: USB / Bluetooth
Bateria: Bateria de Lí_o 1.800 mAh 7.4 V (*)
Sistemas: Android, Windows.
Tempo de carga completa: 3-4 horas
ESPECIFICAÇÕES DO AMBIENTE.
Temperatura de operação: -10°C 50°C
Umidade de operação: 20% 85% RH
Temperatura de armazenam/o: -20°C 70°C
Umidade de armazenamento: 5% 95% RH

OUTRAS ESPECIFICAÇÕES
Garantia: 18 (dezoito) Meses
Acessórios:
Fonte de Alimentação 110/220 V
Cabo USB
Carregador Veicular 12V
Bobina de Papel e Manual.

## Comentarios do Gatekeeper

### 1. 2025-01-02T10:25:14.223-0300 | Filipe do Amaral Padilha

Verifiquei os dados que foram anexados e precisamos te devolver o ticket, para que o cliente nos ajude com mais algumas informações importantes para a análise:

>> Precisamos saber o método de impressão que foi utilizado, por exemplo, se foi impressão de nota fiscal, se foi nota de contigência, se foi boleto, etc...

>> Precisamos do login do RCA, para que a gente possa simular também o problema no desenvolvimento usando uma impressora com o mesmo modelo.

>> Precisamos da base do RCA, que constam os dados dos pedidos na timeline onde foi feita a tentativa de geração do arquivo via mini impressora;

>> Precisamos saber dados sobre o(s) pedido(s) (NUMPED e NUMPEDRCA) que foram feitas as tentativas de impressão dos dados, para que possamos conferir se os dados estão sendo enviados via integração corretamente.

## Resposta Canonica

Até o momento, não foi possível identificar a causa do problema de ausência de informações dos pedidos nos tickets impressos.

A análise textual dos dados informados e dos materiais enviados indica que as evidências atuais são insuficientes para concluir a origem da falha. Para continuidade, é necessário complementar as informações abaixo:

- método de impressão utilizado na tentativa, por exemplo: nota fiscal, nota de contingência, boleto, etc.;
- login do RCA, para simulação do problema em desenvolvimento com impressora do mesmo modelo;
- base do RCA em que constam os dados dos pedidos na timeline da tentativa de geração do arquivo via mini impressora;
- dados dos pedidos das tentativas de impressão, incluindo **NUMPED** e **NUMPEDRCA**, para validação do envio via integração.

Limitações da análise atual:
- sem o método de impressão, não é possível avançar na análise;
- sem o login do RCA, não é possível simular o problema;
- sem a base do RCA, não é possível verificar os dados dos pedidos na timeline da tentativa;
- sem **NUMPED** e **NUMPEDRCA**, não é possível conferir se os dados estão sendo enviados corretamente via integração.

Próximo passo:
devolver o ticket ao cliente e solicitar as informações complementares para continuidade da análise.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 414471
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
