# GATE-822 - Venda transmitida

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Gleiciellen Pereira Leal [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Resumo de Vendas
- Natureza: Erro
- Atualizado em: 2025-02-19T09:10:47.208-0300

## Contexto do Problema

## Passos para reproduzir
> Login:rafalim.057
> Valor na venda transmitida presente na tela inicial está divergente do valor no resumo de vendas
>Na base do zero foi apresentado o valor exibido corretamente na tela inicial e no resumo de vendas
> A divergência ocorre apenas na base do RCA

## Resultado apresentado
> Valor na venda transmitida presente na tela inicial está divergente do valor no resumo de vendas

## Resultado esperado
> Valor que apresenta no resumo de vendas ser o mesmo que apresenta na tela inicial

## Descrição
O valor exibido na *tela inicial* da venda transmitida está *divergente* do valor apresentado no *resumo de vendas*.

## Comentarios do Gatekeeper

### 1. 2025-02-19T08:51:40.672-0300 | Filipe do Amaral Padilha

Será encaminhado para desenvolvimento N3, porque pelo o que eu observei, tem dados duplicados na base do RCA, por isso as informações são apresentadas inconsistentes nos gráficos.

Paliativamente eu já mandei apagar as duplicidades, então para resolver o problema do usuário, basta ele mandar atualizar o menu que todos os gráficos serão atualizados com os valores corretamente.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 425072
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A divergência entre o valor da venda transmitida na tela inicial e no resumo de vendas ocorre por dados duplicados na base do RCA. | A divergência ocorre apenas na base do RCA. | Na base do zero, o valor foi exibido corretamente tanto na tela inicial quanto no resumo de vendas. | Remover as duplicidades na base do RCA.
