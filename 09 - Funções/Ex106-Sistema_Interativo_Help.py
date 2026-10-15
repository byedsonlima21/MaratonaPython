from time import sleep

cores = {
    'padrao': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[0;30m'
}

def cabecalho(msg, cor='padrao'):
    tam = len(msg) + 10
    print(cores[cor], end='')
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)
    print(cores['padrao'], end='')

def ajuda(a):
    cabecalho(f'Acessando o manual do comando \'{a}\'', 'azul')
    sleep(0.5)
    help(a)

while True:
    cabecalho('Sistema Interativo Help', 'amarelo')
    comando = str(input('Biblioteca ou função -> ')).upper()
    sleep(0.3)
    if comando == 'FIM':
        sleep(0.6)
        break
    else:
        sleep(0.3)
        ajuda(comando)
    sleep(0.4)

cabecalho('PROGRAMA FINALIZADO!', 'vermelho')