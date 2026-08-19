num = int(input("Digite um número inteiro: "))
opcao = int(input("Escolha uma das bases para conversão:\n"
"[ 1 ] converter para BINÁRIO\n"
"[ 2 ] converter para OCTAL\n"
"[ 3 ] converter para HEXADECIMAL\n"))

if opcao == 1:
    print(f'O número {num} em binário é {bin(num)}.')
elif opcao == 2:
    print(f'O número {num} em octal é {oct(num)}.')
elif opcao == 3:
    print(f'O número {num} em binário é {hex(num)}.')
else:
    print('Opção inválida!')