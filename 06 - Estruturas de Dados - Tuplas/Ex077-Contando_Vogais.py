palavra = ('ESTUDAR', 'PYTHON', 'PROGRAMACAO', 'ESCOLA', 'PROGRAMADOR', 'MERCADO', 'PRATICAR', 'TRABALHAR')

for i in palavra:
    print(f'\nNa palavra {i} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')