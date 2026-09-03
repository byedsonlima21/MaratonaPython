soma = 0
a = 0

for c in range(1,501, 2):
    if c % 3 == 0:
        a = a + 1
        soma = soma + c

print(f'\nA soma dos {a} valores encontrados são {soma}.')