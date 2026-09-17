valor = int(input('Digite o valor que quer sacar: R$'))
total = valor
cedula = 200
total_ced = 0

while True:
    if total >= cedula:
        total -= cedula
        total_ced += 1

    else:
        if total_ced > 0:
            print(f'Total de {total_ced} de R${cedula}')
        if cedula == 200:
            cedula = 100

        elif cedula == 100:
            cedula = 50

        elif cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 5


        elif cedula == 5:
            cedula = 1

        total_ced = 0
        if total == 0:
            break