from Ex115_Menu import *
from time import sleep

while True:
    menu()
    sleep(0.3)
    n = leiaint("Escolha uma opção: ")

    n = int(n)
    if n == 1:
        ver_pessoas()
    elif n == 2:
        cadastro()
    elif n == 3:
        sair()
        break
    else:
        print('-='*20)
        print('\033[31mOPÇÃO INVÁLIDA!!\033[m')