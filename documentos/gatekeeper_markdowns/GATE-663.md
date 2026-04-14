# GATE-663 - Cliente não aparece para ser roteirizado

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: ROTVENDN - Cliente - Não Aparece no Sistema
- Natureza: Dúvida
- Atualizado em: 2025-01-21T09:34:39.481-0300

## Contexto do Problema

## Passos para reproduzir
>> Abrir roteirizador de vendedores;
>> Roteirizar RCA MAICON RODRIGUES LISKOSKI;
>> Buscar cliente 65273;

## Resultado apresentado
Cliente não aparece no sistema para ser roteirizado, mesmo estando vinculado ao RCA no campo MXSCLIENT.CODUSUR1.

## Resultado esperado
Cliente aparecendo na listagem para roteiziação.

## Descrição
Cliente não aparece no sistema para ser roteirizado, mesmo estando vinculado ao RCA no campo MXSCLIENT.CODUSUR1.

CODCLI: 65273

## Comentarios do Gatekeeper

### 1. 2025-01-21T09:34:39.479-0300 | Filipe do Amaral Padilha

RCA
MAICON RODRIGUES LISKOSKI

O cliente 65273 não aparece para ser roteirizado porque não possui coordenadas cadastradas.

Para resolver, antes de Roteirizador o RCA, deve ser verificado os "clientes sem coord." e validar que o cliente em questão 65273 não possui coordenadas. Elas devem ser cadastradas conforme o endereço do cliente ou se souber também a localização exata. Somente assim será possível adicionar no Roteiro de visitas do RCA.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 417909
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Embora o cliente esteja vinculado ao RCA no campo MXSCLIENT.CODUSUR1" | "Conforme validado"
