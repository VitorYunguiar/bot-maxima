# GATE-484 - Relatorio 8012 não é gerado

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatório - 800
- Natureza: Dúvida
- Atualizado em: 2024-12-11T09:39:02.743-0300

## Contexto do Problema

## Passos para reproduzir
>> Acessar maxGestão;
>> Buscar relatório 8012 e gerar com os mesmos filtros.

## Resultado apresentado
Exibido apenas uma faixa vermelha de erro e o log na pasta do gerador informa somente "O relatório não foi gerado." sem mais informações.

## Resultado esperado
Relatório sendo gerado.

## Descrição
O relatório não é gerado no maxGestão, e o unico log que aparece na pasta GERADOR00 > LOGS informa apenas "O relatório não foi gerado."

No Winthor o relatório é gerado normalmente.

Relatório 8012

## Comentarios do Gatekeeper

### 1. 2024-12-11T09:39:02.742-0300 | Filipe do Amaral Padilha

Se tratava de atualização dos relatórios na pasta interna, na máquina onde foi instalado o IIS. Conforme conversamos também, no caso do rel 8012, está tendo um erro de SQL e se quiser mostrar o log desse erro na tela do maxGestão, teria de ser uma melhoria

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 411540
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'O comportamento ocorre por conta da atualização dos relatórios na pasta interna da máquina onde o IIS foi instalado.' — o texto-fonte menciona a atualização dos relatórios, mas não afirma explicitamente que essa é a causa do comportamento. | 'No maxGestão, a geração do relatório falha' — o texto-fonte não diz que a geração do relatório falha. | 'o log disponível informa apenas que “O relatório não foi gerado”' — essa mensagem não aparece no texto-fonte. | 'Atualmente, o erro de SQL não é exibido na tela do maxGestão.' — o texto-fonte diz apenas que, se quiser mostrar o log desse erro na tela do maxGestão, teria de ser uma melhoria; não afirma explicitamente o estado atual nesses termos. | 'Ação recomendada: Atualizar os relatórios na pasta interna da máquina onde foi instalado o IIS.' — o texto-fonte menciona que se tratava de atualização dos relatórios, mas não formula isso como recomendação ou próximo passo. | 'O maxGestão não mostra na tela o log do erro de SQL.' — inferência não explicitada literalmente no texto-fonte. | 'Realizar a atualização dos relatórios na pasta interna da máquina com IIS' como próximo passo — não está explicitamente indicado no texto-fonte como próximo passo.
