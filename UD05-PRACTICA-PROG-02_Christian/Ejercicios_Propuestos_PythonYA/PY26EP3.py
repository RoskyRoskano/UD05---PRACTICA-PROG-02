def calcular_producto(lista):
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto

# Defino una lista de enteros
lista_enteros = [2, 3, 5, 7, 11]

# Llamo a la función y muestro el resultado
resultado_producto = calcular_producto(lista_enteros)

print(f"El producto de los elementos de la lista es: {resultado_producto}")
