class Livro:
  def __init__(self, titulo, autor, ano_publicacao, status="disponível"):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
    self.status = status

  def exibir_detalhes(self):
    return f'Nome: {self.titulo}, autor: {self.autor}, ano: {self.ano_publicacao}, status: {self.status}'

  def emprestar(self):
    if self.status == "disponível":
      self.status = "emprestado"
      return f'Livro emprestado'
    else:
      return f'O livro não pode ser emprestado pois está indisponível'

  def devolver(self):
    if self.status == "emprestado":
      self.status = "disponível"
      return f'Livro devolvido'
    else:
      return f'O livro já está disponível'


livro1 = Livro("O Alquimista", "Paulo Coelho", 1988)
print(livro1.exibir_detalhes())
print(livro1.emprestar())
print(livro1.devolver())