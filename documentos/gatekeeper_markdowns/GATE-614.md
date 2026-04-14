# GATE-614 - Integradora rejeitando pedido pois estamos gravando um CODAUXILIAR errado

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor Cloud
- Assunto: MXPED - Produto - Embalagem
- Natureza: N/A
- Atualizado em: 2025-01-10T15:32:11.040-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Iniciar um pedido no cliente 34503
>>Ir na aba tabela e procurar pelo item 29825
>>Adicionar o mesmo ao pedido
>>Salvar e enviar o pedido
>>E assim a integradora irá rejeitar o pedido informando que o preço de tabela está zerado e o CODAUXILIAR não existe no winthor

OBS: CONSTATEI SOMENTE ISSO QUE ESTAMOS MANDANDO ERRADO

Login: jfrios.jeconias
senha: acesso temporário

## Resultado apresentado
Integradora rejeitando pedido devido estarmos enviando o CODAUXILIAR da embalagem que não existe no winthor

## Resultado esperado
Que a gente envia o CODAUXILIAR correto e a integradora aceite o pedido

## Descrição
Ao tentar realizar pedidos pelo MaxPedido com o item 29825 a integradora está rejeitando os pedidos pois estamos gravando na PCPEDIFV o CODAUXILIAR 10061 que não existe na PCEMBALAGEM, esse CODAUXILIAR existe somente na nossa tabela do banco nuvem MXSEMBALAGEM.

Logo vê-se que está tendo divergência entre as tabelas PCEMABALAGEM  e MXSEMBALAGEM.

Foi realizado de teste o pedido 62255039.

Constatei somente o CODAUXILIAR que estamos mandando errado sobre o preço não constatei nada.

Dados para conectar no banco T-CLOUD do cliente
Schema: MAXSOLUCOES
senha: 3bRSjdMvmEhWR8FH5xu1
Service name: CR0V85_124364_W_high.paas.oracle.com
Host: 181.41.189.71

## Comentarios do Gatekeeper

### 1. 2025-01-10T15:30:58.609-0300 | Filipe do Amaral Padilha

Foi feita normalização do produto 29825 e dos demais registros da filial 2, onde foi detectado o problema.

Não foi possível identificar a causa exata da divergência, por esse motivo foram adicionados logs no cliente na trigger das embalagens para que caso ocorra algum problema semelhante novamente, possamos ter mais informações para análise.

Os logs na trigger não foram colocados no atualizador do banco nuvem. Então caso o cliente seja atualizado, vai perder os logs que foram colocados diretamente no ambiente do cliente (no caso, vai parar de gerar log).

Para validar os RCAs podem estar sincronizando o maxPedido. A embalagem errada foi excluída, para transmitir o pedido corretamente o RCA deve sincronizar, remover o item do pedido caso esteja a embalagem ainda errada, e inserir novamente antes de transmitir o pedido.

No caso eu vou todos os dias excluir os logs para que novos sejam gerados sem comprometer o espaço do banco, essa trigger gera muitos logs então não dá para deixar virar mais de um dia gerando logs.

Quando o cliente ou suporte identificarem o problema novamente, se tivermos sorte, vamos conseguir analisar os logs criados.

## Resposta Canonica

Foi identificada inconsistência de embalagem no produto **29825**, também observada em **demais registros da filial 2**. A **embalagem incorreta foi excluída**, porém **não foi possível determinar a causa exata da divergência**.

Como ação de diagnóstico, foram **adicionados logs na trigger de embalagens no ambiente do cliente** para capturar informações caso o problema volte a ocorrer. Esses logs têm caráter temporário, pois:

- **geram grande volume de registros**;
- **não foram incluídos no atualizador do banco nuvem**;
- **podem ser perdidos em caso de atualização do cliente**;
- por volume, **não devem permanecer ativos por mais de um dia**.

### Orientação para validação
Para testar e contornar o cenário atual:

1. solicitar que os **RCAs sincronizem o MaxPedido**;
2. **remover o item do pedido** se ainda estiver com a embalagem incorreta;
3. **inserir o item novamente** antes de transmitir o pedido.

### Próximo passo
Se o problema voltar a ocorrer, será necessário **analisar os logs gerados** para tentar identificar a origem da divergência.

### Observação operacional
Foi informado que os **logs serão excluídos diariamente** para permitir novas coletas sem comprometer o espaço do banco.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 416281
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
