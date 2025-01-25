from abc import ABC, abstractmethod

class ContaBancaria(ABC):
  def __init__(self, titular):
    self.titular = titular
    self.saldo = 0
    
  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      return f'Valor adicionado'
    else:
      return f'Digite um valor válido para o depósito'

  def sacar(self, valor):
    if valor <= self.saldo:
      self.saldo -= valor
      return f'Valor sacado'
    else:
      return f'Digite um número válido para o saque'

  def exibir_detalhes(self):
    return f'Titular: {self.titular} saldo: {self.saldo}'

  @abstractmethod
  def calcula_juros(self):
    pass

class ContaCorrente(ContaBancaria):
  def __init__(self, titular):
    super().__init__(titular)
    self.manutencao_juro = 10

  def calcula_juros(self):
    juros = self.saldo * 0.01
    self.saldo += juros
    return f'Juros de R${juros} aplicados'

  def descontar_manutencao_juro(self):
    self.saldo -= self.manutencao_juro
    return f'Taxa de manutenção de R${self.manutencao_juro} aplicada'


class ContaPoupanca(ContaBancaria):
  def __init__(self, titular):
    super().__init__(titular)

  def calcula_juros(self):
    juros = self.saldo * 0.05
    self.saldo += juros
    return f'Juros de R${juros} aplicados'

conta_corrente = ContaCorrente('Carlos Souza')
print(conta_corrente.depositar(1000))
print(conta_corrente.calcula_juros()) 
print(conta_corrente.descontar_manutencao_juro()) 
print(conta_corrente.exibir_detalhes())

conta_poupanca = ContaPoupanca('Ana Silva')
print(conta_poupanca.depositar(2000))
print(conta_poupanca.calcula_juros())
print(conta_poupanca.exibir_detalhes())