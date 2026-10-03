from datetime import date

hoje = date.today().year

func = dict()

func['Nome'] = str(input("Nome: ")).title()
func['Nasc'] = int(input("Ano de Nascimento: "))
func['Cpts'] = int(input("N° da Carteira de Trabalho (0 se não tiver): "))

if func['Cpts'] == 0:
    print(f'{func['nome']} não possui Carteira de Trabalho')
else:
    func['Cpts'] = int(func['Cpts'])
    func['Admissao'] = int(input('Ano de Admissão: '))
    func['Salario'] = int(input('Salário: '))
    func['Aposentadoria'] = func['Nasc'] + 65

for k, v in func.items():
    print(f'{k} = {v}')

    # ou


print(f'\n{func["Nome"]} nasceu em {func["Nasc"]} e tem {hoje - func["Nasc"]} anos.')
print(f'{func['Nome']} vai se aposentar em {func['Aposentadoria']} com {(func['Nasc'] + 65) - func['Nasc']} anos')