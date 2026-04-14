# GATE-626 - Comissões

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: PROTON
- Assunto: MXPED - Comissão
- Natureza: Dúvida
- Atualizado em: 2025-01-13T16:22:23.127-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Ticket sendo aberto para análise do fluxo de comissão.

Login para teste:

destak.rca

## Comentarios do Gatekeeper

### 1. 2025-01-13T16:20:28.325-0300 | Filipe do Amaral Padilha

Hoje eles usam 3.264.0 do maxPedido
Alguns na 3.256.2 e 3.242.1 do maxPedido

Trabalhar com comissão no maxPedido versão 3.268.3
Usuário que utilizamos: DESTAK.rca
Senha: asd123

Permissões do usuário ou perfil de usuários:
- Visualizar valor de comissão de venda: marcado [V]
- Orçamentos > Orçamentos efetuados > Ocultar Informações de Comissão: desmarcado []
- Pedidos > Pedidos efetuados > Ocultar Informações de Comissão: desmarcado []

Documentos que temos na base:
Permissões -> [https://basedeconhecimento.maximatech.com.br/pages/viewpage.action?pageId=105645845]
Parâmetro -> [https://basedeconhecimento.maximatech.com.br/pages/viewpage.action?pageId=105645836]

MXSFAIXACOMISSAOUSUR Calcular a comissão que é enviada aqui, na tela de negociação do maxPedido seria melhoria. Ele trabalha com o parâmetro HABILITA_FAIXA_COMISSAO = S.

Exemplo de POST
/api/v

{version}/FaixaComissaoVendedor
-> version = v1
[
\{ "codusur": "string", "numregiao": "string", "codprod": "string", "dtinicio": "2025-01-13T18:26:43.061Z", "dtfim": "2025-01-13T18:26:43.061Z", "faixa_ini_comissao": 0, "faixa_fim_comissao": 0, "comissao_padrao": 0, "hash": "string" }
]

Para cadastrar comissão percentual no produto e mostrar no campo customizado da tela 'Informações':

MXSPRODFILIAL.PCOMERP1, MXSPRODFILIAL.PCOMINT1 e MXSPRODFILIAL.PCOMEXT1

/api/v\{version}

/ProdutosFiliais
[

{ "codfilial": "string", "codprod": "string", "multiplo": 0, "qtminimaatacado": 0, "pcomrep1": 0, "pcomint1": 0,--Caso o vendedor seja do tipo "I" na MXSUSUARI "pcomext1": 0,--Caso o vendedor seja do tipo "E" na MXSUSUARI "qtmaxpedvenda": 0, "percmargemmin": 0, "qtminautoserv": 0, "calculaipi": "string", "hash": "string", "utilizaqtdesupmultipla": "string", "enviarforcavendas": "string", "checarmultiplovendabnf": "string", "proibidavenda": "string", "aceitavendafracao": "string", "permitirbrokertv5": "string" }

]

Comissão por RCA do botão "Comissões" da tela de negociação do maxPedido:
Endpoint MXSCOMISSAOUSUR parâmetro EXIBIR_SUGESTAO_PRECO_COMISSAO = S.

Exemplo: 91 3.1 5 5 FAIXA3-394.0 RP NULL NULL 394.0 P

/api/v

{version}

/ComissoesUsuarios
[

{ "codfaixa": "string", --FAIXA1-394.0 "percdescini": 0, --1 "percdescfim": 0, --5 "percom": 0, --5 "codusur": "string", --91 "codepto": "string", --NULL "codsec": "string", --NULL "codprod": "string", --394.0 "hash": "string", --NULL "tipo": "string", --P "tipocomissao": "string" --NULL }

]

Obs importante sobre o resumo de vendas:

A comissão prevista na tela inicial carrega conforme comissão retornada nos endpoints de histórico:

MXSHISTORICOPEDC.COMISSAO --na venda sem apuração por nota fiscal do resumo de vendas

Se for com apuração por nota fiscal dai seria na ERP_MXSNFSAID.COMISSAO

—

Outra informação importante:
Se usar a tabela MXSCOMISSAOUSUR e MXSPRODFILIAL, funciona o cálculo previsto de comissão no final do pedido e inclusive, os dois também mexem na comissão apresentada do produto nos campos customizados.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 416563
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Foi identificada necessidade de análise do fluxo de comissão no maxPedido. | a análise deve ser realizada na versão 3.268.3; | o usuário de validação é `DESTAK.rca`. | Configurações já verificadas: | Comportamento atual identificado: | Pontos de validação: | Limitação identificada: | o cálculo da comissão enviada via `MXSFAIXACOMISSAOUSUR` na tela de negociação do maxPedido não está caracterizado como comportamento atual e deve ser tratado como melhoria. | Próximo passo: | realizar a análise do fluxo de comissão no maxPedido 3.268.3 com o usuário `DESTAK.rca`, validando permissões, parâmetros e o comportamento dos endpoints e tabelas citados.
