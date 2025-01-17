class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"Livro: {self.titulo}, autor: {self.autor}, ano: {self.ano}"

    def chamar_livro(self):
        print("O livro é: ", self.titulo)

    def chamar_autor(self):
         print("O autor é: ", self.autor)

    def chamar_ano(self):
         print("Foi lançado no de: ", self.ano)


livro1 = Livro("principe", "gabriel", 1980)
print(livro1)