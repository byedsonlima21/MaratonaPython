a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Pode formar um triângulo e ele é equilátero!')
    elif a != b != c != a:
        print('Pode formar um triângulo e é escaleno')
    else:
        print('Pode formar triângulo e é isósceles')
else:
    print('Não forma triângulo!')