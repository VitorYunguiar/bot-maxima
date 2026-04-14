# GATE-416 - Problema no Processamento de Fotos no Ponto de Montagem

## Metadados

- Status: RESOLVIDO
- Responsavel: Filipe do Amaral Padilha
- Solicitante: Vitor de Aguiar Adrião
- ERP do cliente: Winthor
- Assunto: MXPED - Fotos - Ponto de Montagem
- Natureza: Dúvida
- Atualizado em: 2024-11-29T09:43:54.219-0300

## Contexto do Problema

## Passos para reproduzir
Servidor Linux
189.17.83.116:2224
192.168.8.158
usuário=maxima
senha=maxima*321

>>Banco nuvem
>SELECT * FROM MXSPRODUTOSFOTOS WHERE CODPROD IN(108827, 108789); -- obs: o produto 108789 tem foto e está ok, o produto 108827 tem foto no Linux mas não gera registro na MXSPRODUTOSFOTOS ao rodar a job no hangfire

-- Cliente relatou que o problema acontece em diversos produtos, não só nesses
-- Se consultar na SELECT * FROM MXSPRODUTOSFOTOS WHERE LINK LIKE '%found%'; pode verificar todos os produtos com o problema nas fotos.

## Resultado apresentado
Algumas fotos de alguns produtos não estão sendo processadas ao rodar a job de fotos. Esses produtos tem um caminho válido no Winthor porém ao rodar a job as fotos de alguns produtos não é processada, sem apresentar falhas.

## Resultado esperado
Ao rodar a job, processar as fotos e criar o registro na MXSPRODUTOSFOTOS

## Descrição
Boa tarde, Filipe/Carlos,

Estou enfrentando um problema no ponto de montagem da NORDIL (DILNOR), onde algumas fotos de produtos não estão sendo processadas durante a execução da job de fotos. Esses produtos possuem caminhos válidos no Winthor, mas, ao rodar a job, as fotos de alguns produtos não são processadas, sem que sejam apresentadas mensagens de falha.

Verifiquei que as fotos estão no caminho correto no Linux e que os arquivos de fato existem. Não consegui confirmar se as fotos estão corrompidas ou apresentam outro problema. Solicitei ao cliente que realizasse o upload das imagens novamente no Winthor, mas essa ação não trouxe resultados.

Poderiam me ajudar a identificar a causa do problema?

Obrigado desde já.

## Comentarios do Gatekeeper

### 1. 2024-11-29T09:43:54.216-0300 | Filipe do Amaral Padilha

Existia um problema com as imagens de fato, que era um bug onde elas não atualizavam sozinhas daquela condição de "notfound" ao rodar a job de fotos.

Eu não consegui corrigir esse bug (até pq não sou dev ainda né), mas eu resolvi o cenário fazendo o seguinte:
Eu alterei o diretório da stack do portainer para uma que não era funcional, colocando P:\FOTOS\, salvei a stack assim e rodei a job.

Com isso, todas as fotos foram apagadas, até as que estavam com problemas de "notfound" só que a job apagou elas no S3 e também no banco nuvem.

Depois disso eu só troquei novamente na stack para o original \\192.168.8.103\p\PRODUTOS_DILNOR\ e disparei a job. Todas as fotos voltaram a subir e inclusive as dos produtos que estavam com problemas atualizaram e passaram a ser exibidas com link válido no S3:
SELECT * FROM MXSPRODUTOSFOTOS m WHERE CODPROD IN(108771, 108776, 108875, 108777, 108876, 108773, 108774, 108829, 108830, 108831, 108832, 108926);

Nesse caso eu descobri também que o "p" ou "P" e o "jpg" ou "JPG" não mudam nada no cenário.

As fotos que continuam com codoperacao 2 ou inválidas, ou não existe um diretório como no caso do produto 108827; Tem um motivo específico. Ou o cadastro da DIRFOTOPROD está errado, ou a imagem não existe na pasta de fotos.

No caso do produto 108827 em específico, como eles mudaram a imagem na pasta de fotos para "108827.jpeg" e na DIRFOTOPROD da PCPRODUTO está "108827.JPG", dai nossa job não encontrou a imagem para atualizar. Ai para resolver basta eles ou mudarem a imagem novamente para jpg ou trocar no cadastro do produto para jpeg.

## Resposta Canonica

**Causa identificada**

Havia um bug em que imagens na condição **`notfound`** não se atualizavam automaticamente ao executar a job de fotos. Esse cenário explica os casos em que a foto não era reprocessada mesmo sem erro aparente.

Além disso, fotos que permanecem com **`codoperacao 2`** ou inválidas têm causa específica:
- cadastro incorreto no campo **`DIRFOTOPROD`** da **`PCPRODUTO`**; ou
- inexistência real do arquivo na pasta de fotos.

No caso do **produto 108827**, a divergência encontrada foi:
- arquivo na pasta de fotos: **`108827.jpeg`**
- cadastro em **`DIRFOTOPROD`** da **`PCPRODUTO`**: **`108827.JPG`**

Com isso, a job não encontrou a imagem para atualizar o registro.

**Análise realizada**

Foi feito um teste controlado alterando temporariamente o diretório da stack do Portainer para **`P:\FOTOS\`**, salvando a stack e executando a job. Após isso, todas as fotos foram apagadas do S3 e do banco nuvem, inclusive as que estavam em **`notfound`**.

Na sequência, o diretório foi restaurado para **`\\192.168.8.103\p\PRODUTOS_DILNOR\`** e a job executada novamente. Após essa reversão, todas as fotos voltaram a subir, inclusive as que estavam com problema, passando a ficar com link válido no S3.

Também foi informado que diferenças como **`p`/`P`** e **`jpg`/`JPG`** não alteram o cenário. Ainda assim, no produto **108827**, o que consta é que o arquivo existente está como **`.jpeg`** e o cadastro aponta para **`.JPG`**.

**Ação recomendada**

1. Para imagens presas em **`notfound`**:
   - alterar temporariamente o diretório da stack para um caminho não funcional;
   - salvar a stack e rodar a job para limpar as fotos do S3 e do banco nuvem;
   - restaurar o diretório original;
   - executar novamente a job para reenviar as fotos.

2. Para fotos que continuam com **`codoperacao 2`** ou inválidas:
   - validar se o **`DIRFOTOPROD`** está correto;
   - confirmar se o arquivo existe de fato na pasta de fotos.

3. Para o **produto 108827**:
   - ajustar a correspondência entre cadastro e arquivo físico, renomeando a imagem para **jpg** ou alterando o cadastro para **jpeg**.

**Limitação**

O procedimento acima contorna o problema de reprocessamento, mas **não representa correção do bug**. A correção definitiva do bug depende de desenvolvimento.

```sql
SELECT * FROM MXSPRODUTOSFOTOS m WHERE CODPROD IN(108771, 108776, 108875, 108777, 108876, 108773, 108774, 108829, 108830, 108831, 108832, 108926);
```

## Qualidade

- Flags: nenhuma
- Comentarios primarios: 409464
- Secoes ausentes: nenhuma
- Groundedness aprovado: sim
