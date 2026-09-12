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
    if idade >= 18:
        if sx == 'm':
            somamaiorm += 1
        elif sx == 'f':
            somamaiorf += 1
        else:
            print('Sexo inválido! Digite apenas M ou F.')

    elif idade < 18:
        if sx == 'm':
            somamenorm += 1
        elif sx == 'f':
            somamenorf += 1
        else:
            print('Sexo inválido! Digite apenas M ou F.')

print(f'A média da idade é {somaidade / 4}.')
print(f'O grupo têm {somamaiorm + somamaiorf} pessoas maiores de idade.')
print(f'O grupo têm {somamenorm + somamenorf} menores de idade.')
print(f'O grupo têm {somamaiorf} mulheres maior de idade.')