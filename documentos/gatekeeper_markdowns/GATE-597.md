# GATE-597 - Falha na geocodificação de clientes no Roteirizador

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: ROTVENDN - Coordenadas - Cliente
- Natureza: Dúvida
- Atualizado em: 2025-01-08T12:52:03.867-0300

## Contexto do Problema

## Passos para reproduzir
>> acessar o roteirizador do cliente e buscar pela RCA NATALIA ALVES PEREIRA;
>> clicar em gerenciar coordenadas;
>> buscar pelo cliente 323943;
>> clicar em ações e observar o resultado.

## Resultado apresentado
está ocorrendo falha conforme o erro em anexo

## Resultado esperado
é esperado que não ocorra a exception e que possa gravar a geolocalização do cliente normalmente.

## Descrição
Senhores, ao realizar o fluxo de configuração da geolocalização, está ocorrendo o seguinte falha conforme abaixo:

!https://cdn.discordapp.com/attachments/1009929379322806302/1326514251959111765/image.png?ex=677fb42b&is=677e62ab&hm=f51057dd9fd77d5712c65fedd465f02d0b17365ca1efb51b37dbeda03cb09084&=!

!https://cdn.discordapp.com/attachments/1009929379322806302/1326514300763766804/image.png?ex=677fb436&is=677e62b6&hm=777f8917870ebfb3a88fd111f0670a8662c77c305324d7295a46233b44c2664c&=!

## Comentarios do Gatekeeper

### 1. 2025-01-08T12:35:16.816-0300 | Filipe do Amaral Padilha

Existiam dois registros ID 21052 e 21053 na tabela MXMP_LOCALIZACAO_CLIENTE_VENDA, com isso, na hora de realizar a busca das coordenadas do cliente, ocorria uma exceção no código.

O Roteirizador já conta na versão mais atualizada, com mecanismos para impedir que a localização do cliente seja gravada duas vezes na mesma tabela. Então provavelmente esse registro estava duplicado devido a uma versão antiga do Roteirizador que foi utilizada pela cliente e ainda possuía a falha.

Também foi verificado que o único registro duplicado era desse cliente 323943, nenhum outro registro estava duplicado que poderia causar o mesmo problema.

Para resolver foi feita normalização dos registros, deletando a duplicidade da tabela no banco de dados ORACLE.

Foi feito o teste no Roteirizador de vendedores no cenário informado e o erro não ocorreu novamente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 415641
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Ação recomendada: remover a duplicidade na tabela MXMP_LOCALIZACAO_CLIENTE_VENDA. | Ação recomendada: manter o cliente na versão mais atualizada do Roteirizador, que já possui mecanismo para impedir esse tipo de gravação duplicada. | Ação recomendada: acompanhar o comportamento após a normalização para validar se o cenário permanece estável.
