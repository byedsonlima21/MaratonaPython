class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. SALDO: R${self.saldo:.2f}')

    def __str__(self):
        return f"A conta \033[32m{self.id}\033[m é do(a) {self.titular} e tem {self.saldo:.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${self.saldo:.2f} feito com sucesso na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Saque de R${self.saldo:.2f} feito com sucesso na conta {self.id}')


c1 = ContaBancaria(1010, "Edson", 160)
c1.sacar(1100)
print(c1)