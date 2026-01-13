class Conta: 
    def __init__(self, numero, titular, senha, saldo_inicial=0, limite=10000):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo_inicial
        self.limite = limite

    def senha_correta(self):
        """Método auxiliar para validar a senha em qualquer operação."""
        senha_digitada = input('Por favor, digite sua senha: ')
        if senha_digitada == self.senha: 
            return True
        else: 
            print("Senha incorreta! Acesso negado.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso! Novo saldo: R$ {self.saldo:.2f}.')
        else: 
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        # Agora usamos o validador que você criou!
        if self.senha_correta():
            saldo_disponivel = self.saldo + self.limite 

            if saldo_disponivel >= valor: 
                self.saldo -= valor
                print(f'Saque de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}.')
                return True
            else: 
                print(f'SALDO INSUFICIENTE. Disponível: R$ {saldo_disponivel:.2f}.')
                return False
        return False 

    def exibir_saldo(self):
        # Protegendo o extrato com senha também
        if self.senha_correta():
            print("\n" + "="*30)
            print(f"EXTRATO BANCÁRIO")
            print(f"Titular: {self.titular}")
            print(f"Saldo em Conta: R$ {self.saldo:.2f}")
            print(f"Limite de Crédito: R$ {self.limite:.2f}")
            print(f"Total Disponível: R$ {(self.saldo + self.limite):.2f}")
            print("="*30)