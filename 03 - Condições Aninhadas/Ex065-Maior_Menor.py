x = []

while True:
    a = int(input("Digite um número: "))
    x.append(a)
    text = str(input("Deseja continuar? [S/N] : ")).upper().strip()[0]

    while text not in ('S', 'N'):
        print("Resposta inválida! Por favor, digite apenas S para Sim ou N para Não.")
        text = input("Deseja continuar? [S/N]: ").strip().upper()

    if text == 'N':
        break

print(f"Você digitou {len(x)} números e a média é {sum(x)/len(x):.2f}!")
print(f'E o valor máximo é {max(x)} e O mínimo {min(x)}')