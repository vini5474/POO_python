class ContaBancaria:
  def __init__(self, titular="desconhecido"):
    self.__saldo = 0
    self.__titular = titular

  def __validar_saldo(self, valor):
    self.__saldo >= valor

  def get__saldo(self):
    return f'Saldo da conta R${self.__saldo}' 

  def set__titular(self, nome):
    self.__titular = nome

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
      return f'{valor} adicionado ao saldo'
    else:
      return f'Digite um valor válido para o depósito'

  def sacar(self, valor):
    if self.__validar_saldo(valor):
      self.__saldo -= valor
      return f'{valor} foi sacado da conta'
    else:
      return f'Digite um valor valido para o saque'

  def exibir_detalhes(self):
    return f'titular: {self.__titular} saldo: {self.__saldo}'

  @staticmethod
  def informa_juros():
    return 0.05

conta = ContaBancaria("João Silva")
print(conta.exibir_detalhes())
conta.depositar(1000)
print(conta.exibir_detalhes())
conta.sacar(500)
print(conta.exibir_detalhes())
conta.sacar(600)
print(conta.exibir_detalhes())
print(f'Taxa de juros do banco: {ContaBancaria.informa_juros() * 100}%')