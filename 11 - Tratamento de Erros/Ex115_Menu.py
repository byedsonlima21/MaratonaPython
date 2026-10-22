from time import sleep

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

def cabecalho(txt):
    print('-=' * 20)
    print(f'{txt}'.center(40))
    print('-=' * 20)

def menu():
    cabecalho("MENU PRINCIPAL")
    print("""1 - Ver pessoas cadastradas \
        \n2 - Cadastrar uma pessoa \
        \n3 - Sair do sistema""")

#

#

#
