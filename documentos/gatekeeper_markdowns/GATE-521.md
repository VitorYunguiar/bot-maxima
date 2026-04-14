# GATE-521 - Divergencia entre a PCPLPAGCLI e a MXSPLPAGCLI

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Plano de Pagamento
- Natureza: Dúvida
- Atualizado em: 2024-12-18T09:34:11.453-0300

## Contexto do Problema

## Passos para reproduzir
>>Baixar a base do RCA 55 em anexo DONACOTA.SAULO, base em anexo ou base do zero
>>Iniciar pedido no cliente 10201
>>Cobrança Bk (COBRANCA BANCARIA)

## Resultado apresentado
>>Aparecem apenas dois planos de pagamento, 1 e 3
>>Verificando na MXSPLPAGCLI realmente aparecem apenas os registros 1 e 3
>>Porém na PCPLPAGCLI aparecem 4 registros

## Resultado esperado
>>Tanto na MXSPLPAGCLI  quanto no aplicativo deve aparecer os planos de pagamento para o cliente

## Descrição
>>Poucos planos de pagamento esão aparecendo para os cliente, exemplo 10201

>>Na PCPLPAGCLI existem 4 registros para esse cliente

>>Na MXSPLPAGCLI existem apenas dois registros

>>Esta divergência está fazendo com que os planos de pagamento não apareçam para os RCA's

## Comentarios do Gatekeeper

### 1. 2024-12-18T09:08:52.058-0300 | Filipe do Amaral Padilha

Não passar esses dados para o cliente:
Sobre a MXSPLPAGCLI, provavelmente quando a implantação fez a
carga de filial, não habilitou a opção 'Clientes', com isso os dados de vínculo do cliente (PCPLPAGCLI) não desceram para a nuvem.

Outra possibilidade é que esse registro nunca foi alterado porque a trigger muda ele. Pode ser q na carga não subiu, por algum motivo: Por exemplo: cliente não fazia parte da regra; plano não fazia parte da regra.

Para resolver então eu fiz a carga de dados, como eles são T-Cloud está demorando para descer os registros, mas eu vou fechar o ticket e é só esperar os registros caírem na:
SELECT * FROM MXSPLPAGCLI WHERE CODCLI IN(10201);

Se quiser acompanhar via postman o comando é:

SELECT TABELA, COUNT(*) FROM PCMXSINTEGRACAO WHERE STATUS = -1 GROUP BY TABELA;

A partir daqui pode passar para o cliente se quiser:

Para resolver o problema de divergência da PLPAGCLI foi feita normalização de dados. Depois que os registros finalizarem a integração, basta sincronizar o maxPedido.

Além desse ponto, tem alguns objetos inválidos lá no banco do cliente no nosso schema porque fizemos uma melhoria recentemente que não teve as tabelas criadas.

Então eles precisam rodar esse arquivo:
SCRIPT_TCLOUD_MAXIMA.txt

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 412818
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Identificada divergência entre as tabelas de vínculo de plano de pagamento do cliente 10201: na `PCPLPAGCLI` existem 4 registros, enquanto na `MXSPLPAGCLI` existem apenas 2" — o texto-fonte não informa quantidades de registros nem compara diretamente essas tabelas. | "refletindo diretamente no aplicativo, que apresenta somente os planos 1 e 3 para a cobrança Bk" — não há menção a aplicativo, planos 1 e 3, nem cobrança Bk no texto-fonte. | "Consultas utilizadas na validação" — o texto-fonte traz consultas para acompanhar/consultar, mas não afirma que foram usadas na validação. | "Acompanhar a integração pela `PCMXSINTEGRACAO`" — o texto-fonte diz "Se quiser acompanhar via postman o comando é...", não afirma explicitamente essa ação como recomendação formal pela tabela em si.
