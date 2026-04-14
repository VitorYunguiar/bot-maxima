# GATE-623 - PCPEDC divergente da MXSHISTORICOPEDC

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Banco de Dados
- Natureza: N/A
- Atualizado em: 2025-01-13T10:32:03.659-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar base do RCA em anexo
>>Verificar a timeline de pedidos
>>Verificar as tabelas MXSINTEGRACAOPEDIDO, MXSHISTORICOPEDC e PCPEDC

Login: OCIDENTAL.RCA119
Senha:Temporária
Login: OCIDENTAL.RCA119
Senha: Temporária

## Resultado apresentado
>>Os pedidos não foram enviados para a MXSHISTORICOPEDC e ao tentar pesquisar pelo post ocorrem erros(possívelmente ligado ao motivo do erro)
>>Os pedidos constam como L na timeline, porém já foram faturados na PCPEDC

## Resultado esperado
>>Os registros da PCPEDC devem ser passados para a MXSHISTORICOPEDC e atualizarem na timeline do cliente

## Descrição
>>Os pedidos estão sendo gravados na PCPEDC porém não estão aparecendo na MXSHISTORICOPEDC, exemplo o pedido '119219089'

## Comentarios do Gatekeeper

### 1. 2025-01-13T10:32:03.656-0300 | Filipe do Amaral Padilha

Ao verificar o pedido na MXSHISTORICOPEDC, constatei que já foi integrado automaticamente com POSICAO = 'F'.

SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED = 119014790
MXSHISTORICOPEDC e MXSHISTORICOPEDI normalizadas.

Provavelmente, como eles estavam na versão 3.1.3.295 do banco anteriormente, então não estavam atualizados com a nossa alteração na TRIGGER para descer os registros para a MXSHISTORICOPEDC.

Então depois que o banco aplicou a atualização no banco local, os registros integraram normalmente.

Também fiz uma avaliação do banco local do cliente e constatei que não existem LOCKs e também não há problemas com objetos inválidos; O ambiente está funcional.

Se o cliente observar uma lentidão no processamento ou o problema novamente com outros pedidos, por gentileza, reabrir o ticket informando as novas evidências.

## Resposta Canonica

**Causa provável**  
O banco local provavelmente estava anteriormente na versão **3.1.3.295** e ainda não continha a alteração na **trigger** responsável por enviar os registros para a **MXSHISTORICOPEDC**. A causa é **provável, não conclusiva**.

**Análise realizada**  
Foi validado que, no banco local do cliente:

- o pedido consultado já consta integrado automaticamente na **MXSHISTORICOPEDC** com **POSICAO = 'F'**;
- as tabelas **MXSHISTORICOPEDC** e **MXSHISTORICOPEDI** estão normalizadas;
- após a atualização aplicada no banco local, os registros passaram a integrar normalmente;
- não foram identificados **LOCKs**;
- não há problemas com **objetos inválidos**;
- o ambiente está funcional.

SQL utilizado na validação:
```sql
SELECT * FROM MXSHISTORICOPEDC WHERE NUMPED = 119014790
```

**Conclusão**  
No momento da análise, a integração para a **MXSHISTORICOPEDC** estava ocorrendo normalmente após a atualização do banco local, com evidência de pedido já integrado com **POSICAO = 'F'**.

**Próximo passo**  
Manter monitoramento. Se o cliente voltar a observar o problema com outros pedidos ou perceber lentidão no processamento, o ticket deve ser reaberto com novas evidências para nova análise.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 416419
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
