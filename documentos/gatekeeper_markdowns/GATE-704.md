# GATE-704 - Pedidos não estão sendo enviados para a nuvem da Máxima (V3 e V4)

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Henrique Torres Andrade [X]
- ERP do cliente: Sankhya
- Assunto: MXPED - Integração - API Máxima
- Natureza: Dúvida
- Atualizado em: 2025-01-28T15:45:45.436-0300

## Contexto do Problema

## Passos para reproduzir
>> Login: FRICO.CLEIDVALDO
>> Acessar a timeline de pedidos
>> Observar os pedidos 1658 e 1659
>> Realizar Swipe

## Resultado apresentado
>> Os pedidos não estão sendo enviados para o banco nuvem

## Resultado esperado
>> Pedidos serem enviados para a nuvem

## Descrição
>> Cliente informa que vários RCAs estão passando pedidos, e alguns pedidos simplesmente não são enviados para a nuvem, mesmo com o ato do "Swipe"
>> Foi passado uma base como exemplo, e mesmo importando a base no meu aparelho e fazendo swipe, os pedidos não foram enviados
>> Realizado teste na versão ponta da V3 e também na ponta da V4, e mesmo assim os pedidos não foram enviados

## Comentarios do Gatekeeper

### 1. 2025-01-28T15:45:45.434-0300 | Filipe do Amaral Padilha

--O cliente Fricó utiliza o maxSync

E estava na versão antiga que ainda não havia passado pelas correções da sinc automática. Inclusive, usar a base do cliente com a versão antiga do maxPedido causa problemas de sincronismo dos dados.

SELECT * FROM MXSUSUARIOS WHERE CODUSUR IN(127);
--Está com a opção marcada USAMSGMAXSYNC = S

Nesse caso, por estar usando versão antiga com o maxSync, o que houve foi um problema com os registros dos pedidos, que já foram enviados para a nuvem e processados, porém não ocorreu o retorno correto via sinc automática para a base do RCA.

Para resolver eu atualizei a versão do bd nuvem e do maxPedido e reprocessei somente os pedidos em específico 1658 e 1659.

Foi também habilitado o parâmetro HABILITA_SYNC_AUTOMATICA = S por usuário somente nesse RCA.

O problema foi causado por utilizar o fluxo de sync automática ativo no usuário, sem o parâmetro estar ativo.

E a correção se deu reenviando os dados do pedido e utilizando sync automática.

Se por acaso não quiserem mais usar sync automática nesse RCA, deve ser desfeito, o parâmetro HABILITA_SYNC_AUTOMATICA = N e o USAMSGMAXSYNC = N na MXSUSUARI (Suporte deve fazer).

O RCA deve migrar para a versão mais recente do maxPedido e sincronizar assim terá os status atualizados automaticamente, o sincronismo será somente para pegar os parâmetros e configurações alteradas.

Outra opção como expliquei, fica na versão antiga, desfaz as configurações do maxSync e sincroniza.

## Resposta Canonica

**Causa identificada**  
O problema ocorre pelo uso de versão antiga do maxPedido em conjunto com maxSync/fluxo de sincronização automática ativo no usuário, sem o parâmetro `HABILITA_SYNC_AUTOMATICA` habilitado. Nesse cenário, o retorno da sincronização automática para a base do RCA não ocorre corretamente.

**Análise objetiva**  
- O cliente Fricó utiliza o maxSync.  
- A versão em uso era antiga e ainda não continha as correções da sincronização automática.  
- Com a base do cliente nessa versão antiga do maxPedido, foram observados problemas de sincronismo dos dados.  
- Para o `CODUSUR 127`, na tabela `MXSUSUARIOS`, a opção `USAMSGMAXSYNC` estava marcada como `S`.  
- Os pedidos **1658** e **1659** já foram enviados para a nuvem e processados, porém o retorno correto via sincronização automática não aconteceu na base do RCA.

```sql
SELECT * FROM MXSUSUARIOS WHERE CODUSUR IN(127);
```

**Ação recomendada**  
- Atualizar a versão do BD nuvem e do maxPedido.  
- Reprocessar os pedidos **1658** e **1659**.  
- Habilitar `HABILITA_SYNC_AUTOMATICA = S` por usuário nesse RCA.  
- Se não houver interesse em manter a sync automática nesse RCA, desfazer a configuração com:
  - `HABILITA_SYNC_AUTOMATICA = N`
  - `USAMSGMAXSYNC = N` na `MXSUSUARIOS`  
- Como próximo passo, migrar o RCA para a versão mais recente do maxPedido e sincronizar para obter os status atualizados automaticamente. Como alternativa, permanecer na versão antiga e desfazer as configurações do maxSync.

**Responsável**  
- Suporte deve realizar o ajuste.

**Limitação informada**  
- O parâmetro `HABILITA_SYNC_AUTOMATICA = S` foi habilitado por usuário somente nesse RCA.  
- O sincronismo será apenas para buscar os parâmetros e configurações alteradas.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 419660
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
