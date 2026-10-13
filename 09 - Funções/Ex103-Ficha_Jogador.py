def ficha(jogador='desconhecido', gols=0):

    if jogador == '':
        jogador = '<desconhecido>'

    if str(gols).isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f'O jogador {jogador} fez {gols} gols')

jogador = str(input('Qual o jogador: ')).title()
gols = input('Quantos gols: ')

ficha(jogador, gols)