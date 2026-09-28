from random import randint

lista = []
jogos = []
cont = 0

n = int(input("Quantos jogos você quer que eu sorteie? "))
print(f'Sorteando {n} jogos')

while cont < n:
    num = [randint(1,60)]
    while True:
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()

for c in range(0, n):
    print(f'Jogo {c+1}: {jogos}')
