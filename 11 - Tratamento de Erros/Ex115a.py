from Ex115_Menu import *
from Ex115b_aquivo import *
from time import sleep


arq = 'cursoemvideo'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    menu()
    sleep(0.3)
    n = leiaint("Escolha uma opção: ")

    n = int(n)
    if n == 1:
        lerArquivo(arq)
    elif n == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif n == 3:
        cabecalho("Saindo do sistema...")
        break
    else:
        print('-='*20)
        print('\033[31mOPÇÃO INVÁLIDA!!\033[m')