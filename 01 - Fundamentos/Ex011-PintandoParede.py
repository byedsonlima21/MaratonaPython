largura = float(input('Qual a largura da parede? '))
tamanho = float(input('Qual a tamanho da parede? '))

print(f'A área da parede é {largura * tamanho}m².\nJá que com 1L você pinta 2m², então você vai precisar de {(largura * tamanho) / 2:.2f}l')