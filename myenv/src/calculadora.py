class calculadora():
    def __init__(self):
        pass

    def show(self):
        while True:
            print("1 - Soma")
            print("2 - Subtração ")
            print("3 - Divisão ")
            print("4 - Multiplicação ")
            print("5 - Fatorial")
            print("6 - Pontecia")
            print("7 - Raiz")
            print("8 - Velocidade media")
            print("9 - Distancia entre dois pontos")
            print("0 - Sair do programa")

            op = int(input("Qual a operação você deseja?"))
            if (op == 0):
                break

            try:
                num1 = float(input("Entrada do primeiro valor: "))
                num2 = float(input("Entrada do segundon valor: "))
                num3 = 0
                num4 = 0
            except ValueError:
                print("erro! entrada incorreta!")

            def escolha(op):
                match op:
                    case 1:
                        self.soma(num1, num2)
                        
                    case 2:
                        self.sub(num1, num2)
                        
                    case 3:
                        try:
                            self.divisao(num1, num2)
                        except ZeroDivisionError:
                            print("Erro! Divisores 0 ou nulos")    
                        
                    case 4:
                        self.multiplicao(num1, num2)
                        
                    case 5:
                        self.fatorial(num1)
                        
                    case 6:
                        self.potencia(num1)
                        
                    case 7:
                        self.raiz(num1)

                    case 8:
                        num3 = float(input("entrada com o terceiro valor: "))
                        num4 = float(input("entrada com o quarto valor: "))
                        self.velocidade_media(num1, num2, num3, num4)
                        

                    case 9:
                        num3 = float(input("entrada com o terceiro valor: "))
                        num4 = float(input("entrada com o quarto valor: "))      
                    
                    case _:
                        print("erro! operação incorreta")

    @staticmethod
    def soma(a, b):
        print( a + b)
    @staticmethod 
    def sub(a, b):
        print( a - b)
    @staticmethod
    def multiplicao(a, b):
        print( a * b)
    @staticmethod
    def divisao(a, b):
        if b == 0:
            print("Erro! Divisão menor que 0")
        print( a/b)

    @staticmethod
    def fatorial(a):
        result = 1
        i = 1
        while i <= a:
            resultado *= a
            i += 1
        print( resultado)

    @staticmethod    
    def potencia(a, b):
        if (a == 1) and (b == 0):
            print("1^0 = 0")
        print( a ** b)
    
    @staticmethod
    def raiz(a):
        import math
        print( math.sqrt(a))

    @staticmethod
    def velocidade_media(a1, a2, b1, b2):
        vm = (a2 - a1) / (b2 - b1)
        vm *= 3,5
        print( vm)

    @staticmethod
    def calcular_distancia_pontos(a1, a2, b1, b2):
        import math
        a = (a2 - a1) ** 2
        b = (b2 - b1) ** 2
        
        distancia = (a + b)

        print( math.sqrt(distancia))