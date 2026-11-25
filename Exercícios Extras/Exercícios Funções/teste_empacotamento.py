def soma(*args):
    total = 0
    for n in args:
        total += n
    return total

soma1 = soma(2, 3, 4)
print(soma1)

numeros = 1, 2, 3, 4, 5
print(*numeros)
print(soma(*numeros))
#soma2 = soma(numeros)
print(sum(numeros))
print(sum(*numeros))