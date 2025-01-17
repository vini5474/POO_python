class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        return f"Título: {self.titulo}, autor: {self.autor}, ano: {self.ano}, disponibilidade: {self.disponivel}"
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f"O livro '{self.titulo}' foi emprestado."
        else:
            return f"O livro '{self.titulo}' não está disponível."
        
    def devolver(self):
        self.disponivel = True
        return f"O livro '{self.titulo}' foi devolvido."

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def remover(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                return f"O livro '{titulo}' foi removido da biblioteca."
        return f"O livro '{titulo}' não foi encontrado na biblioteca."
    
    def listar_disponivel(self):
        livros_disponiveis = [livro for livro in self.livros if livro.disponivel]
        if not livros_disponiveis:
            return "Não há livros disponíveis para empréstimo."
        else:
            return "\n".join(str(livro) for livro in livros_disponiveis)
        
    def buscar_livros(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return str(livro)
        return f"O livro '{titulo}' não foi encontrado na biblioteca."

# Exemplo de uso:

# Criando livros
livro1 = Livro("O Príncipe", "Maquiavel", 1532)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1900)
livro3 = Livro("1984", "George Orwell", 1949)

# Criando a biblioteca e adicionando livros
biblioteca = Biblioteca()
biblioteca.adicionar(livro1)
biblioteca.adicionar(livro2)
biblioteca.adicionar(livro3)

# Listando livros disponíveis
print("Livros disponíveis para empréstimo:")
print(biblioteca.listar_disponivel())

# Emprestando um livro
print("\nEmprestando 'Dom Casmurro':")
print(livro2.emprestar())

# Tentando emprestar o mesmo livro novamente
print("\nTentando emprestar 'Dom Casmurro' novamente:")
print(livro2.emprestar())

# Listando livros disponíveis após empréstimo
print("\nLivros disponíveis após empréstimo:")
print(biblioteca.listar_disponivel())

# Devolvendo um livro
print("\nDevolvendo 'Dom Casmurro':")
print(livro2.devolver())

# Listando livros disponíveis após devolução
print("\nLivros disponíveis após devolução:")
print(biblioteca.listar_disponivel())

# Removendo um livro
print("\nRemovendo '1984':")
print(biblioteca.remover("1984"))

# Buscando um livro
print("\nBuscando 'O Príncipe':")
print(biblioteca.buscar_livros("O Príncipe"))

# Tentando buscar um livro não existente
print("\nBuscando 'Harry Potter':")
print(biblioteca.buscar_livros("Harry Potter"))