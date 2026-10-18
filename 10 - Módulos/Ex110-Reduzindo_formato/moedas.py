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
        return v / 5.07

def aumentar(v = 0, taxa = 0, formato = True):
    if formato:
        return moeda(v + (v * taxa / 100))
    else:
        return v + (v * taxa/100)

def diminuir(v = 0, taxa1= 0, formato = True):
    if formato:
        return moeda(v - (v * taxa1/100))
    else:
        return v - (v * taxa1/100)

def moeda(v = 0, moeda = 'R$'):
    return f'{moeda} {v:.2f}'.replace('.', ',')

def resumo(v, aumento = 10, promo = 5):
    print("~" * 30)
    print(f"{'Resumo do valor':^30}")
    print("~" * 30)
    print(f"Valor: \t\t\t\t{moeda(v)}")
    print(f"Dobro do Preço: \t{dobro(v, formato=True)}")
    print(f"Triplo do preço: \t{triplo(v, formato=True)}")
    print(f"Em dólar: \t\t\t{converter_dolar(v, formato=True)}")
    print(f"Aumentado em {aumento}%: \t{aumentar(v, aumento, formato=True)}")
    print(f"Diminuído em {promo}%: \t{diminuir(v, promo, formato=True)}")