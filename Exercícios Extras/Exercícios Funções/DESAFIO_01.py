"""Desafio 1 – Desconto de Loja:
Crie uma fábrica de descontos que receba a porcentagem
e retorne uma função que receba o preço do produto,
devolvendo o valor final já descontado. Teste criando
um desconto comum (10%) e um VIP (25%) aplicados a um item de R$ 200."""

def valor_desconto(valor):
    def preco_produto(preco):
        return float((preco - (preco * (valor / 100))))
    return preco_produto

p1 = valor_desconto(10)
produto2 = valor_desconto(11.5)

print(f'R$ {p1(100):.2f}')
print(f'R$ {produto2(250):.2f}')
