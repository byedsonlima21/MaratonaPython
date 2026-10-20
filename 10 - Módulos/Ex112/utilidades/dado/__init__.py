
def leia_dinheiro(v):

    while True:
        entrada = str(input(v)).replace('.', ',').strip()
        if entrada.isalpha() or entrada == '':
            print(f"\033[0;31mERRO! \'{entrada}\' não é válido.\033[m")
        else:
            return float(entrada)