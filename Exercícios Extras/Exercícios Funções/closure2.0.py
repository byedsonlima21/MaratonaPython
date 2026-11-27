def multiplicador(base):
    def multiplicar(numero):
        return numero * base
    return multiplicar


dobrar = multiplicador(2)
triplicar = multiplicador(3)

print(dobrar(10))
print(triplicar(5))