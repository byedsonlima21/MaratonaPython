somaidade = 0
somamaiorm = 0
somamaiorf = 0
somamenorm = 0
somamenorf = 0

for c in range(1, 5):
    print(f'--{c}ª PESSOA--')
    #nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sx = str(input('Sexo [M/F]: ')).lower().strip()

    somaidade += idade
    if idade >= 18 and sx == 'm':
        somamaiorm += 1

    elif idade >= 18 and sx == 'f':
        somamaiorf += 1

    elif idade < 18 and sx == 'm':
        somamenorm += 1

    elif idade < 18 and sx == 'f':
        somamenorf += 1

print(f'A média da idade é {somaidade / 4}.')
print(f'O grupo têm {somamaiorm + somamaiorf} pessoas maiores de idade.')
print(f'O grupo têm {somamenorm + somamenorf} menores de idade.')
print(f'O grupo têm {somamaiorf} mulheres maior de idade.')