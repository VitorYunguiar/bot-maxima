# GATE-230 - Produto não aparece

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Dúvida
- Atualizado em: 2024-10-25T11:01:19.382-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Iniciar um pedido em qualquer cliente ou ir no card de produtos na tela inicial
>>Procurar pelo item 92656
>>E o mesmo não aparece

Login: petropolis.956
senha: acesso temporário

## Resultado apresentado
Produto 92656 não aparece ao RCA

## Resultado esperado
Que o produto 92656 apareça ao RCA.

## Descrição
O produto 92656 não aparece ao RCA 956, o mesmo não aparece somente a esse vendedor e pelo que analisei as tabela principais estão ok.

## Comentarios do Gatekeeper

### 1. 2024-10-25T11:01:10.333-0300 | Filipe do Amaral Padilha

O produto não aparece em alguns casos devido a região selecionada de precificação, conforme vou explicar abaixo:

SELECT PVENDA1,PTABELA,CODOPERACAO,CODPROD,NUMREGIAO FROM MXSTABPR WHERE CODPROD IN(92656) AND NUMREGIAO IN(2, 3, 1, 10, 11, 6, 8, 12, 15);

--O RCA tem acesso às regiões

--2, 3, 1, 10, 11, 6, 8, 12, 15

--Ele só vai conseguir vender para clientes das regiões:

--2, 12, 6, 8, 10, 11, 1

--Porque só nelas o produto está precificado

Então por exemplo, ele aparece para o cliente 833952 e buscando no card de produtos pelo código dele na região 1. Se o cliente quiser que ele apareça para outros clientes de outras regiões, bem como no card de produtos de outras regiões, ele vai precisar precificar esse produto nessas regiões específicas.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 403067
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que o problema ocorre especificamente para o "RCA 956" não está no texto-fonte. O texto menciona apenas "O RCA", sem identificar código/número. | A conclusão "Não se trata de falha de exibição do RCA" não está explicitamente afirmada no texto-fonte. | A indicação "Responsável pela ação: Cliente" não consta no texto-fonte.
