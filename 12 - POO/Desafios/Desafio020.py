from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, jogos):
        self.favoritos.append(jogos)
        self.favoritos.sort()

    def status(self):
        conteudo = (f'Nome Real: [bold white on yellow] {self.nome} [/]\n\n'
                    f'Jogos Favoritos:')
        for i,v in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [blue]{v}[/]'


        #lista = [f':video_game: {jg}' for jg in self.favoritos]
        #jogos = '\n'.join(lista)
        #conteudo = (f'Nome Real: [bold red on yellow] {self.nome} [/]\n\n'
        #            f'Jogos favoritos:\n[bold blue]{jogos}[/]')
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width = 50)
        print(painel)


j1 = Gamer('Edson Lima', 'SrUchiha21')
j1.add_favoritos("The Witcher 3 - Wild Hunt")
j1.add_favoritos("Baldurs Gate 3")
j1.add_favoritos("Child Of Light")
j1.add_favoritos("Life is Strange")
j1.add_favoritos("Metal Gear Solid V - The Phantom Pain")
j1.add_favoritos("Assasins Creed - Brotherhood")
j1.add_favoritos("Crysis 3")
j1.add_favoritos("Call of Duty")
j1.add_favoritos("Dirty Bomb")
j1.add_favoritos("Creatverse")
j1.add_favoritos("Dont Starve Together")
j1.add_favoritos("Aragami")
j1.status()



j2 = Gamer('Josue da Silva', 'sobra_nada')
j2.add_favoritos("Dishonore: Death of the Outsider")
j2.add_favoritos("The Elder Scrolls V: Skyrim")
j2.add_favoritos("Warframe")
j2.add_favoritos("Left 4 Dead 2")
j2.add_favoritos("Bordelands 2")
j2.status()
