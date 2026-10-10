from random import randint

num = []

def sorteio():
    for i in range(5):
        num.append(randint(1, 50))
    print(f'Os numeros sorteador foram: {num}')

def somatorio():
    soma = 0
    for i in num:
        if i % 2 == 0:
            soma += i
    print(f'Soma dos pares: {soma}')

sorteio()
somatorio()