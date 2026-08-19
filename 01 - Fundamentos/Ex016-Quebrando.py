import math

n = float(input('Digite um numero decimal: '))

print(f'O numero digitado foi {n} e o valor arredondado é {math.ceil(n)}.\nSendo assim, a parte inteira é {math.trunc(n)}')
print(f'A parte inteira é {int(n)}')