class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        aumento = self.salario * (porcentagem / 100)
        self.salario += aumento
        print(f"Aumento de {porcentagem}% aplicado")

    def desconto(self, valor):
        self.salario -= valor
        print(f"Desconto de {valor} aplicado")

    def mostrar(self):
        print(f"Funcionário: {self.nome}")
        print(f"Salário: {self.salario}")

f1 = Funcionario("Lucas", 5000)

f1.aumentar_salario(10)
f1.desconto(1000)
f1.mostrar()
