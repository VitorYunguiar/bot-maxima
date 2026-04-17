# GATE-32 - Preço unitário na tela de negociação

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Max Lobo Magalhães de Aguia
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Embalagem
- Natureza: Dúvida
- Atualizado em: 2024-09-06T15:59:24.230-0300

## Contexto do Problema

## Passos para reproduzir
>> Logar no maxPedido;
>> iniciar pedido para cliente 1718;
>> Abrir produto 941;
>> Verificar que não é exibido o valor unitário do produto, apenas o valor total;

## Descrição
Cliente quer que seja exibido o preço unitário na tela de negociação. Ja foram criados os parâmetros EXIBIR_VALOR_UNITARIO e EXIBE_PRECO_UNIT_LISTAGEM porem ainda exibe apenas o valor total. Alterado na base da APK o PVENDA para 10 e o MXSEMBALAGEM.QTUNIT para 12 na intenção de verificar se era a falta de informação de valor unitário e quantidade de unidades na embalagem porem o campo segue inalterado.

Login: MBCOMERCIO.ELIANE
Cliente: 1718
Produto 941;

## Comentarios do Gatekeeper

### 1. 2024-09-06T15:59:24.228-0300 | Filipe do Amaral Padilha

Para o cliente trabalhar com a informação "Valor Un:" o primeiro passo é desativar a permissão "Exibir Valor Total" do cadastro do RCA ou do Perfil de usuários.

Em seguida, o parâmetro EXIBIR_VALOR_UNITARIO deve ser configurado = S (Sim).

E por fim, o cliente precisa alterar a informação da quantidade Unitário do produto no cadastro da rotina 203. No banco de dados nuvem é a QTUNIT da MXSPRODUT, no banco do Winthor é a QTUNIT da PCPRODUT.

Informações técnicas:

(*Não passar para o cliente*)

Para validar o cenário, acessar o inspect e setar:

UPDATE MXSPRODUT SET QTUNIT = 20 WHERE CODPROD IN(941)

Lembre-se de averiguar o parâmetro e a permissão.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: missing_context_sections, needs_review
- Comentarios primarios: 393292
- Secoes ausentes: Resultado apresentado, Resultado esperado
- Groundedness aprovado: nao
