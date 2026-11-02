from rich import print
from rich.panel import Panel

caixa = Panel('[bold white]Caixa de Exemplos[/]:+1:', title='Exemplos', style='bold red', subtitle="Thank you", width=40)

print(caixa)