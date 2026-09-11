from time import sleep

print("Vamos calcular uma PA!\n")
sleep(0.4)
a1 = int(input('Primeiro valor: '))
a = a1
r = int(input('Qual a razão? '))
pg = 10
res = 0
cont = 1

while cont <= 10:
    print(f'{a1}', end=' -> ')
    res = a1 + r
    a1 = res
    cont += 1
    if cont == 11:
        print(f'ACABOU!')