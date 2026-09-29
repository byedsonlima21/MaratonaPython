from random import randint

lista = []
jogos = []
tot = 1

n = int(input("Quantos jogos você quer que eu sorteie? "))
print(f'Sorteando {n} jogos')

while tot <= n:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()

    tot += 1

for i, c in enumerate(jogos):
    print(f'Jogo {i+1}: {c}')
