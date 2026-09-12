print('Vamos fazer o cálculo de uma Super PA!\n')

a1 = int(input('Qual é o primeiro termo que você simular? '))
a = a1
r = int(input('Qual é a razão? '))
res = 0
c = 1
t = 0
mais = 10

while mais != 0:
    t = t + mais

    while c <= t:
        print(f'{a1}', end=' -> ')
        a1 += r
        res += a
        c += 1
    print('Pausa')
    mais = int(input('Quantos mais termos deseja fazer? '))

print(f'FIM! Você viu {t} termos.')