# GATE-758 - Itens do carregamento pronta entrega não aparecem no aplicativo

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2025-02-07T12:58:22.202-0300

## Contexto do Problema

## Passos para reproduzir
>>baixar base do zero ou base em anexo
>>Abrir a aba'Consultas' e depois 'Venda pronta entrega'

## Resultado apresentado
>>Aparece na tela o carregamento 152743 porém não aparece nenhum item para ser incluído

## Resultado esperado
>>Os itens devem aparecer para serem vendidos

## Descrição
>>Verificado que ao entrar no carregamento do pronta entrega os itens do carregamento 152743 não aparecem para o RCA

Tabelas que verifiquei:

ERP_MXSMOV e PCMOV> Ambas possuem registros do carregamento 152743

ERP_MXSCARREG e PCCARREG > Na PCCARREG aparecem registros para o carregamento, porém na ERP_MXSMOV não aparece nenhum registro o que pode ser a causa da divergência

MXSESTMANIF> Não possui registros para esse usuario

## Comentarios do Gatekeeper

### 1. 2025-02-07T12:58:22.200-0300 | Filipe do Amaral Padilha

O processo de Prontra Entrega com o maxPedido considera vendas do tipo CONDVENDA = 13 na MXSHISTORICOPEDC e ERP_MXSNFSAID.

Além disso, a gente utiliza da informação da tabela ERP_MXSCARREG para gerar o estoque no maxPedido.

No caso do cliente, exisitia uma divergência de banco de dados, onde a PCCARREG possuia o número do carregamento, porém ele não desceu para o nosso banco nuvem.

Para resolver eu fiz uma carga de vários registros dessa tabela PCCARREG para elas descerem para o nosso banco nuvem.

Durante a análise não identifiquei problemas com os objetos do banco de dados e nem logs de erros.

Pode ter ocorrido algum problema com os registros, para a nossa trigger não ter pego de forma automática os dados, porém não conseguimos identificar. Como expliquei, foi feita então essa descida manual dos registros.

Nesse sentido, eu recomendo acompanhar para caso ocorra outra situação dessas, a gente encaminhar para outra equipe da Máxima que pode aprofundar a análise.

Para o RCA receber o carregamento no aparelho, basta realizar uma sincronização parcial (apertar para sincronizar o maxPedido, que os produtos serão exibidos).

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 422361
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que a ausência do dado no banco nuvem 'impediu a exibição dos itens no carregamento 152743 para o RCA' não está totalmente suportada, pois o texto-fonte não menciona o carregamento 152743 nem estabelece explicitamente essa relação causal específica. | A afirmação de que 'não foi possível determinar com exatidão por que a trigger não capturou os dados automaticamente' extrapola o texto-fonte, que diz apenas que 'pode ter ocorrido algum problema com os registros, para a nossa trigger não ter pego de forma automática os dados, porém não conseguimos identificar'. Isso é semelhante, mas não afirma exatamente a mesma formulação conclusiva.
