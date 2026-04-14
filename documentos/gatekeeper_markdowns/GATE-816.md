# GATE-816 - observação padrão em pedido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Não se Aplica
- Assunto: MXPED - Parametrização
- Natureza: Dúvida
- Atualizado em: 2025-02-18T12:49:17.138-0300

## Contexto do Problema

## Passos para reproduzir
conforme descrição

## Resultado apresentado
conforme descrição

## Resultado esperado
conforme descrição

## Descrição
Senhores, fiz algumas consultas no ambiente do cliente, bases de conhecimento e tickets o JIRA, mas não identifiquei algo que se aproxime da necessidade do cliente.

Existe alguma funcionalidade no aplicativo que permita cadastrar observações padrões por clientes de modo que cada vez que um vendedor digitar um pedido essa observação entre no pedido ?

## Comentarios do Gatekeeper

### 1. 2025-02-18T12:49:17.134-0300 | Filipe do Amaral Padilha

Dado o contexto do ticket, eu analisei e encontrei essas seguintes opções:

--Essa parte só funcionou na v4 durante os meus testes

Teria como mostrar o campo:
OBS2 que vai cadastrado na MXSCLIENT
Porém ele depende dos parâmetros HABILITAR_OBSERVACOES_CLIENTE e CON_GRAVAROBSCLIENTENOPEDIDO estarem ambos ativos; sendo o HABILITAR_OBSERVACOES_CLIENTE  da MXSPARAMETRO e o CON_GRAVAROBSCLIENTENOPEDIDO da MXSPARAMFILIAL.

--Essa parte funcionou na v3.264.0 e na v4

No pedido, para ter observações fixas por cliente sempre que inicia o pedido, é só cadastrar os campos
OBSENTREGA1 = ex 'ENTREGAR RUA XXXXX N 25434'
OBSENTREGA2 = ex '1542132'
OBSENTREGA3 = ex 'CELULAR 9999999999'

Preenchendo os dados de OBS1,2,3,4 e 5 do cliente, vai aparecer na aba Inf. Cliente (Informações do cliente) no card "Outros";

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 424813
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que as opções são 'para atender essa necessidade' não está explicitamente suportada pelo texto-fonte, que apenas lista opções encontradas no contexto do ticket. | A seção 'Recomendação' (validar com o cliente, testar no ambiente/versão utilizada, garantir ativação dos parâmetros) não aparece no texto-fonte. | A formulação 'o uso do campo OBS2 na MXSCLIENT foi validado apenas na v4' extrapola levemente o texto, que diz apenas que 'essa parte só funcionou na v4 durante os meus testes'.
