tabela = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Bahia', 'Fluminense', 'Cruzeiro', 'Atlético-MG', 'Coritiba', 'Red Bull Bragantino', 'Santos', 'Botafogo', 'São Paulo', 'Vitória', 'Corinthians', 'Mirassol', 'Grêmio', 'Vasco', 'Internacional', 'Remo', 'Chapecoense')

while True:
    time = str(input("Digite um time: "))

    print(f'Os primeiros times da tabela são {tabela[0:5]}')
    print(f'Os últimos times da tabela são {tabela[-4:]}')
    print(f'Nomes em ordem alfabética: {sorted(tabela)}')
    print(f'O time "{time}" está na {tabela.index(time) + 1}ª posição')
    break

print('\nIsso é tudo pessoal')