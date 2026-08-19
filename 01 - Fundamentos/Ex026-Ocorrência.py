frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A primeira vez que a letra A apareceu foi na posiçõo {frase.find("A")+1}')
print(f'A primeira vez que a letra A apareceu foi na posiçõo {frase.rfind("A")+1}')