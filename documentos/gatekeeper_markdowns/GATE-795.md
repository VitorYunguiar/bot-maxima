# GATE-795 - Coordenadas clientes

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Gleiciellen Pereira Leal [X]
- ERP do cliente: PROTON
- Assunto: MXPED - Cliente - Geolocalização
- Natureza: Dúvida
- Atualizado em: 2025-02-14T08:55:00.704-0300

## Contexto do Problema

## Passos para reproduzir
- Cliente utiliza roteirizador e gostaria de importar as coordenadas dos clientes para o maxPedido

## Resultado apresentado
- Cliente utiliza roteirizador e gostaria de importar as coordenadas dos clientes para o maxPedido

## Resultado esperado
- Cliente utiliza roteirizador e gostaria de importar as coordenadas dos clientes para o maxPedido

## Descrição
Cliente utiliza roteirizador e gostaria de importar as coordenadas dos clientes para o maxPedido

## Comentarios do Gatekeeper

### 1. 2025-02-14T08:55:00.702-0300 | Filipe do Amaral Padilha

Não se trata de um erro, o cliente não cadastrou as coordenadas no nosso endpoint MXSCLIENT e atualmente eles teriam de fazer isso manualmente via Central de Configurações do maxPedido, ou através de integração com o ERP, sendo do ERP -> Máxima.

Com as coordenadas cadastradas, os RCAs precisam sincronizar o maxPedido, e então vão receber os dados que o sistema usa para validar localização do RCA e comparar na hora de realizar o Check-in/Check-out com Raio.

Para resolver definitivamente, é necessário o cliente construir uma integração que envie esses dados para Máxima. Eles podem por exemplo, pegar as coordenadas que vamos transferir para a tabela MXSCLIENT e guardar no ERP e depois enviar no mesmo endpoint.

Outra opção que eles teriam é solicitar uma melhoria, porque essa movimentação de dados que vou fazer no banco de dados nuvem será manual e não existe uma automação nos sistemas da Máxima para isso.

Paliativamente então foi feita transferência dos dados das coordenadas do Roteirizador para o endpoint MXSCLIENT através do banco de dados nuvem, dessa forma os RCAs podem sincronizar os dados no maxPedido. Observação importante: Se o ERP sobrescrever a informação do endpoint MXSCLIENT nos campos LATITUDE e LONGITUDE, os dados das coordenadas serão novamente perdidos.

## Resposta Canonica

**Causa identificada**  
Não se trata de erro de sistema. As coordenadas dos clientes não foram cadastradas no endpoint **MXSCLIENT**, que é a origem considerada pelo maxPedido para esse uso.

**Análise**  
Foi identificado que:
- o cliente não cadastrou as coordenadas no **MXSCLIENT**;
- atualmente, esse cadastro precisa ser feito manualmente pela **Central de Configurações do maxPedido** ou por **integração com o ERP** no fluxo **ERP -> Máxima**;
- houve uma transferência paliativa das coordenadas do Roteirizador para o **MXSCLIENT** por meio do banco de dados nuvem;
- após o cadastro das coordenadas, os **RCAs** precisam sincronizar o **maxPedido** para receber os dados utilizados na validação de localização e no **Check-in/Check-out com Raio**;
- se o ERP sobrescrever os campos **LATITUDE** e **LONGITUDE** no endpoint **MXSCLIENT**, as coordenadas serão perdidas novamente.

**Limitações**  
- A movimentação realizada no banco de dados nuvem é manual.
- Não há automação nos sistemas da Máxima para essa transferência de dados.
- Qualquer sobrescrita dos campos **LATITUDE** e **LONGITUDE** pelo ERP remove novamente as coordenadas.

**Ação recomendada**  
- Construir uma integração para enviar as coordenadas para a Máxima.
- Se necessário, cadastrar manualmente as coordenadas pela Central de Configurações do maxPedido.
- Implementar o fluxo **ERP -> Máxima** para manter os dados no **MXSCLIENT**.
- Sincronizar o maxPedido nos RCAs após o cadastro das coordenadas.
- Caso seja necessária automação nativa dessa movimentação, solicitar uma melhoria.

**Responsável**  
Cliente.

**Próximo passo**  
Sincronizar o maxPedido nos RCAs após a transferência das coordenadas e definir uma solução definitiva de envio das coordenadas para a Máxima, via integração ou solicitação de melhoria.

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 423953
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
