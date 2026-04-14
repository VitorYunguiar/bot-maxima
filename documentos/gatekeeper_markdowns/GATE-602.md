# GATE-602 - Divergência entre a ERP_MXSPREST e a PCPREST

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Banco de Dados
- Natureza: Dúvida
- Atualizado em: 2025-01-09T11:46:58.517-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar base do zero ou base em anexo
>>Abrir o cadastro do cliente 507353 na aba títulos

## Resultado apresentado
>>O título 669805 consta como pendente
>>Na ERP_MXSPREST também consta como pendente
>Na PCPREST  o título está pago

## Resultado esperado
>>O título deve aparecer como pago no banco nuvem, da forma que já está no banco local

## Descrição
>>No Winthor a duplicata 669805 foi baixada, porém no banco nuvem essa duplicata ainda permanece sem DTPAG e VPAGO como segue prints em anexo

## Comentarios do Gatekeeper

### 1. 2025-01-09T11:46:58.513-0300 | Filipe do Amaral Padilha

Foi realizada a normalização dos registros, sanando a divergência entre os bancos local e nuvem.

A duplicata no processo foi definida para codoperacao = 2, isso garante que ela será dada como baixa (apagado) do maxPedido.

O problema ocorreu porque no passado, no dia 06/12/2024 houve a seguinte falha "-6508 -ORA-06508: PL/SQL: could not find program unit being called", que não encontrava o programa para realizar a subida das informações da nuvem. O problema posteriormente foi corrigido, porém os dados retroativos só sobem realizando a normalização.

A job vai rodar para atualizar o registro na MXSTITULOSABERTOS às 12:05:00 hoje, ela dispara a cada 1h, então depois desse horário: Para validar o RCA pode estar sincronizando o maxPedido, o título vai sumir do maxPedido.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 415928
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Na análise do título em questão, a duplicata foi definida com `codoperacao = 2`, condição que garante sua baixa (apagado) no maxPedido. | **Próximo passo:** aguardar a execução da job às **12:05:00** e, em seguida, validar se o título foi atualizado na `MXSTITULOSABERTOS` e se deixou de aparecer no maxPedido.
