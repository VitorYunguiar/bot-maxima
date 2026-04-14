# GATE-102 - Troca de usuário

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Pedro Henrique Rodrigues Moura
- ERP do cliente: SOFTPOOL
- Assunto: MXPED - Usuário - Cadastro
- Natureza: Dúvida
- Atualizado em: 2024-09-26T15:46:03.907-0300

## Contexto do Problema

## Passos para reproduzir
- Login: tozzi.anderson

>> Acessar Central de configurações / Acessar o cadastro do usuário do mesmo;
>> Trocar seu CODUSUR por outro;

>> Acessar MaxPedido;
>> Menu "Ferramentas" / Supervisor;

## Resultado apresentado
>> Apresenta em branco;

## Resultado esperado
>> Apresenta o seu usuário representante para trocar de base.

## Descrição
>> O cliente possui um RCA Anderson que é Supervisor e RCA, o mesmo realiza troca de CODUSUR pela central de configurações, e quando tenta retornar para a base dele no app, não apresenta nada, fluxo testado na V2 e V3.

## Comentarios do Gatekeeper

### 1. 2024-09-26T12:34:20.764-0300 | Filipe do Amaral Padilha

Nesse caso não se trata de uma falha de sistema, vou explicar abaixo como a funcionalidade trabalha e também o motivo de não exibir nenhum RCA quando a troca é realizada diretamente via Central.

A funcionalidade trabalha da seguinte forma: O Supervisor no caso 218, usa o maxPedido, com o código de RCA 218, por dentro do maxPedido, quando ele vai trocar de base para outro RCA, serão exibidos todos os RCAs que estiverem vincualdos ao supervisor 218 pelo CODSUPERVISOR da tabela MXSUSUARI e que estiverem ativos e também com licença liberada do maxPedido. Então quando o Supervisor pelo maxPedido dele troca de base, automaticamente na Central é atualizada a referência de Código de RCA para a base que ele selecionou, porém o código padrão dele se mantém 218, para que, quando ele for retornar para a base dele também seja exibida essa opção. E essa funcionalidade está normal, pelo menos na versão 3.251.4. Na V2 o conceito é o mesmo, apesar que pode estar com algum problema não tratado.

Porque não aparece nenhum usuário quando é colocado direto um outro CODUSUR via Central de Configurações? Isso ocorre porque nenhum RCA da equipe 218 está ativo e com licença liberada do maxPedido, então apesar de conseguir acessar a base do RCA fazendo uma modificação direta pela Central, isso fere as validações que o aplicativo faz para que seja possível voltar para a base de origem, sendo necessário caso o usuário queira voltar, faça a alteração manualmente via Central.

*Obs, não passar para o cliente: No caso para o cliente resolver o problema dele, ele deve seguir as orientações de como a funcionalidade trabalha, se ele bater o pé que não quer dessa forma, então seria melhoria, porque atualmente a aplicação não opera de outra forma a não ser essa que expliquei.*

## Resposta Canonica

Não foi identificada falha de sistema.

O comportamento ocorre porque a troca direta de **CODUSUR** pela **Central de Configurações** fere as validações do aplicativo para retorno à base de origem. Na funcionalidade **Ferramentas > Supervisor**, o sistema exibe para o supervisor **218** apenas os RCAs vinculados a ele pelo campo **CODSUPERVISOR** da tabela **MXSUSUARI**, desde que estejam **ativos** e com **licença do maxPedido liberada**.

Na análise do cenário, **nenhum RCA da equipe 218 está ativo e com licença liberada do maxPedido**, por isso a tela é apresentada em branco.

Funcionamento esperado:
- Quando a troca de base é feita pelo **maxPedido**, a Central atualiza a referência do **Código de RCA** para a base selecionada;
- O **código padrão permanece 218**, permitindo o retorno à base de origem pelo aplicativo.

Como a alteração foi feita manualmente pela Central, esse fluxo não é respeitado, e o retorno à base pelo app deixa de atender às validações previstas.

Validação:
- **Versão 3.251.4**: funcionamento normal.
- **V2**: mantém o mesmo conceito, embora possa haver algum problema não tratado.

Orientação:
- Realizar a troca de base pelo **maxPedido**, e não pela **Central de Configurações**.
- Se a alteração já foi feita manualmente pela Central, o retorno também deve ser realizado manualmente pela Central.
- Caso o cliente solicite comportamento diferente do atual, a demanda deve ser tratada como **melhoria**.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 397271
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
