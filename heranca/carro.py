from heranca.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, estado, portas):
        super().__init__(marca, modelo, estado)
        self.portas = portas

    def __str__(self):
        return f"{self.marca} {self.modelo} | Portas: {self.portas} | Ligado: {self._estado}"
