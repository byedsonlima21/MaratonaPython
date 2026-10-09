from time import sleep

#def cabecalho():
#    print('-=' * 10)
#    print('CONTAGEM')
#    print('-=' * 10)


def cont():
    print('-=' * 10)
    print('CONTAGEM de 1 até 10!')
    for c in range(1, 11, 1):
        print(f'{c}', end=' ')
        sleep(0.5)
    print()

def cont1():
    print('-=' * 10)
    print('CONTAGEM de 10 até 1!')
    for i in range(10, 0, -1):
        print(f'{i}', end=' ')
        sleep(0.5)
    print()

def cont2():
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        for n in range(inicio, fim + 1, passo):
            print(f'{n}', end=' ', flush=True)
            sleep(0.5)
        print('Fim')
    else:
        for n in range(inicio, fim - 1, -passo):
            print(f'{n}', end=' ', flush=True)
            sleep(0.5)
    print('Fim')

cont2()