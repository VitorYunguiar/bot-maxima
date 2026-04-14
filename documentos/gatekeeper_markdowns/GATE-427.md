# GATE-427 - Parâmetros cadastro de cliente

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Não Informado
- Assunto: MXPED - Parametrização
- Natureza: Dúvida
- Atualizado em: 2024-12-02T16:48:51.854-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Bom dia Filipe / Carlos,

O cliente LDF abriu uma demanda questionando sobre alguns parâmetros da central de configurações que ele não sabe o  funcionamento, e nem eu.

Gostaria de ajuda pra entender o que fazem esses parâmetros de "cadastro de cliente".

## Comentarios do Gatekeeper

### 1. 2024-12-02T16:48:17.863-0300 | Filipe do Amaral Padilha

Todas essas informações vão do maxPedido via integração para o Winthor e chegam na PCCLIENTFV que é a tabela intermediária da integração. A tabela que finaliza o cadastro é a PCCLIENT que a TOTVs grava, a gente vai somente até a PCCLIENTFV.

Todos esses parâmetros são validados somente por usuário ou perfil de usuários. Não tem para geral e nem por filial:

"Cadastro de cliente: Valor do credito do cliente": Serve para definir um limite de crédito disponível para todo novo cliente cadastrado pelo RCA através do maxPedido. (O RCA não pode alterar essa informação, vai padrão da integração do maxPedido para o Winthor);

"Cadastro de cliente: Valor padrão para Calcular ST": Serve para definir se é calculado ST no cliente (O RCA não pode alterar essa informação, vai padrão da integração do maxPedido para o Winthor);

"Cadastro de cliente: Valor padrão para Cliente contribuinte": Serve para vir marcado por padrão se o cliente é contribuinte ou não, essa informação é exibida na tela de cadastro de clientes do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das permissões do usuário.

"Cadastro de cliente: Valor padrão para Plano de Pagamento": Serve para vir padrão um plano de pagamento cadastrado para o cliente, essa informação é exibida na tela de cadastro de clientes dentro do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das configurações do formulário de cadastros da Central (Configurações > Configurações > Formulários).

"Cadastro de cliente: Valor padrão para Praca de Atendimento":  Serve para vir padrão uma praça cadastrado para o cliente, essa informação é exibida na tela de cadastro de clientes dentro do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das configurações do formulário de cadastros da Central (Configurações > Configurações > Formulários).

"Cadastro de cliente: Valor padrão para Simples Nacional": Serve para vir marcado por padrão se o cliente é simples nacional ou não, essa informação é exibida na tela de cadastro de clientes do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das permissões do usuário.

"Cadastro de cliente: Valor padrão para Tipo de Cobranca": Serve para vir padrão uma cobrança cadastrada para o cliente, essa informação é exibida na tela de cadastro de clientes dentro do maxPedido. O RCA pode alterar ela caso ela não esteja ocultada através das configurações do formulário de cadastros da Central (Configurações > Configurações > Formulários).

"Cadastro de cliente: Valor padrão para Tipo de Empresa": Por padrão vem "P", eu não achei essa informação para ser alterada pelo aplicativo, mas eu acredito que ela vai assim padrão para que não ocorra problemas com a integração com o Winthor. E então chega no campo TIPOEMPRESA na PCCLIENTFV.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409885
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Segue a orientação canônica sobre os parâmetros de Cadastro de Cliente na Central de Configurações." | "Para o cliente LDF, a orientação é informar o comportamento acima e validar:" | A menção específica ao "cliente LDF" não aparece no texto-fonte. | "Se a dúvida envolver a gravação final na PCCLIENT, é necessário acionar a TOTVs, pois essa etapa está fora do escopo analisado."
