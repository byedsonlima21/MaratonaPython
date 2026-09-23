num = []

while True:
    num.append(int(input('Digite um valor: ')))

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break

num.sort(reverse=True)
print(f'Você digitou {len(num)} elementos.')
print(f'A lista em ordem decrescente: {num}')

if 5 in num:
    print('O valor 5 apareceu na lista.')
else:
    print('Na lista não tem o valor 5')