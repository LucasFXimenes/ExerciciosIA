
class Livro:
    def __init__ (self,titulo,autor,disponivel):
        self.titulo = titulo 
        self.autor = autor 
        self.disponivel = disponivel 

class Biblioteca:
    def __init__(self,adicionar,emprestar,devolver,listar):
        self.adicionar = adicionar
        self.emprestar = emprestar
        self.devolver = devolver
        self.listar = listar
