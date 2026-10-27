palavra_secreta = "perfume"
letras_acertadas = ''
cont = 0

while True:
    letra_digitada = str(input("Digite uma letra: "))
    cont += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    ganhou = True

    for letras_secreta in palavra_secreta:
        if letras_secreta in letras_acertadas:
            print(letras_secreta, end='')
        else:
            print('*', end='')
            ganhou = False
    print()

    if ganhou:
        print(f"\nVOCÊ GANHOU! A palavra era '{palavra_secreta}'.")
        print(f"Total de tentativas: {cont}")
        break