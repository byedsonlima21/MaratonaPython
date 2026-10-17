import moedas

valor = float(input('Digite um valor: R$'))

print(f'O dobro do valor {moedas.moeda(valor)} é {moedas.moeda(moedas.dobro(valor))}')
print(f'O triplo do valor {moedas.moeda(valor)} é R${moedas.triplo(valor)}')
print(f'O valor {moedas.moeda(valor)} em dólares é {moedas.moeda(moedas.converter_dolar(valor), "US$")}')
print(f'O valor {moedas.moeda(valor)} com 10% de aumento é {moedas.aumentar(valor)}')
print(f'O valor {moedas.moeda(valor)} com 10% de desconto é {moedas.diminuir(valor)}')
