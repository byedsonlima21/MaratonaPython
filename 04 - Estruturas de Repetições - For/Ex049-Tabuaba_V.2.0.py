from time import sleep

a = int(input("Digite o número que você quer calcular: "))

for i in range(1,11):
    print(f'{a} x {i:2} = {a * i:2}')
    sleep(0.5)