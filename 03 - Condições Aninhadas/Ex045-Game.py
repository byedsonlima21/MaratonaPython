from  random import randint

itens = ('', 'Pedra', 'Papel', 'Tesoura')
a = randint(1, 3)
print("Considere:\n"
               "1 = PEDRA\n"
               "2 = PAPEL\n"
               "3 = TESOURA\n")
b = int(input('Qual é a sua escolha? '))

if 1< b > 3:
    print('Opção Inválida!')
elif b == a:
    print('Deu empate!')
elif (b == 1 and a == 3) or (b == 2 and a == 1) or (b == 3 and a == 2):
    print(f'\033[1;34mVoce ganhou!\nO computador escolheu {itens[a]}')
else:
    print(f'\033[1;31mVoce perdeu!\nO computador escolheu {itens[a]}')