jogador = dict()
gols = []

jogador['nome'] = str(input('Nome do jogador: ')).title()
jogos = int(input(f'Quantos jogos teve {jogador["nome"]} no campeonato? '))
for i in range(jogos):
    gols.append(int(input(f'Quantos gols marcou na {i+1}ª partida? ')))
jogador['gols'] = gols.copy()
jogador['total'] = sum(gols)

print('-='*25)
print(jogador)
print('-='*25)

print(f'O {jogador['nome']} marcou {jogador["total"]} gols no campeonato!')
for m, n in enumerate(jogador['gols']):
    print(f'Na partida {m+1} fez {n} gols')
print('-='*25)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*25)