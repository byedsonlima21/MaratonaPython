geral = []
jogadores = dict()
gols = []

jogadores['nome'] = str(input('Nome: ')).title()
jogadores['jogos'] = int(input(f'Quantos jogos teve {jogadores["nome"]}: '))

for i in range(jogadores["jogos"]):
    jogadores['gols'] = int(input(f'Quantos gols marcou na {i+1}ª partida: '))