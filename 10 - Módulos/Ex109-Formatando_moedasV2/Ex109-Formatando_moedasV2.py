import moedas

valor = float(input('Digite um valor: R$'))

print(f'O dobro do valor {moedas.moeda(valor)} é {moedas.dobro(valor, formato=True)}')
print(f'O triplo do valor {moedas.moeda(valor)} é {moedas.triplo(valor, formato=True)}')
print(f'O valor {moedas.moeda(valor)} em dólares é {moedas.converter_dolar(valor, formato=True)}')
print(f'O valor {moedas.moeda(valor)} com 10% de aumento é {moedas.aumentar(valor, formato=True)}')
print(f'O valor {moedas.moeda(valor)} com 10% de desconto é {moedas.diminuir(valor, formato=True)}')
