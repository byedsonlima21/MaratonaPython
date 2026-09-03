soma = 0
a = 0

for c in range(1,501, 2):
    if c % 3 == 0:
        a = a + 1
        soma = soma + c

print(f'\nA soma dos {a} valores encontrados são {soma}.')


# exercício importante pois fiz um erro de conflito de variaveis soma <=> c e usei o mesmo c no laço
# depois de ter entendido o erro, consegui refazer
