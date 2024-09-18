# Crie um programa de locação de veículo, que receba o cadastro de um usuário para que ele possa escolher entre 5 veículos previamente cadastrados no sistema, e no final o programa exibe os dados do cliente e do carro que ele decidiu alugar.

class Veiculo:
    def __init__(self, marca, cor, preco):
        self.__marca = marca
        self.__cor = cor
        self.__preco = preco
        self.cliente = []

    @property
    def marca(self):
        return self.__marca
    @property
    def cor(self):
        return self.__cor
    @property
    def preco(self):
        return self.__preco

    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
    @preco.setter
    def preco(self, preco):
        self.__preco = preco
    
    # Método de acesso
    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)
    def listar_curso(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome)
        return lista

class Cliente:
    def __init__(self, nome, cpf,):
        self.__nome = nome
        self.__cpf = cpf
        
        self.veiculos = []


    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def turno(self):
        return self.__turno
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    # Método de ação
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            aluno.inscrever_curso(self)
    
    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome)
        return lista
    