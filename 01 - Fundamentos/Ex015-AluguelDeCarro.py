km = float(input("Quantos km você vai rodar com o carro? "))

dias = int(input("Quantos dias pretende ficar como o carro? "))

preco = (dias * 60) + (km * 0.15)

print(f'O preço total que você pagará é R${preco:.2f}')

