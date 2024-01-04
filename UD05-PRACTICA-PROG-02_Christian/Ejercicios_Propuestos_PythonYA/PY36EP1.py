def cargar_empleados():
    
    # Carga los datos de los empleados en un diccionario.
    
    empleados = {}

    cant_empleados = int(input("Ingrese la cantidad de empleados a cargar: "))
    for i in range(cant_empleados):
        legajo = input(f"Ingrese el número de legajo del empleado {i+1}: ")
        nombre = input(f"Ingrese el nombre del empleado {legajo}: ")
        profesion = input(f"Ingrese la profesión del empleado {legajo}: ")
        sueldo = float(input(f"Ingrese el sueldo del empleado {legajo}: "))

        # Almacenar los datos en el diccionario
        empleados[legajo] = [nombre, profesion, sueldo]

    return empleados

def modificar_sueldo(empleados):
    
    # Modificar el sueldo de un empleado ingresando su número de legajo.
    
    legajo_modificar = input("Ingrese el número de legajo del empleado a modificar: ")

    if legajo_modificar in empleados:
        nuevo_sueldo = float(input(f"Ingrese el nuevo sueldo para el empleado {legajo_modificar}: "))
        empleados[legajo_modificar][2] = nuevo_sueldo
        print(f"Sueldo del empleado {legajo_modificar} modificado correctamente.")
    else:
        print(f"No se encontró al empleado con número de legajo {legajo_modificar}.")

def mostrar_analistas(empleados):
    
    # Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas".
    
    print("\nEmpleados con profesión 'analista de sistemas':")
    for legajo, datos in empleados.items():
        if datos[1] == "analista de sistemas":
            print(f"Legajo: {legajo}, Nombre: {datos[0]}, Profesión: {datos[1]}, Sueldo: {datos[2]}")

# Ejemplo
empleados_empresa = cargar_empleados()
modificar_sueldo(empleados_empresa)
mostrar_analistas(empleados_empresa)
