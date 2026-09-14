a = 0
l = []

while a != 999:
    a = int(input(f'Digite um valor: '))
    if a != 999:
        l.append(a)

print(f'A soma dos valores é {sum(l)} e a média é {sum(l)/len(l)}')