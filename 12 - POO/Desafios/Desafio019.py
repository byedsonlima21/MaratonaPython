from rich import print
from time import sleep

class Livro:

    def __init__(self, titulo, pagina):
        self.titulo = titulo
        self.pagina = pagina
        self.pagina_atual = 1

        print(f':open_book:Você abriu o livro [bold red]{self.titulo}[/] que tem [bold green]{self.pagina} páginas no total[/]'
              f' e você está na [bold yellow]página {self.pagina_atual}[/]')

    def avancar_pagina(self, pulo = 1):
        cont = 0

        while self.pagina_atual <= self.pagina:
            print(f'pag{self.pagina_atual} -> ', end='')
            sleep(0.3)
            self.pagina_atual += 1
            cont += 1
            if cont == pulo:
                print(f'Você avançou {cont} páginas')
                print(f'Você está na [green]página {self.pagina_atual}[/]')
                break
            if self.pagina_atual == self.pagina:
                print(f'\n:closed_book:[red]Você está o final do livro![/]')


l1 = Livro('Metamorfose', 20)
l1.avancar_pagina(5)
l1.avancar_pagina(15)
l1.avancar_pagina(5)
