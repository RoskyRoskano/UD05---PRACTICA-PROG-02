def retornar_superficie(lado1, lado2):
    #Calculo la superficie del rectangulo
    superficie = lado1 * lado2
    return superficie

# Recojo las medidas del rectangulo
lado_a = int(input("Ingrese la longitud del primer lado del rectángulo: "))
lado_b = int(input("Ingrese la longitud del segundo lado del rectángulo: "))

# Llamo a la función y le paso los parametros
resultado = retornar_superficie(lado_a, lado_b)

print(f"La superficie del rectángulo es: {resultado}")
