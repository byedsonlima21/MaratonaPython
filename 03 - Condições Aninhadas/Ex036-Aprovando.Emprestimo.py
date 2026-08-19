valor_do_imovel = int(input('Qual o valor do imóvel que você deseja adquirir? '))
sal = int(input('Qual é o seu salário? '))
anos = float(input('Em quantos anos você quer pagar? '))

prestacao = valor_do_imovel / (anos * 12)

if prestacao > (sal * (30 / 100)):
    print('Não foi possível liberar seu empréstimo!')
else:
    print(f'Seu empréstimo ficou de R${prestacao:.2f} reais e você pagará em {anos*12:.0f} vezes')