# Taxi-agentes-autonomos

## Configurando um ambiente virtual:

````bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

## Executar teste:

````bash
pytest test_taxi.py --capture=tee-sys
````

## Executar arquivo:

````bash
python Taxi.py 
````

## Descricao do projeto
Projeto que gera os passos para chegar o taxi pegar o passageiro e deixa-lo no destino desejado, apartir do algoritmo A*.

### Estados
Os estados são representados por:
  * as coordenadas do taxi
  * as coordenadas do passageiro
  * as coordenadas de destino
  * as coordenadas dos obstaculos
  * o tamanho do mapa 
  * uma variavel booleana para indicar se o passageiro esta ou nao no carro
  * um operador, o qual descreve qual ação foi realizada. As ações são em relação ao taxi, Sendo as opções de operador: up, down, right , left e pegar a pessoa.


### Sucessores
Para gerar os sucessores é analisado a localizacao do espaço vazio, para assim listar as possibilidades de movimentação. Sendo elas:
  * se a coordenada do taxi eh igual a do passageiro, e o passageiro nao esta no carro -> pega o passageiro
  * se a linha de cima da posicao atual do taxi eh maior que 0 e a posicao eh valida -> sobe
  * se a linha de baixo da posicao atual do taxi eh maior que 0 e a posicao eh valida -> desce
  * se a coluna da esquerda da posicao atual do taxi eh maior que 0 e a posicao eh valida -> esquerda
  * se a coluna da dirieta da posicao atual do taxi eh maior que 0 e a posicao eh valida -> direita
 
 ### Heuristica
 A heuristica inicialmente verifica se o passageiro esta no carro, se ele esta retorna a distancia do taxi ate o destino. Se ele nao esta retorna a distancia do taxi ate o passgeiro
