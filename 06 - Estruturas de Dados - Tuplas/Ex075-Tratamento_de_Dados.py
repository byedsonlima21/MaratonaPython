num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
a = 0

print(f'Os números digitados foram: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print(f'O número 3 não está na tupla')
for n in num:
    if n % 2 == 0:
        a += 1
print(f'{a} valores é/são par(es)')
