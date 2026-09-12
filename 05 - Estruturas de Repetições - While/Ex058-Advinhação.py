from random import randint

palpite = 0
comp = randint(1, 10)
eu = int(input("Qual é o seu palpite? "))

while comp != eu:
    if eu > comp:
        print("Valor maior que o do computador")
        eu = int(input("Você errou. Tente novamente! "))
        palpite += 1
    else:
        print("Valor menor que o do computador")
        eu = int(input("Você errou. Tente novamente! "))
        palpite += 1

print(f"Parabéns! Você acertou em {palpite} palpites")