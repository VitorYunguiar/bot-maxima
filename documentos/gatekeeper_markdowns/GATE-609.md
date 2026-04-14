# GATE-609 - falhas com gerador de relatorios 800

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Relatório - 800
- Natureza: Dúvida
- Atualizado em: 2025-01-10T08:08:00.955-0300

## Contexto do Problema

## Passos para reproduzir
Acessar o maxgestão do cliente, ir em relatorios winthor, buscar pelo relatorio 8044 e tentar gerar o mesmo

## Resultado apresentado
está ocorrendo falha na geração dos relatorios.

## Resultado esperado
é esperado que o relatorio seja gerado sem falhas.

## Descrição
Senhores, ao analisar o cenário relatado pelo cliente, não estou identificando qual a razão de estar apresentando falha nas gerações.

o parametro do endereços dos relatorios está configurado adequadamente:

!image-2025-01-09-12-51-44-094.png!

o acesso externo está sendo realizado normalmente:

!image-2025-01-09-12-52-12-115.png!

os teste de autenticação e autorização estão corretamente aplicados:

!image-2025-01-09-12-53-12-024.png!

assim como o acesso a pasta dos relatorios estão operando normalmente:

!image-2025-01-09-12-54-08-763.png!

porém não é carregado nem os parametros do relatorio ou a geração dele é executada:

!image-2025-01-09-12-54-46-942.png!

o que está acontecendo que está gerando essas situação, uma vez que todas das configurações esperadas de serem realizadas, estão corretas? existe algum outro ponto de configuração que demanda de ser realizado?

## Comentarios do Gatekeeper

### 1. 2025-01-10T08:08:00.953-0300 | Filipe do Amaral Padilha

Verifiquei a instalação dos relatórios 800, procurei também por LOGs e não identifiquei nenhum problema com essas informações.

Eu realizei atualização do arquivo gerador da 800, removi a porta 8090 que estava sem uso para evitar qualquer tipo de conflito, deixando somente a 9090;

Realizei uma normalização de dados, onde identifiquei que parâmetros da nossa nuvem estavam divergentes da PCPARAMETROS;

Embora tenha validado tudo isso, não resolveu a situação. Então eu validei a questão de acessos:

Com a VPN e com uma máquina usando a rede na região brasileira, está acessando normalmente o IP http://vpn.root.net.br:9090/admin;

Porém no Workspace não está acessando, provavelmente é algum bloqueio de região que o cliente possui na rede dele.

O maxGestão precisa acessar pelo AWS, geralmente o pessoal libera porque a request do gestão utiliza essa conexão.

Comparei também com outros clientes (MEGGA e HOTBEL) que estão funcionando atualmente e acessam pelo Workspace.

Então sugiro duas coisas:

1° Solicitar ao cliente verificar possíveis bloqueios por região, de forma que permita o acesso externo através de uma máquina que está fora do País (Vírginia - USA)
2° Depois de liberado se continuar sem funcionar, realizar uma reinstalação do serviço, limpando as pastas e configurações desnecessárias, já instalando na versão mais recente dos REL 800 com o instalador novo: link para os arquivos: https://drive.google.com/drive/folders/1K0tlQEl0tRY4e-rvBOMMlK3WSclCWQaq?usp=sharing

## Resposta Canonica

Após as validações realizadas, não foram identificados problemas na instalação dos relatórios 800 nem nos LOGs. Também foram executados os seguintes ajustes sem resolução do cenário:

- atualização do arquivo gerador da 800;
- remoção da porta 8090, mantendo somente a 9090 para evitar conflito;
- normalização de dados, após identificação de divergência entre os parâmetros da nuvem e a tabela PCPARAMETROS.

Mesmo com esses ajustes, a falha permaneceu.

A evidência técnica aponta como causa provável um bloqueio de região na rede do cliente, impedindo o acesso pelo Workspace/AWS. Isso se sustenta porque:

- com VPN e com uma máquina utilizando rede na região brasileira, o endereço `http://vpn.root.net.br:9090/admin` acessa normalmente;
- no Workspace, o acesso não ocorre;
- em comparação com outros clientes, como MEGGA e HOTBEL, o acesso pelo Workspace está funcionando normalmente;
- o maxGestão precisa realizar esse acesso via AWS, e normalmente essa conexão precisa estar liberada na rede do cliente.

### Ação recomendada
Solicitar ao cliente a verificação de possíveis bloqueios por região, liberando o acesso externo também para uma máquina fora do país, especificamente na região de Virginia (USA).

### Próximo passo, se persistir
Caso a liberação seja realizada e o problema continue, a recomendação é reinstalar o serviço dos REL 800, com:

- limpeza de pastas e configurações desnecessárias;
- instalação da versão mais recente dos REL 800 com o instalador novo.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 416107
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
