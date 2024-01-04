# Clase Paciente que hereda de Persona
from Persona import Persona

class Paciente(Persona):
    def __init__(self, dni, nombre, direccion, telefono):
        super().__init__(dni, nombre, direccion, telefono)
        self.historial = []

    def agregar_prueba(self, prueba):
        self.historial.append(prueba)
