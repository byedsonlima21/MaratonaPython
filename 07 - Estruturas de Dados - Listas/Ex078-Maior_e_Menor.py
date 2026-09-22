lista = []

for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição {i + 1}: ')))

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista)) + 1}')
print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista)) + 1}')