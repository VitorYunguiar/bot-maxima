# GATE-357 - Codigo de desbloqueio invalido

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Cadastros - Usuários/Perfil de Usuários
- Natureza: N/A
- Atualizado em: 2024-11-21T15:54:28.896-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxPedido;
>> Tentar fazer check in em qualquer cliente;
>> Gerar codigo de desbloqueio;
>> Acessar o maxGestão PWA;
>> Inserir o codigo de desbloqueio gerado no maxPedido;

## Resultado apresentado
Mensagem de codigo invalido

## Resultado esperado
Codigo sendo desbloqueado com sucesso.

## Descrição
Ao tentar autorizar desbloqueio pelo maxGestão PWA Mobile, retorna que o codigo é invalido. O mesmo codigo na central de configurações do maxPedido passa sem problemas.

tet.maxima
tet@123

Ocorrendo em base do zero.

## Comentarios do Gatekeeper

### 1. 2024-11-21T15:54:28.895-0300 | Filipe do Amaral Padilha

Enviado para N3 acredito que a funcionalidade deveria desbloquear o código no maxPedido através do app do maxGestão PWA porém não está funcionando conforme deveria;

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 407985
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Há 'comportamento divergente na funcionalidade de desbloqueio de código entre os canais disponíveis'. | O 'código de desbloqueio gerado no maxPedido é aceito na central de configurações do próprio maxPedido'. | Ao informar o código no app do maxGestão PWA Mobile 'retorna como inválido'. | Existe uma 'central de configurações do próprio maxPedido'. | Ação recomendada: 'Encaminhar para o time N3' como recomendação da resposta (o texto-fonte apenas diz que foi enviado para N3, não recomenda a ação). | 'Validar e corrigir' o funcionamento como próximo passo não está explicitamente no texto-fonte.
