lista = []

while True:
    num = int(input('Digite um valor: '))

    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print(f'Valor duplicado! Tente novamente')

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp in 'Nn':
        break

print(f'Você escolheu os valores {sorted(lista)}')




