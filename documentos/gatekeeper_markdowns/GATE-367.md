# GATE-367 - Divergencia de comportamento entre base do zero e base do app da RCA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Política de Desconto - Comercial
- Natureza: N/A
- Atualizado em: 2024-11-22T14:37:11.168-0300

## Contexto do Problema

## Passos para reproduzir
efetuar o login na aplicação com o login gtdist.509;
iniciar a negociação para o cliente 29;
tentar negociar os produtos conforme o print na descrição e no video;
comparar os resultados.

## Resultado apresentado
é apresentado divergencia de comportamento entre as bases do zero e base de rca

## Resultado esperado
que assim que o cliente sincronize o seu aparelho, ele consiga negociar sem falhas o produto.

## Descrição
senhores, ao realizar a analise sobre a demanda citada, enquanto em base do zero a negociação ocorre de forma regular:
!image-2024-11-22-08-18-40-579.png!

Na base do RCA mesmo sincronizando acontece essa situação mesmo sincronizando o app:

!image-2024-11-22-08-19-14-083.png!

## Comentarios do Gatekeeper

### 1. 2024-11-22T13:49:28.948-0300 | Filipe do Amaral Padilha

Como ele renovou a política hoje no diaComo ele renovou a política hoje no dia

--2024-11-22 09:05:30.000

--2024-11-22 09:05:30.000

Quando o RCA sincronizar vai descer normalmente, eu testei na base dele sincronizando e desceu.
Dai para garantir que ele sincronize e desça também, eu fiz a carga mesmo assim, o que atualizou para

--2024-11-22 12:23:01.000

--2024-11-22 12:23:01.000

Então para resolver o RCA só precisa sincronizar e atualizar a versão do aplicativo, vou explicar abaixo como eu analisei.

Analisei as bases que rastreei conforme a dica que você deu de atualização ontem 21/11 às 18:55:

[http://maxsolucoes-venda.s3.amazonaws.com/BaseDados/1954/9879/Patch_98006_000_000001_20241121185552_211120240655528484.s3db.gz]

[http://maxsolucoes-venda.s3.amazonaws.com/BaseDados/1954/9879/Patch_98006_000_000001_20241121185048_211120240650484232.s3db.gz]

E rastreei as políticas anteriores que foram cadastradas pelo cliente nos códigos

72025: 2024-11-22 09:02:26.000

72024: 2024-11-21 18:55:08.000

72019: 2024-11-21 18:55:28.000

A última data de atualização delas foi essa acima ao lado dos códigos e foi um comando de deleção dessas políticas, de forma que inativasse ou não enviasse ao força de vendas.

E nesse aspecto o aplicativo se comportou corretamente, baixando as informações conforme o RCA sincronizava.

O que pode ter ocorrido é o seguinte, antes o RCA estava na versão 3.220.8, ontem mesmo 21/11/2024 às 18:50.

Nesse horário a política 72025 estava na base dele, que é a política que validaria a questão dos descontos. Porém nessa versão, não tem a correção que valida políticas cadastradas dessa forma dtini e dtfim estarem 2024-11-21 00:00:00; (Horário totalmente 00:00:00)

Por isso que ao trocar de versão na ponta deu certo e na do RCA não.

Então não é um problema de sincronização de dados e sim da versão, que ao atualizar já resolve o problema de validar a política

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 408202
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "sob responsabilidade do RCA" | "para que a política seja validada corretamente e a negociação para o cliente 29, com o login gtdist.509, ocorra sem falha"
