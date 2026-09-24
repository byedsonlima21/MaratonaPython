geral =[[],[]]
#temp = []

for i in range(5):
    n = int(input(f'Digite o {i+1}° valor: '))
    #temp.append(n)
    if n % 2 == 0:
        geral[0].append(n)
    else:
        geral[1].append(n)

print(f'Os valores pares são: {sorted(geral[0])}')
print(f'Os valores ímpares são: {sorted(geral[1])}')
