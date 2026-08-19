salario = int(input('Qual o seu salario: '))

if salario <= 1650:
    print(f'Seu novo salário passa a ser de R${(salario * 15 / 100) + salario} reais.')
elif 1650 < salario <= 5500:
    print(f'Seu novo salário passa a ser de R${(salario * 10 / 100) + salario} reais.')
else:
    print(f'Se novo salário é de R${(salario * 5 / 100) + salario} reais.')