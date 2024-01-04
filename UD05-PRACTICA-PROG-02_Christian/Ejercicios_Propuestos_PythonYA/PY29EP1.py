def tabla_de_multiplicar(valor, final=10):
    
    print(f"Tabla de multiplicar del {valor} hasta el numero {final}:\n")
    for i in range(1, final + 1):
        resultado = valor * i
        print(f"{valor} x {i} = {resultado}")

# Llamo a la función desde el bloque principal con argumentos nombrados
valor = 5
final = 7

tabla_de_multiplicar(valor=valor, final=final)
