func = dict()


func['nome'] = str(input("Nome: ")).title()
func['nasc'] = int(input("Ano de Nascimento: "))
func['cpts'] = int(input("N° da carteira de trabalho (0 se não tiver: "))
cpts = str(input("Carteira de trabalho (0 se não tiver): "))

if cpts == '0':
    print(f'O {func["nome"]} nasceu em {func["nasc"]}.')
else:
    func['cpts'] = int(cpts)

print(func)
