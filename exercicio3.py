class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def __str__(self):
        return f"Nome do aluno: {self.nome}, Idade: {self.idade}, Nota: {self.nota}"

    def verifica_nota(self):
        if self.nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"


class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar(self, aluno):
        self.alunos.append(aluno)

    def remover(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                self.alunos.remove(aluno)
                break

    def listar(self):
        for aluno in self.alunos:
            print(aluno)

    def aprovacao(self):
        for aluno in self.alunos:
            if aluno.verifica_nota() == "Aprovado":
                print(aluno)

    def media(self):
        total = sum([aluno.nota for aluno in self.alunos])
        return total / len(self.alunos) if self.alunos else 0


# Exemplo de uso:
aluno1 = Aluno("Pedro", 16, 9)
aluno2 = Aluno("Maria", 17, 5)
aluno3 = Aluno("João", 15, 7)

# Criando a turma
turma = Turma()
turma.adicionar(aluno1)
turma.adicionar(aluno2)
turma.adicionar(aluno3)

# Listando todos os alunos
print("Todos os alunos:")
turma.listar()

# Listando alunos aprovados
print("\nAlunos aprovados:")
turma.aprovacao()

# Média das notas
print(f"\nMédia das notas: {turma.media():.2f}")