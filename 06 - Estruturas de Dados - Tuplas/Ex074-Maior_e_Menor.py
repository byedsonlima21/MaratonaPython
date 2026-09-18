from random import randint

lst = tuple(randint(0,10) for i in range(5))

print(f'Os números formam: {lst}')
print(f'O maior número é {max(lst)}')
print(f'O menor número é: {min(lst)}')