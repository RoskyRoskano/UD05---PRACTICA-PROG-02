def cargar_candidatos():
    # Función para cargar los votos obtenidos por tres candidatos.
    candidatos = []

    for i in range(3):
        nombre_candidato = input("Introduce el nombre del candidato: ")
        provincias_votos = []
        # Recogo todos los datos necesarios y los meto en la lista de candidatos
        cant_provincias = int(input(f"Introduce la cantidad de provincias para el candidato {nombre_candidato}: "))
        for j in range(cant_provincias):
            provincia = input("Introduce el nombre de la provincia: ")
            votos = int(input(f"Introduce la cantidad de votos para {nombre_candidato} en {provincia}: "))
            provincias_votos.append((provincia, votos))

        candidatos.append((nombre_candidato, provincias_votos))

    return candidatos

def total_votos(candidatos):
    # Imprimo el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias que tiene
    for candidato, provincias_votos in candidatos:
        total_votos = sum(votos for provincia, votos in provincias_votos)
        print(f"{candidato}: {total_votos} votos")

# Ejemplo
candidatos = cargar_candidatos()
total_votos(candidatos)
