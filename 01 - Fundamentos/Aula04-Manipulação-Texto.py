from os.path import join

frase = ('Curso em Video - Python')

print(len(frase))
print(frase.split())  # separa as palavras em diferentes famílias de micro-memórias
print(frase.strip())  # remove todos os espaços inúteis, os entre palavras e letras continuam.
print(frase.lower())
print(frase.upper())
print(frase.title())
print(frase.capitalize())
print(frase.upper().split())
print(frase.count('o'))
print(frase.replace('Python', 'Android'))
