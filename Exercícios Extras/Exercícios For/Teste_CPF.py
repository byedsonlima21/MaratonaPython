from rich import print

cpf_usuario = '20765687003' \
    .replace('.', '') \
    .replace('-', '')

nove_dig = cpf_usuario[0:9]
result = 0
cont_regressivo_1 = 10

for i in nove_dig:
    result += int(i) * cont_regressivo_1
    cont_regressivo_1 -= 1

digito = (result * 10) % 11
digito = digito if digito <= 9 else 0

## ------------------------------------------------------------------------------

dez_dig = nove_dig + str(digito)
result = 0
cont_regressivo_2 = 11

for i in dez_dig:
    result += int(i) * cont_regressivo_2
    cont_regressivo_2 -= 1

digito1 = (result * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

novo_cpf = f'{nove_dig}{digito}{digito1}'

if cpf_usuario == novo_cpf:
    print(f'[white]{novo_cpf}[/] [bold green]é válido![/]')
else:
    print('[red]CPF não é válido[/]')
