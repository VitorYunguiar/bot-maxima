# GATE-412 - Relatórios maxGestão, dados divergentes

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Larissa Raquel Macêdo [X]
- ERP do cliente: Winthor
- Assunto: MXGESN - Relatórios - Dados Divergentes do ERP
- Natureza: Dúvida
- Atualizado em: 2024-11-28T15:11:59.980-0300

## Contexto do Problema

## Passos para reproduzir
Acessar maxGestão web com usuário sysmax
Ir para a aba de Relatórios
Portaexecitivo ir em "Apuração de metas"
Filial
1 - FRANCA COMERCIO DE PRODUTOS ALIM LTDA
Configuração de campanha
All items checked
Mês de apuração
11/2024
Deduzir
Apurar por	Por supervisor Por RCA's
Equipe:
2
RAFAEL DE AZEVEDO SANTOS
Representante:
2
EDMILSON GOMES DE LIMA FILHO

>> Pesquisar
>> Verificar a informação zerada do Prêmio
>> Comparar com o arquivo anexado da meta que foi apurada na rotina 3309 pelo cliente no Winthor.

## Resultado apresentado
Os dados estão divergentes quando comparados resultados do ERP (Winthor) e os dados extraídos do maxGestão, além disso, os valores que precisariam vir na aba "Prêmios" não estão subindo.

## Resultado esperado
Os dados precisariam estar o menos divergente possível e os valores presentes na aba prêmios deveriam estar aparecendo.

## Descrição
Alguns dados presentes no relatório no maxGestão estão divergentes do ERP ( os dados de valores em relação aos "prêmios" não estão subindo, assim mostrando como zerados)

## Comentarios do Gatekeeper

### 1. 2024-11-28T15:00:26.156-0300 | Filipe do Amaral Padilha

Será encaminhado para N3 para eles verificarem como é feita a apuração e se os dados estão integrando com o banco nuvem para exibir essa informação do prêmio no relatório do portal executivo

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 409315
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Foi identificado que os valores de prêmio no relatório do portal executivo estão sendo exibidos zerados. | No momento, não há causa raiz confirmada. | Também não foram informados parâmetros técnicos nem consultas SQL. | Não está confirmado se a origem da divergência está na apuração ou na integração com o banco nuvem. | Encaminhamento recomendado: direcionar para o N3, responsável por verificar a apuração e a integração dos dados com o banco nuvem para exibição do prêmio no relatório do portal executivo.
