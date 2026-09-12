a = 0
s = []
e = 0
while a != 999:
    b = int(input('Digite um número: '))
    a = b
    s.append(b)
    e += 1

print(f'A soma dos valores é {sum(s) - 999} e você escolheu {e - 1} números.')
