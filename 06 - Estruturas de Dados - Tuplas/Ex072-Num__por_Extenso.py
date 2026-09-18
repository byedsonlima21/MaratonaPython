num = 0
lst = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']

while 0 <= num <= 10:
    num = int(input("Digite um numéro entre  0 e 10: "))

    name = lst[num]

    print(f'Você escolheu o número {name}')

    continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continua in "Nn":
        break