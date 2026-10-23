nome = 'Edson Lima'

while True:
    for l in nome:
        print(f'{l}*', end='')
    print()
    break

name = 'José Marcos da Silva'
i = 0


# Sem usar o for
while i < len(name):
    print(f'{name[i]}*', end='')
    i += 1