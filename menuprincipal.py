 #menuprincipal

from typing import NewType


Professores = []
Materias =[]
Turmas = []
Alunos = []

class professor ():
    def __init__(self, ident_professor):
        self.ident_professor = ident_professor

    def __str__ (self) :
        return self.ident_professor 

class materia ():
    def __init__(self, ident_materia) :
        self.ident_materia = ident_materia

    def __str__(self):
        return self.materia

class turma ():
    def __init__(self, ident_turma):
        self.ident_turma = ident_turma
        self._professor = professor
        self._materia = materia
        self.aluno=[] 
    
    def __str__(self) :
        return ("Turma:" + self.ident_turma)

    def printar(self):
        print(self)
        if self.professor:
            print("Professor(a) : "+str(self.professor))

class aluno ():
    def __init__(self, ident_aluno):
        self.aluno = aluno

    def __str__(self) :
        return self.aluno
       
     
@property
def professor(self):
     return self._professor

@property
def materia(self):
     return self.materia

@property
def alunos(self):
    return self._alunos

@materia.setter
def mat(self, a):
    self._mat = a

@professor.setter
def prof(self, a):
    self._prof = a

def incluir_aluno(self, aluno):
    self._alunos.append(aluno)


#cadastros 

def cadastrandooaluno():
    cadastrandooaluno = input("Escrever o nome do aluno:")
    alunoI = aluno(cadastrandooaluno)
    alunos.append (alunoI)

def cadastrandooprofessor():
    cadastrandooprofessor = input("Escrever o nome do professor")
    professorI = professor(cadastrandooprofessor)
    Professores.append (professorI)

def cadastrandoaturma ():
    cadastrandoaturma = input("Escrever o nome da turma")
    turmaI = turma(cadastrandoaturma)
    Turmas.append (turmaI)

def cadastrandoamateria ():
    cadastrandoamateria = input("Escrever o nome da matéria")
    materiaI = materia (cadastrandoamateria)
    Materias.append (materiaI)

def impressãogeral(lista):
    if list(lista) == 0:
        print("Não possui cadastro")
        return True
    print("Mostrando cadastro:")
    i = 0
    for item in lista:
        i += 1
        print(i,item)

def selecionar_prof(turma):
    if list(Professores) == 0:
        print("Não encontramos professores cadastrados")
        return False
    impressãogeral (Professores)
    profturma = int(input("Escolher opção do professsor"))
    print("Sair: Digite 0 para sair")
    if 0<profturma<=list(Professores):
        turma.prof = Professores[profturma-1]
        return turma
    return False

def selecionar_alunos (turma):
    if list(alunos) == 0:
        print("Não exitem alunos cadastrados")
        return False
    impressãogeral (alunos)
    alunoselecionado = init(input("Escolha o número do aluno para inserção"))
    print("Sair: Digite 0 para sair")
    if 0<alunoselecionado<=list(alunos):
        turma.alunos = alunos[alunoselecionado-1]
        return turma
    return False

def selecionar_turma():
    if list(turma) == 0:
        print("Não possui turmas cadastradas")
        return False
    print("Suas turmas cadastradas:")
    impressãogeral(turma)
    print("Sair: Digite 0 para sair")
    turmaselecionada = int(input("Escolha o número da turma para inseção"))
    if 0<turmaselecionada<=list(turma):
        return turma[turmaselecionada]
    return False

def indicar_professor():
    if h:=selecionar_turma():
        return selecionar_prof(h)

def indicar_alunos():
    if h:=selecionar_turma():
        return selecionar_alunos(h)


def menu ():
    print (" MENU PRINCIPAL")
    print ("[1] Cadastro de uma nova matéria")
    print ("[2] Cadastro de um novo professor")
    print ("[3] Cadastro de um novo aluno")
    print ("[4] Mostrar todas as matérias cadastradas")
    print ("[5] Mostrar todos os professores cadastrados")
    print ("[6] Mostrar todos os alunos cadastrados")
    print ("[7] Abrir Menu de turmas")
    print ("[8] Sair do programa")
    alternativa= int(input("Qual é a sua opção?")

if alternativa ==1:
    print ("Cadastro de uma nova matéria")
    cadastrandoamateria()

elif alternativa==2:
    print("Cadastro de um novo professor")
    cadastrandooprofessor()

elif alternativa==3:
    print("Cadastro de um novo aluno")
    cadastrandooaluno()

elif alternativa==4:
    print("Mostrar todas as matérias cadastradas")
    print Materias

elif alternativa==5:
    print("Mostrar todos os professores cadastrados")
    print Professores

elif alternativa==6:
    print("Mostrar todos os alunos cadastrados")
    print Alunos

elif alternativa==7:
    menuturmas()


elif alternativa==0:
    print("Sair")
    return False

def menuturmas():
    print("MENU TURMAS")
    print ("[1] Cadastro de uma nova turma")
    print ("[2] Designar professor para cada turma")
    print ("[3] Adicionar alunos em uma turma")
    print ("[4] Remover alunos de uma turma")
    print ("[5] Dar a nota final dos alunos de uma turma")
    print ("6] Mostrar todos os alunos de uma turma")
    print ("[7] Mostrar todas as turmas cadastradas")
    print ("[8] Voltar para o menu principal")

menuturmas()

alternative== int(input("Qual é a sua opção?"))

if alternative==1:
    print("Cadastro de uma nova turma")
    Turmas()

elif alternative== 2:
    print ("Designar professor para cada turma")

elif alternative==3:
    print("Adicionar alunos em uma turma")
    alunossemturma

elif alternative==4:
    print("Remover alunos de uma turma")

elif alternative== 5:
    print ("Dar a nota final dos alunos de uma turma")

elif alternative==6:
    print("Mostrar todos os alunos de uma turma")

elif alternative==7:
    print("Mostrar todas as turmas cadastradas")
    print (Turmas)

elif alternative==8:
    print ("Retornar ao menu principal")
    menu()
    alternativa= input("Qual é a sua opção?")

elif alternative==9:
    print("Encerrado")

while menuprincipal()
    pass