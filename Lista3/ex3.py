class Curso(object):
    alunos = []
   
    def __init__(self, carga_horaria, professor,nome_curso  = "COMP"):
        self.carga_horaria = carga_horaria
        self.professor = professor
        self.nome_curso = nome_curso
        
    def matricula(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def imprime_alunos(self):
        for aluno in self.alunos:
            print(aluno)
            
    def imprime_professor(self):
        print(self.professor)   


class Aluno(Curso):
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso 
    
    def matricula (self):
        super().matricula(self.nome)
    
    def isMatriculado(self):
        if self.nome in  super().alunos:
            print("{} estah matriculado em {}".format(self.nome, self.curso))
        else: print("{} nao estah matriculado em {}".format(self.nome, self.curso))
        
        
ariel = Aluno("Ariel", 23, "COMP")
ariel.isMatriculado()
ariel.matricula()
ariel.isMatriculado()
print(Curso.alunos)
gandour = Aluno("Gandour", 20, "COMP")
gandour.isMatriculado()
gandour.matricula()
gandour.isMatriculado()
print(Curso.alunos)