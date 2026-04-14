# GATE-630 - Não gera arquivo ao exportar pedidos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Exportar/Importar
- Natureza: Dúvida
- Atualizado em: 2025-01-14T09:54:41.235-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxPedido;
>> Importar a base anexada;
>> Exportar os pedidos;
>> Limpar a base do aplicativo;
>> Baixar base do zero;
>> Tentar importar os pedidos

## Resultado apresentado
Mensagem informando que "Esse dispositivo não possui pedidos/orçamentos para importar"

## Resultado esperado
Importando os pedidos que foram exportados anteriormente.

## Descrição
Ao exportar os pedidos pelo menu de ferramentas aparentemente não estão sendo gerados os arquivos do pedido, e ao tentar importar os pedidos depois de limpar a base do aplicativo ele retorna que não existem arquivos de pedidos para importação.

Login: ttslz.ticslz2

## Comentarios do Gatekeeper

### 1. 2025-01-14T09:48:17.302-0300 | Filipe do Amaral Padilha

Se trata de erro foi realizado teste na versão 3.256.0 antes da alteração da SDK e funcionalidade estava com comportamento correto:
1° Exportar pedidos
2° Limpar dados no armazenamento externo do maxPedido dentro das configurações do Android
3° Baixar base do zero
4° Importar pedidos
Resultado = pedidos importados com sucesso

Será encaminhado para N3

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 416654
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Assim, a indicação atual é de possível relação com a alteração da SDK" — o texto-fonte informa apenas que antes da alteração da SDK o comportamento estava correto, mas não afirma uma relação possível ou causal com a alteração da SDK. | "não há causa raiz confirmada" — isso não é afirmado explicitamente no texto-fonte. | "não foram informados detalhes adicionais de ambiente além da versão 3.256.0 e do contexto antes da alteração da SDK" — essa é uma inferência sobre ausência de informação, não uma afirmação presente no texto-fonte. | "Próximo passo recomendado: encaminhar para N3" — o texto-fonte diz "Será encaminhado para N3", mas não caracteriza isso como recomendação.
