class UnidadTiempo:
    def __init__(self, valor):
        self.valor = valor

    def avanzar(self):
        pass

    def resetear(self):
        pass

    def __str__(self):
        return str(self.valor).zfill(2)
