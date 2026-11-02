from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        caixa = Panel(f'{self.nome:^30}\n{"":-^30}\n{self.valor:.^30,.2f}', title="Produto",width=35)
        return caixa


p1 = Produto('Mouse', 135)
print(p1.etiqueta())