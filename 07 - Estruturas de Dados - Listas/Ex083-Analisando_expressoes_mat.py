exp = str(input('Digite a expressão númerica: '))
caracter = []

for simb in exp:
    if simb == '(':
        caracter.append('(')
    elif simb == ')':
        if len(caracter) > 0:
            caracter.pop()
        else:
            caracter.append(')')
            break
if len(caracter) == 0:
    print(f'Expressão válida')
else:
    print(f'Expressão não válida')