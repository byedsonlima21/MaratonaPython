
# Tipos: 0-None ; 1-Negrito ; 4-Sublinhado ; 7-Negativo (inverte)
# Textos: 30-Branco ; 31-Vermelho ; 32-Verde ; 33-Amarelo ; 34-Azul ; 35-Roxo ; 36-Ciano ; 37-Cinza
# Fundo: 40-Branco ; 41-Vermelho ; 42-Verde ; 43-Amarelo ; 44-Azul ; 45-Roxo ; 46-Ciano ; 47-Cinza

print('\033[1;31;40mTexto em Negrito, Vermelho, Fundo Branco\033[m')
print('\033[4;32;44mTexto Sublinhado, Verde, Fundo Azul\033[m')
print('\033[7;33mTexto Negativo (Amarelo)\033[m')
print('\033[0;36;40mTexto apenas Ciano\033[m')

#Se não fechar o código, ele fica até o final do terminal
#Nos prints abaixo eu não fechei no primeiro, mas sim no segundo

print('\033[4;31;44mEu gosto de aprender em Python')
print('Quero testar se nao fechar o código\033[m')

# Testando novo print depois de fechar código
print('Testando depois de fechar o código')

# Testando com variáveis

a = 2
b = 3
print(f'O valor de A É \033[1;31;40m{a}\033[m e o valor de B é \033[7;33m{b}\033[m.')

print('\033[1;31;47mAdylla\033[m, eu te amo chatinha')
