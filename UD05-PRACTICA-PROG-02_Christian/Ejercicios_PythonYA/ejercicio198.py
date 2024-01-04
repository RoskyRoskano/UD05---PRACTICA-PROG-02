import random


class Dado:

    def tirar(self):
        # Sacar el valor aleatoriamente
        self.valor=random.randint(1,6)

    def imprimir(self):
        # Imprimir el valor dle dado
        print("Valor del dado:",self.valor)

    def retornar_valor(self):
        # Retornar el valor del dado
        return self.valor


class JuegoDeDados:

    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor()==self.dado3.retornar_valor():
            print("Gano")
        else:
            print("Perdio")


# bloque principal del programa

juego_dados=JuegoDeDados()
juego_dados.jugar()