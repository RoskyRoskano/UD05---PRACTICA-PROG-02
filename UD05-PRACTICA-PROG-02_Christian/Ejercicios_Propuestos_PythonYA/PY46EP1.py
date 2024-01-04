class Socio:
    def __init__(self):
        
        # Inicializo la clase Socio con atributos nombre y antigüedad, solicitando la carga por teclado.
        
        self.nombre = input("Ingresa el nombre del socio: ")
        self.antiguedad = int(input("Ingresa la antigüedad del socio en años: "))

class Club:
    def __init__(self):
        
        # Inicializo la clase Club con 3 objetos de la clase Socio como atributos.
        
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def imprimir_socio_mayor(self):
        
        # Imprimo el nombre del socio con mayor antigüedad en el club.
        
        socios = [self.socio1, self.socio2, self.socio3]

        socio_mayor_antiguedad = max(socios, key=lambda socio: socio.antiguedad)
        print(f"El socio con mayor antigüedad en el club es: {socio_mayor_antiguedad.nombre}")

# Ejemplo
club = Club()
club.imprimir_socio_mayor()
