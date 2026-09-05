a = input('Digite algo que queira testar: ').upper().replace(' ', '')
b = a[::-1]

for i in range(0, len(b)):
    if b == a:
        print('\033[32mTemos um palíndromo\033[m')
        break
    else:
        print('\033[31;40mO que você digitou não é um palíndromo\033[m')
        break

        # exercício difícil, maior dificuldade foi inverter a frase
        # precise consultar