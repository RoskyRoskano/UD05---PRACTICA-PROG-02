class Jugador:

    def __init__(self, d, n, e):
        self.__dorsal = d
        self.__nombre = n
        self.__equipo = e

    def mostrar(self):
        print(f"{self.__dorsal}. {self.__nombre}, {self.__equipo}")

class Equipo:
    def __init__(self, n):
        self.__nombre = n

    def getNombre(self):
        return self.__nombre

e1 = Equipo("Valencia CF")

j1 = Jugador(7, "Jaume Mir", e1.getNombre())
j2 = Jugador(10, "Alejandro Navarro", e1.getNombre())

j1.mostrar()
j2.mostrar()