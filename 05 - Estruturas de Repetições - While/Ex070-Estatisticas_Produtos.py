lst_prod = []
lst_preco = []


while True:
    prod = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))

    lst_prod.append(prod)
    lst_preco.append(preco)

    cont = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input("Opção inválida, escolha entre 'Sim' ou 'Não' ")).strip().lower()[0]

    if cont == 'n':
        break

print(f'A soma de suas compras foi de R${sum(lst_preco):.2f} reais.')
print(f'O produto mais caro foi de R${max(lst_preco)}')

