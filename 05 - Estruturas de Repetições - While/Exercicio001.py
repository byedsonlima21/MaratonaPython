nome = 'Edson Lima'

while True:
    for l in nome:
        print(f'{l}*', end='')
    print()
    break


# Sem usar o for
name = 'José Marcos da Silva'
i = 0

while i < len(name):
    print(f'{name[i]}*', end='')
    i += 1