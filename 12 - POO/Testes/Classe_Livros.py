from rich import print

class Livro:
    def __init__(self, titulo, autor, genero, quantidade=0):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

biblioteca = []

def cadastrar(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f'[green]{titulo}[/] adicionado com sucesso!')

def listar_livro():
    if not biblioteca:
        print("A biblioteca encontra-se vazia")
    for i in biblioteca:
        print(f'{i.titulo} | {i.autor} | {i.genero} | [white]{i.quantidade}[/]')

def buscar_livro(livro_busca):
    for livro in biblioteca:
        if livro.titulo.lower() == livro_busca.lower():
            print(f'[blue]TÍTULO ENCONTRADO![/]')
            print(f'Título: {livro.titulo} | Autor: {livro.autor} | Gênero: {livro.genero} | Quantidade: {livro.quantidade}')
            return
    print(f'O livro "{livro_busca}" não foi encontrado')

cadastrar("Harry Potter", 'JK Rowling', 'Ficção Infantil', 5)
cadastrar("Cartas de um diabo a seu aprendiz", "C.S. Lewis", "Conto", 1)
cadastrar("1984", "George Orwell", "Política", 3)
cadastrar("Meditações", "Marcos Aurélio", "Filosofia", 5)
print()
listar_livro()
