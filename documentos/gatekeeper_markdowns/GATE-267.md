# GATE-267 - resumo de vendas não atualiza (T-Cloud)

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Henrique Torres Andrade [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Resumo de Vendas
- Natureza: Dúvida
- Atualizado em: 2024-11-04T14:31:17.615-0300

## Contexto do Problema

## Passos para reproduzir
>> Login: jotabe.maxima
>> Senha: asd123
>> Tentar atualizar o resumo de vendas

## Resultado apresentado
>> Resumo de vendas não atualiza

## Resultado esperado
>> Atualizar resumo de vendas

## Descrição
>> Verificado que o IP de acesso do cliente, no cadastro do extrator, estava como "https://armazemcruzeiro.extratormaxima.com.br", porém ao rodar a Pipeline de ler variáveis do Jenkins, verifiquei que o DNS correto seria o "https://jotabe.extratormaxima.com.br".
>> Após atualizar para o DNS correto, verificado que o resumo de vendas continuou sem atualizar
>> Creio que não seja bloqueio GEOLOCATION aos IPs dos EUA, pois o cliente agora é T-Cloud
>> Verificado que o hangfire está acessível normalmente (https://jotabe.extratormaxima.com.br/hangfire)

## Comentarios do Gatekeeper

### 1. 2024-11-04T14:14:12.102-0300 | Filipe do Amaral Padilha

Salvando dados:
USER_HANGFIRE=admin
PASS_HANGFIRE=Ozy1L4JM011HzDv+ImCPc6qp6xA=
USUARIO_EXTRATOR_NUVEM=jotabe.armazemcruzeiroproducao
SENHA_EXTRATOR_NUVEM=XC9D2SWJnGArIQ/iLhUE/UwtprTApXfQWDyNkTCyJRU=
USUARIO_SYSTEM_WINTHOR=MAXSOLUCOES
SENHA_SYSTEM_WINTHOR=y+TzuIH5WEzQTZ72nNZYopPDIuhY8vTLJFCpVgMfkgA=
SENHA_MAXSOLUCOES=y+TzuIH5WEzQTZ72nNZYopPDIuhY8vTLJFCpVgMfkgA=
LINK_API_WINTHOR_CANCELAMENTO=
USUARIO_API_WINTHOR_CANCELAMENTO=
SENHA_API_WINTHOR_CANCELAMENTO=
TZ=America/Sao_Paulo
VERSAO:dockermaxima/extrator:3.1.2.442
https://jotabe.extratormaxima.com.br/hangfire

### 2. 2024-11-04T14:31:17.613-0300 | Filipe do Amaral Padilha

O link correto de fato é o [https://jotabe.extratormaxima.com.br|https://jotabe.extratormaxima.com.br/]

As informações para atualização do menu no banco do cliente também estão corretas.

Eu fiz um teste com o usuário jotabe.maxima e assim que baixou a base eu testei a atualização e foi com sucesso:

!image-2024-11-04-14-28-26-030.png!

No caso só não vai atualizar o gráfico de vendas porque o usuário vinculado é o RCA 1 e ele não possui meta cadastrada (verifiquei tabelas PCMETA e PCMETARCA);

Isso aconteceu contigo porque após trocar o link de atualização no cadastro do extrator de "https://armazemcruzeiro.extratormaxima.com.br" para "https://jotabe.extratormaxima.com.br" para essa mudança surtir na apk, é necessário relogar no maxSoluções.

No caso, para resolver basta relogar no maxSoluções visto que você já resolveu ao alterar o link de atualização do menu para https://jotabe.extratormaxima.com.br

## Resposta Canonica

**Causa identificada**

O link de atualização configurado no cadastro do extrator estava incorreto e foi ajustado de `https://armazemcruzeiro.extratormaxima.com.br` para `https://jotabe.extratormaxima.com.br`. Após essa alteração, é necessário **relogar no maxSoluções** para que a mudança seja aplicada na APK.

Além disso, o **gráfico de vendas** não atualiza para o usuário vinculado porque ele está associado ao **RCA 1**, que **não possui meta cadastrada**, conforme verificado nas tabelas **PCMETA** e **PCMETARCA**.

**Evidências analisadas**

- O link correto de atualização é `https://jotabe.extratormaxima.com.br/`.
- As informações de atualização do menu no banco do cliente estão corretas.
- Em teste com o usuário `jotabe.maxima`, após baixar a base, a atualização ocorreu com sucesso.
- O Hangfire está acessível em `https://jotabe.extratormaxima.com.br/hangfire`.
- Foi validado que o usuário vinculado é o **RCA 1** e que não há meta cadastrada para ele.

**Ação recomendada**

1. Solicitar que o usuário **relogue no maxSoluções** para aplicar a troca do link de atualização na APK.
2. Manter o link de atualização do menu como `https://jotabe.extratormaxima.com.br`.
3. Caso seja necessário atualizar o gráfico de vendas, **cadastrar meta para o RCA 1**.

**Limitação**

Sem meta cadastrada para o **RCA 1**, o gráfico de vendas não será atualizado.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 404649, 404657
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
