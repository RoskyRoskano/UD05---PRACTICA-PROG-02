# Comprueba si en la cadena hay alguno de los patrones definidos en la variable patrones
def numeroPatrones(texto):
    texto_lower = texto.lower()

    patrones = ["00", "101", "abc", "ho"]
    contador_patrones = 0

    for patron in patrones:
        contador_patrones += texto_lower.count(patron)

    return contador_patrones

# Ejemplo
cadena_ejemplo = "000101ABC HoHo"
resultado = numeroPatrones(cadena_ejemplo)
print(f"El número total de patrones encontrados es: {resultado}")
