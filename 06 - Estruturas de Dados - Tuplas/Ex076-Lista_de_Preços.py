produtos = ('Arroz (5kg)', 25.90,
            'Feijão Preto (1kg)', 8.50,
            'Óleo de Soja', 6.30,
            'Café Torrado'' (500g)', 18.75,
            'Açúcar Refinado (1kg)', 4.20,
            'Leite Integral (1L)', 5.49,
            'Manteiga (200g)', 12.99,
            'Pão Francês (kg)', 16.80,
            'Macarrão Espaguete', 3.65,
            'Carne Moída (1kg)', 32.10)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30} R$', end='')
    else:
        print(f'{produtos[pos]:>6.2f}')