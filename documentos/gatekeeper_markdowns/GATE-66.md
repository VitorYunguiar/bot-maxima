# GATE-66 - Alterar cod.fábrica pela MARCA do produto na tela de pedido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXPED - Parametrização
- Natureza: Dúvida
- Atualizado em: 2024-09-16T15:53:40.226-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar maxPedido >> Iniciar pedido ou pesquisar produto >> Listagem de produto .

## Resultado apresentado
>> Ao habilitar parametro LIST_PROD_FIELD_MARCA, o cod.Fabricante será alterado para MARCA.

## Resultado esperado
>> Ao habilitar parametro LIST_PROD_FIELD_MARCA, o cod.Fabricante será alterado para MARCA.

## Descrição
Cliente- Queremos alterar a informação cod.fábrica pela marca do produto na tela de pedido

----------------------------------------
Foi hablitado paremetro  LIST_PROD_FIELD_MARCA (Exibe o campo Marca na Listagem de Produtos)

## Comentarios do Gatekeeper

### 1. 2024-09-16T15:53:40.224-0300 | Filipe do Amaral Padilha

Realizando a leitura da demanda, compreendi que o cliente deseja trocar a informação que é apresentada no maxPedido, na listagem de produtos. No caso, ele quer trocar o Código de fábrica dos produtos pela descrição da marca dos produtos.

Para obter esse comportamento, ele pode estar desabilitando o parâmetro HABILITAR_VISUALIZACAO_COD_FAB_PROD_TAB = N, isso vai ocultar o código de fábrica dos produtos na listagem.

E habilitar o LIST_PROD_FIELD_MARCA, que vai exibir o campo da Marca do produto caso esteja cadastrado.

## Resposta Canonica

Para atender ao cenário descrito no maxPedido, a configuração deve ser feita por parâmetros.

Análise do comportamento:
- O objetivo é substituir a informação exibida na listagem de produtos, trocando o **Código de fábrica** pela **descrição da marca**.
- O parâmetro `LIST_PROD_FIELD_MARCA` **exibe o campo Marca** na listagem de produtos, desde que a marca esteja cadastrada.
- Para **ocultar o Código de fábrica**, é necessário desabilitar sua visualização com o parâmetro `HABILITAR_VISUALIZACAO_COD_FAB_PROD_TAB = N`.

Configuração recomendada:
- Definir `HABILITAR_VISUALIZACAO_COD_FAB_PROD_TAB = N`
- Habilitar `LIST_PROD_FIELD_MARCA`

Limitação:
- A marca do produto será exibida apenas se estiver cadastrada.

Próximo passo:
- Configurar os parâmetros indicados e validar na listagem de produtos do maxPedido se o código de fábrica foi ocultado e a marca passou a ser exibida.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 394878
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
