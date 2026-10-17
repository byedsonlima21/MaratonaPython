import moedas

valor = float(input('Digite um valor: R$'))

print(f'O dobro do valor é R${moedas.dobro(valor):.2f}')
print(f'O triplo do valor é R${moedas.triplo(valor):.2f}')
print(f'O valor em dólares é US${moedas.converter_dolar(valor):.2f}')
print(f'O valor com 10% de aumento é {moedas.aumentar(valor):.2f}')
print(f'O valor com 10% de desconto é {moedas.diminuir(valor):.2f}')
