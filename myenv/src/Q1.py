import datetime
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, dataNascimento, altura, peso ):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.altura = altura
        self.peso = peso

    def toString(self):
        print(f'''
            +-----------------------------------------+
            |       DADOS DO JOGADOR          |
            +-----------------------------------------+
             Nome do Jogador: {self.getNome()}    
             Posicao: {self.getPosicao()}            
             Altura: {self.getAltura()}               
             Peso: {self.getPeso()}               
             Data de Nascimento:{self.getDatanascimento()}
             Nacionalidade: {self.getNacionalidade()}     
            +-----------------------------------------+
            ''')

class Jogador(Pessoa):
    def __init__(self,nome, dataNascimento, altura, peso):
        super().__init__(nome, dataNascimento, altura, peso)
        
    def toString(self):
        return super().toString()

    def calcular_tempo(self):
        data_atual =  datetime.datetime.now()
        self.dataNascimento = datetime.datetime.strptime(self.dataNascimento, "%Y-%m-%d")

        diferenca = data_atual - self.dataNascimento
        self.idade = diferenca.days // 365

        print(f"\nA idade do jogador {self.nome} é: {self.idade}")

        if self.idade >= 40:
            print("Jogador aposentado!")        
        elif self.idade >= 36 or self.idade <= 39:
            print("Jogador meio-camp")
        elif self.idade <= 35:
            print("Jogador Atacante")

