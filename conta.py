class Conta: 
    def __init__(self, numero, titular, senha, saldo_inicial=0, limite=10000):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo_inicial
        self.limite = limite

    def senha_correta(self, senha_digitada):
        #"""Agora recebe a senha por parâmetro e apenas retorna True ou False."""
        return senha_digitada == self.senha

    def depositar(self, valor):
        #"""Retorna uma string com o resultado para o Bot exibir."""
        if valor > 0:
            self.saldo += valor
            return f'✅ Depósito de R$ {valor:.2f} realizado! Novo saldo: R$ {self.saldo:.2f}.'
        return '❌ Erro: O valor do depósito deve ser positivo.'

    def sacar(self, valor, senha_fornecida):
        #"""Lógica de saque usando parâmetros e retornos de texto."""
        if not self.senha_correta(senha_fornecida):
            return "⚠️ Senha incorreta! Acesso negado."

        saldo_disponivel = self.saldo + self.limite 
        if saldo_disponivel >= valor: 
            self.saldo -= valor
            return f'✅ Saque de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}.'
        else: 
            return f'❌ Saldo insuficiente. Disponível: R$ {saldo_disponivel:.2f}.'

    def exibir_saldo(self, senha_fornecida):
        #"""Retorna o saldo formatado se a senha estiver correta."""
        if not self.senha_correta(senha_fornecida):
            return "⚠️ Senha incorreta! Acesso negado."
            
        extrato = (
            f"```\n"
            f"{'='*20}\n"
            f" EXTRATO BANCÁRIO\n"
            f"{'='*20}\n"
            f"Titular: {self.titular}\n"
            f"Saldo: R$ {self.saldo:.2f}\n"
            f"Limite: R$ {self.limite:.2f}\n"
            f"Total: R$ {(self.saldo + self.limite):.2f}\n"
            f"{'='*20}\n"
            f"```"
        )
        return extrato