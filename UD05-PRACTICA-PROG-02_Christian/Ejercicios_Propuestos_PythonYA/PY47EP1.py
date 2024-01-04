class Cuenta:
    def __init__(self, titular, monto):
        
        # Inicializo la clase Cuenta con atributos comunes.
        
        self.titular = titular
        self.monto = monto

    def consultar_saldo(self):
        
        # Consulto el saldo de la cuenta.
        
        return self.monto


class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        
        # Inicializo la clase CajaAhorro, heredando de la clase Cuenta.
        
        super().__init__(titular, monto)
        self.intereses_generados = 0

    def generar_intereses(self):
        
        # La CajaAhorro no genera intereses.
        
        print("La Caja de Ahorro no genera intereses.")


class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, tasa_interes):
        
        # Inicializo la clase PlazoFijo, heredando de la clase Cuenta y añadiendo atributos específicos.
        
        super().__init__(titular, monto)
        self.plazo = plazo
        self.tasa_interes = tasa_interes

    def generar_intereses(self):
        
        # Genero intereses para el PlazoFijo.
        
        intereses = self.monto * self.tasa_interes * self.plazo / 365
        self.monto += intereses
        print(f"Intereses generados en Plazo Fijo: {intereses}")


# Ejemplo 
caja_ahorro = CajaAhorro("Juan Pérez", 5000)
plazo_fijo = PlazoFijo("Ana García", 10000, 30, 0.05)

# Consultar saldos
print(f"Saldo en Caja de Ahorro: {caja_ahorro.consultar_saldo()}")
print(f"Saldo en Plazo Fijo: {plazo_fijo.consultar_saldo()}")

# Generar intereses
caja_ahorro.generar_intereses()
plazo_fijo.generar_intereses()

# Consultar saldos después de generar intereses
print(f"Saldo en Caja de Ahorro: {caja_ahorro.consultar_saldo()}")
print(f"Saldo en Plazo Fijo: {plazo_fijo.consultar_saldo()}")
