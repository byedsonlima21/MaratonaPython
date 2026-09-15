while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    for c in range(1, 11):
        if num >= 0:
            print(f'{num} x {c:2} = {num * c:2}')
        else:
            print(f'Programa finalizado!')
            break