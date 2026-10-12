from datetime import date
hj = date.today().year

def votar():
    idade = hj - nasc

    if idade >= 18:
        if 18 <= idade < 70:
            print(f'Com {idade} anos o voto é OBRIGATÓRIO')
        else:
            print(f'Com {idade} anos o voto é OPCIONAL')
    elif 16 <= idade < 18:
        print(f'Com {idade} anos o voto é OPCIONAL')
    else:
        print(f'Com {idade} anos o voto é OPCIONAL')

nasc = int(input('Ano de nascimento: '))
votar()