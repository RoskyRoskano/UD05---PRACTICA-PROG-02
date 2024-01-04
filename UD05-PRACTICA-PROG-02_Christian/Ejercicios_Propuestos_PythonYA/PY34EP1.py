def cargar_personas():
    
    # Carga por teclado los datos de 4 personas en un diccionario.
    
    personas = {}

    for i in range(4):
        documento = input(f"Ingrese el dni de la persona {i+1}: ")
        nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
        personas[documento] = nombre

    return personas

def listar_personas(personas):
    
    # Lista completa del diccionario.
    
    print("\nListado completo del diccionario:")
    for documento, nombre in personas.items():
        print(f"Documento: {documento}, Nombre: {nombre}")

def consultar_nombre_por_documento(personas):
    
    # Consulta del nombre de una persona ingresando su dni.
    
    documento_consulta = input("\nIngrese el dni para consultar el nombre: ")
    
    if documento_consulta in personas:
        print(f"El nombre de la persona con documento {documento_consulta} es: {personas[documento_consulta]}")
    else:
        print(f"No se encontró la persona con documento {documento_consulta}.")

# Ejemplo
datos_personas = cargar_personas()
listar_personas(datos_personas)
consultar_nombre_por_documento(datos_personas)
