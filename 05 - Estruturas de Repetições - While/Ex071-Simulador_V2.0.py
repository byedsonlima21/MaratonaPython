valor = int(input('Digite o valor que quer sacar: R$'))
total = valor
cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
total_ced = 0

while True:
    for cedula in cedulas:
        if total >= cedula:
            qnt_notas = total // cedula
            print(f'Total de {qnt_notas} de R${cedula}')

            total = total % cedula

        if total == 0:
            break

