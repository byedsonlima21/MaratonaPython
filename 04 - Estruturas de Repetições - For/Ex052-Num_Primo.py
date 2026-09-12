a = int(input("Digite um numero inteiro: "))
cont = 0

if a <= 1:
    print(f'O número {a} não é primo')
else:
    for c in range(1, a+1):
        if a % c == 0:
            print(f'\033[32m {c}', end= ' ')
            cont += 1

        else:
            print(f'\033[31m {c}', end= ' ')

if cont > 2:
    print(f'\nO número foi contado {cont} vezes e portanto não  é primo!')
else:
    print(f'\nO número foi contado {cont} vezes e portanto o número é primo!')


# nível de dificuldade mais alto, precisei raciocinar bem e precise de uma leve ajuda