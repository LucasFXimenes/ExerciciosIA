class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def adicionar_estoque(self, qtd):
        self.quantidade += qtd
        print(f"{qtd} adicionados ao estoque")

    def vender(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            print(f"{qtd} vendidos")
        else:
            print("Estoque insuficiente")

    def valor_total(self):
        return self.preco * self.quantidade

    def mostrar(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Quantidade: {self.quantidade}")

p1 = Produto("Teclado", 100, 10)

p1.vender(3)
p1.adicionar_estoque(5)

p1.mostrar()
print(p1.valor_total())
