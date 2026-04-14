# GATE-631 - Plano de pagamento vinculado ao cliente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXPED - Plano de Pagamento
- Natureza: Dúvida
- Atualizado em: 2025-01-14T13:17:15.220-0300

## Contexto do Problema

## Passos para reproduzir
Login - OPTIMI.977
Acessar cliente 4071, ou qualquer cliente.

## Resultado apresentado
Cliente esta questionando que todos os cliente no cabeçalho do pedido esta aparecendo plano de pagamento de 7 dias.

## Resultado esperado
Que apareça o plano vinculado ao cliente

## Descrição
Foi explicando para cliente que:

o plano de pagamento cadastro desse cliente foi excluído, então ele não tem nem um plano de pagamento vinculado a ele, mas o plano de cobrança dele que e o O748 (COBRANCA OPTIMI ) ainda esta ativo, esse plano de cobrança é vinculado a outros planos de cobranças. Em resumo, por padrão vai buscar o que tiver vinculado ao plano de cobrança.

Recomendo você trocar o plano de cobrança e de pagamento desse cliente, assim ele vai buscar o que tiver vinculado a ele.

O comportamento padrão do aplicativo é buscar o plano de pagamento e o plano de cobrança configurados diretamente no cadastro do cliente.

No caso específico do cliente X, ele está vinculado a um plano de pagamento inativo (plano Y). Por isso, o aplicativo busca automaticamente o primeiro plano de pagamento e cobrança ativo que o RCA possui acesso para utilizar com este cliente.

Recomendamos que você compare este cliente X com outro cliente que esteja funcionando da forma desejada. Isso ajudará a identificar as diferenças de configuração no ERP.

A regra de qual plano será carregado por padrão é definida diretamente no ERP, na Rotina 302. É lá que você configura o plano de cobrança e pagamento para cada cliente

*_Só que cliente está questionado o por que esta aparecendo para todos os clientes o no cabeçalho do pedido plano de 7 dias._*

## Comentarios do Gatekeeper

### 1. 2025-01-14T13:17:15.215-0300 | Filipe do Amaral Padilha

Quando o cliente não trabalha com MXSCOBPLPAG e MXSPLPAGCLI, então a aplicação carrega o plano de pagamento inicial cadastrado no cliente (MXSCLIENT campos CODPLPAG e CODCOB);

Se o plano não estiver ativo, existir alguma restrição de uso do plano no cliente ou o RCA não possuir acesso, então não deixa nem iniciar o pedido.

Caso o cliente use o vínculo da MXSCOBPLPAG, então o sistema carrega seguindo a ordenação do menor plano de pagamento e cobranças que o cliente e RCA possuem acessos para utilizar.

Como no caso do cliente 4076, ele possui no cadastro da MXSCLIENT o plano 133 e codcob O748. Se você colocar algum plano ou cobrança que o RCA possui acesso, então ele valida a regra da MXSCLIENT e a da MXSCOBPLPAG em conjunto.
O que carrega é a ordenação dos planos e cobranças que o RCA possui acesso. No caso, as cobranças que ele possui acesso são:

SELECT * FROM MXSACESSODADOS WHERE CODDADOS = 2
- ANT DEPOSITO ANTECIPADO
- BNF BONIFICACAO
- O748 COBRANCA OPTIMI PROM
- COBRANÇA PROMOVET OPTIMI
- SENT ENTREGA FUTURA

O plano 133 ele não existe na base do RCA SELECT * FROM MXSPLPAG WHERE CODPLPAG IN('133').

Então o sistema nesse caso carrega a cobrança direto ao abrir o pedido "O748 COBRANCA OPTIMI PROM" e já carrega os planos que o RCA e cliente possuem acesso ordenando por CODPLPAG.

Se o RCA não tivesse acesso a nenhuma cobrança ou plano então carregaria simplesmente a ordenação do CODCOB e CODPLPAG menor conforme os acessos e a tabela MXSCOBPLPAG (Lembre que nesse caso está usando a MXSCOBPLPAG, se não estivesse usando ele validaria a MXSCLIENT primeiro e daria erro para abrir o pedido)

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 416716
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Isso explica por que pode aparecer no cabeçalho um plano padrão de 7 dias para os clientes afetados' — o texto-fonte não menciona plano padrão de 7 dias nem clientes afetados. | 'o sistema está assumindo o primeiro plano disponível pela ordenação dos acessos, e não o plano cadastrado no cliente' — o texto-fonte diz que, usando MXSCOBPLPAG, carrega pela ordenação dos planos/cobranças com acesso, mas não formula explicitamente essa conclusão geral nesses termos. | 'Responsabilidade da correção: Ajuste no ERP' — o texto-fonte não atribui responsabilidade da correção ao ERP. | 'Ação recomendada' com itens como 'ajustar no cliente', 'reproduzir a abertura do pedido após o ajuste' — são recomendações não presentes no texto-fonte.
