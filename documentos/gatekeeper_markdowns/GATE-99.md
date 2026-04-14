# GATE-99 - Cadastro de Cliente "Cod. Cliente já Existe"

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - Cadastro de Cliente - Falha de envio
- Natureza: Dúvida
- Atualizado em: 2024-09-25T11:25:14.070-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar APK
>Importar base do RCA
>Clientes
>Gerenciar clientes

## Resultado apresentado
Alguns RCAs da Himalaia estão com esse problema ao enviar cadastro de cliente, retorna na crítica de que o "COD. CLIENTE JA EXISTE". O problema ja atingiu vários vendedores, um deles é o que está com a base em anexo.

Esse cliente que a crítica retorna dizendo que o código já existe, o CNPJ não existe na MXSCLIENT, o cadastro só é enviado com êxito se o registro for deletado na MXSINTEGRACAOCLIENTE e reenviar o cadastro.

## Resultado esperado
Poder enviar os cadastros, e caso dê algum problema, continuar reenviando a informação para a PCCLIENTFV.

## Comentarios do Gatekeeper

### 1. 2024-09-25T11:25:14.069-0300 | Filipe do Amaral Padilha

Vai ser enviado para N3 porque já foi alinhado com o Cleyton que isso seria um ponto de correção que a Máxima precisa fazer na hora de gravar um cliente no banco do Winthor

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 396867
- Secoes ausentes: Descrição
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A análise indica que o comportamento relatado — crítica de “COD. CLIENTE JÁ EXISTE” no envio de cadastro, mesmo sem existência do CNPJ na MXSCLIENT e com sucesso apenas após exclusão do registro na MXSINTEGRACAOCLIENTE — já foi alinhado com o Cleyton como necessidade de correção. | Falha no processo de gravação de cliente no banco do Winthor.
