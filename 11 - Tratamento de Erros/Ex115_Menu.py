from time import sleep

ppl = []
pessoas = dict()

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

def ver_pessoas():
    cabecalho("OPÇÃO 1")
    sleep(0.4)
    print(f'{"Nome":<10}{"Idade":>10}')
    for v in ppl:
        for i, k in v.items():
            print(f'{k}', end='')
        #print(f'{v}', end='')
    print()

def cadastro():
    cabecalho("OPÇÃO 2")
    sleep(0.4)
    pessoas['Nome'] = (input('Nome: ')).title()
    pessoas['Idade'] = (input('Idade: '))
    ppl.append(pessoas.copy())


def sair():
    cabecalho("OPÇÃO 3")
    sleep(0.5)
    print('\033[31mSaindo do sistema...\033[m')
