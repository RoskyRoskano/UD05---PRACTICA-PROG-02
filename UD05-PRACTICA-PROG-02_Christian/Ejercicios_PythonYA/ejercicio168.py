def cargar():
    # Cargo los contactos pidiendoselo al usuario
    contactos={}
    continua="s"
    while continua=="s":
        nombre=input("Ingrese el nombre del contacto:")
        telefono=input("Ingrese el numero de telefono:")
        contactos[nombre]=telefono
        continua=input("Ingresa otro contacto[s/n]?:")
    return contactos


def modificar_telefono(contactos):
    # Pregunto el nombre del contacto y si existe modifico el numero de telefono
    nombre=input("Ingrese el nombre de contacto a modificar el telefono:")
    if nombre in contactos:
        telefono=input("Ingrese el nuevo numero telefonico")
        contactos[nombre]=telefono
    else:
        print("No existe un contacto con el nombre ingresado")


def imprimir(contactos):
    # Imprimo todos los contactos
    print("Listado de todos los contactos")
    for nombre in contactos:
        print(nombre,contactos[nombre])


# bloque principal

contactos=cargar()
modificar_telefono(contactos)
imprimir(contactos)