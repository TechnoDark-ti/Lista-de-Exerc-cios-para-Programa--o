#from abc import ABC, abstractmethod

class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    #@abstractmethod
    def imprimirValor(self):
        print(f"Ingresso normal --- valor {self.valor}")


class ingressosVIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimirValor(self):
        valor_vip = self.valor *2
        print(f"Ingreso VIP --- valor: {valor_vip}")

