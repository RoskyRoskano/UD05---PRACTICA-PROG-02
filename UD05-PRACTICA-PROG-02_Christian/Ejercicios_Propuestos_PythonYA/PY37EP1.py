def cargar_lista():
    
    # Cargo de una lista de 10 enteros.
    
    lista = []
    for i in range(10):
        elemento = int(input(f"Ingrese el elemento {i+1}: "))
        lista.append(elemento)
    return lista

def obtener_mitad(lista):
    
    # Recibo una lista y retornar otra con la primera mitad.
    
    mitad = len(lista) // 2
    return lista[:mitad]

def imprimir_lista(lista):
    
    # Imprimo una lista.
    
    print("Lista:")
    for elemento in lista:
        print(elemento)

# Ejemplo
lista_enteros = cargar_lista()
lista_mitad = obtener_mitad(lista_enteros)
imprimir_lista(lista_mitad)
