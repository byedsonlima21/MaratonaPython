princ = []
temp = []
totmai = totmen = 0

while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    temp.append(nome)
    temp.append(peso)
    princ.append(temp[:])

# preciso treinar mais essas comparações, ou desenvolver uma melhor prática

    if len(princ) == 1:
        totmai = totmen = temp[1]
    else:
        if temp[1] > totmai:
            totmai = temp[1]
        if temp[1] < totmen:
            totmen = temp[1]

    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

print('-='*25)
print(f'Os dados foram {princ}')
print(f'Você cadastrou {len(princ)} pessoas')
print(f'A pessoa mais pesada é: ', end='')

for p in princ:
    if p[1] == totmai:
        print(f'{p[0]}')

print(f'A pessoa mais leve é: ', end='')

for i in princ:
    if i[1] == totmen:
        print(f'{i[0]}')