from unidad_tiempo import UnidadTiempo

class Minuto(UnidadTiempo):
    def avanzar(self):
        self.valor = (self.valor + 1) % 60

    def resetear(self):
        self.valor = 0
