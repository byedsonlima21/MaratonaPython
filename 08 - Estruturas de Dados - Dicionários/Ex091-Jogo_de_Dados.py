from random import randint
from time import sleep
from operator import itemgetter

mai = men = 0
dados = dict()

for c in range(0, 5):
    dados[f'jogador{c+1}'] = randint(1, 6)
    if c == 0:
        mai = men = dados[f'jogador{c+1}']
    else:
        if dados[f'jogador{c+1}'] > mai:
            mai = dados[f'jogador{c+1}']
        elif dados[f'jogador{c+1}'] < men:
            men = dados[f'jogador{c+1}']

print("-=" * 20)

for k, v in dados.items():
    print(f'{k} tirou {v}')
    sleep(0.9)
rank = sorted(dados.items(), key=itemgetter(1), reverse=True)

print("-=" * 20)
sleep(0.8)
print("RANKING")
sleep(0.8)

for i, v in enumerate(rank):
    print(f'{i+1}° lugar = {v[0]} tirou {v[1]}')
    sleep(0.8)