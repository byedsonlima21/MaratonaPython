# Declaração de classe
class MinhaClasse:
    def __init__(self, nome, idade):     #Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhoto e tem {self.idade} anos"

# Declaração de objetos
p1 = MinhaClasse('Edson', 22)
p1.aniversario()

p2 = MinhaClasse('Adylla', 23)
print(f'{p1.mensagem()} e {p2.mensagem()}')
