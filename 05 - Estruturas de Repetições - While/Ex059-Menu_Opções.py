n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
op = 0

while op != 5:
    print('\nSelecione as opções\n [1]somar\n [2]multiplicar\n [3]maior\n [4]novo\n [5]sair')
    op = int(input("Digite uma opção: "))
    if op == 1:
        print(f'A soma de {n1} + {n2} é igual a {n1+n2}.')
    elif op == 2:
        print(f'O produto de {n1} * {n2} é {n1*n2}.')
    elif op == 3:
        if n1 == n2:
            print(f'Os valores são iguais.')
        elif n1 > n2:
            print(f'O valor de {n1} é maior que o {n2}.')
        else:
            print(f'O valor de {n2} é maior que o {n1}.')
    elif op == 4:
        n1 = int(input("Digite um novo numero: "))
        n2 = int(input("Digite um novo numero: "))

    elif op == 5:
        print("Saindo do programa...")

    else:
        print('Valor inválido')