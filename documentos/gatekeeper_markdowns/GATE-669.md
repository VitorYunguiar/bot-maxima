# GATE-669 - maxPag não realizou estorno

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido - Crítica
- Natureza: Dúvida
- Atualizado em: 2025-01-22T17:28:03.059-0300

## Contexto do Problema

## Passos para reproduzir
>>Acessar maxPag do cliente LDF
>Transações
>No filtro 'Campos extras' consultar 3320007645
>Clicar para ver as movimentações do pedido
>Observar que não tem histórico de estorno por parte do maxPag
>Observar que o valor do pedido difere do valor atendido pelo ERP

OBS: Link da base está no comentário do ticket em um link WeTransfer.

##SELECTS UTILIZADOS
SELECT NUMPEDERP, CODCLI, VLATEND, VALORTOTAL, em.* FROM MXSINTEGRACAOPEDIDO em WHERE NUMPED = 3320007652;

SELECT * FROM ERP_MXSCORTE WHERE NUMPED = 332050052 OR NUMPED = 3320007645;

## Resultado apresentado
Esse pedido foi para o ERP e teve cortes da integradora, porém esse valor do corte não foi estornado no pedido no maxPag.

## Resultado esperado
Que o valor da diferente de produtos não atendidos no corte seja estornado para o cliente.

## Descrição
Bom dia Carlos / Filipe,

Não coloquei produto gatekeeper maxPag pois não tinha, porém tinha alinhado com o Filipe para subir GateKeeper.

Acontece que no dia 10/01 foi realizado um pedido e feito o pagamento via PIX no maxPag, esse mesmo pedido foi para o ERP e teve cortes pela integradora, porém esse valor do corte não foi estornado no pedido conforme podemos observar nas movimentações do pedido pelo maxPag.

ID TRANSAÇÃO MAXPAG: TMOsfx2IW8Lo6WhipoDaLuA7Nb
NUMPEDRCA: 3320007645
NUMPED: 332050052
VALOR TOTAL NO MAXPAG: 536,73
PCPEDC.VLATEND: 353.25

Verifiquei que não gerou registro de corte dos produtos na PCCORTE, mas não sei se é algo essencial para que o maxPag realize o estorno.

## Comentarios do Gatekeeper

### 1. 2025-01-22T17:28:03.058-0300 | Filipe do Amaral Padilha

Foi feita correção no ticket de Gate mesmo a natureza correta é Erro.

--Foi feita correção direto no Gate e lançado em produção.

Existia um problema onde, o estorno do maxPag acumulava uma lista de pedidos e ele sempre processava seguindo a ordem do primeiro lançado > para o último lançado.

Ou seja no caso o pedido ID_PEDIDO = 921199, ficou no final da fila e o processamento do estorno nunca chegava nele, e haviam outros pedidos nessa condição também.

Para resolver, então foi alterada a lógica das buscas dos pedidos para estorno diretamente no Extrator. Assim que a alteração foi feita, lançamos a versão de extrator 3.1.2.458 e agora nós buscamos de forma dinâmica os pedidos para processar o estorno, garantindo que todos sejam processados corretamente conforme as pendências de estorno.

--Para conferir é só consultar no pedido. Foi gravado o log na tabela e o cliente pode conferir também no maxPag e diretamente com o cliente se o Estorno foi efetuado com sucesso. A chamada do estorno nós fizemos automaticamente via Extrator da Máxima.
SELECT * FROM MXSMAXPAYMENTMOV WHERE ID_PEDIDO IN(921199);

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 418486
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "sob responsabilidade do Gate / Extrator da Máxima" — o texto-fonte menciona correção no Gate e alteração no Extrator, mas não afirma responsabilidade nesses termos. | "Como evidência operacional" — caracterização interpretativa não explicitada no texto-fonte. | "Próximo passo recomendado" — o texto-fonte diz como conferir, mas não apresenta isso como recomendação formal de próximo passo. | "após a correção e publicação da versão 3.1.2.458 do extrator" associado à validação do pedido 921199 — o texto-fonte informa a alteração e publicação da versão, mas não vincula explicitamente essa checagem como um passo posterior nesses termos.
