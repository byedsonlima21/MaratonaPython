hight = float(input('Qual é a sua altura? (m) R: '))
weight = float(input('Qual é a seu peso? (kg) R: '))
imc = weight / (hight**2)
if imc < 18.5:
    print('Você apresenta sinais de magreza.')
elif imc >= 18.5 and imc < 25:
    print('Você está normal.')
elif imc >= 25 and imc < 30:
    print('Você apresenta sinais de sobrepeso.')
elif imc >= 30 and imc < 35:
    print('Você apresenta sinais de obesidade 1.')
elif imc >= 35 and imc < 40:
    print('Você apresenta sinais de obesidade 2.')
elif imc > 50:
    print('Você apresenta sinais de obsedidade 3.')