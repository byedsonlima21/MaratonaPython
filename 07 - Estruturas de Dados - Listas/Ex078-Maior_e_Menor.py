lista = []

for i in range(5):
    num=int(input(f'Digite um valor para a posição {i + 1}: '))
    lista.append(num)

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')