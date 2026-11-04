from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, qnt=5):
        self.titulo = titulo
        self.qnt = qnt

    def analise(self):
        qnt_carne = self.qnt * 0.4
        preco_total = qnt_carne * 82.42
        dados = Panel(f'{""}\nAnalisando o [green]{self.titulo}[/] com [blue]{self.qnt} convidados[/]\n'
                      f'Cada convidado comerá 0.4kg de carne e cada kg custa R$82,42\n'
                      f'Quantidade de Carne: [red]{qnt_carne:,.3f}kg[/]\nPreço Total: R${preco_total:,.2f}\n'
                      f'Preço por pessoa: [yellow]R${preco_total/self.qnt:.2f}[/]', title=self.titulo, width=70)
        print(dados)


c1 = Churrasco('Carne com Friends', 15)
c2 = Churrasco('Casamento do João', 84)
c1.analise()
c2.analise()