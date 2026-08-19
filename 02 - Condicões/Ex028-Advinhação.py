import random

comp = random.randint(0,10)

user = int(input('Digite um número inteiro de 0 a 10: '))

if user == comp:
    print('Parabéns! Você acertou')
else:
    print('Não foi dessa vez!')