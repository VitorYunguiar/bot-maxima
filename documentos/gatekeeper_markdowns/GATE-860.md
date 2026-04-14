# GATE-860 - MaxGestão PWA gerando senha de desbloqueio nula

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não se Aplica
- Assunto: MXGESN - Web divergente PWA
- Natureza: Dúvida
- Atualizado em: 2025-02-26T14:47:47.693-0300

## Contexto do Problema

## Passos para reproduzir
>>tet.maxima
>tet@123

>Acessar maxGestão PWA
>Desbloqueio de vendedor
>Marcar flag "senha master"
>Definir algum tempo limite, por exemplo 5 minutos
>Gerar a senha de desbloqueio

Ao gerar a chave de desbloqueio é retornado uma tela com valores zerados, ao clicar no botão de copiar para área de transferência é copiado o texto "undefined".

## Resultado apresentado
Ao gerar a chave de desbloqueio é retornado uma tela com valores zerados, ao clicar no botão de copiar para área de transferência é copiado o texto "undefined".

## Resultado esperado
Gerar a chave corretamente conforme acontece na central de configurações.

## Comentarios do Gatekeeper

### 1. 2025-02-26T14:47:47.691-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 se trata de erro

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: Descrição
- Groundedness aprovado: nao
