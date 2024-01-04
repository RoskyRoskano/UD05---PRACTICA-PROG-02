def contar_vocales(cadena):

    vocales = "aeiouAEIOU"
    # Cada vez que hay un un caracter que esta dentro de la variable vocales se suma 1
    cantidad_vocales = sum(1 for char in cadena if char in vocales)
    print(f"La cantidad de vocales en '{cadena}' es: {cantidad_vocales}")

# Llamo a la función desde el bloque principal con diferentes strings
print("Llamada 1:")
contar_vocales("Hola")

print("\nLlamada 2:")
contar_vocales("Adios")

print("\nLlamada 3:")
contar_vocales("Jaume")
