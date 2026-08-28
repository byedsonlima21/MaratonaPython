print('='*15,'Loja do Edson','='*15)
s = float(input('Qual o valor da sua compra? R$'))

print('FORMAS DE PAGAMENTO:\n'
      '[1] à vista no dinheiro/cheque\n'
      '[2] à vista no cartão\n'
      '[3] 2x no cartão\n'
      '[4] 3z no cartão de crédito\n')

op = int(input('Qual sua forma de pagamento? R= '))

if op == 1:
    print(f'Você ganha um desconto de 5% ao pagar sua compra escolhendo a opção 1.\n'
          f'O valor a ser pago é de {s - ( s * 5 / 100)}')
elif op == 2:
    print(f'Você ganha um desconto de 3% ao pagar sua compra escolhendo a opção 1.\n'
          f'O valor a ser pago é de {s - ( s * 3 / 100)}')
elif op == 3:
    print(f'Você ganha um desconto de 1% ao pagar sua compra escolhendo a opção 1.\n'
          f'O valor a ser pago é de {s - ( s * 1 / 100)}')
elif op == 4:
    print(f'Você ganha um desconto de 1% ao pagar sua compra escolhendo a opção 1.\n'
          f'O valor a ser pago é de {s - ( s * 0.5 / 100)}')
elif op 1 or 2 or 3 or 4:
    print('Opção inválida!\n'
          'Escolha entre as opções disponiveis')