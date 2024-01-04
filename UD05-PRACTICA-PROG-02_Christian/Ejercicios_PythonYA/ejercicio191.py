class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def imprimir(self):
        # Imprimo las coordenadas
        print("Coordenada del punto")
        print("(",self.x,",",self.y,")")

    def imprimir_cuadrante(self):
        # Imprimo el cuadrante del Punto
        if self.x>0 and self.y>0:
            print("Primer cuadrange")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")


# bloque principal

punto1=Punto(10,-2)
punto1.imprimir()
punto1.imprimir_cuadrante()