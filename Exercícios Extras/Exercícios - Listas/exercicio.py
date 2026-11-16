#lembrar de ativar o 'emulate output' para funcionar o cls

from rich import print
import subprocess

lista = []

while True:
    print('Escolha uma opção:')
    usuario = input('[i]nserir, [a]pagar, [l]istar ').lower()[0]

    if usuario == 'i':
        subprocess.run('cls', shell=True)
        ind = int(input('Qual é o índice que você quer escolher? '))
        objeto = str(input('Qual é o item? ')).title()

        try:
            lista.insert(ind, objeto)

        except (ValueError, IndexError):
            print('Houve um erro ao inserir o dado')

    elif usuario == 'a':
        subprocess.run('cls', shell=True)
        if len(lista) == 0:
            print('A LISTA ESTÁ VAZIA!')
            continue

        try:
            indice_apagar = int(input('Qual é o índice que deseja apagar? '))
            del lista[indice_apagar]

        except (ValueError, IndexError):
            print('Não foi possível apagar esse índice ou item')

    elif usuario == 'l':
        subprocess.run('cls', shell=True)
        if len(lista) == 0:
            print('Não há nada para listar')


        elif len(lista) >= 1:
            for i, v in enumerate(lista):
                print(f'{i} - {v}')