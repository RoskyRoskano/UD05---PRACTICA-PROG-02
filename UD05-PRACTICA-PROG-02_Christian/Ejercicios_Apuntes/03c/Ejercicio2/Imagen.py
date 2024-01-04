from PIL import Image
import os.path

def escalar_imagen(imagen, ancho, alto):
    # Abrir la imagen
    img = Image.open(imagen)

    # Escalar la imagen
    img = img.resize((ancho, alto))

    # Obtener el nombre del archivo original sin extensión
    nombre_original = imagen.split('.')[0]

    # Crear el nombre del archivo escalado
    nombre_escalado = f"{ancho}_{alto}_{nombre_original}.png"

    # Guardar la imagen escalada
    img.save(nombre_escalado)
    print(f"Imagen escalada guardada como {nombre_escalado}")


# Solicitar al usuario el nombre de la imagen
nombre_imagen = input("Ingrese el nombre de la imagen (con extensión): ")

# Comprobar si existe el fichero
if (os.path.isfile(nombre_imagen)):
    # Solicitar al usuario los tamaños de escala
    while True:
        try:
            ancho = int(input("Ingrese el ancho de la imagen (0 para salir): "))
            if ancho == 0:
                break

            alto = int(input("Ingrese el alto de la imagen (0 para salir): "))
            if alto == 0:
                break

            # Escalar y guardar la imagen
            escalar_imagen(nombre_imagen, ancho, alto)

        except ValueError:
            print("Error: Ingrese valores numéricos para el ancho y el alto.")
else:
    print(f"La imagen {nombre_imagen} no existe")