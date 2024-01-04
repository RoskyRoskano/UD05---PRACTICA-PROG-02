class Jugador:

    def __init__(self, d, n):
        self.__dorsal = d
        self.__nombre = n


    def mostrar(self):
        print(f"{self.__dorsal}. {self.__nombre}")

j1 = Jugador(7, "Jaume Mir")
j2 = Jugador(10, "Alejandro Navarro")

j1.mostrar()
j2.mostrar()