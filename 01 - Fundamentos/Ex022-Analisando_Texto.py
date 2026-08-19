nome = str(input('Digite seu nome completo: ')).strip()
v1 = nome.split()

print(f'Seu nome em letras maiusculas é {nome.upper()}')
print(f'Seu nome em letras minusculas é {nome.lower()}')
print(f'Seu nome completo tem {len(nome) - nome.count(' ')} letras')
print(f'Seu nome é {v1[0]} e tem {len(v1[0])} letras')