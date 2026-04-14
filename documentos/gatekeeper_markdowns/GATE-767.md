# GATE-767 - Importação do Mix ideal barra produtos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: SAP
- Assunto: MXPED - Central de Configurações
- Natureza: Dúvida
- Atualizado em: 2025-02-10T10:16:58.810-0300

## Contexto do Problema

## Passos para reproduzir
>> Abrir mix ideal;
>> Tentar importar produtos;
>> Em seguida inserir manualmente produtos que foram barrados na importação.

## Resultado apresentado
erro informando que "itens não foram importados pois não existem na base ou não satisfazem as parametrizações de venda por embalagem"

## Resultado esperado
Importação ocorrendo com sucesso.

## Descrição
Ao tentar inserir produtos na edição do mix ideal pela função de importação de excel, é exibido um erro informando que "itens não foram importados pois não existem na base ou não satisfazem as parametrizações de venda por embalagem", porem é possível inserir esses itens manualmente sem nenhum impeditivo.

Tabela em anexo.

## Comentarios do Gatekeeper

### 1. 2025-02-10T10:16:58.808-0300 | Filipe do Amaral Padilha

Na planilha tem vários CODAUXILIAR associados a produtos que não existem no nosso banco nuvem.

Por exemplo, o produto 1930243014 possui as três embalagens cujos CODAXILIAR são da FILIAL DE06:

17509546695386
2050001915573
2050001915535

Quando é inserido via Central selecionado específico o codprod, então a gente carrega as embalagens conforme a filial selecionada, por isso dá certo. A gente carrega no caso as três embalagens que existem ativas na nuvem:

17509546695386
2050001915573
2050001915535

Pra validar:
--O retorno será somente os produtos com CODAUXILIAR cadastrado na DE06
SELECT * FROM MXSEMBALAGEM WHERE CODAUXILIAR IN(7891024134702,
7891024033715,
7509546656861,
7793100111143,
7509546684789,
7891024025017,
7891024132371,
7509546669953,
7891528038001,
7891528028132,
7891024026434,
7891024184509,
7501033205293,
7891024029886,
7891024136409,
7891024174715,
7891024174210,
7891024110300,
7891024182475,
7891024035139,
7891024027325,
7891024194102,
7891024194607,
7891024120705,
7891024128305,
7793100111143,
7509546684789,
7891024025017,
7509546684048,
7891024135020,
7891024135310,
7509546686042,
7509546688091,
7509546695389,
7891024110409) AND CODFILIAL IN('DE06') AND CODOPERACAO <> 2;

--Select só para vc ver que é o mesmo número que a central retorna, ou seja de 35, somente 14 são encontrados, ficando 21 que não passam na validação.
SELECT 35 - 14 FROM DUAL;

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 422616
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Isso explica a mensagem exibida na importação." | "Próximo passo: executar essas consultas para identificar exatamente os 21 CODAUXILIAR da planilha que não existem ou não atendem à parametrização válida para a filial DE06."
