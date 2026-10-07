geral = []
jogadores = dict()
gols = []

while True:
    jogadores.clear()
    gols.clear()

    jogadores['Nome'] = str(input('Nome: ')).title()
    jogadores['Jogos'] = int(input(f'Quantos jogos teve {jogadores["Nome"]}: '))

    for i in range(jogadores["Jogos"]):
        g = int(input(f'Quantos gols marcou na {i+1}ª partida: '))
        gols.append(g)

    jogadores['Gols'] = gols.copy()
    jogadores['Total'] = sum(jogadores['Gols'])

    geral.append(jogadores.copy())

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

print('-=' * 30)
print(f"{'  TABELA  ':=^60}")
print('-=' * 30)
print(f"{'Cod':<5}{'Nome':<18}{'Gols':<29}{'Total':>18}")

for i, v in enumerate(geral):
    print(f'{i+1:<5}{v["Nome"]:<18}{str(v["Gols"]):<29}{v["Total"]:>8}')

while True:
    conf = int(input('Quer mostrar dados de qual jogador? (999 para parar) '))
    if conf == 999:
        break

    if 1 <= conf <= len(geral):
        print('-=' * 30)
        print(f'LEVANTAMENTO DO {geral[conf -1]["Nome"]}')

        for k, i in enumerate(geral[conf -1]["Gols"]):
            print(f'Na partida {k+1}, marcou {i} gols.')
        print('-=' * 30)
    else:
        print(f'ERRO! Não existe jogador com código {conf}. Tente novamente!')