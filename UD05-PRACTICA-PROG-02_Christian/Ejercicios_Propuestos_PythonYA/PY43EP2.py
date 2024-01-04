class Triangulo:
    def __init__(self):
        
        # Inicializo los atributos de la clase Triangulo.
        
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0

    def inicializar_lados(self, lado1, lado2, lado3):
        
        # Inicializo los atributos de los lados del triángulo.
        
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado(self):
        
        # Imprimo el valor del lado mayor del triángulo.
        
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor del triángulo es: {lado_mayor}")

    def es_equilatero(self):
        
        # Muestro si el triángulo es equilátero o no.
        
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")

# Ejemplo
triangulo = Triangulo()

# Inicializar los lados del triángulo
triangulo.inicializar_lados(5, 5, 5)

# Imprimir el lado mayor del triángulo
triangulo.imprimir_lado()

# Verificar si el triángulo es equilátero
triangulo.es_equilatero()
