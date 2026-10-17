def dobro(v = 0, formato = True):
    if formato == True:
        return moeda(v * 2)
    else:
        return v * 2

def triplo(v = 0, formato = True):
    if formato == True:
        return moeda(v * 3)
    else:
        return v * 3

def converter_dolar(v = 0, formato = True):
    if formato == True:
        return moeda((v / 5.07), "US$")
    else:
        return v * 5.07

def aumentar(v = 0, formato = True):
    if formato == True:
        return moeda(v + (v * 0.1))
    else:
        return v + (v * 0.1)

def diminuir(v = 0, formato = True):
    if formato == True:
        return moeda(v - (v * 0.1))
    else:
        return v - (v * 0.1)

def moeda(v = 0, moeda = 'R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')