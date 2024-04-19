#Cauê Justen Garbi

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    @abstractmethod
    def bonificacao(self):
        pass
    
    def get_nome(self):
        return self.nome
    
    def get_salario(self):
        return self.salario
    
    def bonificacao(self):
        return 0  # Implementação padrão para a classe abstrata Funcionario

    def __str__(self):
        return f"Nome: {self.nome}, Salário: R$ {self.salario:.2f}, Bonificação: R$ {self.bonificacao():.2f}"

class Diretor(Funcionario):
    def __init__(self, nome, salario, departamento="Diretoria"):
        super().__init__(nome, salario)
        self.departamento = departamento
    
    def bonificacao(self):
        return self.salario * 0.115
    
    def get_departamento(self):
        return self.departamento
    
    def __str__(self):
        return f"Nome: {self.nome}, Salário: R$ {self.salario:.2f}, Bonificação: R$ {self.bonificacao():.2f}, Departamento: {self.departamento}"

class Gerente(Funcionario):
    def __init__(self, nome, salario, qtd_funcionarios=0):
        super().__init__(nome, salario)
        self.qtd_funcionarios = qtd_funcionarios
    
    def bonificacao(self):
        return self.salario * 0.057
    
    def set_qtd_funcionarios(self, qtd):
        self.qtd_funcionarios = qtd
    
    def __str__(self):
        return f"Nome: {self.nome}, Salário: R$ {self.salario:.2f}, Bonificação: R$ {self.bonificacao():.2f}, Quantidade de Funcionários: {self.qtd_funcionarios}"

if __name__ == "__main__":
    # Criando objetos
    funcionario = Funcionario("João", 5000.0)
    diretor = Diretor("Carlos", 10000.0)
    gerente = Gerente("Maria", 7000.0)
    
    # Testando métodos
    print(funcionario)
    print(diretor)
    print(gerente)
