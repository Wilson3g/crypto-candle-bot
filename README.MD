<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlLjKAYawACyVgXdIrXdXeRfZMW702_yMhLSYulimqJkIyhvqdrh44cP1c2PIDbaS1NkM&usqp=CAU" align="right" width="200"/>

# Crypto Candle Bot
API que realiza a montagem de candlestickers baseado na cotação em tempo real de uma criptomoeda (Bitcoin)

Não sabe o que é um candlesticker? <a href="https://pt.wikipedia.org/wiki/Candlestick">clique aqui</a>

## Funcionalidade:
- Disponibilizar uma api com dois endpoints responsáveis por iniciar a criação dos candle stickers e por retornar os candles stickers criados.<br>

## Requisitos

- Ter o python instalado <br>
- Ter o pip instaldo <br>
- Ter o MYSQL instaldo <br>

## Instalação

1) Faça o clone do projeto<br>
- ```$ git clone https://github.com/Wilson3g/crypto-candle-bot.git```<br>

2) Crie e ative uma virtual env usando python3<br>
- ```$ python3 -m venv nome_da_sua_env```<br>
- ```$ . nome_da_sua_env/bin/activate```<br>

3) Execute as migrações do banco<br>
- ```$ flask db init```<br>
- ```$ flask db migrate```<br>
- ```$ flask db upgrade```<br>

4) Inicie o servidor Flask
- ```$ flask run```<br>


## Endpoints da aplicação
- POST: http://localhost:5000/candle-sticke - Inicia a criação dos candle stickers
- GET: http://localhost:5000/candle-sticke - Exibe os candle sticker já criados

## Escolha do Framework
Assim que comecei a pesquisar e idealizar como o projeto seria implementado, já tinha em mente que gostaria de disponibilizar uma API com um endpoint que retornasse a lista de candle já criados.

Tendo isso em mente, minha escolha se resumiu aos Frameworks Flask Restful e Django Rest Framework (DRF). Como tenho mais experiência com o DRF, fiquei tentado a usa-lo, porém pela alta customização que o Flask oferece e pensando também na leveza do mesmo, se comparado ao DRF. Decidi usa-lo, já que iria desenvolver uma aplicação simples de início mas que com o passar do tempo poderia ser escalada.

## Dificuldades na implementação

### python

Assim que comecei a codificar, encontrei como primeiro desafio o uso de multithreading no python(visto que, eu tinha noção de como esse recurso funcionava, mas nunca havia usado). Gastando algumas horas de pesquisas, consegui sair do outro lado rapidamente com este problema.

Assim que resolvi o problema das threads e montei a base da arquitetura e organização do projeto, tive minha primeira "decepção". Minha ideia seria disponibiizar um socket para que sempre que um novo candle fosse criado, o dado fosse retornado de maneira "automática" para o usuário. Cheguei a implementar o script, mas logo percebi o custo computacional que minha aplicação teria caso eu á escalasse, isso porque estava rodando multithreads e sockets na mesma aplicação. Tentei separa os scripts mas não consegui realizar a implementação de uma maneira inteligente.

### Docker
Quando terminei o script em Flask, iniciei os meus estudos e tentativas de subir um container com o Flask e MYSQL.

Admito que tenho pouca ou nenhuma experiência com o Docker, mas subir os containers do Flask e MYSQL não foi nada muito complicado. Com poucas horas gastas, consegui realizar a implementação.

Meu primeiro problema com Docker se iniciou quando tentei ligar os dois containers que havia acabado de subir. Demorei mais de um dia para conseguir realizar a conexão do banco com a aplicão. Tive certeza que tudo estava funcionando quando executei as migrations e tudo decorreu com sucesso.

Minha segunda "decepção" aconteceu assim que consegui realizar a conexão dos dois containers. Percebi que o container com Flask estava tentando executar as migrations antes do container MYSQL ser totalmente iniciado. Gastei mais de dois dias tentando resolver o problema, sendo que algumas vezes cheguei bem perto de resolve-lo, mas minha inexperiência com o Docker e o tempo para a entrega que estava se esgotando me fizeram desistir de implementar os containers da forma correta.

## Aprendizado
Como tenho apenas o conhecimento básico do python, desenvolver esta aplicação me possíbilitou aprender tecnologias que eu ainda não havia experimentado. 

Mesmo as frustrações que tive ao tentar montar os containers com Docker e ao tentar implementar um server Flask com sockets, me fizeram aprender e tirar lições valiosas que eu jamais teria percebido se não tivesse realizado esta implementação. 

Esse desafio me possibilitou observar pontos fracos que eu ainda tenho a desenvolver com meus estudos e com a resolução de desafios cada vez mais complexos.

Enfim, fico feliz com o aprendizado que tirei ao realizar este projeto. Tanto das parte em que consegui alcançar meus objetivos, quanto das partes em que não consegui.