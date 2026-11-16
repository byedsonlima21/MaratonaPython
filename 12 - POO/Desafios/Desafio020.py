from rich.panel import Panel

class Gamer:
    lista_favoritos = []

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick

    def add_favoritos(self, jogos):
        lista_favoritos.append(jogos)

    def ficha(self):
        ficha = Panel(f'Jogador {self.nick}')


p1 = Gamer('Edson', 'SrUchiha')
add_favoritos()