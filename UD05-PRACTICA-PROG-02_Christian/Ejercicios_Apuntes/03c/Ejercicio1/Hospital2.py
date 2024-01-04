# hospital.py
from Medico import Medico
from Enfermero import Enfermero
from Paciente import Paciente
from Prueba_Consulta import PruebaConsulta


# Crear medicos y enfermeros del hospital
medico1 = Medico("123456789", "Dr. Jaume", "Calle A", "123456789", "Cardiología")
enfermero1 = Enfermero("987654321", "Enfermero Alejandro", "Calle B", "987654321", "Planta 1")

# Crear paciente
paciente1 = Paciente("11111111A", "Christian", "Calle Contubernio 49", "666666666")

# Agregar pruebas hechas por los médicos al historial del paciente
prueba1 = PruebaConsulta("2024-01-03", medico1)
prueba2 = PruebaConsulta("2024-01-04", medico1)

paciente1.agregar_prueba(prueba1)
paciente1.agregar_prueba(prueba2)

# Mostrar datos completos del paciente
print("Datos del paciente:")
print(f"DNI: {paciente1.dni}")
print(f"Nombre: {paciente1.nombre}")
print(f"Dirección: {paciente1.direccion}")
print(f"Teléfono: {paciente1.telefono}")

print("\nHistorial de pruebas:")
for prueba in paciente1.historial:
    print(f"Fecha: {prueba.fecha}")
    print(f"Médico: {prueba.medico.nombre}, Especialidad: {prueba.medico.especialidad}")
    print("----------------------------")

