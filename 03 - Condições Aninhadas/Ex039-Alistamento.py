from datetime import date

nasc = int(input('Qual ano que voce nasceu? '))
atual = date.today().year
idade = atual - nasc

print(f'Como você nasceu em {nasc}.\nVoce tem {idade} anos.')
if idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} anos atrás')
elif idade == 18:
    print('Você tem se alistar esse ano!')
else:
    print(f'Infelizmente voçê não pode se alistar!\nSeu alistamento será em {nasc + 18}')
