from rich import print
from rich.table import Table

print()
tabela = Table(title='[bold yellow]Preços[/]', style='bold yellow')

tabela.add_column('Produto', justify='right', style='bold blue')
tabela.add_column('Quantidade', justify='center', style='bold red')
tabela.add_column('Preço', justify='center')

tabela.add_row('Biscoito treloso', '5', 'R$ 2,50')
tabela.add_row('Pipoca', '8', 'R$ 1,50')
tabela.add_row('Sorvete', '12', 'R$ 3,00')

print(tabela)