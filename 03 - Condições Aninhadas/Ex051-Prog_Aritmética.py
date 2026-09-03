a1 = int(input("Qual é o primeiro termo da progressão: "))
r = int(input("Qual é a razão? "))

for c in range(1, 10):
    print(f'{a1 + ( c - 1) * r}', end= ' => ')

print("Acabou!")