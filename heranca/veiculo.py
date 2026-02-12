class Veiculo:
    def __init__(self, marca, modelo, estado):
        self.marca = marca
        self.modelo = modelo
        self._estado = estado

    def __str__(self):
        return f"{self.marca} {self.modelo} | Ligado: {self._estado}"
