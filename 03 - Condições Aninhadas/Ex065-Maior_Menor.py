a = int(input("Digite um número: "))
text = str(input("Deseja continuar? [S/N] : ")).upper().strip()[0]
x = []
t = 0

while text != 'N':
    if text == 'S':
        x.append(a)

    else:
        x.append(a)
        t += 1
        break
    a = int(input("Digite um número: "))
    text = str(input("Deseja continuar? [S/N] : ")).upper().strip()[0]
    x.append(a)
    t += 1

print(f"Você digitou {t} números e o valor máximo é {max(x)}")