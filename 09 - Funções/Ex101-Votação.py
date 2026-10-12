
def votar(nasc):
    from datetime import date
    hj = date.today().year
    idade = hj - nasc

    if idade < 16:
        return f'Com {idade} anos não vota'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos o voto é OPCIONAL'
    else:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'

nasc = int(input('Ano de nascimento: '))
print(votar(nasc))