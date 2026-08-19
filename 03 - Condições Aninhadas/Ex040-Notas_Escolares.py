nota1 = float(input('Qual a sua primeira nota: '))
nota2 = float(input('Qual a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Parabéns! Você está aprovado com média {media:.1f}!')
elif 4 < media < 7:
    print(f'Sua média foi {media:.1f}. Você  terá que fazer recuperação')
else:
    print(f'Infelizmente você foi reprovado! Sua media foi {media:.1f}')