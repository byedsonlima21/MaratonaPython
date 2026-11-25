def soma(a, b, *args) -> int:
    return a + b + sum(args)


soma1 = soma(2, 3)
print(f'soma 1 = {soma1}')

soma2 = soma(2, 3, 1, 1, 2)
print(f'soma 2 = {soma2}')

