class Jugador:
    minutos_faltantes = 30  # Variable de clase

    def __init__(self, nombre, puntaje):
        
        # Inicializo la clase Jugador con los atributos nombre y puntaje.
        
        self.nombre = nombre
        self.puntaje = puntaje

    def imprimir(self):
        
        # Imprimo los datos del jugador.
        
        print(f"Jugador: {self.nombre}, Puntaje: {self.puntaje}")

    def pasar_tiempo(self):
        
        # Reduzco en uno la variable de clase minutos_faltantes.
        
        Jugador.minutos_faltantes -= 1


# Bloque principal del programa
jugador1 = Jugador("Carlos", 100)
jugador2 = Jugador("Ana", 150)

while Jugador.minutos_faltantes > 0:
    # Imprimir estado actual de los jugadores y la variable de clase
    jugador1.imprimir()
    jugador2.imprimir()
    print(f"Minutos restantes: {Jugador.minutos_faltantes}")

    # Pasar un minuto
    jugador1.pasar_tiempo()
    jugador2.pasar_tiempo()

# Imprimir mensaje al finalizar el juego
print("¡Fin de juego!")
