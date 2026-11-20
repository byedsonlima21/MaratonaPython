from random import randint

nove_digitos = ''

for i in range(9):
    n = randint(0, 9)
    nove_digitos += str(n)

cont = 10
result = 0

for i in nove_digitos:
    result += int(i) * int(cont)
    cont -= 1

digito1 = (result * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

dez_digitos = nove_digitos + str(digito1)
cont = result = 0

for i in dez_digitos:
    result += int(i) * cont
    cont -= 1

digito2 = (result * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

novo_cpf = dez_digitos + str(digito2)


print(novo_cpf)
