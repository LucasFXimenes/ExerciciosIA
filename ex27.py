class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media

    def situacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

    def mostrar(self):
        print(f"Aluno: {self.nome}")
        print(f"Média: {self.calcular_media()}")
        print(f"Situação: {self.situacao()}")

a1 = Aluno("Lucas", 8, 6)
a1.mostrar()

a2 = Aluno("Juliana", 4, 5)
a2.mostrar()
