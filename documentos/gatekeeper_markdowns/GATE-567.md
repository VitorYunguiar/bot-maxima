# GATE-567 - Campo de endereço de entrega não puxa no relatório

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Relatório - Espelho Pedido/Orçamento
- Natureza: Dúvida
- Atualizado em: 2025-01-02T14:42:46.673-0300

## Contexto do Problema

## Passos para reproduzir
>> Importar base do RCA no maxPedido;
>> Gerar espelho do pedido;

## Resultado apresentado
No espelho do pedido não são apresentadas as informações de endereço de entrega.

## Resultado esperado
Espelho do pedido apresentando informações de endereço de entrega.

## Descrição
Ao gerar o espelho do pedido as informações de endereço de entrega não são apresentadas, mesmo com o endereço constando na base do RCA e no JSON do pedido.

Login: villa.janailmafreire

## Comentarios do Gatekeeper

### 1. 2025-01-02T14:42:46.672-0300 | Filipe do Amaral Padilha

Vou encaminhar para N3 porque não foi possível identificar o motivo do campo não estar gerando no relatório customizado para pedidos que possuem histórico já definido.

Em pedidos novos, seja na versão antiga ou na nova, as informações são apresentadas normalmente.

Na verdade o cliente está usando um relatório customizado 341 Padrão - Villa Camarão:

No caso, atualmente está configurado como \{EnderecoEntrega.endereco}, que traz só a informação da rua quando selecionado no pedido na aba TOTAIS.

Sobre a data de entrega, na aba TOTAIS do maxPedido se o RCA digitar uma "data prevista de faturamento", então essa informação sai no relatório que ele configurou customizado como se fosse "A data de entrega do pedido".

## Resposta Canonica

**Conclusão canônica**

O comportamento foi observado no **relatório customizado 341 Padrão - Villa Camarão**. Não foi possível identificar a causa de o campo de endereço de entrega não ser gerado no relatório **para pedidos que já possuem histórico definido**.

Pelos testes realizados:
- **Em pedidos novos**, tanto na versão antiga quanto na nova, **as informações de endereço são apresentadas normalmente**.
- O relatório está atualmente configurado com o parâmetro **`{EnderecoEntrega.endereco}`**, que **retorna apenas a rua** quando o endereço é selecionado no pedido na aba **TOTAIS**.
- Também foi identificado que, se o RCA preencher a **data prevista de faturamento** na aba **TOTAIS** do maxPedido, essa informação é exibida no relatório customizado como se fosse a **data de entrega do pedido**.

**Limitações da análise**
- Não foi possível determinar o motivo da não geração do campo no relatório customizado para pedidos com histórico já definido.
- A configuração atual do relatório limita a saída do endereço à informação de rua.
- A data exibida como entrega no relatório corresponde, na prática, à **data prevista de faturamento** informada na aba **TOTAIS**.

**Próximo passo**
- **Encaminhar para o N3** a análise do relatório customizado **341 Padrão - Villa Camarão**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 414520
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
