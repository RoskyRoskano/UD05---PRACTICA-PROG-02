class Operaciones:
    def __init__(self):
        
        # Inicializo la clase Operaciones y carga dos valores enteros por teclado.
        
        self.valor1 = int(input("Ingresa el primer valor entero: "))
        self.valor2 = int(input("Ingresa el segundo valor entero: "))

    def suma(self):
        
        # Calculo la suma de los dos valores enteros.
        
        return self.valor1 + self.valor2

    def resta(self):
        
        # Calculo la resta de los dos valores enteros.
        
        return self.valor1 - self.valor2

    def multiplicacion(self):
        
        # Calculo la multiplicación de los dos valores enteros.
        
        return self.valor1 * self.valor2

    def division(self):
        
        # Calculo la división de los dos valores enteros (verifica la división por cero).
        
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: No se puede dividir entre cero."

    def imprimir_resultados(self):
        
        # Imprimo los resultados de las operaciones.
        
        print(f"\nResultados de las operaciones:")
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicación: {self.multiplicacion()}")
        print(f"División: {self.division()}")

# Ejemplo
operaciones = Operaciones()
operaciones.imprimir_resultados()
