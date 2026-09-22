lista = []

for c in range (0, 5):
    n = int(input('Digite um valor: '))

    for i, v in enumerate(lista):

        if n <= v:
            lista.insert(i, n)
            print(f'O valor foi adicionado na posição {i}')
            break
    else:
        lista.append(n)
        print(f'Adicionado no final da lista (posição {len(lista) - 1})...')

print(f'Os valores digitados em ordem foram {lista}')