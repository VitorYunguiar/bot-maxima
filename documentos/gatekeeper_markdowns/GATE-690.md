# GATE-690 - Preenchimento automático de informações no pedido para consumidor final

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Carlos Henrique Rezende Marques
- ERP do cliente: Winthor
- Assunto: MXPED - Pedido/Orçamento - Editar
- Natureza: Dúvida
- Atualizado em: 2025-01-24T18:02:11.911-0300

## Contexto do Problema

## Passos para reproduzir
>>Logar no maxPedido em base do zero ou base em anexo
>>Iniciar pedido para consumidor final
>>Incluir um item
>>Salvar e bloquear o pedido

## Resultado apresentado
Será aberta uma nova tela onde deve se colocar a informações do cliente
Apenas  'Cliente', 'CPF/CNPJ', 'Cidade/UF' e 'Email' são preenchidos

## Resultado esperado
O cliente deseja que todas sejam preenchidas com as informações padrão cadastradas para o cliente 'consumidor final' e que o RCA consiga alterar apenas o que seja necessário a eles.

## Descrição
>>Ao realizar pedido para consumidor final aparece o campo 'consumidor final' onde se preenche com os dados do cliente, porém o cliente deseja que os campos como endereço, numero, bairro, cep, telefone , etc sejam completos automaticamente, porém pelo que vi apenas os campos 'Cliente', 'CPF/CNPJ', 'Cidade/UF' e 'Email' são preenchidos.

Estou abrindo este ticket para que seja verificado se existe algum modo de fazer com que na aba de consumidor final todos os campos podem ser preenchidos e o RCA apague e substitua apenas o necessário a eles.

## Comentarios do Gatekeeper

### 1. 2025-01-24T18:02:11.910-0300 | Filipe do Amaral Padilha

A gente faz preenchimento das informações citadas
"endereço, numero, bairro, cep, telefone"

porém a gente busca de outros campos do cadastro do cliente, no caso se for Winthor, o cliente teria de cadastrar as informações na Rotina 302, referente a endereço comercial dos clientes consumidores finais.

Se for cliente OERPs, seria no endpoint MXSCLIENT os campos:

BAIRROCOM
ENDERCOM
NUMEROCOM
CEPCOM
TELCOM

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 419036
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A afirmação de que o preenchimento automático adicional do consumidor final já contempla, além de Cliente, CPF/CNPJ, Cidade/UF e Email, esses outros campos não está no texto-fonte. | A afirmação de que esses dados não são digitados diretamente nessa tela não está explicitamente no texto-fonte. | A afirmação de que, quando não são preenchidos automaticamente, a causa mais provável é que as informações não estejam cadastradas corretamente na origem não está no texto-fonte. | A recomendação de validar novamente o preenchimento automático na aba de consumidor final não está no texto-fonte. | A referência à aba de consumidor final não aparece no texto-fonte.
