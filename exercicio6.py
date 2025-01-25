class Carro:
  def __init__(self, modelo, cor, ano, estado="desligado"):
    self.modelo = modelo
    self.cor = cor
    self.ano = ano
    self.estado = estado

  def exibir_detalhes(self):
    return f'Modelo: {self.modelo}, cor: {self.cor}, ano: {self.ano} estado: {self.estado}'

  def ligar(self):
    if self.estado == "desligado":
      self.estado = "ligado" 
      return f'{self.modelo} está {self.estado}'
    else:
      return f'O {self.modelo} já está {self.estado}'

  def desligar(self):
    if self.estado == "ligado":
      self.estado = "desligado" 
      return f'{self.modelo} está {self.estado}'
    else:
      return f'O {self.modelo} já está {self.estado}'

  def verifica_estado(self):
    return f'O {self.modelo} está {self.estado}'

  def acelerar(self):
    if self.estado == "ligado":
      return f'O {self.modelo} está acelerando'
    else:
      return f'O {self.modelo} não está ligado, não pode acelerar'

carro1 = Carro("Fusca", "azul", 1978)
print(carro1.exibir_detalhes())
print(carro1.ligar())
print(carro1.desligar())
print(carro1.verifica_estado())
print(carro1.acelerar())
print(carro1.ligar())
print(carro1.acelerar())