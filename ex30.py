class Carrinho:

    def __init__(self):
        self.lista_produtos = []

    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)
        print(f'{produto} adicionado ao carrinho.\n')

    def remover_produto(self, produto):
        if produto in self.lista_produtos:
            self.lista_produtos.remove(produto)
            print(f'{produto} removido do carrinho.\n')
        else:
            print('Este produto não está no carrinho.\n')

    def mostrar_total(self):
        print('Produtos no carrinho:')
        print(self.lista_produtos)
        print(f'Quantidade: {len(self.lista_produtos)}')


p1 = Carrinho()
p1.adicionar_produto('Teclado Razer')
p1.adicionar_produto('Mouse Razer')
p1.adicionar_produto('RTX 3060')

p1.mostrar_total()
p1.remover_produto('Mouse Razer')
p1.mostrar_total()