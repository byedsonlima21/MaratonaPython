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

for i, c in enumerate(jogos):
    print(f'Jogo {i+1}: {c}')
