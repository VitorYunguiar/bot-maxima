# GATE-388 - problemas na leitura de codigo de barras de boleto

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXPED - Títulos
- Natureza: Dúvida
- Atualizado em: 2024-11-28T10:44:44.702-0300

## Contexto do Problema

## Passos para reproduzir
>> login: viana.2
>> cliente 10177
>> compartilhar o titulo 769699-3
>> abrir o PDF gerado e tentar fazer a leitura do codigo em algum app de banco.
>> observar  os resultados.

## Resultado apresentado
o codigo de barras do arquivo gerado, não está sendo lido pelo app.

## Resultado esperado
é esperado que o codigo de barras presente no arquivo, seja lido sem problemas.

## Descrição
Senhores, ao analisarmos o cenário relatado estou observando o mesmo comportamento relatado pela cliente: ao gerarmos um boleto, o código de barras está com problemas de leitura, fiz um teste lendo o boleto em aplicativos de banco diferentes e a leitura não aconteceu em nenhum app.

## Comentarios do Gatekeeper

### 1. 2024-11-26T14:14:03.544-0300 | Filipe do Amaral Padilha

Foi feito teste com o documento anexado no ticket do gate e a leitura do código de barras ocorreu com sucesso. Testei no aplicativo do Flash e Banco Itaú.

Também fiz o teste com o boleto gerado do banco Safra pelo cliente, que está anexado no ticket principal e capturou o boleto com sucesso.

Além disso, baixei a base do RCA que está anexada no ticket de GATE e fiz todos os testes que eu sabia sobre compartilhamento de boleto referente ao número único e ao código de barras começando por:

1° teste: Acessar a aba de Consultas >> Títulos Abertos e apertar em "copiar" cima da linha digitável: Depois acessar o aplicativo de pagamento e colar; Boleto gerado com sucesso.

2° teste: Acessar a aba de Consultas >> Títulos Abertos e apertar em "Compatilhar" Será gerado um arquivo com o código de barras em um boleto gerado pela Máxima: Depois acessar o aplicativo de pagamento e colar; Boleto gerado com sucesso.
------------------------------------------------------------
Houve um teste que eu fiz em base zerada com o título duplicata número 682733 cuja linha digitável é : 42297.17808  00020.041463  00372.861724  1  93540000078349 e nesse teste deu um erro de CIP. A msg que o banco me retornou foi: "Por favor, entre em contato com a emissora do boleto para solucionar o problema de cadastro na CIP".

Eu fiz outro teste com um boleto 7609430-3 e ele está vencido a 36 dias e também gerou com sucesso.

Então dito isso eu identifiquei um padrão: Os boletos vencidos a muitos dias estão apresentando esse erro no CIP.

Por exemplo: boleto 688057 vencido a 535 dias, deu o mesmo erro da mensagem que citei acima.

Com isso eu pensei o seguinte: De fato os números das linhas digitáveis em boletos antigos está com defeito e seria um problema de geração dessa informação no ERP, porque a gente só integra para a nuvem esse campo de linha digitável.Fica no banco local na PCPREST no campo LINHADIG

SELECT * FROM ERP_MXSPREST WHERE DUPLIC IN('682733');--42297.17808  00020.041463  00372.861724  1  93540000078349

Na nossa nuvem LINHADIG da ERP_MXSPREST que é a mesma que é utilizada no maxPedido. Nesse sentido não seria um problema do força de vendas e sim da informação do título que é gerado no ERP e apensas integra com a Máxima.

É um problema da informação em si e nesse caso eu não sei nem como poderia orientar o cliente para ele resolver a questão, isso é algo que ele vai precisar verificar no ERP.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 408743
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Após a análise, não foi confirmada falha geral no compartilhamento ou na leitura do código de barras pelo força de vendas/Máxima." — o texto-fonte relata vários testes com sucesso, mas não afirma explicitamente essa conclusão geral nesses termos. | "Conclusão técnica: há indício de problema na informação da linha digitável gerada/cadastrada no ERP para boletos antigos ou vencidos há muitos dias." — o texto-fonte traz isso como interpretação/opinião do autor ('eu pensei o seguinte'), não como conclusão confirmada. | "A responsabilidade indicada é do ERP" — o texto-fonte sugere que não seria problema do força de vendas e sim da informação gerada no ERP, mas ainda em tom de hipótese/opinião, não como fato plenamente confirmado. | "na nuvem, o campo utilizado no maxPedido é ERP_MXSPREST.LINHADIG" — o texto-fonte diz 'Na nossa nuvem LINHADIG da ERP_MXSPREST que é a mesma que é utilizada no maxPedido', mas a formulação exata como campo utilizado no maxPedido não está tão claramente estabelecida quanto na resposta. | "Encaminhamento: solicitar validação no ERP da geração/cadastro da linha digitável..." — trata-se de recomendação/encaminhamento formulado na resposta, não presente literalmente no texto-fonte.
