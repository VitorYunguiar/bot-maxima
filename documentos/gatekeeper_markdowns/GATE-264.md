# GATE-264 - falha momentanea de reconhecimento de licença  do sistema

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXGESN - Instalação PWA
- Natureza: Dúvida
- Atualizado em: 2024-11-01T16:58:53.675-0300

## Contexto do Problema

## Passos para reproduzir
efetuar o login na aplicação e realizar o uso por um periodo de tempo.

## Resultado apresentado
a aplicação apresenta os alertas como nas imagens, mesmo que o usuário logado, tenha a versão do produto liberada e conexão ativa e regular em seu aparelho.

## Resultado esperado
é esperado que não se apresentem essas mensagens no cenário do usuário, uma vez que o mesmo está regularmente operando, com a versão do produto liberada e adequada.

## Descrição
Senhores, estamos identificando que a aplicação do maxgestão PWA, tem alguns momentos que deixa de reconhecer a licença do produto que o usuário se encontra logado e começa a exibir os alertas que são observados abaixo:

!image-2024-11-01-12-15-43-299.png|width=276,height=592!!image-2024-11-01-12-24-06-760.png|width=272,height=591!

Mesmo estando conectado a internet, demanda que seja refeito o login manualmente para reconhecer a versão do produto adequadamente, ainda que não tenham sido realizadas alterações no usuário que possam indicar essa necessidade, o que gera um falso negativo na visão do cliente que, há um problema com as versões do produto.

Credencial do cliente:

login: pec.reinaldo

senha: pec.reinaldo

## Comentarios do Gatekeeper

### 1. 2024-11-01T15:14:02.739-0300 | Filipe do Amaral Padilha

Foi revisado o fluxo na aplicação e foi constatado que ao logar na aplicação é gerado um token, este token tem validade de 24 horas. Após as 24 horas, o token é expirado fazendo com que a validação da versão pro/plus fique falha. E então o usuário perde acesso as funcionalidades do maxGestão, apresentando assim a mensagem "Acesso Negado".

Nesse caso, é preciso que seja tratado com uma melhoria pra implementar uma função de revalidação/refresh no token, assim, não será preciso matar a aplicação.

Como solução paliativa, é preciso matar a aplicação e fazer o login novamente.

--Tentei rastrear se havia alguma melhoria aberta sobre isso e não encontrei então o melhor é se o cliente quiser, abrir uma nova melhoria sobre o assunto. E cada ticket pai deve ser vinculado a uma melhoria individual. Não pode vincular vários N1 em apenas um N3 de Melhoria mesmo que sejam do mesmo assunto.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 404457
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Portanto, o alerta não está relacionado, pelos fatos analisados, à ausência de conexão ou à liberação da versão do produto"
