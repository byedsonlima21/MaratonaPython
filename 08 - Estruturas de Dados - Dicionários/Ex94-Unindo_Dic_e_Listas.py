geral= list()
pessoas = dict()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')).title().strip()

    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F] : ')).upper().strip()[0]
        if pessoas['Sexo'] in 'MF':
            break
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']

    geral.append(pessoas.copy())

    conf = str(input('Continuar? [S/N] ')).upper().strip()[0]
    while conf not in 'SN':
        print('Pro favor digite apenas S ou N')
    if conf == 'N':
        break

media = soma / len(geral)

print(f'Temos {len(geral)} pessoas cadastradas')
print(f'A média de idades é {media:.2f} anos')
print('As mulheres cadastradas foram ', end='')

for p in geral:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print('A lista das pessoas que estao acima da média são: ')
for p in geral:
    if p['Idade'] >= media:
        print('', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()