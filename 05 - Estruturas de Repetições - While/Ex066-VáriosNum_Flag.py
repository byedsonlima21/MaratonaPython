a = 0
l = []

while True:
    a = int(input(f'Digite um valor: '))
    if a == 999:
        break
    l.append(a)

print(f'A soma dos valores é {sum(l)} e a média é {sum(l)/len(l):.2f}')