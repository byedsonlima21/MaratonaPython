# Declaração de classe
class MinhaClasse:
    def __init__(self):     #Método Construtor
        # Atributos de Instância
        self.nome = 'Edson'
        self.idade = 22

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhoto e tem {self.idade} anos"

# Declaração de objetos
obg = MinhaClasse()
obg.aniversario()
obg.nome = 'João'
print(obg.mensagem())