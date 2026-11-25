from rich import print
from rich.panel import Panel
import subprocess

class TV:
    canal_min: int = 1
    canal_max: int = 8
    volume_min:int = 1
    volume_max: int = 5


    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume:int = volume
        self.power = False

    def ligar_tv(self):
            self.power = True

    def canal_mais(self):
        if self.power == True:
            if self.canal_atual == self.canal_max:
                self.canal_atual = self.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.power == True:
            if self.canal_atual == self.canal_min:
                self.canal_atual = self.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.power == True:
            if self.volume == self.volume_max:
                self.volume = self.volume_max
            else:
                self.volume += 1

    def volume_menos(self):
        if self.power == True:
            if self.volume == self.volume_min:
                self.volume = self.canal_min
            else:
                self.volume -= 1

    def funcoes(self):
        conteudo = ''

        if self.power == False:
            conteudo = f':prohibited: A TV está desligada'
        else:
            conteudo = f'CANAL  = '
            for canal in range(TV.canal_min, TV.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f'[black on red] {canal} [/]'
                else:
                    conteudo += f' {canal} '

            conteudo += '\nVOLUME = '

            for vol in range(TV.volume_min, TV.volume_max + 1):
                if vol == self.volume:
                    conteudo += f'[black on yellow] {vol} [/]'
                else:
                    conteudo += f' {vol} '

        painel = Panel(conteudo, title='[ TV ]', width=40)
        print(painel)

tv = TV()
while True:
    tv.funcoes()
    comando = str(input(f' < CH >  - VOL + \n'))

    match comando:
        case '0':
            break
        case '@':
            tv.ligar_tv()
        case '<':
            tv.canal_menos()
        case '>':
            tv.canal_mais()
        case '-':
            tv.volume_menos()
        case '+':
            tv.volume_mais()
    subprocess.run('cls', shell=True)