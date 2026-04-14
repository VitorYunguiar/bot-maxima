# GATE-900 - Praça de atendimento não oculta do cadastro

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Cadastro de Cliente - APK
- Natureza: Dúvida
- Atualizado em: 2025-03-06T08:40:58.514-0300

## Contexto do Problema

## Passos para reproduzir
Video em anexo.

## Resultado apresentado
APK continua a apresenta obrigatoriedade para preenchimento de praça.

## Resultado esperado
Se foi desmarcado na central, na APK não deveria obrigar o preenchimento do campo.

## Descrição
Cliente deseja impedir o RCA de cadastrar a praça de atendimento no cadastro do cliente via APK, porem mesmo desmarcando a obrigatoriedade e marcando a flag de ocultar o campo na central de configurações ela continua apresentando obrigatoriedade na APK.

Login: goyaco.teste

## Comentarios do Gatekeeper

### 1. 2025-03-06T08:27:04.409-0300 | Filipe do Amaral Padilha

O cadastro da praça é obrigatório, no próprio Layout da TOTVs consta como obrigatório envio do CODPRACA na tabela PCCLIENTFV da integração com o Winthor.

No maxPedido também é obrigatório a praça para carregamento de demais informaçõe sobre os preços dos produtos, mesmo sendo de Outros ERPs.

Na central o campo tem a utilidade de ser permitido edição em novos cadastros e/ou edição; A opção de ocultar é apresentada devido ao padrão genérico de exibição da Central.

Nesse caso acredito que nem sugerir melhoria cabe nesse contexto, porque a integração com o ERP força que um cadastro de praça seja definido.

Uma opção que eles têm é tornar o código da praça padrão e inalterável pelo RCA no maxPedido. Com os Parâmetros COD_PRACA_PADRAO e BLOQUEIA_PRACA_PADRAO somado a configuração da Central no campo de "praça de atendimento".

Assim o RCA não pode alterar e uma praça padrão sempre é enviada via integração do maxPedido para o Winthor.

## Resposta Canonica

**Conclusão canônica**

O comportamento é esperado no cenário informado. Mesmo com a obrigatoriedade desmarcada e com a opção de ocultar o campo na Central, a **praça de atendimento continua sendo exigida** porque a integração com o **ERP/Winthor** requer o envio do **CODPRACA** na tabela **PCCLIENTFV**. Além disso, no **maxPedido**, a praça também é obrigatória para o carregamento das informações de preços dos produtos, inclusive em cenários com outros ERPs.

**Análise objetiva**
- No layout da TOTVS, o envio do **CODPRACA** na **PCCLIENTFV** é obrigatório na integração com o Winthor.
- No maxPedido, a praça é necessária para carregar informações relacionadas a preços dos produtos.
- Na Central, esse campo serve para permitir edição em novos cadastros e/ou em edição.
- A opção de **ocultar** existe por um padrão genérico de exibição da Central, mas **não remove a exigência funcional** da praça quando a integração depende desse dado.
- Portanto, a configuração da Central **não elimina** a necessidade da praça quando o ERP força sua definição.

**Recomendação**
Para atender à necessidade do cliente sem permitir alteração pelo RCA, a orientação é:
- definir uma **praça padrão** no maxPedido;
- bloquear a alteração dessa praça pelo RCA;
- combinar essa configuração com o campo de **praça de atendimento** na Central.

**Parâmetros envolvidos**
- `COD_PRACA_PADRAO`
- `BLOQUEIA_PRACA_PADRAO`

**Próximo passo**
Configurar uma praça padrão e bloquear sua alteração pelo RCA no maxPedido, garantindo que uma praça válida seja sempre enviada na integração com o Winthor.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 427925
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
