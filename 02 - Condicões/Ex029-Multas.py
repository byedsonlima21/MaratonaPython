velocidade = int(input('Qual a velocidade que o carro estava? R= '))
if velocidade > 80:
    print(f'Você foi multado por excesso de velocidade! \033[31mSua multa foi de R${(velocidade - 80) * 7} reais. \033[m')
else:
    print('Parabéns pela boa conduta!')
