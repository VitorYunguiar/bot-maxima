# GATE-262 - Mensagem de Acesso Negado no maxGestão PWA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Henrique Torres Andrade [X]
- ERP do cliente: Winthor
- Assunto: MXGESN - Cadastros - Usuários/Perfil de Usuários
- Natureza: Erro
- Atualizado em: 2024-11-01T15:14:22.076-0300

## Contexto do Problema

## Passos para reproduzir
>> USUÁRIO DE TESTE 1
ekal.alisson
ekal2022
>> USUÁRIO DE TESTE 2
ekal.genison
ekal2022
>> USUÁRIO DE TESTE 3
ekal.icaro
ekal2022

## Resultado apresentado
>> Aparece tela para o usuário informando "Acesso Negado", e que o mesmo não tem permissão para acessar a página, sendo que só aparece as telas que ele possui permissão para acessar

## Resultado esperado
>> Tela de "Acesso Negado" não aparecer para o usuário

## Descrição
>> Realizados testes e verificado que quando se tira uma permissão na central de configurações, a opção some do maxGestão PWA, evitando que o RCA encontre uma tela que ele não tenha acesso
>> Verificado com o Gatekeeper Filipe Padilha que, provavelmente, por estar o app aberto por muito tempo em segundo plano, o app fica sem atualizar, e com isso acaba perdendo o token de acesso, fazendo com que as telas fiquem indispoíveis, sendo necessário fechar o app e abrir novamente

## Comentarios do Gatekeeper

### 1. 2024-11-01T15:14:22.075-0300 | Filipe do Amaral Padilha

Foi revisado o fluxo na aplicação e foi constatado que ao logar na aplicação é gerado um token, este token tem validade de 24 horas. Após as 24 horas, o token é expirado fazendo com que a validação da versão pro/plus fique falha. E então o usuário perde acesso as funcionalidades do maxGestão, apresentando assim a mensagem "Acesso Negado".

Nesse caso, é preciso que seja tratado com uma melhoria pra implementar uma função de revalidação/refresh no token, assim, não será preciso matar a aplicação.

Como solução paliativa, é preciso matar a aplicação e fazer o login novamente.

--Tentei rastrear se havia alguma melhoria aberta sobre isso e não encontrei então o melhor é se o cliente quiser, abrir uma nova melhoria sobre o assunto. E cada ticket pai deve ser vinculado a uma melhoria individual. Não pode vincular vários N1 em apenas um N3 de Melhoria mesmo que sejam do mesmo assunto.

## Resposta Canonica

**Causa identificada**  
O token gerado no login da aplicação possui validade de **24 horas**. Após esse período, o token expira, a validação da versão **pro/plus** falha e o usuário perde acesso às funcionalidades do **maxGestão**, passando a visualizar a mensagem **“Acesso Negado”**.

**Análise realizada**  
Foi revisado o fluxo da aplicação e confirmado que:
- ao realizar o login, é gerado um token;
- esse token tem validade de **24 horas**;
- após a expiração, a validação da versão pro/plus deixa de ocorrer corretamente;
- com isso, o acesso às funcionalidades do maxGestão é perdido;
- nesse cenário, a aplicação exibe **“Acesso Negado”**.

**Ação recomendada**  
- **Definitiva:** implementar uma rotina de **revalidação/refresh do token**.  
- **Paliativa:** **encerrar a aplicação e realizar novo login**.

**Limitações e encaminhamento**  
- Não foi identificada melhoria já aberta para esse tema.  
- Caso o cliente queira evoluir o comportamento, é necessário **abrir uma nova melhoria**.  
- O vínculo deve ser feito de forma **individual por ticket pai**, pois **não é permitido vincular vários N1 em um único N3 de Melhoria**, mesmo sendo o mesmo assunto.

**Responsável pelo próximo passo**  
Cliente, caso opte pela abertura da melhoria.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 404458
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
