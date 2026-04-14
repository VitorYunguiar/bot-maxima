# GATE-421 - Ineficiência do leitor de código de barras do maxPedido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não se Aplica
- Assunto: MXPED - Produto - Pesquisa
- Natureza: Dúvida
- Atualizado em: 2024-11-29T10:56:26.925-0300

## Contexto do Problema

## Passos para reproduzir
>>Usuario: 790.Ldf
>Acessar APK
>Clientes
>Iniciar pedido
>Aba tabela
>Configurações
>Editar método de pesquisa
>Código de barras
>Consultar código de barras em anexo

## Resultado apresentado
É possível notar uma ineficiência no processo de leitura: há demora e falta de precisão ao tentar escanear os códigos de barras.

## Resultado esperado
Uma leitura imediata tal qual apresentada pelos aplicativos gratuitos da PlayStore.

## Descrição
Boa tarde, Filipe/Carlos,

Estou enfrentando uma situação reportada pela LOJAO DUFERRO em relação ao desempenho do leitor de código de barras no aplicativo maxPedido. O cliente relatou uma notável ineficiência no processo de leitura: há demora e falta de precisão ao tentar escanear os códigos de barras.

O cliente apresentou o problema através de dois vídeos:
1. No maxPedido: Mostra a dificuldade em realizar a leitura mesmo com o leitor devidamente posicionado por um longo tempo.
2. Com outro aplicativo: Demonstra que a detecção é praticamente instantânea, sem a necessidade de posicionamento preciso ou prolongado da câmera.

Para validar o cenário, realizei testes com meu aparelho corporativo (Motorola G52) utilizando um produto disponível em minha casa, além de uma foto do mesmo item testado pelo RCA no vídeo. Os resultados confirmaram a dificuldade: o código de barras do produto testado só foi lido uma única vez em diversas tentativas. Outros produtos em minha casa puderam ser lidos, mas com certa dificuldade em alguns momentos.

Por outro lado, ao utilizar outros aplicativos com função similar, o problema não ocorre — a leitura é muito mais rápida e precisa.

DISPOSITIVOS UTILIZADOS

Motorola G52:
Câmera: 50 Mp + 8 Mp + 2 Mp
Resolução: 8165 x 6124 pixel
Versão maxPedido: 3.260.1

Lenovo Tab M9:
Câmera: 8 Mp
Resolução 3266 x 2449 pixel
Versão maxPedido: 3.249.2

## Comentarios do Gatekeeper

### 1. 2024-11-29T10:33:25.724-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 com todas as evidências para que a gente possa mostrar ao time de dev e eles ajudarem a pensar em possíveis soluções

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 409484
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Com base nas evidências relatadas' pressupõe evidências relatadas além do texto-fonte. | 'apresentação completa do cenário e dos testes já realizados' não consta no texto-fonte. | 'para apoio do time de desenvolvimento na análise' extrapola 'ajudarem a pensar em possíveis soluções'. | 'relato de demora e baixa precisão na leitura de código de barras no maxPedido' não consta no texto-fonte. | 'comparação prática com outros aplicativos, nos quais a leitura ocorreu de forma mais rápida e precisa' não consta no texto-fonte. | 'validação adicional em aparelhos diferentes, com reprodução da dificuldade de leitura no maxPedido' não consta no texto-fonte. | 'não há causa definida' não consta explicitamente no texto-fonte. | 'não há solução definida' não consta explicitamente no texto-fonte. | 'consolidar e apresentar todas as evidências já levantadas' só é parcialmente suportado; o texto-fonte menciona encaminhar com todas as evidências, mas não consolidar/apresentar como ação distinta. | 'para análise técnica junto ao desenvolvimento' extrapola o texto-fonte.
