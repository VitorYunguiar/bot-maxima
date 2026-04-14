# GATE-429 - Incluir itens nas familias já criadas no Desconto Progressivo

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não se Aplica
- Assunto: MXPED - Campanha - Desconto Progressivo
- Natureza: Dúvida
- Atualizado em: 2024-12-03T10:01:32.771-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/AAnteriormente, era possível usar o botão "Importar Produtos via XLS" sem a necessidade de selecionar uma filial. No entanto, com a alteração no comportamento do sistema, agora é obrigatório marcar uma filial para realizar essa importação.

Por conta dessa mudança, as famílias de produtos criadas antes dessa atualização não estão permitindo a adição de novos produtos.

## Resultado esperado
Gostaria de saber se seria possível, ao menos, incluir esses produtos diretamente via banco de dados enquanto não sai a melhoria de inserir produtos sem filiais.

## Descrição
Boa tarde Carlos/Filipe,

Na Destro, há diversos cadastros antigos de famílias de produtos criadas para serem utilizadas em conjunto com a campanha de desconto progressivo.

## Comentarios do Gatekeeper

### 1. 2024-12-03T10:01:32.768-0300 | Filipe do Amaral Padilha

--Foi feita a inclusão dos itens nas famílias conforme o print anexado. Para conferir você pode consultar no banco nuvem ambiente de produção da Destro:

SELECT * FROM MXSFAMILIAITENS WHERE CODIGOFAMILIA IN (46) AND CODPROD IN(1965054);--itens da familia --7500435154420
SELECT * FROM MXSFAMILIAITENS WHERE CODIGOFAMILIA IN (39) AND CODPROD IN(1965225);--itens da familia --7500435240512
SELECT * FROM MXSFAMILIAITENS WHERE CODIGOFAMILIA IN (40) AND CODPROD IN(1965223);--itens da familia --7500435170024
SELECT * FROM MXSFAMILIAITENS WHERE CODIGOFAMILIA IN (22) AND CODPROD IN(1965220);--itens da familia --7500435243841
SELECT * FROM MXSFAMILIAITENS WHERE CODIGOFAMILIA IN (22) AND CODPROD IN(1965221);--itens da familia --7500435243834
SELECT * FROM MXSFAMILIAITENS WHERE CODIGOFAMILIA IN (920) AND CODPROD IN(1930243014);--itens da familia --7509546695389

Para o cliente conferir, pode estar olhando diretamente via central no cadastro das famílias.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409981
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Próximo passo: o cliente deve validar essas inclusões no banco de produção da Destro ou via Central no cadastro das famílias." — o texto-fonte diz que o cliente pode conferir diretamente via central no cadastro das famílias, mas não afirma como 'próximo passo' nem que deve validar no banco de produção da Destro.
