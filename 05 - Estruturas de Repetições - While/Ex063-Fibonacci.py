#0- 1 - 1 - 2
#t1 t2 t3  t4

a = int(input('Digite quantos termos quer ver? '))
t1 = 0
t2 = 1
c = 1

while c <= a:
    print(t1, end=' -> ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1

print('FIM')