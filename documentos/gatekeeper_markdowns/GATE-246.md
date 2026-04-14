# GATE-246 - valores divergentes ao filtrar com deduções

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXGESN - Painel Geral - Dados Divergentes do ERP
- Natureza: Dúvida
- Atualizado em: 2024-10-30T12:08:19.062-0300

## Contexto do Problema

## Passos para reproduzir
realizar os filtros conforme a descrição apresentada, no maxgestão e na rotina de resumo de faturaento e comparar os resultados.

## Resultado apresentado
o gestão traz dados divergentes das deduções a serem aplicadas no filtro.

## Resultado esperado
é esperado que os dados entre os dois locais estejam equivalentes, uma vez que os parametros de consulta e a base de dados dos dois locais são os mesmos

## Descrição
Senhores, ao analisar o cenário da demanda, estamos observando divergencias entre valores, de forma inesperada. Quando o filtro aplicado, não possui deduções sendo aplicadas, os valores ficam equivalentes e adequados para venda faturada:
!image-2024-10-29-17-30-36-254.png!

!image-2024-10-29-17-30-55-919.png!

quando se aplicam deduções aos filtros para se obter valores líquidos na apresentação, as divergências começam a serem observadas:

!image-2024-10-29-17-32-19-360.png!

!image-2024-10-29-17-32-40-469.png!

não foi observado problemas relacionados a tipos de venda nas filtragens efetuadas.

## Comentarios do Gatekeeper

### 1. 2024-10-30T11:55:06.155-0300 | Filipe do Amaral Padilha

Foi enviado para N3

Foi feita carga dos dados no banco local do cliente e mesmo assim os dados não batem acredito que seja algum problema com as devoluções calculadas na Rotina 111 e em relação ao que temos para calcular na nuvem.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 403882
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: 'Pelo relato técnico' — o texto-fonte não menciona relato técnico, apenas uma mensagem simples. | 'sem detalhamento adicional de parâmetros ou consultas para validação objetiva' — o texto-fonte não menciona parâmetros, consultas ou validação objetiva. | 'Conclusão canônica' com 'deve ser tratada como possível diferença no cálculo das devoluções da Rotina 111 versus o cálculo executado na nuvem' — embora compatível com a suspeita do texto, a formulação normativa 'deve ser tratada' não está explicitamente no texto-fonte. | 'Validar tecnicamente a diferença entre as devoluções calculadas na Rotina 111 e o cálculo utilizado na nuvem' — trata-se de recomendação/instrução não presente no texto-fonte. | 'Não foram fornecidos parâmetros técnicos adicionais nem SQL' — o texto-fonte não menciona SQL nem ausência de parâmetros técnicos.
