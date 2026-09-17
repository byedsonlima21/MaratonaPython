lst_preco = []
totmil = menor = c = 0
barato = ''

while True:
    prod = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))
    c += 1

    lst_preco.append(preco)
    if preco >= 1000:
        totmil += 1

    if c == 1 or preco < menor:
        menor = preco
        barato = prod

    cont = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while cont not in 'sn':
        cont = str(input("Opção inválida, escolha entre 'Sim' ou 'Não' ")).strip().lower()[0]

    if cont == 'n':
        break

print(f'A soma de suas compras foi de R${sum(lst_preco):.2f} reais.')
print(f'O produto mais caro foi de R${max(lst_preco)} e você tem {totmil} produtos que custam mais de R$1000.')
print(f'O produto mais barato foi {barato} e custou R${menor:.2f}.')

