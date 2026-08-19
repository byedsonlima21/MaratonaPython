km= int(input('Quantos km você vai viajar? '))

if km <= 200:
    print(f'Sua esta apta para a promoção da empresa, ela custará R${km*0.45:.2f} reais')
else:
    print(f'Sua viagem custava R${km*0.50:.2f} reais')