from heranca.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, estado, tipo):
        super().__init__(marca, modelo, estado)
        self.tipo = tipo

    def __str__(self):
        return f"{self.marca} {self.modelo} | Tipo: {self.tipo} | Ligado: {self._estado}"
