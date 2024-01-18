from tqdm import tqdm
import os, time

def animation():
    for i in tqdm(range(3)):
        time.sleep(0.5)
        os.system('clear') or None

class Elevador:
    def __init__(self):
        self.__andarAtual = 0
        self.__totalAndares = 0
        self.__capacidadeElevador = 20
        self.__totalCapacidade = 0
        self.__ligado = False

    def getAndarAtual(self):
        return self.__andarAtual

    def getTotalAndares(self):
        return self.__totalAndares

    def getTotalCapacidade(self):
        return self.__totalCapacidade
    
    def setAndarAtual(self, valor):
        if isinstance(valor, int):
            self.__andarAtual = valor

    def setTotalAndares(self, valor):
        if isinstance(valor, int):
            self.__totalAndares = valor

    def setTotalCapacidade(self, valor):
        if isinstance(valor, int):
            self.__totalCapacidade = valor

    def Incializar(self):
        if not self.__ligado:
            self.__totalCapacidade = 0
            self.__totalAndares = 0
            self.__andarAtual = 0
            self.__andarLimite = 4
            self.__ligado = True
            animation()
            print("O elevador ligou!")
        else:
            print("O elevador já está ligado!")

    def Entrar(self):
        if self.__ligado and self.__capacidadeElevador <= 20:
            self.setTotalCapacidade(self.__totalCapacidade + 1) 
        elif self.__capacidadeElevador == self.__totalCapacidade:
            print("Capacidade Máxima")    
        else:
            print("O elevador está cheio e desligado")    
            
    def Sair(self):
        if self.__ligado:
            self.setTotalCapacidade(self.__totalCapacidade - 1)
        elif self.__totalCapacidade < 0:
            print("Elevador vazio!")    

    def Subir(self):
        if self.__ligado and self.__andarAtual < self.__andarLimite:
            self.setAndarAtual(self.__andarAtual + 1)
        else:
            print("Andar máximo, por favor desça!")    

    def Descer(self):
        if self.__ligado and self.__andarAtual < self.__andarLimite:
            self.setAndarAtual(self.__andarAtual - 1)
        else:
            print("Térreo, por favor suba!")

    def toString(self):
        print('Olá...')
        time.sleep(1)
        os.system('clear') or None
        print(f'''
    --------------------------------------------------
            Elevador do Prédio de tal
    --------------------------------------------------
                STATUS ATUAL:
    O Elevador está: {}
    Total de Andares: {}
    Capacidade Atual: {}
    Capacidade Permitida: {}
    neste momento o elevador no: {}° Andar
    --------------------------------------------------
            ''')
        print('Voltando para o menu ...')
        time.sleep(4)
