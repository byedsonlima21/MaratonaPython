import math
ang = float(input('Digite um angulo qualquer: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
hip = math.tan(math.radians(ang))

print(f'O angulo tem {ang}° e tem o seno de valor {sen:.2f}!')
print(f'O angulo tem {ang}° e tem o cosseno de valor {cos:.2f}!')
print(f'O angulo tem {ang}° e tem a tangente de valor {hip:.2f}!')
