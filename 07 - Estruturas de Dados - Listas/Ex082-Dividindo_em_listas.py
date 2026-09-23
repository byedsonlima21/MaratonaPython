todos = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    todos.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Lista geral: {todos}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos impares: {impares}')