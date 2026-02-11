class Turma:

    def __init__(self, nome_da_turma):
        self.nome_da_turma = nome_da_turma
        self.lista_alunos = []

    def adicionar_aluno(self, nome):
        self.lista_alunos.append(nome)
        print(f'Aluno(a) {nome} adicionado!')

    def remover_aluno(self, nome):
        if nome in self.lista_alunos:
            self.lista_alunos.remove(nome)
            print(f'Aluno(a) {nome} removido!')
        else:
            print('Aluno não encontrado!')

    def listar_alunos(self):
        print(self.lista_alunos)

    def quantidade(self):
        print(len(self.lista_alunos))


t1 = Turma("Python")
t1.adicionar_aluno("Lucas")
t1.adicionar_aluno("Ana")
t1.listar_alunos()
t1.quantidade()
