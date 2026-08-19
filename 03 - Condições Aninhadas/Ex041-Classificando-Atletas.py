from datetime import date
nasc = int(input('Digite o ano de nascimento do aluno: ').strip())
idade = date.today().year - nasc

#CONDIÇÕES
if 0 < idade < 10:
    print(f'O aluno tem {idade} anos, então se encaixa na categoria Mirim.')
elif 10 <= idade < 17:
    print(f'O aluno tem {idade} anos, então se encaixa na categoria Infantil.')
elif 17 <= idade < 21:
    print(f'O aluno tem {idade} anos, então se encaixa na categoria Junior.')
elif idade >= 21:
    print(f'O aluno tem {idade} anos, então se encaixa na categoria Senior.')
else:
    print(f'O aluno tem {idade} anos, então se encaixa na categoria Master.')