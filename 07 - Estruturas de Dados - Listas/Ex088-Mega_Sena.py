from random import randint

n = int(input("Quantos jogos você quer que eu sorteie? "))
num = [randint(0,60) for i in range(n)]
print(f'Sorteando {n} jogos')

for c in range(0, n):
    print(f'Jogo {c+1}: {randint(0,60), randint(0,60), randint(0,60), randint(0,60), randint(0,60), randint(0,60)}')