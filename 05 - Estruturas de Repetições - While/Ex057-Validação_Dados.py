sx = str(input("Qual é o seu sexo? [M/F] ")).lower().strip()[0]

while sx not in "mf":
    sx = str(input("\033[31mSexo inválido\033[m, digite um valor entre as opções: ")).lower().strip()[0]

print(f'Sexo {sx} registrado com sucesso')