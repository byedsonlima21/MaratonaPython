def leiaint(a):

    while True:
        try:
            valor = int(input(a))
            return valor

        except (ValueError, TypeError):
            print('\033[1;31mO Tipo do valor digitado é Inválido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário decidiu não informar os dados.\033[m')
            return 0

def leiareal(a):
    while True:
        try:
            valor = float(input(a))
            return valor

        except (ValueError, TypeError):
            print('\033[1;31mO Tipo do valor digitado é Inválido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário decidiu não informar os dados.\033[m')
            return 0


n = leiaint('Diga um número Inteiro: ')
m = leiareal("Digite número um Real: ")
print(f'Você digitou o número {n} como Inteiro \
e {m} como Real')
