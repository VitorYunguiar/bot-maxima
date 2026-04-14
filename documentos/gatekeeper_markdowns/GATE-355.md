# GATE-355 - Carregamento infinito ao importar planilha de clientes

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não se Aplica
- Assunto: MXPED - Central de Configurações
- Natureza: Dúvida
- Atualizado em: 2024-11-21T10:33:42.121-0300

## Contexto do Problema

## Passos para reproduzir
[AMBIENTE DE HOMOLOGAÇÃO]

>>Inteligência de Negócios
>Recomendação de produtos
>Pré-pedido
>Criar um novo pré-pedido
>Clientes
>Importar
>Importar clientes das planilhas em anexo

## Resultado apresentado
Quando o cliente acessa a tela de pré-pedido na central de configurações e importa os clientes da planilha, no cliente a maioria das vezes fica carregando por muito tempo e não importa. Quando tentei simular, em todos testes que eu fiz deu certo, importou sem problemas.

## Resultado esperado
Importar normalmente a planilha de clientes.

## Descrição
Bom dia Carlos/Filipe,

Tô com uma demanda da DESTRO onde o problema só acontece com o cliente, mas o mesmo evidenciou e eu conectei pra validar.

Acontece o seguinte:
Quando o cliente acessa a tela de pré-pedido na central de configurações e importa os clientes da planilha, no cliente a maioria das vezes fica carregando por muito tempo e não importa. Quando tentei simular, em todos testes que eu fiz deu certo, importou sem problemas.

Conectei no computador do cliente e tentei limpar o cache e trocar de navegador, mesmo assim o problema persistiu. Quando troquei de navegador, a primeira importação deu certo, mas ao fazer outro teste o problema voltou a ocorrer.

Vou deixar em anexo os logs que consegui tirar print, caso sirva de ajuda.\

Obs: Esse problema acontece só no ambiente de homologação, no ambiente de produção, segundo o cliente, funciona normal.

## Comentarios do Gatekeeper

### 1. 2024-11-21T10:32:58.409-0300 | Filipe do Amaral Padilha

Foi feita validação e consegui validar o problema na minha máquina, criei um pré-pedido de teste onde ocorre o problema pré-pedido "TESTE MAXIMA", por gentileza, não apagar porque vou enviar para o nosso desenvolvimento validar o erro e ver as possíveis soluções

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 407829
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "reproduzindo o comportamento relatado na importação de clientes" | "no pré-pedido em homologação" | "No momento, a causa do erro não foi identificada"
