# GATE-59 - Cadastro de cliente não integra - COD. CLIENTE JÁ EXISTE

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - Cadastro de Cliente - Falha de envio
- Natureza: Dúvida
- Atualizado em: 2024-09-13T15:44:34.496-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar MXSINTEGRACAOCLIENTE e consultar os registros com status 14 (Exemplo ID_CLIENTE 16163)
>>Consultar no OBJETO_JSON pelo campo "CriticaImportação"
>>Observar a crítica

RCA que cadastrou o cliente de ID 16163, solicitei a base e irei anexar quando receber.
>>HIMALAIA.1576

## Descrição
Bom dia,

Verifiquei que voltou a ocorrer o problema no envio de cadastro de clientes, onde o registro é enviado porém retorna na crítica que o "COD. CLIENTE JA EXISTE", e só é possível integrar deletando o registro da MXSINTEGRACAOCLIENTE e soliciando ao RCA que abra o cadastro e envie novamente.

O problema já tinha acontecido anteriormente e foi tratado no ticket MXPED-56501

## Comentarios do Gatekeeper

Nenhum comentario elegivel do assignee foi identificado.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, needs_review
- Comentarios primarios: nenhum
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
