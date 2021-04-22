<img src="https://www.pikpng.com/pngl/m/246-2466980_cryptocurrency-png-bitcoin-cloud-clipart.png" align="right" width="200"/>

# Crypto Candle Bot
API que realiza a montagem de candlestickers baseado na cotação em tempo real de uma criptomoeda (Bitcoin)

Não sabe o que é um candlesticker? <a href="https://pt.wikipedia.org/wiki/Candlestick">clique aqui</a>

## Funcionalidade:
- Disponibilizar uma api com dois endpoints responsáveis por iniciar a criação dos candle stickers e por retornar os candles stickers criados.<br>

## Requisitos

- python <br>
- pip <br>
- MYSQL <br>
- ou apenas o Docker <br>

## Instalação manual

1) Faça o clone do projeto<br>
- ```$ git clone https://github.com/Wilson3g/crypto-candle-bot.git```<br>

2) Crie e ative uma virtual env usando python3<br>
- ```$ python3 -m venv nome_da_sua_env```<br>
- ```$ . nome_da_sua_env/bin/activate```<br>

3) Instale as dependências
- ```$ pip install -r requirements.txt```<br>

4) Inicie o servidor Flask
- ```$ flask run```<br>

## Instalação com Docker
1) Faça o clone do projeto<br>
- ```$ git clone https://github.com/Wilson3g/crypto-candle-bot.git```<br>

2) Montagem dos containers Docker<br>
- ```$ docker-compose up```<br>
<b>OBS: Fique ciente que a instalação do projeto com Docker pode levar vários minutos para ser finalizada!</b>


## Endpoints da aplicação
- POST: http://localhost:5000/candle-sticke - Inicia a criação dos candle stickers
- GET: http://localhost:5000/candle-sticke - Exibe os candle sticker já criados

## Uso
- Realize a requisição na rota POST - http://localhost:5000/candle-sticke para que o servido seja iniciado (Leva aproximadamente 1 minuto para que o primeiro candle sticker seja montado e salvo no banco).
- Realize a requisição na rota GET - http://localhost:5000/candle-sticke para exibir os candles criados.

## Teste
1) Executar teste<br>
- ```$ python test.py```<br>

## Escolha do Framework
Assim que comecei a pesquisar e idealizar como o projeto seria implementado, já tinha em mente que gostaria de disponibilizar uma API com um endpoint que retornasse a lista de candle já criados.

Tendo isso em mente, minha escolha se resumiu aos Frameworks Flask Restful e Django Rest Framework (DRF). Como tenho mais experiência com o DRF, fiquei tentado a usa-lo, porém pela alta customização que o Flask oferece e pensando também na leveza do mesmo, decidi usa-lo, já que iria desenvolver uma aplicação simples de início mas que com o passar do tempo poderia ser escalada.

## Dificuldades na implementação

### python

Assim que comecei a codificar, encontrei como primeiro desafio o uso de multithreading no python(visto que, eu tinha noção de como esse recurso funcionava, mas nunca havia usado). Gastando algumas horas de pesquisas, consegui sair do outro lado rapidamente com este problema.

Assim que resolvi o problema das threads e montei a base da arquitetura e organização do projeto, tive minha primeira "decepção". Minha ideia seria disponibiizar um socket para que sempre que um novo candle fosse criado, o dado fosse retornado de maneira "automática" para o usuário. Cheguei a implementar o script, mas logo percebi o custo computacional que minha aplicação teria caso eu á escalasse, isso porque estava rodando multithreads e sockets na mesma aplicação. Tentei separa os scripts mas não consegui realizar a implementação de uma maneira inteligente.

### Docker
Quando terminei o script em Flask, iniciei os meus estudos e tentativas de subir um container com o Flask e MYSQL.

Admito que tenho pouca ou nenhuma experiência com o Docker, mas subir os containers do Flask e MYSQL não foi nada muito complicado. Com poucas horas gastas, consegui realizar a implementação.

Meu primeiro problema com Docker se iniciou quando tentei ligar os dois containers que havia acabado de subir. Demorei mais de um dia para conseguir realizar a conexão do banco com a aplicão. 

Minha segunda "decepção" aconteceu assim que consegui realizar a conexão dos dois containers. Percebi que o container com Flask estava tentando executar as migrations antes do container MYSQL ser totalmente iniciado. Gastei mais de dois dias tentando resolver o problema. 

Acabei descobrindo que a solução se encontrava em uma técnica popularmente chamada de "wait-for-it" que consistem em criar um script responsável por fazer com que um determinado container espere a instância de outro, para assim prosseguir.

## Pontos a melhorar

Entre os vários pontos a melhorar no desenvolvimento, posso listar alguns que particulamente me deixaram incomodado.

1) <b>Organização do projeto:</b>
Como não tenho conhecimento em design patterns ainda, tive que procurar formas de organizar o código e a estrutura de pastas. Creio que se fossem aplicadas técnicas de designer pattern, o projeto ficaria mais organizado.

2) <b>Endpoint usado apenas para startar o servidor:</b>
Me desagradou o fato de disponibilizar um endpoint só para iniciar a criação dos candles. Acho que o ideal seria iniciar a criação dos candles assim que o servidor fosse iniciado.

3) <b>Disponibilizar mais de uma cripto moeda:</b>
Atualmente os candles estão sendo montados usando o bitcoin, seria bom se ouvesse ao menos a montagem de candle das 5 principais cripto moedas do mercado.

4) <b>Socket para exibir os candles em tempo real:</b>
Acredito que seja uma ótima ideia retornar a criação dos candles em tempo real para o usuário

5) <b>Otimizar a montagem dos containers:</b>
Creio que a solução que encontrei para a montagem "sincrôna" dos containers não tenha sido a melhor em questão de performance. Vale a pena tentar criar um script próprio para otimizar o processamento.

5) <b>Aplicar testes:</b>
Como não tenho conhecimento com TDD, não sabia o que testar quando montei a implementação. Acabei testando apenas a criação do candle e a url que lista os mesmos. Uma correção a ser feita seria implementar testes em todas as partes possíveis do sistema.

## Aprendizado
Como tenho apenas o conhecimento básico do python, desenvolver esta aplicação me possíbilitou aprender tecnologias que eu ainda não havia experimentado. 

Mesmo as frustrações que tive ao tentar montar os containers com Docker e ao tentar implementar um server Flask com sockets, me fizeram aprender e tirar lições valiosas que eu jamais teria percebido se não tivesse realizado esta implementação. 

Esse desafio me possibilitou observar pontos fracos que eu ainda tenho a desenvolver com meus estudos e com a resolução de desafios cada vez mais complexos.

Enfim, fico feliz com o aprendizado que tirei ao realizar este projeto. Tanto das parte em que consegui alcançar meus objetivos, quanto das partes em que não consegui.
