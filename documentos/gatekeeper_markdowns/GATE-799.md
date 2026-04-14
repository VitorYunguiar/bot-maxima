# GATE-799 - Comissão divergente do resumo de vendas e Winthor

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Comissão
- Natureza: Dúvida
- Atualizado em: 2025-02-18T09:17:24.450-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxPedido;
>> Buscar resumo de vendas;
>> Verificar campo "Prev. Comissão de venda";
>> Atualizar menu na tela inicial;
>> Verificar campo "Comissão"

## Resultado apresentado
O valor diverge entre informações do próprio maxPedido.

## Resultado esperado
Valores iguais

## Descrição
A comissão apresentada acima do gráfico na tela inicial apresenta um valor divergente do que é apresentado no resumo de vendas/Winthor. O valor diverge entre informações do próprio maxPedido.

Em anexo, prints dos valores apresentados ontem e prints dos valores apresentados hoje.

Na tela inicial: R$1060,00
No Resumo de vendas/Winthor: 1614,54

Login: atitude.329

## Comentarios do Gatekeeper

### 1. 2025-02-14T13:38:17.584-0300 | Filipe do Amaral Padilha

Na tela a informação de comissão bate com o resumo de vendas, porém o filtro selecionado deve ser "Mês atual", ocorre tanto na tela inicial e no resumo agora o RCA pode escolher o filtro referente aos dados apresentados.

O script que gera a informação tela inicial da Comissão no nosso backend vem do
SELECT * FROM MXSSCRIPTS m WHERE OBJETO LIKE '%REQ_MXSRESUMOVENDASDETALHE%';
MXSRESUMOVENDASDETALHE | REQ_MXSRESUMOVENDASDETALHE | REQUEST

É a soma do campo VLCOMISSAOVENDA.

Já sobre a do Resumo de vendas, vem do script SELECT * FROM MXSSCRIPTS m WHERE OBJETO LIKE '%REQ_MXSRESUMOVENDAS%';

MXSRESUMOVENDAS | REQ_MXSRESUMOVENDASE | REQUEST

E todos rodam diretamente no banco local e podem ser comparados somente à Rotina 1249

--Há casos que as notas podem estar divergentes e pode ser necessário recálculo das notas

A comparação da comissão do aplicativo com a comissão da rotina 1248 não é válida porque a aplicação não valida comissão por liquidez, somente a comissão 'pura', enquanto nessa rotina do Winthor são validadas devoluções e outros fatores de deduções do Winthor.

O que geralmente os clientes fazem é criar um relatório na rotina 800 que traz a informação pro rca, aí ele consegue emitir diretamente pelo apk e não vai haver divergência dos valores

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 424104
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "A divergência de comissão no maxPedido" — o texto-fonte não menciona explicitamente 'maxPedido'. | "Pela análise, a conferência correta deve ser feita com o filtro 'Mês atual' selecionado tanto na tela inicial quanto no resumo de vendas" — o texto-fonte diz que o filtro deve ser 'Mês atual', mas também afirma que agora o RCA pode escolher o filtro referente aos dados apresentados; a formulação como regra fixa de conferência extrapola um pouco. | "Os scripts envolvidos rodam diretamente no banco local, o que reforça essa limitação de comparação." — a parte 'o que reforça essa limitação' é interpretação não explicitada no texto-fonte. | "Se ainda houver divergência, verificar possível inconsistência nas notas e executar o recálculo" — o texto-fonte diz que pode ser necessário recálculo das notas em alguns casos, mas não apresenta isso como procedimento condicional direto nem instrução operacional. | "para emissão direta pelo APK e evitar divergências de apresentação" — o texto-fonte diz que não vai haver divergência dos valores, não especificamente 'divergências de apresentação'.
