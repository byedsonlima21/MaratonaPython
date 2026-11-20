def somar(a, b, c=None):
    if c is not None:
        print(a + b + c)
    else:
        print(a + b)

somar(2, 4)
somar(1, 3, 5)

def somar(a, b=1, c=None):
    if c is not None:
        print(a + b + c)
    else:
        print(a + b)

somar(c=7, a=4)
somar(1, 9, 5)
