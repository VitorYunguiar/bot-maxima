# GATE-242 - supervisor auto serviço não aparece e diverência de valores

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXGESN - Dashboard
- Natureza: Dúvida
- Atualizado em: 2024-10-30T15:11:51.918-0300

## Contexto do Problema

## Passos para reproduzir
>>Verificar no maxGestao onde o supervisor "auto serviço" não aparece
>>Verificar no banco os seguintes selects, onde não retornam nada:
(SELECT * FROM MXSHISTORICOPEDC WHERE ORIGEMPED IN('A') AND TRUNC(DATA) BETWEEN TO_DATE('01/10/2024','DD/MM/YYYY') AND TO_DATE('28/10/2024','DD/MM/YYYY') AND POSICAO <> 'C';

SELECT * FROM MXSPARAMETRO WHERE NOME LIKE '%ENVIA_PEDIDOS_AUTOSERVICO%';)

>>O supervisor "Auto Serviço" não aparece.

>>O supervisor deve aparecer no maxgestao e o valor entre o Winthor e o maxGesta deve bater.

## Descrição
>> O campo "Auto serviço" não aparece no maxGestao, nem nos selects via banco

TeamViewer ID: 140 169 544
Sua senha: s3asaqer

## Comentarios do Gatekeeper

### 1. 2024-10-30T15:11:51.916-0300 | Filipe do Amaral Padilha

O motivo de os valores estarem divergentes inicialmente era devido aos pedidos de origem 'A' não estarem sendo integrados ao banco de dados nuvem para a Filial 4.

Então considerando esse cenário, foi realizada conexão no ambiente do cliente, feita configuração para importar pedidos de origem 'A' Auto_servico e também feita a carga de todas as tabelas necessárias para gerar o histórico e apuração no maxGestão.

No momento dia 30/10/2024 essa carga ainda não foi finalizada, provavelmente vai finalizar entre hoje no final do dia 18h e amanhã. Provavelmente de manhã já vai ter finalizado.

Então sob esse contexto, eu acredito que amanhã o cliente possa validar no maxGestão se os dados estão próximos do que ele tem na Rotina 146 do Winthor seguindo os filtros que ele colocou.

Ocorre também que não necessariamente vai bater os dados com a Rotina 146 porque no Winthor os dados são apurados conforme o histórico de capas dos pedidos e no maxGestão nós trazemos uma informação dos históricos dos itens dos pedidos vendidos. Então se o cliente tiver uma divergência entre o valor vendido que fica guardado nas capas dos pedidos em relação aos itens, terá uma pequena diferença de valores e isso é considerado normal.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, grounding_failed, needs_review
- Comentarios primarios: 403936
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Por esse motivo, o supervisor Auto Serviço não aparecia no maxGestão e também não havia retorno nas consultas relacionadas."
