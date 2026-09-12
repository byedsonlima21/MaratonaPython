a = e = 0
s = []

while a != 999:
    a = int(input('Digite um número: '))
    e += 1

    if a != 999:
        s.append(a)
    else:
        break


print(f'A soma dos valores é {sum(s)} e você escolheu {e - 1} números.')
