from random import randint

n = int(input("Quantos jogos você quer que eu sorteie? "))
print(f'Sorteando {n} jogos')

for c in range(0, n):
    num = [randint(0,60) for i in range(n)]
    print(f'Jogo {c+1}: {num}')
