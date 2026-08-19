a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite um último número: '))

if a + b > c and a + c > b and b + c > a:
    print('Formam triângulo')
else:
    print('Não formam triângulo')