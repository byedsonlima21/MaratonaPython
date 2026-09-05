peso = []
acima_25 = 0
abaixo = 0

for i in range(1,6):
    b = float(input(f'Qual é o peso da {i}ª pessoa? '))
    peso.append(b)

for p in peso:
    if p >= 25:
        acima_25 += 1
    else:
        abaixo += 1
print(f'''O maior peso foi de \033[32m{max(peso)}kg\033[m e o menor foi \033[31m{min(peso)}kg\033[m.
{acima_25} pessoas com 25kg ou mais e {abaixo} têm menos de 25kg''')

# fui pouco adiante, bom desafio