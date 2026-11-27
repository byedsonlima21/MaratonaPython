def criar_saudacao(saudacao):
    def dizer_nome(nome):
        return f'{saudacao}, {nome}!'
    return dizer_nome


a = criar_saudacao("Bom dia")
b = criar_saudacao("Boa noite")
c = criar_saudacao("Oi")

print(a("Edson"))
print(b("Maria"))
