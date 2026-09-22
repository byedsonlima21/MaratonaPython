lista = []

for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição {i + 1}: ')))

print(f'Você digitou os valores {lista}')

maior = max(lista)
menor = min(lista)

print(f'O maior valor digitado foi {max(lista)} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i + 1}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i + 1}... ', end='')