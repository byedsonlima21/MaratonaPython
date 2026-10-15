def notas(*num, sit=False):
    d = dict()
    d['total'] = len(num)
    d['maior'] = max(num)
    d['menor'] = min(num)
    d['media'] = sum(num) / len(num)

    if sit == True:
        if d['media'] >= 7:
            d['situação'] = 'aprovado'
        elif d['media'] >= 5:
            d['situação'] = 'recuperação'
        elif d['media'] < 5:
            d['situação'] = 'reprovado'

    return d

n = notas(8, 6, 4.8, 7.7, sit=True)
print(n)

