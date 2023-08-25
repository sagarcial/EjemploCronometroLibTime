from unidad_tiempo import UnidadTiempo

class Hora(UnidadTiempo):
    def avanzar(self):
        self.valor = (self.valor + 1) % 24

    def resetear(self):
        self.valor = 0
