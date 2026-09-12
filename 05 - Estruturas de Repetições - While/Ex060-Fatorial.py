n = int(input("Digite um numero para calcular seu fatorial: "))
c = n
f = 1

print(f'Calculando {n}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    f *= c
    c -= 1

    if c > 0:
        print(f' X ', end='')
    else:
        print(f' = {f}', end='')






