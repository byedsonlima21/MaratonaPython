def leiaint(a):

    while True:
        valor = input(a)

        if valor.isdigit():
            return valor

        else:
            print('\033[31mERRO! Não é número.\033[m')
        break

n = leiaint('Diga um número: ')
print(f'Você acabou de digitar o número {n}')