palavra = ('estudar', 'python', 'programação', 'escola', 'programador', 'mercado', 'praticar', 'trabalhar')

for i in palavra:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')