soma = 0
cont = 0

for c in range(0,6):
    a = int(input("Digite um número par: " ))
    if a % 2 == 0:
        soma = soma + a
        cont += 1

print(f'Você informou {cont} números pares e a soma dos valores escolhidos é: {soma}')