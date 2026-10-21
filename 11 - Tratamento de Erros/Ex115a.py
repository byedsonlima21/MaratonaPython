import Ex115_Menu
from time import sleep

while True:
    Ex115_Menu.menu()
    sleep(0.3)
    n = input("Escolha uma opção: ").strip()

    n = int(n)
    if n == 1:
        Ex115_Menu.ver_pessoas()
    elif n == 2:
        Ex115_Menu.cadastro()
    elif n == 3:
        Ex115_Menu.sair()
        break
    else:
        print('-='*20)
        print('\033[31mOPÇÃO INVÁLIDA!!\033[m')