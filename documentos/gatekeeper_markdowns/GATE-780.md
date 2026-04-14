# GATE-780 - Não está gerando a nota em pedidos do pronta entrega

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Heloysa Santana Rocha
- ERP do cliente: Winthor
- Assunto: MXPED - Central de Configurações
- Natureza: Dúvida
- Atualizado em: 2025-02-12T16:55:53.500-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar o aplicativo
>>Importar a base anexada
>>Ir na tela de pedidos
>>Duplicar o pedido 2582580831
>>Salvar e enviar o pedido
>> Irá ver que o pedido é enviado mais logo após um tempo retorna um x no pedido e a crítica anexada.

Login: grb.258
senha: acesso temporário

## Resultado apresentado
Pedidos realizados utilizando o pronta entrega não está emitindo as notas.

## Resultado esperado
Que os pedidos realizados pelo pronta entrega emita as notas.

## Descrição
Ao realizar alguns pedidos pelo MaxPedido com o tipo de venda pronta entrega, não está emitindo as notas, quando realiza o pedido internamente pelo winthor as notas são emitidas normalmente.

Gostaria de apoio para entender porque os pedidos pelo força de vendas utilizando o pronta entrega está retornando essa crítica e não permitindo emitir as notas.

## Comentarios do Gatekeeper

### 1. 2025-02-12T15:41:13.172-0300 | Filipe do Amaral Padilha

Geralmente quando dá esse erro de geração de nota é alguma questão de cadastro que faltou no Winthor. Isso não é parte da Máxima o cliente precisa verificar no Winthor com a TOTVs se necessário.

Da nossa parte, sempre orientar o cliente a verificar na rotina de faturamento se está emitindo a nota de fato. Se NÃO der erro na geração da nota na rotina de faturamento, então pode ser alguma questão nossa. Mas como no caso a gente não fez nenhuma intervenção e o pedido foi processado com sucesso então foi uma questão de demora ou problema na primeira tentativa de geração da nota no ERP.

Se o Sefaz demorar para gerar a nota dá esse erro também de timeout, ou também quando não gera a nota com sucesso.

Quando dá erro assim no pedido o RCA pode reenviar o pedido, porque assim, caso a nota esteja gerada a gente vai buscar de novo. Ou então ele pode duplicar ou editar e enviar de novo o pedido.

## Resposta Canonica

**Análise canônica**

O comportamento informado está associado, em geral, a falha na geração da nota fiscal no ERP, e não houve intervenção no ambiente durante a análise. O pedido acabou sendo processado com sucesso posteriormente, o que indica cenário compatível com:

- questão de cadastro faltando no Winthor;
- demora ou problema na primeira tentativa de geração da nota no ERP;
- timeout ou demora do Sefaz na geração da nota;
- falha na geração da nota sem sucesso na primeira tentativa.

**Conclusão**
A evidência disponível aponta que a ocorrência pode estar relacionada ao processo de faturamento no Winthor/ERP. Como o pedido foi processado com sucesso sem intervenção, não há confirmação de defeito na Máxima neste caso.

**Orientação**
1. Verificar na rotina de faturamento do Winthor se a nota está sendo emitida de fato.
2. Se houver erro na geração da nota, validar cadastro no Winthor com a TOTVS, se necessário.
3. Se não houver erro na rotina de faturamento, tratar como possível questão a ser avaliada pela Máxima.
4. Quando o pedido retornar com erro, o RCA pode:
   - reenviar o pedido; ou
   - duplicar/editar e enviar novamente.

**Responsabilidade**
- Cliente: validar o processo no Winthor, com apoio da TOTVS se necessário.
- RCA: reenviar, duplicar ou editar o pedido e enviar novamente.

**Limitação da análise**
- Não foi realizada nenhuma intervenção.
- O ponto principal indicado está fora da Máxima, dependendo da validação no Winthor/ERP.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 423431
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
