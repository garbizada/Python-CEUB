# class Gerente:
# class Gerente():      # Três formas equivalentes de criar a classe
class Funcionario(object):
    def __init__(self, cpf, nome, salario=0.0):  # Construtor com default
        self.cpf = cpf                           # Atributos de instância
        self.nome = nome
        self.salario = salario

    def get_cpf(self):                           # Consulta
        return self.cpf
    
    def set_cpf(self, novo_cpf):                 # Altera na memória
        self.cpf = novo_cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_salario(self):
        return self.salario

    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def __str__(self):                 # Método mágico ou método dunder
        s = f"Nome: {self.nome}, CPF: {self.cpf}, salário: {self.salario:.2f}"
        return s   
    
    def bonificacao(self):
        bonificacao = self.salario * 10 / 100
        return bonificacao

     
class Gerente(Funcionario):
    def __init__(self, cpf, nome, salario, senha, qtd_gerencia=1):  # default
        super().__init__(cpf, nome , salario)
        self.senha = senha
        self.qtd_gerencia = qtd_gerencia


    def __str__(self):                 # Método mágico ou método dunder
        s = f"Nome: {self.nome}, CPF: {self.cpf}, salário: {self.salario:.2f}, Quantidade de Funcionarios para Gerenciar: {self.qtd_gerencia}"
        return s   


    def get_qtd_gerencia(self):
        return self.qtd_gerencia
    
    def set_qtd_gerencia(self, nova_qtd):
        self.qtd_gerencia = nova_qtd
        
    def autentica(self):          # Solução 1
        senha = input("Senha: ")  # A variável senha só vale dentro de autentica
        if senha == self.senha:   # O self.senha vale em toda a classe Gerente
            print("Acesso permitido.")
            return True
        else:
            print("Acesso negado.")
            return False


if __name__ == '__main__':
    f1 = Funcionario('123', 'Paulo', 1000.00)  # Cria o objeto, chama o construtor
    print(f'- Funcionário 1:\nNome: {f1.get_nome()}')
    print(f'CPF: {f1.get_cpf()}')              # Consulta
    print('Salário:', f1.get_salario())
    f1.set_nome('Vinícius')                    # Altera
    print(f'Nome alterado: {f1.get_nome()}')
    f2 = Funcionario('12345', 'Ana')   # Cria o objeto f2, chama o construtor
    print(f2)                          # print(f1.__str__())   # Teste
    print(f'- Funcionário 2:\nNome: {f2.get_nome()}')
    print(f'CPF: {f2.get_cpf()}')
    print('Salário:', f2.get_salario())
    f2.set_nome('Emily')
    print(f'Nome alterado: {f2.get_nome()}')

    g1 = Gerente('234', 'Paula', 3000.0, 's1', 5)  # g1, objeto da classe Gerente
    print(f'- Gerente 1:\nCPF: {g1.get_cpf()}')
    print('Nome:', g1.get_nome())
    print('Salário:', g1.get_salario())
    print('Qtd. funcionários:', g1.get_qtd_gerencia())
    g1.set_nome('Alice')
    print(f'Nome alterado: {g1.get_nome()}')
    print(g1.autentica())    # Linhas equivalentes
    
    g2 = Gerente('34', 'Paulo', 5000.0, 's2', 3)
    print(g2.__str__())      # print(g2), conseguiu usando o __str__?
    print('- Gerente 2:\nCPF:', g2.get_cpf())
    print('Nome:', g2.get_nome())
    print('Salário:', g2.get_salario())
    print('Qtd. funcionários:', g2.get_qtd_gerencia())

    print("A bonificação que o Funcionario 1 vai receber é: ",f1.bonificacao())
    print("A bonificação que o gerente 1 vai receber é de: ",g1.bonificacao())


    print(g1.__str__())

    print(g1.vars())