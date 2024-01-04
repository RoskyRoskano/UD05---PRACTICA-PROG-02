class AgendaPersonal:
    def __init__(self):
        
        # Inicializo la clase AgendaPersonal con una lista vacía para almacenar contactos.
        
        self.contactos = []

    def cargar_contacto(self):
        
        # Cargo un contacto en la agenda con nombre, teléfono y mail.
        
        nombre = input("Ingresa el nombre de la persona: ")
        telefono = input("Ingresa el teléfono de la persona: ")
        mail = input("Ingresa el mail de la persona: ")

        contacto = {'Nombre': nombre, 'Teléfono': telefono, 'Mail': mail}
        self.contactos.append(contacto)
        print(f"Contacto {nombre} cargado en la agenda.")

    def listar_agenda(self):
        
        # Muestro un listado completo de la agenda.
        
        print("\nListado completo de la agenda:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto['Nombre']}, Teléfono: {contacto['Teléfono']}, Mail: {contacto['Mail']}")

    def consultar_contacto(self, nombre_consulta):
        
        # Consulto un contacto por nombre e imprime sus datos.
        
        encontrado = False
        for contacto in self.contactos:
            if contacto['Nombre'].lower() == nombre_consulta.lower():
                print(f"\nDatos de {nombre_consulta}:")
                print(f"Nombre: {contacto['Nombre']}")
                print(f"Teléfono: {contacto['Teléfono']}")
                print(f"Mail: {contacto['Mail']}")
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró el contacto {nombre_consulta} en la agenda.")

    def modificar_contacto(self, nombre_modificar):
        
        # Modifico el teléfono y mail de un contacto por nombre.
        
        encontrado = False
        for contacto in self.contactos:
            if contacto['Nombre'].lower() == nombre_modificar.lower():
                nuevo_telefono = input(f"Ingresa el nuevo teléfono para {nombre_modificar}: ")
                nuevo_mail = input(f"Ingresa el nuevo mail para {nombre_modificar}: ")

                contacto['Teléfono'] = nuevo_telefono
                contacto['Mail'] = nuevo_mail

                print(f"\nDatos modificados para {nombre_modificar}:")
                print(f"Nuevo teléfono: {nuevo_telefono}")
                print(f"Nuevo mail: {nuevo_mail}")

                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró el contacto {nombre_modificar} en la agenda.")

    def ejecutar_programa(self):
        
        # Muestro el menú y ejecuta las opciones seleccionadas.
        
        while True:
            print("\nMenú de opciones:")
            print("1- Carga de un contacto en la agenda.")
            print("2- Listado completo de la agenda.")
            print("3- Consulta ingresando el nombre de la persona.")
            print("4- Modificación de su teléfono y mail.")
            print("5- Finalizar programa.")

            opcion = input("Selecciona una opción (1-5): ")

            if opcion == '1':
                self.cargar_contacto()
            elif opcion == '2':
                self.listar_agenda()
            elif opcion == '3':
                nombre_consulta = input("Ingresa el nombre de la persona a consultar: ")
                self.consultar_contacto(nombre_consulta)
            elif opcion == '4':
                nombre_modificar = input("Ingresa el nombre de la persona a modificar: ")
                self.modificar_contacto(nombre_modificar)
            elif opcion == '5':
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

# Ejemplo
agenda = AgendaPersonal()
agenda.ejecutar_programa()
