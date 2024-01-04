# Calculo el fibonacci de un numero 
def fibonacci(num):
    if num < 0 or num > 20:
        return "Número fuera del rango válido [0, 20]"

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, num + 1):
            a, b = b, a + b
        return b

# Ejemplo de uso
numero = 10
resultado = fibonacci(numero)
print(f"El número de Fibonacci para {numero} es: {resultado}")
