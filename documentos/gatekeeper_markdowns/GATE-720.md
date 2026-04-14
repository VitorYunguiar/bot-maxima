# GATE-720 - Erro ao gerar visita avulsa

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Marcos Vinícius de Almeida Macedo [X]
- ERP do cliente: Winthor
- Assunto: MXPED - Cliente - Roteiro de Visitas
- Natureza: Dúvida
- Atualizado em: 2025-01-31T08:40:31.544-0300

## Contexto do Problema

## Passos para reproduzir
Entrar na base zero do rca e gerar a visita avulsa no painel de clientes. Importar a base do rca e realizar o mesmo processo.

## Resultado apresentado
Ao simular na base do rca, ao gerar a visita avulsa a aplicação não inicia o pedido no cliente.

## Resultado esperado
É esperado que o RCA consiga gerar a visita avulsa corretamente.

## Descrição
Cliente relata que o RCA 137 não consegue gerar a visita avulsa em nenhum cliente no aplicativo. Foi realizada a simulação do cenário em base zero, onde o problema não foi replicado, entretanto ao simular na base do RCA, o problema relatado foi apresentado.

Login para teste:
mbm.suelemvieira

## Comentarios do Gatekeeper

### 1. 2025-01-31T08:20:14.938-0300 | Filipe do Amaral Padilha

O maxPedido aparentemente está com um problema para gerar novas visitas avulsas, por não conseguir validar visitas e compromissos já criados.

Como na base do RCA já existem compromissos criados, então o app entra em conflito com eles e não consegue gerar novos atualizados.

Para resolver o problema, eu enviei um comando de deleção dos compromissos e das visitas avulsas criadas para o aparelho do RCA. Então quando ele sincronizar já estará livre para continuar usando o sistema.

Eu encaminhei para N3 para o pessoal avaliar a necessidade de correção dado o cenário encontrado na MXSVISITAS e MXSCOMPROMISSOS.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 420428
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: Em base zero, o problema não foi reproduzido. | Na base do RCA, o problema foi reproduzido conforme relatado. | O comportamento está associado especificamente à presença de registros prévios de visitas/compromissos na base do RCA. | Após o envio do comando de deleção, realizar a sincronização do aparelho do RCA para liberar o uso do sistema. | Aguardar a sincronização do aparelho do RCA para aplicação da deleção dos compromissos e visitas avulsas e, na sequência, prosseguir com a avaliação do N3 sobre a necessidade de correção definitiva. | Responsável: N3.
