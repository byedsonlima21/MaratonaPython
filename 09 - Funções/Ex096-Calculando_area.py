def cal_area():
    c = float(input("Digite o comprimento (m): "))
    l = float(input("Digite o largura (m): "))
    area = c * l
    print(f'A área do terreno é {c} x {l} é de {area:.2f}m²')

def cabecalho():
    print('-=' * 20)
    print(f'{'=' * 5:<10}{" Cálculo do terreno ":^10}{'=' * 5:>10}')
    print('-=' * 20)

cabecalho()
cal_area()