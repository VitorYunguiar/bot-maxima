# GATE-882 - problemas de configuração para funcionamento API De estoque online SANKHYA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Sankhya
- Assunto: MXPED - Produto - Estoque
- Natureza: Dúvida
- Atualizado em: 2025-02-27T16:34:15.727-0300

## Contexto do Problema

## Passos para reproduzir
fazer a validação conforme a descrição

## Resultado apresentado
o token gerado pelo cliente não é valido para a atualização de estoque.
Segundo o cliente, isso acontece por questões de URL e appkey que a maxima usa apenas do ambiente de produção

## Resultado esperado
é esperado que o token citado seja validado normalmente e sem falhas

## Descrição
Senhores, ao analisarmos o cenário relatado pelo cliente, estamos verificando que a sua atualização estoque não está ocorrendo regularmente, conforme aqui indicado:

!image-2025-02-27-10-12-32-061.png!

essa situação vem ocorrendo devido ao TOKEN que o cliente possui cadastrado em seu ambiente de homologação: !image-2025-02-27-10-13-27-153.png!

o qual é reportado estar invalido:

!image-2025-02-27-10-14-05-734.png!

Em contato junto ao cliente, o mesmo reportou que essa situação ocorre devido ao ambiente de homologação do sankhya apontar para outra URL e outro tipo de ambiente e as configurações do APPKEY e URL da maxima apontam para o cenário de produção. Vide áudios em anexo onde o cliente descreve essa questão.

Como proceder com essa configuração? Na biblioteca da maxima em que nos baseamos para analise desse cenário, não estou identificando informações necessárias para proceder com a analise dessa questão, uma vez que não é citado qual a configuração que precisamos alterar para apontar ao ambiente de sanbox ou teste do cliente.

Obs.: o ambiente de produção opera regularmente onde apenas o ambiente de homologação que apresenta a falha aqui relatada:

!image-2025-02-27-10-22-43-932.png!

## Comentarios do Gatekeeper

### 1. 2025-02-27T16:04:29.775-0300 | Filipe do Amaral Padilha

Dentro do maxPedido só existe integração direta com o link de produção da Sankhya: https://api.sankhya.com.br/

A URL é fixa no código do maxPedido, não é parametrizável. Então atualmente não teria como o cliente operar em ambiente de teste usando o maxPedido e o ambiente de HMG.

Precisaria ser tratado como melhoria para mapear a questão de mudança do APPKEY e também da URL que é diferente na homologação da Sankhya.
Link do HMG -> https://api.sandbox.sankhya.com.br/login

Uma alternativa seria ele usar o ambiente de produção mesmo para realizar os testes com 1/dois usuários de teste ou até de produção

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: requires_attachment_review, grounding_failed, needs_review
- Comentarios primarios: 427170
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'a falha ocorre' — o texto-fonte não menciona uma falha específica, apenas limitações da integração | 'o token gerado nesse cenário não será validado como esperado' — não há menção a token ou validação de token no texto-fonte
