def contar_mayores_de_edad(*edades):
    # Compruebo cuales son mayores o iguales a 18 para así poder contar cuantos hay
    mayores_de_edad = [edad for edad in edades if edad >= 18]
    cantidad_mayores = len(mayores_de_edad)
    return cantidad_mayores

# Ejemplo
edades_ingresadas = [15, 22, 19, 16, 25, 30, 17]
cantidad_mayores = contar_mayores_de_edad(*edades_ingresadas)

print(f"La cantidad de personas mayores o iguales a 18 años es: {cantidad_mayores}")
