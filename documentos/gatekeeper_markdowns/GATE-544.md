# GATE-544 - Erro ao cadastrar residência do RCA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXGESN - Mapas
- Natureza: Dúvida
- Atualizado em: 2024-12-23T08:12:41.687-0300

## Contexto do Problema

## Passos para reproduzir
>>Entrar no maxGestao WEB pelo login enviado
>>Entrar na aba 'Geolocalização' > 'mapas'
>>Selecionar o RCA 102870 - Antonio Simoes
>>Ver cliente
>>Clicar na 🏠 'residência do RCA'
>>Colocar a latitude e longitude abaixo:
'-4.57352374112964, -37.774148040377'
>>Salvar

Login: ruralshop.vanessasantos
Senha: @@vanes8

## Resultado apresentado
O maxGestao carrega, porém não aparece nenhuma mensagem de sucesso e continua na mesma tela, e ao sair a localização não fica salva.

## Resultado esperado
>>A localização da residência do RCA deve ser salva ao clicar em 'salvar'

## Descrição
>>Ao tentar incluir um endereço de residência do RCA, o sistema carrega, mas não salva o endereço, como segue vídeo em anexo

## Comentarios do Gatekeeper

### 1. 2024-12-23T08:12:41.684-0300 | Filipe do Amaral Padilha

Será enviado para N3 como Erro porque não está sendo possível cadastrar a casa do RCA e nenhum retorno ocorre na tela

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 413566
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A menção à tela **Geolocalização > Mapas** não aparece no texto-fonte. | A afirmação de que ocorre uma tentativa de salvar não está explicitamente no texto-fonte. | A conclusão de que o sistema não conclui o salvamento da localização da residência do RCA extrapola o texto-fonte. | A afirmação de que não apresenta mensagem de retorno ao usuário é uma inferência; o texto-fonte apenas diz que nenhum retorno ocorre na tela. | A seção **Responsável pelo próximo atendimento: N3** não está explicitamente no texto-fonte, embora haja encaminhamento para N3.
