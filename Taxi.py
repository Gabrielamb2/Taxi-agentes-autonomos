from SearchAlgorithms import AEstrela
from Graph import State
import gym
import numpy as np



def le_mapa(cidade,matriz_cidade):
    pontos = ["R", "G", "Y", "B"]
    alvo = []
    #le todo o mapa
    for i in range(cidade.shape[0]): #percorre o mapa
        for j in range(cidade.shape[1]):
            matriz_cidade[i,j] = cidade[i,j].decode('UTF-8')
            if matriz_cidade[i,j] in pontos: #se
                alvo.append([i,j]) #coloca nos way points
    return alvo

def le_mapa_barrerias(cidade,matriz_cidade):
    BARREIRAS = ["|","-","+"]
    alvo = []
    #le todo o mapa
    for i in range(cidade.shape[0]): #percorre o mapa
        for j in range(cidade.shape[1]):
            matriz_cidade[i,j] = cidade[i,j].decode('UTF-8')
            if matriz_cidade[i,j] in BARREIRAS == ["|","-","+"]:
                alvo.append([i,j]) #coloca nos way points
    return alvo

class taxi_interface():
    def __init__(self,cidade,posicao):  
    
        matriz_cidade = np.zeros((cidade.shape[0],cidade.shape[1]))
        matriz_cidade = matriz_cidade.astype(str)
        alvo = le_mapa(cidade,matriz_cidade)
        
        #o : e | nao sao posicoes
        #se ele ta na posicao 0 do mapa pra mim ele ta na 1, e assim por diante
        # posicao*posicao +1 = posicao atual
        posicoes = list(posicao)
        
        #para as linhas + 1 para pular a primeira
        comeco = [posicoes[0]+1,int(posicoes[1])*2+1]

        self.state = Taxi(comeco,alvo[posicoes[2]],cidade,False,'',alvo[posicoes[3]])
        self.algorithm = AEstrela()
        self.result = self.algorithm.search(self.state)
                
    def path(self):
        operations = []
        if self.result != None:
            # print("oi")
            # print(self.result.show_path())
            operations = (self.result.show_path()+";5").replace(" ","").replace(";"," ").split() # 5 = drop off
            operations = list(map(int,operations))
            return operations
        else:
            return 'Nao achou solucao'

def detec(cidade):
        if type(cidade) != list:
            coordenadas = []
            matriz_cidade = np.zeros((cidade.shape[0],cidade.shape[1]))
            matriz_cidade = matriz_cidade.astype(str)
            coordenadas = le_mapa_barrerias(cidade,matriz_cidade)
            return coordenadas
        return cidade

class Taxi(State):   


    def __init__(self, taxi, passageiro, coordenadas, ta_no_carro, op,destino):

        self.coordenadas = detec(coordenadas)                   
        self.taxi = self.valido(taxi)            
        self.passageiro = self.valido(passageiro)            
        self.ta_no_carro = ta_no_carro              
        self.operator = op                  
        self.destino = destino                    
        
    def env(self):
        return str(self.operator)+str(self.taxi)+str(self.ta_no_carro)

    def valido(self,tupla):
        bounds = max(self.coordenadas)
        if tupla[0] > 0 and tupla[0] < bounds[0]:
            if tupla[1] > 0 and tupla[1] < bounds[1]:
                return tupla
        else:
            raise ValueError("Posição inválida")

    def sucessors(self):
        sucessors = []
        #pegar passageiro
        if not self.ta_no_carro and self.taxi == self.passageiro:
            sucessors.append(Taxi(self.taxi, self.passageiro, self.coordenadas, True, "4", self.destino)) #4 = pickup
        #cima
        if self.taxi and [self.taxi[0]-1,self.taxi[1]] not in self.coordenadas:
            sucessors.append(Taxi([self.taxi[0]-1,self.taxi[1]], self.passageiro, self.coordenadas, self.ta_no_carro, "1", self.destino))#1 = north

        #baixo
        if self.taxi and [self.taxi[0]+1,self.taxi[1]] not in self.coordenadas:
            sucessors.append(Taxi([self.taxi[0]+1,self.taxi[1]], self.passageiro, self.coordenadas, self.ta_no_carro, "0", self.destino)) # 0 = south
    
        #esquerda
        if self.taxi and [self.taxi[0],self.taxi[1]-1] not in self.coordenadas:
            sucessors.append(Taxi([self.taxi[0],self.taxi[1]-2], self.passageiro, self.coordenadas, self.ta_no_carro, "3", self.destino)) # 3 = west

        #direita
        if self.taxi and [self.taxi[0],self.taxi[1]+1] not in self.coordenadas:
            sucessors.append(Taxi([self.taxi[0],self.taxi[1]+2], self.passageiro, self.coordenadas, self.ta_no_carro, "2", self.destino))   #2 = east    
       
        return sucessors
    
    def is_goal(self):
        return self.destino == self.taxi and self.ta_no_carro #destino igual a coordenada do taxi e o passadgeiro esta no carro  

    def description(self):
        return "Taxi"
    
    def cost(self):
        return 1 

    def print(self):
        pass 

    def h(self):
        if(self.ta_no_carro):
            return abs(self.taxi[0] - self.destino[0]) + abs(self.taxi[1] - self.destino[1]) #distancia ate o destino 
        else:
            return abs(self.taxi[0] - self.passageiro[0]) + abs(self.taxi[1] - self.passageiro[1])  #distancia ate o passageiro



    

def main():
    env = gym.make("Taxi-v3").env
    state = env.reset()
    env.render()

    taxi = taxi_interface(env.desc,env.decode(state))
    # print(taxi.path())
    for t in taxi.path():
        # print(t)
        state, reward, done, info = env.step(t)
        env.render()
    if done:
        print("Achou")
    else:
        print("Nao achou solucao")

if __name__ == '__main__':
    main()
