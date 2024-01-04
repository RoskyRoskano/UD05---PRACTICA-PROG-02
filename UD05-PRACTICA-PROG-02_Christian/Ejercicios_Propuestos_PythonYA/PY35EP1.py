def cargar_alumnos():
    
    # Carga por teclado los datos de 3 alumnos en un diccionario.
    
    alumnos = {}

    for i in range(3):
        dni = input(f"Ingrese el DNI del alumno {i+1}: ")
        materias_notas = []

        cant_materias = int(input(f"Ingrese la cantidad de materias para el alumno {dni}: "))
        for j in range(cant_materias):
            materia = input(f"Ingrese el nombre de la materia {j+1}: ")
            nota = float(input(f"Ingrese la nota para la materia {materia}: "))
            materias_notas.append((materia, nota))

        alumnos[dni] = materias_notas

    return alumnos

def listar_alumnos(alumnos):
    
    # Lista todos los alumnos con sus notas.
    
    print("\nListado de todos los alumnos con sus notas:")
    for dni, materias_notas in alumnos.items():
        print(f"DNI: {dni}")
        for materia, nota in materias_notas:
            print(f"    Materia: {materia}, Nota: {nota}")

def consultar_alumno(alumnos):
    
    # Consulta de un alumno por su DNI, muestra las materias que tiene y sus notas.
    
    dni_consulta = input("\nIngrese el DNI del alumno para consultar sus notas: ")
    
    if dni_consulta in alumnos:
        print(f"\nNotas del alumno con DNI {dni_consulta}:")
        for materia, nota in alumnos[dni_consulta]:
            print(f"    Materia: {materia}, Nota: {nota}")
    else:
        print(f"No se encontró al alumno con DNI {dni_consulta}.")

# Ejemplo
datos_alumnos = cargar_alumnos()
listar_alumnos(datos_alumnos)
consultar_alumno(datos_alumnos)
