# GATE-450 - Relatório de espelho de rotas

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Protheus
- Assunto: MXGESN - Espelho de Rotas - Falta informações
- Natureza: Dúvida
- Atualizado em: 2024-12-04T16:46:47.029-0300

## Contexto do Problema

## Passos para reproduzir
Entrar no maxGestão do cliente, selecionar um vendedor qualquer e emitir o relatório de espelho de rotas do mesmo.

## Resultado apresentado
É verificado que o campo supervisor não é apresentado, e o campo filial está em conjunto com o campo usuário.

## Resultado esperado
É esperado que os campos sejam exibidos corretamente no relatório.

## Descrição
Cliente relata que anteriormente no maxGestão, ao emitir o relatório de espelho de rotas, eram apresentadas diversas informações no relatório, como:
- Filial
- Supervisor
- 1º Cli
- Últ. cli
- KM trabalhado
- R$ Ajuda Custo
- KM total
- R$ Ajuda Custo

Foi realizada a correção por parte da equipe de desenvolvimento na demanda MXGESNDV-15051, entretanto foi verificado que o campo supervisor ainda não é apresentado, e o campo filial é apresentado mas a informação gerada nele é em conjunto com o código do usuário, gerando inconsistências ao transmitir os dados dos relatórios para outras ferramentas como B.I.

## Comentarios do Gatekeeper

### 1. 2024-12-04T16:35:32.418-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 de fato a equipe não fez o levantamento de todos os dados do relatório antigo. Fiz o teste com relatório gerado no momento em comparação com o antigo e faltam os campos citados.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410369
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "incluindo a ausência do campo Supervisor" | "a inconsistência na apresentação do campo Filial" | "nem todos os campos esperados foram considerados na correção realizada"
