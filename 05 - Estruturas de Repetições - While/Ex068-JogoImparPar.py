from random import randint

cont = 0

while True:
    comp = randint(0, 10)
    num = int(input(f'Me diga um número para jogar: '))
    a = str(input(f'Você quer par ou impar? [P/I] ')).strip().lower()[0]

    soma = num + comp

    if soma % 2 == 0:
        if a == 'p':
            print(f'Você ganhou. O computador escolheu {comp} e a soma é {soma}')
            cont += 1
        else:
            print(f'Você perdeu. O computador escolheu {comp} e a soma é {soma}')
            break

    elif soma % 2 != 0:
        if a == 'i':
            print(f'Você ganhou. O computador escolheu {comp} e a soma é {soma}')
            cont += 1
        else:
            print(f'Você perdeu. O computador escolheu {comp} e a soma é {soma}')
            break

print(f'Você ganhou {cont} vezes')