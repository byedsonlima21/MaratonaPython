def escreva(txt):
    txt_formatado = f' {txt} '
    tam = len(txt_formatado) + 10
    print('-' * tam )
    print(f'{txt_formatado:-^{tam}}')
    print('-'* tam )

escreva('Edson Lima')
print()
escreva('Josue Pereira Lima')
print()
escreva('Neymar dos Santos Junior')
print()
escreva('Edson Oliveira de Santos Junior')
