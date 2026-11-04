from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        valor = f'  R${self.valor:,.2f}  '
        caixa = Panel(f'{self.nome:^30}\n{"":-^30}\n{valor:-^30}', title="Produto",width=35)
        print(caixa)


p1 = Produto('Mouse', 1_350.14)
p2 = Produto('Iphone 17 Pro Max', 3_298.05)
p3 = Produto('Notebook', 4_598.98)
p1.etiqueta()
p2.etiqueta()
p3.etiqueta()