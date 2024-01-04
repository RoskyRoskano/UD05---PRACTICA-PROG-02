# Clase Enfermero que hereda de Persona
from Persona import Persona

class Enfermero(Persona):
    def __init__(self, dni, nombre, direccion, telefono, planta):
        super().__init__(dni, nombre, direccion, telefono)
        self.planta = planta
