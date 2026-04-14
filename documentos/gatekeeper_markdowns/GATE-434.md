# GATE-434 - Resumo de venda não atualiza

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Danilo Cunha da Silva
- ERP do cliente: Winthor
- Assunto: MXPED - Resumo de Vendas
- Natureza: Dúvida
- Atualizado em: 2024-12-03T11:33:49.083-0300

## Contexto do Problema

## Passos para reproduzir
>> Login: BDMAIS.279
>> Acessar maxPedido, ir em objetivos e pesquisar, depois ir em atualizar menu.

## Resultado apresentado
>> Resumo de venda não atualiza.

## Resultado esperado
>> Resumo de venda atualiza

## Descrição
Resumo de venda não atualiza. Foi verificado as portas 9000/9002 e ambas entao liberadas.

Foi visto no banco nuvem na tabela MXSDIASUTEIS e não tem dias uteis cadastradas para o ano de 2024.

Foi verificado no banco local do cliente e na tabela PCDATAS aparecem os dias cadastradas no ano de 2024.

## Comentarios do Gatekeeper

### 1. 2024-12-03T11:33:31.069-0300 | Filipe do Amaral Padilha

Pelo o que eu analisei usando o IP deles externo: [http://bdmais.fortiddns.com/] nas portas 9000 e 9002 eles estão inacessíveis.

Para testar o teste de portas, você pode fazer assim: [https://testeportas.com.br/]

IP deles público: 201.86.30.77

Portas 9000 e 9002

Não deu para acessar via VPN e nem Workspace quer dizer que eles estão totalmente bloqueados para acesso externo, por isso o resumo de vendas não atualiza.

Para fazer o suporte ao extrator a gente usa a porta 9000 e para atualizar o menu e outras funcionalidades que envolvem API, a gente usa a porta 9002.

Para resolver então eu sugiro que eles façam liberação de TCP externo para qualquer IP externo que tentar conexão nessas portas 9000 e 9002.

Conforme consta no nosso site [https://maximatech.com.br/requisitos/cloud-tipo-erp/cloud-winthor/]
* *Acesso externo para servidor Máxima:* Portas TCP 9000, 9001, 9002, 9003 (Liberar no firewall (NAT) para acesso externo)

Outra opção que eles tem, caso não queiram liberar acesso total, seria liberar somente para os IPS e portas citados na listagem.

"*Acesso externo Liberados no Firewall nos seguintes IP’s e Portas**:* (incluir uma tabela)"

os ips constam no site.

Depois que eles liberarem os acessos externos, dai pode baixar uma base e fazer o teste de atualização de menu no maxPedido.

## Resposta Canonica

Nao gerada.

## Qualidade

- Flags: grounding_failed
- Comentarios primarios: 410034
- Secoes ausentes: nenhuma
- Groundedness aprovado: nao
- Afirmacoes sem suporte: "Foi validado o acesso externo" — o texto-fonte diz "Pelo o que eu analisei" usando o IP externo, mas não usa a formulação de validação formal. | "vinculado ao IP público 201.86.30.77" — o texto-fonte informa o endereço e o IP público, mas não afirma explicitamente que o endereço está vinculado a esse IP. | "o que reforça o cenário de bloqueio para acesso externo" — é uma inferência/ênfase interpretativa além do que está literalmente no texto-fonte. | "A causa do problema não está associada, pelos fatos levantados, à ausência de dias úteis em tabela de nuvem" — esse tema não aparece no texto-fonte. | "Responsável pela ação: Cliente" — o texto-fonte sugere que "eles" façam a liberação, mas não explicita esse campo ou responsável formal.
