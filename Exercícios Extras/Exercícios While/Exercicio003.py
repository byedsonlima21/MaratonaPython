frase = 'De novo em um Maracanã lotado, diante de uma nova retranca armada por um argentino \
(coincidentemente um ex-técnico do Estudiantes). Mas desta vez o Flamengo saiu feliz.'

i = mai = 0
letra_mais_freq = ''

while i < len(frase):
    letra = frase[i]

    if letra.isalpha():
        mais_apareceu = frase.count(letra)

        if mais_apareceu > mai:
            mai = mais_apareceu
            letra_mais_freq = letra

    i += 1

print(f'A letra "{letra_mais_freq.upper()}" apareceu {mai} vezes')
