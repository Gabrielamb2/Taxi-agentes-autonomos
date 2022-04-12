from SearchAlgorithms import AEstrela
from Graph import State

class Taxi(State):   

    def __init__(self, taxi, passageiro,destino, coordenadas, tamanho, ta_no_carro, op):
        self.taxi = taxi 
        self.passageiro  = passageiro
        self.destino = destino
        self.coordenadas = coordenadas
        self.tamanho = tamanho
        self.ta_no_carro = ta_no_carro
        self.operator = op
        

    def env(self):
        return str(self.operator)+str(self.taxi)+str(self.ta_no_carro)
    
    def valido(self, taxi_x):
        for c in self.coordenadas:
            if (c == taxi_x):
                return False #se a localizacao do obstaculo for igual a do taxi retorna falso
        return True
    def sucessors(self):
        sucessores = []

        #pegar passageiro
        if(self.taxi == self.passageiro and not self.ta_no_carro) :
            sucessores.append(Taxi(self.taxi, self.passageiro,self.destino,self.coordenadas,self.tamanho,True,'pegou'))
            
        #cima
        if(self.valido([self.taxi[0]-1, self.taxi[1]]) and self.taxi[0]-1 >=0 ):
            sucessores.append(Taxi([self.taxi[0]-1, self.taxi[1]],self.passageiro,self.destino,self.coordenadas,self.tamanho, self.ta_no_carro,'up'))
            
        #baixo
        if(self.valido([self.taxi[0]+1, self.taxi[1]]) and self.taxi[0]+1 < self.tamanho ):
            sucessores.append(Taxi([self.taxi[0]+1, self.taxi[1]], self.passageiro,self.destino,self.coordenadas,self.tamanho, self.ta_no_carro,'down'))
            
        #esquerda
        if(self.valido([self.taxi[0], self.taxi[1]-1]) and self.taxi[1]-1 >=0 ):
            sucessores.append(Taxi([self.taxi[0], self.taxi[1]-1], self.passageiro,self.destino,self.coordenadas,self.tamanho, self.ta_no_carro,'left'))
            
        #direita
        if(self.valido([self.taxi[0], self.taxi[1]+1]) and self.taxi[1]+1 < self.tamanho):
            sucessores.append(Taxi([self.taxi[0], self.taxi[1]+1], self.passageiro,self.destino,self.coordenadas,self.tamanho, self.ta_no_carro,'right'))
            
        
        return sucessores
    
    def is_goal(self):
        return self.destino == self.taxi and self.ta_no_carro #destino igual a coordenada do taxi e o passadgeiro esta no carro  
    
    def description(self):
        return "Taxi"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        if(self.ta_no_carro):
            return abs(self.taxi[0] - self.destino[0]) + abs(self.taxi[1] - self.destino[1]) #distancia ate o destino 
        else:
            return abs(self.taxi[0] - self.passageiro[0]) + abs(self.taxi[1] - self.passageiro[1])  #distancia ate o passageiro


def main():
    passanger = [0,0] 
    destiny = [4,0]
    blocks = []
    size = 5

    state = Taxi([0,2],passanger,destiny,blocks,size, False,'')
    algorithm = AEstrela()
    result = algorithm.search(state)

    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
