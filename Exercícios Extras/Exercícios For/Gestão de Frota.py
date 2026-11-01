lst_caminhao = []
lst_manutencoes = []
manutencoes = dict()
caminhao = dict()

qnt = int(input('Quantos caminhões que vai cadastrar? '))

for i in range(qnt):
    caminhao.clear()
    caminhao['Modelo'] = input('Modelo do caminhão: ')
    caminhao['Ano'] = int(input('Ano: '))
    caminhao['Manuntenções'] = int(input('Quantas manuntenções teve o veículo? '))

    lst_caminhao.append(caminhao.copy())

print(lst_caminhao)