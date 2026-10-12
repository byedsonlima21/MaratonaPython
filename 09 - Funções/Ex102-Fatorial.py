def fatorial(a=1, show=False):
    """
    -> Calcule o fatorial de um número
    n é o número a ser calculado em fatorial
    show=True (opcional): mostra ou não a conta
    :return: o resultado do fatorial
    """
    print('—'*25)
    f = 1

    for c in range(a, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c:2d} x', end='')
            else:
                print(f'{c:2d} =', end=' ')

    return f

print(fatorial(5, True))
print(fatorial(7, False))

help(fatorial)