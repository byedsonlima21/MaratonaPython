idades = []
sexos = []
sxmaiormasc = sxmaiorfem = maiores = 0
sxfemmen = sxmascmen= 0
qnth = qntf = 0


while True:
    idade = int(input('Idade: '))
    sx = str(input('Sexo: ')).strip().lower()[0]

    while sx not in 'mf':
        print('OPÇÃO INVÁLIDA!')
        sx = str(input('Sexo: ')).strip().lower()[0]

    idades.append(idade)
    sexos.append(sx)

    confirmacao = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    while confirmacao not in 'sn':
        print('OPÇÃO INVÁLIDA!')
        confirmacao = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if confirmacao == 'n':
        break

for idade, s in zip(idades, sexos):

    if idade >= 18:
        maiores += 1

    if s == 'm':
        qnth += 1
        if idade >= 18:
            sxmaiormasc += 1
        else:
            sxmascmen += 1

    elif s == 'f':
        qntf += 1
        if idade >= 18:
            sxmaiorfem += 1
        else:
            sxfemmen += 1


print(f'Tem {maiores} maiores de idade')
print(f'Têm {qnth} do sexo masculino e {qntf} do sexo feminino.')
print(f'Têm {sxmaiormasc} pessoas masculinas maiores de idade e {sxmaiorfem} do sexo feminino.')
print(f'Têm {sxmascmen} pessoas masculinas menores de idade e {sxfemmen} do sexo feminino.')
