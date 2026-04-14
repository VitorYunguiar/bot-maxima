# GATE-324 - Divergencia de base, encaminhar a n3

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: João Pedro Faria Cabral [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Produto - Não Aparece
- Natureza: Erro
- Atualizado em: 2024-11-13T10:12:20.073-0300

## Contexto do Problema

## Passos para reproduzir
jotabe.helen
token

Qualquer cliente
Trocar para filial 2 e filial nf 2
BASE DO ZERO = PRODUTOS
BASE CLIENTE = SEM PRODUTOS

## Resultado apresentado
Divergencia de base

## Resultado esperado
Carga

## Descrição
Ja realizei carga de DTATUALIZ e alteração no CODOPERACAO
sincronizei na base da RCA e não aparecem os produtos

Passei muito tempo tentando conectar no celular dela, não deu certo, maxViewer não instala la.

Tratamos por fotos, ela foi me mandando foto a foto das telas que ela se mexia, de fato mudar o DTATUALIZ e o CODOPERACAO não foi suficiente para fazer os produtos da filial2 e filialnf2 funcionarem

*BASE DO ZERO FUNCIONA NORMAL.*

## Comentarios do Gatekeeper

### 1. 2024-11-13T10:12:20.071-0300 | Filipe do Amaral Padilha

Os produtos não estavam aparecendo por dois motivos:

Haviam itens da MXSPRODFILIAL que não desceram para a base da RCA referente a Filial 2.

E também tem uma restrição de venda código 10, que impede a visualização dos produtos na filial 2, por ser uma restrição geral para a filial 2.

Se ela voltar reclamando que os itens não estão sendo exbidos, pode ser que seja um cliente pessoa jurídica e ela esteja vendendo na filial, e então a restrição de código 10 vai restringir o acesso.

Para ela mudar a restrição de venda pode estar fazendo na Rotina 391 do Winthor.

Como ela limpou a base, então os dados da MXSPRODFILIAL foram novamente sincronizados e por isso os itens podem ter voltado a aparecer para clietes PF.

Não passar para o cliente:

Foi feito debug e visto no SQL o motivo dos itens não serem exibidos.

Também foram feitos vários testes e hoje, ao baixar a base do zero, independente da versão, os itens não estavam sendo exibidos devido validação da restrição de venda.

O João me informou que a cliente limpou a base, então se ela tentar vender para cliente pessoa Jurídica, os itens não serão exibidos, porém se for Pessoa Física, vai aparecer na Filial 2.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 406653
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: A menção a 'Filial NF 2' não aparece no texto-fonte. | A afirmação de que 'a alteração de DTATUALIZ e CODOPERACAO não foi suficiente para normalizar a exibição dos produtos' não consta no texto-fonte.
