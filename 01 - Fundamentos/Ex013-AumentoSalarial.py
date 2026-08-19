sal = float(input("Digite o valor do seu sálario: "))

print(f'Se seu sálario é de R${sal:.2f}, com o ajuste de 15%,\nele fica de R${sal + (sal*15/100):.2f}')