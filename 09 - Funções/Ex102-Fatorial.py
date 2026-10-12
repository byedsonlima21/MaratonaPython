def fatorial(a=1, show=False):
    print('—'*25)
    """
    n é o número a ser calculado em fatorial
    :return:
    """
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