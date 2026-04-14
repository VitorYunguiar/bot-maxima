# GATE-341 - Política não funciona na base do RCA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - Política de Desconto - Comercial
- Natureza: Dúvida
- Atualizado em: 2024-11-14T17:46:06.810-0300

## Contexto do Problema

## Passos para reproduzir
>>abreu.263
>Acessar APK
>Importar base
>Iniciar pedido como balcão reserva (usei o cliente 28505)
>Alterar filial para 3
>Alterar plano de pagamento para 301
>Aba tabela
>Consultar algum produto (usei o 27948)
>Observar que ele carrega apenas a política 1262649, enquanto a 1420314 não é aplicada, e deveria ser automaticamente.

## Resultado apresentado
Nesse RCA 263, a política 1420314 não está aplicando no maxPedido, mesmo ela estando na MXSDESCONTO da base do RCA.

## Resultado esperado
Identificar o que está impedindo a política de funcionar na base do vendedor e realizar carga para corrigir.

## Descrição
!BASE DO 0.png|thumbnail!  !BASE DO 0(1).PNG|thumbnail!  [^263_3.252.0_14-11-2024.zip] Boa tarde Carlos/Filipe,

Estou com um cenário na ABREU & SILVA onde 2 políticas de desconto não funcionam para alguns RCAs, na base do 0 o problema não acontece.

Verifiquei via inspect que na base do RCA ele baixou a política, porém algo impede o mesmo de usar, já que ela não aplica automaticamente o desconto igual faz na base do 0 e na 316.

Políticas: 1262649 e 1420314
RCAs: 311 e 263

Até o momento consegui a base do RCA 263, sigo aguardando a base do outro representante.

## Comentarios do Gatekeeper

### 1. 2024-11-14T17:12:40.637-0300 | Filipe do Amaral Padilha

Enviado para N3 para averiguarem a possível divergência de registros e corrigirem

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 407138
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "na base do RCA" | "o que pode estar impedindo a aplicação automática da política 1420314, apesar de constar na base" | "Responsável: N3" | "Próximo passo: N3 deve analisar a divergência de registros e efetuar a correção necessária"
