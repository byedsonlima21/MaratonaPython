sx = str(input("Qual é o seu sexo? [M/F] ")).lower().strip()[0]

while sx not in "mf":
    sx = str(input("Sexo inválido, digite um valor entre as opções: ")).lower().strip()[0]

print(f'Sexo {sx} registrado com sucesso')