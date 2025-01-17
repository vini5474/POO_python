class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, deposito):
        if not isinstance(deposito, (int, float)) or deposito <= 0:
            return "Digite um valor válido para o depósito (número positivo)"
        else:
            self.saldo += deposito
            return f"Valor {deposito} adicionado ao saldo"

    def sacar(self, saque):
        if not isinstance(saque, (int, float)) or saque <= 0:
            return "Digite um valor válido para o saque (número positivo)"
        if saque > self.saldo:
            return "Valor insuficiente para saque"
        else:
            self.saldo -= saque
            return f"Saque de {saque} bem sucedido"

    def consultar(self):
        return f"Seu saldo é de {self.saldo:.2f}"
    
    def __str__(self):
        return f"Nome do titular: {self.titular}, saldo atual: {self.saldo:.2f}"
    
# Criando uma conta bancária para o titular João Silva
conta1 = ContaBancaria("João Silva")

# Exibindo o saldo inicial
print(conta1)

# Depositando dinheiro
print(conta1.depositar(1000))  # Depósito de 1000
print(conta1)  # Exibe o saldo após o depósito

# Tentando sacar um valor
print(conta1.sacar(500))  # Saque de 500
print(conta1)  # Exibe o saldo após o saque

# Tentando sacar um valor maior que o saldo
print(conta1.sacar(600))  # Tentativa de saque de 600, que é maior que o saldo
