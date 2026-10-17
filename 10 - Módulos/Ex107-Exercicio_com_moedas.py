import moedas

valor = float(input('Digite um valor: R$'))

print(f'O dobro do valor é R${moedas.dobro(valor):.2f}')
print(f'O triplo do valor é R${moedas.triplo(valor):.2f}')
print(f'O valor em dólares é {moedas.converter_dolar(valor):.2f}')

