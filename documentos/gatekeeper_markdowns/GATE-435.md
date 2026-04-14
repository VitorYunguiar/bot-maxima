# GATE-435 - desativar PWA

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Leandro Luiz Fischer
- ERP do cliente: Winthor
- Assunto: MXGESN - Instalação PWA
- Natureza: Dúvida
- Atualizado em: 2024-12-03T12:28:51.338-0300

## Contexto do Problema

## Passos para reproduzir
N/A

## Resultado apresentado
N/A

## Resultado esperado
N/A

## Descrição
Segue abaixo relato da cliente, a qual deseja desativar o PWA, pois tem gerado dificuldades em sua operação.

"Bom Dia! Existe uma forma de desabilitar o novo painel?

Motivo: Quando efetua o login no gestão, pede novamente para efetuar o login e o pessoal estão reclamando."

## Comentarios do Gatekeeper

### 1. 2024-12-03T10:36:14.167-0300 | Filipe do Amaral Padilha

Atualmente para desativar a opção do maxGestão web redirecionar para o PWA web com as opções dos dashboards novos, teria que fazer manualmente via banco a configuração da seguinte forma:

--Confere os usuários que precisam ter a opção desligada
SELECT MOSTRARNOVIDADES, MXSUSUARIOS.* FROM MXSUSUARIOS WHERE CODUSUARIO IN();

--Marca para não mostrar as novidades:
UPDATE MXSUSUARIOS SET MOSTRARNOVIDADES = 'N' WHERE CODUSUARIO IN(); COMMIT;

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410006
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "A solicitação da cliente" | "pois ao efetuar login no gestão está sendo solicitado um novo login, o que tem gerado dificuldade operacional" | "essa desativação não é feita por parâmetro na aplicação" | "Responsável pela execução: banco de dados, manualmente"
