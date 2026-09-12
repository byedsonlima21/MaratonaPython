a1 = int(input("Qual é o primeiro termo da progressão: "))
n = int(input('Até qual termo você deseja ver? '))
r = int(input("Qual é a razão? "))
fim = a1 + (n * r)

for c in range(a1, fim, r):
    print(f'{c}', end= ' => ')

print("Acabou!")