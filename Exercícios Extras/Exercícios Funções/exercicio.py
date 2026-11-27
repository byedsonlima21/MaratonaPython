def teste(a, b, *args):
    return sum(args * 2)

testando = teste(2, 3, 4, 5, 6, 7, 10, 0)

print(testando)

print(4 * 2 + 5 * 2 + 6 * 2 + 7 * 2 + 10 * 2)

def impar_par(a):
    return 'é par' if a % 2 == 0 else 'é impar'

teste_logico = impar_par(testando)

print(teste_logico)