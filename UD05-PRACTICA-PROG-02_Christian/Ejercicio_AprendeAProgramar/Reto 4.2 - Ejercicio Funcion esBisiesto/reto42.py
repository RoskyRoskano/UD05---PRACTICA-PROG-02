# Calculo el factorial
def factorial(num):
    if num < 0 or num > 10:
        return "Número fuera del rango válido [0, 10]"

    resultado = 1
    for i in range(1, num + 1):
        resultado *= i

    return resultado

# Ejemplo
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
