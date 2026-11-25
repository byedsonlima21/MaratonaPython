def soma(x, y):
    return x + y


a = soma(2, 3)
b = soma(4, 5)
print(f'a = {a}\nb = {b}')
print(f'{a + b}')

def teste(a, b) -> int:
    print(a + b)

v1 = teste(3, 7)
v2 = teste(1, 7)

print(v1 + v2)
