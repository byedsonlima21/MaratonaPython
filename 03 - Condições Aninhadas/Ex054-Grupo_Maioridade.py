from datetime import date

hoje = date.today().year
maior = 0
menor = 0

for i in range(1, 4):
    a = int(input(f'Em que ano a pessoa {i}ª nasceu? '))
    idade = hoje - a
    if idade > 18:
        maior += 1
    else:
        menor += 1

print(f'\033[31m{menor} pessoas maiores de idade\033[m')
print(f'\033[32m{maior} pessoas maiores de idade\033[m')

# dificuldade seria so a biblioteca (linha 3) que não tava lembrado o código exato, de resto tava ok