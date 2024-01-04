def encontrar_menor():
    # Solicito tres valores
    valor1 = float(input("Ingrese el primer valor: "))
    valor2 = float(input("Ingrese el segundo valor: "))
    valor3 = float(input("Ingrese el tercer valor: "))

    # Encuentro el menor
    menor = min(valor1, valor2, valor3)

    # Muestro el resultado
    print(f"El menor valor es: {menor}")

# Llamo a la función dos veces desde el bloque principal
print("Primera llamada:")
encontrar_menor()

print("\nSegunda llamada:")
encontrar_menor()
