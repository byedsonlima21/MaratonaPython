from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampa = True

    def escrever(self, msg):
        conteudo = f'[{self.cor}] {msg} [/]'
        print(f'Você precisa destampar a caneta primeiro' if self.tampa == True else conteudo)

    def destampar(self):
        self.tampa = False

    def quebrar_linha(self, pular):
        n = pular
        for i in range(n):
            print()

c1 = Caneta('blue')
c1.escrever('Oi a todos')
c1.destampar()
c1.quebrar_linha(1)
c1.escrever('E ai mano, como vai?')
c1.quebrar_linha(1)

c2 = Caneta('red')
c2.escrever('Nao devo nada a ninguém')
c2.destampar()
c2.quebrar_linha(1)
c2.escrever('Eu ontem tive tanta sorte, a malvada da morte')