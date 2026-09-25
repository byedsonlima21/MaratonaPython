matriz = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
       matriz[i].append(int(input('Digite um valor: ')))

for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()