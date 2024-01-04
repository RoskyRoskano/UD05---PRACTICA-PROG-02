# Clase médico que hereda de persona
from Persona import Persona

class Medico(Persona):
    def __init__(self, dni, nombre, direccion, telefono, especialidad):
        super().__init__(dni, nombre, direccion, telefono)
        self.especialidad = especialidad
