from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def mensagem(self):
        return (f"Olá, me chamo [green]{self.nome}[/]:smiling_face_with_sunglasses: e "
                f"sou do {self.setor}, trabalho como {self.cargo}")

func1 = Funcionario('Edson', 'Financeiro', 'Analista')
print(func1.mensagem())

func2 = Funcionario('Maria', 'RH', 'Coordenadora')
print(func2.mensagem())