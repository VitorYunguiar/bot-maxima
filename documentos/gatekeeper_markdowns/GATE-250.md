# GATE-250 - [MXGESN] Filtro - Relatório de Acessos

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXGESN - Relatórios - Filtros/Pesquisa
- Natureza: Dúvida
- Atualizado em: 2024-10-30T13:48:31.047-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar maxGestão
>Usuários
>Relatórios de Acesso
>Tentar filtrar algum gerente

## Resultado apresentado
Ao filtrar nessa tela do relatório não exibe nenhum gerente, mesmo o usuário sysMax tendo acesso total.

## Resultado esperado
Entender qual é o vinculo entre gerente e supervisor.

## Descrição
Bom dia Filipe,

Estou com uma dúvida, um cliente abriu uma demanda sobre a tela "Relatórios de Acessos", que pra mim é uma novidade, não me lembro de ter visto essa funcionalidade antes.

Nisso, ao filtrar nessa tela do relatório não exibe nenhum gerente, eu não entendi muito bem esse filtro, pois ele filtra gerentes e também supervisores, e os gerentes são necessários para poder visualizar os supervisores.

Gostaria de entender qual amarra é feito entre gerente e supervisor.

## Comentarios do Gatekeeper

### 1. 2024-10-30T13:48:31.045-0300 | Filipe do Amaral Padilha

Para apresentar os gerentes no filtro, será necessário o cliente informar um código de RCA para o Gerente porque o filtro considera as filiais disponíveis conforme a MXSUSUARI (CODFILIAL) e para exisitir essa relação com o Gerente, precisa ter o ERP_MXSGERENTE.CODUSUR = MXSUSUARI.CODUSUR.

No caso deles eles não possuem RCA vinculado ao gerente, por isso não carrega a informação na ERP_MXSGERENTE e consequentemente não exibe no filtro.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 403902
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A resposta afirma que o problema ocorre especificamente no filtro da tela **Relatórios de Acesso**, mas o texto-fonte não menciona essa tela. | A resposta diz que há uma 'amarra entre gerente e supervisor', porém o texto-fonte não menciona supervisor. | A resposta recomenda que 'após isso, a relação poderá ser carregada e o gerente passará a ser exibido no filtro' como efeito futuro explícito; embora seja uma inferência plausível, isso não está dito literalmente no texto-fonte.
