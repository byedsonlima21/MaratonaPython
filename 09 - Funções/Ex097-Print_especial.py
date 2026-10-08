def escreva(txt):
    tam = len(txt)
    print('-' * (tam * 2))
    print(f'{'-':<5}{  txt  :^10}{'-':>5}')
    print('-'* (tam * 2))

escreva('Edson Lima')
print()
escreva('Adylla Lima')