from random import randint

lista = []
cont = 0

n = int(input("Quantos jogos você quer que eu sorteie? "))
print(f'Sorteando {n} jogos')

while cont < n:
    cont = 0
    num = [randint(1,60)]
    for c in range(0, n):
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
print(f'Jogo {c+1}: {num}')
