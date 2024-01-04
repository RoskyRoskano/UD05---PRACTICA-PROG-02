def cargar_lista():
    # Creo y relleno la lista
    lista = []
    for i in range(10):
        elemento = int(input(f"Ingrese el elemento {i + 1}: "))
        lista.append(elemento)
    return lista

def separar_positivos_negativos(lista):
    # Si es mayor que 0 lo meto en positivos y si es menor que 0 lo meto en negativos
    positivos = [x for x in lista if x > 0]
    negativos = [x for x in lista if x < 0]
    return positivos, negativos

# Cargo la lista de 10 elementos
lista_original = cargar_lista()

# Genero dos listas con valores positivos y negativos
positivos, negativos = separar_positivos_negativos(lista_original)

# Imprimo las dos listas generadas
print("\nLista de valores positivos:", positivos)
print("Lista de valores negativos:", negativos)
